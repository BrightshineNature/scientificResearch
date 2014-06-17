var glo_project_id;

function get_subject_id(project_id){

  glo_project_id = project_id;
}


function project_overstatus(){
  var overstatus = $('#overstatus_choice').find("option:selected").val();
  Dajaxice.common.change_project_overstatus(change_overstatus_callback,{'project_id':glo_project_id,"changed_overstatus":overstatus});
}
function change_overstatus_callback(data){
  
  var target = "#overstatus_" + glo_project_id;
  $(target).html(data.res);
}
$('[rel="isover"]').click(function(){
  var pid = $(this).attr("pid");
  Dajaxice.school.isover_control(isover_control_callback,{"pid":pid});
});
