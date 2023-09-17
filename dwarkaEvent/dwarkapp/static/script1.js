let menu = document.querySelector("#menu-bars");
let navbar = document.querySelector(".navbar");

menu.onclick = () => {
  menu.classList.toggle("fa-time");
  navbar.classList.toggle("active");
};

window.onclick = () => {
  menu.classList.toggle("fa-time");
  navbar.classList.toggle("active");
};

var homeSwiper = new Swiper(".home-slider", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  loop: true,
  coverflowEffect: {
    rotate: 50,
    stretch: 0,
    depth: 100,
    modifier: 2,
    slideShadows: true,
  },
  autoplay: {
    delay: 2000,
    disableOnInteraction: false,
  },
});

var reviewSwiper = new Swiper(".review-slider", {
  slidesPerView: 1,
  grabCursor: true,
  loop: true,
  spaceBetween: 10,
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    700: {
      slidesPerView: 2,
    },
    1050: {
      slidesPerView: 3,
    },
  },
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
  },
});
homeSwiper.slideTo(2);
