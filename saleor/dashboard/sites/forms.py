from django import forms
from django.contrib.sites.models import Site
from django.utils.translation import pgettext_lazy

from ...site.models import (AuthorizationKey, SiteSettings, ProductCoupon,
                            ProductBanner, HallOfFame, CategoryTile, CustomerBanner)


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        exclude = []
        labels = {
            'domain': pgettext_lazy(
                'Domain name (FQDN)', 'Domain name'),
            'name': pgettext_lazy(
                'Display name', 'Display name')}


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = ['header_text', 'description', 'track_inventory_by_default']
        labels = {
            'header_text': pgettext_lazy(
                'Header text', 'Header text'),
            'description': pgettext_lazy(
                'Description', 'Description'),
            'track_inventory_by_default': pgettext_lazy(
                'Inventory tracking by default settings toggle label',
                'Enable inventory tracking for newly created products')}
        help_texts = {
            'track_inventory_by_default': pgettext_lazy(
                'handle stock by default settings field help text',
                'This will set the default value of stock handling '
                'on product and variant creation')}


class AuthorizationKeyForm(forms.ModelForm):
    class Meta:
        model = AuthorizationKey
        exclude = []
        labels = {
            'key': pgettext_lazy(
                'Key for chosen authorization method', 'Key'),
            'password': pgettext_lazy(
                'Password', 'Password'),
            'name': pgettext_lazy(
                'Item name', 'Name')}
        widgets = {'password': forms.PasswordInput(render_value=True),
                   'key': forms.TextInput(),
                   'site_settings': forms.widgets.HiddenInput()}


class ProductBannerForm(forms.ModelForm):
    class Meta:
        model = ProductBanner
        exclude = ['site_settings']
        labels = {
            'text': pgettext_lazy(
                'Banner text', 'Text'),
            'image': pgettext_lazy(
                'Banner image', 'Image'),
            'product_url': pgettext_lazy(
                'Link to product', 'Link'),
        }


class HallOfFameForm(forms.ModelForm):
    class Meta:
        model = HallOfFame
        exclude = ['site_settings']
        labels = {
            'image': pgettext_lazy(
                'Banner image', 'Image'),
            'product_url': pgettext_lazy(
                'Link to product', 'Link'),
        }


class CustomerBannerForm(forms.ModelForm):
    class Meta:
        model = CustomerBanner
        exclude = ['site_settings']
        labels = {
            'image': pgettext_lazy(
                'Banner image', 'Image'),
            'product_url': pgettext_lazy(
                'Link', 'Link'),
        }


class ProductCouponForm(forms.ModelForm):
    class Meta:
        model = ProductCoupon
        exclude = ['site_settings']
        labels = {
            'code': pgettext_lazy(
                'Coupon Code', 'Coupon Code'),
            'title': pgettext_lazy(
                'Coupon Title', 'Coupon Title'),
            'description': pgettext_lazy(
                'Coupon Description', 'Coupon Description'),
        }


class CategoryTileForm(forms.ModelForm):
    class Meta:
        model = HallOfFame
        exclude = ['site_settings']
        labels = {
            'name': pgettext_lazy(
                'Category Name', 'Name'),
            'image': pgettext_lazy(
                'Banner image', 'Image'),
            'category_url': pgettext_lazy(
                'Link to product', 'Link'),
        }
