printIP();
function printIP(){
    fetch('http://ip-api.com/json').then(res => {
        if( res.ok ){
            res.json().then(data => {
                const ip = data.query;
                document.getElementById('ip').innerHTML = ip;
                return ip;
            });
        }
    });
}
