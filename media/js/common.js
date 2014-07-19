var glo_project_id;

function get_subject_id(project_id){

  glo_project_id = project_id;
}


function project_overstatus(){
  var overstatus = $('#overstatus_choice').find("option:selected").val();
  Dajaxice.common.change_project_overstatus(change_overstatus_callback,{'project_id':glo_project_id,"changed_overstatus":overstatus});
}
function change_overstatus_callback(data){
  
  var target = "#overstatus_" + glo_project_id;
  $(target).html(data.res);
}
$('[rel="isover"]').click(function(){
  var pid = $(this).attr("pid");
  Dajaxice.school.isover_control(isover_control_callback,{"pid":pid});
});



function saveSpecialName(){
  // alert($('#major_name_form').serialize(true))
   // alert("SBSB")
  Dajaxice.adminStaff.saveSpecialName(saveSpecialNameCallback, {'form':$('#special_form').serialize(false)  } );
};
function saveSpecialNameCallback(data){

    if(data.status == "1")
    {
      location.reload() 
    }
    // else 
    // {
    //   alert("error ")
    // }

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
  if(data.status == 1)
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

