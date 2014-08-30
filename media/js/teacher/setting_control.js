$(document).ready(function(){
    if($("#member_change_form").attr("arg") == "True"){
        $("#id_name").attr("readonly", "true");
        $("#id_card").attr("readonly", "true");
    }
});
