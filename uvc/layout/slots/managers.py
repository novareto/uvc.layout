# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de 


import grok

from megrok.resourceviewlet import ResourcesManager
from uvc.layout.interfaces import *
from zope.interface import Interface

grok.templatedir('templates')


class Resources(ResourcesManager):
    grok.name('uvc-resources')
    grok.context(Interface)


class Headers(grok.ViewletManager):
    """Viewlet Manager for the Header
    """
    grok.name('uvc-headers')
    grok.context(Interface)
    grok.implements(IHeaders)


class AboveContent(grok.ViewletManager):
    grok.name('uvc-above-body')
    grok.context(Interface)
    grok.implements(IAboveContent)


class Tabs(grok.ViewletManager):
    grok.name('uvc-tabs')
    grok.context(Interface)
    grok.implements(ITabs)

    def content(self):
        results = [v.render() for v in self.viewlets]
        return "\n".join([r for r in results if r.strip()])

    def render(self):
        res = self.content()
        if not res:
            return u""
        return """<ul class='nav nav-pills'>%s</ul>""" % res


class BelowContent(grok.ViewletManager):
    grok.name('uvc-below-body')
    grok.context(Interface)
    grok.implements(IBelowContent)


class PageTop(grok.ViewletManager):
    """ViewletManager for the PageTop
    """
    grok.name('uvc-pagetop')
    grok.context(Interface)
    grok.implements(IPageTop)


class Footer(grok.ViewletManager):
    """ViewletManager for the PageTop
    """
    grok.name('uvc-footer')
    grok.context(Interface)
    grok.require('zope.View')


class BeforeActions(grok.ViewletManager):
    grok.name('uvcsite.beforeactions')
    grok.context(Interface)
    grok.implements(IBeforeActions)
    grok.require('zope.View')


class ExtraInfo(grok.ViewletManager):
    grok.name('uvcsite.extrainfo')
    grok.context(Interface)
    grok.implements(IExtraInfo)
    grok.require('zope.View')

