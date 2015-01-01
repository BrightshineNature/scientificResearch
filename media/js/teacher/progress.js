$(document).ready(function(){
    refresh_progress_history();
});

function refresh_progress_history(){
    var pid = $("#progress_form").attr("args");
    Dajaxice.teacher.refreshProgressHistory(refreshCallBack, {"pid": pid,});
}
function refreshCallBack(data){
    $("#progress_history_table").html(data);
}
$(".save_button").click(function(){
    var pid = $(this).attr("args");
    var report_content = $("#id_summary").val();
    Dajaxice.teacher.saveProgress(saveCallBack, {"pid": pid, "report_content": report_content, })
});
function saveCallBack(data){
    if(data == "ok"){
        refresh_progress_history();
    }
    else{
        alert("输入不能为空！");
    }
}

$(".submit_button").click(function(){
    var pid = $(this).attr("args");
    Dajaxice.teacher.submitProgress(submitCallBack, {"pid": pid, });
});
function submitCallBack(data){
    if(data.message == "empty report"){
        alert("本年度进展报告未填写！");
    }
    else{
        if(data.is_redirect){
            window.location.href = "/teacher/file_upload/" + data.pid;
        }
    }
}

var report_id;

$(document).on("click", ".progress_change", function(){
     report_id = $(this).attr("args");
    var year = $(this).parent().parent().find("td").eq(0).html();
    var content = $(this).parent().parent().find("td").eq(1).html();
    $(".modal-title").html(year);
    $(".modal-body #change_content").val(content);
});

$("#change_save_btn").click(function(){
    var report_content = $("#change_content").val();
    Dajaxice.teacher.changeProgress(changeCallBack, {"report_id": report_id, 
                                                      "report_content": report_content, });
});
function changeCallBack(data){
    if(data == "ok"){
        refresh_progress_history();
    }
    else{
        alert("修改内容不能为空!");
    }
}
