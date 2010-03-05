#!/usr/bin/python
# -*- coding: utf-8 -*-

import grokcore.viewlet as grok
from dolmen import menu
from zope.component import queryMultiAdapter
from zope.interface import Interface
from uvc.layout import interfaces

grok.templatedir('templates')
grok.context(Interface)


class GlobalMenu(menu.Menu):
    grok.name("uvc.global.menu")
    grok.implements(interfaces.IGlobalMenu)

    css = ['blue', 'orange', 'violet', 'green', 'brown', 'purple']
    
    def getClass(self, index):
        return self.css[index]


class PersonalMenu(menu.Menu):
    grok.name("uvc.user.menu")
    grok.implements(interfaces.IPersonalMenu)
    

class PersonalPreferences(menu.Menu):
    grok.name("uvc.user.preferences")
    grok.implements(interfaces.IPersonalPreferences)


class SidebarMenu(menu.Menu):
    grok.name("uvc.user.sidebar")
    grok.implements(interfaces.ISidebar)


class HelpMenu(menu.Menu):
    grok.name("uvc.user.help")
    grok.implements(interfaces.IHelp)


class DocumentActionsMenu(menu.Menu):
    grok.name("uvc.user.documentactions")
    grok.implements(interfaces.IFooter)


class GlobalMenuViewlet(grok.Viewlet):
    grok.viewletmanager(interfaces.IPageTop)
    grok.order(10)

    css = ['blue', 'orange', 'violet', 'green', 'brown', 'purple']

    def getClass(self, index):
        return self.css[index]

    def update(self):
        self.menu = GlobalMenu(self.context, self.request, self.view)
        self.menu.update()
    

class PreferencesViewlet(grok.Viewlet):
    grok.viewletmanager(interfaces.IPageTop)
    grok.order(50)

    def render(self):
        menu = PersonalPreferences(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class DocumentActionsViewlet(grok.Viewlet):
    grok.viewletmanager(interfaces.IAboveContent)
    grok.order(10)

    def render(self):
        menu = DocumentActionsMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class SidebarViewlet(grok.Viewlet):
    grok.viewletmanager(interfaces.IPanels)
    grok.order(10)

    def render(self):
        menu = SidebarMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class HelpViewler(grok.Viewlet):
    grok.viewletmanager(interfaces.IPanels)
    grok.order(20)

    def render(self):
        menu = HelpMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()
