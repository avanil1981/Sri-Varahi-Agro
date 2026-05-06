import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add WOW classes to layout columns
    # We use a lambda to avoid double-adding if 'wow' is already in the class
    def replace_col(match):
        class_str = match.group(1)
        if 'wow' not in class_str:
            # We'll use fadeInUp with a generic delay based on the column type to stagger a bit
            delay = "200ms" if "col-xl-4" in class_str else "100ms"
            return f'class="{class_str} wow fadeInUp" data-wow-delay="{delay}"'
        return match.group(0)

    # regex to find class="col-..."
    content = re.sub(r'class="([^"]*col-xl-[468][^"]*)"(?!\s*data-wow)', replace_col, content)
    content = re.sub(r'class="([^"]*col-lg-[46][^"]*)"(?!\s*data-wow)', replace_col, content)
    
    # Also animate section titles
    def replace_title(match):
        class_str = match.group(1)
        if 'wow' not in class_str:
            return f'class="{class_str} wow fadeInDown" data-wow-delay="100ms"'
        return match.group(0)
        
    content = re.sub(r'class="([^"]*sec-title\b[^"]*)"(?!\s*data-wow)', replace_title, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Added scroll animations to {file}")
