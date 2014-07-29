function projectfundsummary(){
    var pid = $("#mainTable").attr("value");
 	Dajaxice.teacher.fundSummary(fundSummary_callback,
                                {   
                                    'form': $('#project_fundsuammary_form').serialize(true),
                                    'pid':pid,       
                            });
}

function fundSummary_callback(data){
	alert(data.message);
    $("#mainTable").html(data.table);
}
