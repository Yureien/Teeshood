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
from ...core.models import CustomDesign
from ...product.utils.availability import get_availability
from ..views import staff_member_required
from .filters import ProductFilter


@staff_member_required
@permission_required('product.view_product')
def custom_design_list(request):
    products = CustomDesign.objects.all()
    product_filter = ProductFilter(request.GET, queryset=products)
    products = get_paginator_items(
        product_filter.qs, settings.DASHBOARD_PAGINATE_BY,
        request.GET.get('page'))
    ctx = {
        'bulk_action_form': forms.ProductBulkUpdate(),
        'products': products,
        'filter_set': product_filter,
        'is_empty': not product_filter.queryset.exists()}
    return TemplateResponse(request, 'dashboard/custom_design/list.html', ctx)


@staff_member_required
@permission_required('product.view_product')
def custom_design_details(request, pk):
    product = get_object_or_404(CustomDesign, pk=pk)
    ctx = {
        'product': product, 'uploader': product.user
    }
    return TemplateResponse(request, 'dashboard/custom_design/detail.html', ctx)


@staff_member_required
@permission_required('product.edit_product')
def custom_design_delete(request, pk):
    product = get_object_or_404(CustomDesign, pk=pk)
    if request.method == 'POST':
        product.delete()
        msg = pgettext_lazy(
            'Dashboard message', 'Removed design %s') % (product,)
        messages.success(request, msg)
        return redirect('dashboard:custom-design-list')
    return TemplateResponse(
        request,
        'dashboard/custom_design/modal/confirm_delete.html',
        {'product': product})
