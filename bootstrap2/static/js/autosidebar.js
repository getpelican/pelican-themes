jQuery.fn.justtext = function() {
    return $(this).clone()
            .children()
            .remove()
            .end()
            .text();
 
};

$(document).ready(function(){    
   $("h1").each(function(){
        $("#sidebar").append(
            "<h4><a href='#'>"+$(this).justtext()+"</a></h4>"
        );
        ul = $("<ul>");
        $("h2",$(this).parent().parent()).each(function(){
            ul.append(
            "<li><a href='#'>"+$(this).justtext()+"</a></li>"
            );
            subul = $("<ul>");
            $("h3",$(this).parent()).each(function(){
                subul.append(
                "<li><a href='#'>"+$(this).justtext()+"</a></li>"
                );
            });
            ul.append(subul);
        });
        $("#sidebar").append(ul);
   });
});