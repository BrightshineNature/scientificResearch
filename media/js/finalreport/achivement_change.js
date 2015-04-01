var achivementid,tr;

$("#achivement_change_table").on("click",".btn-danger",function(){
    var pid = $("#achivement_change_table").attr("value");
    tr=$(this).closest("tr");
    achivementid=$(tr).attr("value");
    var is_submited = $("#achivement_change_table").attr("is_submited");
    Dajaxice.teacher.achivementDelete(delete_achivement_callback,{'achivementid':achivementid,'pid':pid,'is_submited':is_submited,});       
});


function delete_achivement_callback(data){

    $("#achivement_change_table").html(data.table);
    alert(data.message);
}

$("#achivement_change_table ").on("click",".btn-success",function(){
    $(".modal-title").html("修改研究成果信息");
    $("#achivement_save_change").html("确认保存");
    $("#achivement_profile_info").modal();
    tr=$(this).closest("tr");
    achivementid=$(tr).attr("value")
    $("select[name='achivementtype']").val($(tr).children("td:eq(0)").attr("value"));
    $("input[name='achivementtitle']").val($(tr).children("td:eq(1)").html());
    $("input[name='mainmember']").val($(tr).children("td:eq(2)").html());
    $("input[name='introduction']").val($(tr).children("td:eq(3)").html());
    $("input[name='remarks']").val($(tr).children("td:eq(4)").html());

});
$("#add_new_achivement").click(function(){
    achivementid=0;
    $(".modal-title").html("添加研究成果");
    $("#achivement_save_change").html("确认添加");
    $('#achivement_change_form')[0].reset();    
    $("#achivement_profile_info").modal();
});

$("#achivement_save_change").click(function(){
    var pid = $("#achivement_change_table").attr("value");
    var is_submited = $("#achivement_change_table").attr("is_submited");
    Dajaxice.teacher.achivementChange(add_or_update_achivement_callback,
                                {   
                                    'form': $('#achivement_change_form').serialize(true),
                                    'achivementid': achivementid,
                                    'pid':pid,
                                    'is_submited':is_submited,       
                            });
});

function add_or_update_achivement_callback(data){
    $("#achivement_change_table").html(data.table);
    alert(data.message);
}

$('#achivement_next').click(function(){
    $('#li_achivement').removeClass('active'); 
    $('#achivement').removeClass('active in');
    $('#li_datastatics').addClass('active'); 
    $('#datastatics').addClass('active in');
});

