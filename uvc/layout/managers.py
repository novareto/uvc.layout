# -*- coding: utf-8 -*-

import grok
from uvc.layout.interfaces import *
from zope.interface import Interface
from dolmen.app.layout import master 

grok.templatedir('templates')


class Headers(master.Header):
    """Viewlet Manager for the Header
    """
    grok.name('uvcsite.headers')
    grok.context(Interface)
    grok.implements(IHeaders)


class AboveContent(master.AboveBody):
    grok.name('uvcsite.abovecontent')
    grok.context(Interface)
    grok.implements(IAboveContent)


class BelowContent(master.BelowBody):
    grok.name('uvcsite.belowcontent')
    grok.context(Interface)
    grok.implements(IBelowContent)


class Footer(master.Footer):
    """ViewletManager for the Footer
    """
    grok.name('uvcsite.footer')
    grok.context(Interface)
    grok.implements(IFooter)
    grok.require('zope.View')


class PageTop(master.Top):
    """ViewletManager for the PageTop
    """
    grok.name('uvcsite.pagetop')
    grok.context(Interface)
    grok.implements(IPageTop)
    grok.require('zope.View')


class Sidebar(grok.ViewletManager):
    grok.name('uvcsite.sidebar')
    grok.context(Interface)
    grok.implements(ISidebar)
    

class Panels(grok.ViewletManager):
    grok.name('uvcsite.panels')
    grok.context(Interface)
    grok.implements(IHelp)
