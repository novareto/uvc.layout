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
from uvc.layout.directives import bound_resources
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

    def factory(self, title, url, dropdown=True):
        return dict(title = title, url = url, dropdown=dropdown) 


class icon(martian.Directive):
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
        app_url = self.view.application_url() +'/'
        if self.categories is not None:
            for name, item in self.categories.items():
                yield {'title': name, 'url': app_url + item['url'], 'entries': item['items'], 'dropdown': item['dropdown']}

    def sort_by_keyword(self):
        categories = {}
        print self.viewlets
        for i, viewlet in enumerate(self.viewlets):
            name = category.bind(dict(title='Info', url='/')).get(viewlet)
            cat = categories.get(name.get('title'))
            if cat is None:
                cat = categories[name.get('title')] = dict(url=name.get('url'), dropdown=name.get('dropdown', True), items=[], order=i)
            cat['items'].append(viewlet)
        #dd = [{key:categories[key]} for key in sorted(categories, key=lambda s: categories[s]['order'])]
        #import pdb; pdb.set_trace() 
        #return [{key:categories[key]} for key in sorted(categories, key=lambda s: categories[s]['order'])][0]
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

class PersonalPreferencesTemplate(PageTemplate):
    view(PersonalPreferences)

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
