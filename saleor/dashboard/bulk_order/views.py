from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, reverse
from django.template.response import TemplateResponse
from django.utils.translation import npgettext_lazy, pgettext_lazy
from django.views.decorators.http import require_POST

from . import forms
from ...core.utils import get_paginator_items
from ...discount.models import Sale
from ...core.models import BulkOrder, BulkOrderType, BulkOrderColor
from ...product.utils.availability import get_availability
from ..views import staff_member_required
from .filters import ProductFilter


@staff_member_required
@permission_required('product.view_product')
def bulk_order_list(request):
    products = BulkOrder.objects.all()
    product_filter = ProductFilter(request.GET, queryset=products)
    products = get_paginator_items(
        product_filter.qs, settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page'))
    order_type_values = BulkOrderType.objects.all()
    order_color_values = BulkOrderColor.objects.all()
    ctx = {
        'bulk_action_form': forms.ProductBulkUpdate(),
        'products': products,
        'filter_set': product_filter,
        'is_empty': not product_filter.queryset.exists(),
        'order_type_values': order_type_values,
        'order_color_values': order_color_values
    }
    return TemplateResponse(request, 'dashboard/bulk_order/list.html', ctx)


@staff_member_required
@permission_required('product.view_product')
def bulk_order_details(request, pk):
    product = get_object_or_404(BulkOrder, pk=pk)
    ctx = {
        'product': product,
    }
    return TemplateResponse(request, 'dashboard/bulk_order/detail.html', ctx)


@staff_member_required
@permission_required('product.edit_product')
def bulk_order_delete(request, pk):
    product = get_object_or_404(BulkOrder, pk=pk)
    if request.method == 'POST':
        product.delete()
        msg = pgettext_lazy(
            'Dashboard message', 'Removed order %s') % (product,)
        messages.success(request, msg)
        return redirect('dashboard:bulk-order-list')
    return TemplateResponse(
        request,
        'dashboard/bulk_order/modal/confirm_delete.html',
        {'product': product})


@staff_member_required
@permission_required('product.edit_properties')
def order_type_value_create(request):
    form = forms.OrderTypeChoiceValueForm(request.POST or None)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Added attribute\'s value')
        messages.success(request, msg)
        return redirect('dashboard:bulk-order-list')
    ctx = {'form': form}
    return TemplateResponse(
        request,
        'dashboard/bulk_order/attribute_form.html',
        ctx)


@staff_member_required
@permission_required('product.edit_properties')
def order_type_value_edit(request, value_pk):
    value = get_object_or_404(BulkOrderType, pk=value_pk)
    form = forms.OrderTypeChoiceValueForm(request.POST or None, instance=value)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Updated attribute\'s value')
        messages.success(request, msg)
        return redirect('dashboard:bulk-order-list')
    ctx = {'form': form}
    return TemplateResponse(
        request,
        'dashboard/bulk_order/attribute_form.html',
        ctx)


@staff_member_required
@permission_required('product.edit_properties')
def order_type_value_delete(request, value_pk):
    value = get_object_or_404(BulkOrderType, pk=value_pk)
    if request.method == 'POST':
        value.delete()
        msg = pgettext_lazy(
            'Dashboard message',
            'Removed attribute\'s value %s') % (value.name,)
        messages.success(request, msg)
        return redirect('dashboard:bulk-order-list')
    return TemplateResponse(
        request,
        'dashboard/bulk_order/modal/attribute_confirm_delete.html',
        {'value': value, 'action': 'type'})


@staff_member_required
@permission_required('product.edit_properties')
def order_color_value_create(request):
    form = forms.OrderColorChoiceValueForm(request.POST or None)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Added attribute\'s value')
        messages.success(request, msg)
        return redirect('dashboard:bulk-order-list')
    ctx = {'form': form}
    return TemplateResponse(
        request,
        'dashboard/bulk_order/attribute_form.html',
        ctx)


@staff_member_required
@permission_required('product.edit_properties')
def order_color_value_edit(request, value_pk):
    value = get_object_or_404(BulkOrderColor, pk=value_pk)
    form = forms.OrderColorChoiceValueForm(request.POST or None, instance=value)
    if form.is_valid():
        form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Updated attribute\'s value')
        messages.success(request, msg)
        return redirect('dashboard:bulk-order-list')
    ctx = {'form': form}
    return TemplateResponse(
        request,
        'dashboard/bulk_order/attribute_form.html',
        ctx)


@staff_member_required
@permission_required('product.edit_properties')
def order_color_value_delete(request, value_pk):
    value = get_object_or_404(BulkOrderColor, pk=value_pk)
    if request.method == 'POST':
        value.delete()
        msg = pgettext_lazy(
            'Dashboard message',
            'Removed attribute\'s value %s') % (value.name,)
        messages.success(request, msg)
        return redirect('dashboard:bulk-order-list')
    return TemplateResponse(
        request,
        'dashboard/bulk_order/modal/attribute_confirm_delete.html',
        {'value': value, 'action': 'color'})
