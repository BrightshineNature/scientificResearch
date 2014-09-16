var dispatch_form="";
var dispatch_div="";
$(function(){
  $('#dispatch_form .btn').each(function(){
    $(this).click(function(){
      $("#dispatch_error_message").empty();
      dispatch_form = $(this).parents("form");
      page = $(dispatch_form).parent().find(".disabled").attr("value");
      Dajaxice.adminStaff.Dispatch(Dispatch_callback,{'form':$(dispatch_form).serialize(true),'identity':$(this).attr("id"),'page':page});
    })
  })
})
$(document).on("click",".dispatch_paginator .item_page",function(){
      dispatch_div = $(this).parents(".dispatch_paginator");
      page = $(this).attr("arg");
      ids = $(dispatch_div).attr("id").split('_');
      Dajaxice.adminStaff.DispatchPagination(DispatchPaginationCallback,{'page':page,'identity':ids[1]});
})
function DispatchPaginationCallback(data){
    $(dispatch_div).html(data.html);
}
function Dispatch_callback(data){
  if (data.status == "1"){
    // if success all field background turn into white
    $.each(data.field,function(i,item){
      object = $(dispatch_form).find('#'+item);
      object.css("background","white");
    });
    $(dispatch_form).parent().find("table").parent().html(data.table);
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
