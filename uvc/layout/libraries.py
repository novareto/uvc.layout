import grok

from megrok import resource
from hurry.jquery import jquery


class UVCLayoutResources(resource.Library):
    resource.name('uvc.layout.resources')
    grok.path('resources')


common = resource.ResourceInclusion(
    UVCLayoutResources, 'common.js', depends=[jquery])

dropdown_js = resource.ResourceInclusion(
    UVCLayoutResources, 'dropdown.js', depends=[jquery])

dropdown = resource.ResourceInclusion(
    UVCLayoutResources, 'dropdown.css', depends=[jquery, dropdown_js])
