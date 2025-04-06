$(document).ready(function() {
    let currentSlide = 0;
    const totalSlides = $('.slide').length;
    const $slider = $('.slider');
    const $dots = $('.slider-dots');

    for (let i = 0; i < totalSlides; i++) {
        $dots.append(`<div class="dot ${i === 0 ? 'active' : ''}"></div>`);
    }

    function updateSlider() {
        $slider.css('transform', `translateX(-${currentSlide * 33.333}%)`);
        $('.dot').removeClass('active').eq(currentSlide).addClass('active');
    }

    $('.next').click(function() {
        currentSlide = (currentSlide + 1) % totalSlides;
        updateSlider();
    });

    $('.prev').click(function() {
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
        updateSlider();
    });

    $('.dot').click(function() {
        currentSlide = $(this).index();
        updateSlider();
    });

    setInterval(function() {
        currentSlide = (currentSlide + 1) % totalSlides;
        updateSlider();
    }, 10000);

    $('nav a').on('click', function(e) {
        const href = $(this).attr('href');

        if (href.startsWith('#')) {
            e.preventDefault();
            $('html, body').animate({
                scrollTop: $(href).offset().top - 80
            }, 1000, 'swing');
        }
    });

    $('#search button').on('click', function(e) {
        e.preventDefault();
        window.location.href = 'flights.html';
    });

    $('#popular-destinations td').hover(
        function() {
            $(this).css('transform', 'scale(1.05)');
            $(this).css('transition', 'transform 0.3s ease');
        },
        function() {
            $(this).css('transform', 'scale(1)');
        }
    );

    $('#search button').hover(
        function() {
            $(this).css('background-color', '#0056b3');
        },
        function() {
            $(this).css('background-color', '#007bff');
        }
    );
}); 