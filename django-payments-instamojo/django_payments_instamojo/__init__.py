import json
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from payments.core import BasicProvider
from instamojo_wrapper import Instamojo
from payments import RedirectNeeded, PaymentError, PaymentStatus


class InstamojoProvider(BasicProvider):
    """
    Instamojo Provider for django_payments
    """

    def __init__(self, *args, **kwargs):
        self.api_key = kwargs.pop('api_key')
        self.auth_token = kwargs.pop('auth_token')
        self.base_url = kwargs.pop('base_url')
        self.endpoint = kwargs.pop(
            'endpoint', 'https://test.instamojo.com/api/1.1/')
        super(InstamojoProvider, self).__init__(*args, **kwargs)

    def get_form(self, payment, data=None):
        if not payment.id:
            payment.save()
        api = Instamojo(api_key=self.api_key, auth_token=self.auth_token, endpoint=self.endpoint)
        payment_request = api.payment_request_create(
            amount=payment.total,
            purpose=payment.description,
            send_email=False,
            redirect_url=self.base_url + payment.get_process_url(),
        )
        try:
            raise RedirectNeeded(payment_request['payment_request']['longurl'])
        except KeyError:
            raise PaymentError(
                'Error in processing payment. Contact developer. Output: %s' % (payment_request))

    def process_data(self, payment, request):
        if 'payment_request_id' not in request.GET:
            return HttpResponseForbidden('FAILED')
        payment_request_id = request.GET.get('payment_request_id')
        api = Instamojo(api_key=self.api_key, auth_token=self.auth_token, endpoint=self.endpoint)
        status_request = api.payment_request_status(payment_request_id)
        try:
            payment_req = status_request['payment_request']['payments'][0]
            status = payment_req['status']
            if status == 'Credit':
                payment.change_status(PaymentStatus.CONFIRMED)
                payment.captured_amount = payment.total
                payment.extra_data = json.dumps(status_request)
                first_name, last_name = payment_req['buyer_name'].rsplit(' ', 1)
                payment.billing_first_name = first_name
                payment.billing_last_name = last_name
                payment.save()
            elif status == 'Failed':
                payment.change_status(PaymentStatus.REJECTED)
                return redirect(payment.get_failure_url())
        except KeyError:
            payment.change_status(PaymentStatus.REJECTED)
            return redirect(payment.get_failure_url())
        return redirect(payment.get_success_url())
