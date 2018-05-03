var resultEditor = initEditor('result')
var paramsEditor = initEditor('params')
var urlDom = document.getElementById("url");
var nameDom = document.getElementById("name");
var methodDom = document.getElementById("method");
// resultEditor.getSession().setValue(`{"name": "wxnacy", \n"age": 0\n}`)
init()

// document.getElementById("download").addEventListener("click", download, false);
// document.getElementById("save").addEventListener("click", save, false);
document.getElementById("save").addEventListener("click", save, false);
document.getElementById("send").addEventListener("click", send, false);
document.getElementById("fmt").addEventListener("click", fmt, false);

$(function() {
  // $('textarea[data-editor]').each(initEditor);
});

function initEditor(id) {
  var textarea = $(`#${id}`);
  console.log(textarea);
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
    return res.json()
  }).then(function(data){
    console.log(data);
    setEditorValue(resultEditor, JSON.stringify(data))
    format(resultEditor)
  })
};
function fmt(){
  format(resultEditor)
};
function format(editor, fmt='json'){
  var val = editor.getSession().getValue()
  if( fmt == 'json' ){
    val = JSON5.parse(val)
    val = JSON.stringify(val, null, 4)
  }
  editor.getSession().setValue(val)
  var beautify = ace.require("ace/ext/beautify"); // get reference to extension
  beautify.beautify(editor.session);
};

function getEditorValue(editor){
  return editor.getSession().getValue()
};

function setEditorValue(editor, content){
  editor.getSession().setValue(content)
};

function init(){
  var id = getValue('id')
  if(!isEmpty(id)){
    fetchGet(`/api/v1/code/${id}`).then(function(data){
      var params = decodeURIComponent(data.data.code.params)
      var name = data.data.name

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
  if( !checkIsLogin() ){
    alert('请登录')
    return
  }
  console.log('save');
  var code = {
    params: encodeURIComponent(getEditorValue(paramsEditor)),
    url: urlDom.value,
    method: methodDom.value
  }
  var params = {
    name: '',
    id: getValue('id'),
    description: '',
    source: 'wapi',
    code: code
  }

  fetchPost(`/api/v1/code`, params).then(data => {
    if( data.status == 401 ){
      alert('请先登录')
      return
    }
    let id = data.data.id
    window.location.href = `${window.location.pathname}?id=${id}`
  })
}
