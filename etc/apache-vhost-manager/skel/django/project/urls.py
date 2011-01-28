from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^/$', 'dashboard', name='common-dashboard'),
)

