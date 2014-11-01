$(document).ready(function(){
    if($("#member_change_form").attr("arg") == "True"){
        $("#id_name").attr("readonly", "true");
        $("#id_card").attr("readonly", "true");
    }
});
$("button#setting_submit").click(function(){
    if($("input#id_base_name").val().trim().length == 0) $("input#id_base_name").val("无");
    return true;
});
