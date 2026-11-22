/* A small vocabulary of one-time entrances. Continuous logo travel and the two
   signature scroll scenes keep their own timelines. No scroll interception. */
(() => {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  if (reduced.matches || !('IntersectionObserver' in window) || !Element.prototype.animate) return;
  const pending = new Set();
  const active = new Map();
  const targets = new Map();
  const ease = 'cubic-bezier(.16,1,.3,1)';
  const clear = element => { pending.delete(element); element.style.removeProperty('opacity'); };
  const add = (element, kind, delay = 0) => {
    if (element && !targets.has(element)) targets.set(element, {kind, delay});
  };
  const recipes = {
    text: [{opacity: 0, transform: 'translateY(28px)'}, {opacity: 1, transform: 'translateY(0)'}],
    content: [{opacity: 0, transform: 'translateY(54px)'}, {opacity: 1, transform: 'translateY(0)'}],
    heading: [{opacity: 1, clipPath: 'inset(0 0 100% 0)', transform: 'translateY(24px)'},
              {opacity: 1, clipPath: 'inset(0 0 0% 0)', transform: 'translateY(0)'}],
    'band-left': [{opacity: .35, clipPath: 'inset(0 100% 0 0)', transform: 'translateX(-32px)'},
                  {opacity: 1, clipPath: 'inset(0 0% 0 0)', transform: 'translateX(0)'}],
    'band-right': [{opacity: .35, clipPath: 'inset(0 0 0 100%)', transform: 'translateX(32px)'},
                   {opacity: 1, clipPath: 'inset(0 0 0 0%)', transform: 'translateX(0)'}],
    left: [{opacity: 0, transform: 'translateX(-42px)'}, {opacity: 1, transform: 'translateX(0)'}],
    right: [{opacity: 0, transform: 'translateX(42px)'}, {opacity: 1, transform: 'translateX(0)'}],
    image: [{opacity: 1, clipPath: 'inset(0 0 100% 0)'}, {opacity: 1, clipPath: 'inset(0 0 0% 0)'}],
    scale: [{opacity: 0, transform: 'translateY(20px) scale(.94)'}, {opacity: 1, transform: 'translateY(0) scale(1)'}],
    quote: [{opacity: 0, filter: 'blur(4px)', transform: 'translateY(32px)'},
            {opacity: 1, filter: 'blur(0px)', transform: 'translateY(0)'}],
    number: [{opacity: 1, clipPath: 'inset(100% 0 0 0)', transform: 'translateY(18px)'},
             {opacity: 1, clipPath: 'inset(0% 0 0 0)', transform: 'translateY(0)'}],
    close: [{opacity: 1, clipPath: 'inset(0 100% 0 0)'}, {opacity: 1, clipPath: 'inset(0 0% 0 0)'}],
    fade: [{opacity: 0}, {opacity: 1}]
  };
  document.querySelectorAll('.strip__band').forEach((element, index) => add(element, index % 2 ? 'band-right' : 'band-left', index * 140));
  document.querySelectorAll('#services .head, #work .head, .team__intro, .voices .head').forEach(group => {
    [...group.children].forEach((element, index) => add(element, element.matches('h2') && !group.closest('#work') ? 'heading' : 'text', index * 100));
  });
  document.querySelectorAll('.bento > article').forEach((element, index) => add(element, index % 2 ? 'right' : 'left', (index % 3) * 100));
  document.querySelectorAll('.work > .case').forEach((card, index) => add(card, 'content', index * 130));
  document.querySelectorAll('.people > .person').forEach((element, index) => add(element, 'scale', index * 100));
  document.querySelectorAll('.voices__track > .voice').forEach((element, index) => add(element, 'quote', index * 140));
  document.querySelectorAll('.figs > div').forEach((element, index) => add(element, 'text', (index % 3) * 90));
  document.querySelectorAll('.close__inner > *').forEach((element, index) => add(element,
    element.matches('h2') ? 'close' : element.matches('a') ? 'scale' : 'right', index * 140));

  const cancel = element => {
    clear(element);
    (active.get(element) || []).forEach(animation => animation.cancel());
    active.delete(element);
  };
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting || !pending.has(entry.target)) return;
      const element = entry.target;
      observer.unobserve(element);
      const {delay, kind} = targets.get(element);
      const stagger = innerWidth < 700 ? Math.min(delay, 100) : delay;
      const animation = element.animate(recipes[kind], {
        duration: ['image', 'band-left', 'band-right', 'close'].includes(kind) ? 1300 : kind === 'text' ? 900 : 1100,
        delay: stagger, easing: ease, fill: 'both'
      });
      const animations = [animation];
      // A separate inner image plane settles inside the opening mask.
      if (kind === 'image') {
        const image = element.querySelector('img, video');
        if (image) animations.push(image.animate([{transform: 'scale(1.12)'}, {transform: 'scale(1)'}],
          {duration: 1600, delay: stagger, easing: ease, fill: 'both'}));
      }
      active.set(element, animations);
      Promise.all(animations.map(item => item.finished)).then(() => cancel(element)).catch(() => clear(element));
    });
  }, {threshold: 0, rootMargin: '0px 0px -64px 0px'});
  const revealAll = () => {
    observer.disconnect();
    [...pending].forEach(cancel);
    [...active.keys()].forEach(cancel);
  };
  targets.forEach((options, element) => {
    if (element.getBoundingClientRect().bottom < 0) return;
    element.style.opacity = '0'; pending.add(element); observer.observe(element);
  });
  // Never make keyboard users wait for a link or any of its content.
  document.addEventListener('focusin', event => {
    targets.forEach((options, element) => {
      if (element === event.target || element.contains(event.target) || event.target.contains(element)) {
        observer.unobserve(element); cancel(element);
      }
    });
  });
  reduced.addEventListener('change', event => { if (event.matches) revealAll(); });
  addEventListener('beforeprint', revealAll);
  addEventListener('pageshow', event => { if (event.persisted) revealAll(); });
})();
