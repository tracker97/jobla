from django.conf.urls import url
from jobapp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^jobs/(?P<id>[0-9]+)/$', views.job_detail, name='job_detail'),
    url(r'^my_jobs/$', views.my_jobs, name='my_jobs'),
    url(r'^create_job/$', views.create_job, name='create_job'),
    url(r'^edit_job/(?P<id>[0-9]+)/$', views.edit_job, name='edit_job'),
    url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
]
