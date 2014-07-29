
$(".form-date").datetimepicker({
    weekStart:1,
    todayBtn: 1,
    autoclose: 1,
    todayHighlight:1,
    startView:2,
    forceParse:0,
    minView:2
});

$(".form-year").datetimepicker({
    format:'yyyy',
    weekStart:1,
    // todayBtn: 1,
    autoclose: 1,
    startView: 4,

    // todayHighlight:1,
    // startView:2,
    // forceParse:0,
    minView:4,
});




$(document).on("click", "#addNewProjectMember", function(){

    $("input[name='name']").val("");
    $("input[name='birth_year']").val("");
    $("input[name='tel']").val("");
    $("input[name='mail']").val("");

    $("select[name='professional_title']").val("");
    $("select[name='executive_position']").val("");

    $(member_info_modal).attr("mid", "");

    $(member_info_modal).find("h4").text("添加项目成员");

})

$(document).on("click", "#saveProjectMember", function(){
    var pid = $(this).parents("[pid]").attr("pid");
    var form = $("#project_member_form").serialize();

    $(member_info_modal).find("h4").text("修改项目成员");

    // alert($(""));
    // alert(form);
    Dajaxice.common.saveProjectMember(saveProjectMemberCallback, {
        'form':form,
        'pid':pid,
        'mid':$(member_info_modal).attr("mid"),
    })
});

function saveProjectMemberCallback(data){

    // alert("SB");
    // alert(data.project_member_table);
    if(data.status == 1)
    {
        $('#project_member_table_div').html(data.project_member_table);
    }

}




$(document).on("click", ".modifyProjectMember", function(){
    var pid = $(this).parents("[pid]").attr("pid");
    var cnt = $(this).parent().parent();
    // alert(cnt.html());


    $(member_info_modal).attr("mid", $(cnt).attr("mid"));

    $("input[name='name']").val($(cnt).children("td:eq(0)").html());
    $("input[name='birth_year']").val($(cnt).children("td:eq(1)").html());
    $("input[name='tel']").val($(cnt).children("td:eq(2)").html());
    $("input[name='mail']").val($(cnt).children("td:eq(3)").html());

    $("select[name='professional_title']").val($(cnt).children("td:eq(4)").attr("value"));
    $("select[name='executive_position']").val($(cnt).children("td:eq(5)").attr("value"));


});

$(document).on("click", ".deleteProjectMember", function(){
    var cnt = $(this).parent().parent();

    Dajaxice.common.deleteProjectMember(deleteProjectMemberCallback,{
        'mid' : $(cnt).attr("mid"),
         
        })


});

function deleteProjectMemberCallback(data){
    if(data.status == 1)
    {
        $('#project_member_table_div').html(data.project_member_table);
    }

}



























function jump(cnt_content, cnt_tab){
    next_content = cnt_content.next();
    next_tab = cnt_tab.next();
    cnt_content.removeClass("active");
    cnt_content.removeClass("in");

    cnt_tab.removeClass("active");
    cnt_tab.removeClass("in");

    next_content.addClass("active");
    next_content.addClass("in");

    next_tab.addClass("active");
    next_tab.addClass("in");
}


$(document).on("click", ".save_button",function(){
    // alert("TT");
    
    var cnt_content = $(this).parent();
    
    var pid = $(this).parents("[pid]").attr("pid");
    // alert(pid);
    if($(cnt_content).attr("id") == "project_info_form")
    {
        var cnt_tab = $(this).parent().parent().prev().children("li:eq(0)");        
        jump(cnt_content, cnt_tab);    
        
        

        // alert($("#project_info_form").children("form").serialize());
        Dajaxice.common.saveProjectInfoForm(saveProjectInfoFormCallback,{
            'form': $("#project_info_form").children("form").serialize(),
            'pid': pid,
        })

    }
    else if($(cnt_content).attr("id") == "project_member")
    {
        var cnt_tab = $(this).parent().parent().prev().children("li:eq(1)");
        jump(cnt_content, cnt_tab);
    }
    else if($(cnt_content).attr("id") == "basis_content")
    {
        var cnt_tab = $(this).parent().parent().prev().children("li:eq(2)");
        jump(cnt_content, cnt_tab);

        Dajaxice.common.saveBasisContent(saveBasisContentCallback,{
            'form': $("#basis_content_form").serialize(),
            'pid': pid,
            'bid': $("#basis_content_form").attr("bid"),
        })
    }
    else if($(cnt_content).attr("id") == "base_condition")
    {
        var cnt_tab = $(this).parent().parent().prev().children("li:eq(3)");
        
        user = $("[user]").attr("user");
        alert(user);
        location.href = "/" + user + "/file_upload/" + pid;

        // alert($("#base_condition_form").attr("bid"));
        Dajaxice.common.saveBaseCondition(saveBaseConditionCallback,{
            'form': $("#base_condition_form").serialize(),
            'pid': pid,
            'bid': $("#base_condition_form").attr("bid"),
        })
    }

});

function saveProjectInfoFormCallback(data) {

}
function saveBasisContentCallback(data) {

}
function saveBaseConditionCallback(data){

}