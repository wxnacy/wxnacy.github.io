var Q      = require('q');
var mysql  = require('mysql');
var config = require('../local_config.json').mysql;

var query = function(sql,kwargs){
  var d = Q.defer();
  var conn = mysql.createConnection(config);
  conn.query(sql,kwargs,function(e, r, f){
    conn.end()
    if (e){
      d.reject(e);
    }
    d.resolve(r);
  })
  return d.promise;
}
const Sequelize = require('sequelize');
const sequelize = new Sequelize(config.database, config.user, config.password, {
    host: config.host,
    dialect: 'mysql',
    pool: {
        max: 100,
        min: 0,
        acquire: 30000,
        idle: 10000
    },
    define: {
        timestamps: false, // true by default
        // createAt: 'create_ts',
        // updateAt: 'update_ts',
        freezeTableName: true,
    }
});

module.exports.query = query
module.exports.sequelize = sequelize
module.exports.Sequelize = Sequelize

// let sql = 'select * from blog;'
// let res = query(sql, [])
// console.log(res);
