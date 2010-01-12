# -*- coding: utf-8 -*-
# Copyright (c) 2007-2008 NovaReto GmbH
# cklinger@novareto.de 

import grok
from zope.interface import Interface
from zope.component import queryUtility, getUtility, getMultiAdapter
from zope.traversing.browser import absoluteURL
from uvc.layout.interfaces import IStatusMessage, IBreadCrumb
from z3c.flashmessage.interfaces import IMessageReceiver
from z3c.breadcrumb.interfaces import IBreadcrumb, IBreadcrumbs

grok.templatedir('viewlets_templates')

class Breadcrumbs(grok.Viewlet):
    grok.name('breadcrumb')
    grok.context(Interface)
    grok.viewletmanager(IBreadCrumb)

    def render(self):
        bcs = []
        for bc in getMultiAdapter((self.context, self.request),
                                   IBreadcrumbs).crumbs:
            bcs.append("<a href=%s> %s </a>/" %(bc.get('url'), bc.get('name')))
        return "".join(bcs[1:])

class StatusMessages(grok.Viewlet):
    grok.name('uvcsite.messages')
    grok.context(Interface)
    grok.viewletmanager(IStatusMessage)

    def update(self):
        self.messages=[]
        source = queryUtility(IMessageReceiver)
        if source:
            self.messages = list(source.receive())

