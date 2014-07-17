var achivementid,tr;

$("#achivement_change_table").on("click",".btn-danger",function(){
    achivementid=$(tr).attr("value");
    var finalsubmitid = $("#achivement_change_table").attr("value");
    tr=$(this).closest("tr");
    achivementid=$(tr).attr("value")
    Dajaxice.teacher.achivementDelete(delete_achivement_callback,{'achivementid':achivementid,'finalsubmitid':finalsubmitid});       
});


function delete_achivement_callback(data){
    alert(data.message);
    $("#achivement_change_table").html(data.table);
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
/*    $("select[name='achivementtype']").val('0');
    $("input[name='achivementtitle']").val('');
    $("input[name='mainmember']").val('');
    $("input[name='introduction']").val('');
    $("input[name='remarks']").val('');*/
    $('#achivement_change_form')[0].reset();    
    $("#achivement_profile_info").modal();
});

$("#achivement_save_change").click(function(){
    var finalsubmitid = $("#achivement_change_table").attr("value");
    Dajaxice.teacher.achivementChange(add_or_update_achivement_callback,
                                {   
                                    'form': $('#achivement_change_form').serialize(true),
                                    'achivementid': achivementid,
                                    'finalsubmitid':finalsubmitid,       
                            });
});

function add_or_update_achivement_callback(data){
    alert(data.message);
    $("#achivement_change_table").html(data.table);
}

