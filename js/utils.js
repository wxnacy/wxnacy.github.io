/**
 * Created by wxnacy on 17/8/4.
 */
'use strict';

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
        console.log(document.body.clientWidth, document.body.clientHeight)
        console.log('screen', window.screen.width, window.screen.height)
        console.log('scroll', document.body.scrollWidth, document.body.scrollHeight)
        var w = document.body.scrollWidth;
        var h = document.body.scrollHeight;
        // if (w <= h) {
        //     $(".layout").css({width: w})
        // }
    }
};

var web = {};