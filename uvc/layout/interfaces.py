# -*- coding: utf-8 -*-

from zope.interface import Interface
from grok.interfaces import IContainer


class IHeaders(Interface):
    """ Marker For Headers"""


class IToolbar(Interface):
    """ Marker for Toolbar"""


class IGlobalMenu(Interface):
    """ Marker for GlobalMenu"""


class ISidebar(Interface):
    """ Marker for Sitebar"""


class IFooter(Interface):
    """ Marker for Footer"""


class ILogo(Interface):
    """ Marker for Logo"""


class IPersonalMenu(Interface):
    """ Marker for PersonalMenu """


class IStatusMessage(Interface):
    """ Marker for StatusMessage """


class IHelp(Interface):
    """ Marker for Help """


class IPersonalPreferences(Interface):
    """ Marker for Personal Preferences """


class IBreadCrumb(Interface):
    """ Marker for Breadcrumbs"""


class IDocumentActions(Interface):
    """ Marker for Breadcrumbs"""
