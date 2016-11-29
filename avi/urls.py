"""
GAVIP Example AVIS: Simple AVI

These URLs are used by the AVI web-interface.
@req: REQ-0006
@comp: AVI Web System
"""
from django.conf.urls import include, patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from plugins.urls import job_list_urls
from avi import views

urlpatterns = patterns(
    '',
    url(r'^$',
        views.index,
        name='index'),

    url(r'^job_list/',
        include(job_list_urls,
        namespace='job_list')),

    url(r'^run_query/$',
        views.run_query,
        name='run_query'),

    url(r'^result/(?P<job_id>[0-9]+)/$',
        views.job_result,
        name='job_result')
)
