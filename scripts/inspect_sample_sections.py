# -*- coding: utf-8 -*-
import re

def inspect_section(filepath, code_regex):
    content = open(filepath, encoding='utf-8').read()
    m = re.search(code_regex, content, re.MULTILINE)
    if not m:
        print(f"Not found: {code_regex} in {filepath}")
        return
    start = m.start()
    # Find next section
    next_m = re.search(r'\n(?=#{1,2}\s+[A-Z0-9]+[a-z]?\.|\Z)', content[start+1:])
    end = start + 1 + next_m.start() if next_m else len(content)
    sec_text = content[start:end]
    print(f"=== {sec_text.splitlines()[0]} ({len(sec_text)} chars) ===")
    lines = [l for l in sec_text.splitlines() if l.strip()]
    print("\n".join(lines[:25]))
    print("...")

inspect_section("reloaded-source/Act I - Into the Mists/Arc C - Into the Valley.md", r'^#\s+C1\.\s+')
inspect_section("reloaded-source/Act II - The Shadowed Town/Arc D - St. Andral\'s Feast.md", r'^#\s+D1\.\s+')
inspect_section("reloaded-source/Act IV - Secrets of the Ancient/Epilogue.md", r'^##\s+1\.\s+')
