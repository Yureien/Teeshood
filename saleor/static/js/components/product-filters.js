$('.filters-menu').on('click', (e) => {
  const menuContainer = $('.filters-menu__body');
  if (menuContainer.hasClass('d-none')) {
    menuContainer.removeClass('d-none');
  } else {
    menuContainer.addClass('d-none');
  }
});

$('.filter-section__header').on('click', (event) => {
  const $target = $(event.currentTarget).parent();
  if ($target.attr('aria-expanded') === 'true') {
    $target.attr('aria-expanded', 'false').addClass('filter-section--closed');
  } else {
    $target.attr('aria-expanded', 'true').removeClass('filter-section--closed');
  }
});

$('.filters-toggle').on('click', () => {
  $('.filters-menu__body').toggleClass('d-none');
});

$('#pincode-checker').submit(function(e) {
	let opts = $(this).serializeArray();
	let url = opts[1]['value'].replace('0', opts[0]['value']);
	$.getJSON(url, function(data) {
		if (data['available']) {
			$('#pincode-validator span').removeClass('text-danger');
			$('#pincode-validator span').addClass('text-success');
			$('#pincode-validator span').text("Product available in pincode.");
		} else {
			$('#pincode-validator span').removeClass('text-success');
			$('#pincode-validator span').addClass('text-danger');
			$('#pincode-validator span').text("Product not available in pincode.");
		}
	});
	return false;
});
