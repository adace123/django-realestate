const mainNav = document.querySelector('div#main-nav');

window.addEventListener('scroll', (e) => {
    if (!mainNav.classList.contains('fixed-top') && mainNav.scrollHeight * 2 <= window.scrollY) {
        mainNav.classList.add('fixed-top');
    } else if (mainNav.scrollHeight * 2 > window.scrollY && mainNav.classList.contains('fixed-top')) {
        mainNav.classList.remove('fixed-top');
    }
});