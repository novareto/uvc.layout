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
import megrok.pagetemplate as pt

from megrok import navigation

grok.templatedir('templates')
grok.context(Interface)


### SubMenu
class SubMenu(navigation.Menu):
    grok.baseclass()


class SubMenuTemplate(pt.PageTemplate):
    pt.view(SubMenu)


### GlobalMenu
class GlobalMenu(navigation.Menu):
    grok.name("uvc.global.menu")
    grok.implements(interfaces.IGlobalMenu)

    def update(self):
        super(GlobalMenu, self).update()
        libraries.dropdown_js.need()

    css = ['blue', 'violet', 'green', 'brown', 'purple', 'orange']

    def getClass(self, index):
        css = self.css*3
        return css[index-1]


class GlobalMenuTemplate(pt.PageTemplate):
    pt.view(GlobalMenu)


## DocumentActionsMenu
class DocumentActionsMenu(navigation.Menu):
    grok.name("uvc.user.documentactions")
    grok.implements(interfaces.IDocumentActions)


class DocumentActionsTemplate(pt.PageTemplate):
    pt.view(DocumentActionsMenu)


### Footer Menu
class Footer(navigation.Menu):
    grok.name('uvcsite.footer')
    grok.implements(interfaces.IFooter)
    grok.require('zope.View')


class FooterTemplate(pt.PageTemplate):
    pt.view(Footer)


### PersonalMenu
class PersonalMenu(navigation.Menu):
    grok.name("uvc.user.menu")
    grok.implements(interfaces.IPersonalMenu)
    

### PersonalPreferences
class PersonalPreferences(navigation.Menu):
    grok.name("uvc.user.preferences")
    grok.implements(interfaces.IPersonalPreferences)


class PersonalPreferencesTemplate(pt.PageTemplate):
    pt.view(PersonalPreferences)


### ExtraViews
class ExtraViews(navigation.Menu):
    grok.title(u'View as')
    grok.name("uvc.extraviews")
    grok.description(u"Alternative content views")
    grok.implements(interfaces.IExtraViews)
    menu_class = "extra-views dropdown"

    id = "extraviews"
    title = "Ansichten"
