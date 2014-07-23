function saveSpecialName(){  
  Dajaxice.adminStaff.saveSpecialName(saveSpecialNameCallback, {'form':$('#special_form').serialize(false)  } );
};
function saveSpecialNameCallback(data){

    if(data.status == "1")
    {
      location.reload() ;
    }
}

function deleteSpecialName() {
  var c = $('input#special_checkbox');
  var checked = new Array();
  for(var i = 0; i < c.length; ++ i)
  {
    if(c[i].checked)
      checked.push(c[i].value);
  }  
  Dajaxice.adminStaff.deleteSpecialName(deleteSpecialNameCallback, {'checked':checked } );  
}

function deleteSpecialNameCallback(data) {
  if(data.status == '1')
  {
    location.reload() ;
  }
}



function selectAll() {

  // alert("SBSB&&&")
  cnt = $("#all_special_checkbox");

  var boxs = $('input#special_checkbox')

  for(var i = 0; i < boxs.length; ++ i)
      boxs[i].checked = cnt[0].checked;


}


var cnt_user;

function contain(arr, x) {
  for(var i = 0; i < arr.length; ++ i) 
  {
    if(arr[i] == x) return true;
  }
  return false;

}

$("#special_alloc").on("click", "#user_special_alloc", function() 
{

  var p = $(this).parent().parent();
  cnt_user = p.children("td:eq(0)").text();
  
  var boxs = $("input#special_alloc_checkbox");
  var s = p.children("td:eq(1)").text();
  // alert(s);
  s = s.split(',');
  
  // alert(s);

  // alert(contain(s, 34))

  for(var i = 0; i < boxs.length; ++ i) 
  {
    if(contain(s, boxs[i].name)) 
    {
      boxs[i].checked = true;
    }
    else boxs[i].checked = false;

    // alert("**" + boxs[i].name + boxs[i].checked)

  }
})

$("#special_modal").on("click", "#save_special_alloc", function() 
{
  // alert("@!@#");
  var boxs = $("input#special_alloc_checkbox");
  var alloced = new Array();
  for(var i = 0; i < boxs.length; ++ i)
  {
    if(boxs[i].checked) 
    {
        alloced.push(boxs[i].name  );
        // alert(boxs[i].name);
        // alert($(boxs[i]).text())

    }
  }

  Dajaxice.adminStaff.allocSpecial(allocSpecialCallback, {'user':cnt_user, 'alloced':alloced});



})

function allocSpecialCallback(data){
  if(data.status == '1')
  {
    location.reload() ;
  }

}
