# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 


from fanstatic import Library, Resource
from js.jquery import jquery


library = Library('uvc.layout.resources', 'resources')


common = Resource(library, 'common.js', depends=[jquery])

dropdown_js = Resource(library, 'dropdown.js', depends=[jquery])

dropdown = Resource(library, 'dropdown.css', depends=[jquery, dropdown_js])
