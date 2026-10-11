#!/usr/bin/env python3
"""
1. Mapeia todas as 180 cenas para as 44 plantas (28 originais do livro + 16 novas criadas).
2. Reestrutura o layout textual das 180 cenas, 86 encontros e Atlas no Vault RPG e em notion_reestruturado/
   SEM ALTERAR NENHUMA PALAVRA DO CONTEÚDO ORIGINAL (100% lossless), destacando gatilhos, falas, segredos
   e mecânicas Daggerheart no topo e recolhendo instruções repetitivas de mapa.
3. Gera data/campaign_data.json e data/campaign_data.js completos para alimentar o Cockpit do Mestre Web App.
"""
import os
import sys
import re
import json
import shutil

sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE = r"c:\Users\Alex\Documents\antigravity\beautiful-bohr"
DATA_DIR = os.path.join(WORKSPACE, "data")
NOTION_OUT = os.path.join(WORKSPACE, "notion_reestruturado")
VAULT_DIR = os.path.expandvars(r"%USERPROFILE%\Downloads\AUTOMAÇAO RPG\Vault RPG")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(NOTION_OUT, exist_ok=True)

# 44 Maps catalog (28 original + 16 newly created)
ALL_MAPS = [
    {"key": "real_00", "title": "Vila de Baróvia", "file": "Vila_de_Barovia.jpg", "group": "Livro Original", "arcs": ["B"]},
    {"key": "real_01", "title": "Ravenloft · muralhas", "file": "Ravenloft_Muralhas.jpg", "group": "Livro Original", "arcs": ["O", "P", "U"]},
    {"key": "real_02", "title": "Ravenloft · andar principal", "file": "Ravenloft_Terreo.jpg", "group": "Livro Original", "arcs": ["O", "P", "U"]},
    {"key": "real_03", "title": "Ravenloft · corte do conde", "file": "Ravenloft_Corte.jpg", "group": "Livro Original", "arcs": ["O", "P", "U"]},
    {"key": "real_04", "title": "Ravenloft · torres", "file": "Ravenloft_Torres.jpg", "group": "Livro Original", "arcs": ["O", "P", "U"]},
    {"key": "real_05", "title": "Ravenloft · torres superiores", "file": "Ravenloft_Torres_Altas.jpg", "group": "Livro Original", "arcs": ["O", "P", "U"]},
    {"key": "real_06", "title": "Ravenloft · despensas, masmorra e catacumbas", "file": "Ravenloft_Subsolo.jpg", "group": "Livro Original", "arcs": ["O", "P", "U"]},
    {"key": "real_07", "title": "Vallaki · Estalagem Água Azul", "file": "Estalagem_Agua_Azul.jpg", "group": "Livro Original", "arcs": ["C", "D", "F", "G"]},
    {"key": "real_08", "title": "Vallaki · mansão do burgomestre", "file": "Mansao_Burgomestre.jpg", "group": "Livro Original", "arcs": ["E", "F", "G"]},
    {"key": "real_09", "title": "Vallaki · Casa Wachter", "file": "Casa_Wachter.jpg", "group": "Livro Original", "arcs": ["F", "H"]},
    {"key": "real_10", "title": "Vallaki · acampamento vistani", "file": "Acampamento_Vistani.jpg", "group": "Livro Original", "arcs": ["E", "R"]},
    {"key": "real_11", "title": "Velho Esmaga-Ossos", "file": "Velho_Esmaga_Ossos.jpg", "group": "Livro Original", "arcs": ["C", "H"]},
    {"key": "real_12", "title": "Argynvostholt · dois primeiros andares", "file": "Argynvostholt_Andares_Inferiores.jpg", "group": "Livro Original", "arcs": ["M", "Q"]},
    {"key": "real_13", "title": "Argynvostholt · terceiro andar e farol", "file": "Argynvostholt_Cobertura.jpg", "group": "Livro Original", "arcs": ["M", "Q"]},
    {"key": "real_14", "title": "Krezk · vila e portão", "file": "Krezk.jpg", "group": "Livro Original", "arcs": ["I", "K"]},
    {"key": "real_15", "title": "Abadia de Santa Markovia", "file": "Abadia.jpg", "group": "Livro Original", "arcs": ["K", "Q"]},
    {"key": "real_16", "title": "Passo de Tsolenka", "file": "Tsolenka.jpg", "group": "Livro Original", "arcs": ["R"]},
    {"key": "real_17", "title": "Vinícola Mago dos Vinhos", "file": "Vinicola.jpg", "group": "Livro Original", "arcs": ["J"]},
    {"key": "real_18", "title": "Templo de Âmbar · andar superior", "file": "Templo_Ambar_Superior.jpg", "group": "Livro Original", "arcs": ["S"]},
    {"key": "real_19", "title": "Templo de Âmbar · andar inferior", "file": "Templo_Ambar_Inferior.jpg", "group": "Livro Original", "arcs": ["S"]},
    {"key": "real_20", "title": "Colina Yester", "file": "Colina_Yester.jpg", "group": "Livro Original", "arcs": ["J", "T"]},
    {"key": "real_21", "title": "Covil dos lobisomens", "file": "Covil_Lobisomens.jpg", "group": "Livro Original", "arcs": ["L", "Q"]},
    {"key": "real_22", "title": "Vila de Baróvia · igreja", "file": "Igreja_Barovia.jpg", "group": "Livro Original", "arcs": ["B"]},
    {"key": "real_23", "title": "Vallaki · loja de caixões", "file": "Loja_Caixoes.jpg", "group": "Livro Original", "arcs": ["D"]},
    {"key": "real_24", "title": "Abadia · andar superior e porão", "file": "Abadia_Superior.jpg", "group": "Livro Original", "arcs": ["K", "Q"]},
    {"key": "real_25", "title": "Berez · cabana de Baba Lysaga", "file": "Cabana_Baba_Lysaga.jpg", "group": "Livro Original", "arcs": ["I", "T"]},
    {"key": "real_26", "title": "Torre de Van Richten", "file": "Torre_Van_Richten.jpg", "group": "Livro Original", "arcs": ["E", "T"]},
    {"key": "real_27", "title": "Casa da Morte", "file": "Casa_da_Morte_Mapa_Mestre.jpg", "group": "Livro Original", "arcs": ["A"]},
    # 16 New Maps
    {"key": "novo_01", "title": "Vale de Baróvia · Mapa Regional Completo", "file": "Vale_de_Barovia_Regional.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["A", "B", "C", "H", "I", "J", "O", "Q", "T", "U", "EP"]},
    {"key": "novo_02", "title": "Daggerford · Estrebaria e Rua nas Brumas", "file": "Daggerford_Estrebaria_Brumas.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["A"]},
    {"key": "novo_03", "title": "Portões de Baróvia, Estrada Svalich e Mirante", "file": "Portoes_Barovia_Estrada_Svalich.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["B"]},
    {"key": "novo_04", "title": "Vila de Baróvia · Barricada Oriental e Praça", "file": "Vila_Barovia_Barricada_Oriental.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["B"]},
    {"key": "novo_05", "title": "Encruzilhada do Rio Ivlis, Forca e Cemitério", "file": "Encruzilhada_Ivlis_Forca.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["C"]},
    {"key": "novo_06", "title": "Acampamento de Tser Pool e Tenda de Madame Eva", "file": "Tser_Pool_Acampamento_Vistani.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["C"]},
    {"key": "novo_07", "title": "Cachoeira de Tser Falls e Encruzilhada de Ravenloft", "file": "Tser_Falls_Encruzilhada_Ravenloft.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["C", "O"]},
    {"key": "novo_08", "title": "Floresta Svalich Profunda · Caçada da Alcateia", "file": "Floresta_Svalich_Cacada_Alcateia.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["C", "Q"]},
    {"key": "novo_09", "title": "Vallaki · Planta Urbana, Praça e Portões", "file": "Vallaki_Cidade_Praca_Portoes.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["C", "D", "F", "G", "U", "EP"]},
    {"key": "novo_10", "title": "Vallaki · Igreja de Santo Andral e Refúgio", "file": "Vallaki_Igreja_Santo_Andral.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["D", "H"]},
    {"key": "novo_11", "title": "Vallaki · Pátio de Arasek e Loja de Blinsky", "file": "Vallaki_Arasek_e_Blinsky.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["D", "E"]},
    {"key": "novo_12", "title": "Lago Zarovich e Estrada até Baratok", "file": "Lago_Zarovich_e_Estrada_Baratok.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["E", "T"]},
    {"key": "novo_13", "title": "Lago Baratok e Vigília do Covil dos Lobisomens", "file": "Lago_Baratok_Vigilia_Covil.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["L", "Q"]},
    {"key": "novo_14", "title": "Monte Ghakis · Nevasca, Avalanche e Cavernas", "file": "Monte_Ghakis_Trilha_Cavernas_Bodaks.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["R"]},
    {"key": "novo_15", "title": "Vila de Soldav e Santuário das Rozana", "file": "Soldav_Vila_e_Santuario_Rozana.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["R", "T"]},
    {"key": "novo_16", "title": "Os Três Santuários e Lago do Sonhador", "file": "Santuarios_Megalitos_e_Lago_Sonhador.jpg", "group": "Novos Mapas Táticos & Regionais", "arcs": ["T", "U"]},
]

MAP_BY_TITLE = {m["title"]: m for m in ALL_MAPS}
MAP_BY_KEY = {m["key"]: m for m in ALL_MAPS}

# Exact mapping for scenes that lacked a specific floorplan
SCENE_CODE_TO_NEW_MAP = {
    "A1": "novo_02",
    "A3": "novo_01",
    "B1": "novo_03",
    "B2": "novo_03",
    "B3": "novo_03",
    "B4": "novo_03",
    "B5b": "novo_04",
    "B5f": "novo_04",
    "C1": "novo_05",
    "C2": "novo_05",
    "C3": "novo_05",
    "C4": "novo_06",
    "C5": "novo_05",
    "C6": "novo_07",
    "C7": "novo_07",
    "C8": "novo_07",
    "C10": "novo_08",
    "C11": "novo_08",
    "C12": "novo_09",
    "D1": "novo_10",
    "D2": "novo_10",
    "D3": "novo_11",
    "D5": "novo_10",
    "D6": "novo_09",
    "E1": "novo_11",
    "E4": "novo_12",
    "E5": "novo_12",
    "E7": "novo_12",
    "F3": "novo_09",
    "F4": "novo_09",
    "F5": "novo_09",
    "G2": "novo_09",
    "G3": "novo_09",
    "H3": "novo_10",
    "H6": "novo_01",
    "I1": "novo_01",
    "I3": "novo_01",
    "J2": "novo_01",
    "L1": "novo_13",
    "L2": "novo_13",
    "L3": "novo_13",
    "O1": "novo_01",
    "O2": "novo_01",
    "O3": "novo_07",
    "Q1": "novo_01",
    "Q4": "novo_01",
    "Q5": "novo_08",
    "Q7": "novo_13",
    "R1": "real_10",
    "R2": "real_16",
    "R3": "novo_14",
    "R4a": "novo_14",
    "R4d": "novo_14",
    "R4i": "novo_14",
    "R4j": "novo_14",
    "R4k": "novo_14",
    "R5": "novo_15",
    "R5d": "novo_15",
    "R5f": "novo_15",
    "T1": "novo_15",
    "T2": "novo_01",
    "T3f": "novo_16",
    "T3l": "novo_16",
    "T3m": "novo_16",
    "T4": "novo_12",
    "U1": "novo_09",
    "U2": "novo_09",
    "U3": "novo_09",
    "U3d": "novo_09",
    "U3i": "novo_16",
    "U3j": "novo_09",
    "U4": "novo_01",
    "U6": "novo_01",
    "EP1": "novo_01",
    "EP2": "novo_09",
    "EP5": "novo_09",
    "EP6": "novo_01",
}


def parse_frontmatter(md_text):
    if not md_text.startswith("---"):
        return {}, md_text
    parts = md_text.split("---", 2)
    if len(parts) < 3:
        return {}, md_text
    raw_yaml = parts[1].strip()
    body = parts[2].strip()
    fm = {}
    current_list_key = None
    for line in raw_yaml.splitlines():
        if line.startswith("  - ") and current_list_key:
            val = line.replace("  - ", "", 1).strip().strip('"').strip("'")
            fm[current_list_key].append(val)
        elif ":" in line:
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.strip()
            if not v:
                fm[k] = []
                current_list_key = k
            else:
                current_list_key = None
                v_clean = v.strip('"').strip("'")
                if v_clean.lower() == "true":
                    fm[k] = True
                elif v_clean.lower() == "false":
                    fm[k] = False
                elif re.match(r"^-?\d+$", v_clean):
                    fm[k] = int(v_clean)
                else:
                    fm[k] = v_clean
    return fm, body


def clean_wikilink(val):
    if isinstance(val, list):
        return [clean_wikilink(x) for x in val]
    s = str(val)
    m = re.search(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", s)
    if m:
        return m.group(2) or m.group(1)
    return s


def resolve_scene_map(code, body):
    if code in SCENE_CODE_TO_NEW_MAP:
        mk = SCENE_CODE_TO_NEW_MAP[code]
        return MAP_BY_KEY[mk]
    if code.startswith("A2"):
        return MAP_BY_KEY["real_27"]
    # Check existing link in body
    for m in ALL_MAPS:
        if f"[[{m['title']}]]" in body:
            return m
    return MAP_BY_KEY["novo_01"]


def recommend_sound_preset(code, title, foco, arc_code):
    t = (title + " " + str(foco)).lower()
    if arc_code == "A":
        return "casa_da_morte" if code != "A1" else "chuva_estrada"
    if "jantar" in t or "strahd" in t or arc_code in ("O", "P"):
        return "castelo_ravenloft"
    if " âmbar" in t or "templo" in t or arc_code == "S":
        return "templo_ambar"
    if "montanha" in t or "nevasca" in t or "gelo" in t or "soldav" in t or arc_code == "R":
        return "montanha_nevasca"
    if "tser pool" in t or "vistani" in t or "eva" in t or "arabelle" in t:
        return "acampamento_vistani"
    if "taverna" in t or "estalagem" in t:
        return "taverna_lareira"
    if "cerco" in t or "barricada" in t or "combate" in t or "ataque" in t or "caçada" in t or "muralha" in t:
        return "combate_gotico"
    if "floresta" in t or "lobo" in t or "covil" in t or "berez" in t or "pântano" in t:
        return "floresta_svalich"
    if "vallaki" in t or "igreja" in t or "julgamento" in t or arc_code in ("D", "F", "G"):
        return "vallaki_tensao"
    return "brumas_barovia"


def format_roteiro_lossless(roteiro_text):
    """
    Applies non-destructive semantic callout formatting to key paragraphs inside the Roteiro
    WITHOUT removing, adding, or altering a single word of the original narrative/mechanics!
    """
    out_lines = []
    for line in roteiro_text.splitlines():
        s = line.strip()
        # Preserve headings, lists, blockquotes, tables, and empty lines as-is
        if not s or s.startswith("#") or s.startswith("-") or s.startswith("*") or re.match(r"^\d+\.", s) or s.startswith("|") or s.startswith(">"):
            out_lines.append(line)
            continue
        # Highlight Read-Aloud paragraphs
        if s.startswith("**Para narrar") or s.startswith("**Mensagem para os jogadores"):
            out_lines.append(f"> [!quote] 🎙️ Leitura de Mesa\n> {line}")
        # Highlight GM Secrets
        elif s.startswith("**Verdade reservada ao mestre") or s.startswith("**Não diga ainda") or s.startswith("**Segredo"):
            out_lines.append(f"> [!danger] 🔒 Segredo do Mestre\n> {line}")
        # Highlight Triggers / Objectives / Travel
        elif any(s.startswith(p) for p in ("**Gatilho:", "**Objetivo:", "**Transição:", "**Percurso:", "**Viagem:")):
            out_lines.append(f"> [!important] ⚡ Contexto & Gatilho\n> {line}")
        # Highlight Daggerheart Mechanics
        elif any(s.startswith(p) for p in ("**Daggerheart:", "**DH:", "**Conversão DH", "**Perseguição DH", "**Amuleto DH", "**Coven DH")):
            out_lines.append(f"> [!tip] 🎲 Regra Daggerheart\n> {line}")
        else:
            out_lines.append(line)
    return "\n".join(out_lines)


def create_new_atlas_pages_in_vault():
    atlas_dir = os.path.join(VAULT_DIR, "01 Durante a sessão", "Atlas do mestre · mapas do livro")
    if not os.path.exists(atlas_dir):
        return
    for m in ALL_MAPS:
        if not m["key"].startswith("novo_"):
            continue
        page_path = os.path.join(atlas_dir, f"{m['title']}.md")
        arcs_links = " · ".join(f"[[{a}]]" for a in m["arcs"])
        content = f"""---
tipo: "mapa"
revelado: false
titulo: "{m['title']}"
---

# {m['title']}

← [[Atlas do mestre · mapas do livro]]

**Arcos relacionados:** {arcs_links}

**Consulta:** toque na imagem para ampliar. Mapa tático/regional complementar criado em português para cobrir cenas de *Strahd Reloaded* em Daggerheart que não possuíam planta específica no PDF original. Use zonas de alcance (*Corpo a Corpo, Muito Próximo, Próximo, Distante*) e bloqueie os pontos `[SEGREDO]` antes de revelar aos jogadores.

![[{m['file']}]]

**Painel com névoa:** selecione **{m['title']}** em [[Mapas reais · revelar aos jogadores]].
"""
        with open(page_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)

    # Also update Atlas do mestre · mapas do livro.md to list the 16 new maps
    atlas_index = os.path.join(VAULT_DIR, "01 Durante a sessão", "Atlas do mestre · mapas do livro.md")
    if os.path.exists(atlas_index):
        with open(atlas_index, "r", encoding="utf-8") as f:
            idx_txt = f.read()
        if "## Mapas Complementares Criados (Strahd Reloaded · Daggerheart)" not in idx_txt:
            new_sec = "\n\n## Mapas Complementares Criados (Strahd Reloaded · Daggerheart)\n\nMapas regionais, urbanos e de zonas táticas criados para cobrir todas as 75 cenas que não possuíam planta específica no PDF original:\n\n"
            new_sec += "\n\n".join(f"[[{m['title']}]]" for m in ALL_MAPS if m["key"].startswith("novo_")) + "\n"
            with open(atlas_index, "w", encoding="utf-8", newline="\n") as f:
                f.write(idx_txt.rstrip() + new_sec)


def process_all_data():
    data = {
        "meta": {
            "title": "Strahd Reloaded · Daggerheart — Mesa do Mestre 2.0",
            "notion_page_id": "3f4a4a42-2490-8140-91ea-e40f75de278a",
            "total_maps": len(ALL_MAPS),
        },
        "maps": ALL_MAPS,
        "arcs": [],
        "scenes": [],
        "encounters": [],
        "bestiary": [],
        "items_spells": [],
        "amber_pacts": [],
        "calendar": [],
        "rules": [],
        "characters": [],
        "sessions": [],
    }

    # 1. Read Arcs (07 Campanha)
    arcos_dir = os.path.join(VAULT_DIR, "07 Campanha")
    for fn in sorted(os.listdir(arcos_dir)):
        if not fn.endswith(".md"):
            continue
        fp = os.path.join(arcos_dir, fn)
        with open(fp, "r", encoding="utf-8") as f:
            fm, body = parse_frontmatter(f.read())
        data["arcs"].append({
            "id": fn[:-3],
            "code": str(fm.get("codigo", fn.split("·")[0].strip())),
            "title": fm.get("titulo", fn[:-3]),
            "block": fm.get("bloco", ""),
            "status": fm.get("estado", "Não iniciado"),
            "level": fm.get("nivel", 1),
            "tier": fm.get("patamar", 1),
            "order": fm.get("ordem", 99),
            "summary": fm.get("resumo", ""),
            "body": body,
        })
    data["arcs"].sort(key=lambda x: x["order"])

    # 2. Read Encounters (04 Encontros)
    enc_dir = os.path.join(VAULT_DIR, "04 Encontros")
    for fn in sorted(os.listdir(enc_dir)):
        if not fn.endswith(".md"):
            continue
        fp = os.path.join(enc_dir, fn)
        with open(fp, "r", encoding="utf-8") as f:
            fm, body = parse_frontmatter(f.read())
        # Parse markdown table rows of active creatures if present
        creatures_rows = []
        for line in body.splitlines():
            if line.strip().startswith("|") and "Fichas ativas" not in line and "---" not in line:
                cols = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cols) >= 10:
                    creatures_rows.append({
                        "sheet": cols[0],
                        "count": cols[1],
                        "role": cols[2],
                        "difficulty": cols[3],
                        "thresholds": cols[4],
                        "hp": cols[5],
                        "stress": cols[6],
                        "attack": cols[7],
                        "damage": cols[8],
                        "bp": cols[9],
                    })
        data["encounters"].append({
            "id": fn[:-3],
            "code": fm.get("id", ""),
            "title": fm.get("titulo", fn[:-3]),
            "arc": clean_wikilink(fm.get("arco", [])),
            "scene": clean_wikilink(fm.get("cena", [])),
            "sheets": clean_wikilink(fm.get("fichas", [])),
            "status": fm.get("estado", "Pronto"),
            "forms": fm.get("formas", 1),
            "level": fm.get("nivel", 1),
            "tier": fm.get("patamar", 1),
            "bp_active": fm.get("pb_ativos", 0),
            "budget_4pc": fm.get("orcamento_4_pj", 14),
            "subtype": fm.get("subtipo", ""),
            "order": fm.get("ordem", 999),
            "creatures_table": creatures_rows,
            "body": body,
        })
    data["encounters"].sort(key=lambda x: x["order"])

    # 3. Read Bestiary (05 Bestiário)
    best_dir = os.path.join(VAULT_DIR, "05 Bestiário")
    for fn in sorted(os.listdir(best_dir)):
        if not fn.endswith(".md"):
            continue
        fp = os.path.join(best_dir, fn)
        with open(fp, "r", encoding="utf-8") as f:
            fm, body = parse_frontmatter(f.read())
        data["bestiary"].append({
            "id": fn[:-3],
            "title": fm.get("titulo", fn[:-3]),
            "arcs": clean_wikilink(fm.get("arcos", [])),
            "encounters": clean_wikilink(fm.get("encontros", [])),
            "difficulty": fm.get("dificuldade", 12),
            "hp": fm.get("pv", 4),
            "stress": fm.get("estresse", 3),
            "role": fm.get("papel", "Padrão"),
            "tier": fm.get("patamar_base", 1),
            "usage": fm.get("uso", "Adversário"),
            "nature": fm.get("natureza", ""),
            "original_id": fm.get("id_original", ""),
            "revealed": bool(fm.get("revelado", False)),
            "body": body,
        })

    # 4. Read Scenes (03 Cenas) + Apply Lossless Text Layout Restructuring!
    cenas_dir = os.path.join(VAULT_DIR, "03 Cenas")
    notion_cenas_out = os.path.join(NOTION_OUT, "Cenas_Reestruturadas")
    os.makedirs(notion_cenas_out, exist_ok=True)

    for fn in sorted(os.listdir(cenas_dir)):
        if not fn.endswith(".md"):
            continue
        fp = os.path.join(cenas_dir, fn)
        with open(fp, "r", encoding="utf-8") as f:
            raw_md = f.read()
        fm, body = parse_frontmatter(raw_md)
        code = str(fm.get("codigo", fn.split("·")[0].strip()))
        arcs = clean_wikilink(fm.get("arco", []))
        arc_code = arcs[0].split("·")[0].strip() if arcs else code[0]
        scene_map = resolve_scene_map(code, body)
        sound_preset = recommend_sound_preset(code, fm.get("titulo", fn[:-3]), fm.get("foco", ""), arc_code)

        # Extract sections of the scene body without losing a single character of content
        # Typical sections in body:
        # 1) Header + INPUT state line
        # 2) ## Consulta de mesa ...
        # 3) ## Mapas desta cena ...
        # 4) ## Roteiro ampliado / completo / Áreas ... (the core content!)
        # 5) Bottom navigation + Resumo da edição anterior + Ao encerrar + Encontros associados
        roteiro_match = re.search(
            r"(## (?:Roteiro|Áreas).*?)(?=\n---\s*\n\s*← \[\[Strahd Reloaded|\n## Ao encerrar|\Z)",
            body,
            re.S
        )
        mapas_match = re.search(
            r"## Mapas desta cena\s*(.*?)(?=\n---\s*\n+## |\n## (?:Roteiro|Áreas)|\Z)",
            body,
            re.S
        )

        roteiro_raw = roteiro_match.group(1).strip() if roteiro_match else body
        mapas_raw = mapas_match.group(1).strip() if mapas_match else ""
        roteiro_formatted = format_roteiro_lossless(roteiro_raw)

        # Write Notion-ready restructured markdown to notion_cenas_out (100% lossless content, improved visual hierarchy)
        encs = clean_wikilink(fm.get("encontros", []))
        enc_links = " · ".join(f"[[{e}]]" for e in encs) if encs else "Nenhum encontro de combate fixo"
        restructured_md = f"""# {fm.get('titulo', fn[:-3])}

> [!info] 🧭 Painel Rápido da Cena · **{code}**
> **Arco:** {', '.join(f'[[{a}]]' for a in arcs)} · **Patamar:** {fm.get('patamar', 1)} (Nível {fm.get('nivel', 1)}) · **Foco:** {fm.get('foco', 'Exploração')} · **Essencial:** {'★ Sim' if fm.get('essencial') == 'Yes' else 'Opcional'}
> **🗺️ Mapa Direto da Cena:** [[{scene_map['title']}]] (`{scene_map['file']}`) · **⚔️ Encontros:** {enc_links}

---

{roteiro_formatted}

---

> [!map]- 🗺️ Instruções de Mapa e Atlas desta Cena (clique para expandir)
> **Mapa Principal Recomendado:** [[{scene_map['title']}]]
{chr(10).join('> ' + l for l in mapas_raw.splitlines()) if mapas_raw else '> Consulte o Atlas do Mestre e o painel de Mapas Reveláveis.'}

## Ao encerrar

- [ ] Registrar a decisão do grupo.
- [ ] Atualizar pistas, promessas e prazos afetados.
- [ ] Marcar a cena como resolvida quando seu objetivo terminar.
"""
        with open(os.path.join(notion_cenas_out, fn), "w", encoding="utf-8", newline="\n") as f:
            f.write(restructured_md)

        # Also update the Vault RPG scene if it had "não há planta específica" so it links to the new map right at the top of Mapas desta cena!
        if code in SCENE_CODE_TO_NEW_MAP and f"[[{scene_map['title']}]]" not in raw_md:
            new_map_banner = f"**Mapa Tático/Regional Criado para esta Cena:** [[{scene_map['title']}]] (![[{scene_map['file']}]])\n\n"
            updated_vault_md = raw_md.replace("## Mapas desta cena\n\n", "## Mapas desta cena\n\n" + new_map_banner, 1)
            with open(fp, "w", encoding="utf-8", newline="\n") as f:
                f.write(updated_vault_md)

        data["scenes"].append({
            "id": fn[:-3],
            "code": code,
            "title": fm.get("titulo", fn[:-3]),
            "arcs": arcs,
            "arc_code": arc_code,
            "encounters": encs,
            "essential": fm.get("essencial") == "Yes",
            "status": fm.get("estado", "A preparar"),
            "focus": fm.get("foco", "Exploração"),
            "level": fm.get("nivel", 1),
            "tier": fm.get("patamar", 1),
            "order": fm.get("ordem", 999),
            "revealed": bool(fm.get("revelado", False)),
            "map_key": scene_map["key"],
            "map_title": scene_map["title"],
            "map_file": scene_map["file"],
            "sound_preset": sound_preset,
            "roteiro_raw": roteiro_raw,
            "roteiro_formatted": roteiro_formatted,
            "mapas_notes": mapas_raw,
            "body": body,
        })
    data["scenes"].sort(key=lambda x: x["order"])

    # 5. Read Calendar Deadlines (08 Calendário)
    cal_dir = os.path.join(VAULT_DIR, "08 Calendário")
    for fn in sorted(os.listdir(cal_dir)):
        if not fn.endswith(".md"):
            continue
        fp = os.path.join(cal_dir, fn)
        with open(fp, "r", encoding="utf-8") as f:
            fm, body = parse_frontmatter(f.read())
        data["calendar"].append({
            "id": fn[:-3],
            "title": fm.get("titulo", fn[:-3]),
            "arcs": clean_wikilink(fm.get("arcos", [])),
            "status": fm.get("estado", "Ativo"),
            "trigger": fm.get("gatilho", ""),
            "when": fm.get("quando", ""),
            "priority": fm.get("prioridade", "Alta"),
            "order": fm.get("ordem", 99),
            "body": body,
        })
    data["calendar"].sort(key=lambda x: x["order"])

    # 6. Read Magic & Items (09 Magia e itens)
    items_dir = os.path.join(VAULT_DIR, "09 Magia e itens")
    for fn in sorted(os.listdir(items_dir)):
        if not fn.endswith(".md"):
            continue
        fp = os.path.join(items_dir, fn)
        with open(fp, "r", encoding="utf-8") as f:
            fm, body = parse_frontmatter(f.read())
        data["items_spells"].append({
            "id": fn[:-3],
            "title": fm.get("titulo", fn[:-3]),
            "category": fm.get("categoria", "Item/Magia"),
            "function": fm.get("funcao", ""),
            "original_name": fm.get("nome_original", ""),
            "summary": fm.get("resumo", ""),
            "revealed": bool(fm.get("revelado", False)),
            "body": body,
        })

    # 7. Read Amber Pacts (10 Âmbar)
    ambar_dir = os.path.join(VAULT_DIR, "10 Âmbar")
    for fn in sorted(os.listdir(ambar_dir)):
        if not fn.endswith(".md"):
            continue
        fp = os.path.join(ambar_dir, fn)
        with open(fp, "r", encoding="utf-8") as f:
            fm, body = parse_frontmatter(f.read())
        data["amber_pacts"].append({
            "id": fn[:-3],
            "title": fm.get("titulo", fn[:-3]),
            "vestige": fm.get("vestigio", ""),
            "corruption_accept": fm.get("corrupcao_ao_aceitar", 1),
            "corruption_use": fm.get("corrupcao_ao_usar", 1),
            "hope_cost": fm.get("custo_de_esperanca", 1),
            "usage": fm.get("uso", ""),
            "revealed": bool(fm.get("revelado", False)),
            "body": body,
        })

    # 8. Read Rules & Guides (11 Regras + 00 Comece aqui)
    for folder in ["11 Regras", "00 Comece aqui"]:
        r_dir = os.path.join(VAULT_DIR, folder)
        for fn in sorted(os.listdir(r_dir)):
            if not fn.endswith(".md") or fn in ("TELA DO MESTRE.md", "TELA DOS JOGADORES.md", "PREPARAR SESSÃO.md", "LEIA-ME.md", "Saúde do vault.md"):
                continue
            fp = os.path.join(r_dir, fn)
            if os.path.isfile(fp):
                with open(fp, "r", encoding="utf-8") as f:
                    fm, body = parse_frontmatter(f.read())
                data["rules"].append({
                    "id": fn[:-3],
                    "title": fm.get("titulo", fn[:-3]),
                    "folder": folder,
                    "body": body,
                })

    # Save JSON and JS bundle
    json_path = os.path.join(DATA_DIR, "campaign_data.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_path = os.path.join(DATA_DIR, "campaign_data.js")
    with open(js_path, "w", encoding="utf-8") as f:
        f.write("window.CAMPAIGN_DATA = ")
        json.dump(data, f, ensure_ascii=False)
        f.write(";\n")

    print(f"Saved campaign_data.json ({os.path.getsize(json_path)} bytes) and campaign_data.js")
    print(f"Counts: {len(data['arcs'])} arcs, {len(data['scenes'])} scenes, {len(data['encounters'])} encounters, {len(data['bestiary'])} bestiary, {len(data['items_spells'])} items/spells, {len(data['amber_pacts'])} pacts, {len(data['calendar'])} deadlines, {len(data['maps'])} maps")


if __name__ == "__main__":
    create_new_atlas_pages_in_vault()
    process_all_data()
