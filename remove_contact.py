import re

files = [
    'd:/portfolio_2.0/index.html',
    'd:/portfolio_2.0/projects.html',
    'd:/portfolio_2.0/certificates.html',
    'd:/portfolio_2.0/github.html',
    'd:/portfolio_2.0/leetcode.html',
]

# Patterns for desktop and mobile nav contact links (exact variations found)
patterns = [
    # index.html desktop nav
    r'\s*<a class="font-body-md text-body-md text-text-low hover:text-text-high hover:bg-white/5 transition-all duration-300 px-4 py-2 rounded-full magnetic-effect active:scale-95" href="#contact">Contact</a>',
    # index.html mobile nav
    r'\s*<a class="font-body-md text-body-md text-text-low py-2 hover:text-text-high" href="#contact">Contact</a>',
    # projects/certificates desktop nav
    r'\s*<a class="font-body-md text-body-md text-text-low hover:text-text-high hover:bg-white/5 transition-all duration-300 px-4 py-2 rounded-full" href="index\.html#contact">Contact</a>',
    # projects mobile nav
    r'\s*<a class="font-body-md text-text-low py-2 hover:text-text-high" href="index\.html#contact">Contact</a>',
    # github/leetcode desktop nav
    r'\s*<a class="text-text-low hover:text-text-high hover:bg-white/5 transition-all px-4 py-2 rounded-full text-sm" href="index\.html#contact">Contact</a>',
    # github/leetcode mobile nav
    r'\s*<a class="text-text-low py-2 hover:text-text-high text-sm" href="index\.html#contact">Contact</a>',
    # certificates mobile nav (slightly different class)
    r'\s*<a class="font-body-md text-text-low py-2 hover:text-text-high" href="index\.html#contact">Contact</a>',
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    for p in patterns:
        content = re.sub(p, '', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  OK   {filepath.split("/")[-1]}')
    else:
        print(f'  SKIP {filepath.split("/")[-1]} (no change)')
