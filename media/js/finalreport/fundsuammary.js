function projectfundsummary(){
    var pid = $("#mainTable").attr("value");
 	Dajaxice.teacher.fundSummary(fundSummary_callback,
                                {   
                                    'form': $('#project_fundsuammary_form').serialize(true),
                                    'pid':pid,       
                            });
}

function fundSummary_callback(data){
    $("#mainTable").html(data.table);
    alert(data.message);
    $('#li_auditing').removeClass('active');        
    $('#auditing').removeClass('active in');
    $('#li_achivement').addClass('active');        
    $('#achivement').addClass('active in');
}
