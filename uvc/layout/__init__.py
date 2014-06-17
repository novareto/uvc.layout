# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import grokcore.message
from grok.components import ViewSupportMixin
from grok import baseclass, View as BaseView
from grok.interfaces import IGrokView
from grokcore.layout import Page as BasePage
from megrok.z3ctable import TablePage

from .layout import Layout
from .interfaces import *
from .slots.components import Menu, MenuItem, SubMenu
from .forms.event import IAfterSaveEvent

from zope.interface import implementer


@implementer(IGrokView)
class GrokView(ViewSupportMixin):
    pass


class View(BaseView):
    baseclass()


class Page(GrokView, BasePage):
    baseclass()


class TablePage(GrokView, TablePage):
    baseclass()
