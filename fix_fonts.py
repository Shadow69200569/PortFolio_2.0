import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

pattern = r'<a style="font-family:''Space Mono'',monospace;font-size:11px;color:rgba\(255,255,255,0\.5\);text-decoration:none;transition:color \.3s;" onmouseover="this\.style\.color=''#fff''" onmouseout="this\.style\.color=''rgba\(255,255,255,0\.5\)''" (href="[^"]*"(?: target="_blank" rel="noopener")?)>([^<]+)</a>'

replacement = r'<a class="font-label-mono text-[11px] text-text-low hover:text-text-high transition-colors duration-300" \1>\2</a>'

span_pattern = r'<span style="font-family:''Space Mono'',monospace;font-size:10px;letter-spacing:0\.1em;color:rgba\(255,255,255,0\.4\);">(.*?)</span>'
span_replacement = r'<span class="font-label-mono text-[10px] tracking-widest text-text-low opacity-70">\1</span>'

div_pattern = r'<div style="font-family:''Space Mono'',monospace;font-size:10px;color:rgba\(255,255,255,0\.4\);text-transform:uppercase;letter-spacing:0\.05em;">(.*?)</div>'
div_replacement = r'<div class="font-label-mono text-[10px] text-text-low opacity-70 uppercase tracking-wider">\1</div>'

div2_pattern = r'<div style="font-family:''Space Mono'',monospace;font-size:10px;color:rgba\(255,255,255,0\.3\);margin-bottom:24px; flex-grow: 1;">(.*?)</div>'
div2_replacement = r'<div class="font-label-mono text-[10px] text-text-low opacity-50 mb-6 flex-grow">\1</div>'

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = re.sub(pattern, replacement, content)
    new_content = re.sub(span_pattern, span_replacement, new_content)
    new_content = re.sub(div_pattern, div_replacement, new_content)
    new_content = re.sub(div2_pattern, div2_replacement, new_content)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
