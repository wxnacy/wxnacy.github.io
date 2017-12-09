
var digits = [
    '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9',
    'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    '!', '@', '#', '$', '%', '^',
    '&','*'
];
var NUM = [
    '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9',
];
var letter = [
    'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z',
];
var LETTER = [
    'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
];
var special = [
    '!', '@', '#', '$', '%', '^',
    '&','*'
];
function getRandom(len){
    var array = new Array(len);
    array[0] = LETTER[parseInt(Math.random() * LETTER.length)];
    array[1] = letter[parseInt(Math.random() * letter.length)];
    array[2] = special[parseInt(Math.random() * special.length)];
    array[3] = NUM[parseInt(Math.random() * NUM.length)];
    for(var i = 4; i < len; i++){
        array[i] = digits[parseInt(Math.random() * digits.length)];
    }
    var res = array.join('');
    document.getElementById('out').innerHTML = res;
    return array.join('');
}

