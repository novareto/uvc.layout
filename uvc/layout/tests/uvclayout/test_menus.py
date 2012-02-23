"""
 >>> from zope.publisher.browser import TestRequest
 >>> from zope.component import getMultiAdapter
 >>> from zope.interface import Interface
 >>> root = getRootFolder()

 >>> root['app'] = context = Context()
 >>> request = TestRequest()

 >>> view = getMultiAdapter((context, request), name='index')
 >>> view
 <uvc.layout.tests.layout.test_menus.Index object at ...>

 >>> from zope.viewlet.interfaces import IContentProvider
 >>> menu = getMultiAdapter((context, request, view), IContentProvider, 'globalmenu')
 >>> menu
 <uvc.layout.tests.layout.test_menus.GlobalMenu object at ...>

 >>> from pprint import pformat
 >>> menu.update()
 >>> print pformat(menu.getMenuItems())
 [{'action': 'user',
   'description': 'User Description',
   'icon': '@@/dd/pdf.png',
   'selected': False,
   'submenu': [],
   'title': 'User'}]

"""

import grok

from zope.interface import Interface
from uvc.layout import Menu, MenuItem, SubMenu


class Context(grok.Context):
    pass


class Index(grok.View):
    grok.context(Interface)
    grok.name('index')

    def render(self):
        return "BL"


class GlobalMenu(Menu):
    pass


class User(MenuItem):
    grok.viewletmanager(GlobalMenu)
    grok.title('User')
    grok.description('User Description')

    action = "user"
    icon = "@@/dd/pdf.png"


class IndexMenu(MenuItem):
    grok.viewletmanager(GlobalMenu)
    grok.title('Startseite')
    
    action = "index"


class Apps(SubMenu):
    grok.viewletmanager(GlobalMenu)
    grok.title('Apps')


class Entgeltnachweis(MenuItem):
    grok.viewletmanager(Apps)
    grok.title('Entgeltnachweis')

    action = "BLA"


class Unfallanzeige(MenuItem):
    grok.viewletmanager(Apps)
    grok.title('Unfallanzeige')


    def available(self):
        return False

