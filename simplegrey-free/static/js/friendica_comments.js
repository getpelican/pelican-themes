var article = document.getElementsByTagName("article")[0].innerHTML;
var article_name= article.substring(article.indexOf('<p>')+3,article.indexOf('<p>')+33);
var search = friendica_domain + "/search?search=" + article_name.replace(/ /gi,'+');
var http, http2 = null;
var ergebnis = "";

http = new XMLHttpRequest();
if (http !== null) {
   http.open("GET", search, true);
   http.onreadystatechange = SearchFriendica;
   http.send(null);
}

function SearchFriendica() {
   if (http.readyState == 4 && http.status==200) {
    var SearchResult= http.responseText;
    var start = SearchResult.indexOf('wall-item-bottom');
    var start2 = SearchResult.indexOf('a href=\'http',start);
    var end = SearchResult.indexOf('id',start);
    ergebnis = SearchResult.substring(start2+8,end-2);
   }

http2 = new XMLHttpRequest(); 
    if (http2 !== null) {
   http2.open("GET", ergebnis, true);
   http2.onreadystatechange = SearchComments;
   http2.send(null);
}   

function SearchComments() {
   if (http.readyState == 4 && http.status == 200) {
    var CommentsResult = http2.responseText;
    var ergebnisse = ("<div class='comment'> <a href='" + ergebnis +"'> Comments</a> powered by Friendica</div>" );
    var arr = new Array();
    arr = CommentsResult.split("wall-item-container comment");
    for (i=1;i<arr.length;i++){
        var photo = arr[i].substring(arr[i].indexOf('<a href'),arr[i].indexOf('</a>')+4);
        var start = arr[i].indexOf('<div class=\"wall-item-actions-author\">');
        var end = arr[i].indexOf('<div class=\"wall-item-bottom\">',start);
        var comment = arr[i].substring(start,end-1);
        ergebnisse = ergebnisse + '<div class=\"comment-container\">' + photo + comment + '</div>';
       }
    document.getElementById("comments").innerHTML = ergebnisse;
    }
}
}