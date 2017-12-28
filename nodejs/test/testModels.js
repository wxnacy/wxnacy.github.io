'use strict'
const mysql = require('../src/mysql-util.js')
const sequelize = mysql.sequelize;
const Sequelize = mysql.Sequelize;
const Op = Sequelize.Op;
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
}, {
    timestamps: true,
    updatedAt: false,
    createdAt: 'create_ts'
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

Blog.findById(23).then(blog => {
    console.log(blog);
    sequelize.close()
}).catch(e => {
    console.log(e);
    sequelize.close()
})

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

// Blog.findOrCreate({where: {route: "test"}, defaults: {page_view: 10}})
    // .spread((blog, created) => {
        // console.log(blog.get({plain: true}).id, created);
        // console.log(blog.toJSON().id);
        // sequelize.close()
    // })
    // // .then(res => {
        // // console.log();
        // // sequelize.close()
    // // })
//

Blog.findAll({
    where: {
        route: {
            [Op.like]: '/2017/%'
        }
    },
    order: [['page_view','DESC']],
    limit: 10
    }) .then(items => {
        let lines = []
        items.forEach(d => {
            d.refresh()
            let line = `- [${d.name}](${d.route})`
            lines.push(line)
        })
        let res = lines.join('\n')
        console.log(res);
    })
