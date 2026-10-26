/*
 * Dynamický banner aktuální akce / workshopu.
 * Zdroj pravdy pro inzerci napříč webem — čte živá data z vibecoding.cz API.
 *
 * Použití: vlož kontejner s id="vibecoding-promo" a data-atributy,
 * pak načti tento skript:
 *
 *   <div class="posts">
 *     <div id="vibecoding-promo" data-utm-campaign="event-promo" style="display:none;"></div>
 *   </div>
 *   <script src="/js/promo-banner.js" defer></script>
 *
 * data-utm-campaign — hodnota utm_campaign v odkazu (default: "event-promo")
 */
(function () {
  var container = document.getElementById('vibecoding-promo');
  if (!container) return;

  var campaign = container.getAttribute('data-utm-campaign') || 'event-promo';
  // Plocha pro promo analytiku (homepage | article | other). Banner bývá v postech → 'article'.
  var surface = container.getAttribute('data-surface') || 'article';
  var months = ['ledna', 'února', 'března', 'dubna', 'května', 'června',
    'července', 'srpna', 'září', 'října', 'listopadu', 'prosince'];

  // Imprese se zapíše, až je banner aspoň z poloviny vidět (stejně jako topflix).
  // Bez ní nejde na vibecoding.cz spočítat CTR marigoldu.
  function trackImpression(e) {
    if (!e.impressionUrl) return;
    var sent = false;
    function send() {
      if (sent) return;
      sent = true;
      try {
        var iu = new URL(e.impressionUrl, 'https://www.vibecoding.cz');
        iu.searchParams.set('site', 'marigold');
        iu.searchParams.set('surface', surface);
        iu.searchParams.set('view_id', window.crypto && crypto.randomUUID
          ? crypto.randomUUID()
          : Date.now() + '-' + Math.random().toString(36).slice(2));
        if (navigator.sendBeacon) navigator.sendBeacon(iu.toString());
        else fetch(iu.toString(), { method: 'POST', keepalive: true, mode: 'no-cors' }).catch(function () {});
      } catch (_) { /* měření nesmí rozbít stránku */ }
    }
    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function (entries) {
        if (entries.some(function (en) { return en.isIntersecting && en.intersectionRatio >= 0.5; })) {
          observer.disconnect();
          send();
        }
      }, { threshold: [0.5] });
      observer.observe(container);
    } else {
      send();
    }
  }

  fetch('https://www.vibecoding.cz/api/active-promotion')
    .then(function (r) { return r.json(); })
    .then(function (e) {
      if (!e || !e.slug) return;

      // Data z API se vkládají do innerHTML — escapuj vše interpolované.
      function esc(s) {
        return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
          return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
        });
      }

      // Reklama / externí promo slot (isAd): nemá reálný termín ani město,
      // místo „Naše akce" má vlastní štítek a CTA „Více". Datum se nezobrazuje.
      var isAd = !!e.isAd;
      // V promo zóně (ad-zone-top.html) říká „Naše akce" už štítek zóny → odznak by se zdvojil.
      var zone = container.closest('.ad-zone-top');
      var showBadge = isAd || !zone;

      var dateText = '';
      if (!isAd && e.date) {
        var d = e.date.split('-');
        var df = parseInt(d[2]) + '. ' + months[parseInt(d[1]) - 1] + ' ' + d[0];
        var city = e.city || (e.location ? e.location.split(',').slice(-1)[0].trim() : '');
        dateText = df + (city ? ' · ' + city : '') +
          (e.dateVariants && e.dateVariants.length > 1 ? ' · a další termíny' : '');
      }
      // Klik vede přes náš promo redirect (změří klik podle site/surface + připojí UTM).
      // clickUrl nemá query string → parametry přidáváme přes URL API, ne lepením '&'.
      // Fallback na přímý odkaz na akci, kdyby clickUrl chybělo (starší cache odpovědi).
      var url;
      if (e.clickUrl) {
        try {
          var cu = new URL(e.clickUrl);
          cu.searchParams.set('site', 'marigold');
          cu.searchParams.set('surface', surface);
          url = cu.toString();
        } catch (_) { url = e.clickUrl; }
      } else {
        url = 'https://www.vibecoding.cz/akce/' + encodeURIComponent(e.slug).replace(/%2F/gi, '/') +
          '/?utm_source=marigold&utm_medium=web&utm_campaign=' + encodeURIComponent(campaign);
      }

      if (e.isPaid) {
        // Tmavý workshop banner
        var earlyHtml = '';
        if (e.earlyBirdPrice && e.earlyBirdDeadline) {
          var now = new Date();
          var deadline = new Date(e.earlyBirdDeadline + 'T23:59:59');
          if (now <= deadline) {
            var ed = e.earlyBirdDeadline.split('-');
            earlyHtml = '<div class="workshop-banner-early">Early bird — do ' +
              parseInt(ed[2]) + '. ' + months[parseInt(ed[1]) - 1] + '.</div>';
          }
        }
        container.innerHTML =
          '<a href="' + url + '" class="workshop-banner-link">' +
            '<div class="workshop-banner">' +
              '<div class="workshop-banner-content">' +
                '<div class="workshop-banner-header-row">' +
                  '<span class="workshop-banner-badge">' + (e.isPaid ? 'Workshop' : 'Akce') + '</span>' +
                  '<span class="workshop-banner-date">' + esc(dateText) + '</span>' +
                '</div>' +
                '<div class="workshop-banner-title">' + esc(e.title) + '</div>' +
                (e.bannerDescription ? '<div class="workshop-banner-desc">' + esc(e.bannerDescription) + '</div>' : '') +
                earlyHtml +
              '</div>' +
              '<div class="workshop-banner-cta">' +
                '<span class="workshop-banner-btn">Detaily &rarr;</span>' +
              '</div>' +
            '</div>' +
          '</a>';
      } else {
        // Kompaktní "Naše akce" banner
        container.innerHTML =
          '<a href="' + url + '" class="promo-card-compact-link">' +
            '<div class="promo-card-compact">' +
              '<div class="promo-left">' +
                (showBadge ? '<span class="promo-badge-sm">' + (isAd ? esc(e.badgeLabel || 'Tip') : 'Naše akce') + '</span>' : '') +
                '<span class="promo-title-sm">' + esc(e.title) + '</span>' +
                (dateText ? '<span class="promo-meta">' + esc(dateText) + '</span>' : '') +
                (e.bannerDescription ? '<span class="promo-meta">' + esc(e.bannerDescription) + '</span>' : '') +
              '</div>' +
              '<div class="promo-right">' +
                '<span class="promo-cta-btn">' + (isAd ? 'Více' : 'Detaily') + ' &rarr;</span>' +
              '</div>' +
            '</div>' +
          '</a>';
      }
      container.style.display = '';
      trackImpression(e);

      // Štítek zóny (ad-zone-top.html) — placený slot musí být označen jako reklama.
      var label = zone && zone.querySelector('.ad-zone-label');
      if (label) {
        label.querySelector('span').textContent = isAd ? 'Reklama' : 'Naše akce';
        label.hidden = false;
      }
    })
    .catch(function () {});
})();
