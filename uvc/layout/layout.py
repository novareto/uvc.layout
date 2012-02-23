# -*- coding: utf-8 -*-
# Copyright (c) 2007-2008 NovaReto GmbH
# cklinger@novareto.de 

import grok

from megrok import layout
from zope import interface

from zope.container.interfaces import IContainer
from zope.publisher.interfaces import browser
from zope.traversing.browser import absoluteURL


grok.templatedir('templates')


class IUVCBaseLayer(browser.IDefaultBrowserLayer):
    """Base layer for uvc applications
    """


class IUVCSkin(IUVCBaseLayer):
    """Base skin layer for an UVC Site
    """
    grok.skin('uvcskin')


class Layout(layout.Layout):
    grok.context(interface.Interface)
    grok.layer(IUVCBaseLayer)
    grok.name('uvc.layout')

    def update(self):
        self.base = absoluteURL(self.context, self.request)
        if IContainer.providedBy(self.context) and self.base[:-1] != '/':
            self.base = self.base + '/'
