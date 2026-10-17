# -*- coding: utf-8 -*-
"""
Upgrades Mapas_Reais_Revelaveis_Barovia.html to v3.5 (Minimalist UI + Real High-Res Maps + 2nd Physical Monitor Optimization + Anti-Spoiler Player Layer):
- Embeds all 28 original book maps + all 16 real high-resolution community/official maps downloaded from GitHub (Mike Schley, DM Andy, etc.)
- Uses Player-Safe base images (without area numbers/markers) for Regional Barovia and Vallaki when projecting to the 2nd monitor
- Minimalist, single-bar compact toolbar (zero visual clutter, maximum canvas area)
- Synchronizes Zoom & Pan viewport framing with the 2nd physical monitor + Brightness/Contrast boost for TV/Monitor visibility across the table
- Strips all GM spoilers from map titles shown to players
"""

import os
import json
import base64
from pathlib import Path
import io
from PIL import Image

WORKSPACE = Path(r"c:\Users\Alex\Documents\antigravity\beautiful-bohr")
VAULT_DIR = Path(r"C:\Users\Alex\Downloads\AUTOMAÇAO RPG\Vault RPG")
ORIG_HTML_PATH = VAULT_DIR / "_ferramentas" / "mapas" / "Mapas_Reais_Revelaveis_Barovia.html"
DOWNLOADS_HTML_PATH = Path(r"C:\Users\Alex\Downloads\Mapas_Reais_Revelaveis_Barovia.html")
WORKSPACE_HTML_PATH = WORKSPACE / "mapas.html"
VAULT_COCKPIT_MAP_PATH = VAULT_DIR / "_ferramentas" / "cockpit" / "mapas.html"

CAMPAIGN_JSON = WORKSPACE / "data" / "campaign_data.json"
MAPS_DIR = WORKSPACE / "assets" / "maps"


def encode_optimized_image(img_path: Path, max_dim=2200, quality=82):
    with Image.open(img_path) as im:
        im = im.convert("RGB")
        if im.width > max_dim or im.height > max_dim:
            im.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=quality, optimize=True)
        b64 = base64.b64encode(buf.getvalue()).decode("ascii")
        return b64, im.width, im.height


def extract_original_28_maps(html_path: Path):
    text = html_path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("const MAPS="):
            json_str = line[len("const MAPS="):].rstrip(";")
            all_loaded = json.loads(json_str)
            return [m for m in all_loaded if str(m.get("key", "")).startswith("real_")]
    raise RuntimeError("Could not find const MAPS= in HTML")


def build_upgraded_html():
    orig_maps = extract_original_28_maps(ORIG_HTML_PATH)
    print(f"Preserved {len(orig_maps)} original book maps.")

    campaign = json.loads(CAMPAIGN_JSON.read_text(encoding="utf-8"))
    all_maps_meta = campaign["maps"]
    scenes = campaign["scenes"]

    meta_by_key = {cm["key"]: cm for cm in all_maps_meta}
    for m in orig_maps:
        cm = meta_by_key.get(m["key"], {})
        m["category"] = "Planta do Livro"
        m["arcs"] = cm.get("arcs", [])
        m["publicTitle"] = m["title"].split("·")[0].strip()

        # Replace with high-resolution Strahd Reloaded / HD image if available
        if cm.get("file"):
            img_path = MAPS_DIR / cm["file"]
            if img_path.exists():
                b64, w, h = encode_optimized_image(img_path)
                m["src"] = f"data:image/jpeg;base64,{b64}"
                m["w"] = w
                m["h"] = h
                if "title" in cm:
                    m["title"] = cm["title"]
                    m["publicTitle"] = cm["title"].split("·")[0].strip()

    # Append the 16 real high-resolution maps + new Strahd Reloaded tactical floors
    new_maps_list = [cm for cm in all_maps_meta if cm["key"].startswith("novo_") or cm["key"].startswith("reloaded_")]
    for cm in new_maps_list:
        key = cm["key"]
        img_path = MAPS_DIR / cm["file"]
        if not img_path.exists():
            continue
        b64, w, h = encode_optimized_image(img_path)

        category_label = "Strahd Reloaded · Tático" if key.startswith("reloaded_") else "Mapa Tático / Regional"
        entry = {
            "key": key,
            "title": f"★ {cm['title']}",
            "publicTitle": cm["title"].split("·")[0].strip(),
            "src": f"data:image/jpeg;base64,{b64}",
            "w": w,
            "h": h,
            "category": category_label,
            "arcs": cm.get("arcs", [])
        }

        # Check if a player-safe version (without pins/numbers) exists
        player_candidate = MAPS_DIR / cm["file"].replace(".jpg", "_Players.jpg")
        if player_candidate.exists():
            pb64, _, _ = encode_optimized_image(player_candidate)
            entry["playerSrc"] = f"data:image/jpeg;base64,{pb64}"

        orig_maps.append(entry)

    print(f"Total embedded maps in v3.6: {len(orig_maps)}")

    scene_index = []
    for s in scenes:
        arc_label = s["arcs"][0] if s.get("arcs") else s.get("arc_code", "Geral")
        # Public non-spoiler name: only the general location, never the plot twist
        scene_index.append({
            "code": s["code"],
            "title": s["title"],
            "arc": arc_label,
            "mapKey": s.get("map_key", "novo_01"),
            "mapName": s.get("map_title", ""),
        })

    maps_json = json.dumps(orig_maps, ensure_ascii=False)
    scenes_json = json.dumps(scene_index, ensure_ascii=False)

    html = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Baróvia · Mapas com Névoa (v3.5 Minimalista)</title>
<style>
*{{box-sizing:border-box}}
html,body{{margin:0;padding:0;height:100vh;overflow:hidden;background:#0a0c10;color:#ece7dc;font:13.5px/1.4 'Inter','Segoe UI',system-ui,sans-serif}}
#app{{display:flex;flex-direction:column;height:100vh;width:100vw;overflow:hidden}}
header.bar{{background:#12151e;border-bottom:1px solid #262d40;padding:6px 10px;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:6px;z-index:10}}
.group{{display:flex;align-items:center;gap:5px;flex-wrap:wrap}}
button,select,input{{font:inherit;color:inherit}}
button,select{{height:32px;background:#1b202e;border:1px solid #353f58;border-radius:6px;padding:0 9px;cursor:pointer;white-space:nowrap;transition:all .12s}}
button:hover,select:hover{{border-color:#e5c170;background:#232a3c}}
button[aria-pressed=true]{{background:#e5c170;color:#0b0d12;border-color:#ffe391;font-weight:700}}
button.live-btn{{background:#115e45;border-color:#34d399;color:#ecfdf5;font-weight:600}}
button.danger:hover{{background:#691515;border-color:#f87171}}
select{{max-width:250px;text-overflow:ellipsis}}
input[type=range]{{width:85px;accent-color:#e5c170;cursor:pointer}}
.sep{{width:1px;height:20px;background:#283044;margin:0 2px}}
.viewport{{flex:1;overflow:auto;background:#050608;position:relative;display:flex;align-items:safe center;justify-content:safe center}}
.viewport.pan-cursor{{cursor:grab}}
.viewport.pan-cursor.panning{{cursor:grabbing}}
.stage{{position:relative;transform-origin:top left;flex-shrink:0}}
.stage canvas{{display:block;width:100%;height:100%;position:absolute;top:0;left:0}}
#base{{position:relative}}
#fog{{touch-action:none;opacity:.46}}
#secret{{pointer-events:none;opacity:.62}}
#tactical{{pointer-events:none;opacity:1}}
.player #fog,.player #secret{{opacity:1}}
.pan #fog{{pointer-events:none}}
.player .master{{display:none!important}}
.back{{display:none;position:fixed;top:10px;left:10px;z-index:99;background:#e5c170;color:#111;font-weight:700}}
.player .back{{display:inline-flex;align-items:center}}
footer.foot{{height:28px;background:#0f1219;border-top:1px solid #222838;padding:0 12px;display:flex;align-items:center;justify-content:space-between;font-size:12px;color:#94a0b8}}
#status{{color:#e5c170;margin:0}}

@media (max-width: 768px) {{
  header.bar {{
    padding: 4px 6px;
    gap: 4px;
    overflow-x: auto;
    flex-wrap: nowrap;
    -webkit-overflow-scrolling: touch;
    white-space: nowrap;
    scrollbar-width: none;
    height: auto;
    min-height: 38px;
  }}
  .group {{
    flex-wrap: nowrap;
    flex-shrink: 0;
    gap: 4px;
  }}
  button, select {{
    height: 30px;
    padding: 0 6px;
    font-size: 11.5px;
  }}
  select {{
    max-width: 150px;
  }}
  footer.foot {{
    font-size: 10.5px;
    padding: 0 6px;
  }}
}}
</style>
</head>
<body>
<div id="app">
  <button id="back" class="back">⬅ Voltar ao Mestre</button>

  <header class="bar master">
    <!-- Seleção de Cena e Mapa -->
    <div class="group">
      <select id="sceneSelect" title="Escolher cena do roteiro (180 cenas)">
        <option value="">🎯 Cena (A1–EP6)…</option>
      </select>
      <select id="map" title="Escolher planta ou mapa (44 mapas)"></select>
    </div>

    <!-- Ferramentas de Névoa e Zoom Sincronizado -->
    <div class="group">
      <button id="reveal" aria-pressed="true" title="Revelar névoa">☀️ Revelar</button>
      <button id="cover" aria-pressed="false" title="Cobrir com névoa">🌑 Cobrir</button>
      <button id="lock" aria-pressed="false" title="Ocultar segredo ('S', armadilhas)">🔒 Segredo</button>
      <button id="unlock" aria-pressed="false" title="Remover bloqueio de segredo">🔓</button>
      <button id="pan" aria-pressed="false" title="Arrastar com o mouse para mover o mapa (ou botão do meio do mouse)">✋ Mover</button>
      <div class="sep"></div>
      <button id="shapeBrush" aria-pressed="true" title="Pincel circular">🖌️</button>
      <button id="shapeRect" aria-pressed="false" title="Revelar/cobrir sala em retângulo">▭ Sala</button>
      <label style="display:inline-flex;align-items:center;gap:4px;font-size:12px" title="Tamanho do pincel">
        <span id="radiusText">45</span>
        <input id="radius" type="range" min="6" max="200" value="45">
      </label>
      <div class="sep"></div>
      <button id="zoomOutBtn" title="Diminuir Zoom">-</button>
      <label style="display:inline-flex;align-items:center;gap:4px;font-size:12px" title="Zoom do mapa (sincronizado com o 2º Monitor)">
        <span id="zoomText" style="min-width:38px;text-align:center;font-weight:700;color:#ffe391">100%</span>
        <input id="zoom" type="range" min="0.5" max="5" step="0.1" value="1">
      </label>
      <button id="zoomInBtn" title="Aumentar Zoom">+</button>
      <button id="zoomFitBtn" title="Ajustar mapa inteiro à tela (100%)">1× Ajustar</button>
      <button id="undo" title="Desfazer última ação">↩</button>
      <button id="reset" class="danger" title="Cobrir tudo (toque 2x)">Cobrir Tudo</button>
      <button id="all" title="Revelar tudo exceto segredos bloqueados (toque 2x)">Revelar Tudo</button>
    </div>

    <!-- Tokens, Ping e 2º Monitor -->
    <div class="group">
      <button id="pingMode" aria-pressed="false" title="Clique no mapa para apontar na tela dos jogadores">🎯 Ping</button>
      <button id="tokenDragMode" aria-pressed="false" title="Arrastar tokens (botão direito edita/exclui)">♟️ Tokens</button>
      <button id="addPC" title="Adicionar PJ">+PJ</button>
      <button id="addEnemy" title="Adicionar Inimigo">+Inimigo</button>
      <button id="toggleRings" aria-pressed="false" title="Mostrar anéis de alcance Daggerheart">⭕ Alcances</button>
      <button id="clearTokens" class="danger" title="Limpar tokens">🗑️</button>
      <div class="sep"></div>
      <button id="syncViewBtn" aria-pressed="true" title="Sincronizar o Zoom/Enquadramento exato do Mestre com o 2º Monitor dos Jogadores">🔍 Sincronizar Zoom</button>
      <button id="boostBtn" aria-pressed="true" title="Aumentar brilho e nitidez no 2º Monitor para melhor visibilidade à distância">💡 Brilho TV</button>
      <button id="live" class="live-btn" title="Abrir janela limpa para o 2º monitor físico">📺 2º Monitor</button>
    </div>
  </header>

  <div class="viewport" id="viewport">
    <div class="stage" id="stage">
      <canvas id="base"></canvas>
      <canvas id="fog"></canvas>
      <canvas id="secret"></canvas>
      <canvas id="tactical"></canvas>
    </div>
  </div>

  <footer class="foot master">
    <span id="status">Carregando…</span>
    <div style="display:flex;gap:8px;align-items:center">
      <button id="view" style="height:22px;font-size:11px">👁️ Testar Vista Jogador</button>
      <button id="export" style="height:22px;font-size:11px">📸 Baixar PNG</button>
      <button id="save" style="height:22px;font-size:11px">💾 Salvar</button>
      <label style="font-size:11px;cursor:pointer">📂 Restaurar <input id="restore" type="file" accept=".json" style="display:none"></label>
    </div>
  </footer>
  <a id="fallback" style="display:none" download></a>
</div>

<script>
const MAPS={maps_json};
const SCENES={scenes_json};

const $=id=>document.getElementById(id);
const base=$('base'),fog=$('fog'),secret=$('secret'),tactical=$('tactical');
const b=base.getContext('2d'),f=fog.getContext('2d'),s=secret.getContext('2d'),t=tactical.getContext('2d');

// Hidden offscreen canvas holding the Player-Safe base image (without DM pins/numbers when available)
const playerBaseCanvas=document.createElement('canvas');
const pbCtx=playerBaseCanvas.getContext('2d');

let current=0,mode='reveal',shape='brush',ready=false,down=false,last=null,rectStart=null,rectCurrent=null;
let history=[],serial=0,states={{}},tacticalStates={{}},url=null,armed={{}},storageOK=true;
let playerWindow=null,liveTimer=null,liveSequence=0;
let showRings=false,selectedTokenId=null,draggingToken=null,pings=[];
let syncViewportToPlayer=true, boostPlayerBrightness=true;
let isPanning=false, panStartX=0, panStartY=0, panScrollLeft=0, panScrollTop=0;

const liveToken='barovia-'+Date.now()+'-'+Math.random().toString(36).slice(2);
const bc = typeof BroadcastChannel !== 'undefined' ? new BroadcastChannel('strahd-daggerheart-live') : null;

try{{
  states=JSON.parse(localStorage.getItem('barovia-real-v2')||'{{}}');
  if(!states||typeof states!=='object')states={{}};
  tacticalStates=JSON.parse(localStorage.getItem('barovia-tactical-v3')||'{{}}');
  if(!tacticalStates||typeof tacticalStates!=='object')tacticalStates={{}};
}}catch(e){{storageOK=false;states={{}};tacticalStates={{}}}}

const say=x=>$('status').textContent=x;
const img=src=>new Promise((resolve,reject)=>{{const a=new Image;a.onload=()=>resolve(a);a.onerror=reject;a.src=src}});

const grpNew=document.createElement('optgroup');grpNew.label='🗺️ Mapas Regionais, Urbanos e de Encontros (16)';
const grpOrig=document.createElement('optgroup');grpOrig.label='📜 Plantas de Masmorras e Locais do Livro (28)';
MAPS.forEach((m,i)=>{{
  const o=document.createElement('option');
  o.value=i;
  o.textContent=m.title;
  if(String(m.key).startsWith('novo_'))grpNew.append(o);
  else grpOrig.append(o);
}});
$('map').append(grpNew,grpOrig);

const arcsMap=new Map();
SCENES.forEach(sc=>{{
  if(!arcsMap.has(sc.arc))arcsMap.set(sc.arc,[]);
  arcsMap.get(sc.arc).push(sc);
}});
for(const [arcName,list] of arcsMap.entries()){{
  const og=document.createElement('optgroup');
  og.label=arcName;
  list.forEach(sc=>{{
    const o=document.createElement('option');
    o.value=sc.mapKey;
    o.textContent=`${{sc.code}} · ${{sc.title}}`;
    og.append(o);
  }});
  $('sceneSelect').append(og);
}}

$('sceneSelect').onchange=()=>{{
  const key=$('sceneSelect').value;
  if(!key)return;
  const idx=MAPS.findIndex(m=>m.key===key);
  if(idx>=0){{$('map').value=idx;load(idx);}}
}};

function getMapTokens(){{
  const k=MAPS[current].key;
  if(!Array.isArray(tacticalStates[k]))tacticalStates[k]=[];
  return tacticalStates[k];
}}

function saveTokens(){{
  try{{localStorage.setItem('barovia-tactical-v3',JSON.stringify(tacticalStates))}}catch(e){{}}
  renderTactical();
  queueLive();
}}

function fill(){{
  f.globalCompositeOperation='source-over';
  f.fillStyle='#090d14';
  f.fillRect(0,0,fog.width,fog.height);
}}

function persist(){{
  if(!ready)return;
  states[MAPS[current].key]={{fog:fog.toDataURL(),secret:secret.toDataURL()}};
  try{{localStorage.setItem('barovia-real-v2',JSON.stringify(states))}}catch(e){{storageOK=false}}
  queueLive();
}}

function snapshot(){{
  history.push({{fog:fog.toDataURL(),secret:secret.toDataURL()}});
  if(history.length>12)history.shift();
}}

// Exact normalized visible rectangle [0..1] of #base inside #viewport using getBoundingClientRect()
function getViewportNorm(){{
  const vp=$('viewport');
  const rVp=vp.getBoundingClientRect();
  const rImg=base.getBoundingClientRect();
  const z=Number($('zoom').value)||1;
  if(!rImg.width || !rImg.height)return {{x:0,y:0,w:1,h:1,zoom:z}};

  const left=Math.max(rVp.left, rImg.left);
  const top=Math.max(rVp.top, rImg.top);
  const right=Math.min(rVp.right, rImg.right);
  const bottom=Math.min(rVp.bottom, rImg.bottom);

  const x=Math.max(0, Math.min(1, (left - rImg.left) / rImg.width));
  const y=Math.max(0, Math.min(1, (top - rImg.top) / rImg.height));
  const w=Math.max(0.04, Math.min(1 - x, (right - left) / rImg.width));
  const h=Math.max(0.04, Math.min(1 - y, (bottom - top) / rImg.height));

  return {{x, y, w, h, zoom:z}};
}}

// Instant lightweight viewport sync (60fps, no JPEG re-encoding needed on scroll/zoom)
function sendViewportLive(){{
  if(!ready)return;
  const msg={{
    type:'barovia-player-viewport',
    viewport: syncViewportToPlayer ? getViewportNorm() : null
  }};
  if(playerWindow&&!playerWindow.closed){{
    try{{playerWindow.postMessage(msg,'*')}}catch(e){{}}
  }}
  if(bc){{
    try{{bc.postMessage(msg)}}catch(e){{}}
  }}
}}

function zoom(keepCenter=true){{
  const vp=$('viewport');
  const st=$('stage');
  const m=MAPS[current];
  if(!m||!vp)return;
  const z=Number($('zoom').value)||1;
  $('zoomText').textContent=Math.round(z*100)+'%';

  const prev=getViewportNorm();
  const cx=prev.x + prev.w/2;
  const cy=prev.y + prev.h/2;

  const availW=Math.max(200, vp.clientWidth - 12);
  const availH=Math.max(200, vp.clientHeight - 12);
  const fitScale=Math.min(availW / m.w, availH / m.h);

  const targetW=Math.max(100, Math.round(m.w * fitScale * z));
  const targetH=Math.max(100, Math.round(m.h * fitScale * z));

  st.style.width=targetW+'px';
  st.style.height=targetH+'px';

  if(keepCenter){{
    vp.scrollLeft=Math.max(0, Math.round(cx * targetW - vp.clientWidth/2));
    vp.scrollTop=Math.max(0, Math.round(cy * targetH - vp.clientHeight/2));
  }}
  sendViewportLive();
}}

function stepZoom(delta){{
  const cur=Number($('zoom').value)||1;
  const next=Math.max(0.5, Math.min(5, Math.round((cur + delta)*10)/10));
  $('zoom').value=next;
  zoom(true);
}}

$('zoomInBtn').onclick=()=>stepZoom(0.2);
$('zoomOutBtn').onclick=()=>stepZoom(-0.2);
$('zoomFitBtn').onclick=()=>{{
  $('zoom').value=1;
  zoom(false);
  $('viewport').scrollTo?.(0,0);
  sendViewportLive();
}};

window.addEventListener('resize',()=>zoom(true));

$('viewport').addEventListener('scroll',()=>{{
  if(syncViewportToPlayer)sendViewportLive();
}}, {{passive:true}});

// Mouse-wheel zoom (Ctrl+Wheel in any mode, or Wheel directly in Mover mode)
$('viewport').addEventListener('wheel',e=>{{
  if(e.ctrlKey || e.metaKey || mode==='pan'){{
    e.preventDefault();
    stepZoom(e.deltaY < 0 ? 0.15 : -0.15);
  }}
}}, {{passive:false}});

// Click-and-drag panning in Mover mode or with Middle Mouse Button (button === 1)
$('viewport').addEventListener('pointerdown',e=>{{
  if(mode==='pan' || e.button===1 || e.shiftKey){{
    isPanning=true;
    panStartX=e.clientX;
    panStartY=e.clientY;
    panScrollLeft=$('viewport').scrollLeft;
    panScrollTop=$('viewport').scrollTop;
    $('viewport').classList.add('panning');
    try{{$('viewport').setPointerCapture(e.pointerId)}}catch(err){{}}
    e.preventDefault();
  }}
}});

$('viewport').addEventListener('pointermove',e=>{{
  if(!isPanning)return;
  const dx=e.clientX - panStartX;
  const dy=e.clientY - panStartY;
  $('viewport').scrollLeft = panScrollLeft - dx;
  $('viewport').scrollTop = panScrollTop - dy;
  sendViewportLive();
}});

for(const ev of ['pointerup','pointercancel','lostpointercapture']){{
  $('viewport').addEventListener(ev,()=>{{
    if(isPanning){{
      isPanning=false;
      $('viewport').classList.remove('panning');
      sendViewportLive();
    }}
  }});
}}

$('syncViewBtn').onclick=()=>{{
  syncViewportToPlayer=!syncViewportToPlayer;
  $('syncViewBtn').setAttribute('aria-pressed',String(syncViewportToPlayer));
  sendViewportLive();
}};

$('boostBtn').onclick=()=>{{
  boostPlayerBrightness=!boostPlayerBrightness;
  $('boostBtn').setAttribute('aria-pressed',String(boostPlayerBrightness));
  queueLive();
}};

function renderTactical(forPlayer=false, targetCtx=t){{
  const w=tactical.width, h=tactical.height;
  if(targetCtx===t)targetCtx.clearRect(0,0,w,h);

  if(!forPlayer && down && shape==='rect' && rectStart && rectCurrent){{
    targetCtx.save();
    targetCtx.strokeStyle=mode==='reveal'||mode==='unlock'?'#ffe391':'#ef4444';
    targetCtx.lineWidth=3;
    targetCtx.setLineDash([8,6]);
    const rx=Math.min(rectStart.x,rectCurrent.x), ry=Math.min(rectStart.y,rectCurrent.y);
    const rw=Math.abs(rectCurrent.x-rectStart.x), rh=Math.abs(rectCurrent.y-rectStart.y);
    targetCtx.strokeRect(rx,ry,rw,rh);
    targetCtx.fillStyle=mode==='reveal'||mode==='unlock'?'rgba(255,227,145,0.15)':'rgba(239,68,68,0.2)';
    targetCtx.fillRect(rx,ry,rw,rh);
    targetCtx.restore();
  }}

  const tokens=getMapTokens();
  tokens.forEach(tk=>{{
    if(showRings && (tk.id===selectedTokenId || (!selectedTokenId && tk.type==='pc'))){{
      const rings=[
        {{r:50, color:'rgba(239,68,68,0.85)', label:'Corpo a Corpo'}},
        {{r:130, color:'rgba(245,158,11,0.8)', label:'Muito Próximo'}},
        {{r:260, color:'rgba(56,189,248,0.75)', label:'Próximo'}},
        {{r:420, color:'rgba(168,85,247,0.65)', label:'Distante'}}
      ];
      rings.forEach(rg=>{{
        targetCtx.save();
        targetCtx.beginPath();
        targetCtx.arc(tk.x,tk.y,rg.r,0,Math.PI*2);
        targetCtx.strokeStyle=rg.color;
        targetCtx.lineWidth=3;
        targetCtx.setLineDash([8,5]);
        targetCtx.stroke();
        targetCtx.fillStyle=rg.color;
        targetCtx.font='bold 14px system-ui';
        targetCtx.fillText(rg.label, tk.x+8, tk.y-rg.r+16);
        targetCtx.restore();
      }});
    }}

    const rad=tk.type==='boss'?26:22;
    targetCtx.save();
    targetCtx.beginPath();
    targetCtx.arc(tk.x,tk.y,rad,0,Math.PI*2);
    targetCtx.fillStyle=tk.color||'#2563eb';
    targetCtx.fill();
    targetCtx.lineWidth=4;
    targetCtx.strokeStyle=tk.id===selectedTokenId?'#ffe391':'#ffffff';
    targetCtx.stroke();

    targetCtx.fillStyle='#ffffff';
    targetCtx.font='bold 14px system-ui';
    targetCtx.textAlign='center';
    targetCtx.textBaseline='middle';
    targetCtx.fillText(tk.short||tk.label.slice(0,3).toUpperCase(), tk.x, tk.y);

    targetCtx.font='bold 13px system-ui';
    const tw=targetCtx.measureText(tk.label).width+12;
    targetCtx.fillStyle='rgba(8,10,15,0.9)';
    targetCtx.fillRect(tk.x-tw/2, tk.y+rad+4, tw, 20);
    targetCtx.fillStyle='#ffe391';
    targetCtx.fillText(tk.label, tk.x, tk.y+rad+14);
    targetCtx.restore();
  }});

  const now=Date.now();
  pings=pings.filter(p=>now-p.start<2800);
  pings.forEach(p=>{{
    const elapsed=(now-p.start)/2800;
    const r1=12+elapsed*110;
    const r2=6+((elapsed*1.6)%1)*85;
    const alpha=1-elapsed;
    targetCtx.save();
    targetCtx.strokeStyle=`rgba(255,220,70,${{alpha}})`;
    targetCtx.lineWidth=5;
    targetCtx.beginPath();targetCtx.arc(p.x,p.y,r1,0,Math.PI*2);targetCtx.stroke();
    targetCtx.strokeStyle=`rgba(239,68,68,${{alpha}})`;
    targetCtx.lineWidth=4;
    targetCtx.beginPath();targetCtx.arc(p.x,p.y,r2,0,Math.PI*2);targetCtx.stroke();
    targetCtx.fillStyle=`rgba(255,235,150,${{alpha}})`;
    targetCtx.beginPath();targetCtx.arc(p.x,p.y,8,0,Math.PI*2);targetCtx.fill();
    targetCtx.restore();
  }});
  if(pings.length>0){{
    requestAnimationFrame(()=>{{renderTactical();queueLive();}});
  }}
}}

async function load(i){{
  persist();
  const n=++serial;
  current=i;ready=false;down=false;last=null;history=[];armed={{}};
  sendLive();
  const m=MAPS[i];
  for(const c of [base,fog,secret,tactical,playerBaseCanvas]){{c.width=m.w;c.height=m.h}}
  fill();
  $('zoom').value=1;zoom(false);
  $('viewport').scrollTo?.(0,0);
  try{{
    const a=await img(m.src);
    if(n!==serial)return;
    b.drawImage(a,0,0,m.w,m.h);

    // Load Player-Safe map (without area numbers/pins) if available
    if(m.playerSrc){{
      const pa=await img(m.playerSrc);
      if(n!==serial)return;
      pbCtx.drawImage(pa,0,0,m.w,m.h);
    }}else{{
      pbCtx.drawImage(a,0,0,m.w,m.h);
    }}

    const state=states[m.key];
    if(state){{
      for(const [ctx,key] of [[f,'fog'],[s,'secret']]){{
        if(!state[key])continue;
        const a=await img(state[key]);
        if(n!==serial)return;
        ctx.clearRect(0,0,m.w,m.h);
        ctx.globalCompositeOperation='source-over';
        ctx.drawImage(a,0,0,m.w,m.h);
      }}
    }}
    ready=true;
    zoom(false);
    renderTactical();
    queueLive();
    say(`${{m.title}} (${{m.w}}×${{m.h}})`);
  }}catch(e){{
    if(n===serial)say('Erro ao carregar mapa.');
  }}
}}

const MODES=['reveal','cover','lock','unlock','pan','pingMode','tokenDragMode'];
function setMode(m){{
  mode=m;last=null;rectStart=null;rectCurrent=null;
  for(const id of MODES)$(id).setAttribute('aria-pressed',String(id===m));
  $('stage').classList.toggle('pan',m==='pan');
  $('viewport').classList.toggle('pan-cursor',m==='pan');
}}
for(const id of MODES)$(id).onclick=()=>setMode(id);

function setShape(sh){{
  shape=sh;
  $('shapeBrush').setAttribute('aria-pressed',String(sh==='brush'));
  $('shapeRect').setAttribute('aria-pressed',String(sh==='rect'));
}}
$('shapeBrush').onclick=()=>setShape('brush');
$('shapeRect').onclick=()=>setShape('rect');

function point(e){{
  const r=fog.getBoundingClientRect();
  return{{x:(e.clientX-r.left)*fog.width/r.width,y:(e.clientY-r.top)*fog.height/r.height}};
}}

function paint(p){{
  const ctx=mode==='lock'||mode==='unlock'?s:f;
  ctx.globalCompositeOperation=mode==='reveal'||mode==='unlock'?'destination-out':'source-over';
  ctx.fillStyle=ctx.strokeStyle='#090d14';
  ctx.lineWidth=Number($('radius').value)*2;
  ctx.lineCap='round';
  if(last){{
    ctx.beginPath();ctx.moveTo(last.x,last.y);ctx.lineTo(p.x,p.y);ctx.stroke();
  }}
  ctx.beginPath();ctx.arc(p.x,p.y,Number($('radius').value),0,2*Math.PI);ctx.fill();
  last=p;
  queueLive();
}}

function applyRect(p1,p2){{
  const ctx=mode==='lock'||mode==='unlock'?s:f;
  ctx.globalCompositeOperation=mode==='reveal'||mode==='unlock'?'destination-out':'source-over';
  ctx.fillStyle='#090d14';
  const rx=Math.min(p1.x,p2.x), ry=Math.min(p1.y,p2.y);
  const rw=Math.abs(p2.x-p1.x), rh=Math.abs(p2.y-p1.y);
  ctx.fillRect(rx,ry,rw,rh);
  queueLive();
}}

fog.addEventListener('pointerdown',e=>{{
  if(!ready||mode==='pan'||$('app').classList.contains('player'))return;
  const p=point(e);

  if(mode==='pingMode'){{
    pings.push({{x:p.x,y:p.y,start:Date.now()}});
    renderTactical();
    queueLive();
    say('🎯 Ping enviado para o 2º Monitor!');
    return;
  }}

  if(mode==='tokenDragMode'){{
    const tokens=getMapTokens();
    const hit=[...tokens].reverse().find(tk=>Math.hypot(tk.x-p.x,tk.y-p.y)<=28);
    if(hit){{
      selectedTokenId=hit.id;
      if(e.button===2){{
        const action=prompt(`Editar nome de "${{hit.label}}" (ou digite EXCLUIR):`,hit.label);
        if(action&&action.toUpperCase()==='EXCLUIR'){{
          tacticalStates[MAPS[current].key]=tokens.filter(x=>x.id!==hit.id);
          selectedTokenId=null;
        }}else if(action){{
          hit.label=action;
          hit.short=action.slice(0,3).toUpperCase();
        }}
        saveTokens();
        return;
      }}
      draggingToken=hit;
      down=true;
      fog.setPointerCapture(e.pointerId);
      renderTactical();
    }}else{{
      selectedTokenId=null;
      renderTactical();
    }}
    return;
  }}

  snapshot();
  down=true;
  fog.setPointerCapture(e.pointerId);
  if(shape==='rect'){{
    rectStart=p;rectCurrent=p;
    renderTactical();
  }}else{{
    last=null;
    paint(p);
  }}
  e.preventDefault();
}});

fog.addEventListener('contextmenu',e=>{{if(mode==='tokenDragMode')e.preventDefault();}});

fog.addEventListener('pointermove',e=>{{
  if(!down)return;
  const p=point(e);
  if(mode==='tokenDragMode'&&draggingToken){{
    draggingToken.x=Math.max(15,Math.min(fog.width-15,p.x));
    draggingToken.y=Math.max(15,Math.min(fog.height-15,p.y));
    renderTactical();
    queueLive();
    return;
  }}
  if(shape==='rect'){{
    rectCurrent=p;
    renderTactical();
  }}else{{
    paint(p);
  }}
}});

function finish(){{
  if(!down)return;
  down=false;
  if(mode==='tokenDragMode'){{
    draggingToken=null;
    saveTokens();
    return;
  }}
  if(shape==='rect'&&rectStart&&rectCurrent){{
    applyRect(rectStart,rectCurrent);
    rectStart=null;rectCurrent=null;
    renderTactical();
  }}
  last=null;
  persist();
}}
for(const e of ['pointerup','pointercancel','lostpointercapture'])fog.addEventListener(e,finish);

function addToken(type,defaultLabel,color){{
  const tokens=getMapTokens();
  const count=tokens.filter(x=>x.type===type).length+1;
  const label=prompt('Nome público do token (visível aos jogadores):',`${{defaultLabel}} ${{count}}`);
  if(!label)return;
  const vp=getViewportNorm();
  const cx=Math.round((vp.x + vp.w/2)*fog.width);
  const cy=Math.round((vp.y + vp.h/2)*fog.height);
  const tk={{
    id:'tk_'+Date.now()+'_'+Math.random().toString(36).slice(2,6),
    type,
    label,
    short:label.slice(0,3).toUpperCase(),
    color,
    x:Math.max(30,Math.min(fog.width-30, cx + Math.round((Math.random()-0.5)*80))),
    y:Math.max(30,Math.min(fog.height-30, cy + Math.round((Math.random()-0.5)*80)))
  }};
  tokens.push(tk);
  selectedTokenId=tk.id;
  setMode('tokenDragMode');
  saveTokens();
}}

$('addPC').onclick=()=>addToken('pc','PJ','#2563eb');
$('addEnemy').onclick=()=>addToken('enemy','Inimigo','#dc2626');

$('toggleRings').onclick=()=>{{
  showRings=!showRings;
  $('toggleRings').setAttribute('aria-pressed',String(showRings));
  renderTactical();
  queueLive();
}};

$('clearTokens').onclick=()=>{{
  if(!confirm('Limpar tokens deste mapa?'))return;
  tacticalStates[MAPS[current].key]=[];
  selectedTokenId=null;
  saveTokens();
}};

$('map').onchange=()=>load(Number($('map').value));
$('radius').oninput=()=>$('radiusText').textContent=$('radius').value;
$('zoom').oninput=()=>zoom(true);

$('undo').onclick=async()=>{{
  if(!ready||!history.length)return;
  const n=serial,old=history.pop();
  ready=false;
  try{{
    for(const [ctx,key] of [[f,'fog'],[s,'secret']]){{
      const a=await img(old[key]);
      if(n!==serial)return;
      ctx.clearRect(0,0,fog.width,fog.height);
      ctx.globalCompositeOperation='source-over';
      ctx.drawImage(a,0,0);
    }}
    ready=true;persist();
  }}catch(e){{ready=true}}
}};

function confirmTwice(key,fn){{
  if(!ready)return;
  if(!armed[key]||Date.now()-armed[key]>4000){{
    armed[key]=Date.now();
    say('Clique novamente para confirmar.');
    return;
  }}
  snapshot();fn();persist();armed[key]=0;
}}
$('reset').onclick=()=>confirmTwice('reset',fill);
$('all').onclick=()=>confirmTwice('all',()=>f.clearRect(0,0,fog.width,fog.height));

function download(blob,name){{
  if(url)URL.revokeObjectURL(url);
  url=URL.createObjectURL(blob);
  const a=$('fallback');a.href=url;a.download=name;a.click();
}}

// Flattened image for Players: uses playerBaseCanvas (no DM markers) + tokens + opaque fog + opaque secret masks!
function flattened(){{
  const c=document.createElement('canvas');
  c.width=base.width;c.height=base.height;
  const q=c.getContext('2d');
  if(boostPlayerBrightness){{
    q.filter='brightness(1.18) contrast(1.08) saturate(1.08)';
  }}
  q.drawImage(playerBaseCanvas,0,0);
  q.filter='none';
  renderTactical(true, q);
  q.drawImage(fog,0,0);
  q.drawImage(secret,0,0);
  return c;
}}

$('export').onclick=()=>{{
  if(!ready)return;
  finish();persist();
  const key=MAPS[current].key,c=flattened();
  c.toBlob(blob=>{{if(blob)download(blob,'Barovia_'+key+'_jogadores.png')}},'image/png');
}};

$('save').onclick=()=>{{
  finish();persist();
  download(new Blob([JSON.stringify({{format:'barovia-real-v2',states,tacticalStates}})],{{type:'application/json'}}),'Barovia_mapas_progresso.json');
}};

$('restore').onchange=async e=>{{
  const file=e.target.files[0];if(!file)return;
  try{{
    const a=JSON.parse(await file.text());
    if(a.states)states=a.states;
    if(a.tacticalStates)tacticalStates=a.tacticalStates;
    await load(current);persist();
  }}catch(err){{}}
  e.target.value='';
}};

function sendLive(){{
  const frame={{
    type:'barovia-player-frame',
    token:liveToken,
    sequence:++liveSequence,
    viewport: syncViewportToPlayer ? getViewportNorm() : null
  }};
  if(ready){{
    frame.png=flattened().toDataURL('image/jpeg', 0.88);
    // Spoiler-free public title
    frame.title=MAPS[current].publicTitle || 'Baróvia';
    frame.key=MAPS[current].key;
    frame.w=base.width;
    frame.h=base.height;
  }}else frame.waiting=true;

  if(playerWindow&&!playerWindow.closed){{
    try{{playerWindow.postMessage(frame,'*')}}catch(e){{}}
  }}
  if(bc){{
    try{{bc.postMessage(frame)}}catch(e){{}}
  }}
}}

function queueLive(){{
  if(liveTimer!==null)return;
  liveTimer=setTimeout(()=>{{liveTimer=null;sendLive()}},80);
}}

$('live').onclick=()=>{{
  finish();
  if(playerWindow&&!playerWindow.closed){{playerWindow.focus();sendLive();return}}
  playerWindow=window.open('player.html','strahd-player-live','width=1366,height=840');
  setTimeout(()=>sendLive(), 500);
}};

if(bc){{
  bc.onmessage=e=>{{
    if(e.data?.type==='barovia-player-ready')sendLive();
  }};
}}

window.addEventListener('message',e=>{{
  if(e.data?.type==='barovia-player-ready')sendLive();
  if(e.data?.type==='barovia-select-map'){{
    const idx=MAPS.findIndex(m=>m.key===e.data.key);
    if(idx>=0){{$('map').value=idx;load(idx);}}
  }}
  if(e.data?.type==='barovia-select-scene'){{
    const sc=SCENES.find(s=>s.code===e.data.code);
    if(sc){{
      $('sceneSelect').value=sc.mapKey;
      const idx=MAPS.findIndex(m=>m.key===sc.mapKey);
      if(idx>=0){{$('map').value=idx;load(idx);}}
    }}
  }}
}});

$('view').onclick=()=>{{finish();$('app').classList.add('player');setMode('pan');}};
$('back').onclick=()=>{{$('app').classList.remove('player');setMode('reveal');}};

load(0);
</script>
</body>
</html>
"""

    for out_path in [ORIG_HTML_PATH, DOWNLOADS_HTML_PATH, WORKSPACE_HTML_PATH, VAULT_COCKPIT_MAP_PATH]:
        if out_path.parent.exists():
            out_path.write_text(html, encoding="utf-8")
            print(f"Wrote upgraded v3.5 map tool ({len(html) // 1024} KB) to {out_path}")


if __name__ == "__main__":
    build_upgraded_html()
