/* ==========================================================================
   WellBeing Psychotherapy — Shared behavior
   Mobile menu toggle, FAQ accordion, active nav state.
   Active nav state is set per-page via a `data-page` attribute on <body>
   plus a matching `data-nav` attribute on each nav link — see the HTML.
   ========================================================================== */

document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Active nav highlighting ---------- */
  var currentPage = document.body.getAttribute('data-page');
  if (currentPage) {
    document.querySelectorAll('[data-nav]').forEach(function (link) {
      if (link.getAttribute('data-nav') === currentPage) {
        link.classList.add('active');
      }
    });
  }

  /* ---------- Mobile menu toggle ---------- */
  var hamburger = document.querySelector('.hamburger');
  var mobileNav = document.querySelector('.nav-mobile');

  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', function () {
      var isOpen = mobileNav.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      hamburger.textContent = isOpen ? '✕' : '☰';
    });

    // Close mobile menu automatically when a nav link is clicked (navigation happens anyway)
    mobileNav.querySelectorAll('a, button').forEach(function (el) {
      el.addEventListener('click', function () {
        mobileNav.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
        hamburger.textContent = '☰';
      });
    });

    // Close mobile menu if window is resized past the mobile breakpoint
    window.addEventListener('resize', function () {
      if (window.innerWidth > 860 && mobileNav.classList.contains('open')) {
        mobileNav.classList.remove('open');
        hamburger.setAttribute('aria-expanded', 'false');
        hamburger.textContent = '☰';
      }
    });
  }

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll('.faq-row').forEach(function (row) {
    row.addEventListener('click', function () {
      var item = row.closest('.faq-item');
      var icon = row.querySelector('.faq-icon');
      var isOpen = item.classList.toggle('open');
      if (icon) icon.textContent = isOpen ? '−' : '+';
      row.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  });

});
