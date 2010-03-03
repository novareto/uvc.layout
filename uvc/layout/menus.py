#!/usr/bin/python
# -*- coding: utf-8 -*-

import grokcore.viewlet as grok
from dolmen import menu
from zope.interface import Interface
from uvc.layout.interfaces import (
    IPersonalPreferences, IGlobalMenu, IPersonalMenu, IPageTop)

grok.templatedir('templates')
grok.context(Interface)


class GlobalMenu(grok.ViewletManager):
    grok.name("uvc.global.menu")
    grok.implements(IGlobalMenu)


class PersonalMenu(grok.ViewletManager):
    grok.name("uvc.user.menu")
    grok.implements(IPersonalMenu)
    

class PersonalPreferences(grok.ViewletManager):
    grok.name("uvc.user.preference")
    grok.implements(IPersonalPreferences)
