if(!String.prototype.format) {
    String.prototype.format = function() {
        var args = arguments;
        return this.replace(/{(\d+)}/g, function(match, number) {
            return typeof args[number] != 'undefined'
                ? args[number] : match;
        });
    };
}

var glob_path;

$(document).ready(function(){
    $("#button_operator_cancel").hide(); 

    glob_path = window.location.pathname.split('/')[2];
});

$("#alloc_tab").click(function(){
    $("#button_operator_cancel").show();
    $("#button_operator_alloc").hide();
});
$("#unalloc_tab").click(function(){
    $("#button_operator_cancel").hide(); 
    $("#button_operator_alloc").show();
});


$(document).on("click", ".select_all", function(){
    var state = this.checked;
    target = "[name='{0}']".format($(this).attr("arg"));
    $(target).each(function(){
        this.checked = state;  
    });
});

var glob_project_college_id = "-1";
var glob_project_special_id = "-1";

$("#project_filter_button").click(function(){
    glob_project_college_id = $("#project_filter_form #id_colleges").val();
    glob_project_special_id = $("#project_filter_form #id_specials").val();
    Dajaxice.school.getProjectList(getProjectListCallback, {"college_id": glob_project_college_id, 
                                                          "special_id": glob_project_special_id,});
});
function getProjectListCallback(data){
    $("#alloced-section").html(data.html_alloc);
    $("#unalloced-section").html(data.html_unalloc);
}


$(document).on("click", "#unalloc_paginator .item_page", function(){
    page = $(this).attr("arg");   
    Dajaxice.school.getUnallocProjectPagination(getUnallocCallback, {"page": page}); 
});
function getUnallocCallback(data){
    $("#unalloced-section").html(data.html);
}

$(document).on("click", "#alloc_paginator .item_page", function(){
    page = $(this).attr("arg");   
    Dajaxice.school.getAllocProjectPagination(getAllocCallback, {"page": page}); 
});
function getAllocCallback(data){
    $("#alloced-section").html(data.html);
}

var glob_expert_college_id = "-1";

$(document).on("click", "#alloc_expert_paginator .item_page", function(){
    page = $(this).attr("arg");
    Dajaxice.school.getAllocExpertPagination(getAllocExpertCallback, {"page": page,
                                                                      "id": glob_expert_college_id,});
});
function getAllocExpertCallback(data){
    $("#expert_list_div").html(data.html);
}

$("#expert_filter_button").click(function(){
    glob_expert_college_id = $("#expert_filter_form #id_colleges").val();
    Dajaxice.school.getExpertList(getExpertListCallback, {"id": glob_expert_college_id, });
});
function getExpertListCallback(data){
    $("#expert_list_div").html(data.html);
}

$("#button_operator_alloc button").click(function(){
    var expert_list = []
    var project_list = []
    $("input[name='checkbox_expert']:checkbox:checked").each(function(){ 
        expert_list.push($(this).val());
    });
    $("input[name='checkbox_unalloc_project']:checkbox:checked").each(function(){ 
        project_list.push($(this).val());
    });
    alert(expert_list);
    alert(project_list);
});



