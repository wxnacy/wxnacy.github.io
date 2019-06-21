/**
 * Created by wxnacy on 17/8/4.
 */
'use strict';

$(function () {
    layout.init_html();
})

var utils = {
    isEmpty(val){
        if (val == '' || val == null || val == undefined || val == "undefined") {
            return true;
        }
        return false;
    },
    //获取html传参
    getValue(key)
    {
        var name = key + "=";
        var str = window.location.search;
        var beginIndex = str.indexOf("?" + name);
        if (beginIndex == -1) {
            beginIndex = str.indexOf("&" + name);
        }
        if (beginIndex != -1) {
            var pos_start = beginIndex + name.length + 1;
            var pos_end = str.indexOf("&", pos_start);
            if (pos_end == -1) {
                return decodeURIComponent(str.substring(pos_start));
            } else {
                return decodeURIComponent(str.substring(pos_start, pos_end));
            }
        }
    },
    getTimestamp(){
        var timestamp = new Date().getTime();
        return timestamp;
    }
};

var layout = {
    window_adaptive(){
        console.log(document.body.clientWidth, document.body.clientHeight);
        console.log('screen', window.screen.width, window.screen.height);
        console.log('scroll', document.body.scrollWidth, document.body.scrollHeight);
        var w = document.body.scrollWidth;
        var h = document.body.scrollHeight;
        // if (w <= h) {
        //     $(".layout").css({width: w})
        // }
    },
    init_html(){
        $("#header").html('<span><a href="/">wxnacy博客</a></span><nav><ul><li><a href="/">文章</a></li><li><a href="/pages/contact.html">联系</a></li></ul></nav>');
        $("#footer").html(' © 2017 wxnacy.com 版权所有 <a href="http://www.miitbeian.gov.cn/" target="_blank">京ICP备15062634号-3</a>');
        // var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");
        // $('body').append(unescape("%3Cspan id='cnzz_stat_icon_1263285686'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s13.cnzz.com/z_stat.php%3Fid%3D1263285686%26show%3Dpic' type='text/javascript'%3E%3C/script%3E"))
        // document.write(unescape("%3Cspan id='cnzz_stat_icon_1263285686'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s13.cnzz.com/z_stat.php%3Fid%3D1263285686%26show%3Dpic' type='text/javascript'%3E%3C/script%3E"));
        // fetch('http://localhost:8082/api/v1/user',{
        //     method:"POST"
        // }).then(res=>{
        //     console.log(res)
        // })
    }
};

var web = {};