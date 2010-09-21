var timeout    = 0;
var closetimer = 0;
var opendd     = null;

function dd_close() { 
   opendd.hide();
}

function dd_timer() {
  closetimer = window.setTimeout(dd_close, timeout);
}

function dd_canceltimer() {
  if(closetimer) {
     window.clearTimeout(closetimer);
     closetimer = null;
  }
}

$(document).ready(function(){
    $("dl.dropdown").hover(
        function() {
           dd_canceltimer();
	   if (opendd != null) { dd_close(); }
           opendd = $("dd", this).show();
        }, 
        function() {
	   dd_timer();
        } 
    );
});
