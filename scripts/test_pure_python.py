# -*- coding: utf-8 -*-
with open('reloaded-source/Act II - The Shadowed Town/Arc E - The Missing Vistana.md', encoding='utf-8') as f:
    text = f.read()
import re
m = re.search(r'^#{1,3}\s+E4\.\s+([^\n]+)', text, re.MULTILINE)
print("Result in python script:", m)
if m:
    print("Matched:", m.group(0))
