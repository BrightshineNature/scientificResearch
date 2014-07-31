STATICS_DATA_TYPE={
    '0':"国家级自然科学一等奖",
    '1':"国家级自然科学二等奖",
    '2':"国家级科技进步一等奖", 
    '3':"国家级科技进步二等奖", 
    '4':"国家级发明一等奖", 
    '5':"国家级发明二等奖", 
    '6':"省部级自然科学一等奖", 
    '7':"省部级自然科学二等奖", 
    '8':"省部级科技进步一等奖",
    '9':"省部级科技进步二等奖", 
    '10':"国际学术奖", 
    '11':"其它",
    '12':"国际会议特邀报告",
    '13':"国际会议分组报告",
    '14':"全国性会议特邀报告", 
    '15':"全国性会议分组报告", 
    '16':"国际刊物", 
    '17':"国内核心刊物", 
    '18':"SCI", 
    '19':"EI", 
    '20':"ISTP",
    '21':"ISR", 
    '22':"中文已出版", 
    '23':"中文待出版",
    '24':"外文已出版", 
    '25':"外文待出版",
    '26':"国内申请",
    '27':"国内批准",
    '28':"国外申请", 
    '29':"国外批准", 
    '30':"可推广项数",
    '31':"已推广项数", 
    '32':"经济效益（万元）", 
    '33':"软件/数据库", 
    '34':"图表/图集", 
    '35':"新仪器/新方法",
    '36':"鉴定及其它",
    '37':"博士后在站",
    '38':"博士后出站",
    '39':"博士在读", 
    '40':"博士毕业", 
    '41':"硕士在读",
    '42':"硕士毕业", 
    '43':"中青年学术带头人(40岁以下)", 
    '44':"中青年学术带头人(40-50岁)", 
    '45':"国际次数",
    '46':"国际人数",
    '47':"国内次数",
    '48':"国内人数", 
    '49':"出国参加国际学术会议人数次数",
    '50':"出国参加国际学术会议人数人数", 
}
var datastaticsid,tr;
$("#datastatics_change_table").on("click",".btn-danger",function(){
    var pid = $("#datastatics_change_table").attr("value");
    var is_submited = $("#datastatics_change_table").attr("is_submited");
    tr=$(this).closest("tr");
    datastaticsid=$(tr).attr("value")
    Dajaxice.teacher.datastaticsDelete(delete_datastatics_callback,{'datastaticsid':datastaticsid,'pid':pid,'is_submited':is_submited,}); 
        
});

function delete_datastatics_callback(data){

    $("#datastatics_change_table").html(data.table);
    alert(data.message);    
}

$("#datastatics_change_table ").on("click",".btn-success",function(){
    $(".modal-title").html("修改数据信息");
    $("#datastatics_save_change").html("确认保存");
    $("#datastatics_profile_info").modal();
    tr=$(this).closest("tr");
    datastaticsid=$(tr).attr("value")
    $("select[name='staticstype']").val($(tr).children("td:eq(0)").attr("value"));
    change_staticsdatatype();
    $("select[name='staticsdatatype']").val($(tr).children("td:eq(1)").attr("value"));
    $("input[name='statics_num']").val($(tr).children("td:eq(2)").html());

});
$("#add_new_datastatics").click(function(){
    datastaticsid=0;
    $(".modal-title").html("添加新数据");
    $("#datastatics_save_change").html("确认添加");
    $('#datastatics_change_form')[0].reset();
    change_staticsdatatype();    
    $("#datastatics_profile_info").modal();
});

$("#datastatics_save_change").click(function(){
    var pid = $("#datastatics_change_table").attr("value");
    var is_submited = $("#datastatics_change_table").attr("is_submited");
    Dajaxice.teacher.datastaticsChange(add_or_update_datastatics_callback,
                                {   
                                    'form': $('#datastatics_change_form').serialize(true),
                                    'datastaticsid': datastaticsid,
                                    'pid':pid,
                                    'is_submited':is_submited,       
                            });
});

function add_or_update_datastatics_callback(data){

    $("#datastatics_change_table").html(data.table);
    alert(data.message);
}

$("#id_staticstype").change(function(){
    change_staticsdatatype();
});

function change_staticsdatatype(){
    var statics_type = $("#id_staticstype").val();
    Dajaxice.teacher.staticsChange(staticschange_callback,
                                {   
                                    'statics_type':statics_type,       
                            });
}

function staticschange_callback(data){
    var content = data.staticsdatatype;
    var s = "";
    $.each(content,function(index,value){
        s+="<option value=" + value + ">" + STATICS_DATA_TYPE[value] + "</option>";
    });
    $("#id_staticsdatatype").html(s);
}


$('#finalreport_finish').click(function(){
    var pid =$(this).attr("pid");
	Dajaxice.teacher.finalReportFinish(finalreportfinish_callback,{'pid':pid,});
});

function finalreportfinish_callback(data){
	alert(data.message);
    location.href = "/teacher/file_upload/"+data.pid;
}
