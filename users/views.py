# coding: UTF-8
'''
Created on 2013-4-03

@author: tianwei

Desc: This module contains views that allow users to submit the calculated
      tasks.
'''
import datetime
import logging
import os
import sys

from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponseForbidden, Http404
from django.template import RequestContext
from django.utils import simplejson
from django.views.decorators import csrf
from django.contrib.auth.decorators import login_required

from backend.logging import logger, loginfo
from backend.decorators import *
from const import *
from users.models import *
from users.forms import *


def base_profile_view(request, authority=None):
    """
        check and load base view
        Arguments:
            In:
                *request, http request
                *authority, CONST lib
            Out: basic profile object or None
    """
    is_auth = check_auth(user=request.user, authority=authority)
    if not is_auth:
        return None
    return None
def get_redirect_urls(request):
    if check_auth(user=request.user, authority=SCHOOL_USER):
        return "/school"
    elif check_auth(user=request.user, authority=COLLEGE_USER):
        return "/college"
    elif check_auth(user=request.user, authority=EXPERT_USER):
        return "/expert"
    elif check_auth(user=request.user, authority=ADMINSTAFF_USER):
        return "/adminStaff"
    elif check_auth(user=request.user, authority=TEACHER_USER):
        return "/teacher"
    else:
        return  "/settings/profile"

@login_required
@csrf.csrf_protect
def profile_view(request):
    """
        Get or Post UserProfile, it will check the user authorities first
    """
    if request.method == "POST":
        return redirect(get_redirect_urls(request))
    else:
        data = {}
        return render(request, "settings/profile.html", data)


@login_required
@csrf.csrf_protect
def admin_account_view(request):
    """
        Set Password
    """
    user = request.user
    if request.method == "POST":
        form = PasswordForm(user, request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data["new_password"])
            user.save()
    else:
        form = PasswordForm(user)
    data = {"form": form}
    return render(request, "settings/admin.html", data)
