# -*- coding: utf-8 -*-

from zope.interface import Interface


class IAboveContent(Interface):
    """Marker For Headers
    """


class IHeaders(Interface):
    """Marker For Headers
    """


class IToolbar(Interface):
    """Marker for Toolbar
    """


class IGlobalMenu(Interface):
    """Marker for GlobalMenu
    """


class ISidebar(Interface):
    """Marker for Sitebar
    """


class IFooter(Interface):
    """Marker for Footer
    """


class IHelp(Interface):
    """Marker for Help
    """
