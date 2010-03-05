#!/usr/bin/python
# -*- coding: utf-8 -*-

import grokcore.viewlet as grok
from dolmen import menu
from zope.component import queryMultiAdapter
from zope.interface import Interface
from uvc.layout.interfaces import (
    IPersonalPreferences, IGlobalMenu, IPersonalMenu, IPageTop, IFooter, ISidebar, IAboveContent)

grok.templatedir('templates')
grok.context(Interface)


class GlobalMenu(menu.Menu):
    grok.name("uvc.global.menu")
    grok.implements(IGlobalMenu)

    css = ['blue', 'orange', 'violet', 'green', 'brown', 'purple']

    def getClass(self, index):
        return self.css[index]


class PersonalMenu(menu.Menu):
    grok.name("uvc.user.menu")
    grok.implements(IPersonalMenu)
    

class PersonalPreferences(menu.Menu):
    grok.name("uvc.user.preferences")
    grok.implements(IPersonalPreferences)


class SidebarMenu(menu.Menu):
    grok.name("uvc.user.sidebar")
    grok.implements(ISidebar)


class FooterMenu(menu.Menu):
    grok.name("uvc.user.footer")
    grok.implements(IFooter)


class DocumentActionsMenu(menu.Menu):
    grok.name("uvc.user.documentactions")
    grok.implements(IFooter)



class GlobalMenuViewlet(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(IPageTop)
    grok.order(10)

    def render(self):
        menu = GlobalMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()
    

class PreferencesViewlet(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(IPageTop)
    grok.order(50)

    def render(self):
        menu = PersonalPreferences(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class SidebarViewlet(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(ISidebar)
    grok.order(50)

    def render(self):
        menu = SidebarMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class FooterViewlet(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(IFooter)
    grok.order(10)

    def render(self):
        menu = FooterMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()


class DocumentActionsViewlet(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(IAboveContent)
    grok.order(10)

    def render(self):
        menu = DocumentActionsMenu(self.context, self.request, self.view)
        menu.update()
        return menu.render()
