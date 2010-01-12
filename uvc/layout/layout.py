# -*- coding: utf-8 -*-
# Copyright (c) 2007-2008 NovaReto GmbH
# cklinger@novareto.de 

import grok
import megrok.layout

from zope.interface import Interface

grok.templatedir('layout_templates')

class Layout(megrok.layout.Layout):
    grok.context(Interface)
