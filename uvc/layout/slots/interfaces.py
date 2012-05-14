# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de 

from zope.interface import Interface


class ISubMenu(Interface):
    """ Marker Interface for Sub Menus"""

class IRenderable(Interface):
    """ Marker Interface for MenuItems which render Itself """
