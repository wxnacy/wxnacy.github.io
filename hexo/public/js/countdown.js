(function () {
    var Ticts=function Ticts() {
        this.ticts = {};
    };
    Ticts.prototype.createTicts=function(id, dealline) {
        var ticts=this;
        var dd = new Date(dealline)     // 倒计时最终时间
        var time = dd - new Date()      // 距今天的毫秒数
        var _ticts=this.ticts[id] = {
            dealine: dealline
            , id: id
            , time: time
            , interval: setInterval(function () {
                var t = null;
                var d = null;
                var h = null;
                var m = null;
                var s = null;

                var now = new Date();
                t = _ticts.time / 1000; //js默认时间戳为毫秒,需要转化成秒
                var y = dd.getFullYear() - now.getFullYear()
                var M = dd.getMonth() - now.getMonth()
                var d = dd.getDate() - now.getDate()
                var h = dd.getHours() - now.getHours()
                if( M < 0 ){
                    y--;
                    M = M + 12
                }
                var flag = [1, 3, 5, 7, 8, 10, 12, 4, 6, 9, 11, 2];
                if( d < 0 ){
                    M--;
                    var index = flag.findIndex((temp) => {
                        return temp === now.getMonth() + 1
                    });
                    var monthLength;
                    if (index <= 6) {
                        monthLength = 31;
                    } else if (index > 6 && index <= 10) {
                        monthLength = 30;
                    } else {
                        monthLength = 28;
                    }
                    d = dd.getDate() + (monthLength - now.getDate());
                }
                if( h < 0 ){
                    d--;
                }
                t = t - y * 365 * 24 * 3600
                var total_day = Math.floor(t / (24 * 3600))
                t = t - 24 * 3600 * total_day
                h = Math.floor(t / 3600);
                t = t -h * 3600
                m = Math.floor(t / 60);
                t = t - m * 60
                s = Math.floor(t);
　　　　　　　　　//这里可以做一个格式化的处理,甚至做毫秒级的页面渲染,基于DOM操作,太多个倒计时一起会导致页面性能下降
                document.getElementById(id).innerHTML = `${y} 年 ${M} 月 ${d} 天 ${h} 小时 ${m} 分钟 ${s} 秒`
                _ticts.time -= 1000;
                if (_ticts.time < 0)
　　　　　　　　　　　ticts.deleteTicts(id);//判断是否到期,到期后自动删除定时器
            }, 1000)
        }
    };
    Ticts.prototype.deleteTicts = function(id) {
        clearInterval(this.ticts[id].interval);//清楚定时器的方法,需要定时器的指针作为参数传入clearInterval
        delete this.ticts[id];//通过delete的方法删除对象中的属性
    };
   //新建一个ticts对象,放到window全局函数中,那么在html页面是(或者其他js文件)可以访问该对象
    window.Ticts=new Ticts();
})();
