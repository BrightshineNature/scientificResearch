# coding: UTF-8

from adminStaff.models import ProjectSingle


def get_application_year_choice():
    project_group=ProjectSingle.objects.all()
    year = [('-1',u"申请年度")]
    year_has=[]
    for item in project_group:
        year_has.append(item.application_year)
    year_has=list(set(year_has))
    
    for y in year_has:
        year.append((y,y))
    return tuple(year)
def get_approval_year_choice():
    project_group=ProjectSingle.objects.all()
    year = [('-1',u"立项年度")]
    year_has=[]
    for item in project_group:
        year_has.append(item.approval_year)
    year_has=list(set(year_has))
    for y in year_has:
        year.append((y,y))
    return tuple(year)
