# -*- coding: utf-8 -*-
# Copyright (c) 2007-2008 NovaReto GmbH
# cklinger@novareto.de 

import grok
from uvc.layout.libraries import common
from dolmen.app.layout import master, skin
from zope.interface import Interface

grok.templatedir('layout_templates')


class IUVCLayer(skin.IBaseLayer):
    """Base skin layer for an UVC Site
    """


class Layout(master.Master):
    grok.layer(IUVCLayer)
    grok.name('uvc.layout')

    def update(self):
        common.need()
        master.Master.update(self)
