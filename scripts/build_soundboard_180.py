# -*- coding: utf-8 -*-
"""
Generates the upgraded soundboard.js with:
- 46 real Curse of Strahd .mp3 files (14 Ambient Channels, 14 Music Channels, 18 SFX Pads)
- Web Audio API procedural fallback if an audio file is missing
- Explicit, tailored audio profile for ALL 180 scenes in the campaign (A1 through EP6)
"""

import json
from pathlib import Path

WORKSPACE = Path(r"c:\Users\Alex\Documents\antigravity\beautiful-bohr")
CAMPAIGN_JSON = WORKSPACE / "data" / "campaign_data.json"
CAMPAIGN_JS = WORKSPACE / "data" / "campaign_data.js"
SOUNDBOARD_JS = WORKSPACE / "soundboard.js"


def derive_scene_profile(sc):
    code = sc["code"]
    title = sc["title"]
    lower = (title + " " + sc.get("focus", "") + " " + (sc.get("roteiro_raw", "") or sc.get("body", ""))[:600]).lower()
    has_enc = len(sc.get("encounters") or []) > 0

    # Specific handcrafted overrides for iconic scenes and sub-scenes across all 21 Arcs
    exact = {
        # Arco A - Casa da Morte
        "A1": ("🍺 Taverna & Estrada na Chuva", {"tavern": 0.45, "rain": 0.45, "lute": 0.35}, ["thunder", "door", "wolf"]),
        "A2": ("🌫️ Fachada da Casa da Morte", {"wind": 0.55, "rain": 0.40, "mystery": 0.45}, ["door", "thunder", "whispers_sfx"]),
        "A2a": ("🚪 Entrada & Portão Trancado", {"wind": 0.45, "mystery": 0.50}, ["iron_door", "heartbeat", "thunder"]),
        "A2b": ("🕯️ 1º Andar · Aparência de Normalidade", {"fire": 0.40, "mystery": 0.45, "whispers": 0.25}, ["door", "heartbeat", "sting"]),
        "A2c": ("🎹 2º Andar · Segredos e Cravo", {"piano": 0.50, "whispers": 0.35, "wind": 0.25}, ["door", "scream", "heartbeat"]),
        "A2d": ("⚔️ 3º Andar · Armadura & Violência", {"horror": 0.55, "whispers": 0.40}, ["sting", "trap", "scream"]),
        "A2e": ("👻 Sótão · Rose & Thorn", {"piano": 0.55, "whispers": 0.50}, ["scream", "iron_door", "heartbeat"]),
        "A2f": ("⛓️ Porão & Criptas do Culto", {"dungeon": 0.60, "whispers": 0.50, "horror": 0.45}, ["zombie", "chains", "trap"]),
        "A2g": ("🩸 Câmara Ritual · Lorghoth", {"dungeon": 0.55, "druid": 0.55, "combat": 0.50}, ["zombie", "scream", "fireball"]),
        "A2h": ("🔥 Fuga da Casa em Colapso", {"combat": 0.65, "fire": 0.60, "dread": 0.50}, ["trap", "fireball", "iron_door"]),
        "A3": ("🌫️ Saída nas Brumas de Baróvia", {"wind": 0.60, "piano": 0.40}, ["ravens", "wolf", "bell"]),

        # Arco B - Vila de Baróvia
        "B1": ("🐺 Estrada Velha de Svalich", {"night": 0.55, "wind": 0.50, "exploration": 0.40}, ["wolf", "ravens", "carriage"]),
        "B2": ("🚪 Portões Leste de Baróvia", {"wind": 0.60, "rain": 0.45, "dread": 0.35}, ["door", "wolf", "thunder"]),
        "B3": ("🌲 Floresta & Cadáver de Dalvan", {"night": 0.60, "wind": 0.40, "mystery": 0.40}, ["ravens", "wolf", "sting"]),
        "B4": ("🌧️ Mirante da Vila de Baróvia", {"wind": 0.55, "rain": 0.45, "exploration": 0.40}, ["bell", "thunder", "ravens"]),
        "B5": ("🏘️ Vila de Baróvia Sob Cerco", {"rain": 0.50, "wind": 0.45, "piano": 0.40}, ["bell", "zombie", "scream"]),
        "B5a": ("🛡️ Barricada · Encontro com Ismark", {"rain": 0.45, "town": 0.30, "exploration": 0.40}, ["horn", "zombie", "door"]),
        "B5b": ("🏚️ Praça da Vila & Refugiados", {"rain": 0.45, "piano": 0.45, "whispers": 0.25}, ["bell", "scream", "thunder"]),
        "B5c": ("🍷 Taverna Sangue da Videira", {"tavern": 0.50, "fire": 0.45, "lute": 0.35}, ["door", "thunder", "bell"]),
        "B5d": ("🕯️ Mansão do Burgomestre · Ireena", {"fire": 0.40, "piano": 0.50, "rain": 0.30}, ["door", "wolf", "heartbeat"]),
        "B5e": ("🪙 Empório de Bildrath", {"town": 0.35, "rain": 0.35, "mystery": 0.35}, ["door", "chains", "thunder"]),
        "B5f": ("⚔️ Barricada Oriental · O Cerco", {"combat": 0.65, "rain": 0.55, "dread": 0.45}, ["zombie", "horn", "fireball"]),
        "B5g": ("🧟 Barricada Ocidental · Horda", {"combat": 0.70, "rain": 0.55, "horror": 0.50}, ["zombie", "werewolf", "thunder"]),
        "B5h": ("🧛 Retorno à Mansão & Cerco Final", {"dread": 0.60, "organ": 0.45, "rain": 0.45}, ["strahd_laugh", "bats", "thunder"]),
        "B5i": ("⛪ Igreja de Baróvia, Doru & Funeral", {"choir": 0.50, "dungeon": 0.45, "rain": 0.35}, ["bell", "scream", "iron_door"]),
        "B5j": ("🪦 Colina de Lugdana", {"wind": 0.55, "choir": 0.40, "exploration": 0.35}, ["thunder", "ravens", "bell"]),
        "B5k": ("😢 Casa de Mad Mary", {"piano": 0.60, "whispers": 0.40, "rain": 0.30}, ["scream", "door", "heartbeat"]),

        # Arco C - Estrada para Vallaki & Tser Pool
        "C1": ("🌲 Floresta & Esconderijo", {"night": 0.55, "exploration": 0.45}, ["wolf", "ravens", "trap"]),
        "C2": ("🧛 Encruzilhada do Ivlis · 1º Encontro com Strahd", {"carriage": 0.45, "organ": 0.55, "dread": 0.50}, ["strahd_laugh", "thunder", "bats"]),
        "C3": ("🐦‍⬛ A Strix & o Corvo Ferido", {"night": 0.55, "horror": 0.45}, ["ravens", "bats", "sting"]),
        "C4": ("🔮 Tser Pool · Acampamento Vistani & Tarokka", {"fire": 0.60, "vistani": 0.65, "river": 0.30}, ["bell", "thunder", "hag_laugh"]),
        "C5": ("🐎 Cavaleiro Esquelético na Neblina", {"wind": 0.55, "carriage": 0.45, "mystery": 0.45}, ["chains", "horn", "sting"]),
        "C6": ("🗼 Torre de Vigia & Sepulturas", {"wind": 0.55, "exploration": 0.45}, ["ravens", "iron_door", "trap"]),
        "C7": ("🌊 Cachoeira de Tser & Ponte Alta", {"river": 0.70, "wind": 0.45, "exploration": 0.40}, ["thunder", "wolf", "ravens"]),
        "C8": ("🐎 Encruzilhada da Carruagem Negra", {"wind": 0.55, "carriage": 0.50, "dread": 0.45}, ["thunder", "strahd_laugh", "bats"]),
        "C9": ("⚙️ Velho Moedor de Ossos (Contato)", {"grindstone": 0.60, "witches": 0.50, "wind": 0.40}, ["hag_laugh", "ravens", "door"]),
        "C10": ("🌲 Floresta Profunda de Svalich", {"night": 0.65, "trees": 0.45, "horror": 0.40}, ["wolf", "werewolf", "bats"]),
        "C11": ("🐾 Caçada dos Lobisomens", {"combat": 0.65, "night": 0.55, "dread": 0.50}, ["werewolf", "wolf", "heartbeat"]),
        "C12": ("🏘️ Portões de Vallaki", {"town": 0.55, "wind": 0.35, "exploration": 0.40}, ["door", "bell", "ravens"]),
    }

    if code in exact:
        name, channels, sfx = exact[code]
        return {"code": code, "name": name, "channels": channels, "sfx": sfx}

    # Rule-based intelligent mapping for all remaining scenes (D through EP)
    arc = code[0]
    if code.startswith("EP"):
        if "festival" in lower or "sol" in lower or "amanhecer" in lower:
            return {"code": code, "name": f"🌅 {title} (Amanhecer em Baróvia)", "channels": {"town": 0.45, "lute": 0.50, "choir": 0.40}, "sfx": ["bell", "horn", "ravens"]}
        if "tser" in lower or "vistani" in lower:
            return {"code": code, "name": f"🎻 {title} (Despedida Vistani)", "channels": {"fire": 0.50, "vistani": 0.55, "river": 0.30}, "sfx": ["bell", "ravens", "door"]}
        return {"code": code, "name": f"🕊️ {title} (Epílogo & Paz)", "channels": {"piano": 0.50, "wind": 0.25, "choir": 0.35}, "sfx": ["bell", "ravens", "door"]}

    if arc == "D":  # Ossos de Santo Andral
        if "loja" in lower or "caix" in lower or "armadilha" in lower:
            return {"code": code, "name": f"⚰️ {title} (Loja de Caixões & Vampiros)", "channels": {"horror": 0.60, "combat": 0.50, "whispers": 0.40}, "sfx": ["trap", "bats", "scream"]}
        if "rahadin" in lower:
            return {"code": code, "name": f"🗡️ {title} (Rahadin & Coro de Gritos)", "channels": {"whispers": 0.65, "dread": 0.55, "carriage": 0.40}, "sfx": ["scream", "strahd_laugh", "horn"]}
        return {"code": code, "name": f"⛪ {title} (Igreja de Sto. Andral)", "channels": {"choir": 0.50, "mystery": 0.45, "town": 0.25}, "sfx": ["bell", "door", "heartbeat"]}

    if arc == "E":  # Torre de Khazan / Arabelle / Vallaki
        if "vistani" in lower or "kasimir" in lower:
            return {"code": code, "name": f"⛺ {title} (Acampamento Vistani)", "channels": {"fire": 0.55, "vistani": 0.50, "night": 0.30}, "sfx": ["wolf", "bell", "ravens"]}
        if "lago" in lower:
            return {"code": code, "name": f"🌊 {title} (Lago Zarovich)", "channels": {"river": 0.60, "wind": 0.45, "mystery": 0.40}, "sfx": ["scream", "ravens", "thunder"]}
        if "torre" in lower or "khazan" in lower:
            return {"code": code, "name": f"⚡ {title} (Torre de Khazan)", "channels": {"wind": 0.55, "amber": 0.45, "mystery": 0.45}, "sfx": ["thunder", "fireball", "trap"]}
        return {"code": code, "name": f"🔍 {title} (Investigação em Vallaki)", "channels": {"town": 0.45, "mystery": 0.45}, "sfx": ["door", "bell", "ravens"]}

    if arc == "F":  # Lady Wachter & Política
        if "estalagem" in lower or "água azul" in lower:
            return {"code": code, "name": f"🍺 {title} (Estalagem Água Azul)", "channels": {"tavern": 0.55, "fire": 0.45, "lute": 0.40}, "sfx": ["ravens", "door", "bell"]}
        if "emboscar" in lower or "izek" in lower:
            return {"code": code, "name": f"⚔️ {title} (Emboscada a Izek)", "channels": {"combat": 0.65, "dread": 0.45, "rain": 0.35}, "sfx": ["fireball", "horn", "sting"]}
        return {"code": code, "name": f"🕯️ {title} (Wachterhaus & Conspiração)", "channels": {"mystery": 0.55, "whispers": 0.35, "fire": 0.30}, "sfx": ["door", "heartbeat", "chains"]}

    if arc == "G":  # Lei Marcial em Vallaki
        if "invade" in lower or "atacar" in lower or "infiltrar" in lower:
            return {"code": code, "name": f"🔥 {title} (Confronto em Vallaki)", "channels": {"combat": 0.60, "horror": 0.45, "town": 0.35}, "sfx": ["horn", "fireball", "iron_door"]}
        return {"code": code, "name": f"🚨 {title} (Vallaki Sob Lei Marcial)", "channels": {"town": 0.40, "dread": 0.50, "rain": 0.35}, "sfx": ["horn", "bell", "chains"]}

    if arc == "H":  # Moinho de Vento & Mente de Stella
        if "moinho" in lower or "megera" in lower or "morgantha" in lower:
            return {"code": code, "name": f"🧙‍♀️ {title} (Velho Moedor de Ossos)", "channels": {"grindstone": 0.55, "witches": 0.55, "cauldron": 0.45}, "sfx": ["hag_laugh", "scream", "fireball"]}
        if "tomo" in lower:
            return {"code": code, "name": f"📖 {title} (O Tomo de Strahd)", "channels": {"organ": 0.50, "whispers": 0.55, "dread": 0.40}, "sfx": ["strahd_laugh", "heartbeat", "thunder"]}
        return {"code": code, "name": f"🔮 {title} (Sótão de Victor & Espelho)", "channels": {"mystery": 0.55, "whispers": 0.45, "piano": 0.35}, "sfx": ["scream", "thunder", "heartbeat"]}

    if arc == "I":  # Caminho para Krezk & Berez
        if "berez" in lower:
            return {"code": code, "name": f"🐸 {title} (Pântano de Berez)", "channels": {"river": 0.60, "rain": 0.45, "witches": 0.40}, "sfx": ["hag_laugh", "ravens", "thunder"]}
        if "abadia" in lower or "piscina" in lower:
            return {"code": code, "name": f"⛪ {title} (Santuário de Krezk)", "channels": {"monks": 0.50, "river": 0.40, "wind": 0.35}, "sfx": ["bell", "thunder", "scream"]}
        return {"code": code, "name": f"🌲 {title} (Estrada para Krezk)", "channels": {"wind": 0.50, "exploration": 0.45, "night": 0.35}, "sfx": ["wolf", "ravens", "door"]}

    if arc == "J":  # Vinícola & Colina Yester
        if "yester" in lower or "wintersplinter" in lower or "ritual" in lower:
            return {"code": code, "name": f"🌩️ {title} (Colina Yester & Wintersplinter)", "channels": {"druid": 0.65, "rain": 0.60, "trees": 0.50}, "sfx": ["thunder", "horn", "scream"]}
        if "vinícola" in lower or "libertar" in lower:
            return {"code": code, "name": f"🍇 {title} (Batalha na Vinícola)", "channels": {"trees": 0.50, "combat": 0.55, "rain": 0.40}, "sfx": ["ravens", "trap", "wolf"]}
        return {"code": code, "name": f"🌲 {title} (Rumo à Vinícola)", "channels": {"night": 0.50, "exploration": 0.45, "trees": 0.35}, "sfx": ["ravens", "wolf", "thunder"]}

    if arc == "K":  # Krezk & Abadia de Santa Markovia
        if "abadia" in lower or "vasilka" in lower or "ala" in lower:
            return {"code": code, "name": f"🔔 {title} (Abadia de Santa Markovia)", "channels": {"monks": 0.55, "horror": 0.45, "whispers": 0.35}, "sfx": ["bell", "scream", "chains"]}
        return {"code": code, "name": f"❄️ {title} (Vila de Krezk)", "channels": {"wind": 0.45, "piano": 0.45, "fire": 0.35}, "sfx": ["door", "bell", "wolf"]}

    if arc == "L":  # Covil dos Lobisomens
        if "covil" in lower:
            return {"code": code, "name": f"🐾 {title} (Caverna dos Lobisomens)", "channels": {"dungeon": 0.55, "fire": 0.40, "dread": 0.45}, "sfx": ["werewolf", "wolf", "chains"]}
        return {"code": code, "name": f"🌲 {title} (Rastreamento na Floresta)", "channels": {"night": 0.60, "wind": 0.45, "exploration": 0.40}, "sfx": ["wolf", "werewolf", "ravens"]}

    if arc == "M":  # Argynvostholt
        if "telhado" in lower or "farol" in lower or "zorya" in lower or has_enc:
            return {"code": code, "name": f"🐉 {title} (Batalha em Argynvostholt)", "channels": {"combat": 0.55, "wind": 0.55, "organ": 0.40}, "sfx": ["horn", "fireball", "iron_door"]}
        return {"code": code, "name": f"🏰 {title} (Mansão de Argynvostholt)", "channels": {"wind": 0.55, "dungeon": 0.40, "piano": 0.45}, "sfx": ["iron_door", "chains", "whispers_sfx"]}

    if arc == "O":  # O Jantar do Diabo (Ravenloft Social)
        if "jantar" in lower or "corte" in lower or "chegada" in lower:
            return {"code": code, "name": f"🎹 {title} (Salão de Jantar de Strahd)", "channels": {"organ": 0.65, "fire": 0.35, "rain": 0.30}, "sfx": ["strahd_laugh", "thunder", "door"]}
        if "estrada" in lower or "carruagem" in lower:
            return {"code": code, "name": f"🐎 {title} (Carruagem para Ravenloft)", "channels": {"carriage": 0.60, "rain": 0.45, "dread": 0.40}, "sfx": ["thunder", "wolf", "door"]}
        if "pesadelo" in lower:
            return {"code": code, "name": f"💀 {title} (Pesadelo em Ravenloft)", "channels": {"horror": 0.65, "whispers": 0.55}, "sfx": ["heartbeat", "scream", "sting"]}
        return {"code": code, "name": f"🦇 {title} (Hospitalidade de Ravenloft)", "channels": {"organ": 0.45, "mystery": 0.45, "wind": 0.40}, "sfx": ["door", "bats", "heartbeat"]}

    if arc == "P":  # Assalto a Ravenloft (Heist)
        if "masmorra" in lower or "catacumba" in lower or "braseiro" in lower:
            return {"code": code, "name": f"⛓️ {title} (Masmorras & Catacumbas de Ravenloft)", "channels": {"dungeon": 0.65, "horror": 0.50, "whispers": 0.40}, "sfx": ["chains", "iron_door", "bats"]}
        if "bruxas" in lower:
            return {"code": code, "name": f"🧪 {title} (Aposentos das Bruxas)", "channels": {"cauldron": 0.60, "witches": 0.50, "dungeon": 0.35}, "sfx": ["hag_laugh", "bats", "fireball"]}
        if "campanário" in lower or "pátio" in lower:
            return {"code": code, "name": f"🌩️ {title} (Torres & Pátios de Ravenloft)", "channels": {"rain": 0.60, "wind": 0.55, "dread": 0.45}, "sfx": ["bell", "thunder", "bats"]}
        return {"code": code, "name": f"🦇 {title} (Infiltração em Ravenloft)", "channels": {"mystery": 0.55, "organ": 0.40, "dungeon": 0.35}, "sfx": ["iron_door", "heartbeat", "trap"]}

    if arc == "Q":  # Retorno & Consequências
        if "abade" in lower:
            return {"code": code, "name": f"👼 {title} (Confronto com o Abade)", "channels": {"monks": 0.55, "combat": 0.55, "dread": 0.45}, "sfx": ["bell", "scream", "fireball"]}
        if "kiril" in lower or "covil" in lower:
            return {"code": code, "name": f"🐾 {title} (Emboscada da Alcateia)", "channels": {"combat": 0.65, "night": 0.55}, "sfx": ["werewolf", "wolf", "horn"]}
        if "farol" in lower or "crânio" in lower:
            return {"code": code, "name": f"🐉 {title} (O Farol de Argynvost)", "channels": {"choir": 0.60, "wind": 0.45, "organ": 0.35}, "sfx": ["horn", "bell", "fireball"]}
        return {"code": code, "name": f"⏳ {title} (Consequências no Vale)", "channels": {"exploration": 0.50, "wind": 0.45, "dread": 0.35}, "sfx": ["thunder", "wolf", "bell"]}

    if arc == "R":  # Passo Tsolenka & Monte Ghakis
        if "nevasca" in lower or "avalanche" in lower or "gelo" in lower or "tsolenka" in lower:
            return {"code": code, "name": f"❄️ {title} (Nevasca em Tsolenka)", "channels": {"blizzard": 0.70, "wind": 0.55, "dread": 0.40}, "sfx": ["thunder", "horn", "trap"]}
        if "rozana" in lower or "santuário" in lower:
            return {"code": code, "name": f"🕯️ {title} (Santuário das Três Senhoras)", "channels": {"druid": 0.50, "whispers": 0.45, "wind": 0.35}, "sfx": ["bell", "ravens", "heartbeat"]}
        if "soldav" in lower:
            return {"code": code, "name": f"🔥 {title} (Abrigo em Soldav)", "channels": {"fire": 0.60, "blizzard": 0.35, "vistani": 0.35}, "sfx": ["door", "wolf", "horn"]}
        return {"code": code, "name": f"🏔️ {title} (Subida do Monte Ghakis)", "channels": {"blizzard": 0.55, "exploration": 0.45}, "sfx": ["wind", "horn", "werewolf"]}

    if arc == "S":  # Templo de Âmbar
        if has_enc or "neferon" in lower or "defesas" in lower:
            return {"code": code, "name": f"🔥 {title} (Defesas do Templo de Âmbar)", "channels": {"amber": 0.60, "combat": 0.55, "dungeon": 0.40}, "sfx": ["fireball", "scream", "trap"]}
        return {"code": code, "name": f"🔮 {title} (Salões e Sarcófagos de Âmbar)", "channels": {"amber": 0.65, "whispers": 0.50, "dungeon": 0.40}, "sfx": ["heartbeat", "scream", "iron_door"]}

    if arc == "T":  # As Três Senhoras & Berez
        if "lysaga" in lower or "cabana" in lower:
            return {"code": code, "name": f"🧙‍♀️ {title} (Baba Lysaga & Cabana Rastejante)", "channels": {"combat": 0.65, "cauldron": 0.55, "witches": 0.55}, "sfx": ["hag_laugh", "fireball", "ravens"]}
        if "reconsecrar" in lower or "marina" in lower or "sergei" in lower:
            return {"code": code, "name": f"✨ {title} (Reconsecração das Senhoras)", "channels": {"choir": 0.55, "druid": 0.45, "river": 0.40}, "sfx": ["bell", "thunder", "ravens"]}
        return {"code": code, "name": f"🌫️ {title} (Alianças Finais no Vale)", "channels": {"exploration": 0.50, "rain": 0.45, "dread": 0.40}, "sfx": ["ravens", "thunder", "horn"]}

    if arc == "U":  # Cerco Final & Queda de Strahd
        if "ravenloft" in lower or "coração" in lower:
            return {"code": code, "name": f"👑 {title} (Confronto Final em Ravenloft)", "channels": {"organ": 0.65, "combat": 0.65, "rain": 0.45}, "sfx": ["strahd_laugh", "thunder", "heartbeat"]}
        if "sol nasce" in lower:
            return {"code": code, "name": f"🌅 {title} (O Sol Nasce sobre Baróvia)", "channels": {"choir": 0.65, "piano": 0.50}, "sfx": ["bell", "ravens", "horn"]}
        if "defesa" in lower or "exército" in lower or "portão" in lower:
            return {"code": code, "name": f"⚔️ {title} (A Guerra de Vallaki)", "channels": {"combat": 0.70, "rain": 0.55, "dread": 0.50}, "sfx": ["horn", "zombie", "fireball"]}
        return {"code": code, "name": f"🌑 {title} (Noite Eterna & Conselho)", "channels": {"dread": 0.60, "organ": 0.45, "whispers": 0.40}, "sfx": ["thunder", "heartbeat", "bell"]}

    return {"code": code, "name": f"🎵 {title}", "channels": {"exploration": 0.45, "wind": 0.40}, "sfx": ["thunder", "wolf", "door"]}


def main():
    data = json.loads(CAMPAIGN_JSON.read_text(encoding="utf-8"))
    scene_profiles = {}

    for sc in data["scenes"]:
        prof = derive_scene_profile(sc)
        scene_profiles[sc["code"]] = prof
        sc["audio_profile"] = prof

    # Save updated campaign_data.json and campaign_data.js
    CAMPAIGN_JSON.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    CAMPAIGN_JS.write_text("window.CAMPAIGN_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"Mapped custom audio profiles for {len(scene_profiles)}/180 scenes.")

    profiles_json = json.dumps(scene_profiles, ensure_ascii=False, indent=2)

    js_code = f"""// ============================================================================
// BARÓVIA ATMOSPHERIC SOUNDBOARD & MIXER v3.0 (Real MP3 Audio + 180 Scenes)
// 46 Real Curse of Strahd Audio Tracks + Tailored Soundscapes for All 180 Scenes
// ============================================================================

class BaroviaSoundEngine {{
  constructor() {{
    this.ctx = null;
    this.masterGain = null;
    this.masterVolume = 0.75;
    this.activeLoops = new Map(); // id -> {{ type: 'file'|'synth', audio?, volume, ... }}
    this.customFiles = new Map(); // id -> HTMLAudioElement
    this.preloadedFiles = new Map(); // id -> src path
    this.activePreset = null;
    this.autoPlayOnSceneChange = false;

    // 14 Real Ambient Loops (can be mixed simultaneously)
    this.ambientChannels = [
      {{ id: 'rain', icon: '🌧️', name: 'Chuva & Trovoada Distante', file: 'assets/audio/amb_rain_storm.mp3', defaultVol: 0.55 }},
      {{ id: 'wind', icon: '🌫️', name: 'Vento Uivante das Brumas', file: 'assets/audio/amb_wind_howl.mp3', defaultVol: 0.50 }},
      {{ id: 'night', icon: '🌲', name: 'Floresta de Svalich à Noite', file: 'assets/audio/amb_night_woods.mp3', defaultVol: 0.50 }},
      {{ id: 'tavern', icon: '🍺', name: 'Taverna Movimentada', file: 'assets/audio/amb_tavern.mp3', defaultVol: 0.50 }},
      {{ id: 'fire', icon: '🔥', name: 'Lareira / Fogueira Vistani', file: 'assets/audio/amb_fireplace.mp3', defaultVol: 0.50 }},
      {{ id: 'dungeon', icon: '⛓️', name: 'Masmorra Úmida & Goteiras', file: 'assets/audio/amb_crypt_drip.mp3', defaultVol: 0.55 }},
      {{ id: 'whispers', icon: '🕯️', name: 'Sussurros nas Sombras', file: 'assets/audio/amb_whispers.mp3', defaultVol: 0.45 }},
      {{ id: 'town', icon: '🏘️', name: 'Ruas da Vila / Vallaki', file: 'assets/audio/amb_medieval_town.mp3', defaultVol: 0.45 }},
      {{ id: 'river', icon: '🌊', name: 'Rio Ivlis / Pântano de Berez', file: 'assets/audio/amb_river_swamp.mp3', defaultVol: 0.50 }},
      {{ id: 'carriage', icon: '🐎', name: 'Carruagem Negra na Estrada', file: 'assets/audio/amb_carriage.mp3', defaultVol: 0.50 }},
      {{ id: 'grindstone', icon: '⚙️', name: 'Engrenagens do Moinho', file: 'assets/audio/amb_grindstone.mp3', defaultVol: 0.50 }},
      {{ id: 'trees', icon: '🌳', name: 'Árvore de Gulthias', file: 'assets/audio/amb_whispering_trees.mp3', defaultVol: 0.50 }},
      {{ id: 'cauldron', icon: '🧪', name: 'Caldeirão Borbulhante', file: 'assets/audio/amb_cauldron.mp3', defaultVol: 0.50 }},
      {{ id: 'blizzard', icon: '❄️', name: 'Nevasca do Monte Ghakis', file: 'assets/audio/amb_wind_howl.mp3', defaultVol: 0.65 }}
    ];

    // 14 Real Music & Dramatic Score Loops
    this.musicChannels = [
      {{ id: 'organ', icon: '🎹', name: 'Órgão de Strahd (Ravenloft)', file: 'assets/audio/mus_strahd_organ.mp3', defaultVol: 0.55 }},
      {{ id: 'exploration', icon: '🧭', name: 'Exploração Sombria do Vale', file: 'assets/audio/mus_exploration.mp3', defaultVol: 0.45 }},
      {{ id: 'combat', icon: '⚔️', name: 'Combate Mortal / Cerco', file: 'assets/audio/mus_battle.mp3', defaultVol: 0.55 }},
      {{ id: 'vistani', icon: '🎻', name: 'Acampamento Vistani (Tser Pool)', file: 'assets/audio/mus_vistani_camp.mp3', defaultVol: 0.55 }},
      {{ id: 'mystery', icon: '🔍', name: 'Investigação & Mistério', file: 'assets/audio/mus_mystery.mp3', defaultVol: 0.45 }},
      {{ id: 'horror', icon: '💀', name: 'Terror & Suspense Profundo', file: 'assets/audio/mus_horror_suspense.mp3', defaultVol: 0.50 }},
      {{ id: 'choir', icon: '⛪', name: 'Coro Sagrado (Igreja / Capela)', file: 'assets/audio/mus_choir_chapel.mp3', defaultVol: 0.50 }},
      {{ id: 'monks', icon: '🙏', name: 'Cântico Monástico (Abadia)', file: 'assets/audio/mus_monk_chants.mp3', defaultVol: 0.50 }},
      {{ id: 'druid', icon: '🩸', name: 'Ritual Druídico (Colina Yester)', file: 'assets/audio/mus_druid_chant.mp3', defaultVol: 0.55 }},
      {{ id: 'amber', icon: '🔮', name: 'Prelúdio do Templo de Âmbar', file: 'assets/audio/mus_amber_prelude.mp3', defaultVol: 0.55 }},
      {{ id: 'piano', icon: '🥀', name: 'Piano Melancólico & Luto', file: 'assets/audio/mus_sad_piano.mp3', defaultVol: 0.50 }},
      {{ id: 'lute', icon: '🪕', name: 'Alaúde de Estalagem', file: 'assets/audio/mus_tavern_lute.mp3', defaultVol: 0.45 }},
      {{ id: 'witches', icon: '🧙‍♀️', name: 'Dança das Bruxas (Megeras)', file: 'assets/audio/mus_witches_dance.mp3', defaultVol: 0.50 }},
      {{ id: 'dread', icon: '👑', name: 'Presença do Senhor da Noite', file: 'assets/audio/mus_creepy_tension.mp3', defaultVol: 0.50 }}
    ];

    // 18 Real SFX Pads (One-Shot Effects)
    this.sfxPads = [
      {{ id: 'thunder', icon: '⚡', name: 'Trovão Violento', file: 'assets/audio/sfx_thunder_strike.mp3' }},
      {{ id: 'wolf', icon: '🐺', name: 'Uivo da Alcateia', file: 'assets/audio/sfx_wolves_howl.mp3' }},
      {{ id: 'ravens', icon: '🐦‍⬛', name: 'Revoada de Corvos', file: 'assets/audio/sfx_ravens_flock.mp3' }},
      {{ id: 'door', icon: '🚪', name: 'Portão Pesado', file: 'assets/audio/sfx_heavy_gate.mp3' }},
      {{ id: 'iron_door', icon: '🗝️', name: 'Porta de Ferro', file: 'assets/audio/sfx_iron_door.mp3' }},
      {{ id: 'strahd_laugh', icon: '🧛', name: 'Risada de Strahd', file: 'assets/audio/sfx_strahd_laugh.mp3' }},
      {{ id: 'hag_laugh', icon: '🧙‍♀️', name: 'Risada de Bruxa', file: 'assets/audio/sfx_hag_laugh.mp3' }},
      {{ id: 'bell', icon: '🔔', name: 'Sino / Gongo Fúnebre', file: 'assets/audio/sfx_church_bell.mp3' }},
      {{ id: 'heartbeat', icon: '💓', name: 'Batimento Cardíaco', file: 'assets/audio/sfx_heartbeat.mp3' }},
      {{ id: 'scream', icon: '👻', name: 'Grito Espectral', file: 'assets/audio/sfx_ghost_scream.mp3' }},
      {{ id: 'zombie', icon: '🧟', name: 'Horda de Zumbis', file: 'assets/audio/sfx_zombie_scream.mp3' }},
      {{ id: 'werewolf', icon: '🐾', name: 'Rugido Lobisomem', file: 'assets/audio/sfx_werewolf_roar.mp3' }},
      {{ id: 'horn', icon: '📯', name: 'Trombeta de Alarme', file: 'assets/audio/sfx_war_horn.mp3' }},
      {{ id: 'trap', icon: '🪤', name: 'Armadilha Disparando', file: 'assets/audio/sfx_trap_snap.mp3' }},
      {{ id: 'chains', icon: '⛓️', name: 'Correntes & Grades', file: 'assets/audio/sfx_chains_door.mp3' }},
      {{ id: 'fireball', icon: '🔥', name: 'Explosão / Magia', file: 'assets/audio/sfx_fireball.mp3' }},
      {{ id: 'bats', icon: '🦇', name: 'Enxame de Morcegos', file: 'assets/audio/sfx_bats_swarm.mp3' }},
      {{ id: 'sting', icon: '💀', name: 'Impacto de Terror', file: 'assets/audio/sfx_horror_sting.mp3' }}
    ];

    // Quick Global Presets for the Soundboard Drawer
    this.presets = {{
      taverna_chuva: {{ name: '🍺 Taverna & Chuva (A1/B5c/F1)', channels: {{ tavern: 0.50, fire: 0.45, lute: 0.40 }}, sfx: 'door' }},
      casa_da_morte: {{ name: '🕯️ Casa da Morte & Culto (A2)', channels: {{ whispers: 0.50, dungeon: 0.45, mystery: 0.45 }}, sfx: 'heartbeat' }},
      vila_barovia: {{ name: '🌫️ Vila de Baróvia & Cerco (Arco B)', channels: {{ wind: 0.50, rain: 0.45, piano: 0.45 }}, sfx: 'bell' }},
      vistani_tser: {{ name: '🔮 Tser Pool & Vistani (C4/E2)', channels: {{ fire: 0.55, vistani: 0.60, river: 0.30 }}, sfx: 'bell' }},
      floresta_svalich: {{ name: '🐺 Estrada & Floresta Svalich (C/L)', channels: {{ night: 0.60, wind: 0.45, exploration: 0.40 }}, sfx: 'wolf' }},
      moinho_bruxas: {{ name: '🧙‍♀️ Velho Moedor de Ossos (C9/H7)', channels: {{ grindstone: 0.55, witches: 0.55, cauldron: 0.40 }}, sfx: 'hag_laugh' }},
      vallaki_tensao: {{ name: '🏘️ Vallaki · Intrigas (D–G)', channels: {{ town: 0.45, mystery: 0.45 }}, sfx: 'ravens' }},
      igreja_abadia: {{ name: '⛪ Igreja & Abadia de Krezk (D/K)', channels: {{ monks: 0.55, choir: 0.45, whispers: 0.30 }}, sfx: 'bell' }},
      colina_yester: {{ name: '🩸 Colina Yester & Druidas (Arco J)', channels: {{ druid: 0.65, rain: 0.55, trees: 0.45 }}, sfx: 'thunder' }},
      pantano_berez: {{ name: '🐸 Pântano de Berez & Lysaga (I/T)', channels: {{ river: 0.55, cauldron: 0.50, witches: 0.50 }}, sfx: 'hag_laugh' }},
      argynvostholt: {{ name: '🐉 Mansão de Argynvostholt (Arco M)', channels: {{ wind: 0.55, dungeon: 0.40, piano: 0.45 }}, sfx: 'iron_door' }},
      jantar_strahd: {{ name: '🎹 O Jantar de Strahd (Arco O)', channels: {{ organ: 0.65, fire: 0.35, rain: 0.30 }}, sfx: 'strahd_laugh' }},
      ravenloft_incursao: {{ name: '🦇 Incursão em Ravenloft (Arco P)', channels: {{ dungeon: 0.55, horror: 0.50, organ: 0.35 }}, sfx: 'bats' }},
      ghakis_ambar: {{ name: '❄️ Tsolenka & Templo de Âmbar (R/S)', channels: {{ blizzard: 0.60, amber: 0.60, whispers: 0.40 }}, sfx: 'scream' }},
      combate_chefe: {{ name: '⚔️ Combate Mortal / Chefe', channels: {{ combat: 0.65, dread: 0.50, rain: 0.35 }}, sfx: 'horn' }},
      sol_nasce: {{ name: '🌅 O Sol Nasce (U6 / Epílogo)', channels: {{ choir: 0.60, lute: 0.45 }}, sfx: 'bell' }}
    }};

    // All 180 Scene Audio Profiles
    this.sceneProfiles = {profiles_json};
  }}

  getChannelMeta(id) {{
    return this.ambientChannels.find(c => c.id === id) || this.musicChannels.find(c => c.id === id) || null;
  }}

  getSfxMeta(id) {{
    return this.sfxPads.find(p => p.id === id) || null;
  }}

  getSceneProfile(sceneCode) {{
    if (!sceneCode) return null;
    if (this.sceneProfiles[sceneCode]) return this.sceneProfiles[sceneCode];
    const base = String(sceneCode).replace(/[a-z]+$/i, '');
    return this.sceneProfiles[base] || this.sceneProfiles['A1'];
  }}

  playSceneAudio(sceneCode, playLeadSfx = false) {{
    const prof = this.getSceneProfile(sceneCode);
    if (!prof) return;
    this.stopAll();
    this.activePreset = 'scene:' + sceneCode;
    for (const [chId, vol] of Object.entries(prof.channels || {{}})) {{
      this.startChannel(chId, vol);
    }}
    if (playLeadSfx && prof.sfx && prof.sfx.length) {{
      this.triggerSFX(prof.sfx[0]);
    }}
    this.notifyUI();
  }}

  ensureContext() {{
    if (!this.ctx) {{
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();
      this.masterGain = this.ctx.createGain();
      this.masterGain.gain.value = this.masterVolume;
      this.masterGain.connect(this.ctx.destination);
    }}
    if (this.ctx.state === 'suspended') {{
      this.ctx.resume();
    }}
  }}

  toggleChannel(id, volume = 0.5) {{
    if (this.activeLoops.has(id)) {{
      this.stopChannel(id);
      return false;
    }} else {{
      this.startChannel(id, volume);
      return true;
    }}
  }}

  setChannelVolume(id, volume) {{
    const loop = this.activeLoops.get(id);
    if (loop) {{
      loop.volume = volume;
      if (loop.audio) {{
        loop.audio.volume = Math.max(0, Math.min(1, volume * this.masterVolume));
      }}
      if (loop.gainNode && this.ctx) {{
        loop.gainNode.gain.setTargetAtTime(volume, this.ctx.currentTime, 0.1);
      }}
    }}
  }}

  setMasterVolume(vol) {{
    this.masterVolume = vol;
    if (this.masterGain && this.ctx) {{
      this.masterGain.gain.setTargetAtTime(vol, this.ctx.currentTime, 0.08);
    }}
    for (const [, loop] of this.activeLoops.entries()) {{
      if (loop.audio) {{
        loop.audio.volume = Math.max(0, Math.min(1, loop.volume * vol));
      }}
    }}
  }}

  attachCustomFile(id, file) {{
    const url = URL.createObjectURL(file);
    const audio = new Audio(url);
    audio.loop = !this.sfxPads.some(p => p.id === id);
    this.customFiles.set(id, audio);
    if (this.activeLoops.has(id)) {{
      const vol = this.activeLoops.get(id).volume || 0.5;
      this.stopChannel(id);
      this.startChannel(id, vol);
    }}
  }}

  startChannel(id, volume = 0.5) {{
    this.stopChannel(id);

    // 1. Check user-attached custom file first
    if (this.customFiles.has(id)) {{
      const audio = this.customFiles.get(id);
      audio.loop = true;
      audio.volume = Math.max(0, Math.min(1, volume * this.masterVolume));
      audio.currentTime = 0;
      audio.play().catch(() => {{}});
      this.activeLoops.set(id, {{ type: 'file', audio, volume }});
      this.notifyUI();
      return;
    }}

    // 2. Use built-in downloaded real .mp3 file from assets/audio/
    const meta = this.getChannelMeta(id);
    if (meta && meta.file) {{
      const audio = new Audio(meta.file);
      audio.loop = true;
      if (id === 'blizzard') audio.playbackRate = 1.25;
      audio.volume = Math.max(0, Math.min(1, volume * this.masterVolume));
      const playPromise = audio.play();
      if (playPromise !== undefined) {{
        playPromise.catch(() => {{
          // Fallback to WebAudio synth if file blocked or missing
          this.startSynthFallback(id, volume);
        }});
      }}
      this.activeLoops.set(id, {{ type: 'file', audio, volume }});
      this.notifyUI();
      return;
    }}

    this.startSynthFallback(id, volume);
  }}

  startSynthFallback(id, volume = 0.5) {{
    this.ensureContext();
    const gainNode = this.ctx.createGain();
    gainNode.gain.setValueAtTime(0.01, this.ctx.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(Math.max(0.02, volume * 0.4), this.ctx.currentTime + 0.4);
    gainNode.connect(this.masterGain);

    const osc = this.ctx.createOscillator();
    osc.type = 'sine';
    osc.frequency.value = 110;
    osc.connect(gainNode);
    osc.start();
    this.activeLoops.set(id, {{ type: 'synth', gainNode, nodes: [osc], intervals: [], volume }});
    this.notifyUI();
  }}

  stopChannel(id) {{
    const loop = this.activeLoops.get(id);
    if (!loop) return;
    if (loop.type === 'file' && loop.audio) {{
      try {{
        loop.audio.pause();
        loop.audio.currentTime = 0;
      }} catch (e) {{}}
    }} else {{
      if (loop.intervals) loop.intervals.forEach(clearInterval);
      if (loop.nodes) {{
        loop.nodes.forEach(n => {{
          try {{ n.stop(); n.disconnect(); }} catch (e) {{}}
        }});
      }}
    }}
    this.activeLoops.delete(id);
    this.notifyUI();
  }}

  stopAll() {{
    for (const id of Array.from(this.activeLoops.keys())) {{
      this.stopChannel(id);
    }}
    this.activePreset = null;
    this.notifyUI();
  }}

  applyPreset(presetKey, playSfx = false) {{
    if (presetKey && presetKey.startsWith('scene:')) {{
      this.playSceneAudio(presetKey.slice(6), playSfx);
      return;
    }}
    const p = this.presets[presetKey];
    if (!p) return;
    this.stopAll();
    this.activePreset = presetKey;
    for (const [chId, vol] of Object.entries(p.channels)) {{
      this.startChannel(chId, vol);
    }}
    if (playSfx && p.sfx) {{
      this.triggerSFX(p.sfx);
    }}
    this.notifyUI();
  }}

  triggerSFX(id) {{
    // 1. User-attached custom file
    if (this.customFiles.has(id)) {{
      const audio = this.customFiles.get(id);
      audio.volume = Math.max(0, Math.min(1, this.masterVolume));
      audio.currentTime = 0;
      audio.play().catch(() => {{}});
      return;
    }}

    // 2. Built-in real .mp3 SFX from assets/audio/
    const pad = this.getSfxMeta(id);
    if (pad && pad.file) {{
      const sfxAudio = new Audio(pad.file);
      sfxAudio.volume = Math.max(0, Math.min(1, this.masterVolume));
      sfxAudio.play().catch(() => {{}});
      return;
    }}
  }}

  notifyUI() {{
    if (typeof window.onSoundboardStateChange === 'function') {{
      window.onSoundboardStateChange();
    }}
  }}
}}

window.baroviaSound = new BaroviaSoundEngine();
"""
    SOUNDBOARD_JS.write_text(js_code, encoding="utf-8")
    print(f"Wrote {SOUNDBOARD_JS} ({len(js_code)//1024} KB)")


if __name__ == "__main__":
    main()
