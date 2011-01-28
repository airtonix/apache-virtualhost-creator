#!/usr/bin/env python
import os, sys
import django.core.handlers.wsgi

sys.path.insert(0,'/var/www/${DOMAIN_FQDN}')
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
application = django.core.handlers.wsgi.WSGIHandler()

