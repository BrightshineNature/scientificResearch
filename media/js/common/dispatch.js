var dispatch_form="";
$(function(){
  $('#dispatch_form input').each(function(){
    $(this).click(function(){
      dispatch_form = $(this).parents("form");
      Dajaxice.adminStaff.Dispatch(Dispatch_callback,{'form':$(dispatch_form).serialize(true)},identity:$(this).attr("id"));
    })
  })
})
function Dispatch_callback(data){
  if (data.status == "1"){
    // if success all field background turn into white
    $(dispatch_form).each(data.field,function(i,item){
      object = $('#'+item);
      object.css("background","white");
      $("#send_mail_table").html(data.table);
    });
    //$("#time_settings_form").css("background","white");
    $("#expert_email_error_message").append("<strong>"+data.message+"</strong>");
  }
  else
  {
    $(dispatch_form).each(data.field,function(i,item){
      object = $('#'+item);
      object.css("background","white");
    });
    //error field background turn into red
    $(dispatch_form).each(data.error_id,function(i,item){
      object = $('#'+item);
      object.css("background","red");
    });
    $("#expert_email_error_message").append("<strong>"+data.message+"</strong>");
  }
}
