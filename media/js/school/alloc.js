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
    $("#id_div_expert").hide();

});
$("#unalloc_tab").click(function(){
    $("#button_operator_cancel").hide(); 
    $("#button_operator_alloc").show();
    $("#id_div_expert").show();
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
                                                            "special_id": glob_project_special_id,
                                                            "path": glob_path,});
});
function getProjectListCallback(data){
    $("#alloced-section").html(data.html_alloc);
    $("#unalloced-section").html(data.html_unalloc);
}


$(document).on("click", "#unalloc_paginator .item_page", function(){
    page = $(this).attr("arg");   
    Dajaxice.school.getUnallocProjectPagination(getUnallocCallback, {"page": page,
                                                                     "college_id": glob_project_college_id,
                                                                     "special_id": glob_project_special_id,
                                                                     "path": glob_path,}); 
});
function getUnallocCallback(data){
    $("#unalloced-section").html(data.html);
}

$(document).on("click", "#alloc_paginator .item_page", function(){
    page = $(this).attr("arg");   
    Dajaxice.school.getAllocProjectPagination(getAllocCallback, {"page": page,
                                                                 "college_id": glob_project_college_id,
                                                                 "special_id": glob_project_special_id,
                                                                 "path": glob_path,}); 

});
function getAllocCallback(data){
    $("#alloced-section").html(data.html);
}

var glob_expert_college_id = "-1";

$(document).on("click", "#alloc_expert_paginator .item_page", function(){
    page = $(this).attr("arg");
    Dajaxice.school.getAllocExpertPagination(getAllocExpertCallback, {"page": page,
                                                                      "id": glob_expert_college_id,
                                                                      "path": glob_path,});
});
function getAllocExpertCallback(data){
    $("#expert_list_div").html(data.html);
}

$("#expert_filter_button").click(function(){
    glob_expert_college_id = $("#expert_filter_form #id_colleges").val();
    Dajaxice.school.getExpertList(getExpertListCallback, {"id": glob_expert_college_id, 
                                                          "path": glob_path,});
});
function getExpertListCallback(data){
    $("#expert_list_div").html(data.html);
}

function refresh(){
    var page1 = $("#alloc_expert_paginator .disabled").val()
    var page2 = $("#alloc_paginator .disabled").val()
    var page3 = $("#unalloc_paginator .disabled").val()
    Dajaxice.school.getUnallocProjectPagination(getUnallocCallback, {"page": page3,
                                                                     "college_id": glob_project_college_id,
                                                                     "special_id": glob_project_special_id,
                                                                     "path": glob_path, }); 
    Dajaxice.school.getAllocProjectPagination(getAllocCallback, {"page": page2,
                                                                     "college_id": glob_project_college_id,
                                                                     "special_id": glob_project_special_id,
                                                                     "path": glob_path,}); 

    Dajaxice.school.getAllocExpertPagination(getAllocExpertCallback, {"page": page1,
                                                                      "id": glob_expert_college_id,
                                                                      "path": glob_path,});

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
    Dajaxice.school.allocProjectToExpert(allocProjectToExpertCallback, {"project_list": project_list,
                                                                        "expert_list": expert_list,
                                                                        "path": glob_path,});
});

function allocProjectToExpertCallback(data){
    if(data.message == "ok"){
        refresh();
        alert("分配成功！");
    }
    else if(data.message == "no project"){
        alert("选中的项目集合为空！");
    }
    else{
        alert("选中的评审集合为空！");
    }
}


$("#button_operator_cancel button").click(function(){
    var project_list = []
    $("input[name='checkbox_alloc_project']:checkbox:checked").each(function(){ 
        project_list.push($(this).val());
    });
    Dajaxice.school.cancelProjectAlloc(cancelProjectAllocCallback, {"project_list": project_list,
                                                                    "path": glob_path,});
});
function cancelProjectAllocCallback(data){
    if(data.message == "ok"){
        refresh();
        alert("操作成功！");
    }
    else{
        alert("选中的项目集合为空！");
    }
}

$(document).on("click", ".query_info", function(){
    project_id = $(this).attr("arg");
    Dajaxice.school.queryAllocedExpert(queryAllocedExpertCallback, {"project_id": project_id, 
                                                                    "path": glob_path,});
});
function queryAllocedExpertCallback(data){
    $("#query_modal .modal-body").html(data.html);
}
