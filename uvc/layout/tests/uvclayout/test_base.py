"""
  >>> from zope.component import getMultiAdapter
  >>> from zope.publisher.browser import TestRequest
  >>> from zope.interface import directlyProvides
  >>> from uvc.layout.layout import IUVCBaseLayer 
  >>> root = getRootFolder()

  >>> root['app'] = context = Context()
  >>> context.__name__ = "app"
  >>> context.__parent__ = root

  >>> request = TestRequest()
  >>> directlyProvides(request, IUVCBaseLayer)

  >>> from grokcore.layout.interfaces import ILayout
  >>> layout = getMultiAdapter((request, context), ILayout)

  >>> layout
  <uvc.layout.layout.Layout object at ...>

  >>> layout.update()
  >>> layout.render()

"""


import grok

class Context(grok.Context):
    pass

