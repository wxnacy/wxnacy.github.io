const parser = (data) => {
    console.log(data);
    data = JSON.parse(data);
    console.log(data);
    let res = JSON.stringify(data, null, 4);
    return res;
}

module.exports.parser = parser;

// const res = parser('{"name":"age"}')
// console.log("res ", res);
// res = parser("{\"name\":\"'age'\"}")
// console.log(res)
// res = parser("{'name':'age'}")
// console.log("res", res);
