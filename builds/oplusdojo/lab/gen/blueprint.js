/* Signature move: the blueprint drafts itself from the act's --sc-p, the
   revision ledger accumulates, and the drawing is stamped for production. */
(function () {
  var act = document.getElementById('blueprint');
  if (!act) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return; // finished drawing stays

  var phases = { a: [0.03, 0.24], b: [0.22, 0.48], c: [0.47, 0.68], d: [0.67, 0.86] };
  var STAMP_AT = 0.9;
  var items = [];
  Object.keys(phases).forEach(function (k) {
    var g = act.querySelector('[data-ph="' + k + '"]');
    var els = [].slice.call(g.children);
    var strokes = els.filter(function (e) { return e.hasAttribute('pathLength'); });
    var others = els.filter(function (e) { return !e.hasAttribute('pathLength'); });
    var s = phases[k][0], len = phases[k][1] - phases[k][0];
    strokes.forEach(function (e, i) {
      var from = s + (i / strokes.length) * len * 0.55;
      items.push({ el: e, kind: 'stroke', from: from, to: from + len * 0.45, dash: e.getAttribute('stroke-dasharray') });
    });
    others.forEach(function (e, i) {
      var from = s + len * (0.35 + 0.4 * (i / Math.max(others.length, 1)));
      items.push({ el: e, kind: 'fade', from: from, to: from + len * 0.25 });
    });
  });
  var pencil = act.querySelector('[data-ph="a"]');
  var penText = [].slice.call(pencil.querySelectorAll('text'));
  var rows = [].slice.call(act.querySelectorAll('.bp__rows li'));
  var stamp = act.querySelector('.stamp');
  var sheet = act.querySelector('.bp__sheet');
  act.classList.add('bp-live');

  function clamp(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }
  var last = -1;
  function frame() {
    var p = parseFloat(act.style.getPropertyValue('--sc-p')) || 0;
    if (Math.abs(p - last) > 0.0005) {
      last = p;
      for (var i = 0; i < items.length; i++) {
        var it = items[i], t = clamp((p - it.from) / (it.to - it.from));
        if (it.kind === 'stroke') {
          if (it.dash) {
            // dashed lines reveal through opacity so their dash pattern survives
            it.el.style.opacity = t;
          } else {
            it.el.style.strokeDasharray = '1 1';
            it.el.style.strokeDashoffset = (1 - t).toFixed(4);
          }
        } else {
          it.el.style.opacity = t;
        }
      }
      // the concept sketch recedes once the architecture is inked
      var fadeP = clamp((p - 0.4) / 0.12);
      pencil.style.opacity = (1 - 0.72 * fadeP).toFixed(3);
      for (var q = 0; q < penText.length; q++) penText[q].style.opacity = (1 - fadeP).toFixed(3);
      var phaseKeys = ['a', 'b', 'c', 'd'], cur = -1;
      phaseKeys.forEach(function (k, idx) { if (p >= phases[k][0]) cur = idx; });
      rows.forEach(function (r, idx) {
        r.classList.toggle('is-on', idx <= cur);
        r.classList.toggle('is-current', idx === cur);
      });
      stamp.classList.toggle('is-on', p >= STAMP_AT);
      // phones: the sheet is wider than the screen, so the camera follows the pen
      sheet.style.setProperty('--bp-pan', clamp((p - 0.05) / 0.8).toFixed(4));
    }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();
