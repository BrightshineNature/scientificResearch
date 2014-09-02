var userstatus;
$("#budgetjudge").click(function(){

    userstatus="budget";
    var pid=$("#budgetForm").attr("pid");
    var value=$("#review_select").val();
    if(value!="-1"){
        Dajaxice.common.LookThroughResult(look_through_call_back,{
            "judgeid":pid,
            "page":-1,
            "page2":-1,
            "search":0,
            "searchForm":"",
            "userrole":"finance",
            "userstatus":"budget",
            "look_through_form":$("#budgetForm").serialize(true)
        });
    }

});
$("#finaljudge").click(function(){
    userstatus="final";
    var pid=$("#finalForm").attr("pid");
    var value=$("review_select").val();
    if(value!="-1"){
        Dajaxice.common.LookThroughResult(look_through_call_back,{
            "judgeid":pid,
             "page":-1,
            "page2":-1,
            "search":0,
            "searchForm":"","userrole":"finance",
            "userstatus":"final",
            "look_through_form":$("#finalForm").serialize(true)
        });
    }
});
function look_through_call_back(data){
    if(userstatus=="budget"){
        window.location.href="/finance";
    }
    if(userstatus=="final"){
        window.location.href="/finance/concludingProject"  ; 
    }
}
