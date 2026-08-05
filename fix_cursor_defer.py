files = [
    'd:/portfolio_2.0/github.html',
    'd:/portfolio_2.0/leetcode.html',
    'd:/portfolio_2.0/certificates.html',
    'd:/portfolio_2.0/index.html',
    'd:/portfolio_2.0/projects.html',
]
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    old = 'src="cursor.js" defer'
    new_tag = 'src="cursor.js"'
    updated = c.replace(old, new_tag)
    if updated != c:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(updated)
        print('Updated', f.split('/')[-1])
    else:
        print('No change in', f.split('/')[-1])
