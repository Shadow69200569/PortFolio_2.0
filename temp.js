
  document.addEventListener('DOMContentLoaded', () => {
    const scrollFill = document.getElementById('scroll-progress-fill');
    if (!scrollFill) return;
    let ticking = false;
    const updateScrollProgress = () => {
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrollPercentage = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
      scrollFill.style.height = scrollPercentage + '%';
      ticking = false;
    };
    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(updateScrollProgress);
        ticking = true;
      }
    }, { passive: true });
    updateScrollProgress(); // init
  });

