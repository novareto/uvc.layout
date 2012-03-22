# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de 

import grok

from zope.interface import Interface
from uvc.layout.slots.interfaces import ISubMenu


class Menu(grok.ViewletManager):
    grok.baseclass()
    grok.context(Interface)

    def getMenuItems(self):
        rc = []
        self.update()
        for viewlet in self.viewlets:
            submenuitems = []
            if ISubMenu.providedBy(viewlet):
                submenu = viewlet
                submenu.update()
                for submenuitem in submenu.viewlets:
                    submenuitems.append(dict(
                        title = submenuitem.title or grok.title.bind().get(submenuitem),
                        id = submenuitem.__class__.__name__.lower(),
                        description = grok.description.bind().get(submenuitem),
                        selected = submenuitem.selected,
                        icon = submenuitem.icon,
                        action = submenuitem.action))
            submenuitems.reverse()
            rc.append(dict(
                title = viewlet.title or grok.title.bind().get(viewlet),
                id = viewlet.__class__.__name__.lower(),
                description = grok.description.bind().get(viewlet),
                selected = viewlet.selected,
                icon = viewlet.icon,
                submenu = submenuitems,
                action = viewlet.action))
        rc.reverse()
        return rc


class MenuItem(grok.Viewlet):
    grok.baseclass()
    grok.context(Interface)

    title = ""
    action = ""
    icon = ""

    @property
    def selected(self):
        request_url = self.request.getURL()
        normalized_action = self.action
        if self.action.startswith('@@'):
            normalized_action = self.action[2:]
        if request_url.endswith('/'+normalized_action):
            return True
        if request_url.endswith('/++view++'+normalized_action):
            return True
        if request_url.endswith('/@@'+normalized_action):
            return True
        if request_url == self.action:
            return True
        if request_url.endswith('/@@index'):
            if request_url[:-8] == self.action:
                return True
        return False

    def render(self):
        return u""


class SubMenu(MenuItem, grok.ViewletManager):
    grok.baseclass()
    grok.implements(ISubMenu)

    def update(self):
        grok.ViewletManager.update(self)
