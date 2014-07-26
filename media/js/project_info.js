var judgeid,userrole,userstatus,projectstatus,applicationstatus_s,applicationstatus_c,finalstatus;
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

$("#judge").click(function(){
    judgeid=$(this).closest("tr").attr("iid");
    userrole=$(this).closest("table").attr("userrole");
    userstatus=$(this).closest("table").attr("userstatus");
    projectstatus=$(this).closest("tr").attr("status");
});
$("#commit").click(function(){

    var value=$("#review_select").val();
    if(value!=-1){
        Dajaxice.common.LookThroughResult(look_through_call_back,{
            "judgeid":judgeid,
            "userrole":userrole,
            "userstatus":userstatus,
            "look_through_form":$("#lookThroughForm").serialize(true)
        });
    }
    
});
function look_through_call_back(data){
    
}
