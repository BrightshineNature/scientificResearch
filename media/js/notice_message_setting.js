var mod;
$("#add_new_notice").click(function(){
    $("#notice_profile_info input").val('');
    $("#notice_profile_info textarea").val('');
    mod=1;
});
var button_group_html= '<div class="btn-group"> <button class="btn btn-primary" id="select_template_notice">选择</button> <button class="btn btn-success" data-toggle="modal" data-target="#notice_profile_info" id="change_template_notice">修改</button><button class="btn btn-info"  data-toggle="modal" data-target="#notice_delete_info" id="delete_template_notice">删除</button></div>';

var tr,cnt=0;
$(".table").on("click","#select_template_notice",function(){
    tr=$(this).closest("tr");
    $("#textarea").val($(tr).children("td:eq(2)").html());
});
$("#add_or_update_notice").click(function(){
    if(mod==1)
        {
            tr=$("<tr></tr>");
            var table=$("#temlate_notice_table table");
            tr.appendTo(table);
            cnt++;
            $('<td>'+cnt+'</td><td>'+$("#message_title").val()+'</td><td>'+$("#message_content").val()+'</td><td>'+button_group_html+'</td>').appendTo(tr);
        }
        else
            {
                $(tr).children("td:eq(1)").html($("#message_title").val());
                $(tr).children("td:eq(2)").html($("#message_content").val());
            }
});
$(".table").on("click","#delete_template_notice",function(){
    tr=$(this).closest("tr");
});
$("#notice_delete_info").on("click","#delete_notice",function(){
    $(tr).remove();
});
$(".table").on("click","#change_template_notice",function(){
    mod=0;
    tr=$(this).closest("tr");
    $("#message_title").val($(tr).children("td:eq(1)").html());
    $("#message_content").val($(tr).children("td:eq(2)").html());
})
