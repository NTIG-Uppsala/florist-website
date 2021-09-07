// Scripts// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });
    
    const navbarMenu = document.getElementById('navbarMenu');
    const navbarCollapse = document.getElementById('navbarResponsive');
    navbarMenu.onclick = function(){
        if (navbarCollapse.classList.contains('show')) {
            navbarToggler.classList.remove('focus')
            navbarCollapse.classList.remove('show')
            return
        }
        navbarToggler.classList.add('focus')
        navbarCollapse.classList.add('show')
    }

    const mastheadContainer = document.getElementById('mastheadContainer');
    if(window.innerHeight <= 650) {
        mastheadContainer.scrollIntoView();
    }
    
});
