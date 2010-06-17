import martian
import os.path
from zope.browserresource.metaconfigure import resource
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from uvc.layout.directives import bound_resources


class BoundResourcesGrokker(martian.GlobalGrokker):

    def grok(self, name, module, module_info, config, **kw):
        entries = module_info.getAnnotation('grok.boundresources', [])
       
        for factory, filepath, atype, name in entries:
            filepath = module_info.getResourcePath(filepath)
            resource(config, name, layer=IDefaultBrowserLayer,
                     permission='zope.Public', file=filepath)
            current = bound_resources.bind({}).get(factory)
            current[name] = '/@@/++resource++' + name
            bound_resources.set(factory, current)
        return True
