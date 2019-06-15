$(document).ready(function(){

  console.log("cool");

  // Slider
  $('.slider').slider();

  //Wow effect
  new WOW().init();
 

  //smooth scroll
    $('a[href*="#"]')
        // Remove links that don't actually link to anything
        .not('[href="#"]')
        .not('[href="#0"]')
        .click(function(event) {
          // On-page links
          if (
            location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
            && 
            location.hostname == this.hostname
          ) {
            // Figure out element to scroll to
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            // Does a scroll target exist?
            if (target.length) {
              // Only prevent default if animation is actually gonna happen
              event.preventDefault();
              $('html, body').animate({
                scrollTop: target.offset().top
              }, 2000, function() {
                // Callback after animation
                // Must change focus!
                var $target = $(target);
                $target.focus();
                if ($target.is(":focus")) { // Checking if the target was focused
                  return false;
                } else {
                  $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
                  $target.focus(); // Set focus again
                };
              });
            }
          }
        });



   // people say
  $(function(){
    
    $('.textSlider .slidesParttext:gt(0)').hide();
    setInterval(function(){
      $('.textSlider :first-child').fadeOut(2000).next('.slidesParttext').fadeIn(2000)
      .end().appendTo('.textSlider');
  }, 7000);
    
  });   
       
});


$(document).scroll(function() {
	//Main Menu
           if($(window).scrollTop() > 50){

            $("section#menu-bar").css("background","rgba(59, 190, 179, 0.92)");
            $("section#menu-bar").css("height","80px");
            $(".navbar").css("padding-top","22px");
            $("a#side-menu-button").css("margin-top","-30px");
             
 
           }else if($(window).scrollTop() < 50){

            $("section#menu-bar").css("background","");
            $("section#menu-bar").css("height","");
            $(".navbar").css("padding-top","");
            $("a#side-menu-button").css("margin-top","");
  
           }
       
    });