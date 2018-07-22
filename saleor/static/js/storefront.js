import 'jquery';
import 'jquery.cookie';
import 'bootstrap';

import '../scss/storefront.scss';

import './components/navbar';
import './components/cart';
import './components/sorter';
import './components/variant-picker';
import './components/language-picker';
import './components/footer';
import './components/product-filters';
import './components/address-form';
import './components/password-input';
import './components/styleguide';
import './components/misc';

$('document').ready(function () {
    var doMenuAnim = true;
    let navbarMenu = $('.navbar__menu');
    if ($(window).width() >= 768) {
	doMenuAnim = true;
	navbarMenu.removeClass('d-block');
	navbarMenu.removeClass('d-md-none');
	if (navbarMenu.hasClass('menu-hidden')) navbarMenu.hide();
	else navbarMenu.show();
    } else {
	doMenuAnim = false;
	navbarMenu.addClass('d-block');
	navbarMenu.addClass('d-md-none');
    }
    $(window).on('resize', function() {
	let navbarMenu = $('.navbar__menu');
	if ($(window).width() >= 768) {
	    doMenuAnim = true;
	    navbarMenu.removeClass('d-block');
	    navbarMenu.removeClass('d-md-none');
	    if (navbarMenu.hasClass('menu-hidden')) navbarMenu.hide();
	    else navbarMenu.show();
	} else {
	    doMenuAnim = false;
	    navbarMenu.addClass('d-block');
	    navbarMenu.addClass('d-md-none');
	}
    });
    if (doMenuAnim) {
	$('#navToggle').on('click', function() {
	    let navbarMenu = $('.navbar__menu');
	    if (navbarMenu.hasClass('menu-hidden')) {
		navbarMenu.removeClass('menu-hidden');
		navbarMenu.slideDown();
	    }
	    else {
		navbarMenu.slideUp();
		navbarMenu.addClass('menu-hidden');
	    }
	});
    }

    $('.background').each(function() {
	let img_link = $(this).attr('data-src');
	if (img_link)
	    $(this).css('background-image', 'url("' + img_link + '")');
    });
});
