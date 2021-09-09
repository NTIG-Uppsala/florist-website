// Scripts// 

window.addEventListener('DOMContentLoaded', event => {

    document.getElementById('mainNav').style.visibility = 'visible';

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

    //
    function getDay() {
        let currentDay = new Date();
        let weekDay = currentDay.getDay();

        switch(weekDay) {
            case 0 :
                return getHours(currentDay, 'söndag');

            case 6 :
                return getHours(currentDay, 'lördag');

            default :
                return getHours(currentDay, 'vardag');
        }
    }

    //
    function getHours(date, day) {
       
        let dayHours = date.getHours();

        if(day == 'vardag') {
            if (dayHours >= 10 && dayHours < 16) {
                return 'öppet';
            }
            return 'stängt';
        }
        if(day == 'Lördag') {
            if (dayHours >= 12 && dayHours < 15) {
                return 'öppet';
            }
            return 'stängtLördag';
        }
        if(day == 'söndag') {
            return 'söndag';
        }
    }

    //
    function checkTime() {
        const status = getDay();
        if(status == 'öppet') {
            document.getElementById('liveOpeningHours').innerHTML = 'Vi har just nu öppet';
            return;
        }
        if(status == 'stängt') {
            document.getElementById('liveOpeningHours').innerHTML = ` Vi har just nu stängt, vi öppnar om ${timeLeft()}`;
            return;
        }
        if(status == 'stängtLördag') {
            document.getElementById('liveOpeningHours').innerHTML = ` Vi har just nu stängt, vi öppnar om ${timeLeft()}`;
            return;
        }
        document.getElementById('liveOpeningHours').innerHTML = 'Vi öppnar på måndag kl. 10:00';
        
    }

    //
    function timeLeft() {
        let currentDate = new Date();
        let dayHours = currentDate.getHours();
        let dayMinutes = currentDate.getMinutes();
        const status = getDay();
        //
        if(status == 'stängt') {
            if(dayHours < 10) {
                let leftHours = 10 - dayHours;
                let leftMinutes = leftHours*60 - dayMinutes;

                 let hoursLeft = leftMinutes/60;
                 let convertHours = Math.floor(hoursLeft);

                let minutesLeft = (hoursLeft - convertHours) * 60;
                let convertMinutes = Math.floor(minutesLeft);

                 return `${convertHours} timmar och ${convertMinutes} minuter`;
            }
            if (dayHours >= 16) {
                let leftHours = (23 - dayHours) + 11;
                let leftMinutes = leftHours*60 - dayMinutes;

                let hoursLeft = leftMinutes/60;
                let convertHours = Math.floor(hoursLeft);

                let minutesLeft = (hoursLeft - convertHours) * 60;
                let convertMinutes = Math.floor(minutesLeft);

                 return `${convertHours} timmar och ${convertMinutes} minuter`;
            }
        }
        //
        if(status == 'stängtLördag') {
            if(dayHours < 12) {
                let leftHours = 12 - dayHours;
                let leftMinutes = leftHours*60 - dayMinutes;

                 let hoursLeft = leftMinutes/60;
                 let convertHours = Math.floor(hoursLeft);

                let minutesLeft = (hoursLeft - convertHours) * 60;
                let convertMinutes = Math.floor(minutesLeft);

                 return `${convertHours} timmar och ${convertMinutes} minuter`;
            }
            if (dayHours >= 15) {
                let leftHours = (23 - dayHours) + 13;
                let leftMinutes = leftHours*60 - dayMinutes;

                let hoursLeft = leftMinutes/60;
                 let convertHours = Math.floor(hoursLeft);

                let minutesLeft = (hoursLeft - convertHours) * 60;
                let convertMinutes = Math.floor(minutesLeft);

                 return `${convertHours} timmar och ${convertMinutes} minuter`;
            }
        }     
    }
    checkTime();   
});
