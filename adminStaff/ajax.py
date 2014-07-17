# coding: UTF-8
import os, sys,pickle
from django.shortcuts import get_object_or_404
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.utils import simplejson
from django.template.loader import render_to_string

from adminStaff.forms import NewsForm, SpecialForm, CollegeForm,TemplateNoticeMessageForm
from django import  forms
from adminStaff.models import Special

@dajaxice_register
def saveSpecialName(request, form):
    form = SpecialForm(deserialize_form(form))
    
    if form.is_valid():
        print form.cleaned_data['name']
        p = Special(name= form.cleaned_data['name'])
        p.save()


    return simplejson.dumps({'status':'1', 'res':"res"})