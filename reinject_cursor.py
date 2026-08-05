"""
Move cursor.js script inside </body> on pages where it ended up after </body>
Also ensure the script tag is the VERY LAST thing inside </body>
"""
files = [
    'd:/portfolio_2.0/github.html',
    'd:/portfolio_2.0/leetcode.html',
    'd:/portfolio_2.0/certificates.html',
    'd:/portfolio_2.0/index.html',
    'd:/portfolio_2.0/projects.html',
]

cursor_block = '\n<!-- Aether Custom Cursor System -->\n<script src="cursor.js"></script>\n'

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()

    # Remove ALL existing cursor.js injections (wherever they are)
    c = c.replace('<!-- Aether Custom Cursor System -->\n<script src="cursor.js"></script>\n', '')
    c = c.replace('<!-- Aether Custom Cursor System -->\n<script src="cursor.js" defer></script>\n', '')
    c = c.replace('\n<!-- Aether Custom Cursor System -->\n<script src="cursor.js"></script>', '')
    c = c.replace('\n<!-- Aether Custom Cursor System -->\n<script src="cursor.js" defer></script>', '')
    
    # Now inject it as the very last thing before </body> if present
    if '</body>' in c:
        c = c.replace('</body>', cursor_block + '</body>', 1)
        print(f'  OK (before </body>): {f.split("/")[-1]}')
    elif '</html>' in c:
        c = c.replace('</html>', cursor_block + '</html>', 1)
        print(f'  OK (before </html>): {f.split("/")[-1]}')
    else:
        c = c.rstrip() + cursor_block
        print(f'  OK (appended): {f.split("/")[-1]}')

    with open(f, 'w', encoding='utf-8') as fh:
        fh.write(c)
