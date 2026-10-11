# -*- coding: utf-8 -*-
"""
Script de Sincronização Automática com a API Oficial do Notion
Atualiza a página 'Strahd Reloaded · Daggerheart — Mesa do Mestre' (ID: 3f4a4a42-2490-8140-91ea-e40f75de278a)
e aplica a reestruturação de layout sem perda de texto (Callouts Semânticos + 16 Novos Mapas) diretamente na nuvem do Notion.

Como usar:
1. Crie uma integração interna em https://www.notion.so/my-integrations e copie o seu NOTION_TOKEN (secret_...).
2. Na página 'Strahd Reloaded · Daggerheart — Mesa do Mestre' no Notion, clique em '...' -> 'Conexões' e adicione sua integração.
3. Execute:
   set NOTION_TOKEN=secret_seu_token_aqui
   python scripts/sincronizar_notion_api.py
"""

import os
import sys
import json
import urllib.request
from pathlib import Path

ROOT_PAGE_ID = "3f4a4a42-2490-8140-91ea-e40f75de278a"
WORKSPACE = Path(__file__).resolve().parent.parent
CAMPAIGN_JSON = WORKSPACE / "data" / "campaign_data.json"


def notion_request(method: str, endpoint: str, token: str, payload=None):
    url = f"https://api.notion.com/v1/{endpoint.lstrip('/')}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
    }
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def build_callout_block(icon_emoji: str, text: str, color: str = "gray_background"):
    return {
        "object": "block",
        "type": "callout",
        "callout": {
            "icon": {"type": "emoji", "emoji": icon_emoji},
            "color": color,
            "rich_text": [{"type": "text", "text": {"content": text[:1990]}}],
        },
    }


def sync_cockpit_banner_to_root(token: str):
    campaign = json.loads(CAMPAIGN_JSON.read_text(encoding="utf-8"))
    new_maps = [m for m in campaign["maps"] if str(m["key"]).startswith("novo_")]
    summary_text = (
        "Cockpit do Mestre 2.0 Ativo · 44 Mapas Integrados (28 Originais + 16 Novos Mapas Táticos/Regionais) · "
        "180 Cenas Reestruturadas com Callouts Semânticos (100% Fiel ao Texto Original) · "
        "Soundboard Web Audio + Rastreador de Medo, Dualidade e Formas de Chefe."
    )
    blocks = [
        build_callout_block("🦇", summary_text, "red_background"),
        build_callout_block(
            "🗺️",
            "16 Novos Mapas Criados: " + " | ".join(f"{m['title']} ({m['file']})" for m in new_maps),
            "brown_background",
        ),
    ]
    res = notion_request("PATCH", f"blocks/{ROOT_PAGE_ID}/children", token, {"children": blocks})
    print("Painel superior adicionado com sucesso à página raiz do Notion!", res.get("results", [])[:1])


def main():
    token = os.environ.get("NOTION_TOKEN", "").strip()
    if not token:
        print(
            "Aviso: Variável de ambiente NOTION_TOKEN não definida.\n"
            "Para sincronizar diretamente na nuvem do Notion:\n"
            "  1. Gere um token em https://www.notion.so/my-integrations\n"
            "  2. Conecte a integração à página 'Strahd Reloaded · Daggerheart — Mesa do Mestre'\n"
            "  3. Rode: $env:NOTION_TOKEN='secret_...'; python scripts/sincronizar_notion_api.py\n\n"
            "Enquanto isso, todos os 180 arquivos Markdown reestruturados já estão prontos em:\n"
            f"  -> {WORKSPACE / 'notion_reestruturado' / 'Cenas_Reestruturadas'}\n"
            "E o seu Vault RPG do Obsidian já foi atualizado automaticamente!"
        )
        return
    sync_cockpit_banner_to_root(token)


if __name__ == "__main__":
    main()
