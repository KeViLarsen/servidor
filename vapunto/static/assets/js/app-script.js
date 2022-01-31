
$(function() {
    "use strict";
     
	 
//sidebar menu js
$.sidebarMenu($('.sidebar-menu'));

// === toggle-menu js
$(".toggle-menu").on("click", function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });	 
	   
// === sidebar menu activation js

$(function() {
        for (var i = window.location, o = $(".sidebar-menu a").filter(function() {
            return this.href == i;
        }).addClass("active").parent().addClass("active"); ;) {
            if (!o.is("li")) break;
            o = o.parent().addClass("in").parent().addClass("active");
        }
    }), 	   
	   

/* Top Header */

$(document).ready(function(){ 
    $(window).on("scroll", function(){ 
        if ($(this).scrollTop() > 60) { 
            $('.topbar-nav .navbar').addClass('bg-dark'); 
        } else { 
            $('.topbar-nav .navbar').removeClass('bg-dark'); 
        } 
    });

 });


/* Back To Top */

$(document).ready(function(){ 
    $(window).on("scroll", function(){ 
        if ($(this).scrollTop() > 300) { 
            $('.back-to-top').fadeIn(); 
        } else { 
            $('.back-to-top').fadeOut(); 
        } 
    }); 

    $('.back-to-top').on("click", function(){ 
        $("html, body").animate({ scrollTop: 0 }, 600); 
        return false; 
    }); 
});	   
	    
   
$(function () {
  $('[data-toggle="popover"]').popover()
})


$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})


	 // theme setting
	 $(".switcher-icon").on("click", function(e) {
        e.preventDefault();
        $(".right-sidebar").toggleClass("right-toggled");
    });
	
	$('#theme1').click(theme1);
    $('#theme2').click(theme2);
    $('#theme3').click(theme3);
    $('#theme4').click(theme4);
    $('#theme5').click(theme5);
    $('#theme6').click(theme6);
    $('#theme7').click(theme7);
    $('#theme8').click(theme8);
    $('#theme9').click(theme9);
    $('#theme10').click(theme10);
    $('#theme11').click(theme11);
    $('#theme12').click(theme12);
    $('#theme13').click(theme13);
    $('#theme14').click(theme14);
    $('#theme15').click(theme15);

    window.onload = function recordarSeleccionTema() {
      switch(localStorage.getItem('1')) {
        case '1': theme1(); break;
        case '2': theme2(); break;
        case '3': theme3(); break;
        case '4': theme4(); break;
        case '5': theme5(); break;
        case '6': theme6(); break;
        case '7': theme7(); break;
        case '8': theme8(); break;
        case '9': theme9(); break;
        case '10': theme10(); break;
        case '11': theme11(); break;
        case '12': theme12(); break;
        case '13': theme13(); break;
        case '14': theme14(); break;
        case '15': theme15(); break;
      }
    }

    function grabarTema(nro) {
      
      return localStorage.setItem('1', nro)
    }

    function theme1() {
      $('body').attr('class', 'bg-theme bg-theme1');
      grabarTema(1)
    }

    function theme2() {
      $('body').attr('class', 'bg-theme bg-theme2');
      grabarTema(2)
    }

    function theme3() {
      $('body').attr('class', 'bg-theme bg-theme3');
      grabarTema(3)
    }

    function theme4() {
      $('body').attr('class', 'bg-theme bg-theme4');
      grabarTema(4)
    }
	
	function theme5() {
      $('body').attr('class', 'bg-theme bg-theme5');
      grabarTema(5)
    }
	
	function theme6() {
      $('body').attr('class', 'bg-theme bg-theme6');
      grabarTema(6)
    }

    function theme7() {
      $('body').attr('class', 'bg-theme bg-theme7');
      grabarTema(7)
    }

    function theme8() {
      $('body').attr('class', 'bg-theme bg-theme8');
      grabarTema(8)
    }

    function theme9() {
      $('body').attr('class', 'bg-theme bg-theme9');
      grabarTema(9)
    }

    function theme10() {
      $('body').attr('class', 'bg-theme bg-theme10');
      grabarTema(10)
    }

    function theme11() {
      $('body').attr('class', 'bg-theme bg-theme11');
      grabarTema(11)
    }

    function theme12() {
      $('body').attr('class', 'bg-theme bg-theme12');
      grabarTema(12)
    }
	
	function theme13() {
      $('body').attr('class', 'bg-theme bg-theme13');
      grabarTema(13)
    }
	
	function theme14() {
      $('body').attr('class', 'bg-theme bg-theme14');
      grabarTema(14)
    }
	
	function theme15() {
      $('body').attr('class', 'bg-theme bg-theme15');
      grabarTema(15)
    }




});