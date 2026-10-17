# -*- coding: utf-8 -*-
import json
import base64
import io
from PIL import Image

print("Updating mapas.html...")

# 1. Encode Fachada image
with Image.open("assets/maps/Casa_da_Morte_Fachada_Exterior.jpg") as im:
    im = im.convert("RGB")
    if im.width > 2200 or im.height > 2200:
        im.thumbnail((2200, 2200), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=82, optimize=True)
    b64 = base64.b64encode(buf.getvalue()).decode("ascii")
    w, h = im.size

fachada_entry = {
    "key": "reloaded_cdm_fachada",
    "title": "★ Casa da Morte · Fachada Exterior & Rua nas Brumas",
    "publicTitle": "Casa da Morte · Fachada Exterior & Rua nas Brumas",
    "src": f"data:image/jpeg;base64,{b64}",
    "w": w,
    "h": h,
    "category": "Strahd Reloaded · Tático",
    "arcs": ["A"]
}

# 2. Read mapas.html
with open("mapas.html", "r", encoding="utf-8") as f:
    text = f.read()

m_idx = text.find("const MAPS=[")
s_idx = text.find("const SCENES=[")
m_end = text.find("];\nconst SCENES=[", m_idx)
s_end = text.find("];\n", s_idx)

maps_list = json.loads(text[m_idx + len("const MAPS=") : m_end + 1])
scenes_list = json.loads(text[s_idx + len("const SCENES=") : s_end + 1])

# 3. Add or update fachada_entry in maps_list
existing_map_idx = next((i for i, m in enumerate(maps_list) if m["key"] == "reloaded_cdm_fachada"), None)
if existing_map_idx is not None:
    maps_list[existing_map_idx] = fachada_entry
else:
    maps_list.append(fachada_entry)

# 4. Update scenes_list for A2 and A2a
for sc in scenes_list:
    if sc["code"] == "A2":
        sc["mapKey"] = "reloaded_cdm_fachada"
        sc["mapName"] = "Casa da Morte · Fachada Exterior & Rua nas Brumas"
    elif sc["code"] == "A2a":
        sc["mapKey"] = "real_27"
        sc["mapName"] = "Casa da Morte · Mansão dos Durst (Strahd Reloaded)"

new_maps_json = json.dumps(maps_list, ensure_ascii=False)
new_scenes_json = json.dumps(scenes_list, ensure_ascii=False)

updated_html = (
    text[:m_idx + len("const MAPS=")]
    + new_maps_json
    + ";\nconst SCENES="
    + new_scenes_json
    + text[s_end + 1:]
)

with open("mapas.html", "w", encoding="utf-8") as f:
    f.write(updated_html)

print(f"mapas.html updated successfully! Total maps: {len(maps_list)}, scenes: {len(scenes_list)}.")
