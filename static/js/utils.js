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
