import martian

from megrok.navigation.meta import MenuViewGrokker
from dolmen.forms.base import ApplicationForm


class FormViewGrokker(MenuViewGrokker):
    martian.component(ApplicationForm)
