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


class PersonalMenu(menu.Menu):
    grok.name("uvc.user.menu")
    grok.implements(interfaces.IPersonalMenu)
    

class PersonalPreferences(menu.Menu):
    grok.name("uvc.user.preferences")
    grok.implements(interfaces.IPersonalPreferences)


class SidebarMenu(menu.Menu):
    grok.name("uvc.user.sidebar")
    grok.title("Navigation")
    grok.implements(interfaces.ISidebar)


class HelpMenu(menu.Menu):
    grok.name("uvc.user.help")
    grok.implements(interfaces.IHelp)


class DocumentActionsMenu(menu.Menu):
    grok.name("uvc.user.documentactions")
    grok.implements(interfaces.IDocumentActions)
