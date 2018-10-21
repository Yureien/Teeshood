import json

from django.contrib import messages
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from impersonate.views import impersonate as orig_impersonate

from .forms import CustomDesignForm, BulkOrderForm
from ..account.models import User
from ..dashboard.views import staff_member_required
from ..product.utils import products_for_homepage
from ..product.utils.availability import products_with_availability
from ..seo.schema.webpage import get_webpage_schema


def home(request):
    products = products_for_homepage()[:8]
    products = list(products_with_availability(
        products, discounts=request.discounts, taxes=request.taxes,
        local_currency=request.currency))
    webpage_schema = get_webpage_schema(request)
    return TemplateResponse(
        request, 'home.html', {
            'parent': None,
            'products': products,
            'webpage_schema': json.dumps(webpage_schema)})


@staff_member_required
def styleguide(request):
    return TemplateResponse(request, 'styleguide.html')


def about(request):
    return TemplateResponse(request, 'about.html')


def contact(request):
    return TemplateResponse(request, 'contact.html')


def privacy_policy(request):
    return TemplateResponse(request, 'privacy_policy.html')


def impersonate(request, uid):
    response = orig_impersonate(request, uid)
    if request.session.modified:
        msg = pgettext_lazy(
            'Impersonation message',
            'You are now logged as {}'.format(User.objects.get(pk=uid)))
        messages.success(request, msg)
    return response


def handle_404(request, exception=None):
    return TemplateResponse(request, '404.html', status=404)


def manifest(request):
    return TemplateResponse(
        request, 'manifest.json', content_type='application/json')


@login_required
def design_upload(request):
    custom_design_form = CustomDesignForm(request.POST or None, request.FILES)
    if custom_design_form.is_valid():
        design = custom_design_form.save(commit=False)
        design.user = request.user
        design.save()
        messages.success(
            request,
            pgettext_lazy(
                'Custom Design message',
                'Sent custom design.')
        )
        return redirect('home')
    ctx = {'custom_design_form': custom_design_form}
    return TemplateResponse(request, 'design_upload.html', ctx)


@login_required
def bulk_order(request):
    bulk_order_form = BulkOrderForm(request.POST or None, request.FILES)
    if bulk_order_form.is_valid():
        design = bulk_order_form.save(commit=False)
        design.user = request.user
        design.save()
        messages.success(
            request,
            pgettext_lazy(
                'Bulk Order message',
                'Sent bulk order.')
        )
        return redirect('home')
    ctx = {'bulk_order_form': bulk_order_form}
    return TemplateResponse(request, 'bulk_order.html', ctx)
