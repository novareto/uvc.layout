# -*- coding: utf-8 -*-

from megrok import navigation
from zope.interface import Interface


class IPageTop(Interface):
    """Marker For the area that sits at the top of the page.
    """


class IAboveContent(Interface):
    """Marker For the area that sits above the page body.
    """


class IBelowContent(Interface):
    """Marker For the area that sits under the page body.
    """


class IHeaders(Interface):
    """Marker For Headers
    """


class IToolbar(Interface):
    """Marker for Toolbar
    """


class IDocumentActions(navigation.interfaces.IMenu):
    """Marker for DocumentActions
    """


class IPersonalPreferences(navigation.interfaces.IMenu):
    """Marker for PersonalPreferences
    """


class IGlobalMenu(navigation.interfaces.IMenu):
    """Marker for GlobalMenu
    """


class IPersonalMenu(navigation.interfaces.IMenu):
    """Marker for PersonalMenu
    """


class ISidebar(Interface):
    """Marker for Sitebar
    """


class IFooter(navigation.interfaces.IMenu):
    """Marker for Footer
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
