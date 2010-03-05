# -*- coding: utf-8 -*-

import megrok.pagetemplate as pt
from grokcore.view import layer
from uvc.skin.skin import IUVCSkin
from z3c.form.interfaces import IInputForm
from dolmen.app.layout.models import DefaultView


class DisplayTemplate(pt.PageTemplate):
    """The basic template for a display form.
    """
    layer(IUVCSkin)
    pt.view(DefaultView)


class InputTemplate(pt.PageTemplate):
    """The basic template for an input form.
    """
    layer(IUVCSkin)
    pt.view(IInputForm)
