# -*- coding: utf-8 -*-

import grok
from uvc.layout.interfaces import *
from zope.interface import Interface
from dolmen import menu
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


class PageTop(master.Top):
    """ViewletManager for the PageTop
    """
    grok.name('uvcsite.pagetop')
    grok.context(Interface)
    grok.implements(IPageTop)
    grok.require('zope.View')


class Panels(grok.ViewletManager):
    grok.name('uvcsite.panels')
    grok.context(Interface)
    grok.implements(IPanels)
    grok.require('zope.View')


class BeforeActions(grok.ViewletManager):
    grok.name('uvcsite.beforeactions')
    grok.context(Interface)
    grok.implements(IBeforeActions)
    grok.require('zope.View')
