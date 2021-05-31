jQuery(document).ready(function($){
	// browser window scroll (in pixels) after which the "menu" link is shown
	var offset = 300;

	var navigationContainer = $('#cd-nav'),
		mainNavigation = navigationContainer.find('#cd-main-nav ul');

	//hide or show the "menu" link
	checkMenu();


	//open or close the menu clicking on the bottom "menu" link
	$('.cd-nav-trigger').on('click', function(){
		$(this).toggleClass('menu-is-open');		
		mainNavigation.off('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend').toggleClass('is-visible');

	});

	function checkMenu() {
        if (mainNavigation.hasClass('is-visible') && !$('html').hasClass('no-csstransitions')) {
            //close the menu with animation
            mainNavigation.addClass('is-hidden').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function () {
                //wait for the menu to be closed and do the rest
                mainNavigation.removeClass('is-visible is-hidden has-transitions');
               //navigationContainer.removeClass('is-fixed');
                $('.cd-nav-trigger').removeClass('menu-is-open');
            });
            //check if the menu is open when scrolling up - fallback if transitions are not supported
        } else if (mainNavigation.hasClass('is-visible') && $('html').hasClass('no-csstransitions')) {
            mainNavigation.removeClass('is-visible has-transitions');
           // navigationContainer.removeClass('is-fixed');
            $('.cd-nav-trigger').removeClass('menu-is-open');
            //scrolling up with menu closed
        } else {
           // navigationContainer.removeClass('is-fixed');
            mainNavigation.removeClass('has-transitions');
        }
	}
});