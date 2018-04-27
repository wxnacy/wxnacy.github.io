// var $navDiv = $('#nav-div')

importHtml()
initLogin()
// $(function(){
  // // initNav()
  // // initLogin()
  // });


// function initNav(){
  // $navDiv.addClass('d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom box-shadow')
  // $navDiv.append('<h5 class="my-0 mr-md-auto font-weight-normal">Wxnacy 工具</h5>')
  // $nav = $('<nav class="my-2 my-md-0 mr-md-3"></nav>')
  // $nav.append('<a class="p-2 text-dark" href="/" target="_black">博客</a>')
  // $navDiv.append($nav)
  // $navDiv.append('<a class="btn btn-outline-primary" data-toggle="modal" data-target="#loginModel" href="#">登录</a>')
  // $navDiv.append('<a class="btn btn-outline-primary" style="margin-left: 10px" href="#">注册</a>')
  // };

function initLogin(){
  document.getElementById("loginBtn").addEventListener('click', function(e){
    var email = document.getElementById("email").value
    var pw = document.getElementById("password").value
    fetchPost('/api/v1/login', {
      email: email, password: pw
    }).then(function(data){
      console.log(data);
    })

  })
};

function importHtml(){
  var links = document.querySelectorAll('link[rel="import"]');
  Array.prototype.forEach.call(links, (link) => {
    console.log(link);
    var template = link.import.querySelector('template');
    var content = template.content.cloneNode(true)
    if( link.href.match('nav.html') ){
      document.getElementById("nav").appendChild(content)
    } else {

      document.querySelector('body').appendChild(content);
    }
  })
};


