var data=[
    {achivementtype:"0",achivementtitle:"创新创造学",mainmember:"张三",introduction:"在实践中调动学生的创新能力",remarks:"课改基金项目"}, 
    {achivementtype:"1",achivementtitle:"大数据挖掘",mainmember:"王林",introduction:"数据分析与挖掘",remarks:"SCI"}
];
ACHIVEMENT_TYPE={
    '0':"专著",
    '1':"期刊论文",
    '2':"会议论文",
    '3':"专利",
    '4':"获奖",
    '5':"其他",
}
function addTr(obj)
{
    var tr=$("<tr></tr>");
    var table=$("#achivement_change_table");
    tr.appendTo(table);
    $("<td value="+obj.achivementtype+">"+ACHIVEMENT_TYPE[obj.achivementtype]+"</td><td>"+obj.achivementtitle+"</td><td>"+obj.mainmember+"</td><td>"+obj.introduction+"</td><td>"+obj.remarks+"</td><td><button class='btn btn-success'>修改信息</button></td><td><button class='btn btn-danger' rel='news_delete'><i class='icon-trash icon-white'></i><span>删除</span></button>").appendTo(tr);
}
for(var i=0;i<data.length;++i)
{ 
    addTr(data[i]);
    //var tr=$("<tr></tr>");
    //var table=$("#member_change_table");
    //tr.appendTo(table);
    //$("<td>"+data[i].teacher_name+"</td><td>"+data[i].teacher_birth+"</td><td>"+data[i].teacher_tel+"</td><td>"+data[i].teacher_email+"</td><td>"+data[i].teacher_professional+"</td><td>"+data[i].teacher_duty+"</td><td><button class='btn btn-success'>修改信息</button></td><td><button class='btn btn-danger' rel='news_delete'><i class='icon-trash icon-white'></i><span>删除</span></button>").appendTo(tr);
    
}

$("#achivement_change_table").on("click",".btn-danger",function(){
    $(this).closest("tr").remove();
        
});
var mod,tr;
$("#achivement_change_table ").on("click",".btn-success",function(){
    mod=0;
    $(".modal-title").html("修改研究成果信息");
    $("#save_change").html("确认保存");
    $("#teacher_profile_info").modal();
    tr=$(this).closest("tr");
    $("select[name='achivementtype']").val($(tr).children("td:eq(0)").attr("value"));
    $("input[name='achivementtitle']").val($(tr).children("td:eq(1)").html());
    $("input[name='mainmember']").val($(tr).children("td:eq(2)").html());
    $("input[name='introduction']").val($(tr).children("td:eq(3)").html());
    $("input[name='remarks']").val($(tr).children("td:eq(4)").html());

});
$("#add_new_achivement").click(function(){
    
    $("#achivement_change_form input").val('');
    $("#achivement_change_form select").val(-1);
    mod=1;
    $(".modal-title").html("添加研究成果");
    $("#save_change").html("确认添加");
    $("#achivement_profile_info").modal();
});

$("#save_change").click(function(){
    var formData=$("#achivement_change_form").serializeArray();
    var obj={};
    $.each(formData,function(i,field){
        obj[field.name]=field.value;
    });
    if(mod==1)
    {
        addTr(obj);

    }
    else
    {
        $(tr).children("td:eq(0)").html(ACHIVEMENT_TYPE[obj.achivementtype]); 
        $(tr).children("td:eq(1)").html(obj.achivementtitle);
        $(tr).children("td:eq(2)").html(obj.mainmember);
        $(tr).children("td:eq(3)").html(obj.introduction);
        $(tr).children("td:eq(4)").html(obj.remarks);
        $(tr).children("td:eq(0)").attr({ "value":obj.achivementtype});
    }
});