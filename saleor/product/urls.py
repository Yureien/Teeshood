from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<slug>[a-z0-9-_]+?)-(?P<product_id>[0-9]+)/$',
        views.product_details, name='details'),
    url(r'^quickview/(?P<slug>[a-z0-9-_]+?)-(?P<product_id>[0-9]+)/$',
        views.product_quickview, name='quickview'),
    url(r'^pincode/(?P<slug>[a-z0-9-_]+?)-(?P<product_id>[0-9]+)-(?P<pincode>[0-9]+)/$',
        views.check_pincode_availability, name='pincode_checker'),
    url(r'^category/(?P<path>[a-z0-9-_/]+?)-(?P<category_id>[0-9]+)/$',
        views.category_index, name='category'),
    url(r'(?P<slug>[a-z0-9-_]+?)-(?P<product_id>[0-9]+)/add/$',
        views.product_add_to_cart, name='add-to-cart'),
    url(r'^collection/(?P<slug>[a-z0-9-_/]+?)-(?P<pk>[0-9]+)/$',
        views.collection_index, name='collection')]
