function projectfundsummary(){
    var pid = $("#mainTable").attr("value");
    var total_budget = parseFloat($('#id_total_budget').val());
    var laborcosts_budget = parseFloat($('#id_laborcosts_budget').val());
    var max_budget = parseFloat($('#max_budget').val()); 
    var projectcode = $("#project_code").val();
    var finance_account = $("#summary_finance_account").val();
    Dajaxice.teacher.fundSummary(fundSummary_callback,
                                    {
                                        'form': $('#project_fundsuammary_form').serialize(true),
                                        'pid':pid,
                                        'finance_account':finance_account
                                });
}

function fundSummary_callback(data){
    alert(data.message);
    if (data.flag) {
        $('#li_auditing').removeClass('active');
        $('#auditing').removeClass('active in');
        $('#li_achivement').addClass('active');        
        $('#achivement').addClass('active in');
    };

}

$('#fundsummary_next').click(function(){
    $('#li_auditing').removeClass('active');        
    $('#auditing').removeClass('active in');
    $('#li_achivement').addClass('active');        
    $('#achivement').addClass('active in');
});
var totalbudget = 0.0;
var totalexpenditure = 0.0;
$("table[name='budgettable']").find("input").bind('change',function(){
    totalbudget = 0;
    totalexpenditure = 0;
    index = 0;
    //alert($(this).attr("id"));
    var cellindex = this.parentNode.cellIndex;
    if(cellindex < 2){
    if($(this).val()<0||isNaN($(this).val()))
    {
        alert("数据格式不对,请重新输入");
        $(this).val(0.0);
    }
    $(" table[name='budgettable'] tbody tr").each(function(){
        if(index > 0 && index < 13){
            //alert($(this).find("td").eq(1).children().val()+' '+index)
            totalbudget += parseFloat($(this).find("td").eq(1).children().val());
            //totalexpenditure += parseFloat($(this).find("td").eq(2).children().val());
        }
        index += 1;
    });
    $("#id_total_budget").val(parseFloat(totalbudget));
    }
});

$("table[name='fundsummarytable']").find("input").bind('change',function(){
    totalbudget = 0;
    totalexpenditure = 0;
    index = 0;
    //alert($(this).attr("id"));
    var cellindex = this.parentNode.cellIndex;
    if(cellindex < 3){
    if($(this).val()<0||isNaN($(this).val()))
    {
        alert("数据格式不对,请重新输入");
        $(this).val(0.0);
    }
    $(" table[name='fundsummarytable'] tbody tr").each(function(){
        //alert($(this).find("td").eq(1).children().val()+' '+index)
        if(index > 0 && index < 13){
            totalbudget += parseFloat($(this).find("td").eq(1).children().val());
            totalexpenditure += parseFloat($(this).find("td").eq(2).children().val());
        }
        index += 1;
    });
    $("table[name='fundsummarytable'] #id_total_budget").val(parseFloat(totalbudget));
    $("#id_total_expenditure").val(parseFloat(totalexpenditure));
    }
});

function projectfundbudget(is_submited){
    var pid = $("#mainTable").attr("value");
    var total_budget = parseFloat($('#id_total_budget').val());
    var laborcosts_budget = parseFloat($('#id_laborcosts_budget').val());
    var max_budget = parseFloat($('#max_budget').val());
    var projectcode = $("#project_code").val();
    //var finance_account = $("#finance_account").val();
    Dajaxice.teacher.fundBudget(fundBudget_callback,
                                    {
                                        'form': $('#project_fundbudget_form').serialize(true),
                                        'pid':pid,
                                        'max_budget':max_budget,
                                        'projectcode':projectcode,
                                        //'finance_account':finance_account,
                                        'is_submited':is_submited
                                });
}

function fundBudget_callback(data){
    if(data.flag){ 
        $('#summary_project_code').val(data.project_code);
        $("#summary_max_budget").val(data.project_budget_max);
        $("#summary_finance_account").val(data.finance_account);
        alert(data.message);
        var pid = $("#mainTable").attr("value");
        location.href = "/teacher/file_upload/"+pid;
    }
    else 
        alert(data.message);
}






// print


$(document).on("click", "#print_button", function(){

    var print_body = $("#print_body").html();
    var body = $("body").html();
    var bodycss = $("body").css("background-image");


    $("body").css("background-image","none");
    $("body").html(print_body);
    print();
    // $("body").html(body);
    // $("body").css("background-image",bodycss);
    window.location.reload();
    // window.location.reload();


})
