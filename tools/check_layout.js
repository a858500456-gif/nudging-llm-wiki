// Check 3-2 畫面檢查：在瀏覽器打開投影片（slides 預覽伺服器），把整段貼進 console 或用瀏覽器工具執行。
// 回傳 { brokenImages, problems }：圖片載入失敗、某頁內容溢出、圖貼蓋到文字。兩個都是空陣列才算通過。
(() => {
  const problems = [];
  const slides = [...document.querySelectorAll('.slide')];
  const brokenImages = [...document.images].filter(i => i.naturalWidth === 0).map(i => i.getAttribute('src'));
  slides.forEach((s, k) => {
    window.deckShow(k);
    s.querySelectorAll('.sticker').forEach(st => { st.style.animation = 'none'; });
    if (s.scrollHeight > s.clientHeight + 2) problems.push(`S${k + 1} 內容溢出`);
    const texts = [];
    const walker = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = walker.nextNode())) {
      if (!n.textContent.trim()) continue;
      if (n.parentElement.closest('details:not([open]) .more-panel')) continue;
      const r = document.createRange();
      r.selectNodeContents(n);
      for (const rc of r.getClientRects()) texts.push([rc, n.textContent.trim().slice(0, 12)]);
    }
    s.querySelectorAll('img.sticker').forEach(img => {
      const b = img.getBoundingClientRect();
      const pad = b.width * 0.12; // 圖貼四周有白色描邊和透明邊，內縮一點再判斷
      const box = { l: b.left + pad, r: b.right - pad, t: b.top + pad, b: b.bottom - pad };
      texts.forEach(([rc, t]) => {
        if (rc.left < box.r && rc.right > box.l && rc.top < box.b && rc.bottom > box.t) {
          problems.push(`S${k + 1} 圖貼 ${img.getAttribute('src').split('/').pop()} 蓋到「${t}」`);
        }
      });
    });
  });
  window.deckShow(0);
  return { brokenImages, problems };
})();
