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

    
      var typed = new Typed('#welcome-title', {
        strings: [
        'Welcome',
        'My Project'
        ],
        typeSpeed: 100,
        backSpeed: 100,
        backDelay: 1000,
        loop: true
      });

      var typed2 = new Typed('#services-title', {
        strings: ['Services','Get Here'],
        typeSpeed: 100,
        backSpeed: 100,
        backDelay: 1000,
        loop: true
      });

      var typed3 = new Typed('#carpetServ-text-title', {
        strings: ['CarpetServ','Get Here'],
        typeSpeed: 100,
        backSpeed: 100,
        backDelay: 1000,
        loop: true
      });

      var typed4 = new Typed('.steps-class', {
        strings: ['Steps','Get Here'],
        typeSpeed: 100,
        backSpeed: 100,
        backDelay: 1000,
        loop: true
      });

      var typed5 = new Typed('#price-title-list', {
        strings: ['Price'],
        typeSpeed: 100,
        backSpeed: 100,
        backDelay: 1000,
        loop: true
      });

      var typed5 = new Typed('#blog-title-list', {
        strings: ['Blog'],
        typeSpeed: 100,
        backSpeed: 100,
        backDelay: 1000,
        loop: true
      });

     // Hide the tuype cursor 
     $('.typed-cursor').hide();


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