import codecs

with codecs.open('d:\\portfolio_2.0\\certificates.html', 'r', 'utf-8') as f:
    lines = f.readlines()

new_script = '''<!-- Certificates Custom Script -->
<script>
// --- CERTIFICATES DATA ---
const certificatesData = [
  {
    title: "Advanced AI Architecture",
    org: "DeepLearning.AI",
    date: "Aug 2025",
    tag: "AI & ML",
    url: "assets/cert_ai.jpg" 
  },
  {
    title: "Cloud Solutions Architect",
    org: "Amazon Web Services",
    date: "May 2025",
    tag: "Cloud",
    url: "assets/cert_cloud.jpg"
  },
  {
    title: "Full Stack Web Development",
    org: "Oracle",
    date: "Dec 2024",
    tag: "Software Engineering",
    url: "assets/cert_web.jpg"
  },
  {
    title: "Cybersecurity Specialist",
    org: "CompTIA",
    date: "Oct 2024",
    tag: "Security",
    url: "assets/cert_security.jpg"
  }
];

document.addEventListener('DOMContentLoaded', () => {
  const listContainer = document.getElementById('certificates-list');
  const previewContainer = document.getElementById('cert-preview-container');
  const previewCard = document.getElementById('cert-preview-card');
  const previewImage = document.getElementById('cert-preview-image');
  
  const modal = document.getElementById('cert-modal');
  const modalImage = document.getElementById('cert-modal-image');
  const modalTitle = document.getElementById('cert-modal-title');
  const modalOrg = document.getElementById('cert-modal-org');
  const modalDate = document.getElementById('cert-modal-date');
  const modalClose = document.getElementById('cert-modal-close');
  const modalNext = document.getElementById('cert-modal-next');
  const modalPrev = document.getElementById('cert-modal-prev');

  let currentModalIndex = 0;
  
  // Render List
  certificatesData.forEach((cert, index) => {
    const row = document.createElement('div');
    row.className = 'group relative flex flex-col md:flex-row md:items-center justify-between p-6 bg-[#0a0a14]/60 border border-white/5 rounded-2xl hover:border-primary/40 transition-all duration-300 cursor-pointer overflow-hidden';
    row.dataset.index = index;
    
    const hoverBg = document.createElement('div');
    hoverBg.className = 'absolute inset-0 bg-gradient-to-r from-primary/0 via-primary/5 to-primary/0 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-1000';
    row.appendChild(hoverBg);
    
    const leftContent = document.createElement('div');
    leftContent.className = 'relative z-10 flex-1';
    leftContent.innerHTML = 
      <h3 class="font-headline-md text-xl md:text-2xl text-text-high group-hover:text-primary group-hover:scale-[1.01] transition-all duration-300 origin-left"> + "$" + {cert.title}</h3>
      <div class="flex items-center gap-4 mt-2 font-label-mono text-xs uppercase tracking-widest text-text-low group-hover:text-text-high transition-colors">
        <span> + "$" + {cert.org}</span>
        <span class="w-1 h-1 rounded-full bg-glass-border"></span>
        <span> + "$" + {cert.date}</span>
      </div>
    ;
    
    const rightContent = document.createElement('div');
    rightContent.className = 'relative z-10 mt-4 md:mt-0 flex items-center gap-4';
    rightContent.innerHTML = 
      <span class="px-4 py-1.5 rounded-full border border-glass-border bg-glass-bg text-xs font-label-mono text-text-low group-hover:border-primary/50 group-hover:text-primary transition-colors"> + "$" + {cert.tag}</span>
      <span class="material-symbols-outlined text-text-low group-hover:text-primary group-hover:translate-x-1 transition-all duration-300 hidden md:block">arrow_forward</span>
    ;
    
    row.appendChild(leftContent);
    row.appendChild(rightContent);
    listContainer.appendChild(row);

    const img = new Image();
    img.src = cert.url;

    row.addEventListener('mouseenter', () => {
      if (window.innerWidth < 768) return; 
      previewImage.src = cert.url;
      previewContainer.style.opacity = '1';
      previewImage.style.opacity = '1';
    });
    
    row.addEventListener('mouseleave', () => {
      previewContainer.style.opacity = '0';
    });
    
    row.addEventListener('click', () => {
      openModal(index);
    });
  });

  let targetX = 0, targetY = 0;
  let currentX = 0, currentY = 0;
  let isHoveringList = false;

  listContainer.addEventListener('mouseenter', () => { isHoveringList = true; });
  listContainer.addEventListener('mouseleave', () => { isHoveringList = false; });
  
  document.addEventListener('mousemove', (e) => {
    targetX = e.clientX;
    targetY = e.clientY;
  });

  function renderPreviewPhysics() {
    if (isHoveringList && window.innerWidth >= 768) {
      currentX += (targetX - currentX) * 0.15;
      currentY += (targetY - currentY) * 0.15;
      
      let xOffset = 20;
      let yOffset = 20;
      
      const cardWidth = 420;
      const cardHeight = 315; 
      
      if (currentX + xOffset + cardWidth > window.innerWidth) {
        xOffset = -cardWidth - 20;
      }
      if (currentY + yOffset + cardHeight > window.innerHeight) {
        yOffset = -cardHeight - 20;
      }

      previewContainer.style.transform = 	ranslate3d( + "$" + {currentX + xOffset}px,  + "$" + {currentY + yOffset}px, 0);
      
      const deltaX = targetX - currentX;
      const deltaY = targetY - currentY;
      
      const rotateX = Math.max(-20, Math.min(20, deltaY * -0.1));
      const rotateY = Math.max(-20, Math.min(20, deltaX * 0.1));
      
      previewCard.style.transform = perspective(1000px) rotateX( + "$" + {rotateX}deg) rotateY( + "$" + {rotateY}deg) scale3d(1, 1, 1);
    }
    requestAnimationFrame(renderPreviewPhysics);
  }
  requestAnimationFrame(renderPreviewPhysics);

  function openModal(index) {
    currentModalIndex = index;
    updateModalContent();
    modal.classList.remove('pointer-events-none');
    modal.style.opacity = '1';
    setTimeout(() => {
      modalImage.style.transform = 'scale(1)';
      modalImage.style.opacity = '1';
    }, 50);
  }

  function closeModal() {
    modal.style.opacity = '0';
    modal.classList.add('pointer-events-none');
    modalImage.style.transform = 'scale(0.95)';
    modalImage.style.opacity = '0';
  }

  function updateModalContent() {
    const cert = certificatesData[currentModalIndex];
    modalImage.style.opacity = '0';
    setTimeout(() => {
      modalImage.src = cert.url;
      modalImage.style.opacity = '1';
      modalTitle.textContent = cert.title;
      modalOrg.textContent = cert.org;
      modalDate.textContent = cert.date;
    }, 300);
  }

  function nextModal() {
    currentModalIndex = (currentModalIndex + 1) % certificatesData.length;
    updateModalContent();
  }

  function prevModal() {
    currentModalIndex = (currentModalIndex - 1 + certificatesData.length) % certificatesData.length;
    updateModalContent();
  }

  modalClose.addEventListener('click', closeModal);
  modalNext.addEventListener('click', nextModal);
  modalPrev.addEventListener('click', prevModal);
  
  modal.addEventListener('click', (e) => {
    if (e.target === modal || e.target.closest('.flex-grow') === e.target) {
        closeModal();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (modal.style.opacity === '1') {
      if (e.key === 'Escape') closeModal();
      if (e.key === 'ArrowRight') nextModal();
      if (e.key === 'ArrowLeft') prevModal();
    }
  });
});
</script>
'''

with codecs.open('d:\\portfolio_2.0\\certificates.html', 'w', 'utf-8') as f:
    f.writelines(lines[:424])
    f.write(new_script)
    f.writelines(lines[641:])
