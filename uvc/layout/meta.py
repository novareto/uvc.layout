import martian

from megrok.navigation.meta import MenuViewGrokker
from dolmen.forms.base import ApplicationForm
import grok

class FormViewGrokker(MenuViewGrokker):
    martian.component(ApplicationForm)

class ViewletGrokker(MenuViewGrokker):
    martian.component(grok.Viewlet)
