# -*- coding: utf-8 -*-
"""
Applies all Strahd Reloaded upgrades:
- Replaces legacy maps with new high-res maps (Death House floors, Old Bonegrinder HD, Barovia Church HD, etc.)
- Adds individual tactical floors for Death House (Floors 1, 2, 3, Dungeon)
- Registers all 33 scene illustrations and handouts
- Links illustrations to their matching scenes
- Writes updated campaign_data.json and campaign_data.js
"""
import os
import json

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(WORKSPACE, "data")
CAMPAIGN_JSON = os.path.join(DATA_DIR, "campaign_data.json")
CAMPAIGN_JS = os.path.join(DATA_DIR, "campaign_data.js")

with open(CAMPAIGN_JSON, "r", encoding="utf-8") as f:
    campaign = json.load(f)

# 1. Update maps
maps_map = {m["key"]: m for m in campaign["maps"]}

# Update Death House master map
if "real_27" in maps_map:
    maps_map["real_27"]["title"] = "Casa da Morte · Mansão dos Durst (Strahd Reloaded)"
    maps_map["real_27"]["file"] = "Casa_da_Morte_Mansao_Strahd_Reloaded.jpg"

# Add tactical floor maps
new_maps = [
    {
        "key": "reloaded_cdm_01",
        "title": "Casa da Morte · Porão dos Cultistas e Catacumbas (Strahd Reloaded)",
        "file": "Casa_da_Morte_Porao_Culto_Strahd_Reloaded.jpg",
        "group": "Strahd Reloaded",
        "arcs": ["A"]
    },
    {
        "key": "reloaded_cdm_02",
        "title": "Casa da Morte · Andar 1 (Térreo e Entrada Tática)",
        "file": "Casa_da_Morte_Andar_1_Terreo.jpg",
        "group": "Strahd Reloaded",
        "arcs": ["A"]
    },
    {
        "key": "reloaded_cdm_03",
        "title": "Casa da Morte · Andar 2 (Biblioteca e Salão de Música)",
        "file": "Casa_da_Morte_Andar_2_Biblioteca.jpg",
        "group": "Strahd Reloaded",
        "arcs": ["A"]
    },
    {
        "key": "reloaded_cdm_04",
        "title": "Casa da Morte · Andar 3 e Sótão (Quarto das Crianças)",
        "file": "Casa_da_Morte_Andar_3_Sotao.jpg",
        "group": "Strahd Reloaded",
        "arcs": ["A"]
    },
    {
        "key": "reloaded_cdm_05",
        "title": "Casa da Morte · Masmorra & Altar do Monte Rastejante",
        "file": "Casa_da_Morte_Masmorra_Catacumbas.jpg",
        "group": "Strahd Reloaded",
        "arcs": ["A"]
    },
    {
        "key": "reloaded_cdm_fachada",
        "title": "Casa da Morte · Fachada Exterior & Rua nas Brumas",
        "file": "Casa_da_Morte_Fachada_Exterior.jpg",
        "group": "Strahd Reloaded",
        "arcs": ["A"]
    }
]

for nm in new_maps:
    if nm["key"] not in maps_map:
        campaign["maps"].append(nm)
        maps_map[nm["key"]] = nm

# Upgrade files for other HD maps
upgrades = {
    "real_11": ("Velho Esmaga-Ossos (Ultra HD)", "Velho_Esmaga_Ossos_HD.jpg"),
    "real_22": ("Vila de Baróvia · Igreja do Padre Donavich (HD)", "Igreja_Barovia_HD.jpg"),
    "real_07": ("Vallaki · Estalagem Água Azul (HD)", "Estalagem_Agua_Azul_HD.jpg"),
    "real_09": ("Vallaki · Casa Wachter (HD)", "Casa_Wachter_HD.jpg"),
    "real_23": ("Vallaki · Loja de Caixões (HD)", "Loja_Caixoes_HD.jpg"),
    "real_21": ("Covil dos Lobisomens (HD)", "Covil_Lobisomens_HD.jpg"),
    "real_17": ("Vinícola Mago dos Vinhos (HD)", "Vinicola_HD.jpg"),
    "real_18": ("Templo de Âmbar (HD)", "Templo_Ambar_HD.jpg"),
    "real_15": ("Abadia de Santa Markovia (HD)", "Abadia_Santa_Markovia_HD.jpg"),
    "real_12": ("Argynvostholt · Mansão dos Dragões (HD)", "Argynvostholt_HD.jpg"),
    "real_26": ("Torre de Van Richten (HD)", "Torre_Van_Richten_HD.jpg"),
    "real_25": ("Berez · Cabana de Baba Lysaga (HD)", "Cabana_Baba_Lysaga_HD.jpg"),
    "novo_07": ("Cachoeira de Tser Falls (4K Strahd Reloaded)", "Tser_Falls_4K_Strahd_Reloaded.jpg"),
    "novo_09": ("Vallaki · Praça Central e Portões (4K Strahd Reloaded)", "Vallaki_Praca_4K_Strahd_Reloaded.jpg"),
    "novo_12": ("Lago Zarovich (4K Strahd Reloaded)", "Lago_Zarovich_4K_Strahd_Reloaded.jpg"),
    "novo_14": ("Monte Ghakis · Covil dos Bodaks (4K)", "Monte_Ghakis_Covil_Bodak_4K.jpg"),
    "novo_16": ("Os Três Santuários · Santuário das Rozana (4K)", "Santuario_Rozana_4K.jpg"),
}

for k, (new_title, new_file) in upgrades.items():
    if k in maps_map:
        maps_map[k]["title"] = new_title
        maps_map[k]["file"] = new_file

# 2. Master Illustrations Catalog
ILLUSTRATIONS = [
    {
        "id": "cdm_fachada",
        "title": "A Fachada da Casa da Morte",
        "subtitle": "A imponente mansão dos Durst envolta pelas brumas eternas de Baróvia",
        "file": "Casa_da_Morte_Fachada_Exterior.jpg",
        "category": "Fachadas & Atmosfera",
        "scenes": ["A2", "A2a", "A2h"]
    },
    {
        "id": "cdm_rose_thorn",
        "title": "Rose e Thornboldt Durst",
        "subtitle": "As crianças fantasmagóricas chorando diante da casa nas brumas",
        "file": "Rose_e_Thorn_Durst.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["A2d", "A2e"]
    },
    {
        "id": "cdm_quadro_durst",
        "title": "Retrato da Família Durst",
        "subtitle": "Pintura a óleo na mansão revelando os rostos soturnos de Gustav e Elisabeth",
        "file": "Quadro_Familia_Durst.jpg",
        "category": "Pistas & Handouts",
        "scenes": ["A2c", "A2f"]
    },
    {
        "id": "cdm_convite",
        "title": "Convite Selado de Gustav Durst",
        "subtitle": "Missiva formal convidando membros aos rituais secretos do culto",
        "file": "Carta_Convite_Gustav_Durst.jpg",
        "category": "Pistas & Handouts",
        "scenes": ["A2b"]
    },
    {
        "id": "cdm_walter",
        "title": "Walter, o Monte Rastejante",
        "subtitle": "A grotesca abominação de carne e relíquias erguida no altar do sacrifício",
        "file": "Walter_O_Monte_Rastejante.jpg",
        "category": "Monstros & Confrontos",
        "scenes": ["A2g"]
    },
    {
        "id": "strahd_dinner",
        "title": "Strahd no Jantar em Ravenloft",
        "subtitle": "O Senhor de Baróvia acolhendo os convidados em sua mesa sob candelabros de prata",
        "file": "Strahd_no_Jantar_Ravenloft.jpg",
        "category": "Fachadas & Atmosfera",
        "scenes": ["O5", "O4"]
    },
    {
        "id": "strahd_beucephalus",
        "title": "Strahd e Beucephalus",
        "subtitle": "O Conde de Baróvia montado em seu Corcel do Pesadelo diante da lua cheia",
        "file": "Strahd_e_Beucephalus.jpg",
        "category": "Monstros & Confrontos",
        "scenes": ["C2", "O4"]
    },
    {
        "id": "strahd_portrait",
        "title": "Conde Strahd von Zarovich",
        "subtitle": "Retrato régio do senhor supremo de Baróvia e primeiro vampiro",
        "file": "Conde_Strahd_von_Zarovich.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["D6", "U5"]
    },
    {
        "id": "ireena",
        "title": "Ireena Kolyana",
        "subtitle": "A nobre adotiva de Baróvia, alvo da obsessão eterna de Strahd",
        "file": "Ireena_Kolyana.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["B5d", "U2"]
    },
    {
        "id": "ismark",
        "title": "Ismark Kolyanovich",
        "subtitle": "Ismark, o Menor, novo burgomestre e espadachim da Vila de Baróvia",
        "file": "Ismark_Kolyanovich.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["B5a", "B5h"]
    },
    {
        "id": "doru_igreja",
        "title": "Doru nas Catacumbas",
        "subtitle": "A prole vampírica faminta acorrentada sob o tabuado da Igreja",
        "file": "Doru_Vampiro_Igreja.jpg",
        "category": "Monstros & Confrontos",
        "scenes": ["B5i"]
    },
    {
        "id": "doru_diario",
        "title": "Diário e Notas de Doru",
        "subtitle": "Páginas manchadas narrando o ataque fracassado ao Castelo Ravenloft",
        "file": "Diario_de_Doru.jpg",
        "category": "Pistas & Handouts",
        "scenes": ["B5i"]
    },
    {
        "id": "padre_lucian",
        "title": "Padre Lucian Petrovich",
        "subtitle": "O pároco devoto da Igreja de Santo Andral em Vallaki",
        "file": "Padre_Lucian_Petrovich.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["D1", "D5", "B5j"]
    },
    {
        "id": "barricadas_barovia",
        "title": "Barricadas Orientais de Baróvia",
        "subtitle": "Paliçadas de troncos e estacas erguidas contra os lobos de Strahd",
        "file": "Barricadas_Orientais_Barovia_HD.jpg",
        "category": "Fachadas & Atmosfera",
        "scenes": ["B5f", "B5g"]
    },
    {
        "id": "morgantha",
        "title": "Morgantha, a Bruxa Noturna",
        "subtitle": "A velha corcunda vendendo suas tortas de sonho pelas ruas enevoadas",
        "file": "Morgantha_Bruxa_Torta.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["C9", "B5b"]
    },
    {
        "id": "conluio_bruxas",
        "title": "O Conluio do Velho Esmaga-Ossos",
        "subtitle": "Morgantha, Bella e Offalia reunidas diante de seu caldeirão de ossos",
        "file": "Conluio_Bruxas_Esmaga_Ossos.jpg",
        "category": "Monstros & Confrontos",
        "scenes": ["C9", "H7"]
    },
    {
        "id": "cartaz_festival",
        "title": "Cartaz: Festival do Sol Incandescente",
        "subtitle": "Proclamação do Barão Vallakovich: 'Tudo Ficará Bem!'",
        "file": "Cartaz_Festival_Sol_Incandescente.jpg",
        "category": "Pistas & Handouts",
        "scenes": ["G2", "D1"]
    },
    {
        "id": "cartaz_carnaval",
        "title": "Cartaz: O Carnaval das Maravilhas de Rictavio",
        "subtitle": "Folheto colorido promovendo o espetáculo do misterioso mestre de picadeiro",
        "file": "Cartaz_Carnaval_Maravilhas_Rictavio.jpg",
        "category": "Pistas & Handouts",
        "scenes": ["E1", "E8"]
    },
    {
        "id": "izek_strazni",
        "title": "Izek Strazni",
        "subtitle": "O temido capitão da guarda de Vallaki com seu braço monstruoso farpado",
        "file": "Izek_Strazni_Braco_Demoniaco.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["F4", "G1"]
    },
    {
        "id": "lady_fiona",
        "title": "Lady Fiona Wachter",
        "subtitle": "A matriarca conspiradora e sacerdotisa leal de Strahd em Vallaki",
        "file": "Lady_Fiona_Wachter.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["F2", "H5"]
    },
    {
        "id": "stella_wachter",
        "title": "Stella Wachter",
        "subtitle": "A jovem nobre enlouquecida que acredita ser um gato",
        "file": "Stella_Wachter.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["H8"]
    },
    {
        "id": "victor_vallakovich",
        "title": "Victor Vallakovich",
        "subtitle": "O filho rebelde do Barão com seu grimório inacabado de teletransporte",
        "file": "Victor_Vallakovich.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["H2", "H4"]
    },
    {
        "id": "familia_martikov",
        "title": "A Família Martikov na Estalagem",
        "subtitle": "Urwin e Danika acolhendo os viajantes no aconchego da Água Azul",
        "file": "Familia_Martikov_Agua_Azul.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["F1", "J1"]
    },
    {
        "id": "rictavio",
        "title": "Rictavio / Dr. Rudolph van Richten",
        "subtitle": "O lendário caçador de monstros disfarçado como um bardo carnavalesco",
        "file": "Rictavio_Bardo_Circo.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["E6", "T4"]
    },
    {
        "id": "arabelle",
        "title": "Arabelle, a Pequena Vistana",
        "subtitle": "A garota profética resgatada das águas escuras do Lago Zarovich",
        "file": "Arabelle_Vistana_do_Lago.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["E4", "E8"]
    },
    {
        "id": "o_abade",
        "title": "O Abade Celestial",
        "subtitle": "O deva corrompido que rege a Abadia de Santa Markovia em Krezk",
        "file": "O_Abade_Celestial.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["K2", "Q3"]
    },
    {
        "id": "vasilka",
        "title": "Vasilka, a Noiva de Retalhos",
        "subtitle": "O golem de carne esculpido para ser a companheira eterna de Strahd",
        "file": "Vasilka_Criacao_do_Abade.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["K2b"]
    },
    {
        "id": "vladimir_horngaard",
        "title": "Sir Vladimir Horngaard",
        "subtitle": "O líder revenante dos Cavaleiros do Dragão Prateado em Argynvostholt",
        "file": "Vladimir_Horngaard_Revenante.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["M3", "M6"]
    },
    {
        "id": "kasimir_velikov",
        "title": "Kasimir Velikov",
        "subtitle": "O elfo do crepúsculo mutilado que busca ressuscitar sua irmã Patrina",
        "file": "Kasimir_Velikov_Elfo_do_Crepusculo.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["E2", "R1"]
    },
    {
        "id": "zuleika",
        "title": "Zuleika Toranescu",
        "subtitle": "A loba alfa que anseia pela libertação de seu companheiro aprisionado",
        "file": "Zuleika_Lobisomem.jpg",
        "category": "Personagens & NPCs",
        "scenes": ["L4"]
    },
    {
        "id": "roc_ghakis",
        "title": "O Roc do Monte Ghakis",
        "subtitle": "A gigantesca ave de rapina predadora que assola os picos congelados",
        "file": "O_Roc_do_Monte_Ghakis.jpg",
        "category": "Monstros & Confrontos",
        "scenes": ["R6"]
    },
    {
        "id": "carvalho_ancestral",
        "title": "O Carvalho Ancestral da Floresta",
        "subtitle": "A árvore milenar onde as brumas se concentram e os mortos sussurram",
        "file": "Carvalho_Ancestral_Svalich.jpg",
        "category": "Fachadas & Atmosfera",
        "scenes": ["C1", "R4"]
    },
    {
        "id": "monumento_marina",
        "title": "O Monumento de Marina em Berez",
        "subtitle": "O memorial de pedra solitário erguido nas ruínas pantanosas",
        "file": "Monumento_de_Marina_Berez.jpg",
        "category": "Fachadas & Atmosfera",
        "scenes": ["T3", "T3f"]
    }
]

campaign["illustrations"] = ILLUSTRATIONS

# Build lookup by scene code
illust_by_scene = {}
for ill in ILLUSTRATIONS:
    for sc in ill["scenes"]:
        if sc not in illust_by_scene:
            illust_by_scene[sc] = []
        illust_by_scene[sc].append(ill)

# 3. Update scenes: map_key & illustrations
scene_map_overrides = {
    "A2": "reloaded_cdm_fachada",
    "A2a": "real_27",
    "A2b": "reloaded_cdm_02",
    "A2c": "reloaded_cdm_03",
    "A2d": "reloaded_cdm_04",
    "A2e": "reloaded_cdm_04",
    "A2f": "reloaded_cdm_01",
    "A2g": "reloaded_cdm_05",
    "A2h": "real_27"
}

for s in campaign["scenes"]:
    code = s.get("code")
    if code in scene_map_overrides:
        s["map_key"] = scene_map_overrides[code]
        meta = maps_map.get(s["map_key"], {})
        s["map_title"] = meta.get("title", s.get("map_title", ""))
        s["map_file"] = meta.get("file", s.get("map_file", ""))

    # Attach illustration(s)
    if code in illust_by_scene:
        s["illustrations"] = illust_by_scene[code]
        s["illustration"] = illust_by_scene[code][0]

# Write JSON
with open(CAMPAIGN_JSON, "w", encoding="utf-8") as f:
    json.dump(campaign, f, ensure_ascii=False, indent=2)

# Write JS
js_content = f"// Strahd Reloaded Daggerheart Campaign Data v3.6 (HD Maps & Scene Illustrations)\nwindow.CAMPAIGN_DATA = {json.dumps(campaign, ensure_ascii=False, indent=2)};\n"
with open(CAMPAIGN_JS, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Updated campaign_data: {len(campaign['maps'])} maps, {len(campaign['illustrations'])} illustrations, {len(campaign['scenes'])} scenes.")
