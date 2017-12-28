'use strict'
const mysql = require('../src/mysql-util.js')
const sequelize = mysql.sequelize;
const Sequelize = mysql.Sequelize;
const models = require('../src/models.js')
const Blog = models.Blog;

const Test = sequelize.define('test', {
    id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true,
    },
    name: {
        type: Sequelize.STRING
    },
    create_ts: {
        type: Sequelize.DATE
    }
});

// Test.build({name: "ning"}).save().then(() => {sequelize.close()})

// Test.build({name: "wxnacy"}).save()
    // .then(() => {
        // return Test.findById(1)
    // }).then(item => {
        // console.log(item.id, item.name);
        // sequelize.close()
    // }).catch(e => {
        // console.log(e);
        // sequelize.close()
    // })

// Test.findOne({where: {name: 'wxnacy'}}).then(test => {
    // console.log(test)
    // sequelize.close()
// }).catch(e => {
    // sequelize.close()
// })

// Blog.findById(23).then(blog => {
    // // console.log(blog.toJSON());
    // return blog.refresh()
    // sequelize.close()
// }).then(res => {
    // console.log(res);
// })

// Blog.create({route: "prototype"}).then(blog => {
    // console.log(blog.toJSON());
// })
//

Blog.findOrCreate({where: {route: "test"}, defaults: {page_view: 10}})
    .spread((blog, created) => {
        console.log(blog.get({plain: true}).id, created);
        console.log(blog.toJSON().id);
        sequelize.close()
    })
    // .then(res => {
        // console.log();
        // sequelize.close()
    // })
