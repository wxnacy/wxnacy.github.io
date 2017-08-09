
$(function(){
	
	var id = getValue('id');
	article(id);
	
	
});



// 显示文章
function article(id){
	var _url = api_http + "/m/article/one/" + id;
	//console.log(_url);
	$.ajax({
		type: "get",
		dataType: "jsonp",
		url: _url,
		error:function(){
			console.log("error")
		},
		success:function(data){
			var status = data.status;
			if(status ==1){
				var title = data.data.title;
				var content = data.data.content;
				var buildTime = new Date(data.data.buildTime).toLocaleString();
				//console.log(buildTime);
				
				var html = '<h1>'+title+'</h1><p>'+buildTime+'<span>wenn</span></p>';
				$('.body_right').find('header').html(html);
				//console.log(totalHtml);
				html = '<p>'+content+'</p>';
				$('.body_right').find('center').html(html);
	
			}else{
				tipShow(data.message);	
			}
		}
	})
}