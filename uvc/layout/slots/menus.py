# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import grok

from megrok.pagetemplate import PageTemplate
from uvc.layout.interfaces import *
from uvc.layout.slots.components import Menu
from zope.component import getMultiAdapter
from zope.interface import Interface
from zope.pagetemplate.interfaces import IPageTemplate


grok.templatedir('templates')


class GlobalMenu(Menu):
    grok.implements(IGlobalMenu)
    grok.name('globalmenu')


class Footer(Menu):
    grok.implements(IFooter)
    grok.name('footermenu')


class PersonalPreferences(Menu):
    grok.implements(IPersonalPreferences)
    grok.name('personalpreferences')


class DocumentActionsMenu(Menu):
    grok.implements(IDocumentActions)
    grok.name('documentactions')


class ExtraViews(Menu):
    grok.implements(IExtraViews)
    grok.context(Interface)
    grok.name('extraviews')


class SpotMenu(Menu):
    grok.implements(ISpotMenu)
    grok.name('spotmenu')


class PersonalMenu(Menu):
    grok.implements(IPersonalMenu)
    grok.context(Interface)
    grok.name('personalmenu')

    def render(self):
        template = getMultiAdapter((self, self.request), IPageTemplate)
        return template()


class PersonalMenuTemplate(PageTemplate):
    grok.view(PersonalMenu)


class QuickLinks(Menu):
    grok.implements(IQuickLinks)
    grok.name('quicklinks')

