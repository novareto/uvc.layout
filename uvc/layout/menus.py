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
    

class PreferencesViewlet(PersonalPreferences):
    grok.name('user-preferences')
    grok.viewletmanager(interfaces.IPageTop)
    grok.order(50)

    def __init__(self, context, request, view, manager):
        PersonalPreferences.__init__(self, context, request, view)
 

class DocumentActionsViewlet(DocumentActionsMenu):
    grok.name('document-actions')
    grok.viewletmanager(interfaces.IAboveContent)
    grok.order(10)

    def __init__(self, context, request, view, manager):
        DocumentActionsMenu.__init__(self, context, request, view)


class SidebarViewlet(SidebarMenu):
    grok.name('sidebar')
    grok.viewletmanager(interfaces.IPanels)
    grok.order(10)

    def __init__(self, context, request, view, manager):
        SidebarMenu.__init__(self, context, request, view)


class HelpViewler(HelpMenu):
    grok.name('help')
    grok.viewletmanager(interfaces.IPanels)
    grok.order(20)

    def __init__(self, context, request, view, manager):
        HelpMenu.__init__(self, context, request, view)
