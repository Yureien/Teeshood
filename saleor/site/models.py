from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import pgettext_lazy
from versatileimagefield.fields import VersatileImageField

from . import AuthenticationBackends
from .patch_sites import patch_contrib_sites

patch_contrib_sites()


class SiteSettings(models.Model):
    site = models.OneToOneField(
        Site, related_name='settings', on_delete=models.CASCADE)
    header_text = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=500, blank=True)
    top_menu = models.ForeignKey(
        'menu.Menu', on_delete=models.SET_NULL, related_name='+', blank=True,
        null=True)
    bottom_menu = models.ForeignKey(
        'menu.Menu', on_delete=models.SET_NULL, related_name='+', blank=True,
        null=True)
    include_taxes_in_prices = models.BooleanField(default=True)
    display_gross_prices = models.BooleanField(default=True)
    charge_taxes_on_shipping = models.BooleanField(default=True)
    track_inventory_by_default = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ('edit_settings',
             pgettext_lazy('Permission description',
                           'Can edit site settings')),
            ('view_settings',
             pgettext_lazy('Permission description',
                           'Can view site settings')))

    def __str__(self):
        return self.site.name

    def available_backends(self):
        return self.authorizationkey_set.values_list('name', flat=True)


class ProductBanner(models.Model):
    site_settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE)
    title = models.CharField(max_length=80, blank=True, null=True)
    text = models.CharField(max_length=500, blank=True, null=True)
    image = VersatileImageField(upload_to='product-banners')
    product_url = models.URLField(blank=True, null=True)

    def __str__(self):
        if self.title:
            return self.title
        return self.name


class CategoryTile(models.Model):
    site_settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, blank=True, null=True)
    image = VersatileImageField(upload_to='product-banners')
    category_url = models.URLField(blank=True, null=True)

    def __str__(self):
        if self.name:
            return self.name
        return ""


class HallOfFame(models.Model):
    site_settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE)
    image = VersatileImageField(upload_to='hall-of-fame')
    product_url = models.URLField(blank=True, null=True)


class CustomerBanner(models.Model):
    site_settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE)
    image = VersatileImageField(upload_to='hall-of-fame')
    url = models.URLField(blank=True, null=True)


class ProductCoupon(models.Model):
    site_settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)


class Career(models.Model):
    site_settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    forms_link = models.URLField()
    experience = models.CharField(max_length=40)
    openings = models.IntegerField()
    categories = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=40)


class AuthorizationKey(models.Model):
    site_settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE)
    name = models.CharField(
        max_length=20, choices=AuthenticationBackends.BACKENDS)
    key = models.TextField()
    password = models.TextField()

    class Meta:
        unique_together = (('site_settings', 'name'),)

    def __str__(self):
        return self.name

    def key_and_secret(self):
        return self.key, self.password
