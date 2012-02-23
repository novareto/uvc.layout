# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de 

import grok

from uvc.layout.interfaces import IPageTop
from grokcore.message import receive
from zope.interface import Interface, moduleProvides

grok.templatedir('templates')

class FlashMessages(grok.Viewlet):
    grok.baseclass()
    grok.order(200)
    grok.context(Interface)
    grok.name('uvcsite.messages')
    grok.viewletmanager(IPageTop)

    def update(self):
        received = receive()
        if received is not None:
            self.messages = list(received)
        else:
            self.messages = []
