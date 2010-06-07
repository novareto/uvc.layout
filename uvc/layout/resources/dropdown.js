$(document).ready(function(){
    $("dl.dropdown").hover(
        function() {
           $("dd", this).show();
           $(this).addClass("unfolding");
        }, 
        function() {
           $("dd", this).hide();
           $(this).removeClass("unfolding");
        } 
    );
});
