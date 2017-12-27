'use strict';
const fetch = require('node-fetch');
const cheerio = require('cheerio');
const mysql = require('./mysql-util.js')

const HTTPS = 'https://wxnacy.com'

function Blog(id, route){
    this.id=id;
    this.route=route;
};

Blog.prototype.refresh = () => {
    console.log(this.id, this.route);
    this.id = 22;
    this.route = '/2017/11/27/make-time-firends';
    console.log(this.route);
    let url = `${HTTPS}${this.route}`
    console.log(url);
    // url = 'https://wxnacy.com/2017/11/27/make-time-firends/'
    fetch(url).then(res => res.text())
        .then(text => {
            const $ = cheerio.load(text);
            let title = $('meta[property="og:title"]').attr('content');
            return {"title": title};
        }).then(data => {
            let sql = 'update blog set name = ? where id = ?';
            return mysql.query(sql, [data['title'], this.id])
        }).then(res => {
            console.log(res);
        }).catch(e => {
            console.log(e);
        })
    console.log(url);
}

let blog = new Blog(22, 'sss');

blog.refresh()
