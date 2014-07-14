# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de 

import uvclight
from cromlech.browser import ITemplate
from grokcore.component import adapter, implementer
from uvc.layout.interfaces import *
from uvc.layout.slots.components import Menu
from zope.component import getMultiAdapter
from zope.interface import Interface


class GlobalMenu(Menu):
    uvclight.implements(IGlobalMenu)
    uvclight.name('globalmenu')


class Footer(Menu):
    uvclight.implements(IFooter)
    uvclight.name('footermenu')


class PersonalPreferences(Menu):
    uvclight.implements(IPersonalPreferences)
    uvclight.name('personalpreferences')


class DocumentActionsMenu(Menu):
    uvclight.implements(IDocumentActions)
    uvclight.name('documentactions')


class ExtraViews(Menu):
    uvclight.implements(IExtraViews)
    uvclight.context(Interface)
    uvclight.name('extraviews')


class SpotMenu(Menu):
    uvclight.implements(ISpotMenu)
    uvclight.name('spotmenu')


class PersonalMenu(Menu):
    uvclight.implements(IPersonalMenu)
    uvclight.context(Interface)
    uvclight.name('personalmenu')

    def render(self):
        template = getMultiAdapter((self, self.request), ITemplate)
        return template()


@adapter(PersonalMenu, Interface)
@implementer(ITemplate)
def PersonalMenuTemplate(context, request):
    return uvclight.get_template('personalmenutemplate.cpt', __file__)
