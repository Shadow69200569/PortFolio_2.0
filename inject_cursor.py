import os

pages = ['index.html', 'projects.html', 'certificates.html', 'github.html', 'leetcode.html']
base  = 'd:/portfolio_2.0'
sentinel = 'cursor.js'

tag = "\n<!-- Aether Custom Cursor System -->\n<script src=\"cursor.js\" defer></script>\n"

for page in pages:
    path = os.path.join(base, page)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if sentinel in content:
        print(f'  SKIP {page} (already injected)')
        continue

    new_content = content.replace('</body>', tag + '</body>', 1)
    if new_content == content:
        print(f'  WARN {page}: </body> not found!')
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'  OK   {page}')
