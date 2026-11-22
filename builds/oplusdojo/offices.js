/* Scroll is the timeline. No animation loop, remote scripts, or runtime assets. */
(() => {
  const section = document.querySelector('.offices');
  if (!section) return;
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const footer = section.closest('footer');
  const routes = [...section.querySelectorAll('[data-office-route]')];
  const regions = [...section.querySelectorAll('[data-office-region]')];
  const pins = [...section.querySelectorAll('[data-office-pin]')];
  const geography = section.querySelector('.offices__geography');
  const clamp = n => Math.max(0, Math.min(1, n));
  let visible = false;
  let frame = 0;

  function render() {
    frame = 0;
    if (document.hidden || !visible) return;
    const footerTop = footer.getBoundingClientRect().top + scrollY;
    const start = Math.max(0, footerTop - innerHeight);
    const end = document.documentElement.scrollHeight - innerHeight;
    const progress = reduced.matches ? 1 : clamp((scrollY - start) / Math.max(1, end - start));
    section.dataset.officeProgress = progress.toFixed(3);
    section.dataset.scVerifyState = progress.toFixed(3);
    geography.style.transform = `scale(${1.08 - .08 * progress}) translateY(${5 * (1 - progress)}px)`;
    routes.forEach((route, i) => {
      const drawn = reduced.matches ? 1 : clamp((progress - i * .15) / (1 - i * .15));
      route.style.strokeDasharray = '1';
      route.style.strokeDashoffset = String(1 - drawn);
      route.style.opacity = String(.35 + drawn * .65);
    });
    regions.forEach((region, i) => {
      const amount = reduced.matches ? 1 : clamp((progress - i * .15) / .4);
      region.style.opacity = String(.1 + .58 * amount);
      pins[i].style.opacity = String(.6 + .4 * amount);
    });
  }
  function schedule() {
    if (visible && !frame && !document.hidden) frame = requestAnimationFrame(render);
  }
  const observer = new IntersectionObserver(entries => {
    visible = entries[0].isIntersecting;
    if (visible) schedule();
  }, { rootMargin: '100px' });
  observer.observe(footer);
  addEventListener('scroll', schedule, { passive: true });
  addEventListener('resize', schedule, { passive: true });
  document.addEventListener('visibilitychange', schedule);
  reduced.addEventListener('change', schedule);
  addEventListener('load', schedule);
  document.fonts.ready.then(schedule);
})();
