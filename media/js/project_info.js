var judgeid,userrole,userstatus,projectstatus,applicationstatus_s,applicationstatus_c,finalstatus;
var search=0;
var glo_project_id;
$("#not_pass_reason").hide();
$("#not_pass_article").hide();
$("#id_judgeresult").css("color","gray");
$("#id_judgeresult").change(function(){
    if($(this).val()=="-1")
    {
        $(this).css("color","gray");
    }
    else
    {
        $(this).css("color","black");
    }
    if($(this).val()=="0")
    {
        $("#not_pass_reason").show(500);
        if(projectstatus==applicationstatus_s||projectstatus==applicationstatus_c||projectstatus==finalstatus){
        $("#not_pass_article").show(500);
        }   

    }
    else
    {
        $("#not_pass_reason").hide(500);
        $("#not_pass_article").hide(500);
    }

});
Dajaxice.common.getStatus(function(data){
    applicationstatus_s=data.application_s;
    applicationstatus_c=data.application_c;
    finalstatus=data.final;
},{});

$(document).on("click","[name='judge']",function(){
    judgeid=$(this).closest("tr").attr("iid");
    projectstatus=$(this).closest("tr").attr("status");
});
$("#commit").click(function(){

    var value=$("#id_judgeresult").val();
    userrole=$(".tab-content").attr("userrole");
    userstatus=$(".tab-content").attr("userstatus");
    if(value!=-1){
        Dajaxice.common.LookThroughResult(look_through_call_back,{
            "judgeid":judgeid,
            "userrole":userrole,
            "userstatus":userstatus,
            "page":$("#not_pass_paginator .disabled").attr("value"),
            "page2":$("#pass_paginator .disabled").attr("value"),
            "search":search,
            "look_through_form":$("#lookThroughForm").serialize(true),
            "searchForm":$("#schedule_form").serialize(true)
        });
    }
    
});
function look_through_call_back(data){
    if(userstatus=="application"){
        $("#applicationTable").html(data.table_html);
    } 
    else{
        $("#researchTable").html(data.table_html);
    }

}
$('td a[href="#project_code_add"]').click(function(){
  glo_project_id = $(this).attr('pid');
  var project_unique_code = $(this).parent().text().trim();
  $('#project_code_add').find('#project_code').val(project_unique_code);
})
$('#project_code_submit').click(function(){
  var project_unique_code = $('#project_code_add').find('#project_code').val().trim();
  Dajaxice.adminStaff.change_project_unique_code(change_projectuniquecode_callback,{'project_id':glo_project_id,"project_unique_code":project_unique_code});
})
function change_projectuniquecode_callback(data){
    if(data.res == "error"){
        alert("格式不合法或相同编号已存在");
    }
    else{
        var target = "#ProjectUniqueCode_" + glo_project_id;
        $(target).html(data.res);
    }
}
function getPagination(page,page2){
    userrole=$(".tab-content").attr("userrole");
    userstatus=$(".tab-content").attr("userstatus");
    
    Dajaxice.common.getPagination(getPaginationCallBack,{
        "page":page,
        "page2":page2,
        "userrole":userrole,
        "userstatus":userstatus,
        "search":search,
        "form":$("#schedule_form").serialize(true)
    });  
}
function getPaginationCallBack(data){
        $("#not_pass").html(data.table_not_pass);
        $("#pass").html(data.table_pass);
}

   
$(document).on("click","#not_pass_paginator .item_page",function(){
    page=$(this).attr("arg");
    page2=$("#pass_paginator .disabled").attr("value");
    getPagination(page,page2); 
});

$(document).on("click","#pass_paginator .item_page",function(){
    page2=$(this).attr("arg");
    
    page=$("#not_pass_paginator .disabled").attr("value");
    getPagination(page,page2); 
});
$("#filter_button").click(function(){
    search=1;
    getPagination(1,1);

});
