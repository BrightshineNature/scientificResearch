$(document).on("click", "#first_round_paginator .item_page", function(){
    page = $(this).attr("arg");
    Dajaxice.expert.getPagination(getPaginationCallback, {"page": page, "is_first_round": true,});
});
function getPaginationCallback(data){
    if(data.message == "first round"){
        $("#first-round-section").html(data.html);          
    }
    else{
        $("#second-round-section").html(data.html);
    }
}
$(document).on("click", "#second_round_paginator .item_page", function(){
    page = $(this).attr("arg");
    Dajaxice.expert.getPagination(getPaginationCallback, {"page": page, "is_first_round": false,});
});
