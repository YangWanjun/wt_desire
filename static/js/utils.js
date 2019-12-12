Utils = function() {
};

Utils.prototype.loading = function() {
    $('body').append(
        '<div class="loading">' +
            '<div class="preloader-wrapper big active">' +
                '<div class="spinner-layer spinner-blue-only">' +
                    '<div class="circle-clipper left"> ' +
                        '<div class="circle"></div>' +
                    '</div>' +
                    '<div class="gap-patch">' +
                        '<div class="circle"></div>' +
                    '</div>' +
                    '<div class="circle-clipper right">' +
                        '<div class="circle"></div>' +
                    '</div>' +
                '</div>' +
            '</div>' +
        '</div>'
    );
    $("html").css("overflow", "hidden");
    $("html").css("padding-right", "17px");
};

/**
 * ローディング画面を消す。
 */
Utils.prototype.loaded = function() {
    var loadings = $("body div.loading");
    var overlay = $("div.modal-overlay");
    if (loadings.length == 1 && overlay.length === 0) {
        loadings.remove();
        $("html").css("overflow", "");
        $("html").css("padding-right", "");
    } else if (loadings.length > 0) {
        // 複数のloading画面が存在する場合、１つだけ削除します。
        loadings.eq(0).remove();
    }
};

/**
  * 日付をフォーマットする
  * @param {Date} date
  * @param {String} format
  */
Utils.prototype.formatDate = function (date, format) {
    if (!format) {
        format = 'YYYY-MM-DD hh:mm:ss.SSS';
    }
    if (!date) {
      return null;
    } else if (typeof date === "string") {
        date = new Date(date);
    }
    format = format.replace(/YYYY/g, date.getFullYear());
    format = format.replace(/MM/g, ('0' + (date.getMonth() + 1)).slice(-2));
    format = format.replace(/DD/g, ('0' + date.getDate()).slice(-2));
    format = format.replace(/hh/g, ('0' + date.getHours()).slice(-2));
    format = format.replace(/mm/g, ('0' + date.getMinutes()).slice(-2));
    format = format.replace(/ss/g, ('0' + date.getSeconds()).slice(-2));
    if (format.match(/S/g)) {
        var milliSeconds = ('00' + date.getMilliseconds()).slice(-3);
        var length = format.match(/S/g).length;
        for (var i = 0; i < length; i++) format = format.replace(/S/, milliSeconds.substring(i, i + 1));
    }
    return format;
};
