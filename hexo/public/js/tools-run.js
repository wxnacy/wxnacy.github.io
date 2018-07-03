var htmlDom = document.getElementById("html");
var nameDom = document.getElementById("name");
document.getElementById("download").addEventListener("click", download, false);
document.getElementById("save").addEventListener("click", save, false);
document.getElementById("run").addEventListener("click", run, false);
document.getElementById("fmt").addEventListener("click", format, false);

document.onkeydown = function(e) {
  var keyCode = e.keyCode || e.which || e.charCode;
  var ctrlKey = e.ctrlKey || e.metaKey;
  if(ctrlKey && keyCode == 83) {
    e.preventDefault();
    save()
  }
  return true;
}

// layer.open({
  // type: 1 //此处以iframe举例
  // ,title: 'console 输出'
  // ,area: ['390px', '330px']
  // ,shade: 0
  // ,offset: [ //为了演示，随机坐标
    // Math.random()*($(window).height()-300)
    // ,Math.random()*($(window).width()-390)
  // ]
  // ,maxmin: true
  // ,content: '<div id="console"></div>'
  // ,btn: ['继续弹出', '全部关闭'] //只是为了演示
  // ,yes: function(){
    // $(that).click(); //此处只是为了演示，实际使用可以剔除
  // }
  // ,btn2: function(){
    // layer.closeAll();
  // }
  // ,zIndex: layer.zIndex //重点1
  // ,success: function(layero){
    // layer.setTop(layero); //重点2
  // }
// });


var editor = '';
$(function() {
  $('textarea[data-editor]').each(function() {
    var textarea = $(this);
    console.log(textarea);
    var mode = this.getAttribute('data-editor')
    var editDiv = $('<div>', {
      position: 'absolute',
      width: textarea.width(),
      height: textarea.height(),
      'class': textarea.attr('class')
    }).insertBefore(textarea);

    // var editDiv = document.createElement("div");
    // editDiv.style.position = "absolute"
    // editDiv.style.width = this.style.width
    // editDiv.style.height = this.style.height

    textarea.css('display', 'none');
    editor = ace.edit(editDiv[0]);
    editor.renderer.setShowGutter(textarea.data('gutter'));
    setEditorValue(textarea.val())
    editor.getSession().setMode("ace/mode/" + mode);
    editor.setTheme("ace/theme/idle_fingers");
    init()
  });
});
function format(){
  var beautify = ace.require("ace/ext/beautify"); // get reference to extension
  beautify.beautify(editor.session);
};
function formatCode(editor, mode) {
  var ace = editor.ace;
  var sel = ace.selection;
  var session = ace.session;
  var range = sel.getRange();

  var value = session.getTextRange(range);

  value = doFormatting(value);

  var end = session.diffAndReplace(range, value);
  sel.setSelectionRange(Range.fromPoints(range.start, end));

  return true;
}

function getEditorValue(){
  return editor.getSession().getValue()
};
function setEditorValue(content){
  htmlDom.value = content
  editor.getSession().setValue(content)

};
function init(){
  var id = WebTools.getArgsValue('id')
  if(!isEmpty(id)){
    fetchGet(`https://api.wxnacy.com/api/v1/code/${id}`).then(function(data){
      var html = decodeURIComponent(data.data.code.html)
      var name = data.data.name

      setEditorValue(html)
      nameDom.value=name
      document.title = name
      run()
    })
  } else {
    run()
  }
}
function download(){
  var cont = getEditorValue()
  var downDom = document.createElement('a');
  downDom.href = `data:text/html;charset=UTF-8,${encodeURIComponent(cont)}`
  downDom.download = nameDom.value || '未命名'
  downDom.click()
};
function run(){
  var content = getEditorValue()
  var preview = document.getElementById('preview');
  preview.srcdoc = content;
}
function save(){
  if( !checkIsLogin() ){
    alert('请登录')
    return
  }
  console.log('save');
  // var content = editor.getSession().getValue(); // htmlDom.value;
  var content = getEditorValue()
  console.log(content);
  var code = {
    html: encodeURIComponent(content),
    js: "",
    css: ""
  }
  var params = {
    name: nameDom.value,
    id: getValue('id'),
    description: '',
    source: 'run',
    code: code
  }

  fetchPost(`https://api.wxnacy.com/api/v1/code`, params).then(data => {
    if( data.status == 401 ){
      alert('请先登录')
      return
    }
    let id = data.data.id
    window.location.href = `${window.location.pathname}?id=${id}`
  })
}
