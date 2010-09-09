#!/usr/bin/python
# -*- coding: utf-8 -*-

import grokcore.viewlet as grok
from dolmen import menu
from zope.interface import Interface
from uvc.layout import interfaces, menus
import megrok.pagetemplate as pt
from dolmen.app.layout import MenuViewlet
from dolmen.app.layout.viewlets import ContextualActions
from megrok.navigation.components import MenuItem, SiteMenuItem, Menu


grok.templatedir('templates')
grok.context(Interface)


class GlobalMenuViewlet(grok.Viewlet):
    grok.viewletmanager(interfaces.IPageTop)
    grok.order(10)

    def update(self):
        self.menu = menus.GlobalMenu(self.context, self.request, self.view)
        self.menu.update()

    def default_namespace(self):
        ns = self.menu.default_namespace()
        ns['menu'] = self.menu
        ns['viewlet'] = self
        return ns

    def render(self):
        return self.menu.render()


class PreferencesViewlet(grok.Viewlet):
    grok.name('user-preferences')
    grok.viewletmanager(interfaces.IPageTop)
    grok.order(20)

    def render(self):
        menu = menus.PersonalPreferences(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class DocumentActionsViewlet(grok.Viewlet):
    grok.name('document-actions')
    grok.viewletmanager(interfaces.IAboveContent)
    grok.order(10)

    def render(self):
        menu = menus.DocumentActionsMenu(
            self.context, self.request, self.view)
        menu.update()
        return menu.render()


class ExtraViewsViewlet(ContextualActions):
    grok.order(20)
    grok.name('extra-views')
    grok.viewletmanager(interfaces.IAboveContent)
    grok.require("zope.Public")

    menu_factory = menus.ExtraViews

    def update(self):
        MenuViewlet.update(self)
        if not len(self.menu.viewlets):
            self.actions = None
        else:
            self.actions = self.compute_actions(self.menu.viewlets)

    def compute_actions(self, viewlets):
        for action in viewlets:
            selected = action.__name__ == self.view.__name__
            url = not selected and "%s/%s" % (self.menu.context_url, action.__name__) or None
            yield {
                'id': action.__name__,
                'url': url,
                'title': action.title or action.__name__,
                'selected': selected,
                'class': (selected and 'selected ' +
                          self.menu.entry_class or self.menu.entry_class),
                }


class ItemTemplate(pt.PageTemplate):
    pt.view(SiteMenuItem)


class MenuItemTemplate(pt.PageTemplate):
    pt.view(MenuItem)
