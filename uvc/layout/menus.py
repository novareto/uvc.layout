#!/usr/bin/python
# -*- coding: utf-8 -*-

import martian
import grokcore.viewlet as grok
from dolmen import menu
from zope.component import queryMultiAdapter
from zope.interface import Interface
from uvc.layout import interfaces
from uvc.layout import libraries
from megrok.pagetemplate import PageTemplate, view

grok.templatedir('templates')
grok.context(Interface)


class category(martian.Directive):
    scope = martian.CLASS
    store = martian.ONCE
    validate = martian.validateText


class GlobalMenu(menu.Menu):
    grok.name("uvc.global.menu")
    grok.implements(interfaces.IGlobalMenu)

    categories = None

    css = ['blue', 'orange', 'violet', 'green', 'brown', 'purple']

    def getClass(self, index):
        return self.css[index]


    def get_categories(self):
        if self.categories is not None:
            for name, items in self.categories.items():
                yield {'title': name, 'entries': items}

    def sort_by_keyword(self):
        categories = {}
        for viewlet in self.viewlets:
            name = category.bind('Info').get(viewlet)
            cat = categories.get(name)
            if cat is None:
                cat = categories[name] = []
            cat.append(viewlet)
        return categories

    def update(self):
        libraries.dropdown_js.need()
        menu.Menu.update(self)
        self.categories = self.sort_by_keyword()


class PersonalMenu(menu.Menu):
    grok.name("uvc.user.menu")
    grok.implements(interfaces.IPersonalMenu)
    

class PersonalPreferences(menu.Menu):
    grok.name("uvc.user.preferences")
    grok.implements(interfaces.IPersonalPreferences)


class Dropdowns(PageTemplate):
    view(GlobalMenu)


class HelpMenu(menu.Menu):
    grok.name("uvc.user.help")
    grok.title("Hilfe")
    grok.implements(interfaces.IHelp)


class DocumentActionsMenu(menu.Menu):
    grok.name("uvc.user.documentactions")
    grok.implements(interfaces.IDocumentActions)


class Footer(menu.Menu):
    grok.name('uvcsite.footer')
    grok.implements(interfaces.IFooter)
    grok.require('zope.View')


class SidebarMenu(menu.Menu):
    grok.name('uvc.user.sidebar')
    grok.title('Navigation')
    grok.implements(interfaces.ISidebar)
