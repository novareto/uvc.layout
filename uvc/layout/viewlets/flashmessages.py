# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de 

import uvclight
from dolmen.message import receive
from uvc.layout.interfaces import IPageTop
from zope.interface import Interface, moduleProvides


class FlashMessages(uvclight.Viewlet):
    uvclight.baseclass()
    uvclight.order(200)
    uvclight.context(Interface)
    uvclight.name('uvcsite.messages')
    uvclight.viewletmanager(IPageTop)

    template = uvclight.get_template('flashmessages.cpt', __file__)
    
    def update(self):
        received = receive()
        if received is not None:
            self.messages = list(received)
        else:
            self.messages = []
