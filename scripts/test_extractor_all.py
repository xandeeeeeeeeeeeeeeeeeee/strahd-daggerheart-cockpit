# -*- coding: utf-8 -*-
import json
import glob
import re

data = json.load(open('data/campaign_data.json', encoding='utf-8'))
scenes = data['scenes']

arc_files = {
    'A': 'reloaded-source/Act I - Into the Mists/Arc A - Escape From Death House.md',
    'B': 'reloaded-source/Act I - Into the Mists/Arc B - Welcome to Barovia.md',
    'C': 'reloaded-source/Act I - Into the Mists/Arc C - Into the Valley.md',
    'D': "reloaded-source/Act II - The Shadowed Town/Arc D - St. Andral's Feast.md",
    'E': 'reloaded-source/Act II - The Shadowed Town/Arc E - The Missing Vistana.md',
    'F': "reloaded-source/Act II - The Shadowed Town/Arc F - Lady Wachter's Wish.md",
    'G': 'reloaded-source/Act II - The Shadowed Town/Arc G - The Strazni Siblings.md',
    'H': 'reloaded-source/Act II - The Shadowed Town/Arc H - The Lost Soul.md',
    'I': 'reloaded-source/Act II - The Shadowed Town/Arc I - The Walls of Krezk.md',
    'J': 'reloaded-source/Act III - The Broken Land/Arc J - The Stolen Gem.md',
    'K': 'reloaded-source/Act III - The Broken Land/Arc K - The Fallen Abbey.md',
    'L': 'reloaded-source/Act III - The Broken Land/Arc L - The Den of Wolves.md',
    'M': "reloaded-source/Act III - The Broken Land/Arc M - The Dragon's Manor.md",
    'O': 'reloaded-source/Act III - The Broken Land/Arc O - Dinner with the Devil.md',
    'P': 'reloaded-source/Act III - The Broken Land/Arc P - Ravenloft Heist.md',
    'Q': 'reloaded-source/Act III - The Broken Land/Arc Q - A Shining Beacon.md',
    'R': 'reloaded-source/Act IV - Secrets of the Ancient/Arc R - Trials of the Mountain.md',
    'S': 'reloaded-source/Act IV - Secrets of the Ancient/Arc S - A Sword of Sunlight.md',
    'T': 'reloaded-source/Act IV - Secrets of the Ancient/Arc T - The Three Fanes.md',
    'U': 'reloaded-source/Act IV - Secrets of the Ancient/Arc U - Dreams of Dawn.md',
    'EP': 'reloaded-source/Act IV - Secrets of the Ancient/Epilogue.md'
}

print("Checking all file paths exist:")
for arc, path in arc_files.items():
    exists = glob.glob(path)
    if not exists:
        print(f"  MISSING: {arc} -> {path}")
    else:
        print(f"  OK: Arc {arc} -> {path} ({len(open(path, encoding='utf-8').read())} chars)")
