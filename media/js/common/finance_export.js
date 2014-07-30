$(function(){
  $("#schedule_form .btn").click(function(){
     export_form = $(this).parents("form");
     Dajaxice.finance.ExportExcel(ExportExcel_callback,{'form':$(export_form).serialize(true),'category':$(this).attr("id")});
  })
})
function ExportExcel_callback(data){
  alert("aaa");
}
