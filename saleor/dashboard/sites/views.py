from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.utils.translation import pgettext_lazy
from django.forms import modelformset_factory

from ...site.models import (AuthorizationKey, SiteSettings, ProductCoupon,
                            ProductBanner, HallOfFame, CategoryTile, CustomerBanner)
from ..views import staff_member_required
from .forms import (AuthorizationKeyForm, SiteForm, ProductCouponForm, CustomerBannerForm,
                    SiteSettingsForm, ProductBannerForm, HallOfFameForm, CategoryTileForm)


@staff_member_required
@permission_required('site.edit_settings')
def index(request):
    site = get_current_site(request)
    settings = site.settings
    return redirect('dashboard:site-details', pk=settings.pk)


@staff_member_required
@permission_required('site.edit_settings')
def site_settings_edit(request, pk):
    site_settings = get_object_or_404(SiteSettings, pk=pk)
    site = site_settings.site
    site_settings_form = SiteSettingsForm(
        request.POST or None, instance=site_settings)
    site_form = SiteForm(request.POST or None, instance=site)

    if site_settings_form.is_valid() and site_form.is_valid():
        site = site_form.save()
        site_settings_form.instance.site = site
        site_settings = site_settings_form.save()
        messages.success(request, pgettext_lazy(
            'Dashboard message', 'Updated site settings'))
        return redirect('dashboard:site-details', pk=site_settings.id)
    ctx = {'site_settings': site_settings,
           'site_settings_form': site_settings_form,
           'site_form': site_form}
    return TemplateResponse(request, 'dashboard/sites/form.html', ctx)


@staff_member_required
@permission_required('site.edit_settings')
def product_banner_edit(request, pk):
    site_settings = get_object_or_404(SiteSettings, pk=pk)
    site = site_settings.site
    ProductBannerFormSet = modelformset_factory(
        ProductBanner, form=ProductBannerForm, extra=5,
        can_delete=True, can_order=True)
    product_banner_formset = ProductBannerFormSet(request.POST or None, request.FILES or None)

    if product_banner_formset.is_valid():
        product_banners = product_banner_formset.save(commit=False)
        for obj in product_banner_formset.deleted_objects:
            obj.delete()
        for banner in product_banners:
            banner.site_settings = site_settings
            banner.save()
        messages.success(request, pgettext_lazy(
            'Dashboard message', 'Updated banners'))
        return redirect('dashboard:site-details', pk=site_settings.id)
    ctx = {'site_settings': site_settings,
           'site': site,
           'product_banner_formset': product_banner_formset}
    return TemplateResponse(request, 'dashboard/sites/product_banner_form.html', ctx)


@staff_member_required
@permission_required('site.edit_settings')
def customer_banner_edit(request, pk):
    site_settings = get_object_or_404(SiteSettings, pk=pk)
    site = site_settings.site
    CustomerBannerFormSet = modelformset_factory(
        CustomerBanner, form=CustomerBannerForm, extra=10,
        can_delete=True, can_order=True)
    customer_banner_formset = CustomerBannerFormSet(request.POST or None, request.FILES or None)

    if customer_banner_formset.is_valid():
        customer_banners = customer_banner_formset.save(commit=False)
        for obj in customer_banner_formset.deleted_objects:
            obj.delete()
        for instance in customer_banners:
            instance.site_settings = site_settings
            instance.save()
        messages.success(request, pgettext_lazy(
            'Dashboard message', 'Updated customer banners'))
        return redirect('dashboard:site-details', pk=site_settings.id)
    ctx = {'site_settings': site_settings,
           'site': site,
           'customer_banner_formset': customer_banner_formset}
    return TemplateResponse(request, 'dashboard/sites/customer_banner_form.html', ctx)


@staff_member_required
@permission_required('site.edit_settings')
def hall_of_fame_edit(request, pk):
    site_settings = get_object_or_404(SiteSettings, pk=pk)
    site = site_settings.site
    HallOfFameFormSet = modelformset_factory(
        HallOfFame, form=HallOfFameForm, max_num=3, extra=3,
        can_delete=True, can_order=True)
    hall_of_fame_formset = HallOfFameFormSet(request.POST or None, request.FILES or None)

    if hall_of_fame_formset.is_valid():
        hall_of_fames = hall_of_fame_formset.save(commit=False)
        for obj in hall_of_fame_formset.deleted_objects:
            obj.delete()
        for instance in hall_of_fames:
            instance.site_settings = site_settings
            instance.save()
        messages.success(request, pgettext_lazy(
            'Dashboard message', 'Updated hall of fame'))
        return redirect('dashboard:site-details', pk=site_settings.id)
    ctx = {'site_settings': site_settings,
           'site': site,
           'hall_of_fame_formset': hall_of_fame_formset}
    return TemplateResponse(request, 'dashboard/sites/hall_of_fame_form.html', ctx)


@staff_member_required
@permission_required('site.edit_settings')
def product_coupon_edit(request, pk):
    site_settings = get_object_or_404(SiteSettings, pk=pk)
    site = site_settings.site
    ProductCouponFormSet = modelformset_factory(
        ProductCoupon, form=ProductCouponForm, can_delete=True, can_order=True, extra=3)
    product_coupon_formset = ProductCouponFormSet(request.POST or None, request.FILES or None)

    if product_coupon_formset.is_valid():
        product_coupons = product_coupon_formset.save(commit=False)
        for obj in product_coupon_formset.deleted_objects:
            obj.delete()
        for instance in product_coupons:
            instance.site_settings = site_settings
            instance.save()
        messages.success(request, pgettext_lazy(
            'Dashboard message', 'Updated product coupon'))
        return redirect('dashboard:site-details', pk=site_settings.id)
    ctx = {'site_settings': site_settings,
           'site': site,
           'product_coupon_formset': product_coupon_formset}
    return TemplateResponse(request, 'dashboard/sites/product_coupon_form.html', ctx)


@staff_member_required
@permission_required('site.edit_settings')
def category_tile_edit(request, pk):
    site_settings = get_object_or_404(SiteSettings, pk=pk)
    site = site_settings.site
    CategoryTileFormSet = modelformset_factory(
        CategoryTile, form=CategoryTileForm, extra=5, can_delete=True, can_order=True)
    category_tile_formset = CategoryTileFormSet(request.POST or None, request.FILES or None)

    if category_tile_formset.is_valid():
        category_tiles = category_tile_formset.save(commit=False)
        for obj in category_tile_formset.deleted_objects:
            obj.delete()
        for instance in category_tiles:
            instance.site_settings = site_settings
            instance.save()
        messages.success(request, pgettext_lazy(
            'Dashboard message', 'Updated category tiles'))
        return redirect('dashboard:site-details', pk=site_settings.id)
    ctx = {'site_settings': site_settings,
           'site': site,
           'category_tile_formset': category_tile_formset}
    return TemplateResponse(request, 'dashboard/sites/category_tile_form.html', ctx)


@staff_member_required
@permission_required('site.edit_settings')
def site_settings_details(request, pk):
    site_settings = get_object_or_404(SiteSettings, pk=pk)
    authorization_keys = AuthorizationKey.objects.filter(
        site_settings=site_settings)
    ctx = {
        'site_settings': site_settings,
        'authorization_keys': authorization_keys,
        'is_empty': not authorization_keys.exists()}
    return TemplateResponse(request, 'dashboard/sites/detail.html', ctx)


@staff_member_required
@permission_required('site.edit_settings')
def authorization_key_add(request, site_settings_pk):
    key = AuthorizationKey(site_settings_id=site_settings_pk)
    form = AuthorizationKeyForm(request.POST or None, instance=key)
    if form.is_valid():
        key = form.save()
        msg = pgettext_lazy(
            'Dashboard message', 'Added authorization key %s') % (key,)
        messages.success(request, msg)
        return redirect('dashboard:site-details', pk=site_settings_pk)
    ctx = {'form': form, 'site_settings_pk': site_settings_pk, 'key': key}
    return TemplateResponse(
        request, 'dashboard/sites/authorization_keys/form.html', ctx)


@staff_member_required
@permission_required('site.edit_settings')
def authorization_key_edit(request, site_settings_pk, key_pk):
    key = get_object_or_404(AuthorizationKey, pk=key_pk)
    form = AuthorizationKeyForm(request.POST or None, instance=key)
    if form.is_valid():
        key = form.save()
        msg = pgettext_lazy(
            'dashboard message', 'Updated authorization key %s') % (key,)
        messages.success(request, msg)
        return redirect('dashboard:site-details', pk=site_settings_pk)
    ctx = {'form': form, 'site_settings_pk': site_settings_pk, 'key': key}
    return TemplateResponse(
        request, 'dashboard/sites/authorization_keys/form.html', ctx)


@staff_member_required
@permission_required('site.edit_settings')
def authorization_key_delete(request, site_settings_pk, key_pk):
    key = get_object_or_404(AuthorizationKey, pk=key_pk)
    if request.method == 'POST':
        key.delete()
        messages.success(
            request,
            pgettext_lazy(
                'Dashboard message',
                'Removed site authorization key %s') %
            (key,))
        return redirect(
            'dashboard:site-details', pk=site_settings_pk)
    return TemplateResponse(
        request, 'dashboard/sites/modal/confirm_delete.html',
        {'key': key, 'site_settings_pk': site_settings_pk})
