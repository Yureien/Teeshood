from django.conf.urls import url
from impersonate.views import stop_impersonate

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^style-guide/', views.styleguide, name='styleguide'),
    url(r'^about/', views.about, name='about'),
    url(r'^privacy-policy/', views.privacy_policy, name='privacy-policy'),
    url(r'^impersonate/(?P<uid>\d+)/', views.impersonate,
        name='impersonate-start'),
    url(r'^impersonate/stop/$', stop_impersonate,
        name='impersonate-stop'),
    url(r'^design-upload/', views.design_upload, name='design-upload'),
    url(r'^bulk-order/', views.bulk_order, name='bulk-order'),
    url(r'^404', views.handle_404, name='handle-404'),
    url(r'^manifest\.json$', views.manifest, name='manifest'),
]
