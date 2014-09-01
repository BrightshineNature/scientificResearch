var text_div;
$("select[name='expert_review']").each(function(){
  $(this).change(function(){
    text_div = $(this).parents(".active");
    Dajaxice.school.ChangeExpertReview(ExpertReview_callback,{'form':$(text_div).find("#expert_review_form").serialize(true),'special_id':$(text_div).attr('id')});
  })
})

$("#project_control_field input").click(function(){
  text_div = $(this).parents(".active");
  Dajaxice.school.ChangeControlStatus(ChangeControlStatus_callback,{'special_id':$(text_div).attr('id'),'type_id':$(this).attr('id'),'type_name':$(this).attr('name')});
})


function ChangeControlStatus_callback(data){
  if (data.status == "1"){
    $(text_div).find("#expert_review_manage_success").show();
    $(text_div).find("#expert_review_manage_fail").hide();
    btn= $(text_div).find("input[id='"+data.type_id+"']");
    span = $(text_div).find("#"+data.type_id+"_span");
    if(data.value){
      $(btn).attr("class","btn btn-warning");
      $(btn).val("关闭"+data.type_name);
      $(span).text(data.type_name+"为打开状态");
      $(span).attr("class","label label-success");
    }else{
      $(btn).attr("class","btn btn-primary");
      $(btn).val("打开"+data.type_name);
      $(span).text(data.type_name+"为关闭状态");
      $(span).attr("class","label label-danger");
    }
  }else{
    $(text_div).find("#expert_review_manage_fail").show();
    $(text_div).find("#expert_review_manage_success").hide();
  }
}
function ExpertReview_callback(data){
  if (data.status == "1"){
    $(text_div).find("#expert_review_success").show();
    $(text_div).find("#expert_review_fail").hide();
  }else{
    $(text_div).find("#expert_review_fail").show();
    $(text_div).find("#expert_review_success").hide();
  }
}
$("[name = 'btn_export']").click(function(){
    var eid = $(this).attr("eid");
    text_div = $(this).parents(".active");
    $('#excelprogress').modal('show');
    Dajaxice.school.ExpertinfoExport(releaseexcel_callback,{'special_id':$(text_div).attr('id'),'eid':eid,});
});

function releaseexcel_callback(data){
  location.href = data.path;
  $('#excelprogress').modal('hide');
}
