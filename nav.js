(function () {
  'use strict';

  /* ── Mobile navigation drawer ── */
  var hamburger = document.querySelector('.nav-hamburger');
  var overlay = document.getElementById('navOverlay');
  var drawer = document.getElementById('navDrawer');

  function openNav() {
    hamburger.classList.add('open');
    overlay.classList.add('open');
    drawer.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeNav() {
    hamburger.classList.remove('open');
    overlay.classList.remove('open');
    drawer.classList.remove('open');
    document.body.style.overflow = '';
  }

  function toggleNav() {
    drawer.classList.contains('open') ? closeNav() : openNav();
  }

  if (hamburger) {
    hamburger.addEventListener('click', toggleNav);
  }
  if (overlay) {
    overlay.addEventListener('click', closeNav);
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && drawer && drawer.classList.contains('open')) {
      closeNav();
    }
  });

  /* ── Drawer theme toggle ── */
  var drawerThemeBtn = drawer ? drawer.querySelector('.theme-toggle') : null;
  if (drawerThemeBtn) {
    drawerThemeBtn.addEventListener('click', function () {
      var next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('growthx-theme', next);
    });
  }

  /* ── Play overlays for inline video clips ── */
  document.querySelectorAll('.inline-clip-body').forEach(function (body) {
    var video = body.querySelector('video');
    if (!video) return;

    if (!body.querySelector('.play-overlay')) {
      var el = document.createElement('div');
      el.className = 'play-overlay';
      el.innerHTML = '<svg viewBox="0 0 24 24"><polygon points="6,3 20,12 6,21"/></svg>';
      body.appendChild(el);
    }

    body.addEventListener('click', function (e) {
      if (e.target.closest('video') && video.controls) return;
      video.paused ? video.play() : video.pause();
    });

    video.addEventListener('play', function () { body.classList.add('playing'); });
    video.addEventListener('pause', function () { body.classList.remove('playing'); });
    video.addEventListener('ended', function () { body.classList.remove('playing'); });
  });
})();
