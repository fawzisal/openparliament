from django.conf.urls import *

urlpatterns = patterns('parliament.committees.views',
    url(r'^$', 'committee_list', name='committee_list'),
    (r'^(?P<committee_id>\d+)/', 'committee_id_redirect'),
    (r'^(?P<slug>[^/]+)/$', 'committee'),
    url(r'^(?P<slug>[^/]+)/(?P<year>2\d\d\d)/$', 'committee_year_archive', name='committee_year_archive'),
    url(r'^(?P<committee_slug>[^/]+)/(?P<session_id>\d+-\d)/(?P<number>\d+)/$', 'committee_meeting', name='committee_meeting'),
    url(r'^(?P<committee_slug>[^/]+)/(?P<session_id>\d+-\d)/(?P<number>\d+)/(?P<slug>[a-zA-Z0-9-]+)/$', 'committee_meeting', name='committee_meeting'),
)