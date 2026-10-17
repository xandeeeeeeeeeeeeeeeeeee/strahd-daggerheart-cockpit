# -*- coding: utf-8 -*-
"""
Downloads and catalogs the best Strahd Reloaded maps and scene illustrations:
1. High-resolution maps from DragnaCarta, Eidolon-Publishing, and DungeonsLab
2. Scene illustrations and handouts for iconic moments (Death House exterior, Rose & Thorn, Durst Family, Walter, Strahd, NPCs, Locations)
3. Registers them in assets/maps and assets/illustrations
"""
import os
import urllib.request
import urllib.parse
from PIL import Image

WORKSPACE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAPS_DIR = os.path.join(WORKSPACE, "assets", "maps")
ILLUST_DIR = os.path.join(WORKSPACE, "assets", "illustrations")
os.makedirs(MAPS_DIR, exist_ok=True)
os.makedirs(ILLUST_DIR, exist_ok=True)

DRAGNA_BASE = "https://raw.githubusercontent.com/DragnaCarta/Curse-of-Strahd-Reloaded/main/"
EIDOLON_BASE = "https://raw.githubusercontent.com/Eidolon-Publishing/cosrl-escape-from-death-house/main/"
DUNGEONSLAB_BASE = "https://raw.githubusercontent.com/q-datum/dungeonslab-gothic-maps-pack/master/"

# Assets to download: (source_url, local_filename, target_dir)
DOWNLOAD_LIST = [
    # 1. Death House Exterior (JamesRPGArt High-Res)
    (
        "https://images.squarespace-cdn.com/content/v1/670447eeba89c103beabb9a5/3d3c91d0-de5e-4609-b49f-086c17db8fd7/Death+House.jpg?format=2500w",
        "Casa_da_Morte_Fachada_Exterior.jpg",
        ILLUST_DIR
    ),
    # 2. Death House Reloaded Official Tactical Maps (Eidolon Publishing / DragnaCarta)
    (
        EIDOLON_BASE + "assets/scene/death-house-reloaded-204-ppi.webp",
        "Casa_da_Morte_Mansao_Strahd_Reloaded.jpg",
        MAPS_DIR
    ),
    (
        EIDOLON_BASE + "assets/scene/death-house-basement-unlit-204-ppi.webp",
        "Casa_da_Morte_Porao_Culto_Strahd_Reloaded.jpg",
        MAPS_DIR
    ),
    # 3. Death House Floors (DungeonsLab Full-Color)
    (
        DUNGEONSLAB_BASE + "assets/tiles/death-house-1.webp",
        "Casa_da_Morte_Andar_1_Terreo.jpg",
        MAPS_DIR
    ),
    (
        DUNGEONSLAB_BASE + "assets/tiles/death-house-2.webp",
        "Casa_da_Morte_Andar_2_Biblioteca.jpg",
        MAPS_DIR
    ),
    (
        DUNGEONSLAB_BASE + "assets/tiles/death-house-3.webp",
        "Casa_da_Morte_Andar_3_Sotao.jpg",
        MAPS_DIR
    ),
    (
        DUNGEONSLAB_BASE + "assets/maps/death-house-dungeon.webp",
        "Casa_da_Morte_Masmorra_Catacumbas.jpg",
        MAPS_DIR
    ),
    # 4. Old Bonegrinder (DungeonsLab 5000x5000 Ultra Res)
    (
        DUNGEONSLAB_BASE + "assets/maps/old-bonegrinder.webp",
        "Velho_Esmaga_Ossos_HD.jpg",
        MAPS_DIR
    ),
    # 5. Barovia Church (DungeonsLab)
    (
        DUNGEONSLAB_BASE + "assets/maps/barovia-church.webp",
        "Igreja_Barovia_HD.jpg",
        MAPS_DIR
    ),
    # 6. Blue Water Inn (DungeonsLab)
    (
        DUNGEONSLAB_BASE + "assets/maps/blue-water-1.webp",
        "Estalagem_Agua_Azul_HD.jpg",
        MAPS_DIR
    ),
    # 7. Coffin Maker (DungeonsLab)
    (
        DUNGEONSLAB_BASE + "assets/maps/coffin-maker.webp",
        "Loja_Caixoes_HD.jpg",
        MAPS_DIR
    ),
    # 8. Wachterhaus (DungeonsLab)
    (
        DUNGEONSLAB_BASE + "assets/maps/wachrerhaus-1.webp",
        "Casa_Wachter_HD.jpg",
        MAPS_DIR
    ),
    # 9. Werewolf Den (DungeonsLab)
    (
        DUNGEONSLAB_BASE + "assets/maps/werewolf-den.webp",
        "Covil_Lobisomens_HD.jpg",
        MAPS_DIR
    ),
    # 10. Wizard of Wines Winery (DungeonsLab)
    (
        DUNGEONSLAB_BASE + "assets/maps/wizard-of-wines-winery.webp",
        "Vinicola_HD.jpg",
        MAPS_DIR
    ),
    # 11. Amber Temple (DungeonsLab)
    (
        DUNGEONSLAB_BASE + "assets/maps/amber-temple.webp",
        "Templo_Ambar_HD.jpg",
        MAPS_DIR
    ),
    # 12. Abbey of Saint Markovia (DungeonsLab)
    (
        DUNGEONSLAB_BASE + "assets/maps/abbey-of-saint-markovia.webp",
        "Abadia_Santa_Markovia_HD.jpg",
        MAPS_DIR
    ),
    # 13. Argynvostholt (DungeonsLab)
    (
        DUNGEONSLAB_BASE + "assets/maps/argynvosrholr.webp",
        "Argynvostholt_HD.jpg",
        MAPS_DIR
    ),
    # 14. Van Richten Tower (DungeonsLab)
    (
        DUNGEONSLAB_BASE + "assets/maps/richten-tower.webp",
        "Torre_Van_Richten_HD.jpg",
        MAPS_DIR
    ),
    # 15. Baba Lysaga's Hut / Berez (DungeonsLab & DragnaCarta)
    (
        DUNGEONSLAB_BASE + "assets/maps/baba-hug.webp",
        "Cabana_Baba_Lysaga_HD.jpg",
        MAPS_DIR
    ),
    (
        DRAGNA_BASE + "images/Berez_Dungeon.png",
        "Berez_Masmorra_Subterranea.jpg",
        MAPS_DIR
    ),
    # 16. DragnaCarta 4K Tactical Maps
    (
        DRAGNA_BASE + "images/Town-Square_4k_NoGrid_30x20_136PPI_Gloom_Fog.jpg",
        "Vallaki_Praca_4K_Strahd_Reloaded.jpg",
        MAPS_DIR
    ),
    (
        DRAGNA_BASE + "images/The-Twin-Falls_4k_NoGrid_40x50_82PPI_Frozen_Snow.jpg",
        "Tser_Falls_4K_Strahd_Reloaded.jpg",
        MAPS_DIR
    ),
    (
        DRAGNA_BASE + "images/Lake-Zarovich_Izek-Encounter_4k_NoGrid_40x30_102PPI_Gloom_Fog.jpg",
        "Lago_Zarovich_4K_Strahd_Reloaded.jpg",
        MAPS_DIR
    ),
    (
        DRAGNA_BASE + "images/Bodak_Lair_4k_NoGrid_60x40_68PPI_Gloom.png",
        "Monte_Ghakis_Covil_Bodak_4K.jpg",
        MAPS_DIR
    ),
    (
        DRAGNA_BASE + "images/The_Shrine_of_the_Rozana.jpg",
        "Santuario_Rozana_4K.jpg",
        MAPS_DIR
    ),
    (
        DRAGNA_BASE + "images/Eastern-Barricades.jpg",
        "Barricadas_Orientais_Barovia_HD.jpg",
        MAPS_DIR
    ),

    # 17. SCENE ILLUSTRATIONS & HANDOUTS (DragnaCarta & Eidolon)
    (
        EIDOLON_BASE + "assets/actors/walter_the_mound.webp",
        "Walter_O_Monte_Rastejante.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Rose and Thorn.png"),
        "Rose_e_Thorn_Durst.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/The Durst Family.png"),
        "Quadro_Familia_Durst.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Durst Invitation.jpg"),
        "Carta_Convite_Gustav_Durst.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Strahd at Dinner.png"),
        "Strahd_no_Jantar_Ravenloft.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Strahd and Beucephalus.png"),
        "Strahd_e_Beucephalus.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Fledgling_Strahd.png"),
        "Conde_Strahd_von_Zarovich.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Ireena.png"),
        "Ireena_Kolyana.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Ismark the Great.png"),
        "Ismark_Kolyanovich.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Father Lucian Petrovich.png"),
        "Padre_Lucian_Petrovich.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Doru.jpg"),
        "Doru_Vampiro_Igreja.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Dorus_Notes.png"),
        "Diario_de_Doru.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/The Bonegrinder Coven.png"),
        "Conluio_Bruxas_Esmaga_Ossos.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Morgantha.png"),
        "Morgantha_Bruxa_Torta.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Lady Fiona Wachter.png"),
        "Lady_Fiona_Wachter.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Stella Wachter.png"),
        "Stella_Wachter.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Victor Vallakovich.png"),
        "Victor_Vallakovich.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Izek Strazni.png"),
        "Izek_Strazni_Braco_Demoniaco.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Vallaki_Martikovs.png"),
        "Familia_Martikov_Agua_Azul.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Rictavio.png"),
        "Rictavio_Bardo_Circo.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/The Abbot.png"),
        "O_Abade_Celestial.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Vasilka.png"),
        "Vasilka_Criacao_do_Abade.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Vladimir Horngaard.png"),
        "Vladimir_Horngaard_Revenante.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Kasimir Velikov 1.png"),
        "Kasimir_Velikov_Elfo_do_Crepusculo.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Arabelle.png"),
        "Arabelle_Vistana_do_Lago.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Zuleika Toranscu.png"),
        "Zuleika_Lobisomem.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/The_Roc_of_Mt._Ghakis_night_hires.jpg"),
        "O_Roc_do_Monte_Ghakis.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Jamboree_Poster_Distressed.png"),
        "Cartaz_Festival_Sol_Incandescente.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Carnival Poster.png"),
        "Cartaz_Carnaval_Maravilhas_Rictavio.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Ancient Oak.jpg"),
        "Carvalho_Ancestral_Svalich.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/The Frozen Lake.png"),
        "O_Lago_Congelado_de_Baratok.jpg",
        ILLUST_DIR
    ),
    (
        DRAGNA_BASE + urllib.parse.quote("images/Marina's Monument.png"),
        "Monumento_de_Marina_Berez.jpg",
        ILLUST_DIR
    )
]

def main():
    print(f"Starting download of {len(DOWNLOAD_LIST)} items...")
    success = 0
    for url, filename, target_dir in DOWNLOAD_LIST:
        dest_path = os.path.join(target_dir, filename)
        temp_dest = dest_path + ".tmp"
        try:
            print(f"Fetching: {filename}...")
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as resp, open(temp_dest, "wb") as f:
                f.write(resp.read())
            
            # Convert / recompress to JPEG if needed (keeping max 3200px width/height for fast mobile/web performance)
            with Image.open(temp_dest) as im:
                im = im.convert("RGB")
                max_dim = 3200
                if im.width > max_dim or im.height > max_dim:
                    im.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
                im.save(dest_path, "JPEG", quality=88, optimize=True)
            
            if os.path.exists(temp_dest):
                os.remove(temp_dest)
            
            size_kb = os.path.getsize(dest_path) / 1024
            print(f"Saved: {filename} ({size_kb:.1f} KB)")
            success += 1
        except Exception as e:
            print(f"ERROR downloading {filename} from {url}: {e}")
            if os.path.exists(temp_dest):
                os.remove(temp_dest)

    print(f"\nCompleted: {success}/{len(DOWNLOAD_LIST)} downloaded successfully.")

if __name__ == "__main__":
    main()
