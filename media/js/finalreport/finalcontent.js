$('#finalsubmitform_btn').click(function(){
    var pid = $(this).attr("pid");
    var is_submited = $(this).attr("is_submited");
    Dajaxice.teacher.finalReportContent(final_content_callback,{'pid':pid,'finalsubmitform':$('#finalsubmitform').serialize(true),'is_submited':is_submited,});
});

function final_content_callback(data){
    if(data.go_next)
    {
        finalcontent_next();
    }
    else
    {
        $('#final_content').html(data.finalsubmitform);
    }
}

function finalcontent_next(){
    $('#li_content').removeClass('active');        
    $('#content').removeClass('active in');
    $('#li_achivement').addClass('active');
    $('#achivement').addClass('active in');
}
