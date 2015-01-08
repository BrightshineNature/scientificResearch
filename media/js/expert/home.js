function is_first_round(){
    var label = $(".nav-pills li.active").attr("args");
    return (label == "first_round");
}

var special = "-1", college = "-1";

$(".nav-pills a").click(function(){
    special = "-1";
    college = "-1";
    $("#id_special").val("-1");
    $("#id_college").val("-1");
});
$("#project_filter_button").click(function(){
    special = $("#id_special").val();
    college = $("#id_college").val();
    get_project_list("1", is_first_round());
});


$(document).on("click", "#first_round_paginator .item_page", function(){
    page = $(this).attr("arg");
    get_project_list(page, true);
});
$(document).on("click", "#second_round_paginator .item_page", function(){
    page = $(this).attr("arg");
    get_project_list(page, false);
});

function get_project_list(page, is_first_round){
    Dajaxice.expert.getPagination(getPaginationCallback, {"special": special, "college": college, "page": page, "is_first_round": is_first_round,});
}
function getPaginationCallback(data){
    if(data.message == "first round"){
        $("#first-round-section").html(data.html);          
    }
    else{
        $("#second-round-section").html(data.html);
    }
}

