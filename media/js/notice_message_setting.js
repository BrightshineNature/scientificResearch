var mod;
$("#add_new_notice").click(function(){
    $("#notice_profile_info input").val('');
    $("#notice_profile_info textarea").val('');
    mod=-1;
});
$(document).on("click","#notice_paginator .item_page",function(){
    page=$(this).attr("arg");
    Dajaxice.adminStaff.getNoticePagination(get_notice_pagination_callback,{
        "page":page
    })
});
function get_notice_pagination_callback(data){
    $("#template_notice_table").html(data.table);
}
var tr;
$(document).on("click",".select_template_notice",function(){
    tr=$(this).closest("tr");
    $("#textarea").val($(tr).children("td:eq(2)").html());
});
$("#add_or_update_notice").click(function(){
    $("#template_notice_error_message").empty();
   Dajaxice.adminStaff.TemplateNoticeChange(add_or_update_notice_callback,{
        "template_form":$("#template_notice_info_form").serialize(true),
        "mod":mod,
        "page":1
    });
});
function add_or_update_notice_callback(data){
    if(data.status == "2") {
        $.each(data.error_id, function (i, item){
            object = $('#'+item);
            object.css("border-color", 'red');
        });
    }
    else if(data.status=="0"){
        $("#template_notice_table").html(data.table);
    }
    //$("#template_notice_error_message").append("<strong>"+data.message+"</strong>");
}
$(document).on("click",".delete_template_notice",function(){
    tr=$(this).closest("tr");
    mod=tr.attr("id");
});
$("#notice_delete_info").on("click","#delete_notice",function(){
     Dajaxice.adminStaff.TemplateNoticeDelete(add_or_update_notice_callback,{
        "deleteID":mod,
        "page":1
    });
});
$(document).on("click",".change_template_notice",function(){
    tr=$(this).closest("tr");
    mod=tr.attr("id");
    $("#id_title").val($(tr).children("td:eq(1)").html());
    $("#id_message").val($(tr).children("td:eq(2)").html());
});
$(document).on("click",".select_template_notice",function(){
    tr=$(this).closest("tr");
    $("#id_mail_content").val($(tr).children("td:eq(2)").html());
    $("#id_mail_title").val($(tr).children("td:eq(1)").html());
});
$("#teacher_chose").hide();
$("#expert_chose").hide();
$(document).on("click","#id_teacher",function(){
    if(this.checked===true){
        $("#teacher_chose").show(300);
    }
    else{
        $("#teacher_chose").hide(300);
    }
});
$(document).on("click","#id_expert",function(){
    if(this.checked===true){
        $("#expert_chose").show(300);
    }
    else{
        $("#expert_chose").hide(300);
    }
});
$("#send_mail").click(function(){
    Dajaxice.common.SendMail(send_mail_callback,{
        form:$("#noticemessage_form").serialize(true)
    });
});
$("#alert_close").click(function(){
    $("#noticemessage_warning").hide();
});
$("#alert_close1").click(function(){
    $("#noticemessage_success").hide();
});
$("#noticemessage_warning").hide();
$("#noticemessage_success").hide();
function send_mail_callback(data){
    alert(data.status);
    if(data.status==1){
        $("#error_message").html("邮件标题不能为空！");

    }
    else if(data.status==2){
        $("#error_message").html("邮件内容不能为空！");
    }
    else if(data.status==3){
        $("#error_message").html("没有符合要求接收者！");
    }
    if(data.status!==0){ $("#noticemessage_warning").show();
$("#noticemessage_success").hide();
}
else{
    $("#noticemessage_warning").hide();
    $("#noticemessage_success").show();
}


}
