$(function(){
  $("#schedule_form .export-excel").click(function(){
     export_form = $(this).parents("form");
     $('#excelprogress').modal('show');
     Dajaxice.common.ExportExcel(ExportExcel_callback,{'form':$(export_form).serialize(true),'category':$(this).attr("eid")});
  })
  $("#teacher_form .export-excel").click(function(){
    $('#excelprogress').modal('show');
    Dajaxice.common.ExportTeacherInfoExcel(ExportExcel_callback,{'category':$(this).attr("eid")});
  })
})
function ExportExcel_callback(data){
  location.href = data.path;
  $('#excelprogress').modal('hide');
}
