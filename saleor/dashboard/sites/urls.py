from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='site-index'),
    url(r'^(?P<pk>\d+)/update/$', views.site_settings_edit,
        name='site-update'),
    url(r'^(?P<pk>\d+)/$', views.site_settings_details,
        name='site-details'),
    url(r'^(?P<pk>\d+)/delete/$', views.site_settings_edit,
        name='site-delete'),
    url(r'^(?P<pk>\d+)/banner-update/$', views.product_banner_edit,
        name='site-home-product-banner-update'),
    url(r'^(?P<pk>\d+)/hall_of_fame_update/$', views.hall_of_fame_edit,
        name='site-home-hall-of-fame-update'),
    url(r'^(?P<pk>\d+)/product-coupon-update/$', views.product_coupon_edit,
        name='site-home-product-coupon-update'),
    url(r'^(?P<pk>\d+)/category-tile-update/$', views.category_tile_edit,
        name='site-home-category-tile-update'),

    url(r'^(?P<site_settings_pk>\d+)/authorization_key/add/$',
        views.authorization_key_add, name='authorization-key-add'),
    url(r'^(?P<site_settings_pk>\d+)/authorization_key/'
        r'(?P<key_pk>\d+)/update/$',
        views.authorization_key_edit, name='authorization-key-edit'),
    url(r'^(?P<site_settings_pk>\d+)/authorization_key/'
        r'(?P<key_pk>\d+)/delete/$',
        views.authorization_key_delete, name='authorization-key-delete')]
