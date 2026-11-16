/* Progressive enhancement: titles navigate; paragraph buttons expand inline cards. */
'use strict';
const grid = document.querySelector('.topic-grid');
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
const finishMotion = () => {
  grid?.getAnimations({ subtree: true }).forEach((animation) => animation.cancel());
};
reduceMotion.addEventListener('change', finishMotion);
document.querySelectorAll('.topic-expand').forEach((button) => {
  const ids = button.getAttribute('aria-controls').split(/\s+/);
  const children = ids.map((id) => document.getElementById(id));
  if (children.some((child) => !child)) return;
  const label = button.querySelector('.expand-label');
  const setExpanded = (expanded) => {
    button.setAttribute('aria-expanded', String(expanded));
    children.forEach((child) => { child.hidden = !expanded; });
    label.textContent = `${expanded ? '收合' : '展開'}延伸閱讀（${children.length}） ${expanded ? '−' : '+'}`;
  };
  setExpanded(false);
  button.addEventListener('click', () => {
    finishMotion();
    const cards = [...grid.children];
    const before = new Map(cards.filter((card) => !card.hidden)
      .map((card) => [card, card.getBoundingClientRect()]));
    const expanded = button.getAttribute('aria-expanded') !== 'true';
    setExpanded(expanded);
    if (reduceMotion.matches) return;
    // Animate the layout change without moving cards out of their normal grid flow.
    cards.filter((card) => !card.hidden).forEach((card) => {
      const previous = before.get(card);
      const next = card.getBoundingClientRect();
      const timing = { duration: 260, easing: 'cubic-bezier(.22,.61,.36,1)' };
      if (previous) {
        card.animate([
          { transform: `translate(${previous.left - next.left}px, ${previous.top - next.top}px)` },
          { transform: 'translate(0, 0)' }
        ], timing);
      } else {
        card.animate([
          { opacity: 0, transform: 'translateY(12px)' },
          { opacity: 1, transform: 'translateY(0)' }
        ], timing);
      }
    });
  });
});
