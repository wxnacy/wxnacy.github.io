
importHtml()
initNew()

function importHtml(){
  var links = document.querySelectorAll('link[rel="import"]');
  Array.prototype.forEach.call(links, (link) => {
    console.log(link);
    var template = link.import.querySelector('template');
    var content = template.content.cloneNode(true)
    if( link.href.match('nav.html') ){
      document.getElementById("nav").appendChild(content)
    } else if( link.href.match('head.html') ){
      document.getElementById("head").appendChild(content)
    }else {
      document.querySelector('body').appendChild(content);
 keys   }
  })
};


function initNew(){
  var newDom = document.getElementById("new");
  if( newDom != null ){
    newDom.href = window.location.pathname
    newDom.target = '_blank'
  }
};

var Tools = (function(){

function saveCode(source, code){
  if( !checkIsLogin() ){
    alert('请登录')
    return
  }
  var params = {
    id: getValue('id'),
    description: '',
    source: source,
    code: code
  }
  var nameDom = document.getElementById("name");

  if( !isEmpty(nameDom) ){
    params['name'] = nameDom.value
  }

  fetchPost(`https://api.wxnacy.com/api/v1/code`, params).then(data => {
    if( data.status == 401 ){
      alert('请先登录')
      return
    }
    let id = data.data.id
    window.location.href = `${window.location.pathname}?id=${id}`
  })
};
return {
  saveCode: saveCode
}
})();
