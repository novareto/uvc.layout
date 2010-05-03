#!/usr/bin/python
# -*- coding: utf-8 -*-

import grokcore.viewlet as grok
from dolmen import menu
from zope.interface import Interface
from uvc.layout import interfaces, menus

grok.templatedir('templates')
grok.context(Interface)


class GlobalMenuViewlet(grok.Viewlet):
    grok.viewletmanager(interfaces.IPageTop)
    grok.order(10)

    def render(self):
        self.menu = menus.GlobalMenu(self.context, self.request, self.view)
        self.menu.update()
        return self.menu.render()
    

class PreferencesViewlet(grok.Viewlet):
    grok.name('user-preferences')
    grok.viewletmanager(interfaces.IPageTop)
    grok.order(50)

    def render(self):
        menu = menus.PersonalPreferences(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class DocumentActionsViewlet(grok.Viewlet):
    grok.name('document-actions')
    grok.viewletmanager(interfaces.IAboveContent)
    grok.order(10)

    def update(self):
        self.menu = menus.DocumentActionsMenu(
            self.context, self.request, self.view)
        self.menu.update()


class HelpViewlet(grok.Viewlet):
    grok.name('help')
    grok.viewletmanager(interfaces.IPanels)
    grok.order(20)

    def render(self):
        menu = menus.HelpMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class SidebarViewlet(grok.Viewlet):
    grok.viewletmanager(interfaces.IPanels)
    grok.order(10)

    def render(self):
        menu = menus.SidebarMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()

