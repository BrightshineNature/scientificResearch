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
        $("#not_pass_article").show(500);

    }
    else
    {
        $("#not_pass_reason").hide(500);
        $("#not_pass_article").hide(500);
    }

});
var judgeid,userrole;
$("#judge").click(function(){
    judgeid=$(this).closest("tr").attr("iid");
    userrole=$(this).closest("table").attr("userrole");
});
$("#commit").click(function(){

    var value=$("#review_select").val();
    if(value!=-1){
        $.get("/"+userrole+"/"+judgeid+"/"+value,function(){});
    }

    location.reload();

});
