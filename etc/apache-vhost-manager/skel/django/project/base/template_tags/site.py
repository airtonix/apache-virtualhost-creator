from django import template
from django.template import Library, Node, resolve_variable
from django.conf import settings

register = template.Library()


class SiteNameNode(Node):
  def __init__(self, nodelist = None):
    self.nodelist = nodelist

  def render(self, context = None):
    return settings.PROJECT_NAME

@register.tag("sitename")
def sitename(parser=None, token=None):
  return SiteNameNode()

class SiteUrlNode(Node):
  def __init__(self, nodelist = None):
    self.nodelist = nodelist

  def render(self, context = None):
    return settings.PROJECT_URL

@register.tag("siteurl")
def siteurl(parser=None, token=None):
  return SiteUrlNode()

