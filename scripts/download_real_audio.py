import os
import urllib.request
import urllib.parse
import shutil

AUDIO_DIR = r"c:\Users\Alex\Documents\antigravity\beautiful-bohr\assets\audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

SDND_BASE = "https://raw.githubusercontent.com/matthewbstroud/sdnd-strahd-adv/main/"
DPRO_BASE = "https://raw.githubusercontent.com/dprothero/strahd-soundboard/main/"

TRACKS = [
    # Ambient Loops (10)
    ("amb_rain_storm.mp3", SDND_BASE + "images/maps/Areas/K/k46_parapets/rain-with-distant-thunder.mp3"),
    ("amb_wind_howl.mp3", SDND_BASE + "images/maps/Areas/K/k01_courtyard_f/howling-wind.mp3"),
    ("amb_night_woods.mp3", SDND_BASE + "images/maps/Areas/P/night-woods.mp3"),
    ("amb_tavern.mp3", SDND_BASE + "images/maps/Areas/E/e2_blood_vine/tavern_ambience.mp3"),
    ("amb_fireplace.mp3", SDND_BASE + "sfx/environment/fireplace_burning.mp3"),
    ("amb_crypt_drip.mp3", SDND_BASE + "images/maps/Areas/K/k31b_elevator_shaft_access/wind-basement-dripping-water.mp3"),
    ("amb_whispers.mp3", SDND_BASE + "sfx/four_voices_whispering_2_wecho-6755.mp3"),
    ("amb_medieval_town.mp3", SDND_BASE + "sfx/ambient/56_Medieval_Town.mp3"),
    ("amb_river_swamp.mp3", SDND_BASE + "sfx/environment/River.mp3"),
    ("amb_carriage.mp3", DPRO_BASE + "mp3/carriage.mp3"),

    # Music / Score Loops (12)
    ("mus_strahd_organ.mp3", SDND_BASE + "images/maps/Areas/K/k10_dining/strahd_organ.mp3"),
    ("mus_exploration.mp3", DPRO_BASE + "mp3/exploration_music.mp3"),
    ("mus_battle.mp3", DPRO_BASE + "mp3/battle_music.mp3"),
    ("mus_vistani_camp.mp3", SDND_BASE + "images/maps/Areas/N/n9_vistani_camp/vistani-camp.mp3"),
    ("mus_mystery.mp3", SDND_BASE + "images/maps/Areas/K/k11_south_archer_post/mystery-music-loop.mp3"),
    ("mus_horror_suspense.mp3", SDND_BASE + "images/maps/Areas/K/k76_torture/horror-background-atmosphere-for-suspenseful-moments.mp3"),
    ("mus_choir_chapel.mp3", SDND_BASE + "images/maps/Areas/K/k71_kingsmen_quarters/spooky-singing-choir.mp3"),
    ("mus_druid_chant.mp3", SDND_BASE + "images/maps/Areas/Y/y3_druid_circle/druid_chant.mp3"),
    ("mus_amber_prelude.mp3", SDND_BASE + "images/maps/Areas/K/k38_false_treasury/eerie-prelude.mp3"),
    ("mus_sad_piano.mp3", SDND_BASE + "images/maps/Areas/K/k51_closet/creepy_piano.mp3"),
    ("mus_tavern_lute.mp3", SDND_BASE + "sfx/medieval-music.mp3"),
    ("mus_witches_dance.mp3", SDND_BASE + "images/maps/Areas/K/k56_cauldron/witches-dance.mp3"),

    # SFX / One-Shots (16)
    ("sfx_wolves_howl.mp3", SDND_BASE + "images/maps/Areas/Q/wolves-howling.mp3"),
    ("sfx_thunder_strike.mp3", SDND_BASE + "images/maps/Areas/K/k45_heroes/big-thunder.mp3"),
    ("sfx_ravens_flock.mp3", SDND_BASE + "images/maps/Areas/O/flock-of-crows-ravens-cawing.mp3"),
    ("sfx_heavy_gate.mp3", SDND_BASE + "images/maps/Areas/B/gate_heavy_openclose.mp3"),
    ("sfx_strahd_laugh.mp3", SDND_BASE + "images/maps/Areas/K/k27_king_hall/laugh evil.mp3"),
    ("sfx_hag_laugh.mp3", SDND_BASE + "images/maps/Areas/O/witch-laughing-104760.mp3"),
    ("sfx_church_bell.mp3", SDND_BASE + "images/maps/Areas/K/k40_belfry/gong.mp3"),
    ("sfx_heartbeat.mp3", SDND_BASE + "sfx/heartbeat-sound-effect-111218.mp3"),
    ("sfx_ghost_scream.mp3", SDND_BASE + "images/maps/Areas/X/x1_amber_temple/ghost_screams.mp3"),
    ("sfx_war_horn.mp3", SDND_BASE + "images/maps/Areas/Q/war_horn.mp3"),
    ("sfx_trap_snap.mp3", SDND_BASE + "sfx/TrapSnap.mp3"),
    ("sfx_chains_door.mp3", SDND_BASE + "sfx/metal-warehouse-door-opened-with-chains-100823.mp3"),
    ("sfx_fireball.mp3", SDND_BASE + "images/maps/Areas/K/k21_tower_s/fireball.mp3"),
    ("sfx_bats_swarm.mp3", SDND_BASE + "images/maps/Areas/K/k60a_tower_peak_n_roof/bats.mp3"),
    ("sfx_werewolf_roar.mp3", SDND_BASE + "images/maps/Areas/Z/z6_kiril_cave/wolf-scary-growl-roar.mp3"),
    ("sfx_horror_sting.mp3", SDND_BASE + "images/maps/Areas/K/k23_servant_entrance/evil-cue.mp3"),
]

def encode_url(u):
    parts = urllib.parse.urlsplit(u)
    path = urllib.parse.quote(parts.path)
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.fragment))

ok = 0
for fname, raw_url in TRACKS:
    dest = os.path.join(AUDIO_DIR, fname)
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        print(f"[SKIP] {fname} ({os.path.getsize(dest)//1024} KB)")
        ok += 1
        continue
    url = encode_url(raw_url)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
            shutil.copyfileobj(r, f)
        sz = os.path.getsize(dest) // 1024
        print(f"[OK]   {fname} ({sz} KB)")
        ok += 1
    except Exception as e:
        print(f"[FAIL] {fname}: {e}")

print(f"\nDownloaded {ok}/{len(TRACKS)} audio tracks.")
