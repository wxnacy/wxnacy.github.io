
importHtml()


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
    }
  })
};


