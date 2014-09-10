
var objects_table_pos;
$(document).on("click", ".saveObjectName",function(){

  var cnt = $(this).parents("[object]");
  objects_table_pos = cnt.find(".object_table_div")[0];

  Dajaxice.adminStaff.saveObjectName(saveObjectNameCallback, { 'object': $(cnt[0]).attr('object'), 'form':$(cnt).find('.object_name').serialize() });

})
function saveObjectNameCallback(data){
    $("#alert_info_modal").attr("data-dismiss", "modal");
    if(data.status == 1)
    {
      $(objects_table_pos).html(data.objects_table);

      $("#alert_info_modal").find(".modal-body").html("<h3>添加成功！<h3>");
      $("#alert_info_modal").modal('show');

    }
    else if(data.status == 0)
    {
      $("#alert_info_modal").find(".modal-body").html("<h3>添加不成功！所添加名字为空或者已存在！<h3>");
      $("#alert_info_modal").modal('show');
    }
}

$(document).on("click", ".deleteObjectName", function(){

  var cnt = $(this).parents("[object]");
  objects_table_pos = cnt.find(".object_table_div")[0];
  var box = $(objects_table_pos).find(".object_checkbox");
  var deleted = new Array();
  for(var i = 0; i < box.length; ++ i)
  {
      if(box[i].checked) deleted.push(box[i].name);
  }
  Dajaxice.adminStaff.deleteObjectName(deleteObjectNameCallback, 
    { 'object': $(cnt[0]).attr('object'), 'deleted': deleted});

});

function deleteObjectNameCallback(data) {
  if(data.status == 1)
  {    
    $("#alert_info_modal").find(".modal-body").html("<h3>删除成功！<h3>");
    $("#alert_info_modal").modal('show');
  }
  else 
  {
    var error;
    if(data.alloced == "")
    {
      error = "<h3>删除不成功！没有选定所要删除的项！"
    }
    else 
    {
      error = "<h3>删除不成功！" + data.alloced + "已被分配到项目中，不可被删除！"
    }
    $("#alert_info_modal").find(".modal-body").html(error);
    $("#alert_info_modal").modal('show');
  }
  $(objects_table_pos).html(data.objects_table);
}


$(document).on( "click", ".all_object_checkbox", function(){
    
    var box = $(this).parent().parent().parent().next().find("input");
    for(var i = 0; i < box.length; ++ i)
    {
      box[i].checked = this.checked;
    }
});

function contain(arr, x) {
  for(var i = 0; i < arr.length; ++ i) 
  {
    if(arr[i] == x) return true;
  }
  return false;

}

var cnt_user;
var object_alloc_pos;


// function alloc() {

$(document).on("click", ".object_alloc", function() {

  var cnt = $(this).parents("[object]")[0]

  object_alloc_pos = cnt;
  objects_table_pos = $(cnt).prev().find(".object_table_div");
  // alert($(objects_table_pos).html())

  $("#object_modal").attr("object", $(cnt).attr('object'));

  
  cnt = $(cnt).prev();
  cnt = $(cnt).find(".object_table_div");
  $("#object_modal").find(".modal-body").html($(cnt).html());
  // selectAll();

  var p = $(this).parent().parent();
  cnt_user = p.children("td:eq(0)").text();  
  // alert(cnt_user)

  $("#object_modal").find("h4").html("当前用户:" + cnt_user )

  var box = $("#object_modal").find(".object_checkbox");
  var s = p.children("td:eq(1)").text();
  s = s.split(',');
  for(var i = 0; i < box.length; ++ i) 
  {
    if(contain(s, box[i].name)) 
    {
      box[i].checked = true;
    }
    else box[i].checked = false;
  }

});

// };

// alloc();

$(document).on("click","#saveObjectAlloc", function() 
{
  var box = $("#object_modal").find(".object_checkbox");
  var cnt = $(this).parents("[object]")[0];

  // alert($(cnt[0]).html())
  // alert($(cnt[0]).attr('object'))
  var alloced = new Array();
  for(var i = 0; i < box.length; ++ i)
  {
    if(box[i].checked) 
    {
        alloced.push(box[i].name);
    }
  }

  Dajaxice.adminStaff.allocObject(allocObjectCallback, 
    {'object': $(cnt).attr('object'),  'user':cnt_user, 'alloced':alloced});

})

function allocObjectCallback(data){
  if(data.status == '1')
  {
    $(object_alloc_pos).html(data.object_alloc);
    // alloc();

    $(objects_table_pos).html(data.object_table);
    // selectAll();

  }

}
