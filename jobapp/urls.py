from django.conf.urls import url
from jobapp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^jobs/(?P<id>[0-9]+)/$', views.job_detail, name='job_detail'),
]
