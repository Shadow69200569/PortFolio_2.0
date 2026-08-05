import re

with open('projects.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add loader HTML to the preview card
preview_card_pattern = r'(<div id="project-preview-card"[^>]*>)\s*<video id="project-preview-video" src="" autoplay loop muted playsinline class="w-full\s*h-full object-cover"></video>'

preview_card_replacement = r'''\1
      <div id="project-preview-loader" class="absolute inset-0 flex items-center justify-center text-primary opacity-0 transition-opacity duration-300 z-10 bg-[#0a0a0f]">
        <svg class="animate-spin h-8 w-8" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
      </div>
      <video id="project-preview-video" src="" autoplay loop muted playsinline class="w-full h-full object-cover transition-opacity duration-300 opacity-0 relative z-20"></video>'''

new_content = re.sub(preview_card_pattern, preview_card_replacement, content)

# 2. Update the javascript
js_pattern = r'''(triggers\.forEach\(trigger => \{\s*trigger\.addEventListener\('mouseenter', function\(\) \{\s*isHovering = true;\s*)(previewVideo\.src = this\.dataset\.video;\s*previewVideo\.play\(\);)'''

js_replacement = r'''\1const videoSrc = this.dataset.video;
          const loader = document.getElementById('project-preview-loader');
          
          if (previewVideo.getAttribute('src') !== videoSrc) {
            previewVideo.style.opacity = '0';
            loader.style.opacity = '1';
            previewVideo.src = videoSrc;
            
            previewVideo.oncanplay = () => {
              if (isHovering && previewVideo.getAttribute('src') === videoSrc) {
                previewVideo.style.opacity = '1';
                loader.style.opacity = '0';
                previewVideo.play().catch(e => console.log(e));
              }
            };
          } else {
            previewVideo.style.opacity = '1';
            loader.style.opacity = '0';
            previewVideo.play().catch(e => console.log(e));
          }'''

new_content = re.sub(js_pattern, js_replacement, new_content)

# 3. Ensure previewContainer shows correctly
# In the original JS: previewContainer.style.opacity = '1'; was present. We need to make sure we didn't override anything else.

with open('projects.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("projects.html updated")
