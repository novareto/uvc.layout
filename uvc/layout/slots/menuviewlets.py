# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de 

import uvclight
from cromlech.browser import ITemplate
from grokcore.component import adapter, implementer
from uvc.layout.interfaces import IPageTop, IFooter, IAboveContent, ITabs
from uvc.layout.slots.managers import Footer
from zope.component import getMultiAdapter, getUtility
from zope.interface import Interface


class GlobalMenuViewlet(uvclight.Viewlet):
    uvclight.viewletmanager(IPageTop)
    uvclight.context(Interface)
    uvclight.order(20)

    id = "globalmenuviewlet"

    def update(self):
        globalmenu = getMultiAdapter(
                (self.view.context, self.request, self.view),
                IContentProvider, 'globalmenu')
        self.menus = globalmenu.getMenuItems()
        self.renderableitems = globalmenu.getRenderableItems()

    def render(self):
        template = getMultiAdapter((self, self.request), ITemplate)
        return template()


@adapter(GlobalMenuViewlet, Interface)
@implementer(ITemplate)
def GlobalMenuTemplate(context, request):
    return uvclight.get_template('globalmenuviewlet.cpt', __file__)


class PersonalPreferencesViewlet(uvclight.Viewlet):
    uvclight.viewletmanager(IPageTop)
    uvclight.context(Interface)
    uvclight.order(40)

    id = "personalpreferencesviewlet"

    def update(self):
        self.menus = getMultiAdapter(
                (self.view.context, self.request, self.view),
                IContentProvider, 'personalpreferences').getMenuItems()

    @property
    def username(self):
        return self.view.request.principal.title

    def render(self):
        template = getMultiAdapter((self, self.request), ITemplate)
        return template()


@adapter(PersonalPreferencesViewlet, Interface)
@implementer(ITemplate)
def PersonalPreferencesTemplate(context, request):
    return uvclight.get_template('personalpreferencesviewlet.cpt', __file__)


class DocumentActionsMenuViewlet(uvclight.Viewlet):
    uvclight.viewletmanager(IAboveContent)
    uvclight.context(Interface)
    uvclight.order(40)

    id = "documentactionsmenuviewlet"

    def update(self):
        self.menus = getMultiAdapter(
                (self.view.context, self.request, self.view),
                IContentProvider, 'documentactions').getMenuItems()

    def render(self):
        template = getMultiAdapter((self, self.request), ITemplate)
        return template()

    
@adapter(DocumentActionsMenuViewlet, Interface)
@implementer(ITemplate)
def DocumentActionsTemplate(context, request):
    return uvclight.get_template('documentactionsmenuviewlet.cpt', __file__)


class FooterViewlet(uvclight.Viewlet):
    uvclight.viewletmanager(Footer)
    uvclight.context(Interface)
    uvclight.order(10)

    id = "footerviewlet"

    def update(self):
        self.menus = getMultiAdapter(
                (self.view.context, self.request, self.view), IContentProvider, 'footermenu').getMenuItems()

    def render(self):
        template = getMultiAdapter((self, self.request), ITemplate)
        return template()


@adapter(FooterViewlet, Interface)
@implementer(ITemplate)
def FooterTemplate(context, request):
    return uvclight.get_template('footerviewlet.cpt', __file__)
        

class ExtraViewsViewlet(uvclight.Viewlet):
    uvclight.viewletmanager(ITabs)
    uvclight.context(Interface)
    uvclight.order(10)

    id = "extraviewsviewlet"

    def update(self):
        self.menus = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IContentProvider, 'extraviews').getMenuItems()

    def render(self):
        template = getMultiAdapter((self, self.request), ITemplate)
        return template()


@adapter(ExtraViewsViewlet, Interface)
@implementer(ITemplate)
def ExtraViewsTemplate(context, request):
    return uvclight.get_template('extraviewstemplate.cpt', __file__)
