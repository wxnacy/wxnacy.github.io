/**
 * Created by wxnacy on 17/4/16.
 */


var config = {
    getPage(){
        var page = getValue('page');
        if (page == undefined) {
            page = 1
        }
        return page
    },
    image_suffix: "?x-oss-process=image/resize,m_lfit,w_120,limit_0/auto-orient,0/quality,q_90",
    getType(){
        var type = getValue('type');
        if (utils.isEmpty(type)) {
            type = 81
        }
        return type;
    }
}


$(function () {

})


var utils = {
    isEmpty(val){
        if (val == '' || val == null || val == undefined || val == "undefined") {
            return true;
        }
        return false;
    },
    //获取html传参
    getValue(key)
    {
        var name = key + "=";
        var str = window.location.search;
        var beginIndex = str.indexOf("?" + name);
        if (beginIndex == -1) {
            beginIndex = str.indexOf("&" + name);
        }
        if (beginIndex != -1) {
            var pos_start = beginIndex + name.length + 1;
            var pos_end = str.indexOf("&", pos_start);
            if (pos_end == -1) {
                return decodeURIComponent(str.substring(pos_start));
            } else {
                return decodeURIComponent(str.substring(pos_start, pos_end));
            }
        }
    },
    getTimestamp(){
        var timestamp = new Date().getTime();
        return timestamp;
    },
    goToPageWithOutCache(url){
        window.location.href = this.makeNoCacheUrl(url);
    },
    makeNoCacheUrl(url){
        if (url.indexOf('?') > 0) {
            url = url + '&timestamp=' + this.getTimestamp();
        } else {
            url = url + "?timestamp=" + this.getTimestamp();
        }
        return url;
    },
    makeInitData(initData){
        initData['loading'] = false;
        return initData;
    },
    makeMain(initData){

        initData['loading'] = false;
        return {
            data() {
                return initData
            },
            methods: {
                onSubmit(e) {
                    var formData = this.form
                    console.log('form_data', formData)
                    $.ajax({
                        url: "/admin/v1/video/edit.json",
                        type: "post",
                        data: formData,
                        success: function (data) {
                            utils.goToPageWithOutCache('list.html');
                        }
                    })
                },
                onBack(e){
                    utils.goToPageWithOutCache('list.html');
                },
                handleUploadImageSuccess(res, file, fileList){
                    this.$set(this.form, "poster", res.data.url)
                    this.loading = false;
                },
                handleBeforeUpload(file){
                    this.loading = true
                }
            }
        }
    }
}


//获取html传参
function getValue(key) {
    return utils.getValue(key);
}

function deleteItem(obj, id, params, url) {
    if (id == "") {
        obj.$message.error('请先选择一条记录');
    } else {
        obj.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
        }).then(() => {
            $.ajax({
                url: url,
                type: "delete",
                data: params,
                success: function (data) {
                    console.log(data)
                    if (data['status'] == 200) {
                        obj.$message({
                            type: 'success',
                            message: '删除成功!'
                        });
                        window.location.href = window.location.href;
                    } else {
                        obj.$message.error(data['删除失败']);
                    }
                },
                error: function (res, error, errorMsg) {
                    obj.$message.error(res['responseJSON']['message'])
                }
            })
        }).catch(() => {
            obj.$message({
                type: 'info',
                message: '已取消删除'
            });
        });
    }
}


function deleteResource(obj, res_id, res_type) {
    deleteItem(obj, res_id, {
        "res_id": res_id,
        "res_type": res_type
    }, "/admin/v1/resource/delete.json")
}

function goToEditHtml(id) {
    if (id == "") {
        this.$message.error('请先选择一条记录');
    } else {
        window.location.href = 'edit.html?id=' + id
    }
}

function fetchGet(url) {
    return fetchRequest(url, 'GET')
}
function fetchPost(url, params) {
    return fetchRequest(url, 'POST', params)
}
function fetchPut(url, params) {
    return fetchRequest(url, 'PUT', params)
}
function fetchRequest(url, method, params) {
    var headers = {
        "authorization": "XXXXXXXXX"
    }
    if( method.toLowerCase() == 'post' ){
        headers['Content-Type']= 'application/json'
    }
    return new Promise(function(resolve, reject) {
        fetch(url, {
            method: method,
            headers: headers,
            body: JSON.stringify(params)
        }).then(function(res){
            return res.json()
        }).then(function(data){
            resolve(data)
        }).catch(function(e){
            console.log(e);
            reject(e)
            // 需要统一的处理错误方式，避免每次都catch
        })
    })
}
