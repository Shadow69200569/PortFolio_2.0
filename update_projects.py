import re

def update_projects_html():
    filepath = 'd:/portfolio_2.0/projects.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Dictionary of project titles (as they appear in the HTML or close to it) to their new images and videos
    # We will look for the specific block for each project and replace its `.relative.h-48.w-full.overflow-hidden` inner div.
    projects = [
        {
            "id": "Deepfake Forensics",
            "img": "project_images/Deepfake.jpeg",
            "vid": ""
        },
        {
            "id": "Food Order System",
            "img": "project_images/Food_Ordering_System.png",
            "vid": "project_videos/Online_Food_Order_Processing_System.mp4"
        },
        {
            "id": "Endee Vision",
            "img": "project_images/Endee_Vision.png",
            "vid": "project_videos/Endee_Vision.mp4"
        },
        {
            "id": "Blurify AI",
            "img": "project_images/Blurify_AI.png",
            "vid": "project_videos/blurify_AI.mp4"
        },
        {
            "id": "Finance Tracker",
            "img": "project_images/Finance_Tracker.png",
            "vid": "project_videos/Finance_Tracker.mp4"
        },
        {
            "id": "Netflix Clone",
            "img": "project_images/Netflix_Clone.png",
            "vid": "project_videos/Netflix_Clone.mp4"
        }
    ]

    # Update normal projects
    for proj in projects:
        # Regex to find the glass-panel div and add the data-video attribute and class
        # It looks like: <div class="glass-panel rounded-2xl overflow-hidden flex flex-col group hover:border-white/30 transition-all duration-500 reveal...">
        
        # We need to find the specific block for the project. 
        # Best way is to find the title, then backtrack to the nearest `glass-panel`
        
        title_pattern = rf'(<div class="glass-panel[^>]*>)\s*<div class="relative h-48 w-full overflow-hidden">.*?</div>\s*<div class="p-6[^>]*>.*?<h3[^>]*>{proj["id"]}</h3>'
        match = re.search(title_pattern, content, re.DOTALL | re.IGNORECASE)
        
        if match:
            # Reconstruct the HTML
            # Add project-hover-trigger and data-video to the panel
            panel_tag = match.group(1)
            new_panel_tag = panel_tag.replace('class="', 'class="project-hover-trigger ')
            if proj["vid"]:
                new_panel_tag = new_panel_tag[:-1] + f' data-video="{proj["vid"]}">'
            
            # The new media block
            media_block = f'''<div class="relative h-48 w-full overflow-hidden">
          <img src="{proj["img"]}" alt="{proj["id"]}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" />
          <div class="absolute inset-0 bg-gradient-to-t from-surface to-transparent opacity-50"></div>
        </div>'''
            
            # Extract everything from the end of the old media block to the title
            inner_content_pattern = rf'<div class="relative h-48 w-full overflow-hidden">.*?</div>(\s*<div class="p-6[^>]*>.*?<h3[^>]*>{proj["id"]}</h3>)'
            inner_match = re.search(inner_content_pattern, match.group(0), re.DOTALL | re.IGNORECASE)
            
            if inner_match:
                new_block = new_panel_tag + '\n        ' + media_block + inner_match.group(1)
                content = content.replace(match.group(0), new_block)
                print(f"Successfully updated {proj['id']}")
            else:
                print(f"Failed to extract inner content for {proj['id']}")
        else:
            print(f"Could not find project block for {proj['id']}")

    # Update Luxe Bites (Featured Project)
    luxe_pattern = r'(<div class="glass-card[^>]*>)\s*(<div class="w-full lg:w-1/2 relative overflow-hidden">)\s*<img src="https://images.unsplash.com[^"]*" alt="Luxe Bites[^"]*"'
    
    luxe_match = re.search(luxe_pattern, content, re.DOTALL)
    if luxe_match:
        panel_tag = luxe_match.group(1)
        new_panel_tag = panel_tag.replace('class="', 'class="project-hover-trigger ')
        new_panel_tag = new_panel_tag[:-1] + ' data-video="project_videos/Luxe_Bites.mp4">'
        
        media_wrapper = luxe_match.group(2)
        new_img = f'<img src="project_images/Luxe_Bites.png" alt="Luxe Bites e-commerce food platform"'
        
        new_luxe_block = new_panel_tag + '\n      ' + media_wrapper + '\n        ' + new_img
        content = content.replace(luxe_match.group(0), new_luxe_block)
        print("Successfully updated Luxe Bites")
    else:
        print("Could not find Luxe Bites")

    # Add the UI block and script
    if 'project-preview-container' not in content:
        ui_and_script = """
  <!-- Floating Cursor Preview (Hidden by default) -->
  <div id="project-preview-container" class="fixed pointer-events-none z-[100] opacity-0 transition-opacity duration-300 flex items-center justify-center top-0 left-0" style="will-change: transform;">
    <div id="project-preview-card" class="glass-card border border-primary/30 rounded-2xl overflow-hidden shadow-[0_0_40px_rgba(123,97,255,0.4)] relative" style="width: 380px; aspect-ratio: 16/9; transform-style: preserve-3d; will-change: transform;">
      <video id="project-preview-video" src="" autoplay loop muted playsinline class="w-full h-full object-cover"></video>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const previewContainer = document.getElementById('project-preview-container');
      const previewVideo = document.getElementById('project-preview-video');
      const triggers = document.querySelectorAll('.project-hover-trigger');
      
      let mouseX = 0, mouseY = 0;
      let containerX = 0, containerY = 0;
      let isHovering = false;
      let animationFrameId = null;

      function lerp(start, end, factor) {
        return start + (end - start) * factor;
      }

      function animate() {
        if (!isHovering) return;
        containerX = lerp(containerX, mouseX, 0.15);
        containerY = lerp(containerY, mouseY, 0.15);
        
        const tiltX = (mouseX - containerX) * 0.1;
        const tiltY = (containerY - mouseY) * 0.1;

        previewContainer.style.transform = `translate(${containerX}px, ${containerY}px) translate(-50%, -100%) rotateX(${tiltY}deg) rotateY(${tiltX}deg)`;
        
        animationFrameId = requestAnimationFrame(animate);
      }

      triggers.forEach(trigger => {
        trigger.addEventListener('mouseenter', (e) => {
          const videoSrc = trigger.getAttribute('data-video');
          if (!videoSrc) return; 
          
          isHovering = true;
          previewVideo.src = videoSrc;
          previewVideo.play().catch(e => console.log('Video autoplay blocked:', e));
          
          mouseX = e.clientX;
          mouseY = e.clientY - 20;
          containerX = mouseX;
          containerY = mouseY;
          
          previewContainer.style.transform = `translate(${containerX}px, ${containerY}px) translate(-50%, -100%)`;
          previewContainer.classList.remove('opacity-0');
          previewContainer.classList.add('opacity-100');
          
          animate();
        });

        trigger.addEventListener('mousemove', (e) => {
          mouseX = e.clientX;
          mouseY = e.clientY - 20;
        });

        trigger.addEventListener('mouseleave', () => {
          isHovering = false;
          previewContainer.classList.remove('opacity-100');
          previewContainer.classList.add('opacity-0');
          setTimeout(() => {
            if (!isHovering) {
               previewVideo.pause();
               previewVideo.src = '';
            }
          }, 300);
          if (animationFrameId) {
            cancelAnimationFrame(animationFrameId);
          }
        });
      });
    });
  </script>
"""
        content = content.replace('</body>', ui_and_script + '\n</body>')
        print("Successfully added UI and script blocks")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_projects_html()
