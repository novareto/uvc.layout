#!/usr/bin/python
# -*- coding: utf-8 -*-

import martian
import grokcore.viewlet as grok
from dolmen import menu
from uvc.layout.layout import IUVCLayer
from zope.component import queryMultiAdapter
from zope.interface import Interface
from uvc.layout import interfaces
from uvc.layout import libraries
from dolmen.app.layout import Page
from megrok.pagetemplate import PageTemplate, view
from zope.interface import Interface
from zope.component import getMultiAdapter
from zope.security.interfaces import Unauthorized
from zope.security.management import checkPermission
from zope.publisher.interfaces import NotFound
from zope.publisher.interfaces.http import IHTTPRequest
from zope.traversing.interfaces import ITraversable, TraversalError
from zope.contentprovider.interfaces import IContentProvider


grok.templatedir('templates')
grok.context(Interface)


class category(martian.Directive):
    scope = martian.CLASS
    store = martian.ONCE
    validate = martian.validateText


class css(martian.Directive):
    scope = martian.CLASS
    store = martian.ONCE
    validate = martian.validateText


class MenuTraverser(grok.MultiAdapter):
    grok.adapts(grok.View, IHTTPRequest)
    grok.provides(ITraversable)
    grok.name('menu')

    def __init__(self, context, request=None):
        self.context = context
        self.request = request
        self.response = request.response

    def traverse(self, name, ignore=None):
        menu = getMultiAdapter(
            (self.context.context, self.request, self.context),
            IContentProvider, name=name)
        stack = self.request.getTraversalStack()
        if stack:
            category = stack.pop()
            self.request.setTraversalStack(stack)
        else:
            category = None
            
        menu.update()
        if category:
            return MenuCategory(
                self.context.context, self.request, menu, category)
        return MenuOverview(
            self.context.context, self.request, menu)


class MenuCategory(Page):
    grok.context(Interface)

    def __init__(self, context, request, menu, category):
        grok.View.__init__(self, context, request)
        self.menu = menu
        self.category = category

    def render(self):
        return str(self.menu.categories.get(self.category))


class MenuOverview(Page):
    grok.context(Interface)

    def __init__(self, context, request, menu):
        grok.View.__init__(self, context, request)
        self.menu = menu

    def render(self):
        return str(self.menu.categories)
    

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
                yield {'title': name,
                       'menupage': "%s/index/++menu++%s/%s" % (
                           self.context_url, grok.name.bind().get(self), name),
                       'entries': items}

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
