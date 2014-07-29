var data=[{teacher_name:"胡俊",teacher_birth:"1888",teacher_tel:"21314234",teacher_email:"fdf@dgf.com",teacher_professional:"2",teacher_duty:"2"}, 
   {teacher_name:"胡俊",teacher_birth:"1888",teacher_tel:"21314234",teacher_email:"fdf@dgf.com",teacher_professional:"2",teacher_duty:"2"}
];
PROFESSIONAL_TITLE={
    '0':"正高级",
    '1':"副高级",
    '2':"中级",
    '3':"其他"
}
EXECUTIVE_POSITION={
    '0':"校级",
    '1':"院（系）级",
    '2':"校部（处）级",
    '3':"无"
}
function addTr(obj)
{
    var tr=$("<tr></tr>");
    var table=$("#member_change_table");
    tr.appendTo(table);
    $("<td>"+obj.teacher_name+"</td><td>"+obj.teacher_birth+"</td><td>"+obj.teacher_tel+"</td><td>"+obj.teacher_email+"</td><td value="+obj.teacher_professional+">"+PROFESSIONAL_TITLE[obj.teacher_professional]+"</td><td value="+obj.teacher_duty+">"+EXECUTIVE_POSITION[obj.teacher_duty]+"</td><td><button class='btn btn-success'>修改信息</button></td><td><button class='btn btn-danger' rel='news_delete'><i class='icon-trash icon-white'></i><span>删除</span></button>").appendTo(tr);
}
for(var i=0;i<data.length;++i)
{ 
    addTr(data[i]);
    //var tr=$("<tr></tr>");
    //var table=$("#member_change_table");
    //tr.appendTo(table);
    //$("<td>"+data[i].teacher_name+"</td><td>"+data[i].teacher_birth+"</td><td>"+data[i].teacher_tel+"</td><td>"+data[i].teacher_email+"</td><td>"+data[i].teacher_professional+"</td><td>"+data[i].teacher_duty+"</td><td><button class='btn btn-success'>修改信息</button></td><td><button class='btn btn-danger' rel='news_delete'><i class='icon-trash icon-white'></i><span>删除</span></button>").appendTo(tr);
    
}

$("#member_change_table").on("click",".btn-danger",function(){
    $(this).closest("tr").remove();
        
});
var mod,tr;
$("#member_change_table ").on("click",".btn-success",function(){
    mod=0;
    $(".modal-title").html("修改教师信息");
    $("#save_change").html("确认保存");
    $("#teacher_profile_info").modal();
    tr=$(this).closest("tr");
    $("input[name='teacher_name']").val($(tr).children("td:eq(0)").html());
    $("input[name='teacher_birth']").val($(tr).children("td:eq(1)").html());
    $("input[name='teacher_tel']").val($(tr).children("td:eq(2)").html());
    $("input[name='teacher_email']").val($(tr).children("td:eq(3)").html());
    $("select[name='teacher_professional']").val($(tr).children("td:eq(4)").attr("value"));
    $("select[name='teacher_duty']").val($(tr).children("td:eq(5)").attr("value"));

});
$("#add_new_member").click(function(){

    // alert("SSBB");
    
    // $("#member_change_form input").val('');
    // $("#member_change_form select").val(-1);
    // mod=1;
    // $(".modal-title").html("添加教师");
    // $("#save_change").html("确认添加");
    // $("#teacher_profile_info").modal();
});
$("#save_change").click(function(){
    var formData=$("#member_change_form").serializeArray();
    var obj={};
    $.each(formData,function(i,field){
        obj[field.name]=field.value;
    });
    if(mod==1)
    {
        addTr(obj);

    }
    else
    {
        $(tr).children("td:eq(0)").html(obj.teacher_name);  
        $(tr).children("td:eq(1)").html(obj.teacher_birth);
        $(tr).children("td:eq(2)").html(obj.teacher_tel);
        $(tr).children("td:eq(3)").html(obj.teacher_email);
        $(tr).children("td:eq(4)").html(PROFESSIONAL_TITLE[obj.teacher_professional]);
        $(tr).children("td:eq(5)").html(EXECUTIVE_POSITION[obj.teacher_duty]);
        $(tr).children("td:eq(4)").attr({ "value":obj.teacher_professional});
        $(tr).children("td:eq(5)").attr({ "value":obj.teacher_duty});

    }
});
//$("#teacher_profile_info").on("shown.bs.modal",function(e){
    //$("#modal_title").text("修改教师信息");
    //$("#save_change").html("保存");
//});
