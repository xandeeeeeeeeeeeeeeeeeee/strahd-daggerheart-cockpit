# -*- coding: utf-8 -*-
"""
Master Pipeline: Enrich Campaign Scenes for Strahd Reloaded Daggerheart Cockpit
Enriches scene descriptions, narrative context, gothic read-alouds, sensory immersion,
and Daggerheart DC dual-dice roll chips across all 180 scenes.
"""

import json
import os
import re
import sys
import shutil

# Ensure utf-8 stdout
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Import bespoke enriched content modules
from enrichment_content_arc_a import ARC_A_SCENES
from enrichment_content_arc_b import ARC_B_SCENES
from enrichment_content_arc_c import ARC_C_SCENES
from enrichment_content_remaining import REMAINING_SCENES

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
JSON_PATH = os.path.join(BASE_DIR, "data", "campaign_data.json")
JS_PATH = os.path.join(BASE_DIR, "data", "campaign_data.js")
MIRROR_DIR = r"C:\Users\Alex\Downloads\AUTOMAÇAO RPG\Vault RPG\_ferramentas\cockpit"

VALID_START_PREFIXES = (
    "## Roteiro",
    "## Preparação",
    "## Áreas",
    "## Chegada",
    "## Fuga",
    "## Ficha",
    "## Escolher",
    "## Emil",
    "## Libertar",
    "## O futuro",
    "## O tesouro",
    "## Q7",
    "## Voltar",
    "**Objetivo:",
    "**Contexto:"
)

def clean_obsidian_boilerplate(text, code, title):
    lines = text.split('\n')
    start_idx = 0
    for i, line in enumerate(lines):
        line_s = line.strip()
        if any(line_s.startswith(prefix) for prefix in VALID_START_PREFIXES):
            start_idx = i
            break
    
    cleaned_lines = lines[start_idx:]
    cleaned_text = '\n'.join(cleaned_lines)
    
    # Cut off bottom boilerplate
    cut_patterns = [
        r'\n## Mapas desta cena[\s\S]*$',
        r'\n---\s*\n← \[\[Strahd Reloaded[\s\S]*$',
        r'\n## Ao encerrar[\s\S]*$',
        r'\n## Encontros associados[\s\S]*$',
        r'\n\s*← \[\[Strahd Reloaded[\s\S]*$'
    ]
    for pat in cut_patterns:
        cleaned_text = re.sub(pat, '', cleaned_text)
    
    cleaned_text = cleaned_text.strip()
    return cleaned_text

def generate_sensory_and_narrar(sc):
    code = sc.get('code', '')
    title = sc.get('title', '')
    focus = sc.get('focus', 'Exploração')
    arc_code = sc.get('arc_code', '')
    
    # Location atmosphere themes
    if arc_code in ('A',):
        loc = "nos corredores lúgubres da Casa da Morte"
        sights = "Paredes de carvalho ressecadas, retratos solenes com olhos velados e sombras esguias que dançam com a luz trêmula das lamparinas."
        sounds = "O ranger cadenciado de assoalhos antigos, o gotejar distante em dutos de ventilação e o estalo de vigas sob tensão sobrenatural."
        smells = "Cera de abelha envelhecida, folhas mortas de outono, cinzas frias de lareira e um sutil toque metálico de cobre e sangue seco."
        touch = "Umidade gélida que arrepia a pele e faz os dedos tremerem ao tocar maçanetas de latão geladas."
    elif arc_code in ('B',):
        loc = "nas ruelas enevoadas e silenciosas da Vila de Baróvia"
        sights = "Sobrados góticos de madeira escura com venezianas trancadas, marcas de garras em batentes e a névoa leitosa que rasteja pelo solo enlameado."
        sounds = "O uivo solitário do vento entre as ruelas, o crocitar rouco de corvos nos telhados e o som distante de um sino fúnebre."
        smells = "Lama fétida, madeira molhada, fumaça cinzenta de turfa e o cheiro doce e pesado de decomposição recente."
        touch = "Gotas gélidas de chuva fina que cortam o rosto e lama pesada que gruda nas botas a cada passo."
    elif arc_code in ('C',):
        loc = "ao longo da Estrada Svalich e do cânion do Rio Ivlis"
        sights = "Pinheiros colossais de trinta metros de altura, águas escuras que serpenteiam por ravinas profundas e o penhasco monumental de Ravenloft vigiando o horizonte."
        sounds = "O bramido distante das águas caindo nas cataratas de Tser, galhos estalando na mata fechada e o canto fúnebre de pássaros noturnos."
        smells = "Resina de pinho fresco, musgo encharcado, terra ácida e o cheiro tênue de fogueiras distantes."
        touch = "Brisa cortante das montanhas e arrepio elétrico que avisa sobre predadores espreitando entre as árvores."
    elif arc_code in ('D', 'E', 'F', 'G'):
        loc = "nas ruas amuralhadas e tensas da cidade de Vallaki"
        sights = "Casas de enxaimel com bandeiras festivas desbotadas, guardas com lanças pontiagudas e moradores de olhares assustados que forçam sorrisos sem alma."
        sounds = "O murmurar tenso da multidão na praça central, carroças rangendo sobre paralelepípedos e o trote firme da guarda da cidade."
        smells = "Pão de centeio assado, cerveja amarga, esgoto canalizado e incenso vindo da igreja de Santo Andral."
        touch = "A sensação palpável de vigilância contínua, com espiões nos telhados e olhos atentos a qualquer palavra de discórdia."
    elif arc_code in ('H', 'I', 'J'):
        loc = "nas terras ocidentais, vinhedos e colinas antigas de Baróvia"
        sights = "Vinhedos carcomidos por vinhas secas, árvores retorcidas sob tempestades elétricas e torres antigas refletidas em lagos cinzentos."
        sounds = "O grasnar protetor de bandos de corvos em voo coordenado, trovões rolando pelas colinas e o zumbido de enxames de agulheiros."
        smells = "Uvas fermentadas no solo, terra vulcânica molhada e o odor elétrico e acre de ozônio que antecede relâmpagos arcanos."
        touch = "Gotas pesadas de chuva de verão e o calor abafado que precede tempestades mágicas no vale."
    elif arc_code in ('K', 'L', 'M'):
        loc = "nos limites austeros de Krezk e nos salões em ruínas de Argynvostholt"
        sights = "Muralhas maciças de pedra calcária, abadias erguidas nas alturas sob névoa espessa e esculturas de dragões de prata desbotadas pelo tempo."
        sounds = "O cântico desafinado e perturbador de criaturas híbridas na colina, passos pesados de armaduras espectrais e o uivo de alcateias de lobisomens."
        smells = "Incenso fúnebre, pelos molhados de predadores e o frio puro de neves eternas descendo dos picos rochosos."
        touch = "Vento glacial das montanhas que queima as bochechas e pedras seculares congeladas ao toque."
    elif arc_code in ('O',):
        loc = "nos pântanos apodrecidos e ruínas afundadas de Berez"
        sights = "Ruínas de pedra afundadas em lamaçal negro, salgueiros chorões com musgo escorrendo como barbas espectrais e a silhueta monstruosa de uma cabana que caminha sobre ossos gigantescos."
        sounds = "O coaxar rouco de milhares de rãs carnívoras, bolhas de gás do pântano estourando com barulho viscoso e gargalhadas estridentes ecoando na bruma."
        smells = "Lodo sulfuroso, matéria orgânica podre em fermentação e sangue antigo manchando raízes de árvores mortas."
        touch = "Água lodosa e pegajosa que suga as pernas e a umidade asfixiante que cola as roupas ao corpo."
    elif arc_code in ('P', 'R', 'S'):
        loc = "nos salões ciclópeos e sarcófagos esquecidos do Templo de Âmbar"
        sights = "Salões titânicos esculpidos no coração da montanha, blocos monumentais de âmbar translúcido brilhando com centelhas sombrias aprisionadas e estátuas colossais de deuses esquecidos."
        sounds = "Sussurros sedutores e frios ecoando diretamente dentro da mente, ecos de passos na pedra polida e o estalar de gelo que nunca derrete."
        smells = "Âmbar queimado, ozônio primordial, ar rarefeito de altitude extrema e o perfume venenoso do poder cósmico proibido."
        touch = "Um frio de zero absoluto que queima os dedos ao tocar a pedra e a atração magnética e tentadora das dádivas sombrias."
    elif arc_code in ('Q', 'T', 'U'):
        loc = "nos salões majestosos e catacumbas letais do Castelo Ravenloft"
        sights = "Arcadas góticas de trinta metros de altura, tapeçarias carmesins bordadas com brasões reais, vitrais refletindo relâmpagos roxos e sarcófagos de mármore negro enfileirados nas catacumbas."
        sounds = "O órgão de tubos ressoando acordes fúnebres imponentes, o crepitar de lareiras monumentais e o sussurro de vampiros se movendo nas sombras do teto."
        smells = "Vinho tinto nobre, incenso real, rosas frescas murchando e o cheiro metálico inconfundível de sangue aristocrático."
        touch = "Mármore polido gélido, veludo pesado de cortinas senhoriais e a presença asfixiante da vontade de ferro de Strahd von Zarovich."
    else:
        loc = "nas terras ancestrais de Baróvia"
        sights = "Paisagens dramáticas sob um céu de chumbo eterno, onde a névoa dança entre montanhas e florestas góticas."
        sounds = "O vento sussurrando segredos seculares através das copas dos pinheiros e o silêncio atento da natureza aprisionada."
        smells = "Pinho silvestre, terra encharcada e a pureza gélida do ar das montanhas."
        touch = "A gravidade solene de uma terra onde cada escolha cobra um tributo de sangue e honra."

    clean_short_title = re.sub(r'^[A-Z0-9]+[a-z]?\s*·\s*', '', title)
    
    # Read-aloud evocative quote
    narrar_quote = f"A névoa espessa abre-se lentamente sobre a paisagem de {clean_short_title}, revelando cada contorno gótico deste momento decisivo. O silêncio que cerca o local não é de paz, mas de expectativa predatória: cada sombra parece respirar e cada pedra guarda o eco de passos esquecidos. Diante de vocês, o destino de Baróvia exige decisões claras e lâminas afiadas."
    
    sensory_block = f"""**Ambiente & Sensações:**
- *Visão:* {sights}
- *Sons:* {sounds}
- *Cheiro:* {smells}
- *Tato & Clima:* {touch}"""

    narrar_block = f"""**Para narrar:** “{narrar_quote}”"""

    return sensory_block, narrar_block

def enrich_existing_scene(sc, cleaned_text):
    code = sc.get('code', '')
    title = sc.get('title', '')
    
    # Check if title header exists
    header = f"## Roteiro Completo · {code} · {title}"
    if not cleaned_text.startswith("## "):
        body = f"{header}\n\n{cleaned_text}"
    else:
        # Standardize header
        first_line, rest = cleaned_text.split('\n', 1) if '\n' in cleaned_text else (cleaned_text, '')
        body = f"{header}\n\n{rest.strip()}"
    
    # Ensure Objective exists
    if "**Objetivo:**" not in body:
        obj_match = re.search(r'\*\*(?:Objetivo|Função|Em uma frase):\*\*\s*([^\n]+)', body, re.IGNORECASE)
        if obj_match:
            obj_text = obj_match.group(1).strip()
            body = re.sub(r'\*\*(?:Objetivo|Função|Em uma frase):\*\*\s*[^\n]+', f"**Objetivo:** {obj_text}", body, count=1)
        else:
            body = f"{header}\n\n**Objetivo:** Conduzir os eventos de {title}, confrontar os dilemas imediatos do local e avançar os objetivos da campanha.\n\n{body[len(header):].strip()}"
    
    # Ensure Context exists
    if "**Contexto" not in body and "**Contexto & O que Está em Jogo:**" not in body:
        ctx_insert = f"**Contexto & O que Está em Jogo:** Os heróis encontram-se em um ponto crucial de Baróvia. As escolhas feitas nesta cena reverberam nas alianças políticas do vale e atraem a atenção do mestre de Ravenloft. O fracasso ou a hesitação alimentam a reserva de Medo e colocam inocentes em risco iminente.\n\n"
        # Insert after Objetivo line
        body = re.sub(r'(\*\*Objetivo:\*\*[^\n]+\n+)', r'\1' + ctx_insert, body, count=1)
    
    # Ensure Sensory and Para narrar exist
    has_narrar = "**Para narrar:**" in body or "**Narração:**" in body or "**Leitura em voz alta:**" in body
    has_sensory = "**Ambiente & Sensações:**" in body or "**Sensações:**" in body or "**Ambiente & Atmosfera:**" in body
    
    if not has_sensory or not has_narrar:
        sensory_block, narrar_block = generate_sensory_and_narrar(sc)
        inject_blocks = ""
        if not has_sensory:
            inject_blocks += sensory_block + "\n\n"
        if not has_narrar:
            inject_blocks += narrar_block + "\n\n"
        
        # Place before the first ### subsection or right after Contexto/Objetivo
        sub_match = re.search(r'\n(###\s+[^\n]+)', body)
        if sub_match:
            idx = sub_match.start()
            body = body[:idx] + "\n\n" + inject_blocks.strip() + "\n\n" + body[idx:].lstrip()
        else:
            body = body.strip() + "\n\n" + inject_blocks.strip()
    
    # Ensure Investigation DCs are formatted with clickable chips
    # Replace plain 'Instinto CD 12' or 'Presença 10' with 'Instinto (CD 12)'
    body = re.sub(r'\b(Instinto|Presença|Conhecimento|Agilidade|Força|Finesse)\s+(\d{1,2})\b', r'\1 (CD \2)', body)
    body = re.sub(r'\bCD\s*(\d{1,2})\b(?!\))', r'(CD \1)', body)
    
    # Ensure Daggerheart callout exists
    if "**Daggerheart:" not in body and "**DH:" not in body and "**Daggerheart & Mecânicas:**" not in body:
        dh_block = "\n\n**Daggerheart & Mecânicas:** Sucessos com Esperança geram momentos heróicos e pistas adicionais. Falhas com Medo permitem ao Mestre avançar relógios de perigo ou gastar 1 Ponto de Medo para manifestar complicações imediatas no ambiente."
        body = body.strip() + dh_block
    
    return body.strip()

def main():
    print("=== STARTING CAMPAIGN SCENE ENRICHMENT PIPELINE ===")
    if not os.path.exists(JSON_PATH):
        print(f"Error: {JSON_PATH} not found!")
        sys.exit(1)
        
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    scenes = data.get('scenes', [])
    print(f"Total campaign scenes: {len(scenes)}")
    
    bespoke_count = 0
    cleaned_count = 0
    enriched_count = 0
    
    all_bespoke = {}
    all_bespoke.update(ARC_A_SCENES)
    all_bespoke.update(ARC_B_SCENES)
    all_bespoke.update(ARC_C_SCENES)
    all_bespoke.update(REMAINING_SCENES)
    
    print(f"Bespoke high-detail scenes available: {len(all_bespoke)}")
    
    for sc in scenes:
        code = sc.get('code', '')
        title = sc.get('title', '')
        raw_before = sc.get('roteiro_raw', '')
        
        if code in all_bespoke:
            # Apply bespoke rich narrative script
            enriched_text = all_bespoke[code].strip()
            sc['roteiro_raw'] = enriched_text
            sc['roteiro_formatted'] = enriched_text
            bespoke_count += 1
        else:
            # Clean and systematically enrich existing scene text
            cleaned_text = clean_obsidian_boilerplate(raw_before, code, title)
            enriched_text = enrich_existing_scene(sc, cleaned_text)
            sc['roteiro_raw'] = enriched_text
            sc['roteiro_formatted'] = enriched_text
            enriched_count += 1
            
        cleaned_count += 1

    print(f"Bespoke scenes applied: {bespoke_count}")
    print(f"Systematically enriched scenes: {enriched_count}")
    print(f"Total scenes processed: {cleaned_count}")
    
    # Save campaign_data.json
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved: {JSON_PATH}")
    
    # Save campaign_data.js
    with open(JS_PATH, 'w', encoding='utf-8') as f:
        f.write("// Strahd Reloaded Daggerheart Campaign Data v3.7 (Enriched Descriptions & Context)\n")
        f.write("window.CAMPAIGN_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n")
    print(f"Saved: {JS_PATH}")
    
    # Mirror files to Vault RPG cockpit
    if os.path.exists(MIRROR_DIR):
        print(f"Mirroring to {MIRROR_DIR}...")
        mirror_data_dir = os.path.join(MIRROR_DIR, "data")
        os.makedirs(mirror_data_dir, exist_ok=True)
        shutil.copy2(JSON_PATH, os.path.join(mirror_data_dir, "campaign_data.json"))
        shutil.copy2(JS_PATH, os.path.join(mirror_data_dir, "campaign_data.js"))
        shutil.copy2(os.path.join(BASE_DIR, "styles.css"), os.path.join(MIRROR_DIR, "styles.css"))
        shutil.copy2(os.path.join(BASE_DIR, "app.js"), os.path.join(MIRROR_DIR, "app.js"))
        print("Mirror sync complete!")
    else:
        print(f"Notice: Mirror dir {MIRROR_DIR} does not exist on this machine.")

    print("=== PIPELINE EXECUTION FINISHED SUCCESSFULLY ===")

if __name__ == "__main__":
    main()
