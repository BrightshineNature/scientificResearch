# coding: UTF-8
'''
Created on 2014-06-10

@author: LiuYe

Desc: const defination
'''
LEVEL_CHOICES = (
    (0, "A"),
    (1, "B"),
    (2, "C"),
    (3, "D"),
    (4, "E"),
    #...
)

UNDIFINED = "undifined"
# For UserIdentity Table
ADMINSTAFF_USER = "adminStaff"
SCHOOL_USER = "school"
COLLEGE_USER = "college"
EXPERT_USER = "expert"
TEACHER_USER = "teacher"
FINANCE_USER = "finance"
VISITOR_USER = "visitor"

TYPE_APPLICATION = ("application",u"申请")
TYPE_TASK = ("task",u"任务书")
TYPE_PROGRESS = ("progress",u"进展报告")
TYPE_FINAL = ("final",u"结题")
TYPE_ALLOC  = ("alloc",u"专家初审")
TYPE_FINAL_ALLOC = ("final_alloc",u"专家终审")

CONTROL_TYPE_CHOICES =(
    TYPE_APPLICATION,
    TYPE_ALLOC,
    TYPE_TASK,
    TYPE_PROGRESS,
    TYPE_FINAL,
    TYPE_FINAL_ALLOC
)

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
SUBMIT_STATUS_APPLICATION = 0
SUBMIT_STATUS_TASK = 1
SUBMIT_STATUS_PROGRESS = 2
SUBMIT_STATUS_FINAL = 3
SUBMIT_STATUS_REVIEW = 4
SUBMIT_STATUS_BUDGET = 5
SUBMIT_STATUS_AUDITE = 6



PROJECT_STATUS_APPLY = 0
PROJECT_STATUS_APPLICATION_WEB_OVER = 1
PROJECT_STATUS_APPLICATION_COMMIT_OVER = 2
PROJECT_STATUS_APPLICATION_COLLEGE_OVER = 3
PROJECT_STATUS_APPLICATION_SCHOOL_OVER = 4
PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT = 5
PROJECT_STATUS_APPROVAL = 6
PROJECT_STATUS_TASK_BUDGET_OVER = 7
PROJECT_STATUS_TASK_FINANCE_OVER = 8
PROJECT_STATUS_TASK_COMMIT_OVER = 9
PROJECT_STATUS_TASK_COLLEGE_OVER = 10
PROJECT_STATUS_TASK_SCHOOL_OVER = 11
PROJECT_STATUS_NONE = 12
PROJECT_STATUS_PROGRESS_WEB_OVER = 13
PROJECT_STATUS_PROGRESS_COMMIT_OVER = 14
PROJECT_STATUS_PROGRESS_SCHOOL_OVER = 15
PROJECT_STATUS_FINAL_AUDITE_OVER = 16#决算提交完成
PROJECT_STATUS_FINAL_FINANCE_OVER = 17
PROJECT_STATUS_FINAL_WEB_OVER = 18
PROJECT_STATUS_FINAL_COMMIT_OVER = 19
PROJECT_STATUS_FINAL_COLLEGE_OVER = 20
PROJECT_STATUS_FINAL_SCHOOL_OVER = 21
PROJECT_STATUS_FINAL_EXPERT_SUBJECT = 22
PROJECT_STATUS_OVER = 23
PROJECT_STATUS_STOP = 24

APPLICATION_WEB_CONFIRM="application_web_confirm"
APPLICATION_SUBMIT_CONFIRM="application_submit_confirm"
APPLICATION_COLLEGE_COMFIRM="application_college_confirm"
APPLICATION_SCHOOL_CONFIRM="application_school_confirm"
APPLICATION_EXPERT_SUBJECT_CONFIRM="application_expert_subject_confirm"
APPLICATION_REVIEW_START_CONFIRM = "application_review_start_confirm"
APPLICATION_REVIEW_CONFIRM="application_review_confirm"
APPROVAL_CONFIRM="approval_confirm"
TASK_BUDGET_CONFIRM="task_budget_confirm"
TASK_SUBMIT_CONFIRM="task_commit_confirm"
TASK_FINANCE_CONFIRM="task_finance_confirm"
TASK_SCHOOL_CONFIRM="task_school_confirm"
PROGRESS_WEB_CONFIRM="task_progress_web_confirm"
PROGRESS_SUBMIT_CONFIRM="task_progress_confirm"
PROGRESS_SCHOOL_CONFIRM="task_progress_school"
FINAL_WEB_CONFIRM="final_web_confirm"
FINAL_SUBMIT_CONFIRM="final_submit_confirm"
FINAL_COMMIT_CONFIRM="final_commit_confirm"
FINAL_FINANCE_CONFIRM="final_finance_confirm"
FINAL_SCHOOL_CONFIRM="final_school_confirm"
FINAL_EXPERT_SUBJECT_CONFIRM="final_expert_subject_confirm"
FINAL_REVIEW_START_CONFIRM="final_review_start_confirm"
FINAL_REVIEW_CONFIRM="final_review_confirm"
PROJECT_OVER_CONFIRM="project_over_confirm"


PROJECT_STATUS_CHOICES=(
    (PROJECT_STATUS_APPLY,u"项目申请"),
    (PROJECT_STATUS_APPLICATION_WEB_OVER,u"申请书网上提交"),
    (PROJECT_STATUS_APPLICATION_COMMIT_OVER,u"申请书提交完成"),
    (PROJECT_STATUS_APPLICATION_COLLEGE_OVER,u"申请书院级审核完成"),
    (PROJECT_STATUS_APPLICATION_SCHOOL_OVER,u"申请书专题审核完成"),
    (PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT,u"申请书专家分配"),
    (PROJECT_STATUS_APPROVAL,u"项目立项"),
    (PROJECT_STATUS_TASK_BUDGET_OVER,u"任务书预算表提交完成"),
    (PROJECT_STATUS_TASK_FINANCE_OVER,u"任务书财务审核完成"),
    (PROJECT_STATUS_TASK_COMMIT_OVER,u"任务书提交完成"),
    (PROJECT_STATUS_TASK_COLLEGE_OVER,u"任务书学院审核完成"),
    (PROJECT_STATUS_TASK_SCHOOL_OVER,u"任务书专题审核完成"),
    (PROJECT_STATUS_NONE,u"任务书专题审核完成"),
    (PROJECT_STATUS_PROGRESS_WEB_OVER,u"进展报告网上提交完成"),
    (PROJECT_STATUS_PROGRESS_COMMIT_OVER,u"进展报告提交完成"),
    (PROJECT_STATUS_PROGRESS_SCHOOL_OVER,u"进展报告专题审核完成"),
    (PROJECT_STATUS_FINAL_AUDITE_OVER,u"结题书决算表提交完成"),
    (PROJECT_STATUS_FINAL_FINANCE_OVER,u"结题书财务审核完成"),
    (PROJECT_STATUS_FINAL_WEB_OVER,u"结题书网上提交"),
    (PROJECT_STATUS_FINAL_COMMIT_OVER,u"结题书提交完成"),
    (PROJECT_STATUS_FINAL_COLLEGE_OVER,u"结题书学院审核完成"),
    (PROJECT_STATUS_FINAL_SCHOOL_OVER,u"结题书专题审核完成"),
    (PROJECT_STATUS_FINAL_EXPERT_SUBJECT,u"结题书专家分配完成"),
    (PROJECT_STATUS_OVER,u"项目结题"),
    (PROJECT_STATUS_STOP,u"终止"),
)


PROJECT_STATUS_PENDDING={
    (PROJECT_STATUS_APPLY,u"请提交网上申请"),
    (PROJECT_STATUS_APPLICATION_WEB_OVER,u"请上传申请书"),
    (PROJECT_STATUS_APPLICATION_COMMIT_OVER,u"等待学院秘书审核"),
    (PROJECT_STATUS_APPLICATION_COLLEGE_OVER,u"等待专题管理员审核申请书"),
    (PROJECT_STATUS_APPLICATION_SCHOOL_OVER,u"等待专家分配"),
    (PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT,u"等待专家评审"),
    (PROJECT_STATUS_APPROVAL,u"请提交任务书预算表"),
    (PROJECT_STATUS_TASK_BUDGET_OVER,u"请上传任务书"),
    (PROJECT_STATUS_TASK_COMMIT_OVER,u"等待专题管理员审核任务书"),
    (PROJECT_STATUS_TASK_SCHOOL_OVER,u"等待财务审核任务书"),
    (PROJECT_STATUS_TASK_FINANCE_OVER,u"请上传进展报告"),
    (PROJECT_STATUS_PROGRESS_WEB_OVER,u"请提交网上进展报告"),
    (PROJECT_STATUS_PROGRESS_COMMIT_OVER,u"等待专题管理员审核进展报告"),
    (PROJECT_STATUS_PROGRESS_SCHOOL_OVER,u"请提交网上结题书"),
    (PROJECT_STATUS_FINAL_WEB_OVER,u"请上传结题书"),
    (PROJECT_STATUS_FINAL_COMMIT_OVER,u"等待专题管理员审核结题书"),
    (PROJECT_STATUS_FINAL_SCHOOL_OVER,u"等待财务审核结题书"),
    (PROJECT_STATUS_FINAL_FINANCE_OVER,u"等待专家分配"),
    (PROJECT_STATUS_FINAL_EXPERT_SUBJECT,u"等待专家评审"),
    (PROJECT_STATUS_OVER,u"项目结题"),
    (PROJECT_STATUS_STOP,u"终止"),
}

NEXT_STATUS = 1
ROLLBACK_STATUS = 2
PENDDING_STATUS = 3

NEXT_PROGRESS_PERMISSION_DICT={
    SCHOOL_USER:(PROJECT_STATUS_APPLICATION_SCHOOL_OVER,PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT,PROJECT_STATUS_APPROVAL,PROJECT_STATUS_TASK_SCHOOL_OVER,PROJECT_STATUS_PROGRESS_SCHOOL_OVER,PROJECT_STATUS_FINAL_SCHOOL_OVER,PROJECT_STATUS_FINAL_EXPERT_SUBJECT,PROJECT_STATUS_OVER,PROJECT_STATUS_STOP),
    COLLEGE_USER:(PROJECT_STATUS_APPLICATION_COLLEGE_OVER,),
    TEACHER_USER:(PROJECT_STATUS_APPLY,PROJECT_STATUS_APPLICATION_WEB_OVER,PROJECT_STATUS_APPLICATION_COMMIT_OVER,PROJECT_STATUS_TASK_BUDGET_OVER,PROJECT_STATUS_TASK_COMMIT_OVER,PROJECT_STATUS_PROGRESS_WEB_OVER,PROJECT_STATUS_FINAL_AUDITE_OVER,PROJECT_STATUS_PROGRESS_COMMIT_OVER,PROJECT_STATUS_FINAL_WEB_OVER,PROJECT_STATUS_FINAL_COMMIT_OVER,PROJECT_STATUS_FINAL_EXPERT_SUBJECT,PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT),
    EXPERT_USER :(),
    FINANCE_USER:(PROJECT_STATUS_TASK_FINANCE_OVER,PROJECT_STATUS_FINAL_FINANCE_OVER),
}
PROGRESS_FILE_DICT={
    PROJECT_STATUS_APPLICATION_WEB_OVER:'file_application',
    PROJECT_STATUS_TASK_COMMIT_OVER:'file_task',
    PROJECT_STATUS_PROGRESS_WEB_OVER:'file_interimchecklist',
    PROJECT_STATUS_FINAL_WEB_OVER:'file_summary',
}

PROGRESS_REVIEW_DICT={
    PROJECT_STATUS_APPLY                      :{NEXT_STATUS:PROJECT_STATUS_APPLICATION_WEB_OVER      ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"请提交网上申请"            },
    PROJECT_STATUS_APPLICATION_WEB_OVER       :{NEXT_STATUS:PROJECT_STATUS_APPLICATION_COMMIT_OVER   ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"请上传申请书"              },
    PROJECT_STATUS_APPLICATION_COMMIT_OVER    :{NEXT_STATUS:PROJECT_STATUS_APPLICATION_COLLEGE_OVER  ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待学院秘书审核"          },
    PROJECT_STATUS_APPLICATION_COLLEGE_OVER   :{NEXT_STATUS:PROJECT_STATUS_APPLICATION_SCHOOL_OVER   ,ROLLBACK_STATUS:PROJECT_STATUS_APPLY               ,PENDDING_STATUS:u"等待专题管理员审核申请书"  },
    PROJECT_STATUS_APPLICATION_SCHOOL_OVER    :{NEXT_STATUS:PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT,ROLLBACK_STATUS:PROJECT_STATUS_APPLY               ,PENDDING_STATUS:u"等待专家评审"              },
    PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT :{NEXT_STATUS:PROJECT_STATUS_APPROVAL                  ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待立项"                  },
    PROJECT_STATUS_APPROVAL                   :{NEXT_STATUS:PROJECT_STATUS_TASK_BUDGET_OVER          ,ROLLBACK_STATUS:PROJECT_STATUS_STOP                ,PENDDING_STATUS:u"请提交任务书预算表"        },
    PROJECT_STATUS_TASK_BUDGET_OVER           :{NEXT_STATUS:PROJECT_STATUS_TASK_FINANCE_OVER         ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待财务审核任务书"        },
    PROJECT_STATUS_TASK_FINANCE_OVER          :{NEXT_STATUS:PROJECT_STATUS_TASK_COMMIT_OVER          ,ROLLBACK_STATUS:PROJECT_STATUS_APPROVAL            ,PENDDING_STATUS:u"请上传任务书"              },
    PROJECT_STATUS_TASK_COMMIT_OVER           :{NEXT_STATUS:PROJECT_STATUS_TASK_SCHOOL_OVER          ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待专题管理员审核任务书"  },
    PROJECT_STATUS_TASK_SCHOOL_OVER           :{NEXT_STATUS:PROJECT_STATUS_PROGRESS_WEB_OVER         ,ROLLBACK_STATUS:PROJECT_STATUS_TASK_FINANCE_OVER   ,PENDDING_STATUS:u"请提交网上进展报告"        },
    PROJECT_STATUS_PROGRESS_WEB_OVER          :{NEXT_STATUS:PROJECT_STATUS_PROGRESS_COMMIT_OVER      ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"请上传进展报告"            },
    PROJECT_STATUS_PROGRESS_COMMIT_OVER       :{NEXT_STATUS:PROJECT_STATUS_PROGRESS_SCHOOL_OVER      ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待专题管理员审核进展报告"},
    PROJECT_STATUS_PROGRESS_SCHOOL_OVER       :{NEXT_STATUS:PROJECT_STATUS_FINAL_AUDITE_OVER         ,ROLLBACK_STATUS:PROJECT_STATUS_TASK_SCHOOL_OVER    ,PENDDING_STATUS:u"请提交任务书决算表"        },
    PROJECT_STATUS_FINAL_AUDITE_OVER          :{NEXT_STATUS:PROJECT_STATUS_FINAL_FINANCE_OVER        ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待财务审核结题书"        },
    PROJECT_STATUS_FINAL_FINANCE_OVER         :{NEXT_STATUS:PROJECT_STATUS_FINAL_WEB_OVER            ,ROLLBACK_STATUS:PROJECT_STATUS_PROGRESS_SCHOOL_OVER,PENDDING_STATUS:u"请提交网上结题书"          },
    PROJECT_STATUS_FINAL_WEB_OVER             :{NEXT_STATUS:PROJECT_STATUS_FINAL_COMMIT_OVER         ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"请上传结题书"              },
    PROJECT_STATUS_FINAL_COMMIT_OVER          :{NEXT_STATUS:PROJECT_STATUS_FINAL_SCHOOL_OVER         ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待专题管理员审核结题书"  },
    PROJECT_STATUS_FINAL_SCHOOL_OVER          :{NEXT_STATUS:PROJECT_STATUS_FINAL_EXPERT_SUBJECT      ,ROLLBACK_STATUS:PROJECT_STATUS_FINAL_FINANCE_OVER  ,PENDDING_STATUS:u"等待专家评审"              },
    PROJECT_STATUS_FINAL_EXPERT_SUBJECT       :{NEXT_STATUS:PROJECT_STATUS_OVER                      ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待结题"                  },
    PROJECT_STATUS_OVER                       :{NEXT_STATUS:PROJECT_STATUS_OVER                      ,ROLLBACK_STATUS:PROJECT_STATUS_STOP                ,PENDDING_STATUS:u"项目结题"                  },
    PROJECT_STATUS_STOP                       :{NEXT_STATUS:PROJECT_STATUS_STOP                      ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"终止"                      },
}

# PROGRESS_NOT_REVIEW_DICT={
#     PROJECT_STATUS_APPLY                      :{NEXT_STATUS:PROJECT_STATUS_APPLICATION_WEB_OVER      ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"请提交网上申请"            },
#     PROJECT_STATUS_APPLICATION_WEB_OVER       :{NEXT_STATUS:PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"请上传申请书"              },
#     PROJECT_STATUS_APPLICATION_EXPERT_SUBJECT :{NEXT_STATUS:PROJECT_STATUS_APPROVAL                  ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待立项"                  },
#     PROJECT_STATUS_APPROVAL                   :{NEXT_STATUS:PROJECT_STATUS_TASK_BUDGET_OVER          ,ROLLBACK_STATUS:PROJECT_STATUS_APPLY               ,PENDDING_STATUS:u"请提交任务书预算表"        },
#     PROJECT_STATUS_TASK_BUDGET_OVER           :{NEXT_STATUS:PROJECT_STATUS_TASK_FINANCE_OVER         ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待财务审核任务书"        },
#     PROJECT_STATUS_TASK_FINANCE_OVER          :{NEXT_STATUS:PROJECT_STATUS_TASK_COMMIT_OVER          ,ROLLBACK_STATUS:PROJECT_STATUS_APPROVAL            ,PENDDING_STATUS:u"请上传任务书"              },
#     PROJECT_STATUS_TASK_COMMIT_OVER           :{NEXT_STATUS:PROJECT_STATUS_TASK_SCHOOL_OVER          ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待专题管理员审核任务书"  },
#     PROJECT_STATUS_TASK_SCHOOL_OVER           :{NEXT_STATUS:PROJECT_STATUS_PROGRESS_WEB_OVER         ,ROLLBACK_STATUS:PROJECT_STATUS_TASK_FINANCE_OVER   ,PENDDING_STATUS:u"请提交网上进展报告"        },
#     PROJECT_STATUS_PROGRESS_WEB_OVER          :{NEXT_STATUS:PROJECT_STATUS_PROGRESS_COMMIT_OVER      ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"请上传进展报告"            },
#     PROJECT_STATUS_PROGRESS_COMMIT_OVER       :{NEXT_STATUS:PROJECT_STATUS_PROGRESS_SCHOOL_OVER      ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待专题管理员审核进展报告"},
#     PROJECT_STATUS_PROGRESS_SCHOOL_OVER       :{NEXT_STATUS:PROJECT_STATUS_FINAL_AUDITE_OVER         ,ROLLBACK_STATUS:PROJECT_STATUS_TASK_SCHOOL_OVER    ,PENDDING_STATUS:u"请提交任务书决算表"        },
#     PROJECT_STATUS_FINAL_AUDITE_OVER          :{NEXT_STATUS:PROJECT_STATUS_FINAL_FINANCE_OVER        ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待财务审核结题书"        },
#     PROJECT_STATUS_FINAL_FINANCE_OVER         :{NEXT_STATUS:PROJECT_STATUS_FINAL_WEB_OVER            ,ROLLBACK_STATUS:PROJECT_STATUS_PROGRESS_SCHOOL_OVER,PENDDING_STATUS:u"请提交网上结题书"          },
#     PROJECT_STATUS_FINAL_WEB_OVER             :{NEXT_STATUS:PROJECT_STATUS_FINAL_EXPERT_SUBJECT      ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"请上传结题书"              },
#     PROJECT_STATUS_FINAL_EXPERT_SUBJECT       :{NEXT_STATUS:PROJECT_STATUS_OVER                      ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"等待项目结题"              },
#     PROJECT_STATUS_OVER                       :{NEXT_STATUS:PROJECT_STATUS_OVER                      ,ROLLBACK_STATUS:PROJECT_STATUS_FINAL_FINANCE_OVER  ,PENDDING_STATUS:u"项目结题"                  },
#     PROJECT_STATUS_STOP                       :{NEXT_STATUS:PROJECT_STATUS_STOP                      ,ROLLBACK_STATUS:None                               ,PENDDING_STATUS:u"终止"                      },
# }

SEX_CHOICES=(
    ('0',u"男"),
    ('1',u"女"),
)
PROJECT_IDENTITY_CHOICES=(
    ('0',u"教师"),
    ('1',u"本科生"),
    ('2',u"硕士生"),
    ('3',u"博士生"),
    ('4',u"博士后"),
    ('5',u"其他"),
)
DEGREE_CHOICES=(
    ('0',u"学士"),
    ('1',u"硕士"),
    ('2',u"博士"),
    ('3',u"其他"),
)
PROFESSIONAL_TITLE_CHOICES =(
    ('0',u"正高级"),
    ('1',u"副高级"),
    ('2',u"中级"),
    ('3',u"其他"),
)
EXECUTIVE_POSITION_CHOICES=(
    ('0',u"校级"),
    ('1',u"院（系）级"),
    ('2',u"校部（处）级"),
    ('3',u"无"),
)
RESEARCH_BASES_TYPE_CHOICES=(
    ('0',u"国家（重点）实验室"),
    ('1',u"教育部重点实验室"),
    ('2',u"国家文科基础学科人才培养和科学研究基地"),
    ('3',u"其他省部级重点实验室"),
    ('4',u"省部级以下重点实验室"),
    ('5',u"无"),
)

STATICS_DATA_TYPE=(
    ('0',u"国家级自然科学一等奖"),
    ('1',u"国家级自然科学二等奖"),
    ('2',u"国家级科技进步一等奖"), 
    ('3',u"国家级科技进步二等奖"), 
    ('4',u"国家级发明一等奖"), 
    ('5',u"国家级发明二等奖"), 
    ('6',u"省部级自然科学一等奖"), 
    ('7',u"省部级自然科学二等奖"), 
    ('8',u"省部级科技进步一等奖"),
    ('9',u"省部级科技进步二等奖"), 
    ('10',u"国际学术奖"), 
    ('11',u"其它"),
    ('12',u"国际会议特邀报告"),
    ('13',u"国际会议分组报告"),
    ('14',u"全国性会议特邀报告"), 
    ('15',u"全国性会议分组报告"), 
    ('16',u"国际刊物"), 
    ('17',u"国内核心刊物"), 
    ('18',u"SCI"), 
    ('19',u"EI"), 
    ('20',u"ISTP"),
    ('21',u"ISR"), 
    ('22',u"中文已出版"), 
    ('23',u"中文待出版"),
    ('24',u"外文已出版"), 
    ('25',u"外文待出版"),
    ('26',u"国内申请"),
    ('27',u"国内批准"),
    ('28',u"国外申请"), 
    ('29',u"国外批准"), 
    ('30',u"可推广项数"),
    ('31',u"已推广项数"), 
    ('32',u"经济效益（万元）"), 
    ('33',u"软件/数据库"), 
    ('34',u"图表/图集"), 
    ('35',u"新仪器/新方法"),
    ('36',u"鉴定及其它"),
    ('37',u"博士后在站"),
    ('38',u"博士后出站"),
    ('39',u"博士在读"), 
    ('40',u"博士毕业"), 
    ('41',u"硕士在读"),
    ('42',u"硕士毕业"), 
    ('43',u"中青年学术带头人(40岁以下)"), 
    ('44',u"中青年学术带头人(40-50岁)"), 
    ('45',u"国际次数"), 
    ('46',u"国际人数"),
    ('47',u"国内次数"),
    ('48',u"国内人数"), 
    ('49',u"出国参加国际学术会议人数次数"),
    ('50',u"出国参加国际学术会议人数人数"), 
)

STATICS_TYPE=(
    ('0',u"获奖（项）"),
    ('1',u"专著／论文（篇）"),
    ('2',u"专利及其它"), 
    ('3',u"人才培养及学术交流"), 
)

ACHIVEMENT_TYPE=(
    ('0',u"专著"),
    ('1',u"期刊论文"),
    ('2',u"会议论文"), 
    ('3',u"专利"), 
    ('4',u"获奖"),
    ('5',u"其他"),

)


PAGE_ELEMENTS = 10
FIRST_ROUND_PATH = "alloc"

# APP: news
# the following 4 variables are used in foreground,
# so use some meaning words
NEWS_CATEGORY_ANNOUNCEMENT = "announcement"
NEWS_CATEGORY_DOCUMENTS = "documents"
NEWS_CATEGORY_CHOICES = (
    (NEWS_CATEGORY_ANNOUNCEMENT, u"通知公告"),
)
# the max length of news_content
NEWS_MAX_LENGTH = 100000

EXPERT_REVIEW_BASICSCIENTIFIC = "basicscientific"
EXPERT_REVIEW_MAJORPROJECT = "majorproject"
EXPERT_REVIEW_KEYLABORATORY = "keylaboratory"
EXPERT_REVIEW_HUMANITIESSOCIAL = "humanitiessocial"
EXPERT_REVIEW_BASICSCIENTIFICSCIENCE = "basicscientificscience"
EXPERT_REVIEW_FRONT = "front"
EXPERT_REVIEW_OUTSTANDING = "outstanding"

EXPERT_REVIEW_TABLE_CHOICES =(
    (EXPERT_REVIEW_BASICSCIENTIFIC , u"基本科研业务费"),
    (EXPERT_REVIEW_HUMANITIESSOCIAL , u"人文社科科研"),
    (EXPERT_REVIEW_MAJORPROJECT , u"重大项目"),
    (EXPERT_REVIEW_KEYLABORATORY , u"重点实验室专题"),
    (EXPERT_REVIEW_BASICSCIENTIFICSCIENCE, "理科基础科研业务费"),
    (EXPERT_REVIEW_FRONT,u"前沿学科基础科研业务费"),
    (EXPERT_REVIEW_OUTSTANDING,u"优秀青年人才基础科研业务费"),
)

EXPERT_FINAL_REVIEW_BASICSCIENTIFIC = "final_basicscientific"
EXPERT_FINAL_REVIEW_MAJORPROJECT = "final_majorproject"
EXPERT_FINAL_REVIEW_KEYLABORATORY = "final_keylaboratory"
EXPERT_FINAL_REVIEW_HUMANITIESSOCIAL = "final_humanitiessocial"
EXPERT_FINAL_REVIEW_BASICSCIENTIFICSCIENCE = "final_basicscientificscience"
EXPERT_FINAL_REVIEW_FRONT = "final_front"
EXPERT_FINAL_REVIEW_OUTSTANDING = "final_outstanding"

EXPERT_FINAL_REVIEW_TABLE_CHOICES = (
    (EXPERT_FINAL_REVIEW_BASICSCIENTIFIC , u"基本科研业务费终审表"),
    (EXPERT_FINAL_REVIEW_HUMANITIESSOCIAL , u"人文社科科研终审表"),
    (EXPERT_FINAL_REVIEW_MAJORPROJECT , u"重大项目终审表"),
    (EXPERT_FINAL_REVIEW_KEYLABORATORY , u"重点实验室专题终审表"),
    (EXPERT_FINAL_REVIEW_BASICSCIENTIFICSCIENCE, "理科基础科研业务费终审表"),
    (EXPERT_FINAL_REVIEW_FRONT,u"前沿学科基础科研业务费终审表"),
    (EXPERT_FINAL_REVIEW_OUTSTANDING,u"优秀青年人才基础科研业务费终审表"),
)

EXPERT_NUM = 20

EXCELTYPE_INFO_COLLECTION = "info_collection"
EXCELTYPE_INFO_SUMMARY =  "info_summary"
EXCELTYPE_INFO_FUNDSUMMARY = "info_fundsummay"
EXCELTYPE_INFO_FUNDBUDGET = "info_fundbudget"
EXCELTYPE_INFO_TEACHERINFO = "info_teacher"

EXCELTYPE_INFO_BASESUMMARY_PREVIEW = EXPERT_REVIEW_BASICSCIENTIFIC
EXCELTYPE_INFO_HUMANITY_PREVIEW = EXPERT_REVIEW_HUMANITIESSOCIAL
EXCELTYPE_INFO_IMPORTANTPROJECT_PREVIEW = EXPERT_REVIEW_MAJORPROJECT
EXCELTYPE_INFO_LABORATORY_PREVIEW = EXPERT_REVIEW_KEYLABORATORY
EXCELTYPE_INFO_BASESUMMARYSCIENCE_PREVIEW = EXPERT_REVIEW_BASICSCIENTIFICSCIENCE
EXCELTYPE_INFO_FRONT_PREVIEW = EXPERT_REVIEW_FRONT 
EXCELTYPE_INFO_OUTSTANDING_PREVIEW = EXPERT_REVIEW_OUTSTANDING


#终审
EXCELTYPE_INFO_FINAL_BASESUMMARY_PREVIEW        = EXPERT_FINAL_REVIEW_BASICSCIENTIFIC
EXCELTYPE_INFO_FINAL_HUMANITY_PREVIEW           = EXPERT_FINAL_REVIEW_HUMANITIESSOCIAL
EXCELTYPE_INFO_FINAL_IMPORTANTPROJECT_PREVIEW   = EXPERT_FINAL_REVIEW_MAJORPROJECT
EXCELTYPE_INFO_FINAL_LABORATORY_PREVIEW         = EXPERT_FINAL_REVIEW_KEYLABORATORY
EXCELTYPE_INFO_FINAL_BASESUMMARYSCIENCE_PREVIEW = EXPERT_FINAL_REVIEW_BASICSCIENTIFICSCIENCE
EXCELTYPE_INFO_FINAL_FRONT_PREVIEW              = EXPERT_FINAL_REVIEW_FRONT 
EXCELTYPE_INFO_FINAL_OUTSTANDING_PREVIEW        = EXPERT_FINAL_REVIEW_OUTSTANDING

class EXCELTYPE_DICT_OBJECT(object):
    """docstring for ClassName"""
    def __init__(self):
        self.INFO_COLLECTION = EXCELTYPE_INFO_COLLECTION
        self.INFO_SUMMARY = EXCELTYPE_INFO_SUMMARY
        self.INFO_FUNDSUMMARY = EXCELTYPE_INFO_FUNDSUMMARY
        self.INFO_FUNDBUDGET = EXCELTYPE_INFO_FUNDBUDGET
        self.INFO_TEACHERINFO = EXCELTYPE_INFO_TEACHERINFO

        self.INFO_BASESUMMARY_PREVIEW = EXCELTYPE_INFO_BASESUMMARY_PREVIEW
        self.INFO_HUMANITY_PREVIEW = EXCELTYPE_INFO_HUMANITY_PREVIEW
        self.INFO_BASESUMMARYSCIENCE_PREVIEW = EXCELTYPE_INFO_BASESUMMARYSCIENCE_PREVIEW
        self.INFO_FRONT_PREVIEW = EXCELTYPE_INFO_FRONT_PREVIEW
        self.INFO_OUTSTANDING_PREVIEW = EXCELTYPE_INFO_OUTSTANDING_PREVIEW
        self.INFO_IMPORTANTPROJECT_PREVIEW = EXCELTYPE_INFO_IMPORTANTPROJECT_PREVIEW
        self.INFO_LABORATORY_PREVIEW = EXCELTYPE_INFO_LABORATORY_PREVIEW
        
        #终审
        self.INFO_FINAL_BASESUMMARY_PREVIEW         = EXCELTYPE_INFO_FINAL_BASESUMMARY_PREVIEW
        self.INFO_FINAL_HUMANITY_PREVIEW            = EXCELTYPE_INFO_FINAL_HUMANITY_PREVIEW
        self.INFO_FINAL_IMPORTANTPROJECT_PREVIEW    = EXCELTYPE_INFO_FINAL_IMPORTANTPROJECT_PREVIEW
        self.INFO_FINAL_LABORATORY_PREVIEW          = EXCELTYPE_INFO_FINAL_LABORATORY_PREVIEW
        self.INFO_FINAL_BASESUMMARYSCIENCE_PREVIEW  = EXCELTYPE_INFO_FINAL_BASESUMMARYSCIENCE_PREVIEW
        self.INFO_FINAL_FRONT_PREVIEW               = EXCELTYPE_INFO_FINAL_FRONT_PREVIEW
        self.INFO_FINAL_OUTSTANDING_PREVIEW = EXCELTYPE_INFO_FINAL_OUTSTANDING_PREVIEW

FileList={
    'file_application' : u"基本科研业务费专项项目申请书",
    'file_task' : u"基本科研业务费专项项目任务书",
    'file_interimchecklist' : u"基本科研业务费专项项目进展报告",
    'file_summary' : u"基本科研业务费专项项目结题报告",
    'file_other':u"其他",
}



NATIONAL_TRADE_CODE_CHOICES = (
    ('0',"A1 农业"),
    ('1',"A2 林业"),
    ('2',"A3 畜牧业"),
    ('3',"A4 渔业"),
    ('4',"A5 农、林、牧、渔服务业"),
    ('5',"B6 煤炭开采和洗选业"),
    ('6',"B7 石油和天然气开采业"),
    ('7',"B8 黑色金属矿采选业"),
    ('8',"B9 有色金属矿采选业"),
    ('9',"B10 非金属矿采选业"),
    ('10',"B11 开采辅助活动"),
    ('11',"B12 其他采矿业"),
    ('12',"C13 农副食品加工业"),
    ('13',"C14 食品制造业"),
    ('14',"C15 酒、饮料和精制茶制造业"),
    ('15',"C16 烟草制品业"),
    ('16',"C17 纺织业"),
    ('17',"C18 纺织服装、服饰业"),
    ('18',"C19 皮革、毛皮、羽毛及其制品和制鞋业"),
    ('19',"C20 木材加工和木、竹、藤、棕、草制品业"),
    ('20',"C21 家具制造业"),
    ('21',"C22 造纸和纸制品业"),
    ('22',"C23 印刷和记录媒介复制业"),
    ('23',"C24 文教、工美、体育和娱乐用品制造业"),
    ('24',"C25 石油加工、炼焦和核燃料加工业"),
    ('25',"C26 化学原料和化学制品制造业"),
    ('26',"C27 医药制造业"),
    ('27',"C28 化学纤维制造业"),
    ('28',"C29 橡胶和塑料制品业"),
    ('29',"C30 非金属矿物制品业"),
    ('30',"C31 黑色金属冶炼和压延加工业"),
    ('31',"C32 有色金属冶炼和压延加工业"),
    ('32',"C33 金属制品业"),
    ('33',"C34 通用设备制造业"),
    ('34',"C35 专用设备制造业"),
    ('35',"C36 汽车制造业"),
    ('36',"C37 铁路、船舶、航空航天和其他运输设备制造业"),
    ('37',"C38 电气机械和器材制造业"),
    ('38',"C39 计算机、通信和其他电子设备制造业"),
    ('39',"C40 仪器仪表制造业"),
    ('40',"C41 其他制造业"),
    ('41',"C42 废弃资源综合利用业"),
    ('42',"C43 金属制品、机械和设备修理业"),
    ('43',"D44 电力、热力生产和供应业"),
    ('44',"D45 燃气生产和供应业"),
    ('45',"D46 水的生产和供应业"),
    ('46',"E47 房屋建筑业"),
    ('47',"E48 土木工程建筑业"),
    ('48',"E49 建筑安装业"),
    ('49',"E50 建筑装饰和其他建筑业"),
    ('50',"F51 批发业"),
    ('51',"F52 零售业"),
    ('52',"G53 铁路运输业"),
    ('53',"G54 道路运输业"),
    ('54',"G55 水上运输业"),
    ('55',"G56 航空运输业"),
    ('56',"G57 管道运输业"),
    ('57',"G58 装卸搬运和运输代理业"),
    ('58',"G59 仓储业"),
    ('59',"G60 邮政业"),
    ('60',"H61 住宿业"),
    ('61',"H62 餐饮业"),
    ('62',"I63 电信、广播电视和卫星传输服务"),
    ('63',"I64 互联网和相关服务"),
    ('64',"I65 软件和信息技术服务业"),
    ('65',"J66 货币金融服务"),
    ('66',"J67 资本市场服务"),
    ('67',"J68 保险业"),
    ('68',"J69 其他金融业"),
    ('69',"K70 房地产业"),
    ('70',"L71 租赁业"),
    ('71',"L72 商务服务业"),
    ('72',"M73 研究和试验发展"),
    ('73',"M74 专业技术服务业"),
    ('74',"M75 科技推广和应用服务业"),
    ('75',"N76 水利管理业"),
    ('76',"N77 生态保护和环境治理业"),
    ('77',"N78 公共设施管理业"),
    ('78',"O79 居民服务业"),
    ('79',"O80 机动车、电子产品和日用产品修理业"),
    ('80',"O81 其他服务业"),
    ('81',"P82 教育"),
    ('82',"Q83 卫生"),
    ('83',"Q84 社会工作"),
    ('84',"R85 新闻和出版业"),
    ('85',"R86 广播、电视、电影和影视录音制作业"),
    ('86',"R87 文化艺术业"),
    ('87',"R88 体育"),
    ('88',"R89 娱乐业"),
    ('89',"S90 中国共产党机关"),
    ('90',"S91 国家机构"),
    ('91',"S92 人民政协、民主党派"),
    ('92',"S93 社会保障"),
    ('93',"S94 群众团体、社会团体和其他成员组织"),
    ('94',"S95 基层群众自治组织"),
    ('95',"T96 国际组织"),
)


SUBJECT_CHOICES = (    
    ('0',"110 数学"),
    ('1',"120 信息科学与系统科学"),
    ('2',"130 力学"),
    ('3',"140 物理学"),
    ('4',"150 化学"),
    ('5',"160 天文学"),
    ('6',"170 地球科学"),
    ('7',"180 生物学"),
    ('8',"190 心理学"),
    ('9',"210 农学"),
    ('10',"220 林学"),
    ('11',"230 畜牧、兽医科学"),
    ('12',"240 水产学"),
    ('13',"310 基础医学"),
    ('14',"320 临床医学"),
    ('15',"330 预防医学与公共卫生学"),
    ('16',"340 军事医学与特种医学"),
    ('17',"350 药学"),
    ('18',"360 中医学与中药学"),
    ('19',"410 工程与技术科学基础学科"),
    ('20',"413 信息与系统科学相关工程与技术"),
    ('21',"416 自然科学相关工程与技术"),
    ('22',"420 测绘科学技术"),
    ('23',"430 材料科学"),
    ('24',"440 矿山工程技术"),
    ('25',"450 冶金工程技术"),
    ('26',"460 机械工程"),
    ('27',"470 动力与电气工程"),
    ('28',"480 能源科学技术"),
    ('29',"490 核科学技术"),
    ('30',"510 电子与通信技术"),
    ('31',"520 计算机科学技术"),
    ('32',"530 化学工程"),
    ('33',"535 产品应用相关工程与技术"),
    ('34',"540 纺织科学技术"),
    ('35',"550 食品科学技术"),
    ('36',"560 土木建筑工程"),
    ('37',"570 水利工程"),
    ('38',"580 交通运输工程"),
    ('39',"590 航空、航天科学技术"),
    ('40',"610 环境科学技术及资源科学技术"),
    ('41',"620 安全科学技术"),
    ('42',"630 管理学"),
    ('43',"710 马克思主义"),
    ('44',"720 哲学"),
    ('45',"730 宗教学"),
    ('46',"740 语言学"),
    ('47',"750 文学"),
    ('48',"760 艺术学"),
    ('49',"770 历史学"),
    ('50',"780 考古学"),
    ('51',"790 经济学"),
    ('52',"810 政治学"),
    ('53',"820 法学"),
    ('54',"830 军事学"),
    ('55',"840 社会学"),
    ('56',"850 民族学与文化学"),
    ('57',"860 新闻学与传播学"),
    ('58',"870 图书馆、情报与文献学"),
    ('59',"880 教育学"),
    ('60',"890 体育科学"),
    ('61',"910 统计学"),
)



SUBJECT_DICTS = {
    110:'0',
    120:'1',
    130:'2',
    140:'3',
    150:'4',
    160:'5',
    170:'6',
    180:'7',
    190:'8',
    210:'9',
    220:'10',
    230:'11',
    240:'12',
    310:'13',
    320:'14',
    330:'15',
    340:'16',
    350:'17',
    360:'18',
    410:'19',
    413:'20',
    416:'21',
    420:'22',
    430:'23',
    440:'24',
    450:'25',
    460:'26',
    470:'27',
    480:'28',
    490:'29',
    510:'30',
    520:'31',
    530:'32',
    535:'33',
    540:'34',
    550:'35',
    560:'36',
    570:'37',
    580:'38',
    590:'39',
    610:'40',
    620:'41',
    630:'42',
    710:'43',
    720:'44',
    730:'45',
    740:'46',
    750:'47',
    760:'48',
    770:'49',
    780:'50',
    790:'51',
    810:'52',
    820:'53',
    830:'54',
    840:'55',
    850:'56',
    860:'57',
    870:'58',
    880:'59',
    890:'60',
    910:'61',
}

NATIONAL_TRADE_CODE_DICTS = {
    "A1" :'0',
    "A2" :'1',
    "A3" :'2',
    "A4" :'3',
    "A5" :'4',
    "B6" :'5',
    "B7" :'6',
    "B8" :'7',
    "B9" :'8',
    "B10":'9',
    "B11":'10',
    "B12":'11',
    "C13":'12',
    "C14":'13',
    "C15":'14',
    "C16":'15',
    "C17":'16',
    "C18":'17',
    "C19":'18',
    "C20":'19',
    "C21":'20',
    "C22":'21',
    "C23":'22',
    "C24":'23',
    "C25":'24',
    "C26":'25',
    "C27":'26',
    "C28":'27',
    "C29":'28',
    "C30":'29',
    "C31":'30',
    "C32":'31',
    "C33":'32',
    "C34":'33',
    "C35":'34',
    "C36":'35',
    "C37":'36',
    "C38":'37',
    "C39":'38',
    "C40":'39',
    "C41":'40',
    "C42":'41',
    "C43":'42',
    "D44":'43',
    "D45":'44',
    "D46":'45',
    "E47":'46',
    "E48":'47',
    "E49":'48',
    "E50":'49',
    "F51":'50',
    "F52":'51',
    "G53":'52',
    "G54":'53',
    "G55":'54',
    "G56":'55',
    "G57":'56',
    "G58":'57',
    "G59":'58',
    "G60":'59',
    "H61":'60',
    "H62":'61',
    "I63":'62',
    "I64":'63',
    "I65":'64',
    "J66":'65',
    "J67":'66',
    "J68":'67',
    "J69":'68',
    "K70":'69',
    "L71":'70',
    "L72":'71',
    "M73":'72',
    "M74":'73',
    "M75":'74',
    "N76":'75',
    "N77":'76',
    "N78":'77',
    "O79":'78',
    "O80":'79',
    "O81":'80',
    "P82":'81',
    "Q83":'82',
    "Q84":'83',
    "R85":'84',
    "R86":'85',
    "R87":'86',
    "R88":'87',
    "R89":'88',
    "S90":'89',
    "S91":'90',
    "S92":'91',
    "S93":'92',
    "S94":'93',
    "S95":'94',
    "T96":'95',
}

SCIENCE_ACTIVITY_TYPE_DICTS={
    u"基础研究"   :'0',
    u"应用研究"   :'1',
    u"试验发展"   :'2',
    u"科技服务"   :'3',
    u"R&D成果应用":'4',
}

SEX_DICTS={
    u"男":'0',
    u"女":'1',
}
PROJECT_IDENTITY_DICTS={
   u"教师"  :'0',
   u"本科生":'1',
   u"硕士生":'2',
   u"博士生":'3',
   u"博士后":'4',
   u"其他"  :'5',
}
DEGREE_DICTS={
   u"学士":'0',
   u"硕士":'1',
   u"博士":'2',
   u"其他":'3',
}
PROFESSIONAL_TITLE_DICTS ={
   u"正高级":'0',
   u"副高级":'1',
   u"中级"  :'2',
   u"其他"  :'3',
}
EXECUTIVE_POSITION_DICTS={
   u"校级"      :'0',
   u"院（系）级"  :'1',
   u"校部（处）级":'2',
   u"无"        :'3',
}
RESEARCH_BASES_TYPE_DICTS={
   u"国家（重点）实验室"                     :'0',
   u"教育部重点实验室"                     :'1',
   u"国家文科基础学科人才培养和科学研究基地":'2',
   u"其他省部级重点实验室"                 :'3',
   u"省部级以下重点实验室"                 :'4',
   u"无"                                  :'5',
}
