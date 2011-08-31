# -*- coding: utf-8 -*-
# Copyright (c) 2007-2010 NovaReto GmbH
# cklinger@novareto.de 

import grok
import z3c.flashmessage.interfaces
import megrok.pagetemplate as pt

from grok import util
from zope import component, interface

from zeam.form import base
from zeam.form import layout
from dolmen.forms.base import ApplicationForm, apply_data_event
from zeam.form.base.interfaces import ICollection 

import zope.event
import zope.lifecycleevent

from zeam.form.composed import SubForm as BaseSubForm
from zeam.form.composed import ComposedForm
from zeam.form.base.errors import Errors, Error
from zope.schema.interfaces import IField
from zeam.form.ztk.validation import InvariantsValidation
from dolmen.forms import wizard
from uvc.layout.event import AfterSaveEvent
from zeam.form.base.markers import SUCCESS, FAILURE
from dolmen.forms.wizard import MF as _
from zeam.form.base.markers import NO_CHANGE


grok.templatedir('templates')

class Form(ApplicationForm):
    """ Base Class form ZEAM-FORM"""
    grok.baseclass()
    grok.require('uvc.AddContent')
    #grok.context(interface.Interface)

    @property
    def id(self):
        return self.prefix + '-' + self.__class__.__name__.lower()

    @property
    def formErrors(self):
        error = self.errors.get(self.prefix, None)
        if error is None or ICollection.providedBy(error):
            return error
        return [error]


class GroupForm(ComposedForm, Form):
    grok.baseclass()



class MyNextAction(wizard.actions.NextAction):
    """Action to move to the next step.
    """
    def __call__(self, form):
        if form.current.actions['save'](form.current) is SUCCESS:
            step = form.getCurrentStepId()
            z = 1
            if hasattr(form.current, 'next_navigation'):
                data, errors = form.current.extractData()
                z=form.current.next_navigation(data)
            form.setCurrentStep(step + z)
            return SUCCESS
        return FAILURE


class MyPreviousAction(wizard.actions.PreviousAction):
    """Action to move to the previous step.
    """

    def __call__(self, form):
        step = form.getCurrentStepId()
        z = 1
        if hasattr(form.current, 'prev_navigation'):
            z = form.current.prev_navigation()
        form.setCurrentStep(step - z)
        return SUCCESS



class MySaveAction(wizard.actions.SaveAction):
    def __call__(self, form):
        if form.current.actions['save'](form.current) is SUCCESS:
            if super(MySaveAction, self).__call__(form) is SUCCESS:
                grok.notify(AfterSaveEvent(form.context, form.request))
                form.redirect(form.url(self.redirect_url))
            return SUCCESS
        return FAILURE


class MyHiddenSaveAction(wizard.actions.HiddenSaveAction):

    def applyData(self, form, content, data):
        for field in form.fields:
            value = data.getWithDefault(field.identifier)
            if value is not NO_CHANGE:
                content.set(field.identifier, value)
            #elif value is _marker:
            #    content.set(field.identifier, None)

class Wizard(wizard.Wizard, Form):
    grok.baseclass()

    actions = base.Actions(
        MyPreviousAction(_(u"Zurück"), identifier="back"),
        MySaveAction(_(u"Speichern")),
        MyNextAction(_(u"Weiter")))    


class Step(wizard.WizardStep, Form):
    grok.baseclass()

    actions = base.Actions(
        MyHiddenSaveAction(u'HiddenEdit', identifier="save"))

    def validateStep(self, data, errors):
        return False

    def validateData(self, fields, data, errors):
        super(Step, self).validateData(fields, data, errors)
        self.validateStep(data, errors)
        return errors


class AddForm(Form):
    grok.baseclass()
    _finishedAdd = False 

    @base.action(u'Hinzufügen')
    def handleAdd(self):
        data, errors = self.extractData()
        if errors:
            self.flash('Es sind Fehler aufgetreten')
            return
        obj = self.createAndAdd(data)
        if obj is not None:
            # mark only as finished if we get the new object
            self._finishedAdd = True
            grok.notify(AfterSaveEvent(obj, self.request))

    def createAndAdd(self, data):
        obj = self.create(data)
        zope.event.notify(zope.lifecycleevent.ObjectCreatedEvent(obj))
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


class SubForm(BaseSubForm):
    grok.baseclass()


class FormTemplate(pt.PageTemplate):
    """Template for a layout aware form.
    """
    pt.view(Form)

from dolmen.app.layout import Form as DAForm
class DAFormTemplate(pt.PageTemplate):
    """Template for a layout aware form.
    """
    template = grok.PageTemplateFile('templates/formtemplate.pt')
    pt.view(DAForm)


class AddFormTemplate(pt.PageTemplate):
    """Template for a layout aware form.
    """
    template = grok.PageTemplateFile('templates/formtemplate.pt')
    pt.view(AddForm)


class SubFormTemplate(pt.PageTemplate):
    """Template for a layout aware form.
    """
    template = grok.PageTemplateFile('templates/subformtemplate.pt')
    pt.view(SubForm)


class ComposedFormTemplate(pt.PageTemplate):
    """Template for a layout aware form.
    """
    template = grok.PageTemplateFile('templates/composedformtemplate.pt')
    pt.view(GroupForm)


class WizardTemplate(pt.PageTemplate):
    """Template for a layout aware form.
    """
    template = grok.PageTemplateFile('templates/wizardtemplate.pt')
    pt.view(Wizard)
