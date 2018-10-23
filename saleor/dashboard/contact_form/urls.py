from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.contact_form_list, name='contact-form-list'),
    url(r'^(?P<pk>[0-9]+)/$',
        views.contact_form_details, name='contact-form-details'),
    url(r'^(?P<pk>[0-9]+)/delete/$',
        views.contact_form_delete, name='contact-form-delete'),
]
