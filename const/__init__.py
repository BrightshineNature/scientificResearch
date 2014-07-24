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
    (SCHOOL_USER, u"专题管理员"),
    (COLLEGE_USER, u"学院管理员"),
    (TEACHER_USER, u"指导老师"),
    (EXPERT_USER, u"专家"),
    (FINANCE_USER, u"财务处"),
    (VISITOR_USER, u"游客"),
)
#Science Activity Type
NOTICE_CHOICE=(
    ('0',"全部"),
    ('1',"专家"),
    ('2',"学院"),
    ('3',"教师"),
)

SCIENCE_ACTIVITY_TYPE_CHOICES=(
    ('0',u"基础研究"),
    ('1',u"应用研究"),
    ('2',u"试验发展"),
    ('3',u"科技服务"),
    ('4',u"R&D成果应用"),
)
PROJECT_STATUS_APPLY = 0
PROJECT_STATUS_APPLICATION_WEB_OVER = 1
PROJECT_STATUS_APPLICATION_COMMIT_OVER = 2
PROJECT_STATUS_APPLICATION_COLLEGE_OVER = 3
PROJECT_STATUS_APPLICATION_SCHOOL_OVER = 4
PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT = 5
PROJECT_STATUS_APPROVAL = 6
PROJECT_STATUS_TASK_BUDGET_OVER = 7
PROJECT_STATUS_TASK_COMMIT_OVER = 8
PROJECT_STATUS_TASK_SCHOOL_OVER = 9
PROJECT_STATUS_TASK_FINANCE_OVER = 10
PROJECT_STATUS_TASK_OVER = 11
PROJECT_STATUS_PROGRESS_COMMIT_OVER = 12
PROJECT_STATUS_PROGRESS_SCHOOL_OVER = 13
PROJECT_STATUS_FINAL_WEB_OVER = 14
PROJECT_STATUS_FINAL_AUDIT_OVER = 15
PROJECT_STATUS_FINAL_MADA_OVER=16
PROJECT_STATUS_FINAL_COMMIT_OVER = 17
PROJECT_STATUS_FINAL_SCHOOL_OVER = 18
PROJECT_STATUS_FINAL_FINANCE_OVER = 19
PROJECT_STATUS_FINAL_OVER = 20
PROJECT_STATUS_FINAL_EXPERT_SUBJECT = 21
PROJECT_STATUS_OVER = 22
PROJECT_STATUS_STOP = 23

APPLICATION_WEB_CONFIRM="application_web_confirm"
APPLICATION_SUBMIT_CONFIRM="application_submit_confirm"
APPLICATION_COLLEGE_COMFIRM="application_college_confirm"
APPLICATION_SCHOOL_CONFIRM="application_school_confirm"
APPLICATION_EXPERT_SUBJECT_CONFIRM="application_expert_subject_confirm"
APPROVAL_CONFIRM="approval_confirm"
TASK_BUDGET_CONFIRM="task_budget_confirm"
TASK_SUBMIT_CONFIRM="task_commit_confirm"
TASK_SCHOOL_CONFIRM="task_school_confirm"
TASK_FINANCE_CONFIRM="task_finance_confirm"
PROGRESS_SUBMIT_CONFIRM="task_progress_confirm"
PROGRESS_SCHOOL_CONFIRM="task_progress_school"
FINAL_WEB_CONFIRM="final_web_confirm"
FINAL_SUBMIT_CONFIRM="final_submit_confirm"
FINAL_AUDIT_CONFIRM="final_audit_confirm"
FINAL_COMMIT_CONFIRM="final_commit_confirm"
FINAL_SCHOOL_CONFIRM="final_school_confirm"
FINAL_FINANCE_CONFIRM="final_finance_confirm"
FINAL_EXPERT_SUBJECT_CONFIRM="final_expert_subject_confirm"
PROJECT_OVER_CONFIRM="project_over_confirm"




PROJECT_STATUS_CHOICES=(
    (PROJECT_STATUS_APPLY,u"项目申请"),
    (PROJECT_STATUS_APPLICATION_WEB_OVER,u"申请书网上提交"),
    (PROJECT_STATUS_APPLICATION_COMMIT_OVER,u"申请书提交完成"),
    (PROJECT_STATUS_APPLICATION_COLLEGE_OVER,u"申请书院级审核完成"),
    (PROJECT_STATUS_APPLICATION_SCHOOL_OVER,u"申请书专题审核完成"),
    (PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT,u"申请书专家分配"),
    (PROJECT_STATUS_APPROVAL,u"项目立项"),
    (PROJECT_STATUS_TASK_BUDGET_OVER,u"任务书预算表"),
    (PROJECT_STATUS_TASK_COMMIT_OVER,u"任务书提交完成"),
    (PROJECT_STATUS_TASK_SCHOOL_OVER,u"任务书专题审核完成"),
    (PROJECT_STATUS_TASK_FINANCE_OVER,u"任务书财务审核完成"),
    (PROJECT_STATUS_TASK_OVER,u"任务审核完成"),
    (PROJECT_STATUS_PROGRESS_COMMIT_OVER,u"进展报告提交完成"),
    (PROJECT_STATUS_PROGRESS_SCHOOL_OVER,u"进展报告专题审核完成"),
    (PROJECT_STATUS_FINAL_WEB_OVER,u"结题书网上提交"),
    (PROJECT_STATUS_FINAL_AUDIT_OVER,u"结题书决算表完成"),
    (PROJECT_STATUS_FINAL_MADA_OVER,u"结题书mada完成"),
    (PROJECT_STATUS_FINAL_COMMIT_OVER,u"结题书提交完成"),
    (PROJECT_STATUS_FINAL_SCHOOL_OVER,u"结题书专题审核完成"),
    (PROJECT_STATUS_FINAL_FINANCE_OVER,u"结题书专家审核完成"),
    (PROJECT_STATUS_FINAL_OVER,u"结题书审核完成"),
    (PROJECT_STATUS_FINAL_EXPERT_SUBJECT,u"结题书专家分配完成"),
    (PROJECT_STATUS_OVER,u"项目结题"),
    (PROJECT_STATUS_STOP,u"终止"),
)
SEX_CHOICES=(
    ('0',"男"),
    ('1',"女"),
)
PROJECT_IDENTITY_CHOICES=(
    ('0',"教师"),
    ('1',"本科生"),
    ('2',"硕士生"),
    ('3',"博士生"),
    ('4',"博士后"),
    ('5',"其他"),
)
DEGREE_CHOICES=(
    ('0',"学士"),
    ('1',"硕士"),
    ('2',"博士"),
    ('3',"其他"),
)
PROFESSIONAL_TITLE_CHOICES =(
    ('0',"正高级"),
    ('1',"副高级"),
    ('2',"中级"),
    ('3',"其他"),
)
EXECUTIVE_POSITION_CHOICES=(
    ('0',"校级"),
    ('1',"院（系）级"),
    ('2',"校部（处）级"),
    ('3',"无"),
)
RESEARCH_BASES_TYPE_CHOICES=(
    ('0',"国家（重点）实验室"),
    ('1',"教育部重点实验室"),
    ('2',"国家文科基础学科人才培养和科学研究基地"),
    ('3',"其他省部级重点实验室"),
    ('4',"省部级以下重点实验室"),
    ('5',"无"),
)

STATICS_DATA_TYPE=(
    ('0',"国家级自然科学一等奖"),
    ('1',"国家级自然科学二等奖"),
    ('2',"国家级科技进步一等奖"), 
    ('3',"国家级科技进步二等奖"), 
    ('4',"国家级发明一等奖"), 
    ('5',"国家级发明二等奖"), 
    ('6',"省部级自然科学一等奖"), 
    ('7',"省部级自然科学二等奖"), 
    ('8',"省部级科技进步一等奖"),
    ('9',"省部级科技进步二等奖"), 
    ('10',"国际学术奖"), 
    ('11',"其它"),
    ('12',"国际会议特邀报告"),
    ('13',"国际会议分组报告"),
    ('14',"全国性会议特邀报告"), 
    ('15',"全国性会议分组报告"), 
    ('16',"国际刊物"), 
    ('17',"国内核心刊物"), 
    ('18',"SCI"), 
    ('19',"EI"), 
    ('20',"ISTP"),
    ('21',"ISR"), 
    ('22',"中文已出版"), 
    ('23',"中文待出版"),
    ('24',"外文已出版"), 
    ('25',"外文待出版"),
    ('26',"国内申请"),
    ('27',"国内批准"),
    ('28',"国外申请"), 
    ('29',"国外批准"), 
    ('30',"可推广项数"),
    ('31',"已推广项数"), 
    ('32',"经济效益（万元）"), 
    ('33',"软件/数据库"), 
    ('34',"图表/图集"), 
    ('35',"新仪器/新方法"),
    ('36',"鉴定及其它"),
    ('37',"博士后在站"),
    ('38',"博士后出站"),
    ('39',"博士在读"), 
    ('40',"博士毕业"), 
    ('41',"硕士在读"),
    ('42',"硕士毕业"), 
    ('43',"中青年学术带头人(40岁以下)"), 
    ('44',"中青年学术带头人(40-50岁)"), 
    ('45',"国际次数"), 
    ('46',"国际人数"),
    ('47',"国内次数"),
    ('48',"国内人数"), 
    ('49',"出国参加国际学术会议人数次数"),
    ('50',"出国参加国际学术会议人数人数"), 
)

STATICS_TYPE=(
    ('0',"获奖（项）"),
    ('1',"专著／论文（篇）"),
    ('2',"专利及其它"), 
    ('3',"人才培养及学术交流"), 
)

ACHIVEMENT_TYPE=(
    ('0',"专著"),
    ('1',"期刊论文"),
    ('2',"会议论文"), 
    ('3',"专利"), 
    ('4',"获奖"),
    ('5',"其他"),

)


PAGE_ELEMENTS = 10




