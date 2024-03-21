/* Picture Carousel */

$('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    autoplay: true,
    autoplayTimeout: 4000,
    responsive:{
    0:{
    items:1
    },
    600:{
    items:3
    },
    1000:{
    items:5
    }
    }
    })

/* Navigation bar functions */

function showSidebar() {
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'flex'
    }

function removeSidebar() {
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'none'
    }

/* Scroll to the top of page - menu page */

function scrollToTop() {
    window.scrollTo(0, 0);
}