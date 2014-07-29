# coding: UTF-8

from django import forms
from django.forms import ModelForm

from adminStaff.models import BasicScientificResearchScoreTable, HumanitiesSocialSciencesResearchScoreTable
from adminStaff.models import MajorProjectScoreTable, KeyLaboratoryProjectScoreTable

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
class HumanitiesSocialSciencesResearchScoreForm(ModelForm):
    class Meta:
        model = HumanitiesSocialSciencesResearchScoreTable
        exclude = ("re_obj", )
        widgets = {"significance": forms.TextInput(attrs={"class": "form-control",}),
                   "innovation": forms.TextInput(attrs={"class": "form-control",}),
                   "feasibility": forms.TextInput(attrs={"class": "form-control",}),
                   "base": forms.TextInput(attrs={"class": "form-control",}),
                  }
class MajorProjectScoreForm(ModelForm):
    class Meta:
        model = MajorProjectScoreTable
        exclude = ("re_obj", )
        widgets = {"evaluation": forms.TextInput(attrs={"class": "form-control",}),
                   "feasibility": forms.TextInput(attrs={"class": "form-control",}),
                   "funds_report": forms.TextInput(attrs={"class": "form-control",}),
                   "expection": forms.TextInput(attrs={"class": "form-control",}),
                   "measures": forms.TextInput(attrs={"class": "form-control",}),
                  }
class KeyLaboratoryProjectScoreForm(ModelForm):
    class Meta:
        model = KeyLaboratoryProjectScoreTable
        exclude = ("re_obj", )
        widgets = {"significance": forms.TextInput(attrs={"class": "form-control",}),
                   "innovation": forms.TextInput(attrs={"class": "form-control",}),
                   "feasibility": forms.TextInput(attrs={"class": "form-control",}),
                   "base": forms.TextInput(attrs={"class": "form-control",}),
                   "funds_report": forms.TextInput(attrs={"class": "form-control",}),
                  }
