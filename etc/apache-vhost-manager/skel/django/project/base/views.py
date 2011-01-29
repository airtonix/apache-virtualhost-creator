import os, datetime, time

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404

from lib.autorender import *
from forms import *

## LISTS
@auto_render
def dashboard(template_name="dashboard.html") :
  return template_name, { "data" : None }

