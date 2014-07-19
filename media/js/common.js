function saveSpecialName(){  
  Dajaxice.adminStaff.saveSpecialName(saveSpecialNameCallback, {'form':$('#special_form').serialize(false)  } );
};
function saveSpecialNameCallback(data){

    if(data.status == "1")
    {
      location.reload() 
    }
}

function deleteSpecialName() {
  var c = $('input#special_checkbox')
  var checked = new Array()
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
    location.reload() 
  }
}


function selectAll() {

  // alert("SBSB&&&")
  cnt = $("#all_special_checkbox")

  var c = $('input#special_checkbox')

  for(var i = 0; i < c.length; ++ i)
      c[i].checked = cnt[0].checked


}

