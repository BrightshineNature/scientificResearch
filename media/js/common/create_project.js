$("#button_create_project").click(function(){
    title = $("#create-form #id_title").val();
    if (title.length == 0){
        $("#create-form #id_title").css("background", "red");
        alert("项目名称不能为空");
    }
    else{
        Dajaxice.adminStaff.CreateProject(CreateProject_callback,{'form':$(this).parents("form").serialize(true)});
    }
});
function CreateProject_callback(data){
  if (data.status == "1"){
    $("#create-form #id_title").val("");
  }
  alert(data.message);
}
