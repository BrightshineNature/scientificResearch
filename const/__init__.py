# coding: UTF-8
'''
Created on 2014-06-10

@author: LiuYe

Desc: const defination
'''
UNDIFINED = "undifined"
# For UserIdentity Table
ADMINSTAFF_USER = "adminStaff"
SCHOOL_USER = "school"
COLLEGE_USER = "college"
EXPERT_USER = "expert"
TEACHER_USER = "teacher"
FINANCE_USER = "finance"
VISITOR_USER = "visitor"

AUTH_CHOICES = (
    (ADMINSTAFF_USER, u"管理员"),
    (SCHOOL_USER, u"学校管理员"),
    (COLLEGE_USER, u"学院管理员"),
    (TEACHER_USER, u"指导老师"),
    (EXPERT_USER, u"专家"),
    (FINANCE_USER, u"财务处"),
    (VISITOR_USER, u"游客"),
)
SCIENCE_ACTIVITY_TYPE=(
    ('0',"基础研究"),
    ('1',"应用研究"),
    ('2',"试验发展"),
    ('3',"科技服务"),
    ('4',"R&D成果应用"),
)
PROJECT_STATUS=(
  ('0',"在研"),
  ('1',"结题"),
  ('2',"终止"),
)
SEX=(
    ('0',"男"),
    ('1',"女"),
)
PROJECT_IDENTITY=(
    ('0',"教师"),
    ('1',"本科生"),
    ('2',"硕士生"),
    ('3',"博士生"),
    ('4',"博士后"),
    ('5',"其他"),
)
DEGREE=(
    ('0',"学士"),
    ('1',"硕士"),
    ('2',"博士"),
    ('3',"其他"),
)
PROFESSIONAL_TITLE=(
    ('0',"正高级"),
    ('1',"副高级"),
    ('2',"中级"),
    ('3',"其他"),
)
EXECUTIVE_POSITION=(
    ('0',"校级"),
    ('1',"院（系）级"),
    ('2',"校部（处）级"),
    ('3',"无"),
)
RESEARCH_BASES_TYPE=(
    ('0',"国家（重点）实验室"),
    ('1',"教育部重点实验室"),
    ('2',"国家文科基础学科人才培养和科学研究基地"),
    ('3',"其他省部级重点实验室"),
    ('4',"省部级以下重点实验室"),
    ('5',"无"),
)







