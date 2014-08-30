var dispatch_form="";
$(function(){
  $('#dispatch_form .btn').each(function(){
    $(this).click(function(){
      $("#dispatch_error_message").empty();
      dispatch_form = $(this).parents("form");
      Dajaxice.adminStaff.Dispatch(Dispatch_callback,{'form':$(dispatch_form).serialize(true),'identity':$(this).attr("id")});
    })
  })
})

function Dispatch_callback(data){
  if (data.status == "1"){
    // if success all field background turn into white
    $.each(data.field,function(i,item){
      object = $(dispatch_form).find('#'+item);
      object.css("background","white");
      $(dispatch_form).parent().find("table").html(data.table);
    });
  }else{
    $.each(data.field,function(i,item){
       object = $(dispatch_form).find('#'+item);
       object.css("background","white");
    });
    //error field background turn into red
    $.each(data.error_id,function(i,item){
       object = $(dispatch_form).find('#'+item);
       object.css("background","red");
    });
  }
  alert(data.message);
}
