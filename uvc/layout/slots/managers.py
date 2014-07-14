# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de 


import uvclight
from uvc.layout.interfaces import *
from zope.interface import Interface


class Headers(uvclight.ViewletManager):
    """Viewlet Manager for the Header
    """
    uvclight.name('uvc-headers')
    uvclight.context(Interface)
    uvclight.implements(IHeaders)


class AboveContent(uvclight.ViewletManager):
    uvclight.name('uvc-above-body')
    uvclight.context(Interface)
    uvclight.implements(IAboveContent)
    

class Tabs(uvclight.ViewletManager):
    uvclight.name('uvc-tabs')
    uvclight.context(Interface)
    uvclight.implements(ITabs)
    
    def content(self):
        results = [v.render() for v in self.viewlets]
        return "\n".join([r for r in results if r.strip()])

    def render(self):
        res = self.content()
        if not res:
            return u""
        return """<ul class='nav nav-pills'>%s</ul>""" % res


class BelowContent(uvclight.ViewletManager):
    uvclight.name('uvc-below-body')
    uvclight.context(Interface)
    uvclight.implements(IBelowContent)


class PageTop(uvclight.ViewletManager):
    """ViewletManager for the PageTop
    """
    uvclight.name('uvc-pagetop')
    uvclight.context(Interface)
    uvclight.implements(IPageTop)
    

class Footer(uvclight.ViewletManager):
    """ViewletManager for the PageTop
    """
    uvclight.name('uvc-footer')
    uvclight.context(Interface)
    uvclight.require('zope.View')
    

class BeforeActions(uvclight.ViewletManager):
    uvclight.name('uvcsite.beforeactions')
    uvclight.context(Interface)
    uvclight.implements(IBeforeActions)
    uvclight.require('zope.View')
    

class ExtraInfo(uvclight.ViewletManager):
    uvclight.name('uvcsite.extrainfo')
    uvclight.context(Interface)
    uvclight.implements(IExtraInfo)
    uvclight.require('zope.View')

