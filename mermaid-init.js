(function () {
  function getTheme() {
    return document.documentElement.getAttribute('data-theme') === 'dark' ? 'dark' : 'default';
  }

  function initMermaid(theme) {
    mermaid.initialize({
      startOnLoad: false,
      theme: theme,
      themeVariables: theme === 'dark'
        ? { primaryColor: '#26262e', primaryTextColor: '#F1EEE9', lineColor: '#555', secondaryColor: '#1a1a1f', tertiaryColor: '#333', primaryBorderColor: '#444', edgeLabelBackground: 'transparent' }
        : { primaryColor: '#E6E3DE', primaryTextColor: '#080A0D', lineColor: '#999', secondaryColor: '#F1EEE9', tertiaryColor: '#ddd', primaryBorderColor: '#B3B3B3', edgeLabelBackground: 'transparent' },
      flowchart: { curve: 'monotoneX', padding: 12 },
      fontFamily: 'Inter, -apple-system, sans-serif',
      fontSize: 13
    });
  }

  var script = document.createElement('script');
  script.src = 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js';
  script.onload = function () {
    var sources = {};
    document.querySelectorAll('.mermaid').forEach(function (el, i) {
      sources[i] = el.textContent;
      el.setAttribute('data-idx', i);
    });

    initMermaid(getTheme());
    mermaid.run();

    var observer = new MutationObserver(function (mutations) {
      mutations.forEach(function (m) {
        if (m.attributeName === 'data-theme') {
          document.querySelectorAll('.mermaid').forEach(function (el) {
            var idx = el.getAttribute('data-idx');
            el.removeAttribute('data-processed');
            el.innerHTML = sources[idx];
          });
          initMermaid(getTheme());
          mermaid.run();
        }
      });
    });
    observer.observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
  };
  document.head.appendChild(script);
})();
