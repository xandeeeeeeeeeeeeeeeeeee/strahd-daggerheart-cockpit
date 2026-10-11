#!/usr/bin/env python3
"""
Gera os 16 mapas ausentes de Strahd Reloaded · Daggerheart (cobrindo todas as 75 cenas sem planta específica
e o Mapa Regional Completo do Vale de Baróvia) e organiza o pacote completo de 44 mapas (28 originais + 16 novos).
"""
import os
import sys
import math
import random
import shutil
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE = r"c:\Users\Alex\Documents\antigravity\beautiful-bohr"
MAPS_OUT = os.path.join(WORKSPACE, "assets", "maps")
VAULT_DIR = os.path.expandvars(r"%USERPROFILE%\Downloads\AUTOMAÇAO RPG\Vault RPG")
VAULT_ANEXOS = os.path.join(VAULT_DIR, "_anexos")

os.makedirs(MAPS_OUT, exist_ok=True)


def get_font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\georgiab.ttf" if bold else r"C:\Windows\Fonts\georgia.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()


def get_title_font(size):
    candidates = [
        r"C:\Windows\Fonts\georgiab.ttf",
        r"C:\Windows\Fonts\timesbd.ttf",
        r"C:\Windows\Fonts\segoeuib.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return get_font(size, bold=True)


def create_gothic_canvas(w=1400, h=1000, theme="parchment", seed=42):
    rng = random.Random(seed)
    palettes = {
        "parchment": ((28, 25, 22), (44, 38, 33), (62, 53, 44)),
        "forest": ((18, 26, 22), (28, 39, 33), (45, 58, 48)),
        "urban": ((24, 24, 29), (36, 37, 44), (52, 54, 64)),
        "snow": ((26, 33, 42), (42, 52, 66), (68, 82, 100)),
        "swamp": ((20, 27, 21), (32, 42, 31), (48, 60, 44)),
        "sanctuary": ((28, 22, 32), (42, 33, 48), (64, 50, 72)),
    }
    c0, c1, c2 = palettes.get(theme, palettes["parchment"])
    img = Image.new("RGB", (w, h), c1)
    draw = ImageDraw.Draw(img, "RGBA")

    for _ in range(150):
        rx = rng.randint(-100, w + 100)
        ry = rng.randint(-100, h + 100)
        rr = rng.randint(40, 220)
        col = c2 if rng.random() > 0.5 else c0
        alpha = rng.randint(12, 34)
        draw.ellipse((rx - rr, ry - rr, rx + rr, ry + rr), fill=(*col, alpha))

    grid_col = (210, 195, 170, 22) if theme != "snow" else (200, 225, 255, 26)
    for x in range(0, w, 70):
        draw.line([(x, 0), (x, h)], fill=grid_col, width=1)
    for y in range(0, h, 70):
        draw.line([(0, y), (w, y)], fill=grid_col, width=1)

    for i in range(25):
        alpha = int(140 * (1 - i / 25))
        draw.rectangle([i, i, w - 1 - i, h - 1 - i], outline=(8, 7, 10, alpha), width=1)

    draw.rectangle([16, 16, w - 16, h - 16], outline=(168, 142, 102, 180), width=2)
    draw.rectangle([22, 22, w - 22, h - 22], outline=(168, 142, 102, 90), width=1)
    return img, draw


def draw_trees(draw, centers, rng, snow=False, dead=False):
    for cx, cy, r in centers:
        draw.ellipse((cx - r + 4, cy - r + 4, cx + r + 4, cy + r + 4), fill=(5, 6, 8, 110))
        if dead:
            draw.ellipse((cx - r // 3, cy - r // 3, cx + r // 3, cy + r // 3), fill=(55, 42, 35, 220))
            for a in range(0, 360, 45):
                rad = math.radians(a + rng.randint(-15, 15))
                ex = cx + int(math.cos(rad) * r)
                ey = cy + int(math.sin(rad) * r)
                draw.line([(cx, cy), (ex, ey)], fill=(95, 78, 65, 210), width=2)
        else:
            base_c = (48, 74, 52, 220) if not snow else (68, 92, 96, 230)
            hi_c = (72, 102, 74, 200) if not snow else (175, 200, 215, 210)
            draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=base_c, outline=(22, 34, 24, 230), width=2)
            draw.ellipse((cx - int(r * 0.65), cy - int(r * 0.65), cx + int(r * 0.5), cy + int(r * 0.5)), fill=hi_c)
            draw.ellipse((cx - 3, cy - 3, cx + 3, cy + 3), fill=(25, 35, 25, 240))


def draw_road(draw, pts, width=36, color=(92, 78, 62), border=(55, 46, 36)):
    if len(pts) < 2:
        return
    draw.line(pts, fill=(*border, 220), width=width + 8, joint="curve")
    draw.line(pts, fill=(*color, 230), width=width, joint="curve")
    draw.line(pts, fill=(125, 108, 86, 90), width=max(4, width // 3), joint="curve")


def draw_river(draw, pts, width=44, bridge_pts=None):
    if len(pts) < 2:
        return
    draw.line(pts, fill=(28, 52, 74, 230), width=width + 12, joint="curve")
    draw.line(pts, fill=(42, 82, 112, 240), width=width, joint="curve")
    draw.line(pts, fill=(88, 145, 180, 120), width=max(6, width // 3), joint="curve")
    if bridge_pts:
        bx1, by1, bx2, by2 = bridge_pts
        draw.rectangle([bx1, by1, bx2, by2], fill=(115, 105, 92, 255), outline=(45, 40, 35, 255), width=3)


def draw_building(draw, rect, name=None, roof_color=(88, 52, 46), interior=False, rooms=None):
    x1, y1, x2, y2 = rect
    draw.rectangle([x1 + 6, y1 + 6, x2 + 6, y2 + 6], fill=(5, 5, 8, 130))
    if interior:
        draw.rectangle([x1, y1, x2, y2], fill=(64, 58, 50, 245), outline=(185, 168, 140, 255), width=4)
        for gx in range(x1 + 25, x2, 25):
            draw.line([(gx, y1), (gx, y2)], fill=(45, 40, 35, 90), width=1)
        for gy in range(y1 + 25, y2, 25):
            draw.line([(x1, gy), (x2, gy)], fill=(45, 40, 35, 90), width=1)
        if rooms:
            for rx1, ry1, rx2, ry2, rlabel in rooms:
                draw.rectangle([rx1, ry1, rx2, ry2], outline=(170, 152, 125, 240), width=3)
                if rlabel:
                    f = get_font(14, bold=True)
                    draw.text(((rx1 + rx2) // 2, (ry1 + ry2) // 2), rlabel, fill=(235, 222, 195, 230), font=f, anchor="mm")
    else:
        draw.rectangle([x1, y1, x2, y2], fill=(*roof_color, 245), outline=(32, 22, 20, 255), width=3)
        if (x2 - x1) >= (y2 - y1):
            my = (y1 + y2) // 2
            draw.line([(x1 + 8, my), (x2 - 8, my)], fill=(140, 95, 82, 200), width=2)
        else:
            mx = (x1 + x2) // 2
            draw.line([(mx, y1 + 8), (mx, y2 - 8)], fill=(140, 95, 82, 200), width=2)
    if name:
        f = get_font(14, bold=True)
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
        bbox = draw.textbbox((cx, cy), name, font=f, anchor="mm")
        draw.rectangle([bbox[0] - 5, bbox[1] - 3, bbox[2] + 5, bbox[3] + 3], fill=(16, 14, 18, 215), outline=(168, 142, 102, 160), width=1)
        draw.text((cx, cy), name, fill=(245, 235, 210, 255), font=f, anchor="mm")


def draw_marker(draw, x, y, code, label, secret=False, pos="auto"):
    r = 16
    fill_c = (155, 38, 38, 245) if secret else (32, 48, 72, 245)
    border_c = (255, 190, 120, 255) if secret else (218, 188, 122, 255)
    draw.ellipse((x - r + 2, y - r + 2, x + r + 2, y + r + 2), fill=(0, 0, 0, 160))
    draw.ellipse((x - r, y - r, x + r, y + r), fill=fill_c, outline=border_c, width=2)
    f_code = get_font(13, bold=True)
    draw.text((x, y), str(code), fill=(255, 248, 230, 255), font=f_code, anchor="mm")
    if label:
        f_lbl = get_font(13, bold=True)
        if pos == "auto":
            pos = "left" if x > 940 else "right"
        if pos == "right":
            tx, ty, anc = x + r + 8, y, "lm"
        elif pos == "left":
            tx, ty, anc = x - r - 8, y, "rm"
        elif pos == "top":
            tx, ty, anc = x, y - r - 12, "mm"
        else:
            tx, ty, anc = x, y + r + 14, "mm"
        bbox = draw.textbbox((tx, ty), label, font=f_lbl, anchor=anc)
        # Clamp inside safe area [36..1364]
        dx = 0
        if bbox[0] < 36:
            dx = 36 - bbox[0]
        elif bbox[2] > 1364:
            dx = 1364 - bbox[2]
        tx += dx
        bbox = (bbox[0] + dx, bbox[1], bbox[2] + dx, bbox[3])
        bg = (65, 18, 22, 232) if secret else (18, 20, 26, 228)
        draw.rectangle([bbox[0] - 6, bbox[1] - 3, bbox[2] + 6, bbox[3] + 3], fill=bg, outline=border_c, width=1)
        draw.text((tx, ty), label, fill=(255, 230, 215, 255) if secret else (240, 232, 212, 255), font=f_lbl, anchor=anc)


def draw_header_and_legend(draw, w, h, title, subtitle, arcs_scenes, legend_items, scale_note="Alcances DH: Corpo a Corpo · Muito Próximo (~3m) · Próximo (~9m) · Distante (~30m)"):
    draw.rectangle([28, 28, w - 28, 108], fill=(16, 15, 20, 235), outline=(168, 142, 102, 215), width=2)
    f_title = get_title_font(24)
    f_sub = get_font(13, bold=False)
    f_arc = get_font(13, bold=True)
    draw.text((44, 50), title, fill=(242, 222, 178, 255), font=f_title, anchor="lm")
    draw.text((44, 84), subtitle, fill=(205, 198, 182, 245), font=f_sub, anchor="lm")
    draw.text((w - 44, 50), f"Arcos / Cenas: {arcs_scenes}", fill=(218, 175, 110, 255), font=f_arc, anchor="rm")
    draw.text((w - 44, 84), scale_note, fill=(165, 188, 210, 240), font=f_sub, anchor="rm")

    cx, cy = w - 72, 164
    draw.ellipse((cx - 32, cy - 32, cx + 32, cy + 32), fill=(18, 18, 24, 215), outline=(168, 142, 102, 200), width=2)
    draw.polygon([(cx, cy - 26), (cx - 7, cy), (cx, cy - 5), (cx + 7, cy)], fill=(220, 185, 115, 255))
    draw.polygon([(cx, cy + 26), (cx - 6, cy), (cx, cy + 5), (cx + 6, cy)], fill=(120, 110, 95, 220))
    draw.text((cx, cy - 34), "N", fill=(245, 225, 175, 255), font=get_font(12, bold=True), anchor="mb")

    if legend_items:
        bh = 76
        draw.rectangle([28, h - 28 - bh, w - 28, h - 28], fill=(14, 14, 18, 236), outline=(168, 142, 102, 200), width=2)
        f_leg_h = get_font(13, bold=True)
        f_leg = get_font(12, bold=False)
        draw.text((44, h - 28 - bh + 18), "LEGENDA DE ÁREAS E PONTOS TÁTICOS (MESTRE & JOGADORES):", fill=(225, 195, 135, 255), font=f_leg_h, anchor="lm")
        mid = (len(legend_items) + 1) // 2
        row1 = "   ·   ".join(legend_items[:mid])
        row2 = "   ·   ".join(legend_items[mid:])
        draw.text((44, h - 28 - bh + 40), row1, fill=(225, 220, 210, 245), font=f_leg, anchor="lm")
        if row2:
            draw.text((44, h - 28 - bh + 58), row2, fill=(210, 205, 195, 240), font=f_leg, anchor="lm")


def generate_all_16_maps():
    maps_meta = []

    # ---------------------------------------------------------
    # 01. VALE DE BARÓVIA · MAPA REGIONAL COMPLETO
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "forest", seed=101)
    rng = random.Random(101)
    for mx in range(80, 1320, 65):
        my = 148 + rng.randint(-15, 20)
        draw.polygon([(mx - 38, my + 35), (mx, my - 25), (mx + 38, my + 35)], fill=(58, 62, 70, 210), outline=(110, 115, 125, 180))
    for mx in range(100, 1300, 60):
        my = 825 + rng.randint(-25, 18)
        draw.polygon([(mx - 45, my + 42), (mx, my - 35), (mx + 45, my + 42)], fill=(65, 72, 84, 220), outline=(145, 160, 180, 190))
    draw.ellipse((590, 235, 770, 340), fill=(32, 72, 102, 235), outline=(85, 135, 165, 200), width=2)
    draw.ellipse((350, 175, 500, 260), fill=(32, 72, 102, 235), outline=(85, 135, 165, 200), width=2)
    draw.ellipse((860, 545, 960, 615), fill=(38, 84, 114, 235), outline=(95, 145, 175, 200), width=2)
    draw.ellipse((460, 635, 610, 725), fill=(38, 64, 52, 225), outline=(85, 115, 95, 190), width=2)
    draw_river(draw, [(425, 260), (440, 390), (540, 460), (540, 655)], width=16)
    draw_river(draw, [(780, 525), (880, 580), (1050, 625), (1260, 655)], width=18)
    draw_road(draw, [(70, 440), (220, 410), (380, 440), (660, 410), (840, 460), (980, 500), (1140, 540), (1320, 540)], width=18)
    draw_road(draw, [(220, 410), (210, 305)], width=14)
    draw_road(draw, [(220, 410), (195, 560), (150, 700)], width=14)
    draw_road(draw, [(520, 430), (470, 535), (535, 655)], width=12)
    draw_road(draw, [(470, 535), (430, 720), (580, 790), (740, 840), (860, 830)], width=13)
    trees = [(rng.randint(80, 1320), rng.randint(175, 775), rng.randint(14, 24)) for _ in range(85)]
    draw_trees(draw, trees, rng)
    pts = [
        (1310, 540, "1", "Portões Leste (B2)", "left"),
        (1140, 505, "2", "Vila de Baróvia (B)", "top"),
        (1045, 635, "3", "Encruzilhada do Ivlis (C2)", "right"),
        (890, 580, "4", "Tser Pool · Eva (C4)", "left"),
        (815, 515, "5", "Tser Falls · Ponte (C7)", "left"),
        (1010, 385, "6", "Castelo Ravenloft (O/P/U)", "right"),
        (815, 425, "7", "Moinho Esmaga-Ossos (C9/H)", "left"),
        (655, 395, "8", "Vallaki (C12/D–G/U3)", "top"),
        (665, 285, "9", "Lago Zarovich (E4)", "right"),
        (600, 468, "10", "Acampamento Vistani (E2)", "right"),
        (430, 325, "11", "Torre de Van Richten (E6/T4)", "right"),
        (375, 215, "12", "Covil dos Lobisomens (L/Q)", "right"),
        (465, 535, "13", "Argynvostholt (M)", "right"),
        (540, 680, "14", "Ruínas de Berez · Lysaga (I/T)", "right"),
        (210, 295, "15", "Krezk e Abadia (K)", "right"),
        (195, 565, "16", "Vinícola Mago dos Vinhos (J)", "right"),
        (145, 705, "17", "Colina Yester (J)", "right"),
        (435, 735, "18", "Passo de Tsolenka (R)", "right"),
        (610, 805, "19", "Vila de Soldav (R5/T1)", "right"),
        (865, 825, "20", "Templo de Âmbar (S)", "right"),
    ]
    for x, y, c, lbl, pos in pts:
        draw_marker(draw, x, y, c, lbl, secret=(c in ("12", "20")), pos=pos)
    draw_header_and_legend(
        draw, 1400, 1000,
        "Vale de Baróvia · Mapa Regional Completo",
        "Geografia geral, estradas, rios, lagos e tempos de viagem de Strahd Reloaded",
        "Arcos A–U e Epílogo",
        [
            "1–2: Entrada Leste » Vila (30 min)",
            "2–3–4: Vila » Ivlis » Tser Pool (1h15)",
            "5–7–8: Tser Falls » Moinho » Vallaki (3h30)",
            "8–15: Vallaki » Krezk (3h45)",
            "8–16–17: Vallaki » Vinícola » Yester (3h30)",
            "18–19–20: Tsolenka » Soldav » Templo de Âmbar"
        ],
        scale_note="Escala Regional · 1 hex = 1/4 milha · Viagem a pé: ~4,8 km/h"
    )
    maps_meta.append(("novo_01", "Vale de Baróvia · Mapa Regional Completo", "Vale_de_Barovia_Regional.jpg", img))

    # ---------------------------------------------------------
    # 02. DAGGERFORD · ESTREBARIA E RUA NAS BRUMAS (A1)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "urban", seed=102)
    draw_road(draw, [(80, 520), (1320, 520)], width=90, color=(65, 62, 58))
    draw_road(draw, [(680, 520), (680, 160)], width=65, color=(65, 62, 58))
    draw_building(draw, (110, 180, 480, 440), None, interior=True, rooms=[
        (120, 190, 310, 320, "Palheiro Úmido"),
        (310, 190, 470, 320, "Baias dos Cavalos"),
        (120, 320, 470, 430, "Pátio de Feno & Carroça")
    ])
    draw_building(draw, (110, 600, 520, 840), "Taverna Rédea do Pesadelo (Lotada)", roof_color=(98, 56, 44))
    draw_building(draw, (760, 600, 1140, 820), "Casas Fechadas (Highharvesttide)", roof_color=(72, 54, 48))
    draw_building(draw, (900, 160, 1290, 430), None, interior=True, rooms=[
        (910, 260, 1100, 420, "Pórtico de Ferro (Área 1)"),
        (1100, 170, 1280, 420, "Salão de Carvalho (Área 2)")
    ])
    for mx, my, mr in [(720, 510, 110), (860, 480, 140), (1020, 460, 150), (880, 320, 120)]:
        draw.ellipse((mx - mr, my - mr // 2, mx + mr, my + mr // 2), fill=(165, 185, 205, 42))
    draw_marker(draw, 190, 240, "1", "Palheiro · Relíquias Despertam", pos="right")
    draw_marker(draw, 290, 520, "2", "Rua Enlameada & Pregoeiro (Mercenários)", pos="right")
    draw_marker(draw, 680, 475, "3", "Beco nas Brumas (Esq. » Dir. » Esq.)", pos="left")
    draw_marker(draw, 950, 395, "4", "Portão Enferrujado · Encontro dos Grupos", pos="left")
    draw_marker(draw, 1190, 235, "5", "Porta Tranca · 18 Unidades até Meia-Noite", secret=True, pos="left")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Daggerford · Estrebaria Rédea do Pesadelo e Rua nas Brumas",
        "Cena A1 e Transição A2a: Abertura sob chuva de Highharvesttide e chamado das relíquias",
        "Arco A (A1, A2a)",
        [
            "1: Palheiro da Estrebaria (abrigo inicial sob chuva)",
            "2: Taverna Rédea do Pesadelo e Rua Principal",
            "3: Rota guiada pelas Relíquias na Névoa",
            "4: Pórtico da Casa Durst (Área 1)",
            "5 [SEGREDO]: Armadilha da Entrada e Relógio de 18 Unidades"
        ]
    )
    maps_meta.append(("novo_02", "Daggerford · Estrebaria e Rua nas Brumas", "Daggerford_Estrebaria_Brumas.jpg", img))

    # ---------------------------------------------------------
    # 03. PORTÕES DE BARÓVIA, ESTRADA SVALICH E MIRANTE (B1-B4)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "forest", seed=103)
    rng = random.Random(103)
    draw_road(draw, [(60, 520), (480, 520), (920, 500), (1340, 480)], width=46)
    draw_road(draw, [(640, 510), (710, 310), (780, 240)], width=22, color=(75, 64, 50))
    draw.rectangle([420, 360, 465, 480], fill=(95, 95, 105, 255), outline=(30, 30, 35, 255), width=3)
    draw.rectangle([420, 560, 465, 680], fill=(95, 95, 105, 255), outline=(30, 30, 35, 255), width=3)
    draw.line([(442, 480), (442, 560)], fill=(45, 48, 55, 255), width=6)
    trees = [(rng.randint(80, 1280), rng.randint(150, 840), rng.randint(18, 32)) for _ in range(55) if abs(rng.randint(150, 840) - 510) > 70]
    draw_trees(draw, trees, rng)
    draw_marker(draw, 110, 520, "1", "B1 · Estrada Svalich e Brumas Asfixiantes", pos="right")
    draw_marker(draw, 442, 410, "2", "B2 · Portões de Baróvia (Estátuas Decapitadas)", pos="right")
    draw_marker(draw, 770, 225, "3", "B3 · Clareira do Cadáver de Dalvan (Carta + Bússola)", pos="right")
    draw_marker(draw, 680, 310, "4", "Rastro do Grande Lobo Cinzento (Verost)", secret=True, pos="left")
    draw_marker(draw, 1250, 465, "5", "B4 · Mirante da Colina (Vista da Vila e Barricadas)", pos="left")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Portões de Baróvia, Estrada Svalich e Floresta de Dalvan",
        "Percurso inicial no vale: Portões antigos, trilha do batedor Dalvan e mirante da vila",
        "Arco B (B1, B2, B3, B4)",
        [
            "1: Estrada Velha de Svalich (chegada da Casa da Morte)",
            "2: Portões de Ferro que se fecham sozinhos",
            "3: Clareira de Dalvan (cadáver, carta de Kolyan, bússola)",
            "4 [SEGREDO]: Espreita de Verost e uivos",
            "5: Mirante da Vila de Baróvia"
        ]
    )
    maps_meta.append(("novo_03", "Portões de Baróvia, Estrada Svalich e Mirante", "Portoes_Barovia_Estrada_Svalich.jpg", img))

    # ---------------------------------------------------------
    # 04. VILA DE BARÓVIA · BARRICADA ORIENTAL E PRAÇA (B5b, B5f)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "urban", seed=104)
    draw_road(draw, [(60, 520), (1340, 520)], width=76, color=(68, 62, 55))
    draw_road(draw, [(420, 160), (420, 860)], width=56, color=(68, 62, 55))
    draw.ellipse((320, 420, 520, 620), fill=(82, 76, 68, 230), outline=(140, 128, 110, 200), width=2)
    draw_building(draw, (120, 220, 340, 390), "Taverna Sangue da Videira (E1)", roof_color=(96, 48, 42))
    draw_building(draw, (490, 220, 710, 390), "Empório de Bildrath (E2)", roof_color=(72, 58, 48))
    draw_building(draw, (120, 640, 350, 820), "Casa de Mad Mary (E3)", roof_color=(64, 52, 62))
    draw_building(draw, (520, 640, 780, 810), "Casas com Tábuas / Telhado Sul", roof_color=(68, 56, 48))
    draw_building(draw, (810, 230, 1040, 400), "Telhado Norte (Posto de Arco)", roof_color=(68, 56, 48))
    draw.rectangle([1055, 410, 1095, 630], fill=(112, 78, 44, 250), outline=(42, 28, 16, 255), width=4)
    draw_marker(draw, 420, 520, "1", "B5b · Praça da Vila (Refugiados e Alenka)", pos="right")
    draw_marker(draw, 1075, 575, "2", "B5f · Barricada Oriental (Linha Principal)", pos="left")
    draw_marker(draw, 940, 460, "3", "Caixa de 12 Garrafas Incendiárias (Ireena)", pos="left")
    draw_marker(draw, 925, 190, "4", "Flanco do Beco Norte (Infiltração de Carniçais)", secret=True, pos="left")
    draw_marker(draw, 1290, 520, "5", "Chegada: 3 Ondas de Mortos e Rahadin", secret=True, pos="left")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Vila de Baróvia · Barricada Oriental e Praça Central",
        "Mapa tático de zonas para B5b, B5f e o Encontro 'B · O cerco' (3 ondas + Rahadin)",
        "Arco B (B5b, B5c, B5f)",
        [
            "1: Praça Central e Poço (Recuo e Civis)",
            "2: Barricada Oriental (Carroças, móveis e estacas)",
            "3: Reserva de Fogo Grego/Garrafas de Ireena",
            "4 [SEGREDO]: Rota lateral dos Carniçais pelo Beco Norte",
            "5 [SEGREDO]: Zona de entrada das 3 Ondas e aparição de Rahadin"
        ]
    )
    maps_meta.append(("novo_04", "Vila de Baróvia · Barricada Oriental e Praça", "Vila_Barovia_Barricada_Oriental.jpg", img))

    # ---------------------------------------------------------
    # 05. ENCRUZILHADA DO RIO IVLIS, FORCA E CEMITÉRIO (C1-C3, C5)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "forest", seed=105)
    rng = random.Random(105)
    draw_river(draw, [(520, 120), (560, 500), (510, 880)], width=58, bridge_pts=(485, 470, 625, 545))
    draw_road(draw, [(80, 510), (555, 510), (880, 510), (1320, 640)], width=40)
    draw_road(draw, [(880, 510), (1120, 230)], width=32)
    draw.rectangle([680, 600, 980, 810], fill=(38, 42, 46, 210), outline=(120, 125, 135, 230), width=3)
    for gx in range(710, 960, 45):
        for gy in range(630, 790, 50):
            draw.rectangle([gx, gy, gx + 14, gy + 22], fill=(135, 140, 148, 220))
    draw.rectangle([820, 380, 910, 455], fill=(95, 72, 48, 245), outline=(40, 28, 18, 255), width=3)
    trees = [(rng.randint(80, 1300), rng.randint(150, 830), rng.randint(18, 30)) for _ in range(40) if not (650 < rng.randint(80, 1300) < 1020 and 350 < rng.randint(150, 830) < 830)]
    draw_trees(draw, trees, rng)
    draw_marker(draw, 190, 360, "1", "C1 · Cache dos Antigos Conhecidos na Floresta", pos="right")
    draw_marker(draw, 555, 508, "2", "Ponte de Pedra sobre o Rio Ivlis", pos="left")
    draw_marker(draw, 865, 415, "3", "C2 · Forca (1º Encontro com Strahd / Meia-Noite com Eva)", pos="left")
    draw_marker(draw, 830, 705, "4", "Cemitério · Marcha dos Mortos (C4) e Cavaleiro (C5)", pos="top")
    draw_marker(draw, 1140, 270, "5", "C3 · Árvore do Corvo Ferido (Muriel) e Strix", secret=True, pos="left")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Encruzilhada do Rio Ivlis, Forca e Cemitério Antigo",
        "Ponte do Ivlis, Forca de Strahd, Cemitério da Marcha dos Mortos e trilha para Tser Pool",
        "Arco C (C1, C2, C3, C4, C5)",
        [
            "1: Esconderijo/Cache na Floresta (C1)",
            "2: Ponte do Rio Ivlis",
            "3: Forca da Encruzilhada (Aparição de Strahd em C2 e Leitura Secreta de Tarokka em C4)",
            "4: Cemitério Antigo (Marcha dos Mortos e Dalvan Esquelético em C5)",
            "5 [SEGREDO]: C3 · Emboscada da Strix ao Corvo Ferido (Muriel)"
        ]
    )
    maps_meta.append(("novo_05", "Encruzilhada do Rio Ivlis, Forca e Cemitério", "Encruzilhada_Ivlis_Forca.jpg", img))

    # ---------------------------------------------------------
    # 06. ACAMPAMENTO DE TSER POOL E TENDA DE MADAME EVA (C4)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "forest", seed=106)
    draw.ellipse((860, 260, 1380, 860), fill=(32, 76, 106, 240), outline=(92, 148, 178, 220), width=4)
    draw_road(draw, [(80, 620), (540, 560), (740, 520)], width=38)
    draw.ellipse((510, 460, 590, 540), fill=(185, 85, 28, 240), outline=(255, 195, 70, 255), width=3)
    draw.polygon([(680, 280), (770, 220), (850, 280), (830, 380), (700, 380)], fill=(112, 42, 68, 245), outline=(225, 185, 110, 255), width=3)
    wagons = [(360, 340, 460, 395), (330, 480, 430, 535), (410, 620, 510, 675), (610, 630, 710, 685), (540, 310, 640, 365)]
    for wx1, wy1, wx2, wy2 in wagons:
        draw_building(draw, (wx1, wy1, wx2, wy2), roof_color=(115, 68, 42))
    draw_marker(draw, 550, 500, "1", "Fogueira · Jogo das Histórias (Stanimir, Arturi, Ireena, Eliza)", pos="right")
    draw_marker(draw, 765, 285, "2", "Tenda de Madame Eva (Convite para Meia-Noite)", pos="left")
    draw_marker(draw, 660, 655, "3", "Carroça de Eliza (Espiã de Strahd · Perseguição 0/4)", secret=True, pos="right")
    draw_marker(draw, 160, 260, "4", "Trilha de Saída Discreta (Finesse 10) e Árvore de Arturi", secret=True, pos="right")
    draw_marker(draw, 1140, 560, "5", "Margem da Lagoa Tser", pos="left")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Acampamento de Tser Pool e Tenda de Madame Eva",
        "Cena C4: Hospitalidade vistani, Jogo das Histórias na fogueira, tenda de Eva e perseguição de Eliza",
        "Arco C (C4)",
        [
            "1: Fogueira do Jogo das Histórias (apostas e relatos)",
            "2: Tenda de Madame Eva (avatar oculta da Vidente)",
            "3 [SEGREDO]: Posição de Eliza (vigiando quem sai à meia-noite)",
            "4 [SEGREDO]: Trilha para a Forca e Refúgio de Arturi contra os mortos",
            "5: Águas calmas de Tser Pool"
        ]
    )
    maps_meta.append(("novo_06", "Acampamento de Tser Pool e Tenda de Madame Eva", "Tser_Pool_Acampamento_Vistani.jpg", img))

    # ---------------------------------------------------------
    # 07. CACHOEIRA DE TSER FALLS, PONTE E ENCRUZILHADA DE RAVENLOFT (C6-C8, O3)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "forest", seed=107)
    draw.rectangle([470, 120, 610, 880], fill=(22, 32, 46, 245), outline=(75, 95, 115, 220), width=3)
    draw_river(draw, [(540, 120), (540, 880)], width=46, bridge_pts=(450, 465, 630, 535))
    draw_road(draw, [(80, 500), (450, 500), (630, 500), (960, 500), (1320, 310)], width=36)
    draw_road(draw, [(960, 500), (1280, 720)], width=34)
    draw_building(draw, (170, 300, 340, 420), "Torre de Vigia (C6)", interior=True)
    draw_marker(draw, 255, 270, "1", "C6 · Torre de Vigia, Sepulturas e Cadáver", pos="right")
    draw_marker(draw, 540, 500, "2", "C7 · Ponte Alta de Tser Falls (Queda de 300m)", pos="right")
    draw_marker(draw, 960, 545, "3", "C8 · Encruzilhada de Ravenloft e Carruagem Negra", pos="left")
    draw_marker(draw, 1120, 370, "4", "O3 · Carvalho Oco (Emboscada de Doru e Cavaleiro)", secret=True, pos="left")
    draw_marker(draw, 1290, 290, "5", "Subida para Castelo Ravenloft", pos="left")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Cachoeira de Tser Falls, Ponte Alta e Encruzilhada de Ravenloft",
        "Torre de vigia (C6), ponte sobre a garganta (C7), encruzilhada da carruagem (C8) e carvalho de Doru (O3)",
        "Arcos C e O (C6, C7, C8, O3)",
        [
            "1: Ruínas da Torre de Vigia e sepulturas (C6)",
            "2: Ponte de Pedra sobre a Cachoeira de Tser Falls (C7)",
            "3: Bifurcação Vallaki / Ravenloft e Carruagem Negra (C8)",
            "4 [SEGREDO]: Carvalho Oco e encontro com Doru em O3",
            "5: Subida para as Muralhas de Ravenloft"
        ]
    )
    maps_meta.append(("novo_07", "Cachoeira de Tser Falls e Encruzilhada de Ravenloft", "Tser_Falls_Encruzilhada_Ravenloft.jpg", img))

    # ---------------------------------------------------------
    # 08. FLORESTA SVALICH PROFUNDA · CAÇADA DOS LOBISOMENS (C10, C11, Q5)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "forest", seed=108)
    rng = random.Random(108)
    draw_road(draw, [(60, 520), (480, 490), (920, 540), (1340, 500)], width=42)
    draw.rectangle([660, 440, 710, 590], fill=(82, 54, 34, 245), outline=(35, 22, 12, 255), width=3)
    trees = [(rng.randint(80, 1320), rng.randint(150, 840), rng.randint(22, 38)) for _ in range(70) if abs(rng.randint(150, 840) - 515) > 65]
    draw_trees(draw, trees, rng)
    draw_marker(draw, 180, 505, "1", "C10 · Floresta Profunda (Brumas e Sinais de Caça)", pos="right")
    draw_marker(draw, 685, 515, "2", "Tronco Caído e Gargalo da Estrada", pos="right")
    draw_marker(draw, 580, 260, "3", "C11 · Flanco Norte da Alcateia (Cobertura)", secret=True, pos="right")
    draw_marker(draw, 720, 740, "4", "Q5 · Emboscada de Kiril, o Alfa (P3 Solo)", secret=True, pos="right")
    draw_marker(draw, 1260, 500, "5", "Rota de Fuga até os Portões de Vallaki", pos="left")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Floresta Svalich Profunda · Caçada da Alcateia",
        "Corredor florestal para C10, C11 (Caçada dos Lobisomens) e Q5 (Retaliação de Kiril)",
        "Arcos C e Q (C10, C11, Q5)",
        [
            "1: Entrada na mata fechada (visibilidade reduzida)",
            "2: Tronco caído na estrada (terreno difícil para carroças/cavalos)",
            "3 [SEGREDO]: Posição elevada de flanco da alcateia",
            "4 [SEGREDO]: Ponto de salto de Kiril e seus caçadores",
            "5: Direção dos Portões de Vallaki / Refúgio"
        ]
    )
    maps_meta.append(("novo_08", "Floresta Svalich Profunda · Caçada da Alcateia", "Floresta_Svalich_Cacada_Alcateia.jpg", img))

    # ---------------------------------------------------------
    # 09. VALLAKI · PLANTA URBANA GERAL, PRAÇA E PORTÕES (C12, D6, F, G, U3, EP2)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "urban", seed=109)
    rng = random.Random(109)
    draw.ellipse((140, 150, 1260, 850), fill=(36, 38, 44, 240), outline=(112, 84, 52, 255), width=8)
    draw_road(draw, [(80, 500), (1320, 500)], width=44, color=(74, 70, 64))
    draw_road(draw, [(700, 120), (700, 880)], width=38, color=(74, 70, 64))
    draw.rectangle([580, 400, 820, 600], fill=(92, 86, 78, 245), outline=(165, 150, 125, 230), width=3)
    draw_building(draw, (240, 320, 410, 440), "N1 · Igreja Sto. Andral")
    draw_building(draw, (460, 260, 630, 370), "N2 · Estalagem Água Azul")
    draw_building(draw, (770, 250, 960, 375), "N3 · Mansão Burgomestre")
    draw_building(draw, (860, 560, 1050, 680), "N4 · Casa Wachter")
    draw_building(draw, (410, 580, 550, 675), "N5 · Arasek")
    draw_building(draw, (1010, 360, 1170, 445), "N6 · Loja Caixões")
    draw_building(draw, (580, 645, 740, 730), "N7 · Brinquedos Blinsky")
    draw_marker(draw, 145, 500, "1", "Portão Ocidental (Sunset Gate)", pos="right")
    draw_marker(draw, 700, 500, "2", "Praça Central · Julgamento (D6) e Conselho (U1)", pos="top")
    draw_marker(draw, 835, 425, "3", "Beco de Emboscada de Izek (F4/G3)", secret=True, pos="right")
    draw_marker(draw, 1255, 500, "4", "Portão Oriental · Defesa (U3j)", pos="left")
    draw_marker(draw, 950, 775, "5", "Muralha Sul · Ruptura da Horda (U3)", secret=True, pos="left")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Vallaki · Planta Urbana Geral, Praça Central, Portões e Muralhas",
        "Locais N1–N7, Praça do Julgamento (D6), Rotas de Izek (F/G) e Defesa na Noite Eterna (U3)",
        "Arcos C12, D–H, U3, EP",
        [
            "1: Portão Ocidental e Igreja de Santo Andral (N1)",
            "2: Praça Central (Palanque de Rahadin em D6, Cartazes em G2, Festival em EP2)",
            "3 [SEGREDO]: Rota de patrulha e emboscada de Izek (F4/G3)",
            "4: Portão Oriental (Defesa de U3j)",
            "5 [SEGREDO]: Setor da Muralha Sul ameaçado em U3"
        ]
    )
    maps_meta.append(("novo_09", "Vallaki · Planta Urbana, Praça e Portões", "Vallaki_Cidade_Praca_Portoes.jpg", img))

    # ---------------------------------------------------------
    # 10. VALLAKI · IGREJA DE SANTO ANDRAL E REFÚGIO DE FRANZ (D1, D2, D5, H3)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "urban", seed=110)
    draw_building(draw, (140, 200, 940, 740), None, interior=True, rooms=[
        (155, 215, 310, 725, "Átrio e Campanário"),
        (310, 215, 720, 725, "Nave Central e Bancos"),
        (720, 215, 925, 520, "Altar do Senhor da Manhã"),
        (720, 520, 925, 725, "Sacristia e Quarto de Yeska")
    ])
    draw.rectangle([980, 200, 1320, 740], fill=(42, 48, 40, 220), outline=(120, 130, 110, 210), width=3)
    draw_building(draw, (1010, 240, 1290, 410), "Tendas dos Refugiados (H3)", roof_color=(88, 76, 58))
    draw_building(draw, (1010, 470, 1290, 680), "Cemitério e Galpão de Milivoj", roof_color=(64, 60, 58))
    draw_marker(draw, 460, 470, "1", "D1 · Nave de Santo Andral (Padre Lucian)", pos="right")
    draw_marker(draw, 825, 320, "2", "D5 · Cripta sob o Altar (Ossos de Sto. Andral)", secret=True, pos="left")
    draw_marker(draw, 825, 650, "3", "Sacristia · Yeska Assustado", pos="left")
    draw_marker(draw, 1150, 710, "4", "D2 · Pátio de Milivoj (Confissão sobre Henrik)", pos="left")
    draw_marker(draw, 1150, 220, "5", "H3 · Acolhimento de Franz e Crianças", pos="left")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Vallaki · Igreja de Santo Andral e Abrigo de Refugiados",
        "Interior da Igreja (N1), Altar dos Ossos (D1/D5), Pátio de Milivoj (D2) e Tendas de Franz (H3)",
        "Arcos D e H (D1, D2, D5, H3)",
        [
            "1: Nave Principal (Padre Lucian Petrovich)",
            "2 [SEGREDO]: Compartimento dos Ossos de Santo Andral sob o Altar",
            "3: Quarto de Yeska e Sacristia",
            "4: Cemitério e Posto de Trabalho de Milivoj (D2)",
            "5: Acampamento de Refugiados de Baróvia e Franz (H3)"
        ]
    )
    maps_meta.append(("novo_10", "Vallaki · Igreja de Santo Andral e Refúgio", "Vallaki_Igreja_Santo_Andral.jpg", img))

    # ---------------------------------------------------------
    # 11. VALLAKI · PÁTIO DE ARASEK E LOJA DE BLINSKY (D3, E1)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "urban", seed=111)
    draw.rectangle([80, 180, 680, 820], fill=(54, 48, 42, 230), outline=(145, 125, 95, 240), width=4)
    draw_building(draw, (110, 210, 380, 410), "Armazém de Günther e Yelena Arasek", roof_color=(88, 62, 46))
    draw_building(draw, (410, 220, 650, 460), None, interior=True, rooms=[
        (425, 235, 635, 445, "Carroça de Carnaval")
    ])
    draw_building(draw, (120, 560, 420, 780), "Carroças Comuns & Suprimentos", roof_color=(72, 58, 44))
    draw_building(draw, (760, 180, 1320, 820), None, interior=True, rooms=[
        (775, 195, 1305, 510, "Salão de Exposição de Brinquedos Macabros"),
        (775, 510, 1040, 805, "Oficina de Blinsky & Piccolo"),
        (1040, 510, 1305, 805, "Depósito de Bonecas (Izek)")
    ])
    draw_marker(draw, 190, 455, "1", "D3 · Pátio de Arasek (Pista sobre Henrik)", pos="right")
    draw_marker(draw, 530, 485, "2", "Carroça de Rictavio (Tigre-de-Sabre)", secret=True, pos="left")
    draw_marker(draw, 1040, 290, "3", "E1 · Balcão de Blinsky (Brinquedo de Arabelle)", pos="top")
    draw_marker(draw, 905, 765, "4", "Oficina e Macaquinho Piccolo", pos="right")
    draw_marker(draw, 1180, 560, "5", "Bonecas Idênticas a Ireena (Feitas para Izek)", secret=True, pos="left")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Vallaki · Pátio de Carroças de Arasek e Brinquedos de Blinsky",
        "Planta combinada para D3 (Pátio de Arasek / Tigre de Rictavio) e E1 (Loja de Gadof Blinsky)",
        "Arcos D, E e G (D3, E1)",
        [
            "1: Escritório de Günther e Yelena Arasek",
            "2 [SEGREDO]: Carroça blindada de Rictavio (distração falsa em D3)",
            "3: Salão da Loja de Brinquedos de Blinsky ('Não é divertido, não é Blinsky!')",
            "4: Bancada de trabalho e Piccolo",
            "5 [SEGREDO]: Estoque de bonecas com o rosto de Ireena para Izek Strazni"
        ]
    )
    maps_meta.append(("novo_11", "Vallaki · Pátio de Arasek e Loja de Blinsky", "Vallaki_Arasek_e_Blinsky.jpg", img))

    # ---------------------------------------------------------
    # 12. LAGO ZAROVICH, MARGEM DE PESCA E ESTRADA DE BARATOK (E4, E5, E7, T4)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "forest", seed=112)
    rng = random.Random(112)
    draw.ellipse((280, 120, 1340, 560), fill=(30, 72, 104, 240), outline=(95, 150, 185, 220), width=4)
    draw_road(draw, [(680, 880), (640, 620), (380, 600), (110, 420)], width=34)
    draw.ellipse((790, 310, 870, 355), fill=(105, 72, 44, 250), outline=(230, 195, 130, 255), width=2)
    draw.ellipse((80, 200, 290, 410), fill=(52, 56, 62, 235), outline=(135, 140, 150, 220), width=3)
    trees = [(rng.randint(100, 1280), rng.randint(580, 840), rng.randint(18, 28)) for _ in range(42)]
    draw_trees(draw, trees, rng)
    draw_marker(draw, 640, 595, "1", "E4 · Margem Sul do Lago Zarovich (Caçadores)", pos="right")
    draw_marker(draw, 830, 332, "2", "Barco de Bluto Krogarov e Arabelle", secret=True, pos="right")
    draw_marker(draw, 390, 600, "3", "E5 · Estrada Oeste rumo ao Lago Baratok", pos="right")
    draw_marker(draw, 185, 305, "4", "E6/T4 · Istmo da Torre de Van Richten e Arturi", pos="right")
    draw_marker(draw, 680, 820, "5", "E7 · Retorno a Vallaki e Acampamento Vistani", pos="right")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Lago Zarovich, Margem de Pesca e Estrada até Baratok",
        "Margem dos caçadores (E4), barco de Bluto, trilha para Baratok (E5) e exterior da Torre (E6/T4)",
        "Arcos E e T (E4, E5, E7, T4)",
        [
            "1: Margem Sul do Lago Zarovich (caçadores de Vallaki)",
            "2 [SEGREDO]: Barco de Bluto Krogarov no lago",
            "3: Estrada de terra rumo ao Lago Baratok (E5)",
            "4: Península da Torre de Khazan / Encontro de Van Richten e Arturi (T4)",
            "5: Caminho de regresso a Vallaki (E7)"
        ]
    )
    maps_meta.append(("novo_12", "Lago Zarovich e Estrada até Baratok", "Lago_Zarovich_e_Estrada_Baratok.jpg", img))

    # ---------------------------------------------------------
    # 13. LAGO BARATOK, SUPRIMENTOS DE EZMERELDA E VIGÍLIA DO COVIL (L1-L3, Q7)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "forest", seed=113)
    rng = random.Random(113)
    draw.ellipse((60, 140, 520, 540), fill=(28, 68, 98, 240), outline=(85, 140, 175, 215), width=3)
    draw_road(draw, [(260, 850), (480, 620), (780, 480), (1080, 340)], width=28, color=(76, 66, 52))
    draw.polygon([(980, 160), (1320, 160), (1320, 780), (1040, 680), (960, 420)], fill=(58, 56, 62, 235), outline=(135, 130, 140, 220), width=3)
    trees = [(rng.randint(120, 940), rng.randint(520, 840), rng.randint(18, 30)) for _ in range(45)]
    draw_trees(draw, trees, rng)
    draw_marker(draw, 280, 780, "1", "L1 · Trilha de Caça para Localizar o Covil", pos="right")
    draw_marker(draw, 420, 480, "2", "L2 · Margem do Lago Baratok (Cache de Ezmerelda)", pos="right")
    draw_marker(draw, 760, 470, "3", "L3 · Depressão Protegida de Vigília na Floresta", pos="left")
    draw_marker(draw, 1080, 320, "4", "Entrada Principal do Covil (Z1) e Guardas", pos="left")
    draw_marker(draw, 1180, 540, "5", "Encosta Rochosa e Fenda Superior (Z8 / Q7)", secret=True, pos="left")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Lago Baratok, Suprimentos de Ezmerelda e Vigília do Covil",
        "Aproximação ao Covil dos Lobisomens: Lago Baratok (L2), Ponto de Vigília (L3) e Acessos Z1/Z8 (L4/Q7)",
        "Arcos L e Q (L1, L2, L3, Q7)",
        [
            "1: Trilha da Floresta de Baratok (L1)",
            "2: Margem Rochosa do Lago Baratok (Suprimentos ocultos de Ezmerelda em L2)",
            "3: Depressão camuflada para observar a alcateia (L3)",
            "4: Boca da Caverna Principal (Z1 da planta do Covil)",
            "5 [SEGREDO]: Subida lateral para a Fenda Z8 e Santuário da Mãe Noite"
        ]
    )
    maps_meta.append(("novo_13", "Lago Baratok e Vigília do Covil dos Lobisomens", "Lago_Baratok_Vigilia_Covil.jpg", img))

    # ---------------------------------------------------------
    # 14. MONTE GHAKIS · NEVASCA, AVALANCHE, BODAKS E CAVERNAS DE GELO (R1-R4k)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "snow", seed=114)
    rng = random.Random(114)
    draw_road(draw, [(100, 780), (340, 640), (580, 440), (860, 320), (1220, 260)], width=30, color=(125, 140, 160), border=(75, 90, 110))
    draw_building(draw, (700, 480, 980, 740), "Ruínas do Covil dos Bodaks (R4j)", interior=True)
    draw_building(draw, (1040, 340, 1310, 680), None, interior=True, rooms=[
        (1055, 355, 1295, 510, "Túnel de Gelo Translúcido"),
        (1055, 510, 1295, 665, "Câmara Congelada")
    ])
    trees = [(rng.randint(80, 660), rng.randint(200, 820), rng.randint(16, 26)) for _ in range(35)]
    draw_trees(draw, trees, rng, snow=True)
    draw_marker(draw, 140, 740, "1", "R3/R4a · Base da Subida com Kasimir (Frio 6)", pos="right")
    draw_marker(draw, 350, 580, "2", "R4d · Platô Exposto da Nevasca", pos="right")
    draw_marker(draw, 580, 380, "3", "R4i · Corredor da Avalanche e Rochas de Abrigo", pos="right")
    draw_marker(draw, 840, 765, "4", "R4j · Ruínas Congeladas · Covil dos Bodaks", secret=True, pos="left")
    draw_marker(draw, 1175, 290, "5", "R4k · Entrada das Cavernas de Gelo rumo a Soldav", pos="left")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Monte Ghakis · Trilha da Nevasca, Avalanche, Bodaks e Cavernas de Gelo",
        "Expedição pela montanha após Tsolenka: Frio 6, Avalanche (R4i), Bodaks (R4j) e Cavernas (R4k)",
        "Arco R (R1–R4k)",
        [
            "1: Início da subida íngreme com Kasimir (R4a)",
            "2: Trecho aberto da Nevasca (Ambiente Montanha Dif. 17, Frio 6)",
            "3: Encosta da Avalanche e saliências rochosas de escape (R4i)",
            "4 [SEGREDO]: Ruínas do Covil dos Bodaks (R4j)",
            "5: Passagem subterrânea das Cavernas de Gelo (R4k)"
        ]
    )
    maps_meta.append(("novo_14", "Monte Ghakis · Nevasca, Avalanche e Cavernas", "Monte_Ghakis_Trilha_Cavernas_Bodaks.jpg", img))

    # ---------------------------------------------------------
    # 15. VILA DE SOLDAV E SANTUÁRIO CAVERNOSO DAS ROZANA (R5-R5f, T1)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "snow", seed=115)
    draw.ellipse((80, 200, 780, 820), fill=(52, 58, 66, 235), outline=(145, 130, 105, 240), width=4)
    draw_building(draw, (280, 260, 580, 440), "Grande Salão da Liderança (R5d)", interior=True)
    draw_building(draw, (140, 480, 320, 620), "Cabanas do Clã", roof_color=(92, 68, 48))
    draw_building(draw, (520, 500, 710, 650), "Tenda dos Caçadores", roof_color=(92, 68, 48))
    draw_building(draw, (840, 200, 1320, 820), None, interior=True, rooms=[
        (855, 215, 1305, 420, "Altar da Caçadora (Lança)"),
        (855, 420, 1305, 620, "Altar da Tecelã (Pântano)"),
        (855, 620, 1305, 805, "Altar da Vidente (Montanha)")
    ])
    draw_marker(draw, 110, 445, "1", "R5 · Portão de Soldav (Hospitalidade)", pos="right")
    draw_marker(draw, 430, 230, "2", "R5d · Grande Salão (Cerunnos e Prazo de Diona)", pos="right")
    draw_marker(draw, 390, 700, "3", "Pátio de Provas Físicas e Fogueira Tribal", pos="right")
    draw_marker(draw, 1080, 175, "4", "R5f / T1 · Santuário Cavernoso das Três Rozana", pos="left")
    draw_marker(draw, 1080, 845, "5", "Mural Antigo: Segredo dos Santuários e do Sonhador", secret=True, pos="left")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Vila Montanhesa de Soldav e Santuário das Rozana",
        "Aldeia berserker de Soldav (R5/R5d) e Caverna Sagrada das Três Damas (R5f e retorno em T1)",
        "Arcos R e T (R5–R5f, T1)",
        [
            "1: Entrada de Soldav (recepção após as cavernas de gelo)",
            "2: Casa da Liderança e Jogos Sociais (R5d)",
            "3: Arena de Provas e Fogueira Central",
            "4: Santuário das Rozana (Altares da Caçadora, Tecelã e Vidente - R5f)",
            "5 [SEGREDO]: Inscrições sobre a reconsecração dos três santuários (T1)"
        ]
    )
    maps_meta.append(("novo_15", "Vila de Soldav e Santuário das Rozana", "Soldav_Vila_e_Santuario_Rozana.jpg", img))

    # ---------------------------------------------------------
    # 16. OS TRÊS SANTUÁRIOS (BOSQUE, PÂNTANO, MONTANHA) E LAGO DO SONHADOR (T3, U3i)
    # ---------------------------------------------------------
    img, draw = create_gothic_canvas(1400, 1000, "sanctuary", seed=116)
    draw.line([(700, 115), (700, 885)], fill=(168, 142, 102, 200), width=3)
    draw.line([(40, 500), (1360, 500)], fill=(168, 142, 102, 200), width=3)
    draw.ellipse((180, 190, 540, 440), fill=(32, 54, 42, 230), outline=(120, 175, 135, 220), width=3)
    for a in range(0, 360, 60):
        rx = 360 + int(math.cos(math.radians(a)) * 110)
        ry = 315 + int(math.sin(math.radians(a)) * 85)
        draw.ellipse((rx - 10, ry - 10, rx + 10, ry + 10), fill=(165, 175, 185, 245))
    draw.ellipse((860, 190, 1220, 440), fill=(42, 58, 38, 230), outline=(165, 195, 120, 220), width=3)
    for a in range(0, 360, 45):
        rx = 1040 + int(math.cos(math.radians(a)) * 115)
        ry = 315 + int(math.sin(math.radians(a)) * 85)
        draw.rectangle([rx - 8, ry - 8, rx + 8, ry + 8], fill=(180, 170, 150, 245))
    draw.ellipse((180, 560, 540, 820), fill=(48, 56, 74, 235), outline=(150, 185, 225, 220), width=3)
    draw.polygon([(360, 610), (270, 760), (450, 760)], outline=(210, 225, 250, 220), width=3)
    draw.ellipse((820, 545, 1260, 835), fill=(28, 62, 92, 240), outline=(110, 175, 220, 230), width=3)
    draw.ellipse((980, 640, 1100, 740), fill=(78, 52, 88, 245), outline=(235, 180, 255, 240), width=3)

    draw_marker(draw, 360, 160, "1", "T3f/T3m · Santuário do Pântano e Monumento de Marina", pos="bottom")
    draw_marker(draw, 1040, 160, "2", "T3l · Megálitos da Caçadora e Rito dos Martikov", pos="bottom")
    draw_marker(draw, 360, 535, "3", "Santuário da Vidente (Progresso 8 / Consequência 6)", pos="bottom")
    draw_marker(draw, 1040, 535, "4", "U3i · Lago e Coração do Sonhador (Negociação/Solo P4)", secret=True, pos="bottom")
    draw_header_and_legend(
        draw, 1400, 1000,
        "Os Três Santuários das Damas e o Lago do Sonhador",
        "Quadro tático quádruplo para os Ritos de Reconsecração (T3f, T3l, T3m) e o Coração do Sonhador (U3i)",
        "Arcos T e U (T3, U3i)",
        [
            "1: Santuário do Pântano (Berez) e Monumento de Marina (Sergei em T3f / Rito em T3m)",
            "2: Círculo Megalítico da Caçadora (Urwin e Davian em T3l)",
            "3: Altar da Vidente (Ambiente Santuários Dif. 20, Progresso 8 / Consequência 6)",
            "4 [SEGREDO]: Ilha Onírica do Coração do Sonhador (U3i · Bênção do Sonhador)"
        ]
    )
    maps_meta.append(("novo_16", "Os Três Santuários e Lago do Sonhador", "Santuarios_Megalitos_e_Lago_Sonhador.jpg", img))

    for key, title, filename, image in maps_meta:
        out1 = os.path.join(MAPS_OUT, filename)
        image.save(out1, "JPEG", quality=92)
        if os.path.exists(VAULT_ANEXOS):
            out2 = os.path.join(VAULT_ANEXOS, filename)
            image.save(out2, "JPEG", quality=92)
        print(f"Saved {filename} ({os.path.getsize(out1)} bytes)")

    if os.path.exists(VAULT_ANEXOS):
        for fn in os.listdir(VAULT_ANEXOS):
            if fn.lower().endswith((".jpg", ".png")):
                src_f = os.path.join(VAULT_ANEXOS, fn)
                dst_f = os.path.join(MAPS_OUT, fn)
                if not os.path.exists(dst_f):
                    shutil.copy2(src_f, dst_f)

    return maps_meta


if __name__ == "__main__":
    generate_all_16_maps()
    print("All 16 new maps regenerated and synced!")
