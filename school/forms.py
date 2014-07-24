# coding: UTF-8

from django import forms
from users.models import College, Special

class FilterForm(forms.Form):
    college_list = College.objects.all()
    COLLEGE_CHOICE = [(-1, "所有学院")]
    COLLEGE_CHOICE.extend([(college.id, college.name) for college in college_list])
    COLLEGE_CHOICE = tuple(COLLEGE_CHOICE)
    colleges = forms.ChoiceField(required = True, choices = COLLEGE_CHOICE, widget = forms.Select(attrs = {"class": "form-control",}))

    SPECIAL_CHOICE = tuple((special.id, special.name) for special in Special.objects.all())
    specials = forms.ChoiceField(required = True, choices = SPECIAL_CHOICE, widget = forms.Select(attrs = {"class": "form-control",}))

    def __init__(self, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        college_list = College.objects.all()
        COLLEGE_CHOICE = [(-1, "所有学院")]
        COLLEGE_CHOICE.extend([(college.id, college.name) for college in college_list])
        COLLEGE_CHOICE = tuple(COLLEGE_CHOICE)

        self.fields["colleges"].choices = COLLEGE_CHOICE
       
        SPECIAL_CHOICE = tuple((special.id, special.name) for special in Special.objects.all())
        specials = forms.ChoiceField(required = True, choices = SPECIAL_CHOICE, widget = forms.Select(attrs = {"class": "form-control",}))


