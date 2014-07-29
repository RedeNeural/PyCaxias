$('.navbar a').on('click', function() {
     $('nav li.active').removeClass('active');
     $(this).parent().addClass('active');
});

