
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



function jump(cnt_content, cnt_tab){
    next_content = cnt_content.next();
    next_tab = cnt_tab.next();
    cnt_content.removeClass("active");
    cnt_tab.removeClass("active");
    next_content.addClass("active");
    next_tab.addClass("active");
}



$(document).on("click", "#saveProjectMember", function(){
    var pid = $(this).parents("[pid]").attr("pid");
    var form = $("#project_member_form").serialize();
    alert($(""));
    alert(form);
    Dajaxice.common.saveProjectMember(saveProjectMemberCallback, {
        'form':form,
        'pid':pid,
    })


});

function saveProjectMemberCallback(){

}
$(document).on("click", ".save_button",function(){
    alert("TT");
    
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
        }
            )




    }

});

function saveProjectInfoFormCallback(data) {

}