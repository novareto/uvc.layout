# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import grok
from zope.interface import Interface
from uvc.layout.interfaces import IPageTop, IFooter, IAboveContent, ITabs
from zope.component import getMultiAdapter
from zope.viewlet.interfaces import IContentProvider
from uvc.layout.slots.managers import Footer
from megrok.pagetemplate import PageTemplate
from zope.pagetemplate.interfaces import IPageTemplate


grok.templatedir('templates')


class Menu(grok.Viewlet):
    grok.baseclass()

    def default_namespace(self):
        namespace = grok.Viewlet.default_namespace(self)
        namespace['entries'] = self.menus
        namespace['component'] = self
        return namespace


class GlobalMenuViewlet(Menu):
    grok.viewletmanager(IPageTop)
    grok.context(Interface)
    grok.order(20)

    id = "globalmenuviewlet"

    def update(self):
        globalmenu = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IContentProvider, 'globalmenu')
        self.menus = globalmenu.getMenuItems()
        self.renderableitems = globalmenu.getRenderableItems()

    def render(self):
        template = getMultiAdapter((self, self.request), IPageTemplate)
        return template()


class GlobalMenuTemplate(PageTemplate):
    grok.view(GlobalMenuViewlet)


class PersonalPreferencesViewlet(Menu):
    grok.viewletmanager(IPageTop)
    grok.context(Interface)
    grok.order(40)

    id = "personalpreferencesviewlet"

    def update(self):
        self.menus = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IContentProvider, 'personalpreferences').getMenuItems()

    @property
    def username(self):
        return self.view.request.principal.title

    def render(self):
        template = getMultiAdapter((self, self.request), IPageTemplate)
        return template()


class PersonalPreferencesTemplate(PageTemplate):
    grok.view(PersonalPreferencesViewlet)


class DocumentActionsMenuViewlet(Menu):
    grok.viewletmanager(IAboveContent)
    grok.context(Interface)
    grok.order(40)

    id = "documentactionsmenuviewlet"
    name = "Document actions"

    def update(self):
        self.menus = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IContentProvider, 'documentactions').getMenuItems()

    def render(self):
        template = getMultiAdapter((self, self.request), IPageTemplate)
        return template()


class DocumentActionsTemplate(PageTemplate):
    grok.view(DocumentActionsMenuViewlet)


class FooterViewlet(Menu):
    grok.viewletmanager(Footer)
    grok.context(Interface)
    grok.order(10)

    id = "footerviewlet"

    def update(self):
        self.menus = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IContentProvider, 'footermenu').getMenuItems()

    def render(self):
        template = getMultiAdapter((self, self.request), IPageTemplate)
        return template()


class FooterTemplate(PageTemplate):
    grok.view(FooterViewlet)


class ExtraViewsViewlet(Menu):
    grok.viewletmanager(ITabs)
    grok.context(Interface)
    grok.order(10)

    id = "extraviewsviewlet"

    def update(self):
        self.menus = getMultiAdapter(
            (self.view.context, self.request, self.view),
            IContentProvider, 'extraviews').getMenuItems()

    def render(self):
        template = getMultiAdapter((self, self.request), IPageTemplate)
        return template()


class ExtraViewsTemplate(PageTemplate):
    grok.view(ExtraViewsViewlet)
