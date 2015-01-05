$("#allocemail_form button").click(function(){
  Dajaxice.school.AllocEmail(AllocEmail_callback,{'form':$("#allocemail_form").serialize(true),'param':$(this).attr("id")});
})

function AllocEmail_callback(data){
  if (data.status == "1"){

  }else if(data.status == "2"){
  }else{
    $("#form_div").html(data.table);
  }
  alert(data.message);
}
