/* ============ Main JS ============ */

(function ($) {
    "use strict";

    var windowOn = $(window);

/*======================================
Preloader activation
========================================*/
    $(window).on('load', function (event) {
        $('#preloader').delay(1000).fadeOut(500);
    });


    $(".preloader-close").on("click", function () {
        $('#preloader').delay(0).fadeOut(500);
    })

    var headerArea = $(".sticky-active"),
        headerClone = headerArea.clone();

    function menuSticky(w) {
        if (w.matches) {
            $(".header").after('<div class="sticky-header-wrap"></div>');
            $(".sticky-header-wrap").html(headerClone);
            $(window).on("scroll", function () {
                var headerSelector = $(".sticky-header-wrap");
                var scroll = $(window).scrollTop();
                if (scroll >= 110) {
                    headerSelector.addClass("fixed");
                } else {
                    headerSelector.removeClass("fixed");
                }
            });
        }
    }

    var minWidth = window.matchMedia("(min-width: 993px)");
    if ($(".header").hasClass("sticky-active")) {
        menuSticky(minWidth);
    } else {
        windowOn.on("scroll", function () {
            var scroll = $(window).scrollTop();
            if (scroll < 100) {
                $(".header").removeClass("header__sticky");
            } else {
                $(".header").addClass("header__sticky");
            }
        });
    }

    //Mobile Menu Js
    $(".mobile-menu-items").meanmenu({
        meanMenuContainer: ".side-menu-wrap",
        meanScreenWidth: "991",
        meanMenuCloseSize: "30px",
        meanRemoveAttrs: true,
        meanExpand: ['<i class="fa-solid fa-caret-down"></i>'],
    });

    // Mobile Sidemenu
    $(".mobile-side-menu-toggle").on("click", function () {
        $(".mobile-side-menu, .mobile-side-menu-overlay").toggleClass("is-open");
    });

    $(".mobile-side-menu-close, .mobile-side-menu-overlay").on("click", function () {
        $(".mobile-side-menu, .mobile-side-menu-overlay").removeClass("is-open");
    });

    // Popup Search Box
    $(function () {
        $("#popup-search-box").removeClass("toggled");

        $(".dl-search-icon").on("click", function (e) {
            e.stopPropagation();
            $("#popup-search-box").toggleClass("toggled");
            $("#popup-search").focus();
        });

        $("#popup-search-box input").on("click", function (e) {
            e.stopPropagation();
        });

        $("#popup-search-box, body").on("click", function () {
            $("#popup-search-box").removeClass("toggled");
        });
    });

    // Popup Sidebox
    function sideBox() {
        $("body").removeClass("open-sidebar");
        $(document).on("click", ".sidebar-trigger", function (e) {
            e.preventDefault();
            $("body").toggleClass("open-sidebar");
        });
        $(document).on("click", ".sidebar-trigger.close, #sidebar-overlay", function (e) {
            e.preventDefault();
            $("body.open-sidebar").removeClass("open-sidebar");
        });
    }

    sideBox();

    // Venobox Video
    new VenoBox({
        selector: ".video-popup, .img-popup",
        bgcolor: "transparent",
        numeration: true,
        infinigall: true,
        spinner: "plane",
    });

    // Data Background
    $("[data-background").each(function () {
        $(this).css("background-image", "url( " + $(this).attr("data-background") + "  )");
    });

    // Custom Cursor
        $('body').append('<div class="mt-cursor"></div>');
        var cursor = $('.mt-cursor'),
            linksCursor = $('a, .swiper-nav, button, .cursor-effect'),
            crossCursor = $('.cross-cursor');

        $(window).on('mousemove', function (e) {
            cursor.css({
                'transform': 'translate(' + (e.clientX - 15) + 'px,' + (e.clientY - 15) + 'px)',
                'visibility': 'inherit'
            });
        });

    /* Odometer */
    $(".odometer").waypoint(
        function () {
            var odo = $(".odometer");
            odo.each(function () {
                var countNumber = $(this).attr("data-count");
                $(this).html(countNumber);
            });
        },
        {
            offset: "80%",
            triggerOnce: true,
        }
    );

    // Wow JS Active
    new WOW().init();

    // Isotop
    $(".filter-items").imagesLoaded(function () {
        // Add isotope click function
        $(".project-filter li").on("click", function () {
            $(".project-filter li").removeClass("active");
            $(this).addClass("active");

            var selector = $(this).attr("data-filter");
            $(".filter-items").isotope({
                filter: selector,
                isOriginLeft: false,
                animationOptions: {
                    duration: 750,
                    easing: "linear",
                    queue: false,
                },
            });
            return false;
        });

        $(".filter-items").isotope({
            itemSelector: ".single-item",
            layoutMode: "fitRows",
            fitRows: {
                gutter: 0,
            },
        });
    });

    // Sponsor Carousel
    var swiperSponsor = new Swiper(".sponsor-carousel", {
        slidesPerView: 45,
        spaceBetween: 50,
        slidesPerGroup: 1,
        loop: true,
        autoplay: true,
        grabcursor: true,
        speed: 400,
        breakpoints: {
            320: {
                slidesPerView: 2,
                slidesPerGroup: 1,
                spaceBetween: 25,
            },
            767: {
                slidesPerView: 4,
                slidesPerGroup: 1,
                spaceBetween: 30,
            },
            1024: {
                slidesPerView: 5,
                slidesPerGroup: 1,
            },
        },
    });

    // Testimonial Carousel
    var testimonialThumb = new Swiper(".thumb-carousel", {
        slidesPerView: 1,
        slidesPerGroup: 1,
        spaceBetween: 0,
        loop: true,
        autoplay: true,
        speed: 600,
    });
    var testimonials = new Swiper(".content-carousel", {
        slidesPerView: 1,
        slidesPerGroup: 1,
        spaceBetween: 0,
        loop: true,
        autoplay: true,
        speed: 600,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        thumbs: {
            swiper: testimonialThumb,
        },
    });

    // Testi Carousel
    var swiperTesti = new Swiper(".testi-carousel", {
        slidesPerView: 4,
        spaceBetween: 30,
        slidesPerGroup: 1,
        loop: true,
        autoplay: true,
        grabcursor: true,
        speed: 600,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                slidesPerGroup: 1,
                spaceBetween: 25,
            },
            767: {
                slidesPerView: 2,
                slidesPerGroup: 1,
                spaceBetween: 30,
            },
            1024: {
                slidesPerView: 3,
                slidesPerGroup: 1,
            },
            1200: {
                slidesPerView: 4,
                slidesPerGroup: 1,
            },
        },
    });

    // Testi Carousel 2
    var swiperTesti = new Swiper(".testi-carousel-2", {
        slidesPerView: 3,
        spaceBetween: 30,
        slidesPerGroup: 1,
        loop: true,
        autoplay: {
            reverseDirection: true,
        },
        grabcursor: true,
        speed: 600,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                slidesPerGroup: 1,
                spaceBetween: 25,
            },
            767: {
                slidesPerView: 2,
                slidesPerGroup: 1,
                spaceBetween: 30,
            },
            1024: {
                slidesPerView: 3,
                slidesPerGroup: 1,
            },
        },
    });

    // Blog Carousel
    var swiperBlog = new Swiper(".blog-carousel", {
        slidesPerView: 3,
        spaceBetween: 30,
        slidesPerGroup: 1,
        loop: true,
        autoplay: true,
        grabcursor: true,
        speed: 600,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                slidesPerGroup: 1,
                spaceBetween: 25,
            },
            767: {
                slidesPerView: 2,
                slidesPerGroup: 1,
                spaceBetween: 30,
            },
            1024: {
                slidesPerView: 3,
                slidesPerGroup: 1,
            },
        },
    });

    // Team Carousel
    var swiperTeam = new Swiper(".team-carousel", {
        slidesPerView: 3,
        spaceBetween: 25,
        slidesPerGroup: 1,
        loop: true,
        autoplay: true,
        grabcursor: true,
        speed: 600,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                slidesPerGroup: 1,
                spaceBetween: 25,
            },
            767: {
                slidesPerView: 2,
                slidesPerGroup: 1,
                spaceBetween: 30,
            },
            1024: {
                slidesPerView: 3,
                slidesPerGroup: 1,
            },
        },
    });

    // Team Carousel
    var swiperTeam = new Swiper(".team-carousel-2", {
        slidesPerView: 4,
        spaceBetween: 25,
        slidesPerGroup: 1,
        loop: true,
        autoplay: true,
        grabcursor: true,
        speed: 600,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                slidesPerGroup: 1,
                spaceBetween: 25,
            },
            767: {
                slidesPerView: 3,
                slidesPerGroup: 1,
                spaceBetween: 30,
            },
            1024: {
                slidesPerView: 4,
                slidesPerGroup: 1,
            },
        },
    });

    // Project Carousel
    var swiperProject = new Swiper(".project-carousel", {
        slidesPerView: 4,
        spaceBetween: 25,
        slidesPerGroup: 1,
        loop: true,
        autoplay: true,
        grabcursor: true,
        speed: 600,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                slidesPerGroup: 1,
                spaceBetween: 25,
            },
            767: {
                slidesPerView: 2,
                slidesPerGroup: 1,
                spaceBetween: 30,
            },
            1024: {
                slidesPerView: 4,
                slidesPerGroup: 1,
            },
        },
    });

    // Pricing Carousel
    var swiperPricing = new Swiper(".pricing-carousel", {
        slidesPerView: 4,
        spaceBetween: 25,
        slidesPerGroup: 1,
        loop: true,
        autoplay: true,
        grabcursor: true,
        speed: 600,
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                slidesPerGroup: 1,
                spaceBetween: 25,
            },
            767: {
                slidesPerView: 2,
                slidesPerGroup: 1,
                spaceBetween: 30,
            },
            1024: {
                slidesPerView: 4,
                slidesPerGroup: 1,
            },
        },
    });
    // Scroll To Top
    var scrollTop = $("#scrollup");
    $(window).on('scroll', function() {
        var topPos = $(this).scrollTop();
        if (topPos > 100) {
            $('#scrollup').removeClass('hide');
            $('#scrollup').addClass('show');

        } else {
            $('#scrollup').removeClass('show');
            $('#scrollup').addClass('hide');
        }
    });

    $(scrollTop).on("click", function() {
        $('html, body').animate({
            scrollTop: 0
        },0);
        return false;
    });
})(jQuery);
