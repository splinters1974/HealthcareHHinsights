/* Hospital Energy Insights: gentle motion.
   Elements drop in as they scroll into view; hero photos drift with the scroll.
   Does nothing if the visitor has asked for reduced motion (the "motion" class
   on <html> is only added when motion is allowed and the browser supports it). */
(function () {
  var root = document.documentElement;
  if (!root.classList.contains('motion')) return;

  // Things that drop in. Items inside a grid are staggered so a row arrives left to right.
  var SINGLE = [
    '.section-kicker', '.section-title', '.section-lead', '.head-row', '.figure', '.table-wrap', '.note',
    '.prose > h2', '.prose > p.answer', '.about-person', '.sample-cta', '.stat-grid', '.cta-strip-inner',
    '.side-cta', '.toc', '.faq-group', '.sources', '.page-hero-inner > *', '.hero-copy > *', '.start-card'
  ];
  var GROUPS = [
    ['.link-grid', '.link-card'], ['.steps', ':scope > div'], ['.reasons', ':scope > div'],
    ['.finding-grid', '.finding'], ['.stat-grid', ':scope > div'], ['.home-more', ':scope > div'],
    ['.faq', 'details'], ['.hero-points', ':scope > div'], ['.split', ':scope > *']
  ];

  var seen = new Set();
  function tag(el, delay) {
    if (seen.has(el) || el.closest('.site-nav, .site-footer')) return;
    seen.add(el);
    el.classList.add('reveal');
    if (delay) el.style.setProperty('--reveal-delay', delay + 'ms');
  }
  GROUPS.forEach(function (g) {
    document.querySelectorAll(g[0]).forEach(function (parent) {
      var kids;
      try { kids = parent.querySelectorAll(g[1]); } catch (e) { kids = parent.children; }
      Array.prototype.forEach.call(kids, function (el, i) { tag(el, Math.min(i, 6) * 90); });
    });
  });
  SINGLE.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (el, i) {
      var inHero = el.closest('.hero-copy, .page-hero-inner');
      tag(el, inHero ? Math.min(i, 5) * 110 : 0);
    });
  });

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  seen.forEach(function (el) { io.observe(el); });

  // Safety net: never leave anything hidden (printing, odd browsers, jump links).
  window.addEventListener('beforeprint', function () { seen.forEach(function (el) { el.classList.add('is-in'); }); });
  setTimeout(function () {
    seen.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight && r.bottom > 0) el.classList.add('is-in');
    });
  }, 1500);

  // Hero photo drifts a little as the page scrolls (on top of its slow pan and zoom).
  var heroes = document.querySelectorAll('.hero-wrap, .page-hero-photo');
  if (heroes.length) {
    var ticking = false;
    var update = function () {
      heroes.forEach(function (h) {
        var r = h.getBoundingClientRect();
        if (r.bottom < 0) return;
        var shift = Math.max(-1, Math.min(1, -r.top / Math.max(r.height, 1)));
        h.style.setProperty('--hero-scroll', (shift * 60).toFixed(1) + 'px');
      });
      ticking = false;
    };
    window.addEventListener('scroll', function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }
})();
