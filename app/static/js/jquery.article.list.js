
$(function(){
	
	var category = getValue('category');
	//console.log(category);
	var page = getValue('page');
	articleList(category,page);
	
	
});



// 显示文章列表
function articleList(category,page){
	var _url = api_http + "/m/article/list/" + category+"/page/"+page;
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
				var list = data.data.rows;
				var total = data.data.total-2;
				console.log(total);
				//console.log(list);
				var totalHtml = '';
				for(var i=0;i<list.length;i++){
					//console.log(list[i].id);
					var id = list[i].id;
					var title = list[i].title;
					var buildTime = new Date(list[i].buildTime);
					var m = buildTime.getMonth()+1;
					var day = buildTime.getDate();
					var html = '	<div id="'+id+'" class="body_right_list_div div_bg_fff div_shade">';
            		html = html + '		<div class="body_right_list_div_date"><span>'+m+'</span></div>';
                	html = html + '		<div class="body_right_list_div_title div_overflow"><span>'+day+'&nbsp;'+title+'</span></div>';
                	html = html + '		<div class="clear"></div></div>';
					
					//setTimeout(function () {
//						$('.body_right').find('div:last').after(html);
//						}, 2000);
					totalHtml = html + totalHtml;
				}
				
				if(total>10){
					var pageNum = parseInt(total/10);
					if(pageNum*10<total){
						pageNum = pageNum+1;
					}else if(pageNum*10>total){
						pageNum = pageNum-1;	
					}
					//页码
					html = '';
					for(var i=1;i<=pageNum;i++){
						html = html+'<span>'+i+'</span>';
					}
					
					totalHtml = totalHtml + '<div class="page_div">';
					totalHtml = totalHtml + '	<div class="page_prev"><span>上一页</span></div>';
					totalHtml = totalHtml + '	<div class="page_center">'+html+'</div>';
					totalHtml = totalHtml + '	<div class="page_next"><span>下一页</span></div>';
					totalHtml = totalHtml + '	<div class="clear"></div></div>';
				}
				
				
				$('.body_right').html(totalHtml);
				//console.log(totalHtml);
				
				//点击文章
				$('.body_right_list_div').click(function(e) {
					e.preventDefault();
					var id = $(this).attr('id');
					location.href="/pages/article.html?id="+id;
				});
				//点击下一页
				$('.page_prev').click(function(e) {
					e.preventDefault();
					page = page-1;
					console.log(page);
					if(page > 0){
						articleList(category,page);
					}
				});
				$('.page_next').click(function(e) {
					e.preventDefault();
					page = parseInt(page)+1;
					console.log(page);
					if(page > 0){
						articleList(category,page);
					}
				});
	
			}else{
				tipShow(data.message);	
			}
		}
	})
}