#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import types
import martian
from martian.error import GrokImportError
from martian.util import frame_is_module


class bound_resources(martian.Directive):
    scope = martian.CLASS
    store = martian.ONCE
    default = {}


class bound_resource:
    """Annotates the class for further grokking
    """

    def __init__(self, filepath, type=None, name=None):
        self.filepath = filepath
        self.type = type
        self.name = name

    def __call__(self, decorated):
        frame = sys._getframe(1)
        if not frame_is_module(frame):
            raise GrokImportError(
                "@bound_resource can only be used at the module level")

        if not self.filepath:
            raise GrokImportError(
                "@bound_resource requires at least one argument.")

        if type(decorated) is types.FunctionType:
            raise NotImplementedError(
                'bound_resource can only decorate classes.')

        entries = frame.f_locals.setdefault("__grok_boundresources__", [])
        entries.append((decorated, self.filepath, self.type, self.name))

        return decorated
