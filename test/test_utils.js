
function getValue(key) {
    var name = key + "=";
    // var str = window.location.search;
    var str = 'http://localhost/www?v=dddddd&n=d3d';
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
}

console.log(getValue('n'));
