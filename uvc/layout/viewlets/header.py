# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de 

import uvclight
from zope.interface import Interface
from uvc.layout.interfaces import IPageTop


class BGHeader(uvclight.Viewlet):
    uvclight.baseclass()
    uvclight.viewletmanager(IPageTop)
    uvclight.context(Interface)
    uvclight.order(10)

    template = uvclight.get_template('bgheader.cpt', __file__)
