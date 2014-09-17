var glob_name;

$("#id_button_search").click(function(){
    glob_name = $("#id_name_input").val();   
    Dajaxice.adminStaff.getTeacherInfo(getTeacherInfoCallback, {'name': glob_name});
});

var glob_setting_id;

function getTeacherInfoCallback(data){
    $("#id_info_table").html(data.html);
}

$(document).on("click", "#id_modify_btn", function(){
    $("#id_input_name").val($(this).attr("arg1"));
    $("#id_input_card").val($(this).attr("arg2"));
    glob_setting_id = $(this).attr("arg3");
});

$(document).on("click", "#id_modify", function(){
    var name = $("#id_input_name").val();
    var card = $("#id_input_card").val();
    Dajaxice.adminStaff.modifyTeacherInfo(modifyTeacherInfoCallback, {"name": name, "card": card, "id": glob_setting_id, });
});
function modifyTeacherInfoCallback(data){
    if(data.message == "ok"){
        alert("修改成功");
        Dajaxice.adminStaff.getTeacherInfo(getTeacherInfoCallback, {'name': glob_name});
    }
    else alert(data.message);
}
