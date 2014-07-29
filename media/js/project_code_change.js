function project_code_add(){
  var project_unique_code = $('#project_code_add').find('#project_code').val().trim();
  Dajaxice.adminStaff.change_project_unique_code(change_projectuniquecode_callback,{'project_id':glo_project_id,"project_unique_code":project_unique_code});
}
function get_project_unique_code(caller){
  glo_project_id = $(caller).attr('pid');
  var project_unique_code = $(caller).parent().text().trim();
  $('#project_code_add').find('#project_code').val(project_unique_code);
}
