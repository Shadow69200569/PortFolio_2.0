import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

# We'll use simple string replacement instead of complex regex
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Replace the anchor tag opening
    new_content = re.sub(
        r'<a style="font-family:\'Space Mono\',monospace;font-size:11px;color:rgba\(255,255,255,0\.5\);text-decoration:none;transition:color \.3s;" onmouseover="this\.style\.color=\'#fff\'" onmouseout="this\.style\.color=\'rgba\(255,255,255,0\.5\)\'"',
        r'<a class="font-label-mono text-[11px] text-text-low hover:text-text-high transition-colors duration-300"',
        content
    )
    
    # 2. Replace the span
    new_content = re.sub(
        r'<span style="font-family:\'Space Mono\',monospace;font-size:10px;letter-spacing:0\.1em;color:rgba\(255,255,255,0\.4\);">',
        r'<span class="font-label-mono text-[10px] tracking-widest text-text-low opacity-70">',
        new_content
    )

    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
