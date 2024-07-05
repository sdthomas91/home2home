// Back to top button

// Show or hide the back to top button
$(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
        $('.btt-btn').fadeIn();
    } else {
        $('.btt-btn').fadeOut();
    }
});

// Scroll to the top when the button is clicked
$('.btt-btn').click(function() {
    $('html, body').animate({ scrollTop: 0 }, 'slow');
    return false;
});