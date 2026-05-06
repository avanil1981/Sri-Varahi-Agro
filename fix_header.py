import os
import re

replacement = """      <style>
          /* Improved Header Layout */
          .main-header-style1__content-bottom {
              min-height: 80px;
              display: flex;
              align-items: center;
          }
          .main-header-style1__content-bottom .main-header-style1__content-bottom-left {
              display: flex !important;
              align-items: center !important;
              justify-content: space-between !important;
              width: 100% !important;
              flex: 1 !important;
              padding-right: 24px !important;
          }
          .main-menu.main-menu-style1 {
              margin-left: auto !important;
              margin-right: 0 !important;
          }
          .main-header-style1__content-bottom-right {
              margin-left: 0 !important;
          }
          
          /* Hamburger Menu Styling */
          .mobile-nav__toggler {
              font-size: 26px !important;
              color: #f1b333 !important;
              cursor: pointer;
              transition: all 0.3s ease;
              display: inline-flex;
              align-items: center;
              justify-content: center;
          }
          .mobile-nav__toggler:hover {
              transform: scale(1.1);
              color: #d19a2b !important;
          }
      </style>"""

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find the existing style block
    pattern = re.compile(r'^[ \t]*<style>\s*\.main-header-style1__content-bottom \.main-header-style1__content-bottom-left.*?margin-left: 0 !important;\s*}\s*</style>', re.MULTILINE | re.DOTALL)
    
    new_content, count = pattern.subn(replacement, content)
    
    if count > 0:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"No match found in {file}")
