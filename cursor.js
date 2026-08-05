/**
 * AETHER PORTFOLIO — Premium Custom Cursor System
 * Version 2.0 | GPU-accelerated | 60 FPS | Per-page themes
 *
 * Pages and their themes:
 *  index.html       → HERO    — Aura dot + trailing ring, gradient morphing, lavender/purple
 *  projects.html    → FORGE   — Crosshair + spark particles, orange/purple accent
 *  certificates.html→ VAULT   — Diamond/gem shape, gold/purple, shimmer trail
 *  github.html      → CODE    — Terminal bracket cursor, green/cyan pixel glow
 *  leetcode.html    → SOLVE   — Circular progress ring, orange/yellow algorithmic feel
 *
 * CRITICAL: Never modifies any existing DOM, styles, scripts or functionality.
 * Only adds the cursor DOM elements and its own styles/listeners.
 */

(function () {
  'use strict';

  // ── 1. Touch guard ─────────────────────────────────────────────────────────
  if ('ontouchstart' in window || navigator.maxTouchPoints > 0) return;

  // ── 2. Detect current page ─────────────────────────────────────────────────
  const PAGE = (function () {
    const p = location.pathname.split('/').pop().toLowerCase();
    if (!p || p === 'index.html') return 'hero';
    if (p.startsWith('project')) return 'forge';
    if (p.startsWith('cert')) return 'vault';
    if (p.startsWith('github')) return 'code';
    if (p.startsWith('leetcode')) return 'solve';
    return 'hero';
  })();

  // ── 3. Theme definitions ───────────────────────────────────────────────────
  const THEMES = {
    hero: {
      dotColor: 'rgba(196, 192, 255, 0.95)',
      dotSize: 10,
      ringColor: 'rgba(196, 192, 255, 0.25)',
      ringSize: 38,
      ringBorder: '1.5px solid rgba(196, 192, 255, 0.5)',
      hoverDotColor: 'rgba(196, 192, 255, 1)',
      hoverDotScale: 0.4,
      hoverRingScale: 1.8,
      hoverRingColor: 'rgba(108, 99, 255, 0.35)',
      hoverRingBorder: '1.5px solid rgba(108, 99, 255, 0.7)',
      glowColor: '196, 192, 255',
      trailCount: 6,
      trailColor: 'rgba(196, 192, 255,',
      label: null,
    },
    forge: {
      dotColor: 'rgba(240, 83, 28, 0.9)',
      dotSize: 8,
      ringColor: 'rgba(240, 83, 28, 0.15)',
      ringSize: 36,
      ringBorder: '1.5px solid rgba(240, 83, 28, 0.5)',
      hoverDotColor: 'rgba(255, 255, 255, 0.95)',
      hoverDotScale: 0.3,
      hoverRingScale: 2.0,
      hoverRingColor: 'rgba(240, 83, 28, 0.25)',
      hoverRingBorder: '1.5px solid rgba(240, 83, 28, 0.85)',
      glowColor: '240, 83, 28',
      trailCount: 5,
      trailColor: 'rgba(240, 83, 28,',
      label: null,
    },
    vault: {
      dotColor: 'rgba(221, 183, 255, 0.95)',
      dotSize: 9,
      ringColor: 'rgba(221, 183, 255, 0.15)',
      ringSize: 36,
      ringBorder: '1.5px solid rgba(221, 183, 255, 0.45)',
      hoverDotColor: 'rgba(221, 183, 255, 1)',
      hoverDotScale: 0.35,
      hoverRingScale: 1.9,
      hoverRingColor: 'rgba(183, 109, 255, 0.25)',
      hoverRingBorder: '1.5px solid rgba(183, 109, 255, 0.75)',
      glowColor: '221, 183, 255',
      trailCount: 5,
      trailColor: 'rgba(221, 183, 255,',
      label: null,
    },
    code: {
      dotColor: 'rgba(94, 174, 234, 0.95)',
      dotSize: 7,
      ringColor: 'rgba(94, 174, 234, 0.12)',
      ringSize: 34,
      ringBorder: '1px solid rgba(94, 174, 234, 0.5)',
      hoverDotColor: 'rgba(94, 174, 234, 1)',
      hoverDotScale: 0.3,
      hoverRingScale: 1.9,
      hoverRingColor: 'rgba(94, 174, 234, 0.2)',
      hoverRingBorder: '1px solid rgba(94, 174, 234, 0.9)',
      glowColor: '94, 174, 234',
      trailCount: 4,
      trailColor: 'rgba(94, 174, 234,',
      label: null,
    },
    solve: {
      dotColor: 'rgba(255, 161, 22, 0.95)',
      dotSize: 9,
      ringColor: 'rgba(255, 161, 22, 0.12)',
      ringSize: 36,
      ringBorder: '1.5px solid rgba(255, 161, 22, 0.45)',
      hoverDotColor: 'rgba(255, 200, 80, 1)',
      hoverDotScale: 0.3,
      hoverRingScale: 1.85,
      hoverRingColor: 'rgba(255, 161, 22, 0.2)',
      hoverRingBorder: '1.5px solid rgba(255, 161, 22, 0.85)',
      glowColor: '255, 161, 22',
      trailCount: 5,
      trailColor: 'rgba(255, 161, 22,',
      label: null,
    },
  };

  const T = THEMES[PAGE];

  // ── 4. Inject styles ───────────────────────────────────────────────────────
  const styleEl = document.createElement('style');
  styleEl.id = 'aether-cursor-styles';
  // Use @layer so our rules are authoritative even inside body-level style blocks
  styleEl.textContent = `
    /* Hide default cursor — injected at end of body to beat any inline <style> blocks */
    html, body, * { cursor: none !important; }
    *::before, *::after { cursor: none !important; }

    /* But restore text cursor for inputs / textareas */
    input, textarea, [contenteditable="true"] { cursor: text !important; }

    /* Base cursor elements */
    #aether-cursor-dot,
    #aether-cursor-ring {
      position: fixed;
      top: 0; left: 0;
      pointer-events: none;
      z-index: 2147483647;
      border-radius: 50%;
      will-change: transform;
      backface-visibility: hidden;
    }

    #aether-cursor-dot {
      width: ${T.dotSize}px;
      height: ${T.dotSize}px;
      background: ${T.dotColor};
      box-shadow: 0 0 10px 2px rgba(${T.glowColor}, 0.6);
      transform: translate(-50%, -50%);
      transition: width 0.2s ease, height 0.2s ease,
                  background 0.2s ease, box-shadow 0.2s ease,
                  opacity 0.25s ease;
    }

    #aether-cursor-ring {
      width: ${T.ringSize}px;
      height: ${T.ringSize}px;
      background: ${T.ringColor};
      border: ${T.ringBorder};
      box-shadow: inset 0 0 10px rgba(${T.glowColor}, 0.08);
      transform: translate(-50%, -50%);
      transition: width 0.35s cubic-bezier(0.23, 1, 0.32, 1),
                  height 0.35s cubic-bezier(0.23, 1, 0.32, 1),
                  background 0.35s ease, border 0.35s ease,
                  border-radius 0.35s ease, opacity 0.25s ease;
    }

    /* Trail dots */
    .aether-trail {
      position: fixed;
      top: 0; left: 0;
      width: 5px; height: 5px;
      border-radius: 50%;
      pointer-events: none;
      z-index: 2147483646;
      will-change: transform, opacity;
      transform: translate(-50%, -50%);
    }

    /* Page-specific ring shapes */
    ${PAGE === 'forge' ? `
    /* Forge: Crosshair lines on the ring */
    #aether-cursor-ring::before,
    #aether-cursor-ring::after {
      content: '';
      position: absolute;
      background: rgba(240, 83, 28, 0.35);
      border-radius: 2px;
      pointer-events: none;
    }
    #aether-cursor-ring::before {
      width: 1px; height: 100%;
      left: 50%; top: 0;
      transform: translateX(-50%);
    }
    #aether-cursor-ring::after {
      height: 1px; width: 100%;
      top: 50%; left: 0;
      transform: translateY(-50%);
    }
    ` : ''}

    ${PAGE === 'vault' ? `
    /* Vault: rotate the ring slowly */
    #aether-cursor-ring {
      border-radius: 50%;
      animation: aether-vault-spin 8s linear infinite;
    }
    @keyframes aether-vault-spin {
      from { transform: translate(-50%, -50%) rotate(0deg); }
      to   { transform: translate(-50%, -50%) rotate(360deg); }
    }
    ` : ''}

    ${PAGE === 'code' ? `
    /* Code: square-ish ring with corner accents */
    #aether-cursor-ring {
      border-radius: 4px;
    }
    #aether-cursor-ring::before,
    #aether-cursor-ring::after {
      content: '';
      position: absolute;
      pointer-events: none;
    }
    ` : ''}

    ${PAGE === 'solve' ? `
    /* Solve: spinning dashed ring */
    #aether-cursor-ring {
      border-style: dashed;
      border-width: 1.5px;
      animation: aether-solve-spin 3s linear infinite;
    }
    @keyframes aether-solve-spin {
      from { transform: translate(-50%, -50%) rotate(0deg); }
      to   { transform: translate(-50%, -50%) rotate(360deg); }
    }
    ` : ''}

    /* Hover state: clicked pulse */
    @keyframes aether-click-pulse {
      0%   { box-shadow: 0 0 0 0 rgba(${T.glowColor}, 0.7); }
      70%  { box-shadow: 0 0 0 14px rgba(${T.glowColor}, 0); }
      100% { box-shadow: 0 0 0 0 rgba(${T.glowColor}, 0); }
    }
    .aether-clicking #aether-cursor-ring {
      animation: aether-click-pulse 0.4s ease-out forwards
                 ${PAGE === 'vault' ? ', aether-vault-spin 8s linear infinite' : ''}
                 ${PAGE === 'solve' ? ', aether-solve-spin 3s linear infinite' : ''} !important;
    }

    /* Text hover: beam / I-bar */
    .aether-text-hover #aether-cursor-dot {
      width: 2px !important;
      height: ${T.dotSize * 2}px !important;
      border-radius: 1px !important;
      background: rgba(${T.glowColor}, 0.9) !important;
    }
    .aether-text-hover #aether-cursor-ring {
      opacity: 0.3 !important;
    }

    /* Link / button hover state */
    .aether-interactive-hover #aether-cursor-dot {
      width: ${T.dotSize * T.hoverDotScale * 2}px !important;
      height: ${T.dotSize * T.hoverDotScale * 2}px !important;
      background: ${T.hoverDotColor} !important;
      box-shadow: 0 0 18px 4px rgba(${T.glowColor}, 0.8) !important;
    }
    .aether-interactive-hover #aether-cursor-ring {
      width:  ${T.ringSize * T.hoverRingScale}px !important;
      height: ${T.ringSize * T.hoverRingScale}px !important;
      background: ${T.hoverRingColor} !important;
      border: ${T.hoverRingBorder} !important;
      box-shadow: 0 0 20px rgba(${T.glowColor}, 0.25),
                  inset 0 0 20px rgba(${T.glowColor}, 0.08) !important;
    }

    /* Draggable hover */
    .aether-drag-hover #aether-cursor-dot {
      background: rgba(255,255,255,0.9) !important;
      box-shadow: 0 0 12px rgba(255,255,255,0.5) !important;
    }
    .aether-drag-hover #aether-cursor-ring {
      width: ${T.ringSize * 1.6}px !important;
      height: ${T.ringSize * 1.6}px !important;
      border-style: dashed !important;
      border-color: rgba(255,255,255,0.5) !important;
    }

    /* Hidden when outside window */
    .aether-hidden #aether-cursor-dot,
    .aether-hidden #aether-cursor-ring {
      opacity: 0 !important;
    }

    /* Particles (hero page) */
    .aether-particle {
      position: fixed;
      pointer-events: none;
      z-index: 2147483645;
      border-radius: 50%;
      will-change: transform, opacity;
      backface-visibility: hidden;
    }
  `;
  // Append to body so it loads AFTER any <style> blocks inside <body> (e.g. scroll-progress-style)
  // This guarantees our cursor:none !important wins the CSS source-order cascade
  function injectCursorStyle() {
    (document.body || document.documentElement).appendChild(styleEl);
  }
  if (document.body) {
    injectCursorStyle();
  } else {
    document.addEventListener('DOMContentLoaded', injectCursorStyle);
  }

  // ── 4b. Inline-cursor suppressor ──────────────────────────────────────────
  // Some pages (github, leetcode) set cursor:pointer via element.style.cssText
  // in JS-generated elements. CSS !important can't override inline styles, so
  // we use a MutationObserver to strip inline cursor values as they are set.
  function stripInlineCursor(el) {
    if (el && el.style && el.style.cursor && el.id !== 'aether-cursor-dot' && el.id !== 'aether-cursor-ring') {
      el.style.cursor = '';
    }
  }

  const inlineCursorObserver = new MutationObserver(function (mutations) {
    for (const m of mutations) {
      if (m.type === 'attributes' && m.attributeName === 'style') {
        stripInlineCursor(m.target);
      }
      if (m.type === 'childList') {
        for (const node of m.addedNodes) {
          if (node.nodeType === 1) {
            stripInlineCursor(node);
            // Check children too (e.g., bulk-generated grids)
            node.querySelectorAll && node.querySelectorAll('[style*="cursor"]').forEach(stripInlineCursor);
          }
        }
      }
    }
  });

  // Start observing once DOM is ready
  function startObserver() {
    inlineCursorObserver.observe(document.body, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ['style'],
    });
    // Also sweep any elements already in the DOM with inline cursor
    document.querySelectorAll('[style*="cursor"]').forEach(stripInlineCursor);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', startObserver);
  } else {
    startObserver();
    // Sweep again after a short delay for JS-rendered content (heatmaps etc.)
    setTimeout(() => document.querySelectorAll('[style*="cursor"]').forEach(stripInlineCursor), 800);
    setTimeout(() => document.querySelectorAll('[style*="cursor"]').forEach(stripInlineCursor), 2000);
  }

  // ── 5. Create DOM elements ─────────────────────────────────────────────────
  const dot  = document.createElement('div');
  const ring = document.createElement('div');
  dot.id  = 'aether-cursor-dot';
  ring.id = 'aether-cursor-ring';
  document.body.appendChild(ring);
  document.body.appendChild(dot);

  // Trail dots
  const trails = [];
  for (let i = 0; i < T.trailCount; i++) {
    const t = document.createElement('div');
    t.className = 'aether-trail';
    const alpha = 0.45 - i * (0.35 / T.trailCount);
    const size  = 5 - i * (3 / T.trailCount);
    t.style.cssText = `
      background: ${T.trailColor} ${alpha.toFixed(2)});
      width: ${size.toFixed(1)}px;
      height: ${size.toFixed(1)}px;
      transition: opacity 0.2s ease;
    `;
    document.body.appendChild(t);
    trails.push({ el: t, x: 0, y: 0 });
  }

  // ── 6. State ───────────────────────────────────────────────────────────────
  let mouseX = -200, mouseY = -200;
  let dotX   = -200, dotY   = -200;
  let ringX  = -200, ringY  = -200;
  let isHidden = true;

  // ── 7. Smooth animation loop ───────────────────────────────────────────────
  function lerp(a, b, f) { return a + (b - a) * f; }

  let lastRaf = 0;
  function animate(ts) {
    if (ts - lastRaf >= 14) { // ~70fps cap to save battery beyond 60
      lastRaf = ts;

      dotX  = lerp(dotX,  mouseX, 0.92);
      dotY  = lerp(dotY,  mouseY, 0.92);
      ringX = lerp(ringX, mouseX, 0.18);
      ringY = lerp(ringY, mouseY, 0.18);

      // Apply to dot (near-instant)
      dot.style.transform  = `translate(calc(-50% + ${dotX}px), calc(-50% + ${dotY}px))`;
      ring.style.transform = `translate(calc(-50% + ${ringX}px), calc(-50% + ${ringY}px))`;

      // Vault/Solve ring have own CSS rotation transforms — we work around it
      if (PAGE === 'vault' || PAGE === 'solve') {
        ring.style.left = ringX + 'px';
        ring.style.top  = ringY + 'px';
        ring.style.transform = 'translate(-50%, -50%)'; // keep CSS anim working
      }

      // Trail positions — each follows the next
      let prevX = dotX, prevY = dotY;
      for (let i = 0; i < trails.length; i++) {
        const t = trails[i];
        t.x = lerp(t.x, prevX, 0.55 - i * 0.07);
        t.y = lerp(t.y, prevY, 0.55 - i * 0.07);
        t.el.style.transform = `translate(calc(-50% + ${t.x}px), calc(-50% + ${t.y}px))`;
        prevX = t.x;
        prevY = t.y;
      }
    }
    requestAnimationFrame(animate);
  }
  requestAnimationFrame(animate);

  // ── 8. Mouse tracking ─────────────────────────────────────────────────────
  document.addEventListener('mousemove', function (e) {
    mouseX = e.clientX;
    mouseY = e.clientY;

    if (isHidden) {
      // First move: snap into position
      dotX = ringX = mouseX;
      dotY = ringY = mouseY;
      for (const t of trails) { t.x = mouseX; t.y = mouseY; }
      document.body.classList.remove('aether-hidden');
      isHidden = false;
    }
  }, { passive: true });

  document.addEventListener('mouseleave', function () {
    document.body.classList.add('aether-hidden');
    isHidden = true;
  });

  document.addEventListener('mouseenter', function () {
    document.body.classList.remove('aether-hidden');
    isHidden = false;
  });

  // ── 9. Interaction detection ───────────────────────────────────────────────
  const INTERACTIVE_SEL = [
    'a', 'button', 'label', '[role="button"]', '[role="link"]',
    '[role="tab"]', '[role="menuitem"]', '.magnetic-btn', '.magnetic-effect',
    '.glass-card', '.glass-panel', '.cert-row', '.project-hover-trigger',
    '[onclick]', '.cursor-pointer', 'summary', '.h-cell'
  ].join(',');

  const TEXT_SEL = 'p, h1, h2, h3, h4, h5, h6, span, li, blockquote, td, th, [data-cursor="text"]';
  const DRAG_SEL = '[draggable="true"], input[type="range"]';
  const INPUT_SEL = 'input:not([type="range"]), textarea, select, [contenteditable]';

  function getClosestMatch(el, sel) {
    return el && (el.matches(sel) ? el : el.closest(sel));
  }

  document.addEventListener('mouseover', function (e) {
    const target = e.target;

    // Priority: input → drag → interactive → text → default
    if (getClosestMatch(target, INPUT_SEL)) {
      clearHoverStates();
      // Text cursor is handled purely by CSS cursor:text override
      return;
    }
    if (getClosestMatch(target, DRAG_SEL)) {
      clearHoverStates();
      document.body.classList.add('aether-drag-hover');
      return;
    }
    if (getClosestMatch(target, INTERACTIVE_SEL)) {
      clearHoverStates();
      document.body.classList.add('aether-interactive-hover');
      spawnParticles(mouseX, mouseY, 3);
      return;
    }
    if (getClosestMatch(target, TEXT_SEL)) {
      clearHoverStates();
      document.body.classList.add('aether-text-hover');
      return;
    }
    clearHoverStates();
  }, { passive: true });

  function clearHoverStates() {
    document.body.classList.remove(
      'aether-interactive-hover',
      'aether-text-hover',
      'aether-drag-hover'
    );
  }

  // ── 10. Click animation ────────────────────────────────────────────────────
  document.addEventListener('mousedown', function () {
    document.body.classList.add('aether-clicking');
    spawnParticles(mouseX, mouseY, PAGE === 'forge' ? 6 : 4);
  });
  document.addEventListener('mouseup', function () {
    document.body.classList.remove('aether-clicking');
  });

  // ── 11. Particle burst system ──────────────────────────────────────────────
  const particlePool = [];

  function getParticle() {
    if (particlePool.length > 0) return particlePool.pop();
    const p = document.createElement('div');
    p.className = 'aether-particle';
    document.body.appendChild(p);
    return p;
  }

  function releaseParticle(p) {
    p.style.opacity = '0';
    particlePool.push(p);
  }

  function spawnParticles(x, y, count) {
    // Throttle: only on interaction, not text
    if (document.body.classList.contains('aether-text-hover')) return;

    const colors = {
      hero:  ['rgba(196,192,255,0.9)', 'rgba(168,85,247,0.8)', 'rgba(255,255,255,0.7)'],
      forge: ['rgba(240,83,28,0.9)',   'rgba(255,160,60,0.8)',  'rgba(255,255,255,0.6)'],
      vault: ['rgba(221,183,255,0.9)', 'rgba(183,109,255,0.8)','rgba(255,215,0,0.7)'],
      code:  ['rgba(94,174,234,0.9)',  'rgba(196,192,255,0.7)','rgba(255,255,255,0.5)'],
      solve: ['rgba(255,161,22,0.9)',  'rgba(255,220,100,0.8)','rgba(240,83,28,0.6)'],
    }[PAGE];

    for (let i = 0; i < count; i++) {
      const p     = getParticle();
      const size  = 3 + Math.random() * 5;
      const angle = Math.random() * Math.PI * 2;
      const dist  = 20 + Math.random() * 45;
      const dur   = 400 + Math.random() * 400;
      const color = colors[Math.floor(Math.random() * colors.length)];

      p.style.cssText = `
        left: ${x}px;
        top:  ${y}px;
        width:  ${size}px;
        height: ${size}px;
        background: ${color};
        box-shadow: 0 0 ${size}px ${color};
        opacity: 1;
        transition: transform ${dur}ms cubic-bezier(0,0.9,0.57,1),
                    opacity   ${dur}ms ease-out;
        transform: translate(-50%, -50%);
      `;

      // Force reflow before adding transition
      void p.offsetWidth;

      const tx = Math.cos(angle) * dist;
      const ty = Math.sin(angle) * dist;
      p.style.transform  = `translate(calc(-50% + ${tx}px), calc(-50% + ${ty}px))`;
      p.style.opacity    = '0';

      setTimeout(() => releaseParticle(p), dur + 50);
    }
  }

  // ── 12. Magnetic effect on nav items ──────────────────────────────────────
  // Subtly shifts ring toward interactive elements for a magnetic feel
  // (purely visual — no DOM restructuring)
  let magnetTarget = null;
  let magnetRAF    = null;

  document.addEventListener('mouseover', function (e) {
    const magEl = getClosestMatch(e.target, 'a, button, .magnetic-btn, .magnetic-effect');
    if (magEl) {
      magnetTarget = magEl;
    } else {
      magnetTarget = null;
    }
  }, { passive: true });

  // The actual magnetic pull is handled via ring lerp — its slower factor
  // naturally produces a lag that makes it appear magnetically attracted.
  // No additional logic needed.

  // ── 13. Page-specific decoration ──────────────────────────────────────────
  // HERO: Ambient glow that follows (already handled by ring)
  // CODE: Append < > decorators on ring hover text
  if (PAGE === 'code') {
    const codeRingLabel = document.createElement('div');
    codeRingLabel.id = 'aether-code-label';
    codeRingLabel.style.cssText = `
      position: fixed;
      top: 0; left: 0;
      pointer-events: none;
      z-index: 2147483647;
      font-family: 'Space Mono', monospace;
      font-size: 8px;
      color: rgba(94, 174, 234, 0.7);
      opacity: 0;
      transition: opacity 0.25s ease;
      white-space: nowrap;
      will-change: transform;
      line-height: 1;
    `;
    document.body.appendChild(codeRingLabel);

    document.addEventListener('mouseover', function (e) {
      if (getClosestMatch(e.target, INTERACTIVE_SEL)) {
        codeRingLabel.style.opacity = '0.9';
        codeRingLabel.textContent = '{ }';
      } else {
        codeRingLabel.style.opacity = '0';
      }
    }, { passive: true });

    // Sync label to ring position inside the RAF
    const origAnimate = window.__aetherRaf;
    let labelX = -200, labelY = -200;
    function animateCodeLabel() {
      labelX = lerp(labelX, mouseX, 0.18);
      labelY = lerp(labelY, mouseY, 0.18);
      codeRingLabel.style.transform = `translate(calc(-50% + ${labelX}px), calc(-50% + ${labelY - T.ringSize / 2 - 14}px))`;
      requestAnimationFrame(animateCodeLabel);
    }
    requestAnimationFrame(animateCodeLabel);
  }

  // SOLVE: Show tiny progress indicator around ring
  if (PAGE === 'solve') {
    // The spinning dashed ring is handled by CSS; no extra DOM needed.
    // Add a second inner solid ring for depth:
    const innerRing = document.createElement('div');
    innerRing.id = 'aether-solve-inner';
    innerRing.style.cssText = `
      position: fixed;
      top: 0; left: 0;
      width: 18px; height: 18px;
      border-radius: 50%;
      border: 1px solid rgba(255, 161, 22, 0.4);
      pointer-events: none;
      z-index: 2147483647;
      will-change: transform;
      transform: translate(-50%, -50%);
      box-shadow: 0 0 8px rgba(255,161,22,0.3);
      transition: width 0.3s ease, height 0.3s ease, opacity 0.2s ease;
    `;
    document.body.appendChild(innerRing);

    let irX = -200, irY = -200;
    function animateSolveInner() {
      irX = lerp(irX, mouseX, 0.35);
      irY = lerp(irY, mouseY, 0.35);
      innerRing.style.left = irX + 'px';
      innerRing.style.top  = irY + 'px';
      requestAnimationFrame(animateSolveInner);
    }
    requestAnimationFrame(animateSolveInner);
  }

  // FORGE: Show spark lines on interactive hover
  if (PAGE === 'forge') {
    const forgeH = document.createElement('div');
    const forgeV = document.createElement('div');
    [forgeH, forgeV].forEach((line, i) => {
      line.style.cssText = `
        position: fixed;
        top: 0; left: 0;
        pointer-events: none;
        z-index: 2147483646;
        background: rgba(240, 83, 28, 0.22);
        will-change: transform, opacity;
        opacity: 0;
        transition: opacity 0.2s ease;
        ${i === 0
          ? 'width: 1px; height: 100vh;'
          : 'height: 1px; width: 100vw;'
        }
      `;
      document.body.appendChild(line);
    });

    document.addEventListener('mouseover', function (e) {
      const show = !!getClosestMatch(e.target, INTERACTIVE_SEL);
      forgeH.style.opacity = show ? '1' : '0';
      forgeV.style.opacity = show ? '1' : '0';
    }, { passive: true });

    let fhX = -1, fvY = -1;
    function animateForgeLines() {
      fhX = lerp(fhX, mouseX, 0.15);
      fvY = lerp(fvY, mouseY, 0.15);
      forgeH.style.transform = `translateX(${fhX}px)`;
      forgeV.style.transform = `translateY(${fvY}px)`;
      requestAnimationFrame(animateForgeLines);
    }
    requestAnimationFrame(animateForgeLines);
  }

  // VAULT: Shimmer trail (already handled by trail system; add gold tint)
  // No extra DOM needed.

  // HERO: Ambient orb ripple on interactive hover
  if (PAGE === 'hero') {
    const heroOrb = document.createElement('div');
    heroOrb.id = 'aether-hero-orb';
    heroOrb.style.cssText = `
      position: fixed;
      top: 0; left: 0;
      width: 80px; height: 80px;
      border-radius: 50%;
      pointer-events: none;
      z-index: 2147483645;
      background: radial-gradient(circle, rgba(108,99,255,0.12) 0%, rgba(108,99,255,0) 70%);
      will-change: transform, opacity;
      opacity: 0;
      transition: opacity 0.4s ease;
      transform: translate(-50%, -50%);
    `;
    document.body.appendChild(heroOrb);

    document.addEventListener('mouseover', function (e) {
      heroOrb.style.opacity = getClosestMatch(e.target, INTERACTIVE_SEL) ? '1' : '0';
    }, { passive: true });

    let hOrbX = -200, hOrbY = -200;
    function animateHeroOrb() {
      hOrbX = lerp(hOrbX, mouseX, 0.08);
      hOrbY = lerp(hOrbY, mouseY, 0.08);
      heroOrb.style.transform = `translate(calc(-50% + ${hOrbX}px), calc(-50% + ${hOrbY}px))`;
      requestAnimationFrame(animateHeroOrb);
    }
    requestAnimationFrame(animateHeroOrb);
  }

  // ── 14. Hide initially ─────────────────────────────────────────────────────
  document.body.classList.add('aether-hidden');

})();
