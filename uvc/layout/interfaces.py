# -*- coding: utf-8 -*-

from cromlech.browser import ISlot


class IPageTop(ISlot):
    """Marker For the area that sits at the top of the page.
    """


class ITabs(ISlot):
    """Marker for the action tabs.
    """
    

class IAboveContent(ISlot):
    """Marker For the area that sits above the page body.
    """


class IBelowContent(ISlot):
    """Marker For the area that sits under the page body.
    """


class IHeaders(ISlot):
    """Marker For Headers
    """


class IToolbar(ISlot):
    """Marker for Toolbar
    """


class IDocumentActions(ISlot):
    """Marker for DocumentActions
    """


class IPersonalPreferences(ISlot):
    """Marker for PersonalPreferences
    """


class IGlobalMenu(ISlot):
    """Marker for GlobalMenu
    """


class IPersonalMenu(ISlot):
    """Marker for PersonalMenu
    """


class ISidebar(ISlot):
    """Marker for Sitebar
    """


class IFooter(ISlot):
    """Marker for Footer
    """


class IPanels(ISlot):
    """Marker interface for the panels display.
    """


class IHelp(ISlot):
    """Marker for Help
    """


class IExtraInfo(ISlot):
    """Marker for ExtraInfo in Forms
    """


class IExtraViews(ISlot):
    """Marker for additional Views for Folders
       Objects etc...
    """

class ISpotMenu(ISlot):
    """ Special Menu """


class IBeforeActions(ISlot):
    """ Marker Interface"""
