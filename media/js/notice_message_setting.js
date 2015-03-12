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
    $("#id_message").val($(tr).children("td:eq(2)").children("span").attr("title"));
});
$(document).on("click",".select_template_notice",function(){
    tr=$(this).closest("tr");
    $("#id_mail_content").val($(tr).children("td:eq(2)").children("span").attr("title"));
    $("#id_mail_title").val($(tr).children("td:eq(1)").html());
});



// $("#teacher_chose").hide();
// $("#expert_chose").hide();
// $("#college_chose").hide();


// $(document).on("click","#id_college",function(){
//     if(this.checked==true){
//         $("#college_chose").show(300);
//     }
//     else{
//         $("#college_chose").hide(300);
//     }
// });
// $(document).on("click","#id_teacher",function(){
//     if(this.checked==true){
//         $("#teacher_chose").show(300);
//     }
//     else{
//         $("#teacher_chose").hide(300);
//     }
// });
// $(document).on("click","#id_expert",function(){
//     if(this.checked==true){
//         $("#expert_chose").show(300);
//     }
//     else{
//         $("#expert_chose").hide(300);
//     }
// });


var all_selected_receiver_name = new Array()
var all_selected_receiver_value = new Array()

function serialize_all_selected()
{
    var r = ""
    for(var i = 0; i < all_selected_receiver_name.length; ++ i)
    {
        if(i > 0) r += "&"
        r += all_selected_receiver_name[i]
        r += "=";
        r += all_selected_receiver_value[i]
    }
    return r;
}

function del(a, b)
{
    for(var i = 0; i < all_selected_receiver_name.length; ++ i)
    {
        if(all_selected_receiver_name[i] == a &&
            all_selected_receiver_value[i] == b)
        {
            all_selected_receiver_name.splice(i, 1);
            all_selected_receiver_value.splice(i, 1);
            return ;
        }
    }
}
function contain(a, b)
{
    for(var i = 0; i < all_selected_receiver_name.length; ++ i)
    {
        if(all_selected_receiver_name[i] == a &&
            all_selected_receiver_value[i] == b)
        {
            return true;
        }
    }
    return false;
}


$(document).on("click", ".checkbox_selected", function()
{
    if(this.checked)
    {
        all_selected_receiver_name.push($(this).attr("name"))
        all_selected_receiver_value.push($(this).attr("value"))
    }
    else 
    {
        del($(this).attr("name"), $(this).attr("value"))
    }

})


$(document).on("click" ,"#select_expert", function()
{
    form = $("#select_expert_form").serialize(true)
    // alert(form);
    Dajaxice.common.getSelectedExpert(getSelectedExpertCallback,{
        "form":form,
    });
})

function getSelectedExpertCallback(data){
    // alert(data.expert_table);
    $("#expert_list_form").html(data.expert_table)

}

$(document).on("click" ,"#select_teacher", function()
{
    form = $("#select_teacher_form").serialize(true)
    // alert(form);
    Dajaxice.common.getSelectedTeacher(getSelectedTeacherCallback,{
        "form":form,
    });
})

function getSelectedTeacherCallback(data){

    // alert(data.teacher_table)
    $("#teacher_list_form").html(data.teacher_table)

}



$(document).on("click", ".checkbox_select_all", function()
{
  var box = $(this).parents("table").find("input");

  for(var i = 0; i < box.length; ++ i) 
  {
    box[i].checked = this.checked;

  }
})

var cnt_user;
$(document).on("click", ".user_alloc_paginator .item_page", function()
{
    page = $(this).attr("arg");

    user = $(this).parents(".tab-pane").attr("id")
    cnt_user = user;
    Dajaxice.common.getUserListPagination(getUserListPaginationCallback,
        {"page":page, "user":user});

})

function getUserListPaginationCallback(data)
{
    $("#"+cnt_user+"_list_form").html(data.html);
    var box = $("#"+cnt_user+"_list_form").find("input")
    for(var i = 0; i < box.length; ++ i)
    {
        if(contain($(box[i]).attr("name"), $(box[i]).attr("value")))
        {
            box[i].checked = true
        }
    }

}

$("#alert_close").click(function(){
    $("#noticemessage_warning").hide();
});
$("#alert_close1").click(function(){
    $("#noticemessage_success").hide();
});
$("#noticemessage_warning").hide();
$("#noticemessage_success").hide();



$("#send_mail").click(function(){
    notice_form = $("#noticemessage_form").serialize(true)
    notice_form += "&"
    notice_form += serialize_all_selected()
    Dajaxice.common.SendMail(send_mail_callback,{
        "form":notice_form
    });
});
function send_mail_callback(data){
    if(data.status==1){
        $("#error_message").html("邮件标题不能为空！");

    }
    else if(data.status==2){
        $("#error_message").html("邮件内容不能为空！");
    }
    else if(data.status==3){
        $("#error_message").html("没有符合要求接收者！");
    }
    if(data.status!==0){ 
        $("#noticemessage_warning").show();
        $("#noticemessage_success").hide();
    }
    else{
        $("#noticemessage_warning").hide();
        $("#noticemessage_success").show();
    }
}

document.getElementById("id_college").checked=true;
document.getElementById("id_teacher").checked=true;
document.getElementById("id_expert").checked=true;
$("#id_college").hide();
$("#id_teacher").hide();
$("#id_expert").hide();



// $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) 
// {
//     // alert(e.target);
//     t = String(e.target).split("#");
//     // alert(t);
//     id = "id_" + t[t.length - 1];
//     // alert(id);
//     document.getElementById(id).checked=true;

//     t = String(e.relatedTarget).split("#");
//     previous_id = "id_" + t[t.length - 1];
//     // alert(previous_id);
//     document.getElementById(previous_id).checked=false;

//     // var previous_id = "id_" + e.relatedTarget
//   // alert(e.target); // newly activated tab
//     // alert(e.relatedTarget);
// })
