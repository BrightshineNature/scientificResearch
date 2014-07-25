var mod;
$("#add_new_notice").click(function(){
    $("#notice_profile_info input").val('');
    $("#notice_profile_info textarea").val('');
    mod=-1;
});
$(document).on("click","#notice_paginator .item_page",function(){
    page=$(this).attr("arg");
    Dajaxice.adminStaff.getNoticePagination(get_notice_pagination_callback,{
        "page":age
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
        "mod":mod
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
$(".table").on("click",".delete_template_notice",function(){
    tr=$(this).closest("tr");
    mod=tr.attr("id");
});
$("#notice_delete_info").on("click","#delete_notice",function(){
     Dajaxice.adminStaff.TemplateNoticeDelete(add_or_update_notice_callback,{
        "deleteID":mod
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
    $("#textarea").val($(tr).children("td:eq(2)").html());
});
