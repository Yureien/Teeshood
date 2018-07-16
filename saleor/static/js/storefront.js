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
    $('#navToggle').on('click', function() {
	let navbarMenu = $('.navbar__menu');
	if (navbarMenu.hasClass('d-md-none'))
	    navbarMenu.removeClass('d-md-none');
	else
	    navbarMenu.addClass('d-md-none');
    });

    $('.background').each(function() {
	let img_link = $(this).attr('data-src');
	if (img_link)
	    $(this).css('background-image', 'url("' + img_link + '")');
    });
});
