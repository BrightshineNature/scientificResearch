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
        Dajaxice.Teacher.createProject(createProjectCallback, {"title": title,
                                                               "spcial": special,});
    }
});
function createProjectCallback(data){
    
}
