
$(".form-date").datetimepicker({
    weekStart:1,
    todayBtn: 1,
    autoclose: 1,
    todayHighlight:1,
    startView:2,
    forceParse:0,
    minView:2
});

function jump(cnt_content, cnt_tab){
    next_content = cnt_content.next();
    next_tab = cnt_tab.next();
    cnt_content.removeClass("active");
    cnt_tab.removeClass("active");
    next_content.addClass("active");
    next_tab.addClass("active");
}
$(document).on("click", ".save_button",function(){
    
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