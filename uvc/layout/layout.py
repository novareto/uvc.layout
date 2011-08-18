# -*- coding: utf-8 -*-
# Copyright (c) 2007-2008 NovaReto GmbH
# cklinger@novareto.de 

import grok
from uvc.layout.libraries import common
from dolmen.app.layout import master, skin
from zope.interface import Interface
from uvc.skin.skin import IUVCSkin

grok.templatedir('layout_templates')


class IUVCBaseLayer(IUVCSkin, skin.IBaseLayer):
    """
    """

class IUVCLayer(IUVCBaseLayer):
    """Base skin layer for an UVC Site
    """
    grok.skin('uvcskin')


class Layout(master.Master):
    grok.layer(IUVCBaseLayer)
    grok.name('uvc.layout')

    def update(self):
        #common.need()
        master.Master.update(self)
