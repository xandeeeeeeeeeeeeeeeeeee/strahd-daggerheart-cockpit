// ============================================================================
// BARÓVIA ATMOSPHERIC SOUNDBOARD & MIXER v3.0 (Real MP3 Audio + 180 Scenes)
// 46 Real Curse of Strahd Audio Tracks + Tailored Soundscapes for All 180 Scenes
// ============================================================================

class BaroviaSoundEngine {
  constructor() {
    this.ctx = null;
    this.masterGain = null;
    this.masterVolume = 0.75;
    this.activeLoops = new Map(); // id -> { type: 'file'|'synth', audio?, volume, ... }
    this.customFiles = new Map(); // id -> HTMLAudioElement
    this.preloadedFiles = new Map(); // id -> src path
    this.activePreset = null;
    this.autoPlayOnSceneChange = false;

    // 14 Real Ambient Loops (can be mixed simultaneously)
    this.ambientChannels = [
      { id: 'rain', icon: '🌧️', name: 'Chuva & Trovoada Distante', file: 'assets/audio/amb_rain_storm.mp3', defaultVol: 0.55 },
      { id: 'wind', icon: '🌫️', name: 'Vento Uivante das Brumas', file: 'assets/audio/amb_wind_howl.mp3', defaultVol: 0.50 },
      { id: 'night', icon: '🌲', name: 'Floresta de Svalich à Noite', file: 'assets/audio/amb_night_woods.mp3', defaultVol: 0.50 },
      { id: 'tavern', icon: '🍺', name: 'Taverna Movimentada', file: 'assets/audio/amb_tavern.mp3', defaultVol: 0.50 },
      { id: 'fire', icon: '🔥', name: 'Lareira / Fogueira Vistani', file: 'assets/audio/amb_fireplace.mp3', defaultVol: 0.50 },
      { id: 'dungeon', icon: '⛓️', name: 'Masmorra Úmida & Goteiras', file: 'assets/audio/amb_crypt_drip.mp3', defaultVol: 0.55 },
      { id: 'whispers', icon: '🕯️', name: 'Sussurros nas Sombras', file: 'assets/audio/amb_whispers.mp3', defaultVol: 0.45 },
      { id: 'town', icon: '🏘️', name: 'Ruas da Vila / Vallaki', file: 'assets/audio/amb_medieval_town.mp3', defaultVol: 0.45 },
      { id: 'river', icon: '🌊', name: 'Rio Ivlis / Pântano de Berez', file: 'assets/audio/amb_river_swamp.mp3', defaultVol: 0.50 },
      { id: 'carriage', icon: '🐎', name: 'Carruagem Negra na Estrada', file: 'assets/audio/amb_carriage.mp3', defaultVol: 0.50 },
      { id: 'grindstone', icon: '⚙️', name: 'Engrenagens do Moinho', file: 'assets/audio/amb_grindstone.mp3', defaultVol: 0.50 },
      { id: 'trees', icon: '🌳', name: 'Árvore de Gulthias', file: 'assets/audio/amb_whispering_trees.mp3', defaultVol: 0.50 },
      { id: 'cauldron', icon: '🧪', name: 'Caldeirão Borbulhante', file: 'assets/audio/amb_cauldron.mp3', defaultVol: 0.50 },
      { id: 'blizzard', icon: '❄️', name: 'Nevasca do Monte Ghakis', file: 'assets/audio/amb_wind_howl.mp3', defaultVol: 0.65 }
    ];

    // 14 Real Music & Dramatic Score Loops
    this.musicChannels = [
      { id: 'organ', icon: '🎹', name: 'Órgão de Strahd (Ravenloft)', file: 'assets/audio/mus_strahd_organ.mp3', defaultVol: 0.55 },
      { id: 'exploration', icon: '🧭', name: 'Exploração Sombria do Vale', file: 'assets/audio/mus_exploration.mp3', defaultVol: 0.45 },
      { id: 'combat', icon: '⚔️', name: 'Combate Mortal / Cerco', file: 'assets/audio/mus_battle.mp3', defaultVol: 0.55 },
      { id: 'vistani', icon: '🎻', name: 'Acampamento Vistani (Tser Pool)', file: 'assets/audio/mus_vistani_camp.mp3', defaultVol: 0.55 },
      { id: 'mystery', icon: '🔍', name: 'Investigação & Mistério', file: 'assets/audio/mus_mystery.mp3', defaultVol: 0.45 },
      { id: 'horror', icon: '💀', name: 'Terror & Suspense Profundo', file: 'assets/audio/mus_horror_suspense.mp3', defaultVol: 0.50 },
      { id: 'choir', icon: '⛪', name: 'Coro Sagrado (Igreja / Capela)', file: 'assets/audio/mus_choir_chapel.mp3', defaultVol: 0.50 },
      { id: 'monks', icon: '🙏', name: 'Cântico Monástico (Abadia)', file: 'assets/audio/mus_monk_chants.mp3', defaultVol: 0.50 },
      { id: 'druid', icon: '🩸', name: 'Ritual Druídico (Colina Yester)', file: 'assets/audio/mus_druid_chant.mp3', defaultVol: 0.55 },
      { id: 'amber', icon: '🔮', name: 'Prelúdio do Templo de Âmbar', file: 'assets/audio/mus_amber_prelude.mp3', defaultVol: 0.55 },
      { id: 'piano', icon: '🥀', name: 'Piano Melancólico & Luto', file: 'assets/audio/mus_sad_piano.mp3', defaultVol: 0.50 },
      { id: 'lute', icon: '🪕', name: 'Alaúde de Estalagem', file: 'assets/audio/mus_tavern_lute.mp3', defaultVol: 0.45 },
      { id: 'witches', icon: '🧙‍♀️', name: 'Dança das Bruxas (Megeras)', file: 'assets/audio/mus_witches_dance.mp3', defaultVol: 0.50 },
      { id: 'dread', icon: '👑', name: 'Presença do Senhor da Noite', file: 'assets/audio/mus_creepy_tension.mp3', defaultVol: 0.50 }
    ];

    // 28 Real SFX Pads (One-Shot Effects)
    this.sfxPads = [
      { id: 'thunder', icon: '⚡', name: 'Trovão Violento', file: 'assets/audio/sfx_thunder_strike.mp3' },
      { id: 'wolf', icon: '🐺', name: 'Uivo da Alcateia', file: 'assets/audio/sfx_wolves_howl.mp3' },
      { id: 'wolf_growl', icon: '🐺', name: 'Rosnado Ameaçador', file: 'assets/audio/sfx_wolf_growl.mp3' },
      { id: 'ravens', icon: '🐦‍⬛', name: 'Revoada de Corvos', file: 'assets/audio/sfx_ravens_flock.mp3' },
      { id: 'door', icon: '🚪', name: 'Portão Pesado', file: 'assets/audio/sfx_heavy_gate.mp3' },
      { id: 'iron_door', icon: '🗝️', name: 'Porta de Ferro', file: 'assets/audio/sfx_iron_door.mp3' },
      { id: 'trapdoor', icon: '🪜', name: 'Alçapão Abrindo', file: 'assets/audio/sfx_trapdoor.mp3' },
      { id: 'wood_creek', icon: '🪵', name: 'Madeira Rangendo', file: 'assets/audio/sfx_wood_creek.mp3' },
      { id: 'stone_scrape', icon: '🪨', name: 'Arrastar de Pedra', file: 'assets/audio/sfx_stone_scrape.mp3' },
      { id: 'glass_break', icon: '🪟', name: 'Vidro Quebrando', file: 'assets/audio/sfx_glass_break.mp3' },
      { id: 'sword_swing', icon: '⚔️', name: 'Golpe de Lâmina', file: 'assets/audio/sfx_sword_swing.mp3' },
      { id: 'strahd_laugh', icon: '🧛', name: 'Risada de Strahd', file: 'assets/audio/sfx_strahd_laugh.mp3' },
      { id: 'hag_laugh', icon: '🧙‍♀️', name: 'Risada de Bruxa', file: 'assets/audio/sfx_hag_laugh.mp3' },
      { id: 'bell', icon: '🔔', name: 'Sino / Gongo Fúnebre', file: 'assets/audio/sfx_church_bell.mp3' },
      { id: 'heartbeat', icon: '💓', name: 'Batimento Cardíaco', file: 'assets/audio/sfx_heartbeat.mp3' },
      { id: 'scared_breath', icon: '😮‍💨', name: 'Respiração Ofegante', file: 'assets/audio/sfx_scared_breath.mp3' },
      { id: 'scream', icon: '👻', name: 'Grito Espectral', file: 'assets/audio/sfx_ghost_scream.mp3' },
      { id: 'zombie', icon: '🧟', name: 'Horda de Zumbis', file: 'assets/audio/sfx_zombie_scream.mp3' },
      { id: 'werewolf', icon: '🐾', name: 'Rugido Lobisomem', file: 'assets/audio/sfx_werewolf_roar.mp3' },
      { id: 'horn', icon: '📯', name: 'Trombeta de Alarme', file: 'assets/audio/sfx_war_horn.mp3' },
      { id: 'trap', icon: '🪤', name: 'Armadilha Disparando', file: 'assets/audio/sfx_trap_snap.mp3' },
      { id: 'chains', icon: '⛓️', name: 'Correntes & Grades', file: 'assets/audio/sfx_chains_door.mp3' },
      { id: 'fireball', icon: '🔥', name: 'Explosão de Fogo', file: 'assets/audio/sfx_fireball.mp3' },
      { id: 'flame_burst', icon: '🔥', name: 'Labareda Súbita', file: 'assets/audio/sfx_flame_burst.mp3' },
      { id: 'avalanche', icon: '🏔️', name: 'Avalanche / Desmoronamento', file: 'assets/audio/sfx_avalanche.mp3' },
      { id: 'bats', icon: '🦇', name: 'Enxame de Morcegos', file: 'assets/audio/sfx_bats_swarm.mp3' },
      { id: 'horror_impact', icon: '💥', name: 'Impacto Macabro', file: 'assets/audio/sfx_horror_impact.mp3' },
      { id: 'sting', icon: '💀', name: 'Acorde de Terror', file: 'assets/audio/sfx_horror_sting.mp3' }
    ];

    // 25 Curated YouTube Masterpieces (Travis Savoie, Michael Ghelfi Studios, Bard's Legacy)
    this.youtubeTracks = [
      {
        id: 'yt_into_mists',
        title: 'Into the Mists (Main Theme)',
        author: 'Travis Savoie',
        category: 'explore',
        categoryLabel: '🗺️ Exploração & Névoas',
        ytId: 'CpTzAPnO1_8',
        desc: 'Trilha orquestral épica para a chegada em Baróvia, travessia dos portões e viagem pelas estradas.',
        scenes: ['A1', 'C1', 'C2', 'C3', 'C5', 'L1']
      },
      {
        id: 'yt_he_is_ancient',
        title: 'I Am The Ancient, I Am The Land',
        author: 'Travis Savoie',
        category: 'strahd',
        categoryLabel: '👑 Strahd & Ravenloft',
        ytId: 'Za2DU-ijcqc',
        desc: 'O tema definitivo do Lorde de Baróvia. Ideal para aparições triunfantes e o clímax final da campanha.',
        scenes: ['U1', 'U2', 'U3', 'U4', 'U5', 'U6', 'C7', 'C8']
      },
      {
        id: 'yt_haunted_mansion',
        title: 'Haunted Mansion (1h Ambience)',
        author: 'Michael Ghelfi Studios',
        category: 'ambient',
        categoryLabel: '🕯️ Ambientes & Terror',
        ytId: 'oef3XIRUeII',
        desc: 'Ambiente soturno de mansão assombrada perfeito para toda a Casa da Morte (Durst Manor).',
        scenes: ['A2', 'A2a', 'A2b', 'A2c', 'A2d', 'A2e', 'A2f']
      },
      {
        id: 'yt_castle_ravenloft',
        title: 'Castle Ravenloft',
        author: 'Travis Savoie',
        category: 'strahd',
        categoryLabel: '👑 Strahd & Ravenloft',
        ytId: '-_CXNbSkYAA',
        desc: 'Tema gótico orquestrado para a aproximação e entrada na fortaleza ancestral de Ravenloft.',
        scenes: ['P1', 'P2', 'P3', 'P4']
      },
      {
        id: 'yt_castle_reworked',
        title: 'Castle Ravenloft (Incursão & Catacumbas)',
        author: 'Travis Savoie',
        category: 'strahd',
        categoryLabel: '👑 Strahd & Ravenloft',
        ytId: 'Xe42Pv_SDA0',
        desc: 'Trilha tensa e sinistra para a exploração profunda das torres, criptas e catacumbas do castelo.',
        scenes: ['P5', 'P6', 'P7', 'P8']
      },
      {
        id: 'yt_vampire_lair',
        title: 'Vampire Lair (Gothic Dark Ambience)',
        author: "Bard's Legacy",
        category: 'ambient',
        categoryLabel: '🕯️ Ambientes & Terror',
        ytId: 'w9__x5MvilQ',
        desc: 'Atmosfera macabra e imersiva para masmorras de vampiros, sepulcros e catacumbas.',
        scenes: ['A2f', 'P6', 'P7']
      },
      {
        id: 'yt_barovian_legends',
        title: 'Barovian Legends (Town Theme)',
        author: 'Travis Savoie',
        category: 'explore',
        categoryLabel: '🗺️ Exploração & Névoas',
        ytId: 'K_j5L7zmA9s',
        desc: 'Melodia melancólica que captura a tristeza e desesperança dos aldeões de Baróvia e Vallaki.',
        scenes: ['B1', 'B2', 'B3', 'B4', 'B5', 'D1', 'D2', 'D3', 'D4', 'D5']
      },
      {
        id: 'yt_quiet_tavern',
        title: 'Quiet Tavern / Innkeeper ASMR (1h Ambience)',
        author: 'Michael Ghelfi Studios',
        category: 'ambient',
        categoryLabel: '🕯️ Ambientes & Terror',
        ytId: 'b1DUhonNQXM',
        desc: 'Ambiente caloroso de estalagem com lareira, canecas e murmúrios na Taverna Sangue na Vinha ou Água Azul.',
        scenes: ['B5c', 'F1', 'F2', 'F3', 'A1']
      },
      {
        id: 'yt_waltzing_shadows',
        title: 'Waltzing Shadows (O Jantar de Strahd)',
        author: 'Travis Savoie',
        category: 'story',
        categoryLabel: '🥀 História & NPCs',
        ytId: 'lBRHq-Ym_pQ',
        desc: 'Valsa macabra e aristocrática para o célebre banquete oferecido pelo Conde em Ravenloft.',
        scenes: ['O1', 'O2', 'O3', 'O4', 'O5', 'O6']
      },
      {
        id: 'yt_ireena_theme',
        title: "A Coveted Soul (Ireena's Theme)",
        author: 'Travis Savoie',
        category: 'story',
        categoryLabel: '🥀 História & NPCs',
        ytId: 'HbJf4z95eKg',
        desc: 'Composição tocante e trágica dedicada à reencarnação de Tatyana e sua fuga do destino.',
        scenes: ['B5a', 'B5b', 'B6', 'C6', 'K4']
      },
      {
        id: 'yt_ezmerelda_theme',
        title: "All Against Darkness (Ezmerelda's Theme)",
        author: 'Travis Savoie',
        category: 'story',
        categoryLabel: '🥀 História & NPCs',
        ytId: 'MDsICwz_noI',
        desc: 'Trilha corajosa e determinada para as aparições de Ezmerelda d’Avenir e Rudolph van Richten.',
        scenes: ['K5', 'M5', 'R2']
      },
      {
        id: 'yt_dream_pastries',
        title: 'Dream Pastries (Old Bonegrinder Coven)',
        author: 'Travis Savoie',
        category: 'combat',
        categoryLabel: '⚔️ Combate & Tensão',
        ytId: 'Qpc8BVTsTpc',
        desc: 'Música perturbadora para o confronto mortal contra Morgantha e suas filhas no moinho.',
        scenes: ['C9', 'H7']
      },
      {
        id: 'yt_wolves_dance',
        title: 'Dancing With the Wolves',
        author: 'Travis Savoie',
        category: 'combat',
        categoryLabel: '⚔️ Combate & Tensão',
        ytId: 'mX-rasUTpQo',
        desc: 'Tema rítmico e perigoso de perseguição e emboscadas na floresta escura.',
        scenes: ['C3', 'L2', 'L3', 'L4', 'L5']
      },
      {
        id: 'yt_vampire_hunters',
        title: 'Vampire Hunters (Combat Score)',
        author: 'Travis Savoie',
        category: 'combat',
        categoryLabel: '⚔️ Combate & Tensão',
        ytId: 'TL6ha77oqqE',
        desc: 'Combate dinâmico e veloz contra vampiros menores, noivos e crias nos corredores ou ruas.',
        scenes: ['E3', 'G1', 'G2', 'G3', 'G4', 'P3']
      },
      {
        id: 'yt_calm_forest',
        title: 'Svalich Woods (1h Dark Forest Ambience)',
        author: 'Michael Ghelfi Studios',
        category: 'ambient',
        categoryLabel: '🕯️ Ambientes & Terror',
        ytId: 'Sd9tKu-8t_I',
        desc: 'Ventos nas copas negras, corvos e sombras entre os pinheiros milenares de Svalich.',
        scenes: ['C2', 'C4', 'C6', 'L1']
      },
      {
        id: 'yt_cathedral_abbey',
        title: 'Abandoned Cathedral (Abbey of Saint Markovia)',
        author: 'Michael Ghelfi Studios',
        category: 'ambient',
        categoryLabel: '🕯️ Ambientes & Terror',
        ytId: 'uCBqy-KFcqM',
        desc: 'Eco sagrado em ruínas. Perfeito para a Igreja de Donavich em Baróvia e a Abadia em Krezk.',
        scenes: ['B7', 'B8', 'K1', 'K2', 'K3']
      },
      {
        id: 'yt_restless_knights',
        title: 'Restless Knights (Argynvostholt)',
        author: 'Travis Savoie',
        category: 'story',
        categoryLabel: '🥀 História & NPCs',
        ytId: '28QpslBWLko',
        desc: 'Marcha fúnebre heroica e desolada para os Cavaleiros Fantasmas de Vladimir Horngaard.',
        scenes: ['M1', 'M2', 'M3', 'M4', 'M5', 'M6']
      },
      {
        id: 'yt_wicked_rites',
        title: 'Wicked Rites (Yester Hill Ritual)',
        author: 'Travis Savoie',
        category: 'combat',
        categoryLabel: '⚔️ Combate & Tensão',
        ytId: 'pUHzlbbollI',
        desc: 'Percussões xamânicas primitivas para o ritual druídico de evocação do Colosso de Raízes.',
        scenes: ['J1', 'J2', 'J3', 'J4', 'J5', 'J6']
      },
      {
        id: 'yt_creeping_hut',
        title: 'The Creeping Hut (Baba Lysaga Boss Battle)',
        author: 'Travis Savoie',
        category: 'combat',
        categoryLabel: '⚔️ Combate & Tensão',
        ytId: '8l30E92iNLE',
        desc: 'Tema cataclísmico e frenético de chefe para a batalha contra Baba Lysaga e a Cabana Andante.',
        scenes: ['T4', 'T5', 'T6']
      },
      {
        id: 'yt_dark_swamp',
        title: 'Dark Swamp of Berez (1h Ambience)',
        author: 'Michael Ghelfi Studios',
        category: 'ambient',
        categoryLabel: '🕯️ Ambientes & Terror',
        ytId: 'kzBx8TWcrG4',
        desc: 'Águas estagnadas, névoa espessa e ruínas submersas da aldeia afogada de Berez.',
        scenes: ['T1', 'T2', 'T3', 'I1', 'I2', 'I3']
      },
      {
        id: 'yt_cursed_marsh',
        title: 'Cursed Marsh & Drownings',
        author: 'Michael Ghelfi Studios',
        category: 'ambient',
        categoryLabel: '🕯️ Ambientes & Terror',
        ytId: 'LqMGCtNlMXQ',
        desc: 'Inquietante e lamacento, perfeito para exploração cautelosa nas margens do Rio Ivlis.',
        scenes: ['I4', 'I5', 'I6']
      },
      {
        id: 'yt_frozen_ghakis',
        title: 'Tsolenka Pass & Mount Ghakis (1h Ambience)',
        author: 'Michael Ghelfi Studios',
        category: 'ambient',
        categoryLabel: '🕯️ Ambientes & Terror',
        ytId: '4EZpX881Cl4',
        desc: 'Ventos gélidos cortantes, desfiladeiros perigosos e fogueira solitária na nevasca.',
        scenes: ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6']
      },
      {
        id: 'yt_dark_vestiges',
        title: 'Dark Vestiges (The Amber Temple)',
        author: 'Travis Savoie',
        category: 'explore',
        categoryLabel: '🗺️ Exploração & Névoas',
        ytId: 'RssjzJL90_s',
        desc: 'Terror cósmico sutil e misterioso para os sarcófagos de âmbar e segredos esquecidos.',
        scenes: ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'S1', 'S2', 'S3']
      },
      {
        id: 'yt_march_dead',
        title: 'March of the Dead',
        author: 'Travis Savoie',
        category: 'ambient',
        categoryLabel: '🕯️ Ambientes & Terror',
        ytId: '9GSCFzOajmo',
        desc: 'A procissão fúnebre noturna dos aventureiros caídos caminhando rumo ao Castelo Ravenloft.',
        scenes: ['B4', 'B8']
      },
      {
        id: 'yt_sunsword_dawn',
        title: 'Glimmer of Hope (Sunsword & Dawn)',
        author: 'Travis Savoie',
        category: 'story',
        categoryLabel: '🥀 História & NPCs',
        ytId: 'mEizS-pvr28',
        desc: 'A luz triunfal da Espada Solar rompendo as trevas de Baróvia. O fim da maldição.',
        scenes: ['U5', 'U6']
      }
    ];

    // Quick Global Presets for the Soundboard Drawer
    this.presets = {
      taverna_chuva: { name: '🍺 Taverna & Chuva (A1/B5c/F1)', channels: { tavern: 0.50, fire: 0.45, lute: 0.40 }, sfx: 'door' },
      casa_da_morte: { name: '🕯️ Casa da Morte & Culto (A2)', channels: { whispers: 0.50, dungeon: 0.45, mystery: 0.45 }, sfx: 'heartbeat' },
      vila_barovia: { name: '🌫️ Vila de Baróvia & Cerco (Arco B)', channels: { wind: 0.50, rain: 0.45, piano: 0.45 }, sfx: 'bell' },
      vistani_tser: { name: '🔮 Tser Pool & Vistani (C4/E2)', channels: { fire: 0.55, vistani: 0.60, river: 0.30 }, sfx: 'bell' },
      floresta_svalich: { name: '🐺 Estrada & Floresta Svalich (C/L)', channels: { night: 0.60, wind: 0.45, exploration: 0.40 }, sfx: 'wolf' },
      moinho_bruxas: { name: '🧙‍♀️ Velho Moedor de Ossos (C9/H7)', channels: { grindstone: 0.55, witches: 0.55, cauldron: 0.40 }, sfx: 'hag_laugh' },
      vallaki_tensao: { name: '🏘️ Vallaki · Intrigas (D–G)', channels: { town: 0.45, mystery: 0.45 }, sfx: 'ravens' },
      igreja_abadia: { name: '⛪ Igreja & Abadia de Krezk (D/K)', channels: { monks: 0.55, choir: 0.45, whispers: 0.30 }, sfx: 'bell' },
      colina_yester: { name: '🩸 Colina Yester & Druidas (Arco J)', channels: { druid: 0.65, rain: 0.55, trees: 0.45 }, sfx: 'thunder' },
      pantano_berez: { name: '🐸 Pântano de Berez & Lysaga (I/T)', channels: { river: 0.55, cauldron: 0.50, witches: 0.50 }, sfx: 'hag_laugh' },
      argynvostholt: { name: '🐉 Mansão de Argynvostholt (Arco M)', channels: { wind: 0.55, dungeon: 0.40, piano: 0.45 }, sfx: 'iron_door' },
      jantar_strahd: { name: '🎹 O Jantar de Strahd (Arco O)', channels: { organ: 0.65, fire: 0.35, rain: 0.30 }, sfx: 'strahd_laugh' },
      ravenloft_incursao: { name: '🦇 Incursão em Ravenloft (Arco P)', channels: { dungeon: 0.55, horror: 0.50, organ: 0.35 }, sfx: 'bats' },
      ghakis_ambar: { name: '❄️ Tsolenka & Templo de Âmbar (R/S)', channels: { blizzard: 0.60, amber: 0.60, whispers: 0.40 }, sfx: 'scream' },
      combate_chefe: { name: '⚔️ Combate Mortal / Chefe', channels: { combat: 0.65, dread: 0.50, rain: 0.35 }, sfx: 'horn' },
      sol_nasce: { name: '🌅 O Sol Nasce (U6 / Epílogo)', channels: { choir: 0.60, lute: 0.45 }, sfx: 'bell' }
    };

    // All 180 Scene Audio Profiles
    this.sceneProfiles = {
  "A1": {
    "code": "A1",
    "name": "🍺 Taverna & Estrada na Chuva",
    "channels": {
      "tavern": 0.45,
      "rain": 0.45,
      "lute": 0.35
    },
    "sfx": [
      "thunder",
      "door",
      "wolf"
    ]
  },
  "A2": {
    "code": "A2",
    "name": "🌫️ Fachada da Casa da Morte",
    "channels": {
      "wind": 0.55,
      "rain": 0.4,
      "mystery": 0.45
    },
    "sfx": [
      "door",
      "thunder",
      "whispers_sfx"
    ]
  },
  "A2a": {
    "code": "A2a",
    "name": "🚪 Entrada & Portão Trancado",
    "channels": {
      "wind": 0.45,
      "mystery": 0.5
    },
    "sfx": [
      "iron_door",
      "heartbeat",
      "thunder"
    ]
  },
  "A2b": {
    "code": "A2b",
    "name": "🕯️ 1º Andar · Aparência de Normalidade",
    "channels": {
      "fire": 0.4,
      "mystery": 0.45,
      "whispers": 0.25
    },
    "sfx": [
      "door",
      "heartbeat",
      "sting"
    ]
  },
  "A2c": {
    "code": "A2c",
    "name": "🎹 2º Andar · Segredos e Cravo",
    "channels": {
      "piano": 0.5,
      "whispers": 0.35,
      "wind": 0.25
    },
    "sfx": [
      "door",
      "scream",
      "heartbeat"
    ]
  },
  "A2d": {
    "code": "A2d",
    "name": "⚔️ 3º Andar · Armadura & Violência",
    "channels": {
      "horror": 0.55,
      "whispers": 0.4
    },
    "sfx": [
      "sting",
      "trap",
      "scream"
    ]
  },
  "A2e": {
    "code": "A2e",
    "name": "👻 Sótão · Rose & Thorn",
    "channels": {
      "piano": 0.55,
      "whispers": 0.5
    },
    "sfx": [
      "scream",
      "iron_door",
      "heartbeat"
    ]
  },
  "A2f": {
    "code": "A2f",
    "name": "⛓️ Porão & Criptas do Culto",
    "channels": {
      "dungeon": 0.6,
      "whispers": 0.5,
      "horror": 0.45
    },
    "sfx": [
      "zombie",
      "chains",
      "trap"
    ]
  },
  "A2g": {
    "code": "A2g",
    "name": "🩸 Câmara Ritual · Lorghoth",
    "channels": {
      "dungeon": 0.55,
      "druid": 0.55,
      "combat": 0.5
    },
    "sfx": [
      "zombie",
      "scream",
      "fireball"
    ]
  },
  "A2h": {
    "code": "A2h",
    "name": "🔥 Fuga da Casa em Colapso",
    "channels": {
      "combat": 0.65,
      "fire": 0.6,
      "dread": 0.5
    },
    "sfx": [
      "trap",
      "fireball",
      "iron_door"
    ]
  },
  "A3": {
    "code": "A3",
    "name": "🌫️ Saída nas Brumas de Baróvia",
    "channels": {
      "wind": 0.6,
      "piano": 0.4
    },
    "sfx": [
      "ravens",
      "wolf",
      "bell"
    ]
  },
  "B1": {
    "code": "B1",
    "name": "🐺 Estrada Velha de Svalich",
    "channels": {
      "night": 0.55,
      "wind": 0.5,
      "exploration": 0.4
    },
    "sfx": [
      "wolf",
      "ravens",
      "carriage"
    ]
  },
  "B2": {
    "code": "B2",
    "name": "🚪 Portões Leste de Baróvia",
    "channels": {
      "wind": 0.6,
      "rain": 0.45,
      "dread": 0.35
    },
    "sfx": [
      "door",
      "wolf",
      "thunder"
    ]
  },
  "B3": {
    "code": "B3",
    "name": "🌲 Floresta & Cadáver de Dalvan",
    "channels": {
      "night": 0.6,
      "wind": 0.4,
      "mystery": 0.4
    },
    "sfx": [
      "ravens",
      "wolf",
      "sting"
    ]
  },
  "B4": {
    "code": "B4",
    "name": "🌧️ Mirante da Vila de Baróvia",
    "channels": {
      "wind": 0.55,
      "rain": 0.45,
      "exploration": 0.4
    },
    "sfx": [
      "bell",
      "thunder",
      "ravens"
    ]
  },
  "B5": {
    "code": "B5",
    "name": "🏘️ Vila de Baróvia Sob Cerco",
    "channels": {
      "rain": 0.5,
      "wind": 0.45,
      "piano": 0.4
    },
    "sfx": [
      "bell",
      "zombie",
      "scream"
    ]
  },
  "B5a": {
    "code": "B5a",
    "name": "🛡️ Barricada · Encontro com Ismark",
    "channels": {
      "rain": 0.45,
      "town": 0.3,
      "exploration": 0.4
    },
    "sfx": [
      "horn",
      "zombie",
      "door"
    ]
  },
  "B5b": {
    "code": "B5b",
    "name": "🏚️ Praça da Vila & Refugiados",
    "channels": {
      "rain": 0.45,
      "piano": 0.45,
      "whispers": 0.25
    },
    "sfx": [
      "bell",
      "scream",
      "thunder"
    ]
  },
  "B5c": {
    "code": "B5c",
    "name": "🍷 Taverna Sangue da Videira",
    "channels": {
      "tavern": 0.5,
      "fire": 0.45,
      "lute": 0.35
    },
    "sfx": [
      "door",
      "thunder",
      "bell"
    ]
  },
  "B5d": {
    "code": "B5d",
    "name": "🕯️ Mansão do Burgomestre · Ireena",
    "channels": {
      "fire": 0.4,
      "piano": 0.5,
      "rain": 0.3
    },
    "sfx": [
      "door",
      "wolf",
      "heartbeat"
    ]
  },
  "B5e": {
    "code": "B5e",
    "name": "🪙 Empório de Bildrath",
    "channels": {
      "town": 0.35,
      "rain": 0.35,
      "mystery": 0.35
    },
    "sfx": [
      "door",
      "chains",
      "thunder"
    ]
  },
  "B5f": {
    "code": "B5f",
    "name": "⚔️ Barricada Oriental · O Cerco",
    "channels": {
      "combat": 0.65,
      "rain": 0.55,
      "dread": 0.45
    },
    "sfx": [
      "zombie",
      "horn",
      "fireball"
    ]
  },
  "B5g": {
    "code": "B5g",
    "name": "🧟 Barricada Ocidental · Horda",
    "channels": {
      "combat": 0.7,
      "rain": 0.55,
      "horror": 0.5
    },
    "sfx": [
      "zombie",
      "werewolf",
      "thunder"
    ]
  },
  "B5h": {
    "code": "B5h",
    "name": "🧛 Retorno à Mansão & Cerco Final",
    "channels": {
      "dread": 0.6,
      "organ": 0.45,
      "rain": 0.45
    },
    "sfx": [
      "strahd_laugh",
      "bats",
      "thunder"
    ]
  },
  "B5i": {
    "code": "B5i",
    "name": "⛪ Igreja de Baróvia, Doru & Funeral",
    "channels": {
      "choir": 0.5,
      "dungeon": 0.45,
      "rain": 0.35
    },
    "sfx": [
      "bell",
      "scream",
      "iron_door"
    ]
  },
  "B5j": {
    "code": "B5j",
    "name": "🪦 Colina de Lugdana",
    "channels": {
      "wind": 0.55,
      "choir": 0.4,
      "exploration": 0.35
    },
    "sfx": [
      "thunder",
      "ravens",
      "bell"
    ]
  },
  "B5k": {
    "code": "B5k",
    "name": "😢 Casa de Mad Mary",
    "channels": {
      "piano": 0.6,
      "whispers": 0.4,
      "rain": 0.3
    },
    "sfx": [
      "scream",
      "door",
      "heartbeat"
    ]
  },
  "C1": {
    "code": "C1",
    "name": "🌲 Floresta & Esconderijo",
    "channels": {
      "night": 0.55,
      "exploration": 0.45
    },
    "sfx": [
      "wolf",
      "ravens",
      "trap"
    ]
  },
  "C2": {
    "code": "C2",
    "name": "🧛 Encruzilhada do Ivlis · 1º Encontro com Strahd",
    "channels": {
      "carriage": 0.45,
      "organ": 0.55,
      "dread": 0.5
    },
    "sfx": [
      "strahd_laugh",
      "thunder",
      "bats"
    ]
  },
  "C3": {
    "code": "C3",
    "name": "🐦‍⬛ A Strix & o Corvo Ferido",
    "channels": {
      "night": 0.55,
      "horror": 0.45
    },
    "sfx": [
      "ravens",
      "bats",
      "sting"
    ]
  },
  "C4": {
    "code": "C4",
    "name": "🔮 Tser Pool · Acampamento Vistani & Tarokka",
    "channels": {
      "fire": 0.6,
      "vistani": 0.65,
      "river": 0.3
    },
    "sfx": [
      "bell",
      "thunder",
      "hag_laugh"
    ]
  },
  "C5": {
    "code": "C5",
    "name": "🐎 Cavaleiro Esquelético na Neblina",
    "channels": {
      "wind": 0.55,
      "carriage": 0.45,
      "mystery": 0.45
    },
    "sfx": [
      "chains",
      "horn",
      "sting"
    ]
  },
  "C6": {
    "code": "C6",
    "name": "🗼 Torre de Vigia & Sepulturas",
    "channels": {
      "wind": 0.55,
      "exploration": 0.45
    },
    "sfx": [
      "ravens",
      "iron_door",
      "trap"
    ]
  },
  "C7": {
    "code": "C7",
    "name": "🌊 Cachoeira de Tser & Ponte Alta",
    "channels": {
      "river": 0.7,
      "wind": 0.45,
      "exploration": 0.4
    },
    "sfx": [
      "thunder",
      "wolf",
      "ravens"
    ]
  },
  "C8": {
    "code": "C8",
    "name": "🐎 Encruzilhada da Carruagem Negra",
    "channels": {
      "wind": 0.55,
      "carriage": 0.5,
      "dread": 0.45
    },
    "sfx": [
      "thunder",
      "strahd_laugh",
      "bats"
    ]
  },
  "C9": {
    "code": "C9",
    "name": "⚙️ Velho Moedor de Ossos (Contato)",
    "channels": {
      "grindstone": 0.6,
      "witches": 0.5,
      "wind": 0.4
    },
    "sfx": [
      "hag_laugh",
      "ravens",
      "door"
    ]
  },
  "C10": {
    "code": "C10",
    "name": "🌲 Floresta Profunda de Svalich",
    "channels": {
      "night": 0.65,
      "trees": 0.45,
      "horror": 0.4
    },
    "sfx": [
      "wolf",
      "werewolf",
      "bats"
    ]
  },
  "C11": {
    "code": "C11",
    "name": "🐾 Caçada dos Lobisomens",
    "channels": {
      "combat": 0.65,
      "night": 0.55,
      "dread": 0.5
    },
    "sfx": [
      "werewolf",
      "wolf",
      "heartbeat"
    ]
  },
  "C12": {
    "code": "C12",
    "name": "🏘️ Portões de Vallaki",
    "channels": {
      "town": 0.55,
      "wind": 0.35,
      "exploration": 0.4
    },
    "sfx": [
      "door",
      "bell",
      "ravens"
    ]
  },
  "D1": {
    "code": "D1",
    "name": "⛪ D1 · Igreja: abrir a investigação (Igreja de Sto. Andral)",
    "channels": {
      "choir": 0.5,
      "mystery": 0.45,
      "town": 0.25
    },
    "sfx": [
      "bell",
      "door",
      "heartbeat"
    ]
  },
  "D2": {
    "code": "D2",
    "name": "⛪ D2 · Milivoj: culpa e necessidade (Igreja de Sto. Andral)",
    "channels": {
      "choir": 0.5,
      "mystery": 0.45,
      "town": 0.25
    },
    "sfx": [
      "bell",
      "door",
      "heartbeat"
    ]
  },
  "D3": {
    "code": "D3",
    "name": "⚰️ D3 · Arasek: a carroça que parece perigosa (Loja de Caixões & Vampiros)",
    "channels": {
      "horror": 0.6,
      "combat": 0.5,
      "whispers": 0.4
    },
    "sfx": [
      "trap",
      "bats",
      "scream"
    ]
  },
  "D4": {
    "code": "D4",
    "name": "⚰️ D4 · Loja de caixões: entrada, ossos e armadilha (Loja de Caixões & Vampiros)",
    "channels": {
      "horror": 0.6,
      "combat": 0.5,
      "whispers": 0.4
    },
    "sfx": [
      "trap",
      "bats",
      "scream"
    ]
  },
  "D5": {
    "code": "D5",
    "name": "⛪ D5 · Restaurar a proteção da igreja (Igreja de Sto. Andral)",
    "channels": {
      "choir": 0.5,
      "mystery": 0.45,
      "town": 0.25
    },
    "sfx": [
      "bell",
      "door",
      "heartbeat"
    ]
  },
  "D6": {
    "code": "D6",
    "name": "🗡️ D6 · Rahadin: convite e julgamento (Rahadin & Coro de Gritos)",
    "channels": {
      "whispers": 0.65,
      "dread": 0.55,
      "carriage": 0.4
    },
    "sfx": [
      "scream",
      "strahd_laugh",
      "horn"
    ]
  },
  "E1": {
    "code": "E1",
    "name": "🔍 E1 · Blinsky: brinquedo e conexões (Investigação em Vallaki)",
    "channels": {
      "town": 0.45,
      "mystery": 0.45
    },
    "sfx": [
      "door",
      "bell",
      "ravens"
    ]
  },
  "E2": {
    "code": "E2",
    "name": "⛺ E2 · Acampamento vistani e Kasimir (Acampamento Vistani)",
    "channels": {
      "fire": 0.55,
      "vistani": 0.5,
      "night": 0.3
    },
    "sfx": [
      "wolf",
      "bell",
      "ravens"
    ]
  },
  "E3": {
    "code": "E3",
    "name": "⚡ E3 · Mansão e biblioteca do barão (Torre de Khazan)",
    "channels": {
      "wind": 0.55,
      "amber": 0.45,
      "mystery": 0.45
    },
    "sfx": [
      "thunder",
      "fireball",
      "trap"
    ]
  },
  "E4": {
    "code": "E4",
    "name": "🌊 E4 · Lago Zarovich: caçadores e orientação (Lago Zarovich)",
    "channels": {
      "river": 0.6,
      "wind": 0.45,
      "mystery": 0.4
    },
    "sfx": [
      "scream",
      "ravens",
      "thunder"
    ]
  },
  "E5": {
    "code": "E5",
    "name": "🔍 E5 · Estrada até Baratok (Investigação em Vallaki)",
    "channels": {
      "town": 0.45,
      "mystery": 0.45
    },
    "sfx": [
      "door",
      "bell",
      "ravens"
    ]
  },
  "E6": {
    "code": "E6",
    "name": "⚡ E6 · Torre de Khazan e carroça de Ezmerelda (Torre de Khazan)",
    "channels": {
      "wind": 0.55,
      "amber": 0.45,
      "mystery": 0.45
    },
    "sfx": [
      "thunder",
      "fireball",
      "trap"
    ]
  },
  "E7": {
    "code": "E7",
    "name": "⚡ E7 · Regresso com a descoberta (Torre de Khazan)",
    "channels": {
      "wind": 0.55,
      "amber": 0.45,
      "mystery": 0.45
    },
    "sfx": [
      "thunder",
      "fireball",
      "trap"
    ]
  },
  "E8": {
    "code": "E8",
    "name": "🔍 E8 · Rictavio, Arabelle e Arrigal (Investigação em Vallaki)",
    "channels": {
      "town": 0.45,
      "mystery": 0.45
    },
    "sfx": [
      "door",
      "bell",
      "ravens"
    ]
  },
  "F1": {
    "code": "F1",
    "name": "🍺 F1 · Convite na Estalagem Água Azul (Estalagem Água Azul)",
    "channels": {
      "tavern": 0.55,
      "fire": 0.45,
      "lute": 0.4
    },
    "sfx": [
      "ravens",
      "door",
      "bell"
    ]
  },
  "F2": {
    "code": "F2",
    "name": "🕯️ F2 · Wachterhaus: proposta política (Wachterhaus & Conspiração)",
    "channels": {
      "mystery": 0.55,
      "whispers": 0.35,
      "fire": 0.3
    },
    "sfx": [
      "door",
      "heartbeat",
      "chains"
    ]
  },
  "F3": {
    "code": "F3",
    "name": "🍺 F3 · Ernst e a preparação (Estalagem Água Azul)",
    "channels": {
      "tavern": 0.55,
      "fire": 0.45,
      "lute": 0.4
    },
    "sfx": [
      "ravens",
      "door",
      "bell"
    ]
  },
  "F4": {
    "code": "F4",
    "name": "⚔️ F4 · Acompanhar e emboscar Izek (Emboscada a Izek)",
    "channels": {
      "combat": 0.65,
      "dread": 0.45,
      "rain": 0.35
    },
    "sfx": [
      "fireball",
      "horn",
      "sting"
    ]
  },
  "F5": {
    "code": "F5",
    "name": "⚔️ F5 · Mudança de governo e pagamento (Emboscada a Izek)",
    "channels": {
      "combat": 0.65,
      "dread": 0.45,
      "rain": 0.35
    },
    "sfx": [
      "fireball",
      "horn",
      "sting"
    ]
  },
  "G1": {
    "code": "G1",
    "name": "🔥 G1 · Izek invade a estalagem (Confronto em Vallaki)",
    "channels": {
      "combat": 0.6,
      "horror": 0.45,
      "town": 0.35
    },
    "sfx": [
      "horn",
      "fireball",
      "iron_door"
    ]
  },
  "G2": {
    "code": "G2",
    "name": "🚨 G2 · Cartazes pela cidade (Vallaki Sob Lei Marcial)",
    "channels": {
      "town": 0.4,
      "dread": 0.5,
      "rain": 0.35
    },
    "sfx": [
      "horn",
      "bell",
      "chains"
    ]
  },
  "G3": {
    "code": "G3",
    "name": "🚨 G3 · Sequestro (Vallaki Sob Lei Marcial)",
    "channels": {
      "town": 0.4,
      "dread": 0.5,
      "rain": 0.35
    },
    "sfx": [
      "horn",
      "bell",
      "chains"
    ]
  },
  "G4": {
    "code": "G4",
    "name": "🔥 G4 · Infiltrar ou atacar a mansão (Confronto em Vallaki)",
    "channels": {
      "combat": 0.6,
      "horror": 0.45,
      "town": 0.35
    },
    "sfx": [
      "horn",
      "fireball",
      "iron_door"
    ]
  },
  "H1": {
    "code": "H1",
    "name": "🔮 H1 · Erasmus pede ajuda (Sótão de Victor & Espelho)",
    "channels": {
      "mystery": 0.55,
      "whispers": 0.45,
      "piano": 0.35
    },
    "sfx": [
      "scream",
      "thunder",
      "heartbeat"
    ]
  },
  "H2": {
    "code": "H2",
    "name": "🔮 H2 · Victor e o espelho espiritual (Sótão de Victor & Espelho)",
    "channels": {
      "mystery": 0.55,
      "whispers": 0.45,
      "piano": 0.35
    },
    "sfx": [
      "scream",
      "thunder",
      "heartbeat"
    ]
  },
  "H3": {
    "code": "H3",
    "name": "🔮 H3 · Refugiados e Franz (Sótão de Victor & Espelho)",
    "channels": {
      "mystery": 0.55,
      "whispers": 0.45,
      "piano": 0.35
    },
    "sfx": [
      "scream",
      "thunder",
      "heartbeat"
    ]
  },
  "H4": {
    "code": "H4",
    "name": "🔮 H4 · As duas rotas de Victor (Sótão de Victor & Espelho)",
    "channels": {
      "mystery": 0.55,
      "whispers": 0.45,
      "piano": 0.35
    },
    "sfx": [
      "scream",
      "thunder",
      "heartbeat"
    ]
  },
  "H5": {
    "code": "H5",
    "name": "🔮 H5 · Conseguir a ajuda de Fiona (Sótão de Victor & Espelho)",
    "channels": {
      "mystery": 0.55,
      "whispers": 0.45,
      "piano": 0.35
    },
    "sfx": [
      "scream",
      "thunder",
      "heartbeat"
    ]
  },
  "H6": {
    "code": "H6",
    "name": "🧙‍♀️ H6 · Viagem ao moinho (Velho Moedor de Ossos)",
    "channels": {
      "grindstone": 0.55,
      "witches": 0.55,
      "cauldron": 0.45
    },
    "sfx": [
      "hag_laugh",
      "scream",
      "fireball"
    ]
  },
  "H7": {
    "code": "H7",
    "name": "🧙‍♀️ H7 · Moinho: nomes verdadeiros, crianças e pedra (Velho Moedor de Ossos)",
    "channels": {
      "grindstone": 0.55,
      "witches": 0.55,
      "cauldron": 0.45
    },
    "sfx": [
      "hag_laugh",
      "scream",
      "fireball"
    ]
  },
  "H8": {
    "code": "H8",
    "name": "🔮 H8 · Lua cheia: restauração de Stella (Sótão de Victor & Espelho)",
    "channels": {
      "mystery": 0.55,
      "whispers": 0.45,
      "piano": 0.35
    },
    "sfx": [
      "scream",
      "thunder",
      "heartbeat"
    ]
  },
  "H9": {
    "code": "H9",
    "name": "📖 H9 · Tomo de Strahd (O Tomo de Strahd)",
    "channels": {
      "organ": 0.5,
      "whispers": 0.55,
      "dread": 0.4
    },
    "sfx": [
      "strahd_laugh",
      "heartbeat",
      "thunder"
    ]
  },
  "I1": {
    "code": "I1",
    "name": "🌲 I1 · Viagem para Krezk (Estrada para Krezk)",
    "channels": {
      "wind": 0.5,
      "exploration": 0.45,
      "night": 0.35
    },
    "sfx": [
      "wolf",
      "ravens",
      "door"
    ]
  },
  "I2": {
    "code": "I2",
    "name": "🐸 I2 · Dmitri no portão (Pântano de Berez)",
    "channels": {
      "river": 0.6,
      "rain": 0.45,
      "witches": 0.4
    },
    "sfx": [
      "hag_laugh",
      "ravens",
      "thunder"
    ]
  },
  "I3": {
    "code": "I3",
    "name": "🐸 I3 · Estrada para Berez (Pântano de Berez)",
    "channels": {
      "river": 0.6,
      "rain": 0.45,
      "witches": 0.4
    },
    "sfx": [
      "hag_laugh",
      "ravens",
      "thunder"
    ]
  },
  "I4": {
    "code": "I4",
    "name": "🐸 I4 · Berez: negociação e vidência (Pântano de Berez)",
    "channels": {
      "river": 0.6,
      "rain": 0.45,
      "witches": 0.4
    },
    "sfx": [
      "hag_laugh",
      "ravens",
      "thunder"
    ]
  },
  "I5": {
    "code": "I5",
    "name": "🐸 I5 · Retorno com a informação (Pântano de Berez)",
    "channels": {
      "river": 0.6,
      "rain": 0.45,
      "witches": 0.4
    },
    "sfx": [
      "hag_laugh",
      "ravens",
      "thunder"
    ]
  },
  "I6": {
    "code": "I6",
    "name": "⛪ I6 · Entrada, piscina e abadia (Santuário de Krezk)",
    "channels": {
      "monks": 0.5,
      "river": 0.4,
      "wind": 0.35
    },
    "sfx": [
      "bell",
      "thunder",
      "scream"
    ]
  },
  "J1": {
    "code": "J1",
    "name": "🌩️ J1 · Novo pedido de Urwin (Colina Yester & Wintersplinter)",
    "channels": {
      "druid": 0.65,
      "rain": 0.6,
      "trees": 0.5
    },
    "sfx": [
      "thunder",
      "horn",
      "scream"
    ]
  },
  "J2": {
    "code": "J2",
    "name": "🌩️ J2 · Estrada para a vinícola (Colina Yester & Wintersplinter)",
    "channels": {
      "druid": 0.65,
      "rain": 0.6,
      "trees": 0.5
    },
    "sfx": [
      "thunder",
      "horn",
      "scream"
    ]
  },
  "J3": {
    "code": "J3",
    "name": "🌩️ J3 · Libertar a Vinícola Mago dos Vinhos (Colina Yester & Wintersplinter)",
    "channels": {
      "druid": 0.65,
      "rain": 0.6,
      "trees": 0.5
    },
    "sfx": [
      "thunder",
      "horn",
      "scream"
    ]
  },
  "J4": {
    "code": "J4",
    "name": "🌩️ J4 · Kavan e a viagem antes do amanhecer (Colina Yester & Wintersplinter)",
    "channels": {
      "druid": 0.65,
      "rain": 0.6,
      "trees": 0.5
    },
    "sfx": [
      "thunder",
      "horn",
      "scream"
    ]
  },
  "J5": {
    "code": "J5",
    "name": "🌩️ J5 · Yester: impedir Wintersplinter (Colina Yester & Wintersplinter)",
    "channels": {
      "druid": 0.65,
      "rain": 0.6,
      "trees": 0.5
    },
    "sfx": [
      "thunder",
      "horn",
      "scream"
    ]
  },
  "J6": {
    "code": "J6",
    "name": "🌩️ J6 · Depois do ritual (Colina Yester & Wintersplinter)",
    "channels": {
      "druid": 0.65,
      "rain": 0.6,
      "trees": 0.5
    },
    "sfx": [
      "thunder",
      "horn",
      "scream"
    ]
  },
  "J7": {
    "code": "J7",
    "name": "🍇 J7 · Devolver a gema (Batalha na Vinícola)",
    "channels": {
      "trees": 0.5,
      "combat": 0.55,
      "rain": 0.4
    },
    "sfx": [
      "ravens",
      "trap",
      "wolf"
    ]
  },
  "K1": {
    "code": "K1",
    "name": "🔔 K1 · Krezk e a dívida da família (Abadia de Santa Markovia)",
    "channels": {
      "monks": 0.55,
      "horror": 0.45,
      "whispers": 0.35
    },
    "sfx": [
      "bell",
      "scream",
      "chains"
    ]
  },
  "K1a": {
    "code": "K1a",
    "name": "🔔 K1a · Casa dos Krezkov (Abadia de Santa Markovia)",
    "channels": {
      "monks": 0.55,
      "horror": 0.45,
      "whispers": 0.35
    },
    "sfx": [
      "bell",
      "scream",
      "chains"
    ]
  },
  "K2": {
    "code": "K2",
    "name": "🔔 K2 · Abadia e aliança com Ezmerelda (Abadia de Santa Markovia)",
    "channels": {
      "monks": 0.55,
      "horror": 0.45,
      "whispers": 0.35
    },
    "sfx": [
      "bell",
      "scream",
      "chains"
    ]
  },
  "K2a": {
    "code": "K2a",
    "name": "🔔 K2a · Portão e disponibilidade da aliada (Abadia de Santa Markovia)",
    "channels": {
      "monks": 0.55,
      "horror": 0.45,
      "whispers": 0.35
    },
    "sfx": [
      "bell",
      "scream",
      "chains"
    ]
  },
  "K2b": {
    "code": "K2b",
    "name": "🔔 K2b · Salão principal e Vasilka (Abadia de Santa Markovia)",
    "channels": {
      "monks": 0.55,
      "horror": 0.45,
      "whispers": 0.35
    },
    "sfx": [
      "bell",
      "scream",
      "chains"
    ]
  },
  "K2c": {
    "code": "K2c",
    "name": "🔔 K2c · Ala oriental: Ezmerelda e investigação (Abadia de Santa Markovia)",
    "channels": {
      "monks": 0.55,
      "horror": 0.45,
      "whispers": 0.35
    },
    "sfx": [
      "bell",
      "scream",
      "chains"
    ]
  },
  "L1": {
    "code": "L1",
    "name": "🐾 L1 · Localizar o covil (Caverna dos Lobisomens)",
    "channels": {
      "dungeon": 0.55,
      "fire": 0.4,
      "dread": 0.45
    },
    "sfx": [
      "werewolf",
      "wolf",
      "chains"
    ]
  },
  "L2": {
    "code": "L2",
    "name": "🌲 L2 · Lago Baratok: recuperar suprimentos (Rastreamento na Floresta)",
    "channels": {
      "night": 0.6,
      "wind": 0.45,
      "exploration": 0.4
    },
    "sfx": [
      "wolf",
      "werewolf",
      "ravens"
    ]
  },
  "L3": {
    "code": "L3",
    "name": "🐾 L3 · Vigília na floresta (Caverna dos Lobisomens)",
    "channels": {
      "dungeon": 0.55,
      "fire": 0.4,
      "dread": 0.45
    },
    "sfx": [
      "werewolf",
      "wolf",
      "chains"
    ]
  },
  "L4": {
    "code": "L4",
    "name": "🐾 L4 · Covil, prisioneiros e acordo (Caverna dos Lobisomens)",
    "channels": {
      "dungeon": 0.55,
      "fire": 0.4,
      "dread": 0.45
    },
    "sfx": [
      "werewolf",
      "wolf",
      "chains"
    ]
  },
  "M1": {
    "code": "M1",
    "name": "🐉 M1 · Rumo a Argynvostholt (Batalha em Argynvostholt)",
    "channels": {
      "combat": 0.55,
      "wind": 0.55,
      "organ": 0.4
    },
    "sfx": [
      "horn",
      "fireball",
      "iron_door"
    ]
  },
  "M2": {
    "code": "M2",
    "name": "🏰 M2 · Exterior da mansão (Mansão de Argynvostholt)",
    "channels": {
      "wind": 0.55,
      "dungeon": 0.4,
      "piano": 0.45
    },
    "sfx": [
      "iron_door",
      "chains",
      "whispers_sfx"
    ]
  },
  "M3": {
    "code": "M3",
    "name": "🐉 M3 · Entrada e encontro com Godfrey (Batalha em Argynvostholt)",
    "channels": {
      "combat": 0.55,
      "wind": 0.55,
      "organ": 0.4
    },
    "sfx": [
      "horn",
      "fireball",
      "iron_door"
    ]
  },
  "M4": {
    "code": "M4",
    "name": "🐉 M4 · Primeiro andar: Zorya e os mortos (Batalha em Argynvostholt)",
    "channels": {
      "combat": 0.55,
      "wind": 0.55,
      "organ": 0.4
    },
    "sfx": [
      "horn",
      "fireball",
      "iron_door"
    ]
  },
  "M5": {
    "code": "M5",
    "name": "🐉 M5 · Segundo andar: exploração por alas (Batalha em Argynvostholt)",
    "channels": {
      "combat": 0.55,
      "wind": 0.55,
      "organ": 0.4
    },
    "sfx": [
      "horn",
      "fireball",
      "iron_door"
    ]
  },
  "M6": {
    "code": "M6",
    "name": "🐉 M6 · Terceiro andar: juramento e memória (Batalha em Argynvostholt)",
    "channels": {
      "combat": 0.55,
      "wind": 0.55,
      "organ": 0.4
    },
    "sfx": [
      "horn",
      "fireball",
      "iron_door"
    ]
  },
  "M7": {
    "code": "M7",
    "name": "🐉 M7 · Telhado e farol apagado (Batalha em Argynvostholt)",
    "channels": {
      "combat": 0.55,
      "wind": 0.55,
      "organ": 0.4
    },
    "sfx": [
      "horn",
      "fireball",
      "iron_door"
    ]
  },
  "O1": {
    "code": "O1",
    "name": "🎹 O1 · Convite e garantia de hospitalidade (Salão de Jantar de Strahd)",
    "channels": {
      "organ": 0.65,
      "fire": 0.35,
      "rain": 0.3
    },
    "sfx": [
      "strahd_laugh",
      "thunder",
      "door"
    ]
  },
  "O2": {
    "code": "O2",
    "name": "🎹 O2 · Arrigal aponta um possível traidor (Salão de Jantar de Strahd)",
    "channels": {
      "organ": 0.65,
      "fire": 0.35,
      "rain": 0.3
    },
    "sfx": [
      "strahd_laugh",
      "thunder",
      "door"
    ]
  },
  "O3": {
    "code": "O3",
    "name": "🐎 O3 · Estrada: Doru, cavaleiro e carruagem (Carruagem para Ravenloft)",
    "channels": {
      "carriage": 0.6,
      "rain": 0.45,
      "dread": 0.4
    },
    "sfx": [
      "thunder",
      "wolf",
      "door"
    ]
  },
  "O4": {
    "code": "O4",
    "name": "🎹 O4 · Chegada e apresentação da corte (Salão de Jantar de Strahd)",
    "channels": {
      "organ": 0.65,
      "fire": 0.35,
      "rain": 0.3
    },
    "sfx": [
      "strahd_laugh",
      "thunder",
      "door"
    ]
  },
  "O5": {
    "code": "O5",
    "name": "🎹 O5 · O jantar: conversa e três perguntas (Salão de Jantar de Strahd)",
    "channels": {
      "organ": 0.65,
      "fire": 0.35,
      "rain": 0.3
    },
    "sfx": [
      "strahd_laugh",
      "thunder",
      "door"
    ]
  },
  "O6": {
    "code": "O6",
    "name": "🎹 O6 · Visita ao castelo e encontro com Sasha (Salão de Jantar de Strahd)",
    "channels": {
      "organ": 0.65,
      "fire": 0.35,
      "rain": 0.3
    },
    "sfx": [
      "strahd_laugh",
      "thunder",
      "door"
    ]
  },
  "O7": {
    "code": "O7",
    "name": "🎹 O7 · A suíte de hóspedes (Salão de Jantar de Strahd)",
    "channels": {
      "organ": 0.65,
      "fire": 0.35,
      "rain": 0.3
    },
    "sfx": [
      "strahd_laugh",
      "thunder",
      "door"
    ]
  },
  "O8": {
    "code": "O8",
    "name": "💀 O8 · Pesadelo de Varushka (Pesadelo em Ravenloft)",
    "channels": {
      "horror": 0.65,
      "whispers": 0.55
    },
    "sfx": [
      "heartbeat",
      "scream",
      "sting"
    ]
  },
  "O9": {
    "code": "O9",
    "name": "🦇 O9 · Despertar (Hospitalidade de Ravenloft)",
    "channels": {
      "organ": 0.45,
      "mystery": 0.45,
      "wind": 0.4
    },
    "sfx": [
      "door",
      "bats",
      "heartbeat"
    ]
  },
  "O10": {
    "code": "O10",
    "name": "🦇 O10 · Exploração antes da partida (Hospitalidade de Ravenloft)",
    "channels": {
      "organ": 0.45,
      "mystery": 0.45,
      "wind": 0.4
    },
    "sfx": [
      "door",
      "bats",
      "heartbeat"
    ]
  },
  "O11": {
    "code": "O11",
    "name": "🎹 O11 · Manhã e saída de Ravenloft (Salão de Jantar de Strahd)",
    "channels": {
      "organ": 0.65,
      "fire": 0.35,
      "rain": 0.3
    },
    "sfx": [
      "strahd_laugh",
      "thunder",
      "door"
    ]
  },
  "P1": {
    "code": "P1",
    "name": "⛓️ P1 · Plano da incursão (Masmorras & Catacumbas de Ravenloft)",
    "channels": {
      "dungeon": 0.65,
      "horror": 0.5,
      "whispers": 0.4
    },
    "sfx": [
      "chains",
      "iron_door",
      "bats"
    ]
  },
  "P2": {
    "code": "P2",
    "name": "🌩️ P2 · Chegada sem convite (Torres & Pátios de Ravenloft)",
    "channels": {
      "rain": 0.6,
      "wind": 0.55,
      "dread": 0.45
    },
    "sfx": [
      "bell",
      "thunder",
      "bats"
    ]
  },
  "P3": {
    "code": "P3",
    "name": "⛓️ P3 · Pátios e acessos externos (Masmorras & Catacumbas de Ravenloft)",
    "channels": {
      "dungeon": 0.65,
      "horror": 0.5,
      "whispers": 0.4
    },
    "sfx": [
      "chains",
      "iron_door",
      "bats"
    ]
  },
  "P4": {
    "code": "P4",
    "name": "🦇 P4 · Áreas comuns do castelo (Infiltração em Ravenloft)",
    "channels": {
      "mystery": 0.55,
      "organ": 0.4,
      "dungeon": 0.35
    },
    "sfx": [
      "iron_door",
      "heartbeat",
      "trap"
    ]
  },
  "P5": {
    "code": "P5",
    "name": "🦇 P5 · Ala dos servos e elevador (Infiltração em Ravenloft)",
    "channels": {
      "mystery": 0.55,
      "organ": 0.4,
      "dungeon": 0.35
    },
    "sfx": [
      "iron_door",
      "heartbeat",
      "trap"
    ]
  },
  "P6": {
    "code": "P6",
    "name": "🦇 P6 · Aposentos reais e Gertruda (Infiltração em Ravenloft)",
    "channels": {
      "mystery": 0.55,
      "organ": 0.4,
      "dungeon": 0.35
    },
    "sfx": [
      "iron_door",
      "heartbeat",
      "trap"
    ]
  },
  "P7": {
    "code": "P7",
    "name": "🌩️ P7 · Campanário e tesouros (Torres & Pátios de Ravenloft)",
    "channels": {
      "rain": 0.6,
      "wind": 0.55,
      "dread": 0.45
    },
    "sfx": [
      "bell",
      "thunder",
      "bats"
    ]
  },
  "P8": {
    "code": "P8",
    "name": "🧪 P8 · Suíte: um lugar conhecido com novas regras (Aposentos das Bruxas)",
    "channels": {
      "cauldron": 0.6,
      "witches": 0.5,
      "dungeon": 0.35
    },
    "sfx": [
      "hag_laugh",
      "bats",
      "fireball"
    ]
  },
  "P9": {
    "code": "P9",
    "name": "🧪 P9 · Aposentos das bruxas (Aposentos das Bruxas)",
    "channels": {
      "cauldron": 0.6,
      "witches": 0.5,
      "dungeon": 0.35
    },
    "sfx": [
      "hag_laugh",
      "bats",
      "fireball"
    ]
  },
  "P10": {
    "code": "P10",
    "name": "🦇 P10 · Guarnição e circulação vertical (Infiltração em Ravenloft)",
    "channels": {
      "mystery": 0.55,
      "organ": 0.4,
      "dungeon": 0.35
    },
    "sfx": [
      "iron_door",
      "heartbeat",
      "trap"
    ]
  },
  "P11": {
    "code": "P11",
    "name": "⛓️ P11 · Masmorras, Emil e braseiro (Masmorras & Catacumbas de Ravenloft)",
    "channels": {
      "dungeon": 0.65,
      "horror": 0.5,
      "whispers": 0.4
    },
    "sfx": [
      "chains",
      "iron_door",
      "bats"
    ]
  },
  "P12": {
    "code": "P12",
    "name": "⛓️ P12 · Catacumbas e relíquias (Masmorras & Catacumbas de Ravenloft)",
    "channels": {
      "dungeon": 0.65,
      "horror": 0.5,
      "whispers": 0.4
    },
    "sfx": [
      "chains",
      "iron_door",
      "bats"
    ]
  },
  "Q1": {
    "code": "Q1",
    "name": "🐉 Q1 · A retirada determina o retorno (O Farol de Argynvost)",
    "channels": {
      "choir": 0.6,
      "wind": 0.45,
      "organ": 0.35
    },
    "sfx": [
      "horn",
      "bell",
      "fireball"
    ]
  },
  "Q2": {
    "code": "Q2",
    "name": "👼 Q2 · Dmitri: perigo até o anoitecer (Confronto com o Abade)",
    "channels": {
      "monks": 0.55,
      "combat": 0.55,
      "dread": 0.45
    },
    "sfx": [
      "bell",
      "scream",
      "fireball"
    ]
  },
  "Q3": {
    "code": "Q3",
    "name": "👼 Q3 · Abade: confronto e possibilidade de redenção (Confronto com o Abade)",
    "channels": {
      "monks": 0.55,
      "combat": 0.55,
      "dread": 0.45
    },
    "sfx": [
      "bell",
      "scream",
      "fireball"
    ]
  },
  "Q4": {
    "code": "Q4",
    "name": "👼 Q4 · O aviso dos revenantes (Confronto com o Abade)",
    "channels": {
      "monks": 0.55,
      "combat": 0.55,
      "dread": 0.45
    },
    "sfx": [
      "bell",
      "scream",
      "fireball"
    ]
  },
  "Q5": {
    "code": "Q5",
    "name": "👼 Q5 · Kiril caça o grupo (Confronto com o Abade)",
    "channels": {
      "monks": 0.55,
      "combat": 0.55,
      "dread": 0.45
    },
    "sfx": [
      "bell",
      "scream",
      "fireball"
    ]
  },
  "Q6": {
    "code": "Q6",
    "name": "🐉 Q6 · Devolver o crânio e acender o farol (O Farol de Argynvost)",
    "channels": {
      "choir": 0.6,
      "wind": 0.45,
      "organ": 0.35
    },
    "sfx": [
      "horn",
      "bell",
      "fireball"
    ]
  },
  "Q7": {
    "code": "Q7",
    "name": "🐾 Q7 · Cumprir o acordo do covil (Emboscada da Alcateia)",
    "channels": {
      "combat": 0.65,
      "night": 0.55
    },
    "sfx": [
      "werewolf",
      "wolf",
      "horn"
    ]
  },
  "R1": {
    "code": "R1",
    "name": "🔥 R1 · Kasimir e o destino de Patrina (Abrigo em Soldav)",
    "channels": {
      "fire": 0.6,
      "blizzard": 0.35,
      "vistani": 0.35
    },
    "sfx": [
      "door",
      "wolf",
      "horn"
    ]
  },
  "R2": {
    "code": "R2",
    "name": "🏔️ R2 · A queda do tirano local (Subida do Monte Ghakis)",
    "channels": {
      "blizzard": 0.55,
      "exploration": 0.45
    },
    "sfx": [
      "wind",
      "horn",
      "werewolf"
    ]
  },
  "R3": {
    "code": "R3",
    "name": "🏔️ R3 · Roupas de frio e primeira provação (Subida do Monte Ghakis)",
    "channels": {
      "blizzard": 0.55,
      "exploration": 0.45
    },
    "sfx": [
      "wind",
      "horn",
      "werewolf"
    ]
  },
  "R4": {
    "code": "R4",
    "name": "❄️ R4 · Passo Tsolenka: sequência de viagem (Nevasca em Tsolenka)",
    "channels": {
      "blizzard": 0.7,
      "wind": 0.55,
      "dread": 0.4
    },
    "sfx": [
      "thunder",
      "horn",
      "trap"
    ]
  },
  "R4a": {
    "code": "R4a",
    "name": "🏔️ R4a · Partida e plano da subida (Subida do Monte Ghakis)",
    "channels": {
      "blizzard": 0.55,
      "exploration": 0.45
    },
    "sfx": [
      "wind",
      "horn",
      "werewolf"
    ]
  },
  "R4d": {
    "code": "R4d",
    "name": "❄️ R4d · Nevasca (Nevasca em Tsolenka)",
    "channels": {
      "blizzard": 0.7,
      "wind": 0.55,
      "dread": 0.4
    },
    "sfx": [
      "thunder",
      "horn",
      "trap"
    ]
  },
  "R4e": {
    "code": "R4e",
    "name": "❄️ R4e · Portaria de Tsolenka (Nevasca em Tsolenka)",
    "channels": {
      "blizzard": 0.7,
      "wind": 0.55,
      "dread": 0.4
    },
    "sfx": [
      "thunder",
      "horn",
      "trap"
    ]
  },
  "R4f": {
    "code": "R4f",
    "name": "🏔️ R4f · Segunda provação do tirano (Subida do Monte Ghakis)",
    "channels": {
      "blizzard": 0.55,
      "exploration": 0.45
    },
    "sfx": [
      "wind",
      "horn",
      "werewolf"
    ]
  },
  "R4i": {
    "code": "R4i",
    "name": "❄️ R4i · Avalanche e rotas de escape (Nevasca em Tsolenka)",
    "channels": {
      "blizzard": 0.7,
      "wind": 0.55,
      "dread": 0.4
    },
    "sfx": [
      "thunder",
      "horn",
      "trap"
    ]
  },
  "R4j": {
    "code": "R4j",
    "name": "🕯️ R4j · Covil dos bodaks (Santuário das Três Senhoras)",
    "channels": {
      "druid": 0.5,
      "whispers": 0.45,
      "wind": 0.35
    },
    "sfx": [
      "bell",
      "ravens",
      "heartbeat"
    ]
  },
  "R4k": {
    "code": "R4k",
    "name": "❄️ R4k · Cavernas de gelo (Nevasca em Tsolenka)",
    "channels": {
      "blizzard": 0.7,
      "wind": 0.55,
      "dread": 0.4
    },
    "sfx": [
      "thunder",
      "horn",
      "trap"
    ]
  },
  "R5": {
    "code": "R5",
    "name": "❄️ R5 · Soldav: abrigo e revelação (Nevasca em Tsolenka)",
    "channels": {
      "blizzard": 0.7,
      "wind": 0.55,
      "dread": 0.4
    },
    "sfx": [
      "thunder",
      "horn",
      "trap"
    ]
  },
  "R5d": {
    "code": "R5d",
    "name": "🏔️ R5d · Casa da liderança e jogos sociais (Subida do Monte Ghakis)",
    "channels": {
      "blizzard": 0.55,
      "exploration": 0.45
    },
    "sfx": [
      "wind",
      "horn",
      "werewolf"
    ]
  },
  "R5f": {
    "code": "R5f",
    "name": "🕯️ R5f · Santuário das Rozana (Santuário das Três Senhoras)",
    "channels": {
      "druid": 0.5,
      "whispers": 0.45,
      "wind": 0.35
    },
    "sfx": [
      "bell",
      "ravens",
      "heartbeat"
    ]
  },
  "R6": {
    "code": "R6",
    "name": "🏔️ R6 · Monte Ghakis: Sangzor e o templo (Subida do Monte Ghakis)",
    "channels": {
      "blizzard": 0.55,
      "exploration": 0.45
    },
    "sfx": [
      "wind",
      "horn",
      "werewolf"
    ]
  },
  "S1": {
    "code": "S1",
    "name": "🔮 S1 · Exterior do templo (Salões e Sarcófagos de Âmbar)",
    "channels": {
      "amber": 0.65,
      "whispers": 0.5,
      "dungeon": 0.4
    },
    "sfx": [
      "heartbeat",
      "scream",
      "iron_door"
    ]
  },
  "S2": {
    "code": "S2",
    "name": "🔥 S2 · Defesas e o falso anfitrião (Defesas do Templo de Âmbar)",
    "channels": {
      "amber": 0.6,
      "combat": 0.55,
      "dungeon": 0.4
    },
    "sfx": [
      "fireball",
      "scream",
      "trap"
    ]
  },
  "S3": {
    "code": "S3",
    "name": "🔥 S3 · Catacumbas e Nardag (Defesas do Templo de Âmbar)",
    "channels": {
      "amber": 0.6,
      "combat": 0.55,
      "dungeon": 0.4
    },
    "sfx": [
      "fireball",
      "scream",
      "trap"
    ]
  },
  "S4": {
    "code": "S4",
    "name": "🔮 S4 · Templo ocidental (Salões e Sarcófagos de Âmbar)",
    "channels": {
      "amber": 0.65,
      "whispers": 0.5,
      "dungeon": 0.4
    },
    "sfx": [
      "heartbeat",
      "scream",
      "iron_door"
    ]
  },
  "S5": {
    "code": "S5",
    "name": "🔥 S5 · Templo oriental (Defesas do Templo de Âmbar)",
    "channels": {
      "amber": 0.6,
      "combat": 0.55,
      "dungeon": 0.4
    },
    "sfx": [
      "fireball",
      "scream",
      "trap"
    ]
  },
  "S6": {
    "code": "S6",
    "name": "🔥 S6 · Tesouros, sarcófagos e Patrina (Defesas do Templo de Âmbar)",
    "channels": {
      "amber": 0.6,
      "combat": 0.55,
      "dungeon": 0.4
    },
    "sfx": [
      "fireball",
      "scream",
      "trap"
    ]
  },
  "S7": {
    "code": "S7",
    "name": "🔮 S7 · Exethanter e o plano de fuga de Strahd (Salões e Sarcófagos de Âmbar)",
    "channels": {
      "amber": 0.65,
      "whispers": 0.5,
      "dungeon": 0.4
    },
    "sfx": [
      "heartbeat",
      "scream",
      "iron_door"
    ]
  },
  "S8": {
    "code": "S8",
    "name": "🔥 S8 · Neferon cobra a saída (Defesas do Templo de Âmbar)",
    "channels": {
      "amber": 0.6,
      "combat": 0.55,
      "dungeon": 0.4
    },
    "sfx": [
      "fireball",
      "scream",
      "trap"
    ]
  },
  "T1": {
    "code": "T1",
    "name": "🌫️ T1 · Voltar a Soldav e obter instruções (Alianças Finais no Vale)",
    "channels": {
      "exploration": 0.5,
      "rain": 0.45,
      "dread": 0.4
    },
    "sfx": [
      "ravens",
      "thunder",
      "horn"
    ]
  },
  "T2": {
    "code": "T2",
    "name": "🧙‍♀️ T2 · Descida: o vale mudou (Baba Lysaga & Cabana Rastejante)",
    "channels": {
      "combat": 0.65,
      "cauldron": 0.55,
      "witches": 0.55
    },
    "sfx": [
      "hag_laugh",
      "fireball",
      "ravens"
    ]
  },
  "T3": {
    "code": "T3",
    "name": "🧙‍♀️ T3 · Berez: resgate, Lysaga e reconciliação (Baba Lysaga & Cabana Rastejante)",
    "channels": {
      "combat": 0.65,
      "cauldron": 0.55,
      "witches": 0.55
    },
    "sfx": [
      "hag_laugh",
      "fireball",
      "ravens"
    ]
  },
  "T3f": {
    "code": "T3f",
    "name": "✨ T3f · Sergei no monumento de Marina (Reconsecração das Senhoras)",
    "channels": {
      "choir": 0.55,
      "druid": 0.45,
      "river": 0.4
    },
    "sfx": [
      "bell",
      "thunder",
      "ravens"
    ]
  },
  "T3k": {
    "code": "T3k",
    "name": "🧙‍♀️ T3k · Confrontar Baba Lysaga e a cabana (Baba Lysaga & Cabana Rastejante)",
    "channels": {
      "combat": 0.65,
      "cauldron": 0.55,
      "witches": 0.55
    },
    "sfx": [
      "hag_laugh",
      "fireball",
      "ravens"
    ]
  },
  "T3l": {
    "code": "T3l",
    "name": "🌫️ T3l · Urwin e Davian: resolver a ruptura (Alianças Finais no Vale)",
    "channels": {
      "exploration": 0.5,
      "rain": 0.45,
      "dread": 0.4
    },
    "sfx": [
      "ravens",
      "thunder",
      "horn"
    ]
  },
  "T3m": {
    "code": "T3m",
    "name": "🧙‍♀️ T3m · Reconsecrar o Pântano (Baba Lysaga & Cabana Rastejante)",
    "channels": {
      "combat": 0.65,
      "cauldron": 0.55,
      "witches": 0.55
    },
    "sfx": [
      "hag_laugh",
      "fireball",
      "ravens"
    ]
  },
  "T4": {
    "code": "T4",
    "name": "🌫️ T4 · Van Richten e Arturi (Alianças Finais no Vale)",
    "channels": {
      "exploration": 0.5,
      "rain": 0.45,
      "dread": 0.4
    },
    "sfx": [
      "ravens",
      "thunder",
      "horn"
    ]
  },
  "T4d": {
    "code": "T4d",
    "name": "✨ T4d · Reconsecrar a Floresta (Reconsecração das Senhoras)",
    "channels": {
      "choir": 0.55,
      "druid": 0.45,
      "river": 0.4
    },
    "sfx": [
      "bell",
      "thunder",
      "ravens"
    ]
  },
  "T5": {
    "code": "T5",
    "name": "🌫️ T5 · Fiona: decidir enfrentar Strahd (Alianças Finais no Vale)",
    "channels": {
      "exploration": 0.5,
      "rain": 0.45,
      "dread": 0.4
    },
    "sfx": [
      "ravens",
      "thunder",
      "horn"
    ]
  },
  "T5d": {
    "code": "T5d",
    "name": "✨ T5d · Reconsecrar a Montanha (Reconsecração das Senhoras)",
    "channels": {
      "choir": 0.55,
      "druid": 0.45,
      "river": 0.4
    },
    "sfx": [
      "bell",
      "thunder",
      "ravens"
    ]
  },
  "U1": {
    "code": "U1",
    "name": "🌑 U1 · Conselho de guerra (Noite Eterna & Conselho)",
    "channels": {
      "dread": 0.6,
      "organ": 0.45,
      "whispers": 0.4
    },
    "sfx": [
      "thunder",
      "heartbeat",
      "bell"
    ]
  },
  "U2": {
    "code": "U2",
    "name": "🌑 U2 · O sonho e o preço de Ireena (Noite Eterna & Conselho)",
    "channels": {
      "dread": 0.6,
      "organ": 0.45,
      "whispers": 0.4
    },
    "sfx": [
      "thunder",
      "heartbeat",
      "bell"
    ]
  },
  "U3": {
    "code": "U3",
    "name": "👑 U3 · Noite eterna e defesa de Vallaki (Confronto Final em Ravenloft)",
    "channels": {
      "organ": 0.65,
      "combat": 0.65,
      "rain": 0.45
    },
    "sfx": [
      "strahd_laugh",
      "thunder",
      "heartbeat"
    ]
  },
  "U3d": {
    "code": "U3d",
    "name": "🌑 U3d · Pesadelos (Noite Eterna & Conselho)",
    "channels": {
      "dread": 0.6,
      "organ": 0.45,
      "whispers": 0.4
    },
    "sfx": [
      "thunder",
      "heartbeat",
      "bell"
    ]
  },
  "U3i": {
    "code": "U3i",
    "name": "👑 U3i · Lago e coração do Sonhador (Confronto Final em Ravenloft)",
    "channels": {
      "organ": 0.65,
      "combat": 0.65,
      "rain": 0.45
    },
    "sfx": [
      "strahd_laugh",
      "thunder",
      "heartbeat"
    ]
  },
  "U3j": {
    "code": "U3j",
    "name": "⚔️ U3j · Portão oriental: organizar a defesa (A Guerra de Vallaki)",
    "channels": {
      "combat": 0.7,
      "rain": 0.55,
      "dread": 0.5
    },
    "sfx": [
      "horn",
      "zombie",
      "fireball"
    ]
  },
  "U4": {
    "code": "U4",
    "name": "⚔️ U4 · Estrada e o exército de mortos (A Guerra de Vallaki)",
    "channels": {
      "combat": 0.7,
      "rain": 0.55,
      "dread": 0.5
    },
    "sfx": [
      "horn",
      "zombie",
      "fireball"
    ]
  },
  "U5": {
    "code": "U5",
    "name": "👑 U5 · Ravenloft e o Coração da Tristeza (Confronto Final em Ravenloft)",
    "channels": {
      "organ": 0.65,
      "combat": 0.65,
      "rain": 0.45
    },
    "sfx": [
      "strahd_laugh",
      "thunder",
      "heartbeat"
    ]
  },
  "U6": {
    "code": "U6",
    "name": "🌅 U6 · O sol nasce (O Sol Nasce sobre Baróvia)",
    "channels": {
      "choir": 0.65,
      "piano": 0.5
    },
    "sfx": [
      "bell",
      "ravens",
      "horn"
    ]
  },
  "EP1": {
    "code": "EP1",
    "name": "🕊️ EP1 · Retorno do castelo (Epílogo & Paz)",
    "channels": {
      "piano": 0.5,
      "wind": 0.25,
      "choir": 0.35
    },
    "sfx": [
      "bell",
      "ravens",
      "door"
    ]
  },
  "EP2": {
    "code": "EP2",
    "name": "🌅 EP2 · Festival do Amanhecer (Amanhecer em Baróvia)",
    "channels": {
      "town": 0.45,
      "lute": 0.5,
      "choir": 0.4
    },
    "sfx": [
      "bell",
      "horn",
      "ravens"
    ]
  },
  "EP3": {
    "code": "EP3",
    "name": "🌅 EP3 · Retorno a Krezk (Amanhecer em Baróvia)",
    "channels": {
      "town": 0.45,
      "lute": 0.5,
      "choir": 0.4
    },
    "sfx": [
      "bell",
      "horn",
      "ravens"
    ]
  },
  "EP4": {
    "code": "EP4",
    "name": "🎻 EP4 · Vila de Baróvia e Tser Pool (Despedida Vistani)",
    "channels": {
      "fire": 0.5,
      "vistani": 0.55,
      "river": 0.3
    },
    "sfx": [
      "bell",
      "ravens",
      "door"
    ]
  },
  "EP5": {
    "code": "EP5",
    "name": "🕊️ EP5 · O destino de Escher (Epílogo & Paz)",
    "channels": {
      "piano": 0.5,
      "wind": 0.25,
      "choir": 0.35
    },
    "sfx": [
      "bell",
      "ravens",
      "door"
    ]
  },
  "EP6": {
    "code": "EP6",
    "name": "🕊️ EP6 · Encerramentos e novos começos (Epílogo & Paz)",
    "channels": {
      "piano": 0.5,
      "wind": 0.25,
      "choir": 0.35
    },
    "sfx": [
      "bell",
      "ravens",
      "door"
    ]
  }
};
  }

  getChannelMeta(id) {
    return this.ambientChannels.find(c => c.id === id) || this.musicChannels.find(c => c.id === id) || null;
  }

  getSfxMeta(id) {
    return this.sfxPads.find(p => p.id === id) || null;
  }

  getSceneProfile(sceneCode) {
    if (!sceneCode) return null;
    if (this.sceneProfiles[sceneCode]) return this.sceneProfiles[sceneCode];
    const base = String(sceneCode).replace(/[a-z]+$/i, '');
    return this.sceneProfiles[base] || this.sceneProfiles['A1'];
  }

  getYouTubeTracks(category = 'all') {
    if (!category || category === 'all') return this.youtubeTracks;
    return this.youtubeTracks.filter(t => t.category === category);
  }

  getYoutubeRecommendationForScene(sceneCode) {
    if (!sceneCode) return this.youtubeTracks[0];
    const match = this.youtubeTracks.find(t => t.scenes && t.scenes.includes(sceneCode));
    if (match) return match;

    const code = String(sceneCode).trim().toUpperCase();
    if (code.startsWith('A2')) return this.youtubeTracks.find(t => t.id === 'yt_haunted_mansion') || this.youtubeTracks[0];
    if (code.startsWith('A1')) return this.youtubeTracks.find(t => t.id === 'yt_quiet_tavern') || this.youtubeTracks[0];
    if (code.startsWith('B')) return this.youtubeTracks.find(t => t.id === 'yt_barovian_legends') || this.youtubeTracks[0];
    if (code.startsWith('C9') || code.startsWith('H')) return this.youtubeTracks.find(t => t.id === 'yt_dream_pastries') || this.youtubeTracks[0];
    if (code.startsWith('C')) return this.youtubeTracks.find(t => t.id === 'yt_into_mists') || this.youtubeTracks[0];
    if (code.startsWith('D') || code.startsWith('E') || code.startsWith('F') || code.startsWith('G')) return this.youtubeTracks.find(t => t.id === 'yt_barovian_legends') || this.youtubeTracks[0];
    if (code.startsWith('J')) return this.youtubeTracks.find(t => t.id === 'yt_wicked_rites') || this.youtubeTracks[0];
    if (code.startsWith('K')) return this.youtubeTracks.find(t => t.id === 'yt_cathedral_abbey') || this.youtubeTracks[0];
    if (code.startsWith('L')) return this.youtubeTracks.find(t => t.id === 'yt_wolves_dance') || this.youtubeTracks[0];
    if (code.startsWith('M')) return this.youtubeTracks.find(t => t.id === 'yt_restless_knights') || this.youtubeTracks[0];
    if (code.startsWith('O')) return this.youtubeTracks.find(t => t.id === 'yt_waltzing_shadows') || this.youtubeTracks[0];
    if (code.startsWith('P')) return this.youtubeTracks.find(t => t.id === 'yt_castle_ravenloft') || this.youtubeTracks[0];
    if (code.startsWith('Q')) return this.youtubeTracks.find(t => t.id === 'yt_frozen_ghakis') || this.youtubeTracks[0];
    if (code.startsWith('R') || code.startsWith('S')) return this.youtubeTracks.find(t => t.id === 'yt_dark_vestiges') || this.youtubeTracks[0];
    if (code.startsWith('T') || code.startsWith('I')) return this.youtubeTracks.find(t => t.id === 'yt_creeping_hut') || this.youtubeTracks[0];
    if (code.startsWith('U')) return this.youtubeTracks.find(t => t.id === 'yt_he_is_ancient') || this.youtubeTracks[0];
    if (code.startsWith('EP')) return this.youtubeTracks.find(t => t.id === 'yt_sunsword_dawn') || this.youtubeTracks[0];
    return this.youtubeTracks[0];
  }

  playSceneAudio(sceneCode, playLeadSfx = false) {
    const prof = this.getSceneProfile(sceneCode);
    if (!prof) return;
    this.stopAll();
    this.activePreset = 'scene:' + sceneCode;
    for (const [chId, vol] of Object.entries(prof.channels || {})) {
      this.startChannel(chId, vol);
    }
    if (playLeadSfx && prof.sfx && prof.sfx.length) {
      this.triggerSFX(prof.sfx[0]);
    }
    this.notifyUI();
  }

  ensureContext() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioCtx();
      this.masterGain = this.ctx.createGain();
      this.masterGain.gain.value = this.masterVolume;
      this.masterGain.connect(this.ctx.destination);
    }
    if (this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  toggleChannel(id, volume = 0.5) {
    if (this.activeLoops.has(id)) {
      this.stopChannel(id);
      return false;
    } else {
      this.startChannel(id, volume);
      return true;
    }
  }

  setChannelVolume(id, volume) {
    const loop = this.activeLoops.get(id);
    if (loop) {
      loop.volume = volume;
      if (loop.audio) {
        loop.audio.volume = Math.max(0, Math.min(1, volume * this.masterVolume));
      }
      if (loop.gainNode && this.ctx) {
        loop.gainNode.gain.setTargetAtTime(volume, this.ctx.currentTime, 0.1);
      }
    }
  }

  setMasterVolume(vol) {
    this.masterVolume = vol;
    if (this.masterGain && this.ctx) {
      this.masterGain.gain.setTargetAtTime(vol, this.ctx.currentTime, 0.08);
    }
    for (const [, loop] of this.activeLoops.entries()) {
      if (loop.audio) {
        loop.audio.volume = Math.max(0, Math.min(1, loop.volume * vol));
      }
    }
  }

  attachCustomFile(id, file) {
    const url = URL.createObjectURL(file);
    const audio = new Audio(url);
    audio.loop = !this.sfxPads.some(p => p.id === id);
    this.customFiles.set(id, audio);
    if (this.activeLoops.has(id)) {
      const vol = this.activeLoops.get(id).volume || 0.5;
      this.stopChannel(id);
      this.startChannel(id, vol);
    }
  }

  startChannel(id, volume = 0.5) {
    this.stopChannel(id);

    // 1. Check user-attached custom file first
    if (this.customFiles.has(id)) {
      const audio = this.customFiles.get(id);
      audio.loop = true;
      audio.volume = Math.max(0, Math.min(1, volume * this.masterVolume));
      audio.currentTime = 0;
      audio.play().catch(() => {});
      this.activeLoops.set(id, { type: 'file', audio, volume });
      this.notifyUI();
      return;
    }

    // 2. Use built-in downloaded real .mp3 file from assets/audio/
    const meta = this.getChannelMeta(id);
    if (meta && meta.file) {
      const audio = new Audio(meta.file);
      audio.loop = true;
      if (id === 'blizzard') audio.playbackRate = 1.25;
      audio.volume = Math.max(0, Math.min(1, volume * this.masterVolume));
      const playPromise = audio.play();
      if (playPromise !== undefined) {
        playPromise.catch(() => {
          // Fallback to WebAudio synth if file blocked or missing
          this.startSynthFallback(id, volume);
        });
      }
      this.activeLoops.set(id, { type: 'file', audio, volume });
      this.notifyUI();
      return;
    }

    this.startSynthFallback(id, volume);
  }

  startSynthFallback(id, volume = 0.5) {
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
    this.activeLoops.set(id, { type: 'synth', gainNode, nodes: [osc], intervals: [], volume });
    this.notifyUI();
  }

  stopChannel(id) {
    const loop = this.activeLoops.get(id);
    if (!loop) return;
    if (loop.type === 'file' && loop.audio) {
      try {
        loop.audio.pause();
        loop.audio.currentTime = 0;
      } catch (e) {}
    } else {
      if (loop.intervals) loop.intervals.forEach(clearInterval);
      if (loop.nodes) {
        loop.nodes.forEach(n => {
          try { n.stop(); n.disconnect(); } catch (e) {}
        });
      }
    }
    this.activeLoops.delete(id);
    this.notifyUI();
  }

  stopAll() {
    for (const id of Array.from(this.activeLoops.keys())) {
      this.stopChannel(id);
    }
    this.activePreset = null;
    this.notifyUI();
  }

  applyPreset(presetKey, playSfx = false) {
    if (presetKey && presetKey.startsWith('scene:')) {
      this.playSceneAudio(presetKey.slice(6), playSfx);
      return;
    }
    const p = this.presets[presetKey];
    if (!p) return;
    this.stopAll();
    this.activePreset = presetKey;
    for (const [chId, vol] of Object.entries(p.channels)) {
      this.startChannel(chId, vol);
    }
    if (playSfx && p.sfx) {
      this.triggerSFX(p.sfx);
    }
    this.notifyUI();
  }

  triggerSFX(id) {
    // 1. User-attached custom file
    if (this.customFiles.has(id)) {
      const audio = this.customFiles.get(id);
      audio.volume = Math.max(0, Math.min(1, this.masterVolume));
      audio.currentTime = 0;
      audio.play().catch(() => {});
      return;
    }

    // 2. Built-in real .mp3 SFX from assets/audio/
    const pad = this.getSfxMeta(id);
    if (pad && pad.file) {
      const sfxAudio = new Audio(pad.file);
      sfxAudio.volume = Math.max(0, Math.min(1, this.masterVolume));
      sfxAudio.play().catch(() => {});
      return;
    }
  }

  notifyUI() {
    if (typeof window.onSoundboardStateChange === 'function') {
      window.onSoundboardStateChange();
    }
  }
}

window.baroviaSound = new BaroviaSoundEngine();
