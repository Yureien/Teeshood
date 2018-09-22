from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.bulk_order_list, name='bulk-order-list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.bulk_order_details, name='bulk-order-details'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        views.bulk_order_delete, name='bulk-order-delete'),
    url(r'product-type/value/add/$',
        views.order_type_value_create,
        name='bulk-order-type-value-add'),
    url(r'product-type/value/(?P<value_pk>[0-9]+)/update/$',  # noqa
        views.order_type_value_edit,
        name='bulk-order-type-value-update'),
    url(r'product-type/value/(?P<value_pk>[0-9]+)/delete/$',  # noqa
        views.order_type_value_delete,
        name='bulk-order-type-value-delete'),
    url(r'product-color/value/add/$',
        views.order_color_value_create,
        name='bulk-order-color-value-add'),
    url(r'product-color/value/(?P<value_pk>[0-9]+)/update/$',  # noqa
        views.order_color_value_edit,
        name='bulk-order-color-value-update'),
    url(r'product-color/value/(?P<value_pk>[0-9]+)/delete/$',  # noqa
        views.order_color_value_delete,
        name='bulk-order-color-value-delete'),
]
