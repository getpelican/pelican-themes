$(function(){
    var d_top=$('#go-top');
    document.onscroll=function(){
        var scrTop=(document.body.scrollTop||document.documentElement.scrollTop);
        var d ={queue: false, duration: 500};
        if(scrTop>500){
            d_top.show();
        }else{
            d_top.hide();
            }
    $('#go-top-i').click(function(){
    $("html,body").animate({scrollTop: '0px'},d);
});
}});