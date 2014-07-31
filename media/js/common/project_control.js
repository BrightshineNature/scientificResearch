var text_div;
$("select[name='expert_review']").each(function(){
  $(this).change(function(){
    text_div = $(this).parents(".active");
    Dajaxice.school.ChangeExpertReview(ExpertReview_callback,{'form':$(text_div).find("#expert_review_form").serialize(true),'special_id':$(text_div).attr('id')});
  })
})

$("#project_control_div #alloc").each(function(){
  $(this).click(function(){
    text_div = $(this).parents(".active")
    Dajaxice.school.ChangeAllocStatus(ChangeAllocStatus_callback,{'special_id':$(text_div).attr('id'),'type':"alloc"});
  })
})
$("#project_control_div #final_alloc").each(function(){
  $(this).click(function(){
    text_div = $(this).parents(".active")
    Dajaxice.school.ChangeAllocStatus(ChangeAllocStatus_callback,{'special_id':$(text_div).attr('id'),'type':"final_alloc"});
  })
})
function ChangeAllocStatus_callback(data){
  if (data.status == "1"){
    $(text_div).find("#expert_review_manage_success").show();
    $(text_div).find("#expert_review_manage_fail").hide();
    btn= $(text_div).find("#"+data.type);
    span = $(text_div).find("#"+data.type+"_span");
    if(data.type=="alloc"){
        status_value = "初审";
    }else if(data.type =="final_alloc"){
        status_value = "终审";
    }
    if(data.value){
      $(btn).attr("class","btn btn-warning");
      $(btn).val("关闭项目专家"+status_value);
      $(span).text("项目专家"+status_value+"为打开状态");
      $(span).attr("class","label label-success");
    }else{
      $(btn).attr("class","btn btn-primary");
      $(btn).val("打开项目专家"+status_value);
      $(span).text("项目专家"+status_value+"为关闭状态");
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
