import grok

from megrok import resource
from hurry.jquery import jquery


class UVCLayoutResources(resource.Library):
    resource.name('uvc.layout.resources')
    grok.path('resources')


common = resource.ResourceInclusion(
    UVCLayoutResources, 'common.js', depends=[jquery])
