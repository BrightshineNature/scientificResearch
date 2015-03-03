$(function(){
  $("#schedule_form .btn").click(function(){
     export_form = $(this).parents("form");
    $('#excelprogress').modal('show');
     Dajaxice.finance.ExportExcel(ExportExcel_callback,{'form':$(export_form).serialize(true),'category':$(this).attr("id")});
  })
})
function ExportExcel_callback(data){
  location.href = data.path;
  $('#excelprogress').modal('hide');
}
