#!/usr/bin/python
# -*- coding: utf-8 -*-

import grokcore.viewlet as grok
from dolmen import menu
from zope.component import queryMultiAdapter
from zope.interface import Interface
from uvc.layout.interfaces import (
    IPersonalPreferences, IGlobalMenu, IPersonalMenu, IPageTop)

grok.templatedir('templates')
grok.context(Interface)


class GlobalMenu(grok.ViewletManager):
    grok.name("uvc.global.menu")
    grok.implements(IGlobalMenu)

    css = ['blue', 'orange', 'violet', 'green', 'brown', 'purple']

    def getClass(self, index):
        return self.css[index]


class PersonalMenu(grok.ViewletManager):
    grok.name("uvc.user.menu")
    grok.implements(IPersonalMenu)
    

class PersonalPreferences(grok.ViewletManager):
    grok.name("uvc.user.preferences")
    grok.implements(IPersonalPreferences)


class TopMenus(grok.Viewlet):
    grok.context(Interface)
    grok.viewletmanager(IPageTop)
    grok.order(10)

    def update(self):
        self.menus = []
        discriminants = (self.context, self.request, self.view)
        menus = ['uvc.global.menu', 'uvc.user.menu', 'uvc.user.preferences']
        for menu in menus:
            manager = queryMultiAdapter(discriminants, name=menu)
            if manager is not None:
                manager.update()
                self.menus.append(manager.render())

    def render(self):
        return u"".join(self.menus)
    
