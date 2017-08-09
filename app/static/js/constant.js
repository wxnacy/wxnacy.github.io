var api_http = "http://101.200.193.65:8080";
var web_http = "http://www.wennspring.com";

var path = '';
var img_path ='../images/';
$(function(){
	var page_reg = getPageName();
	if(page_reg == 'index.html' || page_reg==''){
		path = "pages/";
		img_path = 'images/';
	}
	//初始化加载的方法
	onLoad()
	//初始化动作
	onLoadAction();
	
});

function onLoad(){
	
	//初始化加载的方法
	var html = '	<ul>';
	html = html+'		<li name="article_list.html?category=tech&page=1">技术</li>';
	html = html+'		<li name="article_list.html"><a>生活</a></li>';
	html = html+'		<li name="message.html"><a>留言</a></li>';
	html = html+'		<li name="connection.html"><a>联系</a></li>';
	html = html+'		<li name="about.html"><a>关于</a></li>';
	html = html+'	</ul>';
	$('.body_top_right').html(html);	
	
	
	
	html = '		<div class="image_div image_wrap" >';
    html = html + '		<img src="'+img_path+'face1.jpg" alt="头像" width="128" height="128" class="image_wrap" >';
    html = html + ' </div>';
    html = html + ' <div class="ol_div">';
    html = html + '   	<ol>';
    html = html + '       	<li>姓名：wenn</li>';
    html = html + '         <li>职业：java工程师</li>';
    html = html + '         <li>爱好：老婆、周杰伦、电影、英雄联盟</li>';
    html = html + '         <li>简介：<p>本站技术构架纯手打，意在保存展示技术博客和两个人的纪念日等文章</p></li>';
    html = html + '     </ol>';
    html = html + ' </div>';
	html = html + ' <div class="near_article_div">';
	html = html + ' 	<div class="near_article_div_1">';
	html = html + '			<span>近期文章</span>';
	html = html + '		</div>';
	html = html + '		<div class="near_article_div_2">';
	html = html + '			<p>如果对surface还有期待的话，那就是pro4了</p>';
	html = html + '			<hr size="1" noshade="noshade" style=""/>';
	html = html + '			<p>如果对surface还有期待的话，那就是pro4了</p>';
	html = html + '			<hr size="1" noshade="noshade" style=""/>';
	html = html + '			<p>如果对surface还有期待的话，那就是pro4了</p>';
	html = html + '			<hr size="1" noshade="noshade" style=""/>';
	html = html + '			<p>如果对surface还有期待的话，那就是pro4了</p>';
	html = html + '		</div>';
	html = html + '	</div>';
	
	$('.body_left').html(html);
	
	
	$('.body_button').html(' © 2015 wennspring.com 版权所有 <a href="http://www.miitbeian.gov.cn/" target="_blank">京ICP备15062634号-1</a> ');
}


function onLoadAction(){
	$('.body_top_left').click(function(e) {
        e.preventDefault();
		location.href="/index.html";
    });
	
	
	var li = $('.body_top_right').find('li');
	
	//console.log(page_reg);
	li.each(function(index, element) {
        $(this).click(function(e) {
            //console.log($(this).attr('name'));
			var name = $(this).attr('name');
			
			location.href=path+name;
        });
    });
	
}

//取当前页面名称(带后缀名)
function getPageName(){
	var strUrl=location.href;
	var arrUrl=strUrl.split("/");
	var strPage=arrUrl[arrUrl.length-1];
	var i = strPage.indexOf('?');
	if(i>0){
		strPage = strPage.substring(0,strPage.indexOf('?'))
	}
	return strPage;
}
//获取html传参
function getValue(key) {
	var name = key;
	var str = window.location.search;
	if (str.indexOf(name) != -1) {
		var pos_start = str.indexOf(name) + name.length + 1;
		var pos_end = str.indexOf("&", pos_start);
		if (pos_end == -1) {
			return decodeURIComponent(str.substring(pos_start));
		} else {
			return decodeURIComponent(str.substring(pos_start, pos_end));
		}
	}
}

///////////////////////////////////////////////////////////////////////////////////////////////////////////

//显示登陆页
function showLogin(){
	$('#loginHtml').show();
	$('.open-wrap').show();
	if($(window).width()==320){
		$('html,body').animate({scrollTop:200},400);
	}
}

function createLoginHtml(){
	var pageName = getPageName();
	var page = 'pages/';
	
	if(pageName != 'index.html'){
		page = '';		
	}
	var html = 		'<div class="open-wrap">';
	html = html + 	'	<div class="login-box">';
	html = html + 	'		<!--<div class="form">--><form>';
	html = html + 	'			<div class="aline auto">';
	html = html + 	'				<input class="" type="text" id="loginName" placeholder="请输入用户名">';
	html = html + 	'			</div>';
	html = html + 	'			<div class="aline auto">';
	html = html + 	'				<input class="" type="password" id="loginPasswd" placeholder="请输入密码">';
	html = html + 	'			</div>';
	html = html + 	'			<div class="aline">';
	html = html + 	'				<input type="submit" id="loginSub" value="登录">';
	html = html + 	'			</div>';
	html = html + 	'			<div class="bline">';
	html = html + 	'				<a class="link-sign" href="'+page+'sign.html">快速注册</a>';
	html = html + 	'				<a class="log-phone" href="javascript:void(0)">手机短信密码登录</a>';
	html = html + 	'			</div>';
	html = html + 	'		<!--</div>--></form>';
	html = html + 	'		<div class="apart">';
	html = html + 	'			<div class="line"></div>';
	html = html + 	'			<span>使用合作网站账号登录</span>';
	html = html + 	'		</div>';
	html = html + 	'		<ul class="icons in-2">';
	html = html + 	'			<li><img src="'+http_linux+'/images/ico-16.png"></li>';
	html = html + 	'			<li><img src="'+http_linux+'/images/ico-17.png"></li>';
	// html = html + 	'			<li><img src="'+http_linux+'/images/ico-18.png"></li>';
	// html = html + 	'			<li><img src="'+http_linux+'/images/ico-19.png"></li>';
	html = html + 	'		</ul>';
	html = html + 	'	</div>';
	html = html + 	'	<div class="login-box phone-box">';
	html = html + 	'		<!--<div class="form">--><form>';
	html = html + 	'			<div class="aline">';
	html = html + 	'				<a class="back"></a>';
	html = html + 	'			</div>';
	html = html + 	'			<div class="aline auto">';
	html = html + 	'				<input class="test-mobile" type="text" id="mobile" placeholder="请输入手机号">';
	html = html + 	'			</div>';
	html = html + 	'			<div class="zline">';
	html = html + 	'				<input class="" type="text"  id="mobileCode" placeholder="请输入验证码">';
	html = html + 	'				<input class="" type="button" id="btn" value="免费获取验证码">';
	html = html + 	'			</div>';
	html = html + 	'			<div class="aline">';
	html = html + 	'				<input type="submit" id="mobileLogin" value="登录">';
	html = html + 	'			</div>';
	html = html + 	'		<!--</div>--></form>';
	html = html + 	'	</div>';
	html = html + 	'</div>';

	$('#loginHtml').html(html);
}

//获取验证码
function getCode(mobile){
	//var mobile = $('#'+id).val();
	//console.log(mobile);
	// if(mobile == '' || !checkMobile(mobile)){
	// 	alert('请输入正确的手机号1');
	// 	return false;
	// }
	var urljson = http_head+"/m/user/code?mobile="+mobile;//+"&password="+loginPasswd;
	$.ajax({
		type: "get",
		dataType: "jsonp",
		url: urljson,
		error : function() {
			alert('error');
		},
		success : function(data) {
			var status = data.status;
			if(status == 1){
				var code = data.code;
			}else{
				alert(data.message);
				return;
			}
		}
	});
};


//正常登陆
function login(){
	var loginName = $('#loginName').val();
	var loginPasswd = $('#loginPasswd').val();

	if(loginName == ''){
		$('#loginName').parent().addClass('failed')
			if(loginPasswd == ''){
				$('#loginPasswd').parent().addClass('failed')
			}
		return;
	}
	if(loginPasswd == ''){
		$('#loginPasswd').parent().addClass('failed')
		return;
	}
	var urljson = http_head+"/m/user/login?emailOrMobile="+loginName+"&password="+loginPasswd;
	$.ajax({
		type: "get",
		dataType: "jsonp",
		url: urljson,
		error : function() {
			alert('error');
		},
		success : function(data) {
			var status = data.status;
			//console.log(status)
			if(status == 1){
				var userEntity = data.userEntity;
				
				//alert(userEntity);
				setUserCookie(userEntity);
				location.replace(location.href);
			}else{
				$('#loginName').parent().addClass('failed');
				$('#loginPasswd').parent().addClass('failed');
				return;
			}
		}
	})
}

//手机短信登陆
function loginByCode(){
	var mobile = $('#mobile').val();
	var code = $('#mobileCode').val();
	
	if(mobile == '' || !checkMobile(mobile)){
		$('#mobile').parent().addClass('failed')
		if(code == ''){
			$('#mobileCode').parent().addClass('failed')
		}
		return;	
	}
	if(code == ''){
		$('#mobileCode').parent().addClass('failed')
	}
	var urljson = http_head+"/m/user/login/mobile?mobile="+mobile+"&code="+code;
	//alert(urljson);
	$.ajax({
		type: "get",
		dataType: "jsonp",
		url: urljson,
		error : function() {
			alert('error');
		},
		success : function(data) {
			var status = data.status;
			//alert(status);
			if(status == 1){
				var userEntity = data.userEntity;
				alert('登陆成功');
				setUserCookie(userEntity);
				location.replace(location.href);
			}else{
				$('#mobileCode').parent().addClass('failed')
				return;
			}
		}
	})
}

//首页内容
function homeIndex(userUrl,type){
	var home_url = http_head_api+"/info/foucs/homePage?type="+type+userUrl;
	var homeHtml = '';
	$.ajax({
		type: "get",
		dataType: "jsonp",
		url: home_url,
		error : function() {
			alert('error');
		},
		success : function(data) {
			var status = data.status;
			if(status == 1){
				var list = data.data;
				var top = list[0];
				var topList = top.data;
				var videoPath = '';
				var pageName = getPageName();
				var index_ = $('#index_').length;
				if(index_){
					videoPath = 'pages/';
				}
				if(pageName == 'index.html' || pageName == ''){
					videoPath = 'pages/';	
				}
				for(var i=0;i<topList.length;i++){
					var topData = topList[i];
					var pic = topData.pic;
					var videoId = topData.videoId;
					
					var url = topData.url;
					var type = topData.type;
					var href = '';
					if(type == 1){
						href = videoPath+'video.html?videoId='+videoId;	
					}else if(type ==2){
						href = url;	
					}else if(type == 3){
						console.log(isLogin());
						if(!isLogin()){
							href = 'forms/login.html';
						}else{
							href = url+'?source=h5&userId='+getUserId();	
						}
					}
					var html = 		'<li><a href="'+href+'"><img src="'+pic+'" alt=""></a></li>';
					homeHtml = homeHtml + html;
					// +'<li><a href="'+href+'"><img src="images/banner02.png" alt=""></a></li>'
				}
				$('#topBegin').html(homeHtml);
				if($('#topBegin').find('li').length==1){

				}else{
					bannerSlide();
				}
				
				//预约
				var homeReservation = list[1];
				if(homeReservation){
				
					var homeReserHtml='';
					var reserImg = 'images/ico-15.png';
					var pageName = getPageName();
					if(pageName == 'live.html'){
						reserImg = '../images/ico-15.png';	
					}
					var homeReserList = homeReservation.data;
					for(var i=0;i<homeReserList.length;i++){
						var homeReser = homeReserList[i];
						var albumId = homeReser.albumId;
						var name = homeReser.name;
						var isSubscribe = homeReser.isSubscribe;
						//alert(isSubscribe);
						
						var yuyue = '';
						var aclass = '';
						if(isSubscribe == 1){
							yuyue = '已预约';	
							aclass = 'reser';

						}else{
							yuyue = '预约';	
						}
						var html = 		'<li >';
						html = html + 	'	<div class="type"><img src="'+reserImg+'"></div>';
						html = html + 	'	<div class="li-name">'+name+'</div>';
						html = html + 	'	<div class="btn"><a class="order '+aclass+'" id="'+albumId+'" onClick="doReservation(this,&quot;'+name+'&quot;)" href="javascript:void(0)">'+yuyue+'</a></div>';
						html = html + 	'</li>';
						homeReserHtml = homeReserHtml+html;
					}

					$('#homeReservationBegin').after(homeReserHtml);
				}

				var video = list[2];
				if(video){

					var videoHtml = '';
					var videoList = video.data;
					for(var i=0;i<videoList.length;i++){
						var videoData = videoList[i];
						var name = videoData.name;
						var pic = videoData.pic;
						var videoId = videoData.videoId;
						var type = videoData.type;
						var href = '';
						var url = videoData.url;
						if(type == 1|| type == 0){
							href = '/pages/video.html?videoId='+videoId;	
						}else if(type ==2){
							href = url;	
						}

						var html = 		'<li id='+videoId+'>';
						html = html + 	'	<div class="pic">';
						html = html + 	'		<a href="'+href+'"><img src="'+pic+'"></a>';
						html = html + 	'		<!--div class="length">36:12</div-->';
						html = html + 	'	</div>';
						html = html + 	'	<p>'+name+'</p>';
						html = html + 	'</li>';
						videoHtml = videoHtml+html;
					}
					$('#videoBegin').after(videoHtml);
				}
			}else{
				alert(data.message);
				return;
			}
		}
	})
}

//预约
function doReservation(_this,name){
	if(!isLogin()){
		showLogin();
		alert(comment_must_login);
		return;	
	}
	var albumId = $(_this).attr('id');
	var albumName = name;//$(_this).attr('href');
	var flag = $(_this).hasClass('reser');
	//console.log(flag);
	//true就是取消预约，false就是预约
	var url = '';
	if(flag){
		url = http_head+"/m/reservation/del?albumId="+albumId+"&albumName="+albumName+"&userId="+getUserId();
	}else{
		url = http_head+"/m/reservation/add?albumId="+albumId+"&albumName="+albumName+"&userId="+getUserId();
	}
	
	$.ajax({
		type: "get",
		dataType: "jsonp",
		url: url,
		error : function() {
			alert('error');
		},
		
		success : function(data) {
			var status = data.status;
			if(status == 1){
				if(flag){
					$(_this).text('预约');
					$(_this).removeClass('reser');
					alert('取消预约');
				}else{
					$(_this).text('已预约');
					$(_this).addClass('reser');
					$('.disk-buy').show();
				}
			}else{
				alert(data.message);	
			}
		}
	})	
}

//判断logo点效果
function isLoginClick(){
	if(isLogin()){
		$('.btn').removeClass('btn-login');
	}
}

//检查手机号是否规范
function checkMobile(str) {
    var  re = /^1\d{10}$/
    if (re.test(str)) {
        return true;
    } else {
        return false;
    }
}

//检查邮箱是否规范
function checkEmail(email){
	var bo=/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/.test(email);
	if(bo){
		return true;
	}else{
		return false;	
	}
}

//添加cookie
function setCookie(name,value){
	//escape (value)
    var Days = 30;
    var exp = new Date();
    exp.setTime(exp.getTime() + Days*24*60*60*1000);
	//$.cookie('name', 'value', {expires: 7, path: '/', secure: true}); 
	var cookie = name + "="+ encodeURIComponent(value) + ";path=/;expires=" + exp.toGMTString()+"";
	//alert(cookie);
    document.cookie = cookie;
} 

//将用户信息放入cookie中
function setUserCookie(userEntity){
	//userEntity.userName
	//decodeURIComponent
	setCookie('_I',userEntity.id);
	//alert(getUserName());
	setCookie('_N',userEntity.userName);
	setCookie('_S',userEntity.status);
	setCookie('_F',userEntity.faceUrl);
}

//检查用户是否登陆
function isLogin(){
	if(getUserId()){
		return true;	
	}else{
		return false;
	}
}

//获取用户id
function getUserId(){
	return getCookie('_I');
}

//获取用户status
function getUserStatus(){
	return getCookie('_S');	
}

//获取用户姓名
function getUserName(){
	return getCookie('_N');	
}

//获取用户头像
function getUserFace(){
	return getCookie('_F');	
}

//获取cookie值
function getCookie(name){
	var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");
 	//alert(reg);
	if(arr=document.cookie.match(reg)){
		data = decodeURIComponent(arr[2]);
		//alert(data);
		//data = eval("("+data+")");
		//alert(//data);
		return data;
	}else{
		return null;
	}	
}

//ajax
function getDataFromAjax(url){
	var json;
	$.ajax({
		type: "get",
		dataType: "jsonp",
		url: url,
		error : function() {
			alert('error');
		},
		success : function(data) {
			json = data;
		}
	});	
	return json;
}



//导航栏初始化
function navigation(){
	var pageName = getPageName();
	//alert(pageName);
	var ex
	if(pageName == 'index.html'){
		ex = '';
	}else{
		ex = '../';	
	}
	
	var html = 		'<ul class="active_ul">';
	html = html + 	'	<li>';
	html = html + 	'		<a href="'+http_linux+'/index.html'+'">';
	html = html + 	'			<img class="on" src="'+ex+'images/ico-01.png">';
	html = html + 	'			<img class="off" src="'+ex+'images/ico-02.png">';
	html = html + 	'			<span>首页</span>';
	html = html + 	'		</a>';
	html = html + 	'	</li>';
	html = html + 	'	<li>';
	html = html + 	'		<a href="'+http_linux+'/pages/chanal.html'+'">';
	html = html + 	'			<img class="on" src="'+ex+'images/ico-03.png">';
	html = html + 	'			<img class="off" src="'+ex+'images/ico-04.png">';
	html = html + 	'			<span>音乐节</span>';
	html = html + 	'		</a>';
	html = html + 	'	<li>';
	html = html + 	'		<a href="'+http_linux+'/pages/live.html'+'">';
	html = html + 	'			<img class="on" src="'+ex+'images/ico-09.png">';
	html = html + 	'			<img class="off" src="'+ex+'images/ico-10.png">';
	html = html + 	'			<span>直播</span>';
	html = html + 	'		</a>';
	html = html + 	'	</li>';
	html = html + 	'	<li>';
	html = html + 	'		<a href="'+http_linux+'/pages/rank.html'+'">';
	html = html + 	'			<img class="on" src="'+ex+'images/ico-11.png">';
	html = html + 	'			<img class="off" src="'+ex+'images/ico-12.png">';
	html = html + 	'			<span>排行</span>';
	html = html + 	'		</a>';
	html = html + 	'	</li>';
	html = html + 	'	<li>';
	html = html + 	'		<a href="'+http_linux+'/pages/topic.html'+'">';
	html = html + 	'			<img class="on" src="'+ex+'images/ico-13.png">';
	html = html + 	'			<img class="off" src="'+ex+'images/ico-14.png">';
	html = html + 	'			<span>专题</span>';
	html = html + 	'		</a>';
	html = html + 	'	</li>';
	html = html + 	'</ul>';
	
	$('.sj').after(html);
	if(pageName == 'rank.html'){
		$('.active_ul li').eq(3).addClass('active');
	}else if(pageName == 'topic.html'){
		$('.active_ul li').eq(4).addClass('active');
	}else if(pageName == 'index.html' || pageName ==''){
		$('.active_ul li').eq(0).addClass('active');
	}else if(pageName == 'live.html'){
		$('.active_ul li').eq(2).addClass('active');
	}else if(pageName == 'chanal.html'){
		$('.active_ul li').eq(1).addClass('active');
	}
}

//判断图片是否缓存
function imageCache(url){
	var img = new Image();
	img.src = url;
	 
	if(img.complete) {
		//alert('该图片已经存在于缓存之中，不会再去重新下载');
	}else{
		//alert('图片不存在缓存之中');
		img.onload;//
	}	
}

// 错误提示
function errorTip(id,content){
	id.removeClass('hidden');
	id.parent().addClass('failed');
	id.find('span').text(content);
}
function publicError(content){
	$('.publicErrorBar').show().find('span').text(content);
	$('.publicErrorBar').fadeOut(2000);
}


// 提示弹窗（自动消失
function tipShow(content){
	var _wrap = $('.tip-disk');
	_wrap.stop(true,true).fadeIn('fast');
	_wrap.children('span').html(content);
	_wrap.fadeOut(2000);
}

