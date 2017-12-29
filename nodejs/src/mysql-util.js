var Q      = require('q');
var mysql  = require('mysql');
const config = require('../config.js').env_config.mysql;

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
    port: config.port,
    dialect: 'mysql',
    pool: {
        max: 100,
        min: 0,
        acquire: 30000,
        idle: 10000
    },
    define: {
        freezeTableName: true,
        timestamps: true, // true by default
        createdAt: 'create_ts',
        updatedAt: 'update_ts',
    }
});

module.exports.query = query
module.exports.sequelize = sequelize
module.exports.Sequelize = Sequelize

// let sql = 'select * from blog;'
// let res = query(sql, [])
// console.log(res);
