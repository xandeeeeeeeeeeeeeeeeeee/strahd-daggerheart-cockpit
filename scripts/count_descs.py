import glob
import re

files = glob.glob('reloaded-source/**/*.md', recursive=True)
total_descs = 0
by_file = {}
for f in files:
    content = open(f, 'r', encoding='utf-8').read()
    descs = re.findall(r'<div class=["\']?description["\']?[^>]*>([\s\S]*?)</div>', content)
    if descs:
        total_descs += len(descs)
        by_file[f] = len(descs)

print(f"Total description boxes: {total_descs}")
for f, count in sorted(by_file.items(), key=lambda x: -x[1])[:15]:
    print(f"  {f.replace('reloaded-source\\\\', '')}: {count}")
