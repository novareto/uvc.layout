# -*- coding: utf-8 -*-
# Copyright (c) 2007-2008 NovaReto GmbH
# cklinger@novareto.de 

import uvclight
from cromlech.browser.interfaces import ITypedRequest
from cromlech.container.interfaces import IContainer
from dolmen.location import get_absolute_url
from zope.interface import Interface


class IUVCBaseLayer(ITypedRequest):
    """Base layer for uvc applications
    """


class Layout(uvclight.Layout):
    uvclight.context(Interface)
    uvclight.layer(IUVCBaseLayer)
    uvclight.name('')

    def update(self):
        uvclight.Layout.update(self)
        self.base = get_absolute_url(self.context, self.request)
        if IContainer.providedBy(self.context) and self.base[:-1] != '/':
            self.base = self.base + '/'
        self.view.update()
