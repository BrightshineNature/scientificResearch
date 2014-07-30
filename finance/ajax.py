# coding: UTF-8
import os, sys,pickle
from django.shortcuts import get_object_or_404
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from django.utils import simplejson
from django.template.loader import render_to_string
from backend.logging import loginfo

from common.views import get_search_data
from common.forms import ScheduleBaseForm
@dajaxice_register
def ExportExcel(request,form,category):
    schedule_form = ScheduleBaseForm(deserialize_form(form))
    pro_list=get_search_data(schedule_form)
    loginfo(pro_list.count())
    return simplejson.dumps({"status": "ok", })
