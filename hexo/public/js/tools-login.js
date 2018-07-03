const CONTANTS = {
  authorization: 'authorization',
  name: 'name'
}

checkNavLogin()
initLogin()
document.getElementById("logoutBtn").addEventListener('click', logout, false);
function setCookie(cname,cvalue,exdays) {
  var d = new Date();
  d.setTime(d.getTime()+(exdays*24*60*60*1000));
  var expires = "expires="+d.toGMTString();
  document.cookie = cname + "=" + cvalue + "; " + expires;
}

function getCookie(cname){
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i=0; i<ca.length; i++)
  {
    var c = ca[i].trim();
    if (c.indexOf(name)==0) return c.substring(name.length,c.length);
  }
  return "";
}
function initLogin(){
  document.getElementById("loginBtn").addEventListener('click', function(e){
    var email = document.getElementById("login-email").value
    var pw = document.getElementById("login-password").value
    fetchPost('https://api.wxnacy.com/api/v1/login', {
      email: email, password: pw
    }).then(function(data){
      console.log(data);
      if( data.status == 200 ){
        let res = data.data
        setCookie(CONTANTS.authorization, res.authorization)
        setCookie(CONTANTS.name, res.name)
        e.target.previousElementSibling.click()
        checkNavLogin()
      }
    })

  })
};
function checkIsLogin(){
  let authorization = getCookie(CONTANTS.authorization)
  return !isEmpty(authorization)
};
function checkNavLogin(){
  let noLogins = document.querySelectorAll('.no-login')
  let isLogins = document.querySelectorAll('.is-login')
  if( checkIsLogin() ){
    document.getElementById("userName").innerHTML = getCookie(CONTANTS.name)
    noLogins.forEach((e) => {
      e.style.display = 'none'
    })
    isLogins.forEach((e) => {
      e.classList.remove('d-none')
    })
  } else {

    noLogins.forEach((e) => {
      e.style.display = 'block'
    })
    isLogins.forEach((e) => {
      e.classList.add('d-none')
    })
  }
};
function logout(e){
  e.preventDefault()
    e.stopPropagation()
  setCookie(CONTANTS.authorization, "")
  setCookie(CONTANTS.name, "")
  checkNavLogin()
};
