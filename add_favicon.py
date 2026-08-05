import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if favicon already exists
    if 'rel="icon"' in content or 'rel="shortcut icon"' in content:
        # Replace existing favicon link
        new_content = re.sub(
            r'<link[^>]*rel="(?:shortcut )?icon"[^>]*>',
            r'<link rel="icon" type="image/jpeg" href="favicon.jpg">',
            content
        )
    else:
        # Insert before closing </head>
        new_content = re.sub(
            r'</head>',
            r'  <link rel="icon" type="image/jpeg" href="favicon.jpg">\n</head>',
            content
        )
        
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")
