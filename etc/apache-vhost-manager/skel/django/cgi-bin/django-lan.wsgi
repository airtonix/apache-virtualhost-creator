#!/usr/bin/env python
import os
project_path = os.path.abspath( os.path.join( os.path.dirname(__file__) ,"..") )
ALLDIRS = [ project_path, os.path.join(project_path, "environ", "lib", "python2.6", "site-packages"), ]

import sys
import site

# Remember original sys.path.
prev_sys_path = list(sys.path)

# Add each new site-packages directory.
for directory in ALLDIRS:
  site.addsitedir(directory)

# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
  if item not in prev_sys_path:
    new_sys_path.append(item)
    sys.path.remove(item)
sys.path[:0] = new_sys_path

from django.core.handlers.wsgi import WSGIHandler
_application = WSGIHandler()

def application(environ, start_response):
  os.environ['DJANGO_SITE_PROFILE'] = 'lan'
  os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
  return _application(environ, start_response)

