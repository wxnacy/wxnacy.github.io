var digits=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","@","#","$","%","^","&","*"];var NUM=["0","1","2","3","4","5","6","7","8","9"];var letter=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];var LETTER=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"];var special=["!","@","#","$","%","^","&","*"];function getRandom(e){var t=new Array(e);t[0]=LETTER[parseInt(Math.random()*LETTER.length)];t[1]=letter[parseInt(Math.random()*letter.length)];t[2]=special[parseInt(Math.random()*special.length)];t[3]=NUM[parseInt(Math.random()*NUM.length)];for(var n=4;n<e;n++){t[n]=digits[parseInt(Math.random()*digits.length)]}var o=t.join("");document.getElementById("out").innerHTML=o;return t.join("")}function create_visit(){console.log(window.location.search);console.log(document.getElementById("busuanzi_value_page_pv").value);fetch("/api/visit",{method:"POST"}).then(function(e){return e.json()}).then(function(e){console.log(e)})}function create_crypto(e){var t=document.getElementById("msg").value;var n=document.getElementById("key").value;fetch("/api/crypto",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({content:t,type:e,key:n})}).then(function(e){return e.json()}).then(function(t){console.log(t);body=t.data;if(e=="default"||e=="hmac"){document.getElementById("crypto").style.display="none";document.getElementById("hash").style.display="block";document.getElementById("md5").innerHTML=body.md5;document.getElementById("sha1").innerHTML=body.sha1;document.getElementById("sha256").innerHTML=body.sha256;document.getElementById("sha512").innerHTML=body.sha512}else{document.getElementById("hash").style.display="none";document.getElementById("crypto").style.display="block";document.getElementById("result").innerHTML=body.result}})}