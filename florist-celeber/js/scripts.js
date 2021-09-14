// Scripts// 
document.getElementById('mainNav').style.visibility = 'visible';
document.getElementById('mainNav').classList.remove('noJs');

//Checks and changes the liveOpeningHours
function liveOpeningHours(date) {
    const standardOpen = 'Öppnar idag kl 10';
    const standardOpenTomorrow = 'Öppnar imorgon kl 10';
    const openMonday = 'Öppnar på måndag kl 10';
    const openSoon = 'Öppnar snart';
    const closeSoon = 'Stänger snart';
    const open = 'Öppet just nu';
    const openTomorrowSaturday = 'Öppnar imorgon kl 12';
    const openSaturday = 'Öppnar idag kl 12'
    const day = date.getDay();
    const hours = date.getHours();
    const min = date.getMinutes();
    //The diffrent outcomes
    switch (day) {
        case 5: //Friday
            if (((hours == 9) && (min <= 30)) || (hours < 9)) {
                showUserLiveTime(standardOpen);
            } else if (hours >= 16) {
                showUserLiveTime(openTomorrowSaturday);
            } else if ((hours == 9) && (min > 30)) {
                showUserLiveTime(openSoon);
            } else if (hours == 15) {
                showUserLiveTime(closeSoon);
            } else {
                showUserLiveTime(open);
            }
            break;
        case 6: //Saturday
            if (((hours == 11) && (min <= 30)) || (hours < 11)) {
                showUserLiveTime(openSaturday);
            } else if (hours >= 15) {
                showUserLiveTime(openMonday);
            } else if ((hours == 11) && (min > 30)) {
                showUserLiveTime(openSoon);
            } else if (hours == 14) {
                showUserLiveTime(closeSoon);
            } else {
                showUserLiveTime(open);
            }
            break;
        case 0: //Sunday
            showUserLiveTime(standardOpenTomorrow);
            break;
        default :
            if (((hours == 9) && (min <= 30)) || (hours < 9)) {
                showUserLiveTime(standardOpen);
            } else if (hours >= 16) {
                showUserLiveTime(standardOpenTomorrow);
            } else if ((hours == 9) && (min > 30)) {
                showUserLiveTime(openSoon);
            } else if (hours == 15) {
                showUserLiveTime(closeSoon);
            } else {
                showUserLiveTime(open);
            }
    }
}
//Shows it to the user
function showUserLiveTime(msg) {
    let open = document.getElementById('liveOpeningHours');
    open.innerHTML = msg;
}
// Updates the live time every minute so that the info is accurate
setInterval(function() {
    liveOpeningHours(new Date());
}, 6000)

liveOpeningHours(new Date());

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
})