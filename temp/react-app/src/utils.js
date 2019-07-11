import { Message  } from 'element-react';
import fetch from 'node-fetch';
export const fetchGet = (url) => {
    return fetchRequest(url, 'GET', null)
}
export const fetchPost = (url, params) => {
    return fetchRequest(url, 'POST', params)
}
export const fetchRequest = ( url, method, params ) => {
    console.log(`${url}`);
    let headers = {
        "Authorization": "5e589393a1a606cc241250e9b533c8e229b5d12eb06d0cdc166d89e883adc305"
    }
    if( method.toLowerCase() === 'post' || method.toLowerCase() === 'put' ){
        headers['Content-Type']= 'application/json'

    }
    return new Promise(function(resolve, reject) {
        fetch(url, {
            method: method,
            headers: headers,
            body: JSON.stringify(params)
        }).then(res => {
            return res.json()
        }).then(data => {
            console.log(data);
            if( data.status === 200 ){
                resolve(data)
            } else {
                Message({
                    showClose: true,
                    message: data.message,
                    type: 'error'

                });
            }
        }).catch(e => {
            console.log(e);
            Message({
                showClose: true,
                message: e.message,
                type: 'error'

            });

        })
    })
}

