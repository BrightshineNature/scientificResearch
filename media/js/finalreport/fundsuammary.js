function projectfundsummary(){
    var finalsubmitid = $("#mainTable").attr("value");
 	Dajaxice.teacher.fundSummary(fundSummary_callback,
                                {   
                                    'form': $('#project_fundsuammary_form').serialize(true),
                                    'finalsubmitid':finalsubmitid,       
                            });
}

function fundSummary_callback(data){
	alert(data.message);
    $("#mainTable").html(data.table);
}
