var pid;
$("#button_to_create").click(function(){
     $("#create_project_modal #id_title").removeAttr("style");
     $("#create_project_modal #id_title").val("");
});

$("#button_create_project").click(function(){
    title = $("#create_project_modal #id_title").val();
    special = $("#create_project_modal #id_special").val();
    if (title.length == 0){
        $("#create_project_modal #id_title").css("background", "red");
        $("#create_project_modal #id_title").val("输入名称不能为空");
    }
    else{
        $("#create-form").trigger("submit");
    }
});
$(document).on("click","#pro_delete_btn",function(){
    var tr=$(this).closest("tr");
    pid=tr.attr("pid");
});
$("#delete_pro").click(function(){
    Dajaxice.teacher.DeleteProject(procallback,{
        "pid":pid
    });
});
function procallback(){
    window.location.href="/teacher";   
};
$(document).on("change","#id_project_special",function(){
    var tr=$(this).closest("tr");
    pid=tr.attr("pid");
    var value=$(this).val();
    Dajaxice.teacher.ChangeSpecial(procallback,{
        "pid":pid,
        "value":value
    });
});
$().ready(function(){
  if($("#teacher_modal").length>0){
      $('#teacher_notice').modal('show');
  }
});


