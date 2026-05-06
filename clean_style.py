import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the absolute positioning hack at the end
content = re.sub(r'@media\s*\(\s*max-width:\s*1199px\s*\)\s*\{\s*\.main-header-style1__content-bottom-left\s*\{\s*position:\s*relative\s*!important;\s*\}\s*\.mobile-nav__toggler\s*\{\s*position:\s*absolute\s*!important;\s*right:\s*30px\s*!important;\s*top:\s*50%\s*!important;\s*transform:\s*translateY\(-50%\)\s*!important;\s*margin:\s*0\s*!important;\s*\}\s*\}', '', content, flags=re.MULTILINE)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(content)
