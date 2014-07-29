# coding: UTF-8

from django import forms
from django.forms import ModelForm

from adminStaff.models import BasicScientificResearchScoreTable

class BasicScientificResearchScoreForm(ModelForm):
    class Meta:
        model = BasicScientificResearchScoreTable
        exclude = ("re_obj", )
        widgets = {"summary": forms.TextInput(attrs={"class": "form-control",}),
                   "completion": forms.TextInput(attrs={"class": "form-control",}),
                   "achievement": forms.TextInput(attrs={"class": "form-control",}),
                   "prospect": forms.TextInput(attrs={"class": "form-control",}),
                   "funds_report": forms.TextInput(attrs={"class": "form-control",}),
                  }
