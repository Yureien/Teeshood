from django import forms
from django.db.models import Q
from django.utils.translation import npgettext, pgettext_lazy
from django_filters import (
    CharFilter, ChoiceFilter, DateFromToRangeFilter, NumberFilter,
    OrderingFilter, RangeFilter)
from payments import PaymentStatus

from ...core.filters import SortedFilterSet
from ...order import OrderStatus
from ...order.models import Order, OrderComplaint
from ..widgets import DateRangeWidget, MoneyRangeWidget

SORT_BY_FIELDS = [
    ('pk', 'pk'),
    ('payments__status', 'payment_status'),
    ('user__email', 'email'),
    ('created', 'created'),
    ('total_net', 'total')]

SORT_BY_FIELDS_LABELS = {
    'pk': pgettext_lazy('Order list sorting option', '#'),
    'payments__status': pgettext_lazy('Order list sorting option', 'payment'),
    'user__email': pgettext_lazy('Order list sorting option', 'email'),
    'created': pgettext_lazy('Order list sorting option', 'created'),
    'total_net': pgettext_lazy('Order list sorting option', 'created')}


class OrderFilter(SortedFilterSet):
    id = NumberFilter(
        label=pgettext_lazy('Order list filter label', 'ID'))
    name_or_email = CharFilter(
        label=pgettext_lazy(
            'Order list filter label', 'Customer name or email'),
        method='filter_by_order_customer')
    created = DateFromToRangeFilter(
        label=pgettext_lazy('Order list filter label', 'Placed on'),
        name='created', widget=DateRangeWidget)
    status = ChoiceFilter(
        label=pgettext_lazy(
            'Order list filter label', 'Order status'),
        choices=OrderStatus.CHOICES,
        empty_label=pgettext_lazy('Filter empty choice label', 'All'),
        widget=forms.Select)
    payment_status = ChoiceFilter(
        label=pgettext_lazy('Order list filter label', 'Payment status'),
        name='payments__status',
        choices=PaymentStatus.CHOICES,
        empty_label=pgettext_lazy('Filter empty choice label', 'All'),
        widget=forms.Select)
    total_net = RangeFilter(
        label=pgettext_lazy('Order list filter label', 'Total'),
        widget=MoneyRangeWidget)
    sort_by = OrderingFilter(
        label=pgettext_lazy('Order list filter label', 'Sort by'),
        fields=SORT_BY_FIELDS,
        field_labels=SORT_BY_FIELDS_LABELS)

    class Meta:
        model = Order
        fields = []

    def filter_by_order_customer(self, queryset, name, value):
        return queryset.filter(
            Q(user__email__icontains=value) |
            Q(user__default_billing_address__first_name__icontains=value) |
            Q(user__default_billing_address__last_name__icontains=value))

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard orders list',
            'Found %(counter)d matching order',
            'Found %(counter)d matching orders',
            number=counter) % {'counter': counter}


class ComplaintFilter(SortedFilterSet):
    id = NumberFilter(
        label=pgettext_lazy('Order list filter label', 'ID'))
    name_or_email = CharFilter(
        label=pgettext_lazy(
            'Order list filter label', 'Customer name'),
        method='filter_by_order_customer')
    created = DateFromToRangeFilter(
        label=pgettext_lazy('Order list filter label', 'Placed on'),
        name='created', widget=DateRangeWidget)

    class Meta:
        model = OrderComplaint
        fields = []

    def filter_by_order_customer(self, queryset, name, value):
        return queryset.filter(
            Q(order__user__email__icontains=value) |
            Q(order__user__default_billing_address__first_name__icontains=value) |
            Q(order__user__default_billing_address__last_name__icontains=value))

    def get_summary_message(self):
        counter = self.qs.count()
        return npgettext(
            'Number of matching records in the dashboard orders list',
            'Found %(counter)d matching order',
            'Found %(counter)d matching orders',
            number=counter) % {'counter': counter}
