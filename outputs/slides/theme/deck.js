/* Kawaii deck runtime：等比縮放 16:9 畫布、翻頁、小湯圓進度、詳細數據抽屜。
   HTML 需要：<div class="stage"> 內含多個 <section class="slide">。
   可選：<body data-walker="assets/tangyuan/tangyuan_happy.svg"> 指定進度小人。 */
(function () {
  const stage = document.querySelector('.stage');
  const slides = [...document.querySelectorAll('.slide')];
  if (!stage || !slides.length) return;

  // 等比縮放
  function fit() {
    const pad = 70; // 留給底部導覽
    const s = Math.min(window.innerWidth / 1600, (window.innerHeight - pad) / 900);
    stage.style.transform = `translate(-50%, calc(-50% - ${pad / 2 - 6}px)) scale(${s})`;
  }
  window.addEventListener('resize', fit);
  fit();

  // 導覽元件
  const walkerSrc = document.body.dataset.walker || 'assets/tangyuan/tangyuan_happy.svg';
  document.body.insertAdjacentHTML('beforeend', `
    <button class="navbtn prev" aria-label="上一張">←</button>
    <div class="trail" aria-hidden="true">
      <div class="walker"><img src="${walkerSrc}" alt=""></div>
      <span class="count"></span>
    </div>
    <button class="navbtn next" aria-label="下一張">→</button>`);
  const prev = document.querySelector('.navbtn.prev');
  const next = document.querySelector('.navbtn.next');
  const walker = document.querySelector('.trail .walker');
  const count = document.querySelector('.trail .count');

  let i = 0;
  const h = parseInt(location.hash.slice(1), 10);
  if (h >= 1 && h <= slides.length) i = h - 1;

  function show(n) {
    i = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach((s, k) => {
      s.classList.toggle('active', k === i);
      if (k !== i) s.querySelectorAll('details[open]').forEach(d => d.open = false);
    });
    walker.style.left = slides.length > 1 ? `${(i / (slides.length - 1)) * 100}%` : '0%';
    count.textContent = `${i + 1} / ${slides.length}`;
    prev.disabled = i === 0;
    next.disabled = i === slides.length - 1;
    history.replaceState(null, '', `#${i + 1}`);
  }
  window.deckShow = show;

  prev.onclick = () => show(i - 1);
  next.onclick = () => show(i + 1);
  document.addEventListener('keydown', e => {
    if (e.target.closest('input, textarea, summary')) return;
    if (['ArrowRight', 'PageDown', ' '].includes(e.key)) { e.preventDefault(); show(i + 1); }
    if (['ArrowLeft', 'PageUp'].includes(e.key)) { e.preventDefault(); show(i - 1); }
    if (e.key === 'Home') show(0);
    if (e.key === 'End') show(slides.length - 1);
    if (e.key === 'Escape') document.querySelectorAll('details[open]').forEach(d => d.open = false);
  });
  let x0 = null;
  document.addEventListener('touchstart', e => { x0 = e.touches[0].clientX; }, { passive: true });
  document.addEventListener('touchend', e => {
    if (x0 === null || e.target.closest('.more')) { x0 = null; return; }
    const dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 50) show(i + (dx < 0 ? 1 : -1));
    x0 = null;
  });
  show(i);
})();
