# -*- coding: utf-8 -*-
"""
Downloads real, high-resolution community & official Curse of Strahd / Strahd Reloaded
maps from GitHub repositories (matthewbstroud/sdnd-strahd-adv, q-datum/dungeonslab-gothic-maps-pack,
and 5etools-mirror-2/5etools-img) for all 16 missing maps (novo_01 .. novo_16),
plus player-safe versions without GM spoilers!
"""

import io
import os
import urllib.request
import urllib.parse
from pathlib import Path
from PIL import Image

WORKSPACE = Path(r"c:\Users\Alex\Documents\antigravity\beautiful-bohr")
MAPS_DIR = WORKSPACE / "assets" / "maps"
VAULT_ANEXOS = Path(r"C:\Users\Alex\Downloads\AUTOMAÇAO RPG\Vault RPG\_anexos")

MAPS_DIR.mkdir(parents=True, exist_ok=True)

SDND_BASE = "https://raw.githubusercontent.com/matthewbstroud/sdnd-strahd-adv/HEAD/"
GOTHIC_BASE = "https://raw.githubusercontent.com/q-datum/dungeonslab-gothic-maps-pack/HEAD/"
TOOLS_BASE = "https://raw.githubusercontent.com/5etools-mirror-2/5etools-img/HEAD/adventure/CoS/"

# Mapping of our 16 map filenames to real high-resolution maps on GitHub
REAL_MAP_SOURCES = [
    {
        "key": "novo_01",
        "file": "Vale_de_Barovia_Regional.jpg",
        "player_file": "Vale_de_Barovia_Regional_Players.jpg",
        "title": "Vale de Baróvia · Mapa Regional Completo",
        "dm_url": TOOLS_BASE + "007-001.webp",
        "player_url": TOOLS_BASE + "008-cos201.webp",
    },
    {
        "key": "novo_02",
        "file": "Daggerford_Estrebaria_Brumas.jpg",
        "title": "Daggerford · Estrebaria e Acampamento nas Brumas",
        "dm_url": SDND_BASE + "images/maps/Areas/A/a2_campsite/campsite.webp",
    },
    {
        "key": "novo_03",
        "file": "Portoes_Barovia_Estrada_Svalich.jpg",
        "title": "Portões de Baróvia e Estrada Svalich",
        "dm_url": SDND_BASE + "images/maps/Areas/B/b1_gates/east_gates.webp",
    },
    {
        "key": "novo_04",
        "file": "Vila_Barovia_Barricada_Oriental.jpg",
        "title": "Vila de Baróvia · Ruas, Taverna e Cerco",
        "dm_url": GOTHIC_BASE + "assets/maps/barovia-town.webp",
    },
    {
        "key": "novo_05",
        "file": "Encruzilhada_Ivlis_Forca.jpg",
        "title": "Encruzilhada do Rio Ivlis, Forca e Ponte",
        "dm_url": SDND_BASE + "images/maps/Areas/F/f1_xrds/xrds.webp",
    },
    {
        "key": "novo_06",
        "file": "Tser_Pool_Acampamento_Vistani.jpg",
        "title": "Acampamento de Tser Pool e Tenda de Madame Eva",
        "dm_url": SDND_BASE + "images/maps/Areas/G/g1_camp/camp.webp",
    },
    {
        "key": "novo_07",
        "file": "Tser_Falls_Encruzilhada_Ravenloft.jpg",
        "title": "Cachoeira de Tser Falls e Ponte do Desfiladeiro",
        "dm_url": SDND_BASE + "images/maps/Areas/H/h1_falls/falls.webp",
    },
    {
        "key": "novo_08",
        "file": "Floresta_Svalich_Cacada_Alcateia.jpg",
        "title": "Floresta Svalich Profunda · Estrada e Emboscada",
        "dm_url": SDND_BASE + "images/maps/Areas/C/c1_woods/woods.webp",
    },
    {
        "key": "novo_09",
        "file": "Vallaki_Cidade_Praca_Portoes.jpg",
        "player_file": "Vallaki_Cidade_Praca_Portoes_Players.jpg",
        "title": "Vallaki · Planta Urbana Completa e Praça",
        "dm_url": TOOLS_BASE + "047-013.webp",
        "player_url": TOOLS_BASE + "048-cos05-02-player.webp",
    },
    {
        "key": "novo_10",
        "file": "Vallaki_Igreja_Santo_Andral.jpg",
        "title": "Vallaki · Igreja de Santo Andral e Cemitério",
        "dm_url": SDND_BASE + "images/maps/Areas/N/n1_st_andral/andral_first.webp",
    },
    {
        "key": "novo_11",
        "file": "Vallaki_Arasek_e_Blinsky.jpg",
        "title": "Vallaki · Pátio de Arasek e Loja de Blinsky",
        "dm_url": SDND_BASE + "images/maps/Areas/N/n7_toy_maker/ground_floor.webp",
        "secondary_url": SDND_BASE + "images/maps/Areas/N/n5_stockyard/ground_l.webp",
    },
    {
        "key": "novo_12",
        "file": "Lago_Zarovich_e_Estrada_Baratok.jpg",
        "title": "Lago Zarovich e Margem Norte",
        "dm_url": SDND_BASE + "images/maps/Areas/L/l1_zarovich/lake_b.webp",
    },
    {
        "key": "novo_13",
        "file": "Lago_Baratok_Vigilia_Covil.jpg",
        "title": "Entrada do Covil dos Lobisomens e Encosta de Baratok",
        "dm_url": SDND_BASE + "images/maps/Areas/Z/Z1. Cave Mouth/cave_mouth.webp",
    },
    {
        "key": "novo_14",
        "file": "Monte_Ghakis_Trilha_Cavernas_Bodaks.jpg",
        "title": "Monte Ghakis · Trilha da Montanha e Cavernas",
        "dm_url": SDND_BASE + "images/maps/Areas/Y/y1_trail/trail.webp",
    },
    {
        "key": "novo_15",
        "file": "Soldav_Vila_e_Santuario_Rozana.jpg",
        "title": "Vila Montanhesa de Soldav e Montes Tribais",
        "dm_url": SDND_BASE + "images/maps/Areas/Y/y2_berserker_cairns/berserker_cairns.webp",
    },
    {
        "key": "novo_16",
        "file": "Santuarios_Megalitos_e_Lago_Sonhador.jpg",
        "title": "Santuário dos Megálitos Antigos das Rozanas",
        "dm_url": SDND_BASE + "images/maps/Areas/U/u6_standing_stones/megaliths_1.webp",
    },
]


def fetch_image(url: str) -> Image.Image:
    # Properly quote path segments with spaces
    parts = urllib.parse.urlsplit(url)
    quoted_path = urllib.parse.quote(urllib.parse.unquote(parts.path))
    safe_url = urllib.parse.urlunsplit((parts.scheme, parts.netloc, quoted_path, parts.query, parts.fragment))
    req = urllib.request.Request(safe_url, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=25).read()
    img = Image.open(io.BytesIO(raw))
    if img.mode in ("RGBA", "P"):
        bg = Image.new("RGB", img.size, (14, 16, 22))
        if img.mode == "P":
            img = img.convert("RGBA")
        bg.paste(img, mask=img.split()[3])
        return bg
    return img.convert("RGB")


def resize_max(img: Image.Image, max_dim: int = 1800) -> Image.Image:
    w, h = img.size
    if max(w, h) <= max_dim:
        return img
    scale = max_dim / float(max(w, h))
    nw, nh = int(round(w * scale)), int(round(h * scale))
    return img.resize((nw, nh), Image.Resampling.LANCZOS)


def main():
    for item in REAL_MAP_SOURCES:
        print(f"Downloading {item['key']} -> {item['file']} ...")
        img = fetch_image(item["dm_url"])

        # If there's a secondary_url (e.g., Arasek Stockyard + Blinsky Toys), combine side-by-side cleanly
        if "secondary_url" in item:
            img2 = fetch_image(item["secondary_url"])
            target_h = 1100
            w1 = int(img.width * (target_h / img.height))
            w2 = int(img2.width * (target_h / img2.height))
            r1 = img.resize((w1, target_h), Image.Resampling.LANCZOS)
            r2 = img2.resize((w2, target_h), Image.Resampling.LANCZOS)
            combined = Image.new("RGB", (w1 + w2 + 16, target_h), (15, 18, 24))
            combined.paste(r2, (0, 0))
            combined.paste(r1, (w2 + 16, 0))
            img = combined

        img = resize_max(img, 1800)
        out_path = MAPS_DIR / item["file"]
        img.save(out_path, "JPEG", quality=86, optimize=True)
        if VAULT_ANEXOS.exists():
            img.save(VAULT_ANEXOS / item["file"], "JPEG", quality=86, optimize=True)
        print(f"  Saved {out_path.name} ({img.width}x{img.height}, {out_path.stat().st_size // 1024} KB)")

        if "player_url" in item and "player_file" in item:
            pimg = resize_max(fetch_image(item["player_url"]), 1800)
            p_out = MAPS_DIR / item["player_file"]
            pimg.save(p_out, "JPEG", quality=86, optimize=True)
            if VAULT_ANEXOS.exists():
                pimg.save(VAULT_ANEXOS / item["player_file"], "JPEG", quality=86, optimize=True)
            print(f"  Saved Player-Safe {p_out.name} ({pimg.width}x{pimg.height})")


if __name__ == "__main__":
    main()
