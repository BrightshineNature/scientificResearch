var data=[
    {statics_type:"0",statics_grade_type:"1",statics_num:"20"}, 
    {statics_type:"1",statics_grade_type:"2",statics_num:"10"},
];
STATICS_TYPE={
    '0':"获奖（项）",
    '1':"专著／论文（篇）",
    '2':"专利及其它", 
    '3':"人才培养及学术交流", 
}
STATICS_PRIZE_TYPE={
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
}
STATICS_PAPER_TYPE={
    '0':"国际会议特邀报告",
    '1':"国际会议分组报告",
    '2':"全国性会议特邀报告", 
    '3':"全国性会议分组报告", 
    '4':"国际刊物", 
    '5':"国内核心刊物", 
    '6':"SCI", 
    '7':"EI", 
    '8':"ISTP",
    '9':"ISR", 
    '10':"中文已出版", 
    '11':"中文待出版",
    '12':"外文已出版", 
    '13':"外文待出版",
}
STATICS_PATENT_TYPE={
    '0':"国内申请",
    '1':"国内批准",
    '2':"国外申请", 
    '3':"国外批准", 
    '4':"可推广项数",
    '5':"已推广项数", 
    '6':"经济效益（万元）", 
    '7':"软件/数据库", 
    '8':"图表/图集", 
    '9':"新仪器/新方法",
    '10':"鉴定及其它", 
}
STATICS_SCHOLAR_TYPE={
    '0':"博士后在站",
    '1':"博士后出站",
    '2':"博士在读", 
    '3':"博士毕业", 
    '4':"硕士在读",
    '5':"硕士毕业", 
    '6':"中青年学术带头人(40岁以下)", 
    '7':"中青年学术带头人(40-50岁)", 
    '8':"国际次数", 
    '9':"国际人数",
    '10':"国内次数",
    '11':"国内人数", 
    '12':"出国参加国际学术会议人数次数",
    '13':"出国参加国际学术会议人数人数",
}

function add_staticsTr(obj)
{
    var tr=$("<tr></tr>");
    var table=$("#datastatics_change_table");
    tr.appendTo(table);
    var content = get_statictype_content(obj.statics_type);
    $("<td value="+obj.statics_type+">"+STATICS_TYPE[obj.statics_type]+"</td><td value="+obj.statics_grade_type+">"+content[obj.statics_grade_type]+"</td><td>"+obj.statics_num+"</td><td><button class='btn btn-success'>修改信息</button></td><td><button class='btn btn-danger' rel='news_delete'><i class='icon-trash icon-white'></i><span>删除</span></button>").appendTo(tr);
}
for(var i=0;i<data.length;++i)
{ 
    add_staticsTr(data[i]);
    //var tr=$("<tr></tr>");
    //var table=$("#member_change_table");
    //tr.appendTo(table);
    //$("<td>"+data[i].teacher_name+"</td><td>"+data[i].teacher_birth+"</td><td>"+data[i].teacher_tel+"</td><td>"+data[i].teacher_email+"</td><td>"+data[i].teacher_professional+"</td><td>"+data[i].teacher_duty+"</td><td><button class='btn btn-success'>修改信息</button></td><td><button class='btn btn-danger' rel='news_delete'><i class='icon-trash icon-white'></i><span>删除</span></button>").appendTo(tr);
    
}

$("#datastatics_change_table").on("click",".btn-danger",function(){
    $(this).closest("tr").remove();
        
});
var mod,tr;
$("#datastatics_change_table ").on("click",".btn-success",function(){
    mod=0;
    $(".modal-title").html("修改研究成果信息");
    $("#save_change").html("确认保存");
    $("#datastatics_profile_info").modal();
    tr=$(this).closest("tr");
    $("select[name='statics_type']").val($(tr).children("td:eq(0)").attr("value"));
    $("select[name='statics_grade_type']").val($(tr).children("td:eq(1)").attr("value"));
    $("input[name='statics_num']").val($(tr).children("td:eq(2)").html());

});
$("#add_new_datastatics").click(function(){
    
    $("#datastatics_change_form input").val('');
    $("#datastatics_change_form select").val(-1);
    mod=1;
    $(".modal-title").html("添加新数据");
    $("#datastatics_save_change").html("确认添加");
    $("#datastatics_profile_info").modal();
});

$("#datastatics_save_change").click(function(){
    var formData=$("#datastatics_change_form").serializeArray();
    var obj={};
    $.each(formData,function(i,field){
        obj[field.name]=field.value;
    });
    if(mod==1)
    {
        add_staticsTr(obj);

    }
    else
    {
        $(tr).children("td:eq(0)").html(STATICS_TYPE[obj.statics_type]);
        var content = get_statictype_content(obj.statics_type);
        $(tr).children("td:eq(1)").html(content[obj.statics_grade_type]); 
        $(tr).children("td:eq(2)").html(obj.statics_num);
        $(tr).children("td:eq(0)").attr({ "value":obj.statics_type});
        $(tr).children("td:eq(1)").attr({ "value":obj.statics_grade_type});
    }
});

function get_statictype_content(statictype)
{
    var content;
    switch(statictype)
    {
        case '0':
            content = STATICS_PRIZE_TYPE;
            break;
        case '1':
            content = STATICS_PAPER_TYPE;
            break;
        case '2':
            content = STATICS_PATENT_TYPE;
            break;
        case '3':
            content = STATICS_SCHOLAR_TYPE;
            break;
    } 
    return content;   
}
$("#statics_type").change(function(){
    var statics_type = $("#statics_type").val();
    var content = get_statictype_content(statics_type);
    var s = "<option selected="+"true" +"value='-1'>级别</option>";
    $.each(content,function(index,value){
        s+="<option value=" + index + ">" + content[index] + "</option>";
    });
    $("#statics_grade_type").html(s);    

});
