(function () {
  ("use strict");

  lozad(".lazyload").observe();

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim();
    if (all) {
      return [...document.querySelectorAll(el)];
    } else {
      return document.querySelector(el);
    }
  };

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all);
    if (selectEl) {
      if (all) {
        selectEl.forEach((e) => e.addEventListener(type, listener));
      } else {
        selectEl.addEventListener(type, listener);
      }
    }
  };

  /**
   * Easy on scroll event listener
   */
  const onscroll = (el, listener) => {
    el.addEventListener("scroll", listener);
  };

  // let stickyTop = select(".sticky-top");
  // console.log(stickyTop);
  // if (stickyTop) {
  //   const stickyTopScrolled = () => {
  //     if (window.scrollY > 300) {
  //       stickyTop.classList.add("shadow-sm");
  //       stickyTop.style.setProperty("top", "0px");
  //     } else {
  //       stickyTop.classList.remove("shadow-sm");
  //       stickyTop.style.setProperty("top", "-100px");
  //     }
  //   };
  //   window.addEventListener("load", stickyTopScrolled);
  //   onscroll(document, stickyTopScrolled);
  // }

  /**
   * Navbar links active state on scroll
   */
  // let navbarlinks = select("#navbar .scrollto", true);
  // const navbarlinksActive = () => {
  //   let position = window.scrollY + 200;
  //   navbarlinks.forEach((navbarlink) => {
  //     if (!navbarlink.hash) return;
  //     let section = select(navbarlink.hash);
  //     if (!section) return;
  //     if (
  //       position >= section.offsetTop &&
  //       position <= section.offsetTop + section.offsetHeight
  //     ) {
  //       navbarlink.classList.add("active");
  //     } else {
  //       navbarlink.classList.remove("active");
  //     }
  //   });
  // };
  // window.addEventListener("load", navbarlinksActive);
  // onscroll(document, navbarlinksActive);

  /**
   * Scrolls to an element with header offset
   */
  // const scrollto = (el) => {
  //   let header = select("#header");
  //   let offset = header.offsetHeight;

  //   let elementPos = select(el).offsetTop;
  //   window.scrollTo({
  //     top: elementPos - offset,
  //     behavior: "smooth",
  //   });
  // };

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  // let selectHeader = select("#header");
  // if (selectHeader) {
  //   const headerScrolled = () => {
  //     if (window.scrollY > 100) {
  //       selectHeader.classList.add("header-scrolled");
  //     } else {
  //       selectHeader.classList.remove("header-scrolled");
  //     }
  //   };
  //   window.addEventListener("load", headerScrolled);
  //   onscroll(document, headerScrolled);
  // }

  /**
   * Back to top button
   */
  let backtotop = select(".back-to-top");
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add("active");
      } else {
        backtotop.classList.remove("active");
      }
    };
    window.addEventListener("load", toggleBacktotop);
    onscroll(document, toggleBacktotop);
  }

  /**
   * Mobile nav toggle
   */
  on("click", ".mobile-nav-toggle", function (e) {
    select("#navbar").classList.toggle("navbar-mobile");
    this.classList.toggle("bi-list");
    this.classList.toggle("bi-x");
  });

  /**
   * Mobile nav dropdowns activate
   */
  on(
    "click",
    ".navbar .dropdown > a",
    function (e) {
      if (select("#navbar").classList.contains("navbar-mobile")) {
        e.preventDefault();
        this.nextElementSibling.classList.toggle("dropdown-active");
      }
    },
    true
  );

  /**
   * Scrool with offset on links with a class name .scrollto
   */
  // on(
  //   "click",
  //   ".scrollto",
  //   function (e) {
  //     if (select(this.hash)) {
  //       e.preventDefault();

  //       let navbar = select("#navbar");
  //       if (navbar.classList.contains("navbar-mobile")) {
  //         navbar.classList.remove("navbar-mobile");
  //         let navbarToggle = select(".mobile-nav-toggle");
  //         navbarToggle.classList.toggle("bi-list");
  //         navbarToggle.classList.toggle("bi-x");
  //       }
  //       scrollto(this.hash);
  //     }
  //   },
  //   true
  // );

  /**
   * Scroll with offset on page load with hash links in the url
   */
  // window.addEventListener("load", () => {
  //   if (window.location.hash) {
  //     if (select(window.location.hash)) {
  //       scrollto(window.location.hash);
  //     }
  //   }
  // });

  /**
   * Preloader
   */
  // let preloader = select("#preloader");
  // if (preloader) {
  //   window.addEventListener("load", () => {
  //     preloader.remove();
  //   });
  // }

  /**
   * Clients Slider
   */
  // new Swiper(".clients-slider", {
  //   speed: 400,
  //   loop: true,
  //   autoplay: {
  //     delay: 5000,
  //     disableOnInteraction: false,
  //   },
  //   slidesPerView: "auto",
  //   pagination: {
  //     el: ".swiper-pagination",
  //     type: "bullets",
  //     clickable: true,
  //   },
  //   breakpoints: {
  //     320: {
  //       slidesPerView: 2,
  //       spaceBetween: 40,
  //     },
  //     480: {
  //       slidesPerView: 3,
  //       spaceBetween: 60,
  //     },
  //     640: {
  //       slidesPerView: 4,
  //       spaceBetween: 80,
  //     },
  //     992: {
  //       slidesPerView: 6,
  //       spaceBetween: 120,
  //     },
  //   },
  // });

  /**
   * Porfolio isotope and filter
   */
  window.addEventListener("load", () => {
    let portfolioContainer = select(".portfolio-container");
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: ".portfolio-item",
      });

      // let portfolioFilters = select("#portfolio-flters li", true);

      // on(
      //   "click",
      //   "#portfolio-flters li",
      //   function (e) {
      //     e.preventDefault();
      //     portfolioFilters.forEach(function (el) {
      //       el.classList.remove("filter-active");
      //     });
      //     this.classList.add("filter-active");

      //     portfolioIsotope.arrange({
      //       filter: this.getAttribute("data-filter"),
      //     });
      //     portfolioIsotope.on("arrangeComplete", function () {
      //       AOS.refresh();
      //     });
      //   },
      //   true
      // );
    }
  });

  /**
   * Initiate portfolio lightbox
   */
  const portfolioLightbox = GLightbox({
    selector: ".portfolio-lightbox",
  });

  /**
   * Portfolio details slider
   */
  // new Swiper(".portfolio-details-slider", {
  //   speed: 400,
  //   loop: true,
  //   autoplay: {
  //     delay: 5000,
  //     disableOnInteraction: false,
  //   },
  //   pagination: {
  //     el: ".swiper-pagination",
  //     type: "bullets",
  //     clickable: true,
  //   },
  // });

  /**
   * Testimonials slider
   */
  // new Swiper(".testimonials-slider", {
  //   speed: 600,
  //   loop: true,
  //   autoplay: {
  //     delay: 5000,
  //     disableOnInteraction: false,
  //   },
  //   slidesPerView: "auto",
  //   pagination: {
  //     el: ".swiper-pagination",
  //     type: "bullets",
  //     clickable: true,
  //   },
  // });

  /**
   * Animation on scroll
   */
  window.addEventListener("load", () => {
    AOS.init({
      duration: 1000,
      easing: "ease-in-out",
      once: true,
      mirror: false,
    });
  });

  // --

  const range = select("#id_h")
  const range_value = select("#range_value")
  if (range && range_value){
    setValue = () => {
      const newValue = Number(
          ((range.value - range.min) * 100) / (range.max - range.min)
        ),
        newPosition = 10 - newValue * 0.2;
      range_value.innerHTML = `<span>${range.value}</span>`;
      range_value.style.left = `calc(${newValue}% + (${newPosition}px))`;
    };
    document.addEventListener("DOMContentLoaded", setValue);
    range.addEventListener("input", setValue);
  }


  const NF = (val) => new Intl.NumberFormat("ru").format(val);

  const calc = () => {
    const h = Number(select("#id_h").value);
    const h_coeff = Number(select("#id_h_coeff").value);
    // const sct_coeff = Number(select("#id_cst_coeff").value);
    const sct_coeff = Number(select('input[name="cst_coeff"]:checked').value);

    let mf_amount = (h / 0.2) * h_coeff + sct_coeff;
    if (h >= 2) {
      mf_amount += 10000;
    }
    select("#id_mf_amount").textContent = NF(mf_amount);

    const st = Number(select('input[name="st"]:checked').value);
    st_amount = (h / 0.2) * st;
    select("#id_st_amount").textContent = NF(st_amount);

    const rt = Number(select('input[name="rt"]:checked').value);
    rt_amount = (h / 0.2) * rt;
    select("#id_rt_amount").textContent = NF(rt_amount);

    const s_arr = document.getElementsByName("s");
    let s_amount = 0;
    for (var i = 0; i < s_arr.length; i++) {
      if (s_arr[i].checked) {
        s_amount += Number(s_arr[i].value);
      }
    }
    select("#id_s_amount").textContent = NF(s_amount);

    select("#id_total_amount").textContent = NF(
      mf_amount + st_amount + rt_amount + s_amount
    );
  }

  const form_calc = select("#form_calculator");
  if (form_calc) {
    form_calc.addEventListener("change", function () {
      calc();
    });
    calc();
  }

})();
