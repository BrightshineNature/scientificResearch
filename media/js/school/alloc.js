$(document).on("click", "#unalloc_paginator .item_page", function(){
    page = $(this).attr("arg");   
    Dajaxice.school.getUnallocProjectPagination(getUnallocCallback, {"page": page}); 
});

function getUnallocCallback(data){
    $("#unalloced-section").html(data.html);
}
$(document).on("click", "#alloc_paginator .item_page", function(){
    page = $(this).attr("arg");   
    Dajaxice.school.getAllocProjectPagination(getAllocCallback, {"page": page}); 
});

function getAllocCallback(data){
    $("#alloced-section").html(data.html);
}
