$(document).on("click","#news_list_paginator .item_page",function(){
  page = $(this).attr("arg");
  news_cate = $(".news-content-nav").find(".active").attr("name");
  Dajaxice.home.getNewsListPagination(getNewsListCallback,{"page":page,"news_cate":news_cate});
})
function getNewsListCallback(data){
  $("#news-section").html(data.html);
}
