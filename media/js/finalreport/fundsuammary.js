function projectfundsummary(is_submited){
    var pid = $("#mainTable").attr("value");
    var total_budget = parseFloat($('#id_total_budget').val());
    var laborcosts_budget = parseFloat($('#id_laborcosts_budget').val());
    var max_budget = parseFloat($('#max_budget').val()); 
    var projectcode = $("#project_code").val();
    var finance_account = $("#summary_finance_account").val();
    Dajaxice.teacher.fundSummary(fundSummary_callback,
                                    {
                                        'form': $('#project_fundsuammary_form').serialize(true),
                                        "remarkmentform":$('#project_fundsuammaryremarkment_form').serialize(true),
                                        'pid':pid,
                                        'finance_account':finance_account,
                                        'is_submited':is_submited
                                });
}

function projectfundsummaryremarkment(){
  var pid = $("#mainTable").attr("value");
  Dajaxice.teacher.fundSummaryRemarkment(fundSummaryRemarkment_callback,{
    'form':$('#project_fundsuammaryremarkment_form').serialize(true),
    'pid':pid,
  })
}

function fundSummaryRemarkment_callback(data){
  alert(data.message);
}

function fundSummary_callback(data){
    alert(data.message);
    if (data.flag) {
      location.href = "/teacher/finalinfo";
    };
}

var totalbudget = 0.0;
var totalexpenditure = 0.0;
$("table[name='budgettable'] tbody").find("input").bind('change',function(){
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
                                        'remarkmentform':$('#project_fundbudgetremarkment_form').serialize(true),
                                        'pid':pid,
                                        'max_budget':max_budget,
                                        'projectcode':projectcode,
                                        //'finance_account':finance_account,
                                        'is_submited':is_submited
                                });
}

function projectfundbudgetremarkment(){
  var pid = $("#mainTable").attr("value");
  Dajaxice.teacher.fundBudgetRemarkment(fundBudgetRemarkment_callback,{
    'form':$('#project_fundbudgetremarkment_form').serialize(true),
    'pid':pid,
  })
}

function fundBudgetRemarkment_callback(data){
  alert(data.message);
}

function fundBudget_callback(data){
    if(data.flag){ 
        $('#summary_project_code').val(data.project_code);
        $("#summary_max_budget").val(data.project_budget_max);
        $("#summary_finance_account").val(data.finance_account);
        alert(data.message);
        var pid = $("#mainTable").attr("value");
        location.href = "/teacher/finalinfo";
    }
    else 
        alert(data.message);
}

// 经费预算表 print
$(document).on("click", "#budget_detail_print_button", function(){   

    
    $("body").css("background-image","none");
    var print_body = $("#budget-detail").clone(true)

    $(print_body).find("table").addClass("table-bordered");

    // $(print_body).find("table").attr("border", '2');
    // $.each($(print_body).find("tr"), function(){
    //     // alert("FF");

    //     $(this).attr("border-width", '10px');
    //     $(this).attr("border-style", 'solid');
    //     $(this).attr("border-color", 'black');
    // });

    // $.each($(print_body).find("td"), function(){

    //     $(this).attr("border-width", '10px');
    //     $(this).attr("border-style", 'solid');
    //     $(this).attr("border-color", 'black');
        
    // });

    $(print_body).find("button").remove();

    $(print_body).prepend(function(){
        return "<h4>经费预算表</h4>"
    })

    var input_list = $(print_body).find("input");

    for(var i = 0; i < input_list.length; ++ i)
    {
        var pa = $(input_list[i]).parent();
        $(pa).text($(input_list[i]).val());
        $(input_list[i]).remove();        
    }
    $("body").html(print_body);
    // return ;
    print();
    
    // $("body").css("background-image",bodycss);
    // alert(body);

    // $("body").html(body);
    window.location.reload();



});
$(document).on("click", "#budgetremarkment_print_button", function(){

    

    
    $("body").css("background-image","none");
    var print_body = $("#budgetremarkment").clone(true)
    $(print_body).find("button").remove();
    $($(print_body).find("p")[0]).html("<h4>经费预算说明</h4>(对各支出主要用途，测算方法，测算依据进行详细分析说明,如依据前页所填设备费、材料费等逐项填写)");    
    $("body").html(print_body);
    // return ;
    print();
    // $("body").css("background-image",bodycss);
    // alert(body);
    // $("body").html(body);
    window.location.reload();



});












// 决算表 print

$(document).on("click", "#fundsummary_print_button", function() {

    $("body").css("background-image","none");
    var print_body = $("#fundsummary").clone(true)

    $(print_body).find("table").addClass("table-bordered");

    $(print_body).find("button").remove();

    $(print_body).prepend(function(){
        return "<h4>经费决算表</h4>"
    })

    var input_list = $(print_body).find("input");

    for(var i = 0; i < input_list.length; ++ i)
    {
        var pa = $(input_list[i]).parent();
        $(pa).text($(input_list[i]).val());
        $(input_list[i]).remove();        
    }
    $("body").html(print_body);
    
    // return ;
    print();
    
    window.location.reload();

})



$(document).on("click", "#fundsummary_remarkment_print_button", function() {

    $("body").css("background-image","none");
    var print_body = $("#fundsummary_remarkment").clone(true)
    $(print_body).find("button").remove();
    $($(print_body).find("p")[0]).html("<h4>经费决算说明</h4>(对各支出主要用途，测算方法，测算依据进行详细分析说明,如依据前页所填设备费、材料费等逐项填写)");

    
    $("body").html(print_body);
    // return ;
    print();
    
    // $("body").css("background-image",bodycss);
    // alert(body);

    // $("body").html(body);
    window.location.reload();

    
})
