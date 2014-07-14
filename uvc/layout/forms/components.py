# -*- coding: utf-8 -*-
# Copyright (c) 2007-2011 NovaReto GmbH
# cklinger@novareto.de

import uvclight
import zope.lifecycleevent

from dolmen.forms import base
from dolmen.forms import wizard
from dolmen.forms.base import Form as BaseForm
from dolmen.forms.base.markers import NO_CHANGE
from dolmen.forms.base.markers import SUCCESS, FAILURE
from dolmen.forms.composed import ComposedForm
from dolmen.forms.composed import SubForm as BaseSubForm
from dolmen.forms.wizard import MF as _
from uvc.layout.forms.event import AfterSaveEvent
from zope.interface import Interface


class Form(BaseForm):
    uvclight.baseclass()
    legend = ""

    @property
    def id(self):
        return self.prefix + '-' + self.__class__.__name__.lower()


class AddForm(Form):
    uvclight.baseclass()
    uvclight.require('uvc.AddContent')
    _finishedAdd = False

    @base.action(u'Speichern', identifier="uvcsite.add")
    def handleAdd(self):
        data, errors = self.extractData()
        if errors:
            self.flash('Es sind Fehler aufgetreten')
            return
        obj = self.createAndAdd(data)
        if obj is not None:
            # mark only as finished if we get the new object
            self._finishedAdd = True
            uvclight.notify(AfterSaveEvent(obj, self.request))

    def createAndAdd(self, data):
        obj = self.create(data)
        uvclight.notify(zope.lifecycleevent.ObjectCreatedEvent(obj))
        self.add(obj)
        return obj

    def create(self, data):
        raise NotImplementedError

    def add(self, object):
        raise NotImplementedError

    def nextURL(self):
        raise NotImplementedError

    def render(self):
        if self._finishedAdd:
            self.request.response.redirect(self.nextURL())
            return ""
        return super(AddForm, self).render()


class SubForm(BaseSubForm, Form):
    uvclight.baseclass()


class GroupForm(ComposedForm, Form):
    uvclight.baseclass()

## #
## ### Wizard
## #

## class MyNextAction(wizard.actions.NextAction):
##     """Action to move to the next step.
##     """

##     def __call__(self, form):
##         if form.current.actions['save'](form.current) is SUCCESS:
##             step = form.getCurrentStepId()
##             z = 1
##             if hasattr(form.current, 'next_navigation'):
##                 data, errors = form.current.extractData()
##                 z=form.current.next_navigation(data)
##             form.setCurrentStep(step + z)
##             return SUCCESS
##         return FAILURE


## class MyPreviousAction(wizard.actions.PreviousAction):
##     """Action to move to the previous step.
##     """

##     def __call__(self, form):
##         step = form.getCurrentStepId()
##         z = 1
##         if hasattr(form.current, 'prev_navigation'):
##             z = form.current.prev_navigation()
##         form.setCurrentStep(step - z)
##         return SUCCESS


## class MySaveAction(wizard.actions.SaveAction):
##     def __call__(self, form):
##         if form.current.actions['save'](form.current) is SUCCESS:
##             if super(MySaveAction, self).__call__(form) is SUCCESS:
##                 uvclight.notify(AfterSaveEvent(form.context, form.request))
##                 form.redirect(form.url(self.redirect_url))
##             return SUCCESS
##         return FAILURE


class Wizard(wizard.Wizard, Form):
     uvclight.baseclass()

#     actions = base.Actions(
#         MyPreviousAction(_(u"Zurück"), identifier="back"),
#         MySaveAction(_(u"Speichern")),
#         MyNextAction(_(u"Weiter")))


## class MyHiddenSaveAction(wizard.actions.HiddenSaveAction):

##     def applyData(self, form, content, data):
##         for field in form.fields:
##             value = data.getWithDefault(field.identifier)
##             if value is not NO_CHANGE:
##                 content.set(field.identifier, value)
##         return SUCCESS


## class Step(wizard.WizardStep, Form):
##     uvclight.baseclass()

##     actions = base.Actions(
##         MyHiddenSaveAction(u'HiddenEdit', identifier="save"))

##     def validateStep(self, data, errors):
##         return False

##     def validateData(self, fields, data):
##         errors = super(Step, self).validateData(fields, data)
##         self.validateStep(data, errors)
##         return errors
