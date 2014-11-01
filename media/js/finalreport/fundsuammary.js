function projectfundsummary(){
    var pid = $("#mainTable").attr("value");
    var total_budget = parseFloat($('#id_total_budget').val())
    var laborcosts_budget = parseFloat($('#id_laborcosts_budget').val())
    if (totalbudget * 0.3 > laborcosts_budget){
     	Dajaxice.teacher.fundSummary(fundSummary_callback,
                                    {   
                                        'form': $('#project_fundsuammary_form').serialize(true),
                                        'pid':pid,       
                                });
    }
    else
    {
        alert("劳务费应低于总结额的30%,请仔细核实");
    }
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
$("#mainTable").find("input").bind('change',function(){
    totalbudget = 0;
    totalexpenditure = 0
    $("#mainTable tbody tr").each(function(){
        totalbudget += parseFloat($(this).find("td").eq(1).children().val());
        totalexpenditure += parseFloat($(this).find("td").eq(2).children().val());
    });
    $("#id_total_budget").val(parseFloat(totalbudget));
    $("#id_total_expenditure").val(parseFloat(totalexpenditure));
});

function projectfundbudget(){
    var pid = $("#mainTable").attr("value");
    var total_budget = parseFloat($('#id_total_budget').val())
    var laborcosts_budget = parseFloat($('#id_laborcosts_budget').val())
    if (totalbudget * 0.3 > laborcosts_budget){
        Dajaxice.teacher.fundBudget(fundBudget_callback,
                                    {   
                                        'form': $('#project_fundbudget_form').serialize(true),
                                        'pid':pid,       
                                });
    }
    else
    {
        alert("劳务费应低于总结额的30%,请仔细核实");
    }
}

function fundBudget_callback(data){
    alert(data.message);
}