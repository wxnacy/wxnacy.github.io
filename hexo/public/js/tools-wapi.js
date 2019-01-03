var resultEditor = initEditor('result')
var resultHeadersEditor = null;
var paramsEditor = initEditor('params')
var headersEditor = initEditor('headers')
var urlDom = document.getElementById("url");
var nameDom = document.getElementById("name");
var methodDom = document.getElementById("method");
var element = null;
init()
// document.getElementById("download").addEventListener("click", download, false);
// document.getElementById("save").addEventListener("click", save, false);
document.getElementById("save").addEventListener("click", save, false);
document.getElementById("send").addEventListener("click", send, false);
document.getElementById("fmt").addEventListener("click", fmt, false);
console.log(localStorage.key);

$(function() {
  // $('textarea[data-editor]').each(initEditor);
});

layui.use('element', function() {
  initTab()
});

function initTab(){
  if( element == null ){
    element = layui.element;
  }

  //获取hash来切换选项卡，假设当前地址的hash为lay-id对应的值
  var layid = location.hash.replace(/^#test1=/, '');
  element.tabChange('test1', layid); //假设当前地址为：http://a.com#test1=222，那么选项卡会自动切换到“发送消息”这一项

  //监听Tab切换，以改变地址hash值
  element.on('tab(result-filter)', function(data) {
    // location.hash = 'test1='+ this.getAttribute('lay-id');
    console.log(location.hash);
    if( resultHeadersEditor == null ){
      resultHeadersEditor = initEditor('resultHeaders')
    }
    setResultHeaders()

  });

};

function initEditor(id) {
  var textarea = $(`#${id}`);
  var mode = textarea.data('editor')
  var editDiv = $('<div>', {
    position: 'absolute',
    width: textarea.width(),
    height: textarea.height(),
    'class': textarea.attr('class')
  }).insertBefore(textarea);

  textarea.css('display', 'none');
  var editor = ace.edit(editDiv[0]);
  editor.renderer.setShowGutter(textarea.data('gutter'));
  editor.getSession().setValue(textarea.val())
  editor.getSession().setMode("ace/mode/" + mode);
  editor.setTheme("ace/theme/idle_fingers");
  return editor
};

function send(){
  console.log("send");
  var method = document.getElementById("method").value;
  console.log(method);
  var url = document.getElementById("url").value
  var resultDom = document.getElementById("result");
  var params = getEditorValue(paramsEditor)
  console.log(params);
  var headers = {}
  if( method != 'GET' ){
    if( !isEmpty(params) ){
      headers['Content-Type'] = 'application/json'
    }
  }
  var fetchParams = {
    method: method,
    headers: headers
  }

  if( !isEmpty(params) && method != 'GET' ){
    fetchParams['body'] = params
  }
  fetch(url, fetchParams).then(function(res){
    headers = res.headers
    console.log(headers.entries());
    console.log(headers.keys());
    console.log(headers.values());
    var h = {
      'Access-Control-Allow-Origin': headers.get('Access-Control-Allow-Origin'),
      'Connection': headers.get('Connection'),
      'Content-Type': headers.get('Content-Type'),
      'Content-Length': headers.get('Content-Length'),
      'Date': headers.get('Date'),
      'Server': headers.get('Server'),
    }
    console.log(h);
    setResultHeaders(h)

    return res.json()
  }).then(function(data){
    console.log(data);
    setEditorValue(resultEditor, data)
  })
};
function fmt(){
  format(resultEditor)
};
function format(editor, fmt='json'){
  var val = editor.getSession().getValue()
  if( fmt == 'json' ){
    // val = JSON5.parse(val)
    // val = JSON.stringify(val, null, 4)
  }
  editor.getSession().setValue(val)
  var beautify = ace.require("ace/ext/beautify"); // get reference to extension
  beautify.beautify(editor.session);
};

function getEditorValue(editor){
  return editor.getSession().getValue()
};

function setEditorValue(editor, content){
  if( typeof content == 'object' ){
    content = JSON.stringify(content, null, 4)

  }
  format(editor)
  editor.getSession().setValue(content)
};

function init(){
  localStorage.clear()
  var id = getValue('id')
  if(!isEmpty(id)){
    fetchGet(`https://api.wxnacy.com/api/v1/code/${id}`).then(function(data){
      var params = decodeURIComponent(data.data.code.params)
      var name = data.data.name
      var code = data.data.code
      urlDom.value = code.url;

      setEditorValue(paramsEditor, params)
      // nameDom.value=name
      methodDom.value = data.data.code.method
      document.title = name
    })
  } else {
  }
}

function jsSelectIsExitItem(objSelect, objItemValue) {
  var isExit = false;
  for (var i = 0; i < objSelect.options.length; i++) {
    if (objSelect.options[i].value == objItemValue) {
      isExit = true;
      break;
    }
  }
  return isExit;
}
function download(){
  var cont = getEditorValue()
  var downDom = document.createElement('a');
  downDom.href = `data:text/html;charset=UTF-8,${encodeURIComponent(cont)}`
  downDom.download = nameDom.value || '未命名'
  downDom.click()
};
function save(){
  console.log('save');
  var code = {
    params: encodeURIComponent(getEditorValue(paramsEditor)),
    url: urlDom.value,
    method: methodDom.value
  }
  Tools.saveCode('wapi', code)
}
function setItem(k, v){
  if( typeof v == 'object' ){
    v = JSON.stringify(v, null, 4)
  }
  // localStorage.setItem(`${methodDom.value}-${urlDom.value}-${k}`, v)
  localStorage.setItem(k, v)
};
function getItem(k){
  res = localStorage.getItem(k)
  if( isEmpty(res) ){
    res = ''
  }
  return res
};
function setResultHeaders(h){
  k = 'resultHeaders'
  if( !isEmpty(h) ){
    setItem(k, h)
  }
  h = getItem(k)
  if( resultHeadersEditor != null ){
    setEditorValue(resultHeadersEditor, h)
  }

};
