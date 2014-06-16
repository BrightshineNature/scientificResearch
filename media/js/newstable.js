var data=[{news_id:1,news_title:"胡俊",news_category:"通告公知",news_date:"2013-5-3"},
    {news_id:2,news_title:"胡俊",news_category:"通告公知",news_date:"2013-5-3"},
    {news_id:3,news_title:"胡俊",news_category:"通告公知",news_date:"2013-5-3" }
];
for(var i=0;i<data.length;++i)
{ 
    var tr=$("<tr id="+data[i].news_id+"></tr>");
    var table=$("#newscontent");
    tr.appendTo(table);
    $("<td>"+data[i].news_title+"</td><td>"+data[i].news_category+"</td><td>"+data[i].news_date+"</td><td>"+"<button class='btn btn-danger' rel='news_delete' uid='"+data[i].news_id+"'><i class='icon-trash icon-white'></i><span>删除</span></button>").appendTo(tr);
    
}


    $("#newscontent .btn-danger").click(function(){
        $(this).closest("tr").remove();
        
    });
