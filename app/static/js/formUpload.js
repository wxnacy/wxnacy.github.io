/**
 * Created by 郝少禅
 * Email:sxchying@126.com
 * QQ:490746237
 */
window.formUpload = (function () {
    function formUpload() {
    }
    //是否可以上传
    var isNotUpload = false;
    var selectFileOption = {};
    var uploadOption = {};
    (function () {
        //绑定选择文件按钮
        (function ($) {
            var defaults = {
                maxFileSize: 1024 * 1024 * 1024,
                addFiles: function (fileName) {

                },
                errorCallback: function (data) {

                }
            };
            $.fn.selectUpload = function (options) {
                selectFileOption = $.extend(defaults, options || {});
                return this.each(function () {
                    $(this).click(fileOperation.fileSelect);
                });
            };
        })(jQuery);
        //绑定上传按钮
        (function ($) {
            var defaults = {
                initUrl: "",
                uploadProgress: function (data) {

                },
                finishCallback: function (data) {

                },
                errorCallback: function (data) {

                }
            };
            $.fn.upload = function (options) {
                uploadOption = $.extend(defaults, options || {});
                return this.each(function () {
                    $(this).click(function () {
                        if (isNotUpload == false) {
                            uploadOption.errorCallback({ code: 131, msg: "未选择文件" });
                        } else {
                            videoUpload.tryUpload();
                        }
                    });
                });
            };
        })(jQuery);
    })();
    var fileOperation = (function () {
        function fileOperation() {
        }
        var fileTypes = "wmv|avi|dat|asf|rm|rmvb|ram|mpg|mpeg|mp4|mov|m4v|mkv|flv|vob|qt|divx|cpk|fli|flc|mod|dvix|dv|ts";
        var getFileType = function (file) {
            return file.name.split(".").pop();
        };
        var showFileList = function (e) {
            if (e.target.files.length > 1) {
                selectFileOption.errorCallback({ code: 100, msg: "只能选择一个文件" });
            } else {
                var file = e.target.files[0];
                var fType = getFileType(file);
                if (file.size > selectFileOption.maxFileSize) {
                    selectFileOption.errorCallback({ code: 101, msg: "文件过大" });
                } else if (eval("/" + fileTypes + "$/i").test(fType) == false) {
                    selectFileOption.errorCallback({ code: 102, msg: "不支持此文件类型" });
                } else {
                    selectFileOption.addFiles({code:0,fileName:file.name});
                    fileOperation.selectFile = file;
                    isNotUpload = true;
                }
            }
        };
        fileOperation.selectFile = {};
        fileOperation.fileSelect = function (e) {
            var form = document.getElementById("form_Hsc");
            if (!form) {
                form = document.createElement("form");
                $("body").append(form);
                form.setAttribute("id", "form_Hsc");
                form.setAttribute("name", "form_Hsc")
                form.setAttribute("enctype", "multipart/form-data")
            }
            var inpfile = document.getElementById("fileUploadId_Hsc");
            if (inpfile) {
                inpfile.click && e.target != inpfile && inpfile.click();
            } else {
                inpfile = document.createElement("input");
                $("#form_Hsc").append(inpfile);
                inpfile.setAttribute("id", "fileUploadId_Hsc");
                inpfile.setAttribute("name", "fileUploadId_Hsc")
                inpfile.setAttribute("type", "file");
                inpfile.style.display = "none";
                inpfile.addEventListener('change',showFileList, !1);
                inpfile.click && e.target != inpfile && inpfile.click();
            }
        };
        return fileOperation;
    })();
    var videoUpload = (function () {
        function videoUpload() {
        }
        var streamUpload = function (url) {
            var file = fileOperation.selectFile;
            var inittime = (new Date()).getTime();
            var ajax_option = {
                url: url,
                type: "post",
                dataType: "json",
                success: function (data) {
                    if (data.code == 0) {
                        uploadOption.finishCallback({ code: data.code, msg: data.message });
                        isNotUpload = false;
                    } else {
                        uploadOption.errorCallback({ code: data.code, msg: data.message });
                        isNotUpload = false;
                    }
                },
                error: function (data) {
                    isNotUpload = false;
                    uploadOption.errorCallback({ code: data.code, msg: data.message });
                },
                uploadProgress: function (event, loaded, total, percentComplete) {
                    var delttime = ((new Date()).getTime() - inittime) / 1000;
                    var uploadSize = parseInt(percentComplete + "") * file.size / 100;
                    var rate = uploadSize / delttime;
                    rate = rate / 1024;
                    rate = rate > 1024 ? (((rate / 1024 * 10) >> 0) / 10).toFixed(1) + "M/s" : (((rate * 10) >> 0) / 10).toFixed(1) + "K/s";
                    if (percentComplete == 100) {
                        percentComplete = 99;
                    }
                    uploadOption.uploadProgress(percentComplete + "%", rate);
                },
                timeout: 60000000
            }
            $("#form_Hsc").ajaxSubmit(ajax_option);
        };
        videoUpload.tryUpload = function () {
            var file = fileOperation.selectFile;
            $.ajax({
                url: uploadOption.initUrl + "?video_name=" + encodeURIComponent(file.name) + "&uploadtype=0&file_size=" + file.size,
                type: 'get',
                dataType: "json",
                success: function (data) {
                    var url = data.data.upload_url;
                    console.log(data)
                    localStorage.video_unique = data.data.video_unique
                    localStorage.video_id = data.data.video_id
                    streamUpload(url);
                }
            });
        };
        return videoUpload;
    })();
    return formUpload;
})();