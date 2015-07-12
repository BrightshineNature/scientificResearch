# coding: UTF-8

from django import forms
from django.forms import ModelForm

from adminStaff.models import BasicScientificResearchScoreTable, HumanitiesSocialSciencesResearchScoreTable
from adminStaff.models import MajorProjectScoreTable, KeyLaboratoryProjectScoreTable
from adminStaff.models import ScienceFoundationResearchScoreTable
from adminStaff.models import FrontAndIntercrossResreachScoreTable
from adminStaff.models import FrontAndIntercrossResreachFinalScoreTable
from adminStaff.models import OutstandingYoungResreachScoreTable

class ScienceFoundationResearchScoreForm(ModelForm):
    class Meta:
        model = ScienceFoundationResearchScoreTable
        exclude = ("re_obj", )
        widgets = {"check": forms.TextInput(attrs={"class": "form-control",}),
                   "score": forms.TextInput(attrs={"class": "form-control",}),
                  }

class FrontAndIntercrossResreachScoreForm(ModelForm):
    class Meta:
        model = FrontAndIntercrossResreachScoreTable
        exclude = ("re_obj", )
        widgets = {"score": forms.TextInput(attrs={"class": "form-control",}),
                   "level": forms.Select(attrs={"class": "form-control",}),
                  }

class FrontAndIntercrossResreachFinalScoreForm(ModelForm):
    class Meta:
        model = FrontAndIntercrossResreachFinalScoreTable
        exclude = ("re_obj", )
        widgets = {"score": forms.TextInput(attrs={"class": "form-control",}),
                   "level": forms.TextInput(attrs={"class": "form-control",}),
                  }

class OutstandingYoungResreachScoreForm(ModelForm):
    class Meta:
        model = OutstandingYoungResreachScoreTable
        exclude = ("re_obj", )
        widgets = {"score": forms.TextInput(attrs={"class": "form-control",}),
                   "level": forms.Select(attrs={"class": "form-control",}),
                  }


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
