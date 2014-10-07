# coding: UTF-8

import os

from teacher.models import ProjectFundSummary,ProjectFundBudget
from backend.logging import logger, loginfo

def copyFundsummaryToBudget(pid):
    fundsummary = ProjectFundSummary.objects.get(project_id = pid)
    fundbudget = ProjectFundBudget.objects.get(project_id = pid)
    loginfo(p=fundsummary.total_budget,label = "fundsummary")
    loginfo(p=fundbudget.total_budget,label = "fundbudget")
    fundbudget.equcosts_budget = fundsummary.equcosts_budget 
    fundbudget.equacquisition_budget = fundsummary.equacquisition_budget  
    fundbudget.equtrial_budget = fundsummary.equtrial_budget
    fundbudget.equrent_budget = fundsummary.equrent_budget
    fundbudget.material_budget  = fundsummary.material_budget 
    fundbudget.testcosts_budget = fundsummary.testcosts_budget
    fundbudget.fuelpower_budget  = fundsummary.fuelpower_budget 
    fundbudget.travel_budget = fundsummary.travel_budget
    fundbudget.conference_budget  = fundsummary.conference_budget 
    fundbudget.cooperation_budget  = fundsummary.cooperation_budget 
    fundbudget.publish_budget  = fundsummary.publish_budget 
    fundbudget.laborcosts_budget = fundsummary.laborcosts_budget 
    fundbudget.expertadvice_budget = fundsummary.expertadvice_budget
    fundbudget.total_budget = fundsummary.total_budget
    fundbudget.save()

def copyBudgetToFundsummary(pid):
    fundsummary = ProjectFundSummary.objects.get(project_id = pid)
    fundbudget = ProjectFundBudget.objects.get(project_id = pid)
    loginfo(p=fundsummary.total_budget,label = "fundsummary")
    loginfo(p=fundbudget.total_budget,label = "fundbudget")
    fundsummary.equcosts_budget = fundbudget.equcosts_budget 
    fundsummary.equacquisition_budget = fundbudget.equacquisition_budget  
    fundsummary.equtrial_budget = fundbudget.equtrial_budget
    fundsummary.equrent_budget = fundbudget.equrent_budget
    fundsummary.material_budget  = fundbudget.material_budget 
    fundsummary.testcosts_budget = fundbudget.testcosts_budget
    fundsummary.fuelpower_budget  = fundbudget.fuelpower_budget 
    fundsummary.travel_budget = fundbudget.travel_budget
    fundsummary.conference_budget  = fundbudget.conference_budget 
    fundsummary.cooperation_budget  = fundbudget.cooperation_budget 
    fundsummary.publish_budget  = fundbudget.publish_budget 
    fundsummary.laborcosts_budget = fundbudget.laborcosts_budget 
    fundsummary.expertadvice_budget = fundbudget.expertadvice_budget
    fundsummary.total_budget = fundbudget.total_budget
    fundsummary.save()