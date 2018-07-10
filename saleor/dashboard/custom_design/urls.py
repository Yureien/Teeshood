from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.custom_design_list, name='custom-design-list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.custom_design_details, name='custom-design-details'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        views.custom_design_delete, name='custom-design-delete'),
]
