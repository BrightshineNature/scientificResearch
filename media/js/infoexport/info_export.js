$("[name = 'btn_export']").click(function(){
    var eid = $(this).attr("eid");
    $('#excelprogress').modal('show');
    Dajaxice.adminStaff.infoExport(releaseexcel_callback,{'eid':eid,});
});

function releaseexcel_callback(data){
  location.href = data.path;
  $('#excelprogress').modal('hide');
}