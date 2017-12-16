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

module.exports.query = query

