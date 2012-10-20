/*
Set of functions common for other script in this theme
*/
function adjustSelection(e) {
    $(".main-nav").children("li").removeClass("sel"), $("#" + e).parent().addClass("sel")
}

function numberWithCommas(e) {
    return e.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")
}

function prepare_link(event, element) {
    event.preventDefault(), event.stopPropagation();
    return $.url(element.href.replace("/#!",""));
}

function remove_modal() {
    $("div[id$=-profile]").modal('hide');
    $(".modal-backdrop").modal('hide');
}

var spin_opts = {
    lines: 9,
    length: 5,
    width: 2,
    radius: 4,
    rotate: 9,
    color: "#4c4c4c",
    speed: 1.5,
    trail: 40,
    shadow: !1,
    hwaccel: !1,
    className: "spinner",
    zIndex: 2e9
}

var isMobileView = !1
if (typeof window.matchMedia != "undefined") {
    var mediaQuery = window.matchMedia("(max-width:799px)");
    mediaQuery.matches && (isMobileView = !0)
}
$(function () {
    $("#mobile-nav-btn")
        .click(function () {
        $(".main-section")
            .toggleClass("nav-opened")
    })
});
