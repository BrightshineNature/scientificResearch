function projectfundsummary(){
    var pid = $("#mainTable").attr("value");
    var total_budget = parseFloat($('#id_total_budget').val())
    var laborcosts_budget = parseFloat($('#id_laborcosts_budget').val())
    
    Dajaxice.teacher.fundSummary(fundSummary_callback,
                                    {   
                                        'form': $('#project_fundsuammary_form').serialize(true),
                                        'pid':pid,       
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
$("#mainTable").find("input").bind('change',function(){
    totalbudget = 0;
    totalexpenditure = 0;
    index = 0;
    if($(this).val()<0||isNaN($(this).val()))
    {
        alert("数据格式不对,请重新输入");
        $(this).val(0.0);
    }
    $("#mainTable tbody tr").each(function(){
        if(index>0)
        {
            totalbudget += parseFloat($(this).find("td").eq(1).children().val());
            totalexpenditure += parseFloat($(this).find("td").eq(2).children().val());
        }
        index += 1;
    });
    $("#id_total_budget").val(parseFloat(totalbudget));
    $("#id_total_expenditure").val(parseFloat(totalexpenditure));
});

function projectfundbudget(){
    var pid = $("#mainTable").attr("value");
    var total_budget = parseFloat($('#id_total_budget').val())
    var laborcosts_budget = parseFloat($('#id_laborcosts_budget').val())
    Dajaxice.teacher.fundBudget(fundBudget_callback,
                                    {   
                                        'form': $('#project_fundbudget_form').serialize(true),
                                        'pid':pid,       
                                });
}

function fundBudget_callback(data){
    alert(data.message);
}
