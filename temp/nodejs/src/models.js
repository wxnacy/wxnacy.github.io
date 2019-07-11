'use strict';
const fetch = require('node-fetch');
const cheerio = require('cheerio');
const config = require('../config.js');
const env_config = config.env_config;
const mysql = require('./mysql-util.js')
const sequelize = mysql.sequelize;
const Sequelize = mysql.Sequelize;
const HTTPS = env_config.https

const Blog = sequelize.define('blog', {
    id: { type: Sequelize.INTEGER, primaryKey: true, autoIncrement: true, },
    route: { type: Sequelize.STRING, defaultValue: '' },
    name: { type: Sequelize.STRING, defaultValue: '' },
    page_view: { type: Sequelize.INTEGER, defaultValue: 0 },
    ext: { type: Sequelize.JSON, defaultValue: {} },
    is_del: { type: Sequelize.INTEGER, defaultValue: 0 },
});

/**
 * 刷新阅读量
 */
Blog.prototype.refreshPV = function(pv) {
    if( this.page_view < pv   ){
        this.page_view = pv
    }
    return this.save()
}

/**
 * 刷新字段信息
 */
Blog.prototype.refresh = function(){
    let url = `${HTTPS}${this.route}`
    return fetch(url).then(res => res.text())
        .then(text => {
            const $ = cheerio.load(text);
            let title = $('meta[property="og:title"]').attr('content');
            return {"title": title};
        }).then(data => {
            this.name = data['title']
            return this.save()
        });
};

const Code = sequelize.define('code', {
    id: { type: Sequelize.STRING, primaryKey: true },
    name: { type: Sequelize.STRING, defaultValue: '' },
    description: { type: Sequelize.STRING, defaultValue: '' },
    type: { type: Sequelize.STRING, defaultValue: '' },
    code: { type: Sequelize.JSON, defaultValue: {} },
    is_available: { type: Sequelize.INTEGER, defaultValue: 1 },
});

module.exports.Blog = Blog;


