$(".topfilms").owlCarousel({
    loop: true,
    autoplay: true,
    autoplayTimeout: 3000,
    responsive: {
      0:{
        items: 2,
      },
      400:{
        items: 2,
      },
      600:{
        items: 3,
      },
      800:{
        items: 4,
      },
      1000:{
        items: 6,
      }
    }
});
$(".topserials").owlCarousel({
loop: true,
autoplay: true,
autoplayTimeout: 2000,
responsive: {
0:{
  items: 2,
},
400:{
  items: 2,
},
600:{
  items: 3,
},
800:{
  items: 4,
},
1000:{
  items: 6,
}
}
});