# coding: UTF-8
import xlwt
import os,sys
import datetime
from backend.logging import loginfo
from users.models import TeacherProfile
from teacher.models import TeacherInfoSetting
from adminStaff.models import ProjectSingle,Re_Project_Expert
from common.utils import getScoreTable
from settings import TMP_FILES_PATH,MEDIA_URL
from const import EXPERT_NUM

def get_xls_path(request,exceltype,proj_set,specialtype=""):
    """
        exceltype = info_collection info_basesummary_preview info_humanity_preview              
                    info_importantproject_preivew info_laboratory_preview
    """

    loginfo(p=proj_set,label="get_xls_path")
    if exceltype == "info_collection":
        file_path = xls_info_collection(request,proj_set)
    elif exceltype == "info_basesummary_preview":
        file_path = xls_info_basesummary_preview(request,proj_set,specialtype)
    elif exceltype == "info_humanity_preview":
        file_path = xls_info_humanity_preview(request,proj_set)
    elif exceltype == "info_importantproject_preivew":
        file_path = xls_info_importantproject_preivew(request,proj_set)
    elif exceltype == "info_laboratory_preview":
        file_path = xls_info_laboratory_preview(request,proj_set) 
    return MEDIA_URL + "tmp" + file_path[len(TMP_FILES_PATH):]

def xls_info_laboratory_preview_gen(request):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    style = cell_style(horizontal=True,vertical=True)
    # generate header
    worksheet.write_merge(0, 0, 0,5 + EXPERT_NUM ,"%s%s" % (str(datetime.date.today().year), "年度大连理工大学基本科研业务费重点实验室科研专题项目申请评审结果汇总表"),style)
    # generate body
    worksheet.write_merge(1, 1, 0, 0, '序号')
    worksheet.write_merge(1, 1, 1, 1, '申请人')
    worksheet.write_merge(1, 1, 2, 2, '项目名称')
    worksheet.col(2).width = len('项目名称') * 400
    worksheet.write_merge(1, 1, 3, 3, '金额(万)')
    for i in range(0,EXPERT_NUM):
        add_col = i 
        worksheet.write_merge(1,1,4+add_col,4+add_col,'专家'+str(i + 1))
    worksheet.write_merge(1, 1, 4 + EXPERT_NUM, 4 + EXPERT_NUM, '平均分1')
    worksheet.write_merge(1, 1, 5 + EXPERT_NUM, 5 + EXPERT_NUM, '平均分2')
    worksheet.write_merge(1, 1, 6 + EXPERT_NUM, 6 + EXPERT_NUM, '平均分3')


    return worksheet, workbook

def xls_info_laboratory_preview(request,proj_set,specialtype=""):
    """
    """

    xls_obj, workbook = xls_info_laboratory_preview_gen(request)

    _number= 1
    index = 1
    for proj_obj in proj_set:
        teacher = TeacherProfile.objects.get(id = proj_obj.teacher.id)
        manager = teacher.teacherinfosetting
        re_project_expert_list = Re_Project_Expert.objects.filter(project_id = proj_obj)
        
        row = 1 + _number
        xls_obj.write(row, 0, unicode(index)) 
        xls_obj.write(row, 1, unicode(proj_obj.title)) 
        xls_obj.write(row, 2, unicode(manager.name))
        xls_obj.write(row, 3, unicode(proj_obj.projectfundsummary.total_budget))
        i = 0
        score_list = []
        average_score_1 = 0
        average_score_2 = 0
        average_score_3 = 0
        for re_expert_temp in re_project_expert_list:
            score_table = getScoreTable(re_expert_temp.project).objects.get(re_obj = re_expert_temp)
            xls_obj.write(row,4 + i,unicode(score_table.get_total_score()))
            score_list.append(score_table.get_total_score())
            i += 1
        average_score_1 = average(score_list)
        if (len(score_list) > 4):
            score_list=delete_max_and_min(score_list)
            average_score_2 = average(score_list)
            score_list=delete_max_and_min(score_list)
            average_score_3 = average(score_list)
        xls_obj.write(row, 4+EXPERT_NUM,unicode(average_score_1))
        xls_obj.write(row, 5+EXPERT_NUM,unicode(average_score_2))
        xls_obj.write(row, 6+EXPERT_NUM,unicode(average_score_3))
        _number+= 1
        index += 1

    # write xls file
    save_path = os.path.join(TMP_FILES_PATH, "%s%s.xls" % (str(datetime.date.today().year), "年度大连理工大学基本科研业务费重点实验室科研专题项目申请评审结果汇总表"))
    workbook.save(save_path)
    return save_path


def xls_info_importantproject_preivew_gen(request):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    style = cell_style(horizontal=True,vertical=True)
    # generate header
    worksheet.write_merge(0, 0, 0,5 + EXPERT_NUM ,"%s%s" % (str(datetime.date.today().year), "年大连理工大学基本科研业务费重大项目培育科研专题项目申请评审结果汇总表"),style)
    # generate body
    worksheet.write_merge(1, 1, 0, 0, '序号')
    worksheet.write_merge(1, 1, 1, 1, '申请人')
    worksheet.write_merge(1, 1, 2, 2, '项目名称')
    worksheet.col(2).width = len('项目名称') * 400
    worksheet.write_merge(1, 1, 3, 3, '金额(万)')
    for i in range(0,EXPERT_NUM):
        add_col = i 
        worksheet.write_merge(1,1,4+add_col,4+add_col,'专家'+str(i + 1))
    worksheet.write_merge(1, 1, 4 + EXPERT_NUM, 4 + EXPERT_NUM, '平均分1')
    worksheet.write_merge(1, 1, 5 + EXPERT_NUM, 5 + EXPERT_NUM, '平均分2')
    worksheet.write_merge(1, 1, 6 + EXPERT_NUM, 6 + EXPERT_NUM, '平均分3')

    return worksheet, workbook

def xls_info_importantproject_preivew(request,proj_set,specialtype=""):
    """
    """

    xls_obj, workbook = xls_info_importantproject_preivew_gen(request)

    _number= 1
    index = 1 
    for proj_obj in proj_set:
        teacher = TeacherProfile.objects.get(id = proj_obj.teacher.id)
        manager = teacher.teacherinfosetting
        re_project_expert_list = Re_Project_Expert.objects.filter(project_id = proj_obj)
        
        row = 1 + _number
        xls_obj.write(row, 0, unicode(index)) 
        xls_obj.write(row, 1, unicode(proj_obj.title)) 
        xls_obj.write(row, 2, unicode(manager.name))
        xls_obj.write(row, 3, unicode(proj_obj.projectfundsummary.total_budget))
        i = 0
        score_list = []
        average_score_1 = 0
        average_score_2 = 0
        average_score_3 = 0
        for re_expert_temp in re_project_expert_list:
            score_table = getScoreTable(re_expert_temp.project).objects.get(re_obj = re_expert_temp)
            xls_obj.write(row,4 + i,unicode(score_table.get_total_score()))
            score_list.append(score_table.get_total_score())
            i += 1
        average_score_1 = average(score_list)
        if (len(score_list) > 4):
            score_list=delete_max_and_min(score_list)
            average_score_2 = average(score_list)
            score_list=delete_max_and_min(score_list)
            average_score_3 = average(score_list)
        xls_obj.write(row, 4+EXPERT_NUM,unicode(average_score_1))
        xls_obj.write(row, 5+EXPERT_NUM,unicode(average_score_2))
        xls_obj.write(row, 6+EXPERT_NUM,unicode(average_score_3))

        _number+= 1
        index += 1
    # write xls file
    save_path = os.path.join(TMP_FILES_PATH, "%s%s.xls" % (str(datetime.date.today().year), "年大连理工大学基本科研业务费重大项目培育科研专题项目申请评审结果汇总表"))
    workbook.save(save_path)
    return save_path


def xls_info_humanity_preview_gen(request):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    style = cell_style(horizontal=True,vertical=True)
    # generate header
    worksheet.write_merge(0, 0, 0,5 + EXPERT_NUM ,"%s%s" % (str(datetime.date.today().year), "年大连理工大学基本科研业务费人文社科科研专题项目申请评审结果汇总表"),style)
    # generate body
    worksheet.write_merge(1, 1, 0, 0, '序号')
    worksheet.write_merge(1, 1, 1, 1, '申请人')
    worksheet.write_merge(1, 1, 2, 2, '项目名称')
    worksheet.col(2).width = len('项目名称') * 400
    worksheet.write_merge(1, 1, 3, 3, '金额(万)')
    for i in range(0,EXPERT_NUM):
        add_col = i 
        worksheet.write_merge(1,1,4+add_col,4+add_col,'专家'+str(i + 1))
    worksheet.write_merge(1, 1, 4 + EXPERT_NUM, 4 + EXPERT_NUM, '平均分1')
    worksheet.write_merge(1, 1, 5 + EXPERT_NUM, 5 + EXPERT_NUM, '平均分2')


    return worksheet, workbook

def xls_info_humanity_preview(request,proj_set,specialtype=""):
    """
    """

    xls_obj, workbook = xls_info_humanity_preview_gen(request)

    _number= 1
    index = 1
    for proj_obj in proj_set:
        teacher = TeacherProfile.objects.get(id = proj_obj.teacher.id)
        manager = teacher.teacherinfosetting
        re_project_expert_list = Re_Project_Expert.objects.filter(project_id = proj_obj)
        
        row = 1 + _number
        xls_obj.write(row, 0, unicode(index)) 
        xls_obj.write(row, 1, unicode(proj_obj.title)) 
        xls_obj.write(row, 2, unicode(manager.name))
        xls_obj.write(row, 3, unicode(proj_obj.projectfundsummary.total_budget))
        i = 0
        score_list = []
        average_score_1 = 0
        average_score_2 = 0
        for re_expert_temp in re_project_expert_list:
            score_table = getScoreTable(re_expert_temp.project).objects.get(re_obj = re_expert_temp)
            xls_obj.write(row,4 + i,unicode(score_table.get_total_score()))
            score_list.append(score_table.get_total_score())
            i += 1
        average_score_1 = average(score_list) 
        if (len(score_list) > 2):
            delete_max_and_min(score_list)
            average_score_2 = average(score_list)
        xls_obj.write(row, 4+EXPERT_NUM,unicode(average_score_1))
        xls_obj.write(row, 5+EXPERT_NUM,unicode(average_score_2))

        _number+= 1
        index += 1
    # write xls file
    save_path = os.path.join(TMP_FILES_PATH, "%s%s.xls" % (str(datetime.date.today().year), "年大连理工大学基本科研业务费人文社科科研专题项目申请评审结果汇总表"))
    workbook.save(save_path)
    return save_path

def delete_max_and_min(score_list):
    max_score = max(score_list)
    min_score = min(score_list)
    score_list.remove(max_score)
    score_list.remove(min_score)
    return score_list

def xls_info_basesummary_preview_gen(request,specialtype):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    style = cell_style(horizontal=True,vertical=True)
    # generate header
    worksheet.write_merge(0, 0, 0,2 + 2*EXPERT_NUM ,specialtype + '项目结题验收评审打分汇总表',style)
    # generate body
    worksheet.write_merge(1, 2, 0, 0, '序号')
    worksheet.write_merge(1, 2, 1, 1, '项目名称')
    worksheet.col(1).width = len('项目名称') * 400
    worksheet.write_merge(1, 2, 2, 2, '负责人')
    for i in range(0,EXPERT_NUM):
        add_col = i * 2
        worksheet.write_merge(1,1,3+add_col,4+add_col,'专家'+str(i + 1))
        worksheet.write_merge(2,2,3+add_col,3+add_col,'评分(100分)')
        worksheet.write_merge(2,2,4+add_col,4+add_col,'计划完成度(%)')
    return worksheet, workbook

def xls_info_basesummary_preview(request,proj_set,specialtype=""):
    """
    """

    xls_obj, workbook = xls_info_basesummary_preview_gen(request,specialtype)

    _number= 2
    index = 1
    for proj_obj in proj_set:
        teacher = TeacherProfile.objects.get(id = proj_obj.teacher.id)
        manager = teacher.teacherinfosetting
        re_project_expert_list = Re_Project_Expert.objects.filter(project_id = proj_obj)
        
        row = 1 + _number
        xls_obj.write(row, 0, unicode(index)) 
        xls_obj.write(row, 1, unicode(proj_obj.title)) 
        xls_obj.write(row, 2, unicode(manager.name))
        i = 0
        for re_expert_temp in re_project_expert_list:
            score_table = getScoreTable(re_expert_temp.project).objects.get(re_obj = re_expert_temp)
            xls_obj.write(row,3 + i*2,unicode(score_table.get_total_score()))
            xls_obj.write(row,4 + i*2,unicode())

            i += 1
        _number+= 1
        index += 1

    # write xls file
    save_path = os.path.join(TMP_FILES_PATH, "%s%s.xls" % (str(datetime.date.today().year), "年大连理工大学基本科研业务经费科研专题项目结题验收评审结果汇总表"))
    workbook.save(save_path)
    return save_path


def xls_info_collection_gen():
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('sheet1')
    style = cell_style(horizontal=True,vertical=True)
    # generate header
    worksheet.write_merge(0, 0, 0, 10, '项目基本信息',style)
    worksheet.write_merge(0, 0, 11, 11, '项目概述',style)
    worksheet.write_merge(0, 0, 12, 20, '项目负责人信息',style)
    # generate body
    worksheet.write_merge(1, 1, 0, 0, '项目名称')
    worksheet.col(0).width = len('项目名称') * 800
    worksheet.write_merge(1, 1, 1, 1, '项目编号')
    worksheet.col(1).width = len('项目编号') * 300
    worksheet.write_merge(1, 1, 2, 2, '科技活动类型')
    worksheet.write_merge(1, 1, 3, 3, '国民行业代码')
    worksheet.write_merge(1, 1, 4, 4, '学科名称')
    worksheet.write_merge(1, 1, 5, 5, '学科代码')
    worksheet.write_merge(1, 1, 6, 6, '研究开始时间')
    worksheet.write_merge(1, 1, 7, 7, '研究结束时间')
    worksheet.write_merge(1, 1, 8, 8, '立项年度')
    worksheet.write_merge(1, 1, 9, 9, '项目状态')
    worksheet.write_merge(1, 1, 10, 10, '项目类型')
    worksheet.write_merge(1, 1, 11, 11, '项目摘要')
    worksheet.col(11).width = len('项目摘要') * 800
    worksheet.write_merge(1, 1, 12, 12, '姓名')
    worksheet.write_merge(1, 1, 13, 13, '性别')
    worksheet.write_merge(1, 1, 14, 14, '出生年月')
    worksheet.write_merge(1, 1, 15, 15, '支持对象')
    worksheet.write_merge(1, 1, 16, 16, '学位')
    worksheet.write_merge(1, 1, 17, 17, '职称')
    worksheet.write_merge(1, 1, 18, 18, '行政职务')
    worksheet.write_merge(1, 1, 19, 19, '所在研发基地类型')
    worksheet.write_merge(1, 1, 20, 20, '所在研究基地名称')
    return worksheet, workbook

def xls_info_collection(request,proj_set):
    """
    """

    xls_obj, workbook = xls_info_collection_gen()

    _number= 1
    for proj_obj in proj_set:
        teacher = TeacherProfile.objects.get(id = proj_obj.teacher.id)
        manager = teacher.teacherinfosetting
        loginfo(p=manager,label="manager")
        row = 1 + _number
        xls_obj.write(row, 0, unicode(proj_obj.title)) 
        xls_obj.write(row, 1, unicode(proj_obj.project_code)) 
        xls_obj.write(row, 2, unicode(proj_obj.science_type)) 
        xls_obj.write(row, 3, unicode(proj_obj.trade_code)) 
        xls_obj.write(row, 4, unicode(proj_obj.subject_name))
        xls_obj.write(row, 5, unicode(proj_obj.subject_code))  
        xls_obj.write(row, 6, unicode(proj_obj.start_time)) 
        xls_obj.write(row, 7, unicode(proj_obj.end_time))
        xls_obj.write(row, 8, unicode(proj_obj.approval_year)) 
        xls_obj.write(row, 9, unicode(proj_obj.project_status))  
        xls_obj.write(row, 10, unicode(proj_obj.project_tpye)) 
        xls_obj.write(row, 11, unicode(proj_obj.finalsubmit.project_summary))
        xls_obj.write(row, 12, unicode(manager.name)) 
        xls_obj.write(row, 13, unicode(manager.get_sex_display())) 
        xls_obj.write(row, 14, unicode(manager.birth)) 
        xls_obj.write(row, 15, unicode(manager.get_target_type_display())) 
        xls_obj.write(row, 16, unicode(manager.get_degree_display()))
        xls_obj.write(row, 17, unicode(manager.get_title_display()))  
        xls_obj.write(row, 18, unicode(manager.get_position_display())) 
        xls_obj.write(row, 19, unicode(manager.get_base_type_display()))
        xls_obj.write(row, 20, unicode(manager.base_name))

        _number+= 1
    # write xls file
    save_path = os.path.join(TMP_FILES_PATH, "%s%s.xls" % (str(datetime.date.today().year), "年大连理工大学教育部项目信息采集填报表"))
    workbook.save(save_path)
    return save_path

def cell_style(horizontal,vertical):
    """
    为CELL添加水平居中和垂直居中
    """
    alignment = xlwt.Alignment()
    if horizontal:
        alignment.horz = xlwt.Alignment.HORZ_CENTER
    elif vertical:
        alignment.vert = xlwt.Alignment.VERT_CENTER
    style = xlwt.XFStyle() # Create Style
    style.alignment = alignment # Add Alignment to Style
    return style

def average(score_list):
   average_score = set_float(sum(score_list))/len(score_list)
   return set_float(average_score)

def set_float(num):
    return float('%.2f' % num)

