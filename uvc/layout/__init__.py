# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import grokcore.message
from grok import baseclass, util as grok_util
from grok.interfaces import IGrokView
from grokcore.layout import Page as BasePage
from megrok.z3ctable import TablePage

from uvc.layout.interfaces import *
from uvc.layout.slots.components import Menu, MenuItem, SubMenu
from uvc.layout.forms.event import IAfterSaveEvent

from zope.interface import implementer


@implementer(IGrokView)
class GrokView(object):
    
    def application_url(self, name=None, data=None):
        return grok_util.application_url(self.request, self.context, name, data)

    def flash(self, message, type='message'):
        grokcore.message.send(message, type=type, name='session')


class Page(GrokView, BasePage):
    baseclass()


class TablePage(GrokView, TablePage):
    baseclass()
