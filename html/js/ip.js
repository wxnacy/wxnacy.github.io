printIP();
function printIP(){
    fetch('https://ipapi.co/json/').then(res => {
        if( res.ok ){
            res.json().then(data => {
                const ip = data.ip;
                document.getElementById('ip').innerHTML = ip;
                return ip;
            });
        }
    });
}
