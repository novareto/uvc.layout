# -*- coding: utf-8 -*-

from zope.interface import Interface
from uvc.entities.browser.managers import *


class IToolbar(Interface):
    """Marker for Toolbar
    """


class IDocumentActions(Interface):
    """Marker for DocumentActions
    """


class IQuickLinks(Interface):
    """Marker for Qucklinks
    """


class IPersonalPreferences(Interface):
    """Marker for PersonalPreferences
    """


class IGlobalMenu(Interface):
    """Marker for GlobalMenu
    """


class IPersonalMenu(Interface):
    """Marker for PersonalMenu
    """


class ISidebar(Interface):
    """Marker for Sitebar
    """


class IPanels(Interface):
    """Marker interface for the panels display.
    """


class IHelp(Interface):
    """Marker for Help
    """


class IExtraInfo(Interface):
    """Marker for ExtraInfo in Forms
    """


class IExtraViews(Interface):
    """Marker for additional Views for Folders
       Objects etc...
    """

class ISpotMenu(Interface):
    """ Special Menu """


class IBeforeActions(Interface):
    """ Marker Interfae"""
