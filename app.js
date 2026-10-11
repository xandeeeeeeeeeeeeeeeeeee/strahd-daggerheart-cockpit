// ============================================================================
// STRAHD RELOADED · DAGGERHEART — COCKPIT MINIMALISTA 2.5 (app.js)
// Zero poluição visual + Filtro Anti-Spoiler para o 2º Monitor Físico
// ============================================================================

(function () {
  const DATA = window.CAMPAIGN_DATA || {
    arcs: [], scenes: [], encounters: [], bestiary: [],
    items_spells: [], amber_pacts: [], calendar: [], rules: [], maps: []
  };

  const bc = typeof BroadcastChannel !== 'undefined' ? new BroadcastChannel('strahd-daggerheart-live') : null;
  let playerPopup = null;

  const defaultState = {
    fear: 2,
    activeArcCode: 'A',
    activeSceneCode: 'A1',
    sceneStates: {},
    sceneNotes: {},
    lastQuote: '',
    clocks: [
      { id: 'clk_1', name: 'Fuga da Casa da Morte', current: 0, max: 6, public: true },
      { id: 'clk_2', name: 'Cerco na Vila de Baróvia', current: 0, max: 8, public: true },
      { id: 'clk_3', name: 'Caçada em Svalich', current: 0, max: 6, public: false }
    ],
    combatants: [],
    activeEncounterId: '',
    party: [
      { id: 'pc1', name: 'PJ 1', relic: 'Medalhão do Amanhecer', evasion: 10, thresholds: '8/16', hp: 0, maxHp: 6, stress: 0, maxStress: 6, hope: 2, corruption: 0 },
      { id: 'pc2', name: 'PJ 2', relic: 'Pena de Corvo', evasion: 12, thresholds: '7/14', hp: 0, maxHp: 6, stress: 0, maxStress: 6, hope: 2, corruption: 0 },
      { id: 'pc3', name: 'PJ 3', relic: 'Fragmento de Âmbar', evasion: 11, thresholds: '6/13', hp: 0, maxHp: 6, stress: 0, maxStress: 6, hope: 2, corruption: 0 },
      { id: 'pc4', name: 'PJ 4', relic: 'Lâmina Quebrada', evasion: 10, thresholds: '8/15', hp: 0, maxHp: 6, stress: 0, maxStress: 6, hope: 2, corruption: 0 }
    ]
  };

  let state = loadState();
  let currentCatalogType = 'bestiary';

  function loadState() {
    try {
      const raw = localStorage.getItem('strahd-cockpit-state-v2');
      if (!raw) return structuredClone(defaultState);
      return Object.assign(structuredClone(defaultState), JSON.parse(raw));
    } catch (e) {
      return structuredClone(defaultState);
    }
  }

  function saveState() {
    try {
      localStorage.setItem('strahd-cockpit-state-v2', JSON.stringify(state));
    } catch (e) {}
    broadcastCockpitState();
  }

  // ==========================================================================
  // ANTI-SPOILER BROADCAST TO 2ND PHYSICAL MONITOR
  // Never sends internal scene titles ("A armadilha se fecha") or GM secrets!
  // ==========================================================================
  function getPublicRegionName(sc) {
    if (!sc) return 'Baróvia';
    const mp = (sc.map_title || 'Baróvia').split('·')[0].trim();
    return mp || 'Baróvia';
  }

  function broadcastCockpitState(options = {}) {
    const sc = getActiveScene();
    const payload = {
      type: 'cockpit-state-sync',
      fear: state.fear,
      publicLocation: getPublicRegionName(sc),
      clocks: state.clocks,
      quote: options.quote !== undefined ? options.quote : undefined,
      handout: options.handout || undefined,
      clearOverlays: Boolean(options.clearOverlays)
    };
    if (bc) {
      try { bc.postMessage(payload); } catch (e) {}
    }
    if (playerPopup && !playerPopup.closed) {
      try { playerPopup.postMessage(payload, '*'); } catch (e) {}
    }
  }

  // Sanitizes any markdown body to extract ONLY player-safe descriptive text
  // Strips all statblocks, PV, Estresse, Dificuldade, Segredos, Gatilhos, Táticas, etc.
  function extractPlayerSafeText(rawBody) {
    const lines = String(rawBody || '').split('\n');
    const safeLines = [];
    for (let raw of lines) {
      const l = raw.trim();
      if (!l) continue;
      if (l.startsWith('#') || l.startsWith('|') || l.startsWith('---') || l.startsWith('←') || l.startsWith('INPUT[')) continue;
      // If there's an explicit Read-Aloud ("Para narrar") line, prefer it!
      if (l.startsWith('**Para narrar:**') || l.startsWith('**Leitura em voz alta:**')) {
        return l.replace(/^\*\*[^*]+\*\*\s*/, '').replace(/^["“]|["”]$/g, '');
      }
      // Skip any line containing GM mechanics or spoilers
      const lower = l.toLowerCase();
      if (
        lower.includes('segredo') ||
        lower.includes('daggerheart') ||
        lower.includes('dificuldade') ||
        lower.includes('limiares') ||
        lower.includes('estresse') ||
        lower.includes('pontos de vida') ||
        lower.includes('pv:') ||
        lower.includes('ataque') ||
        lower.includes('gatilho') ||
        lower.includes('objetivo') ||
        lower.includes('tática') ||
        lower.includes('comportamento') ||
        lower.includes('medo') ||
        lower.includes('patamar') ||
        lower.includes('papel:') ||
        lower.includes('ficha') ||
        lower.includes('mapa') ||
        lower.includes('verdade') ||
        lower.includes('ocult') ||
        lower.includes('armadilha')
      ) {
        continue;
      }
      const cleaned = l.replace(/\*\*([^*]+)\*\*/g, '$1').replace(/\[\[([^\]]+)\]\]/g, '$1');
      if (cleaned.length > 20) safeLines.push(cleaned);
    }
    return safeLines.slice(0, 2).join('\n\n') || 'Descrição visual reservada ao Mestre (digite aqui apenas o que deseja revelar aos jogadores).';
  }

  const $ = id => document.getElementById(id);

  function escapeHtml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // ==========================================================================
  // 1. HEADER: FEAR, DUALITY, SIDEBAR TOGGLE & 2ND MONITOR
  // ==========================================================================
  $('btnToggleLeftCol').onclick = () => {
    $('cockpitGrid').classList.toggle('hide-left');
  };

  function renderFearBar() {
    const maxF = state.maxFear || 12;
    $('fearCountText').textContent = state.fear > maxF ? `${state.fear}` : `${state.fear}/${maxF}`;
  }

  function changeFear(delta) {
    state.fear = Math.max(0, state.fear + delta);
    saveState();
    renderFearBar();
  }

  $('fearCountText').style.cursor = 'pointer';
  $('fearCountText').title = 'Clique para definir qualquer valor de Medo (sem limite)';
  $('fearCountText').onclick = () => {
    const val = prompt('Definir valor atual de Medo (pode ser maior que 12):', String(state.fear));
    if (val !== null && val.trim() !== '') {
      state.fear = Math.max(0, parseInt(val, 10) || 0);
      saveState();
      renderFearBar();
    }
  };

  $('btnFearMinus').onclick = () => changeFear(-1);
  $('btnFearPlus').onclick = () => changeFear(1);

  $('btnShortRest').onclick = () => {
    const roll = Math.floor(Math.random() * 4) + 1;
    changeFear(roll);
    const box = $('dualityResultBox');
    box.className = 'duality-output fear';
    box.textContent = `⛺ Curto: +${roll} Medo`;
  };

  $('btnLongRest').onclick = () => {
    const roll = Math.floor(Math.random() * 4) + 1;
    const total = roll + (state.party.length || 4);
    changeFear(total);
    const box = $('dualityResultBox');
    box.className = 'duality-output fear';
    box.textContent = `🌙 Longo: +${total} Medo`;
  };

  function rollDuality() {
    const mod = Number($('dualityMod').value) || 0;
    const dc = Number($('dualityDC').value) || 14;
    const hopeDie = Math.floor(Math.random() * 12) + 1;
    const fearDie = Math.floor(Math.random() * 12) + 1;
    const isCrit = hopeDie === fearDie;
    const total = hopeDie + fearDie + mod;
    const ok = isCrit || total >= dc;
    const box = $('dualityResultBox');

    if (isCrit) {
      box.className = 'duality-output crit';
      box.textContent = `🌟 CRÍTICO! ${total} (${hopeDie}=${fearDie})`;
      window.baroviaSound?.triggerSFX('crit');
    } else if (hopeDie > fearDie) {
      box.className = 'duality-output hope';
      box.textContent = `${ok ? '✅' : '❌'} ${total} c/ ESPERANÇA (☀️${hopeDie} 💀${fearDie})`;
    } else {
      box.className = 'duality-output fear';
      box.innerHTML = `${ok ? '⚠️' : '💀'} ${total} c/ MEDO (☀️${hopeDie} 💀${fearDie}) <a href="#" id="quickAddFearLink" style="color:#fff;margin-left:4px">+1💀</a>`;
      const lnk = document.getElementById('quickAddFearLink');
      if (lnk) lnk.onclick = (e) => { e.preventDefault(); changeFear(1); lnk.remove(); };
    }
  }

  $('btnRollDuality').onclick = rollDuality;

  $('btnRollGM20').onclick = () => {
    const mod = Number($('dualityMod').value) || 0;
    const d20 = Math.floor(Math.random() * 20) + 1;
    const total = d20 + mod;
    const box = $('dualityResultBox');
    box.className = 'duality-output' + (d20 === 20 ? ' crit' : '');
    box.textContent = `👹 d20: ${total} (${d20}${mod >= 0 ? '+' + mod : mod})`;
  };

  window.setDualityDCAndRoll = function (dc) {
    $('dualityDC').value = dc;
    rollDuality();
  };

  $('btnClearPlayerOverlays').onclick = () => {
    state.lastQuote = '';
    broadcastCockpitState({ clearOverlays: true, quote: '' });
  };

  $('btnOpenPlayerScreen').onclick = () => {
    playerPopup = window.open('player.html', 'strahd-player-live', 'width=1366,height=840');
    setTimeout(() => broadcastCockpitState(), 500);
  };

  // ==========================================================================
  // 2. NAVIGATION TABS & SUBTABS
  // ==========================================================================
  document.querySelectorAll('.nav-tab').forEach(btn => {
    btn.onclick = () => {
      document.querySelectorAll('.nav-tab').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
      btn.classList.add('active');
      const target = $(btn.dataset.tab);
      if (target) target.classList.add('active');
      if (btn.dataset.tab === 'tab-notion') generateSessionMarkdownLog();
    };
  });

  document.querySelectorAll('.subtab-btn').forEach(btn => {
    btn.onclick = () => {
      document.querySelectorAll('.subtab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.right-tab-pane').forEach(p => p.style.display = 'none');
      btn.classList.add('active');
      const pane = $(btn.dataset.righttab);
      if (pane) pane.style.display = 'block';
    };
  });

  // ==========================================================================
  // 3. LEFT COLUMN: CLEAN SCENE LIST
  // ==========================================================================
  function initArcSelect() {
    const sel = $('arcFilterSelect');
    sel.innerHTML = '<option value="ALL">Todos os 22 Arcos (180 Cenas)</option>';
    DATA.arcs.forEach(arc => {
      const opt = document.createElement('option');
      opt.value = arc.code;
      opt.textContent = `${arc.title} (Nív. ${arc.level})`;
      sel.appendChild(opt);
    });
    sel.value = state.activeArcCode || 'A';
    sel.onchange = () => {
      state.activeArcCode = sel.value;
      saveState();
      renderSceneList();
      renderArcDeadlines();
    };
  }

  function getFilteredScenes() {
    const q = ($('sceneSearchInput').value || '').trim().toLowerCase();
    const stFilter = $('sceneStatusFilter').value;
    const arcCode = $('arcFilterSelect').value;

    return DATA.scenes.filter(sc => {
      if (arcCode && arcCode !== 'ALL' && sc.arc_code !== arcCode) return false;
      const curSt = state.sceneStates[sc.code] || sc.status || 'A preparar';
      if (stFilter && curSt !== stFilter) return false;
      if (q) {
        const hay = `${sc.code} ${sc.title} ${sc.focus} ${sc.map_title}`.toLowerCase();
        if (!hay.includes(q)) return false;
      }
      return true;
    });
  }

  function renderSceneList() {
    const list = getFilteredScenes();
    $('scenesCounterBadge').textContent = list.length;
    const container = $('sceneListContainer');
    container.innerHTML = '';

    list.forEach(sc => {
      const curSt = state.sceneStates[sc.code] || sc.status || 'A preparar';
      const div = document.createElement('div');
      div.className = 'scene-item' +
        (sc.code === state.activeSceneCode ? ' active' : '') +
        (curSt === 'Concluída' ? ' done' : '');

      const stIcon = curSt === 'Concluída' ? '✅' : curSt === 'Em jogo' ? '🔥' : '';
      const shortTitle = sc.title.replace(/^[^\s]+ · /, '');
      div.innerHTML = `
        <div class="scene-item-label" title="${escapeHtml(sc.title)}">
          <span class="scene-code">${stIcon ? stIcon + ' ' : ''}${escapeHtml(sc.code)}</span>
          <span>${escapeHtml(shortTitle)}</span>
        </div>
        ${sc.essential ? '<span class="dot-essential" title="Cena Essencial">★</span>' : ''}
      `;
      div.onclick = () => selectScene(sc.code);
      container.appendChild(div);
    });
  }

  $('sceneSearchInput').oninput = renderSceneList;
  $('sceneStatusFilter').onchange = renderSceneList;

  // ==========================================================================
  // 4. CENTER COLUMN: LOSSLESS STRUCTURED SCENE READER
  // ==========================================================================
  function getActiveScene() {
    return DATA.scenes.find(s => s.code === state.activeSceneCode) || DATA.scenes[0];
  }

  function formatInlineMarkdown(text) {
    let html = escapeHtml(text);
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

    html = html.replace(/\[\[([^\]]+)\]\]/g, (_, target) => {
      return `<a href="#" class="wikilink-ref" data-ref="${escapeHtml(target)}" style="color:var(--gold);text-decoration:underline dotted">${escapeHtml(target)}</a>`;
    });

    html = html.replace(/\b(Dificuldade|CD)\s+(\d{1,2})\b/gi, (_, label, dc) => {
      return `<span class="dc-chip" onclick="window.setDualityDCAndRoll(${dc})" title="Rolar 2d12 Dualidade vs ${label} ${dc}">🎲 ${label} ${dc}</span>`;
    });

    return html;
  }

  function renderLosslessStructuredRoteiro(roteiroRaw) {
    const lines = String(roteiroRaw || '').split('\n');
    const out = [];
    let inList = false;
    let inTable = false;
    let tableRows = [];

    const closeList = () => { if (inList) { out.push('</ul>'); inList = false; } };
    const closeTable = () => {
      if (inTable && tableRows.length) {
        let tbl = '<div style="overflow-x:auto;margin:8px 0"><table style="width:100%;border-collapse:collapse;font-size:12.5px">';
        tableRows.forEach((r, idx) => {
          if (r.every(c => /^[-:]+$/.test(c))) return;
          const tag = idx === 0 ? 'th' : 'td';
          tbl += '<tr>' + r.map(c => `<${tag} style="border:1px solid #283044;padding:5px 7px;text-align:left;background:${idx === 0 ? '#192030' : '#121622'}">${formatInlineMarkdown(c)}</${tag}>`).join('') + '</tr>';
        });
        tbl += '</table></div>';
        out.push(tbl);
        tableRows = [];
        inTable = false;
      }
    };

    for (let rawLine of lines) {
      const line = rawLine.trim();
      if (!line) {
        closeList();
        closeTable();
        continue;
      }

      if (line.startsWith('|') && line.endsWith('|')) {
        closeList();
        inTable = true;
        tableRows.push(line.slice(1, -1).split('|').map(c => c.trim()));
        continue;
      } else {
        closeTable();
      }

      if (line.startsWith('## ')) {
        closeList();
        out.push(`<h2>${formatInlineMarkdown(line.slice(3))}</h2>`);
      } else if (line.startsWith('### ')) {
        closeList();
        out.push(`<h3>${formatInlineMarkdown(line.slice(4))}</h3>`);
      } else if (line.startsWith('- ')) {
        if (!inList) { out.push('<ul style="margin:5px 0 9px 0;padding-left:18px">'); inList = true; }
        out.push(`<li style="margin-bottom:3px">${formatInlineMarkdown(line.slice(2))}</li>`);
      } else if (line.startsWith('**Para narrar:**') || line.startsWith('**Leitura em voz alta:**')) {
        closeList();
        const plainQuote = line.replace(/^\*\*[^*]+\*\*\s*/, '').replace(/[“”"]/g, '');
        out.push(`
          <div class="callout-block callout-readaloud">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:3px">
              <strong style="color:var(--gold);font-family:var(--font-sans);font-size:11px;text-transform:uppercase">📢 Para Narrar</strong>
              <button class="btn btn-xs btn-project-quote" data-quote="${escapeHtml(plainQuote)}" title="Exibir apenas esta frase de narração no 2º Monitor">📺 Mostrar no 2º Monitor</button>
            </div>
            <div>${formatInlineMarkdown(line)}</div>
          </div>
        `);
      } else if (line.startsWith('**Objetivo:**') || line.startsWith('** Objetivo:**')) {
        closeList();
        out.push(`<div class="callout-block callout-objective">🎯 ${formatInlineMarkdown(line)}</div>`);
      } else if (line.startsWith('**Segredo:**') || line.startsWith('**Armadilha')) {
        closeList();
        out.push(`<div class="callout-block callout-secret">🔒 ${formatInlineMarkdown(line)}</div>`);
      } else if (
        line.startsWith('**Daggerheart:**') ||
        line.startsWith('**DH:**') ||
        line.startsWith('**Conversão DH') ||
        line.startsWith('**Perseguição DH') ||
        line.startsWith('**Coven DH')
      ) {
        closeList();
        out.push(`<div class="callout-block callout-dh">🎲 ${formatInlineMarkdown(line)}</div>`);
      } else if (
        line.startsWith('**Contexto:**') ||
        line.startsWith('**Transição:**') ||
        line.startsWith('**Ao sair:**') ||
        line.startsWith('**Gatilho:**') ||
        line.startsWith('**Desenvolvimento:**')
      ) {
        closeList();
        out.push(`<div class="callout-block callout-trigger">⚡ ${formatInlineMarkdown(line)}</div>`);
      } else {
        closeList();
        out.push(`<p style="margin:6px 0">${formatInlineMarkdown(line)}</p>`);
      }
    }
    closeList();
    closeTable();
    return out.join('\n');
  }

  function selectScene(code) {
    const sc = DATA.scenes.find(s => s.code === code);
    if (!sc) return;
    state.activeSceneCode = sc.code;
    if ($('arcFilterSelect').value !== 'ALL' && $('arcFilterSelect').value !== sc.arc_code) {
      $('arcFilterSelect').value = sc.arc_code;
      state.activeArcCode = sc.arc_code;
      renderArcDeadlines();
    }
    saveState();
    renderSceneList();
    renderActiveScene();
    if (window.baroviaSound && window.baroviaSound.autoPlayOnSceneChange) {
      window.baroviaSound.playSceneAudio(code, false);
    }
  }

  function renderSceneAudioBar(sc) {
    const bar = $('sceneAudioBar');
    const sb = window.baroviaSound;
    if (!bar || !sb || !sc) return;

    const prof = sb.getSceneProfile(sc.code) || sc.audio_profile;
    if (!prof) {
      bar.style.display = 'none';
      return;
    }
    bar.style.display = 'flex';

    const chTags = Object.entries(prof.channels || {}).map(([chId, vol]) => {
      const m = sb.getChannelMeta(chId);
      const isPlaying = sb.activeLoops.has(chId);
      return `<span class="tag" style="${isPlaying ? 'border-color:#34d399;color:#6ee7b7;background:#0d2820' : ''}">${m ? m.icon + ' ' + escapeHtml(m.name) : chId} (${Math.round(vol * 100)}%)</span>`;
    }).join('');

    const sfxBtns = (prof.sfx || []).map(sfxId => {
      const sm = sb.getSfxMeta(sfxId);
      if (!sm) return '';
      return `<button class="btn btn-xs" data-scenesfx="${escapeHtml(sfxId)}" title="Disparar efeito sonoro">${sm.icon} ${escapeHtml(sm.name)}</button>`;
    }).join('');

    const isScenePlaying = sb.activePreset === ('scene:' + sc.code) && sb.activeLoops.size > 0;

    bar.innerHTML = `
      <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
        <button class="btn btn-xs ${isScenePlaying ? 'btn-crimson' : 'btn-gold'}" id="btnInlinePlaySceneAudio">
          ${isScenePlaying ? '⏹ Parar Cena' : '▶ Tocar Trilha da Cena'}
        </button>
        <strong style="font-size:12px;color:var(--gold)">${escapeHtml(prof.name)}</strong>
        ${chTags}
      </div>
      <div style="display:flex;align-items:center;gap:4px;flex-wrap:wrap">
        <span style="font-size:11px;color:var(--text-muted)">Gatilhos:</span>
        ${sfxBtns}
      </div>
    `;

    const playBtn = $('btnInlinePlaySceneAudio');
    if (playBtn) {
      playBtn.onclick = () => {
        if (sb.activePreset === ('scene:' + sc.code) && sb.activeLoops.size > 0) {
          sb.stopAll();
        } else {
          sb.playSceneAudio(sc.code, false);
        }
        renderSceneAudioBar(sc);
      };
    }

    bar.querySelectorAll('[data-scenesfx]').forEach(btn => {
      btn.onclick = () => sb.triggerSFX(btn.dataset.scenesfx);
    });

    const sndSel = $('soundSceneSelect');
    if (sndSel && sndSel.value !== sc.code) {
      sndSel.value = sc.code;
    }
  }

  function renderActiveScene() {
    const sc = getActiveScene();
    if (!sc) return;

    $('activeSceneHeaderCode').textContent = sc.code;
    $('sceneMainTitle').textContent = sc.title;
    $('activeSceneStatusSelect').value = state.sceneStates[sc.code] || sc.status || 'A preparar';

    $('sceneMetaBadges').innerHTML = `
      <span class="tag">Patamar ${sc.tier} · Nív. ${sc.level}</span>
      <span class="tag">${escapeHtml(sc.focus)}</span>
      <span class="tag">🗺️ ${escapeHtml(sc.map_title)}</span>
    `;

    renderSceneAudioBar(sc);

    const arcObj = DATA.arcs.find(a => a.code === sc.arc_code);
    $('sceneArcSummaryBtnWrap').innerHTML = arcObj
      ? `<button class="btn btn-xs" id="btnOpenArcModal">📖 Arco ${escapeHtml(arcObj.code)}</button>`
      : '';
    const arcBtn = $('btnOpenArcModal');
    if (arcBtn && arcObj) {
      arcBtn.onclick = () => openModal(arcObj.title, arcObj.body);
    }

    const encList = sc.encounters || [];
    $('sceneEncCount').textContent = encList.length;

    const container = $('sceneRoteiroContent');
    container.innerHTML = renderLosslessStructuredRoteiro(sc.roteiro_raw || sc.body);

    container.querySelectorAll('.btn-project-quote').forEach(btn => {
      btn.onclick = () => {
        const qText = `“${btn.dataset.quote}”`;
        state.lastQuote = qText;
        broadcastCockpitState({ quote: qText });
      };
    });

    container.querySelectorAll('.wikilink-ref').forEach(a => {
      a.onclick = (e) => {
        e.preventDefault();
        openWikilinkTarget(a.dataset.ref);
      };
    });

    $('sceneMapNotesBody').textContent = sc.mapas_notes || `Mapa: ${sc.map_title}`;
    $('sceneLiveNotes').value = state.sceneNotes[sc.code] || '';
    $('sceneReaderScroll').scrollTop = 0;
  }

  $('activeSceneStatusSelect').onchange = () => {
    const sc = getActiveScene();
    if (!sc) return;
    state.sceneStates[sc.code] = $('activeSceneStatusSelect').value;
    saveState();
    renderSceneList();
  };

  $('sceneLiveNotes').oninput = () => {
    const sc = getActiveScene();
    if (!sc) return;
    state.sceneNotes[sc.code] = $('sceneLiveNotes').value;
    saveState();
  };

  $('btnPrevScene').onclick = () => {
    const idx = DATA.scenes.findIndex(s => s.code === state.activeSceneCode);
    if (idx > 0) selectScene(DATA.scenes[idx - 1].code);
  };

  $('btnNextScene').onclick = () => {
    const idx = DATA.scenes.findIndex(s => s.code === state.activeSceneCode);
    if (idx >= 0 && idx < DATA.scenes.length - 1) selectScene(DATA.scenes[idx + 1].code);
  };

  $('btnSceneOpenMap').onclick = () => {
    const sc = getActiveScene();
    if (!sc) return;
    document.querySelector('[data-tab="tab-atlas"]').click();
    const iframe = $('atlasIframe');
    if (iframe && iframe.contentWindow) {
      iframe.contentWindow.postMessage({ type: 'barovia-select-scene', code: sc.code }, '*');
    }
  };

  $('btnScenePlayAudio').onclick = () => {
    const sc = getActiveScene();
    if (!sc || !window.baroviaSound) return;
    window.baroviaSound.playSceneAudio(sc.code, true);
    renderSceneAudioBar(sc);
  };

  $('btnSceneLoadEncounters').onclick = () => {
    const sc = getActiveScene();
    if (!sc) return;
    const encNames = sc.encounters || [];
    if (!encNames.length) return;
    const found = DATA.encounters.find(e => encNames.includes(e.id) || encNames.includes(e.title));
    if (found) {
      document.querySelector('[data-righttab="rt-combat"]').click();
      $('encounterSelect').value = found.id;
      loadEncounterIntoTracker(found.id);
    }
  };

  // ==========================================================================
  // 5. RIGHT COLUMN: COMBAT TRACKER, PARTY & CLOCKS (FIXED, NO CLIPPING)
  // ==========================================================================
  $('btnCalcThreshold').onclick = () => {
    const dmg = Number($('calcDmgInput').value) || 0;
    const raw = ($('calcThresholdsInput').value || '7/14').split('/').map(x => parseInt(x.trim(), 10));
    const major = raw[0] || 7;
    const severe = raw[1] || 14;
    let label = '1 PV (Menor)';
    if (dmg >= severe) label = `3 PV (Severo ≥${severe})`;
    else if (dmg >= major) label = `2 PV (Maior ≥${major})`;
    else if (dmg <= 0) label = '0 PV';
    $('calcThresholdOutput').textContent = label;
  };

  function initRightSelectors() {
    const encSel = $('encounterSelect');
    encSel.innerHTML = '<option value="">⚔️ Carregar Encontro (86)…</option>';
    DATA.encounters.forEach(enc => {
      const opt = document.createElement('option');
      opt.value = enc.id;
      opt.textContent = `${enc.title} (PB ${enc.bp_active}/${enc.budget_4pc})`;
      encSel.appendChild(opt);
    });
    encSel.onchange = () => {
      if (encSel.value) loadEncounterIntoTracker(encSel.value);
    };

    const bestSel = $('addBestiarySelect');
    bestSel.innerHTML = '<option value="">+ Criatura (152)…</option>';
    DATA.bestiary.forEach(b => {
      const opt = document.createElement('option');
      opt.value = b.id;
      opt.textContent = `${b.title} (Dif ${b.difficulty} · PV ${b.hp})`;
      bestSel.appendChild(opt);
    });

    $('btnAddCreatureToTracker').onclick = () => {
      const bid = bestSel.value;
      if (!bid) return;
      const b = DATA.bestiary.find(x => x.id === bid);
      if (b) addCombatantFromBestiary(b);
    };

    $('btnClearCombatTracker').onclick = () => {
      state.combatants = [];
      state.activeEncounterId = '';
      $('activeEncounterSummary').style.display = 'none';
      saveState();
      renderCombatTracker();
    };

    const ambSel = $('quickAmberSelect');
    ambSel.innerHTML = '';
    DATA.amber_pacts.forEach((p, idx) => {
      const opt = document.createElement('option');
      opt.value = idx;
      opt.textContent = `${p.title} (${p.vestige})`;
      ambSel.appendChild(opt);
    });
    ambSel.onchange = () => renderQuickAmber(Number(ambSel.value));
    renderQuickAmber(0);

    const ruleSel = $('quickRuleSelect');
    ruleSel.innerHTML = '';
    DATA.rules.forEach((r, idx) => {
      const opt = document.createElement('option');
      opt.value = idx;
      opt.textContent = r.title;
      ruleSel.appendChild(opt);
    });
    ruleSel.onchange = () => renderQuickRule(Number(ruleSel.value));
    renderQuickRule(0);
  }

  function addCombatantFromBestiary(b, customRow = null) {
    const hpMax = customRow ? (parseInt(customRow.hp, 10) || b.hp || 5) : (b.hp || 5);
    const stressMax = customRow ? (parseInt(customRow.stress, 10) || b.stress || 3) : (b.stress || 3);
    const thresholds = customRow ? customRow.thresholds : '7 / 14';
    const damage = customRow ? customRow.damage : '';

    state.combatants.push({
      uid: 'c_' + Date.now() + '_' + Math.random().toString(36).slice(2, 6),
      bestiaryId: b.id,
      name: b.title,
      role: customRow ? customRow.role : b.role,
      difficulty: customRow ? customRow.difficulty : b.difficulty,
      thresholds,
      damage,
      hp: 0,
      maxHp: hpMax,
      stress: 0,
      maxStress: stressMax
    });
    saveState();
    renderCombatTracker();
  }

  function loadEncounterIntoTracker(encId) {
    const enc = DATA.encounters.find(e => e.id === encId);
    if (!enc) return;
    state.activeEncounterId = enc.id;
    state.combatants = [];

    const sumBox = $('activeEncounterSummary');
    sumBox.style.display = 'block';
    sumBox.innerHTML = `
      <div style="display:flex;justify-content:space-between;align-items:center;gap:6px">
        <strong style="color:var(--gold);overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${escapeHtml(enc.title)}</strong>
        <button class="btn btn-xs" id="btnViewFullEncounter">📄 Tática</button>
      </div>
      <div style="color:var(--text-muted);margin-top:3px">
        Patamar ${enc.tier} · PB ${enc.bp_active}/${enc.budget_4pc} · Formas: ${enc.forms}
      </div>
    `;
    const btnFull = $('btnViewFullEncounter');
    if (btnFull) {
      btnFull.onclick = () => openModal(enc.title, enc.body);
    }

    if (enc.creatures_table && enc.creatures_table.length) {
      enc.creatures_table.forEach(row => {
        const cleanName = row.sheet.replace(/^\[\[|\]\]$/g, '');
        const b = DATA.bestiary.find(x => x.id === cleanName || x.title === cleanName) || {
          id: cleanName, title: cleanName, role: row.role,
          difficulty: row.difficulty, hp: parseInt(row.hp, 10) || 5, stress: parseInt(row.stress, 10) || 3
        };
        const count = Math.min(8, Math.max(1, parseInt(row.count, 10) || 1));
        for (let i = 0; i < count; i++) {
          addCombatantFromBestiary(Object.assign({}, b, {
            title: count > 1 ? `${b.title} #${i + 1}` : b.title
          }), row);
        }
      });
    } else if (enc.sheets && enc.sheets.length) {
      enc.sheets.forEach(shName => {
        const b = DATA.bestiary.find(x => x.id === shName || x.title === shName);
        if (b) addCombatantFromBestiary(b);
      });
    }
    saveState();
    renderCombatTracker();
  }

  function renderCombatTracker() {
    const container = $('combatTrackerList');
    if (!state.combatants.length) {
      container.innerHTML = `<div style="text-align:center;color:var(--text-muted);padding:16px;font-size:12px">
        Nenhum adversário ativo.<br>Escolha um encontro acima ou clique em <b>⚔️ Encontros</b> na cena.
      </div>`;
      return;
    }

    container.innerHTML = '';
    state.combatants.forEach((c, idx) => {
      const isDead = c.hp >= c.maxHp;
      const card = document.createElement('div');
      card.className = 'combatant-card' + (isDead ? ' dead' : '');

      let hpPips = '';
      for (let i = 1; i <= c.maxHp; i++) {
        hpPips += `<div class="pip-box hp ${i <= c.hp ? 'filled' : ''}" data-cidx="${idx}" data-type="hp" data-val="${i}"></div>`;
      }

      let stressPips = '';
      for (let i = 1; i <= c.maxStress; i++) {
        stressPips += `<div class="pip-box stress ${i <= c.stress ? 'filled' : ''}" data-cidx="${idx}" data-type="stress" data-val="${i}"></div>`;
      }

      card.innerHTML = `
        <div style="display:flex;justify-content:space-between;align-items:center;gap:6px;min-width:0">
          <strong style="color:${isDead ? '#f87171' : 'var(--gold)'};font-size:13px;cursor:pointer;overflow:hidden;text-overflow:ellipsis;white-space:nowrap" data-openbestiary="${escapeHtml(c.bestiaryId)}">
            ${isDead ? '💀 ' : ''}${escapeHtml(c.name)}
          </strong>
          <div style="display:flex;gap:4px;flex-shrink:0">
            <button class="btn btn-xs" data-openbestiary="${escapeHtml(c.bestiaryId)}" title="Ficha">📜</button>
            <button class="btn btn-xs" data-delcomb="${idx}" title="Remover">✖</button>
          </div>
        </div>
        <div style="font-size:11.5px;color:var(--text-muted);margin-top:2px">
          Dif <b style="color:#fff">${escapeHtml(c.difficulty)}</b> · Lim <b style="color:#fde68a">${escapeHtml(c.thresholds)}</b> · ${escapeHtml(c.role)}
        </div>
        <div class="pip-row">
          <span class="pip-label" style="color:#fca5a5">PV ${c.hp}/${c.maxHp}</span>
          ${hpPips}
        </div>
        <div class="pip-row">
          <span class="pip-label" style="color:#d8b4fe">Est ${c.stress}/${c.maxStress}</span>
          ${stressPips}
        </div>
        <div class="threshold-bar">
          <button class="thresh-btn" data-hit="${idx}" data-dmg="1">+1 PV (Menor)</button>
          <button class="thresh-btn" data-hit="${idx}" data-dmg="2">+2 PV (Maior)</button>
          <button class="thresh-btn" data-hit="${idx}" data-dmg="3">+3 PV (Severo)</button>
        </div>
      `;
      container.appendChild(card);
    });

    container.querySelectorAll('.pip-box').forEach(pip => {
      pip.onclick = () => {
        const c = state.combatants[Number(pip.dataset.cidx)];
        const val = Number(pip.dataset.val);
        const type = pip.dataset.type;
        c[type] = (c[type] === val) ? val - 1 : val;
        saveState();
        renderCombatTracker();
      };
    });

    container.querySelectorAll('[data-hit]').forEach(btn => {
      btn.onclick = () => {
        const c = state.combatants[Number(btn.dataset.hit)];
        c.hp = Math.min(c.maxHp, c.hp + Number(btn.dataset.dmg));
        saveState();
        renderCombatTracker();
      };
    });

    container.querySelectorAll('[data-delcomb]').forEach(btn => {
      btn.onclick = () => {
        state.combatants.splice(Number(btn.dataset.delcomb), 1);
        saveState();
        renderCombatTracker();
      };
    });

    container.querySelectorAll('[data-openbestiary]').forEach(el => {
      el.onclick = () => {
        const bid = el.dataset.openbestiary;
        const b = DATA.bestiary.find(x => x.id === bid || x.title === bid);
        if (b) openModal(b.title, b.body);
      };
    });
  }

  function renderPartyTracker() {
    const container = $('partyTrackerList');
    container.innerHTML = '';
    state.party.forEach((pc, idx) => {
      const card = document.createElement('div');
      card.className = 'combatant-card';

      let hpPips = '', stressPips = '', hopePips = '', corrPips = '';
      for (let i = 1; i <= pc.maxHp; i++) hpPips += `<div class="pip-box hp ${i <= pc.hp ? 'filled' : ''}" data-pc="${idx}" data-field="hp" data-val="${i}"></div>`;
      for (let i = 1; i <= pc.maxStress; i++) stressPips += `<div class="pip-box stress ${i <= pc.stress ? 'filled' : ''}" data-pc="${idx}" data-field="stress" data-val="${i}"></div>`;
      for (let i = 1; i <= 6; i++) hopePips += `<div class="pip-box hope ${i <= pc.hope ? 'filled' : ''}" data-pc="${idx}" data-field="hope" data-val="${i}"></div>`;
      for (let i = 1; i <= 6; i++) corrPips += `<div class="pip-box corrupt ${i <= pc.corruption ? 'filled' : ''}" data-pc="${idx}" data-field="corruption" data-val="${i}"></div>`;

      card.innerHTML = `
        <div style="display:flex;justify-content:space-between;align-items:center">
          <strong style="color:var(--gold);font-size:12.5px;cursor:pointer" data-editpc="${idx}">🛡️ ${escapeHtml(pc.name)}</strong>
          <span class="tag">Ev ${pc.evasion} · Lim ${escapeHtml(pc.thresholds)}</span>
        </div>
        <div class="pip-row"><span class="pip-label" style="color:#fde68a">Esp ${pc.hope}/6</span>${hopePips}</div>
        <div class="pip-row"><span class="pip-label" style="color:#fca5a5">PV ${pc.hp}/${pc.maxHp}</span>${hpPips}</div>
        <div class="pip-row"><span class="pip-label" style="color:#d8b4fe">Est ${pc.stress}/${pc.maxStress}</span>${stressPips}</div>
        <div class="pip-row"><span class="pip-label" style="color:#fdba74">Âmb ${pc.corruption}/6</span>${corrPips}</div>
      `;
      container.appendChild(card);
    });

    container.querySelectorAll('.pip-box').forEach(pip => {
      pip.onclick = () => {
        const pc = state.party[Number(pip.dataset.pc)];
        const f = pip.dataset.field;
        const v = Number(pip.dataset.val);
        pc[f] = (pc[f] === v) ? v - 1 : v;
        saveState();
        renderPartyTracker();
      };
    });

    container.querySelectorAll('[data-editpc]').forEach(el => {
      el.onclick = () => {
        const pc = state.party[Number(el.dataset.editpc)];
        const name = prompt('Nome do PJ:', pc.name);
        if (name) pc.name = name;
        const thresh = prompt('Limiares Maior/Severo:', pc.thresholds);
        if (thresh) pc.thresholds = thresh;
        saveState();
        renderPartyTracker();
      };
    });
  }

  $('btnAddPartyMember').onclick = () => {
    const name = prompt('Nome do PJ:', `PJ ${state.party.length + 1}`);
    if (!name) return;
    state.party.push({
      id: 'pc_' + Date.now(), name, relic: '', evasion: 10, thresholds: '7/14',
      hp: 0, maxHp: 6, stress: 0, maxStress: 6, hope: 2, corruption: 0
    });
    saveState();
    renderPartyTracker();
  };

  function renderClocks() {
    const container = $('clocksContainer');
    container.innerHTML = '';
    state.clocks.forEach((clk, idx) => {
      const card = document.createElement('div');
      card.className = 'clock-card';
      const pct = Math.max(0, Math.min(100, Math.round((clk.current / Math.max(1, clk.max)) * 100)));

      let visualHtml = '';
      if (clk.max <= 16) {
        let segsHtml = '';
        for (let s = 1; s <= clk.max; s++) {
          segsHtml += `<div class="clock-seg ${s <= clk.current ? 'filled' : ''}" data-idx="${idx}" data-val="${s}"></div>`;
        }
        visualHtml = `<div class="clock-segments">${segsHtml}</div>`;
      } else {
        visualHtml = `
          <div class="clock-bar-large" data-baridx="${idx}" title="Clique na barra para ajustar proporcionalmente (${pct}%)" style="position:relative;height:16px;background:#10141f;border:1px solid #353f58;border-radius:6px;overflow:hidden;cursor:pointer;margin-top:6px">
            <div style="width:${pct}%;height:100%;background:linear-gradient(90deg,#d97706 0%,#fbbf24 100%);transition:width .15s"></div>
            <span style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:10.5px;font-weight:700;color:#fff;text-shadow:0 1px 3px #000">${clk.current} / ${clk.max} (${pct}%)</span>
          </div>
        `;
      }

      card.innerHTML = `
        <div style="display:flex;justify-content:space-between;align-items:center;gap:6px;flex-wrap:wrap">
          <div style="display:flex;align-items:center;gap:6px;min-width:0">
            <strong style="font-size:12.5px;cursor:pointer;color:var(--gold)" data-editclkname="${idx}" title="Clique para renomear">${escapeHtml(clk.name)}</strong>
            <span class="tag" style="cursor:pointer;font-weight:700;color:#fde68a" data-editclkval="${idx}" title="Clique para digitar o valor atual ou máximo">${clk.current}/${clk.max}</span>
          </div>
          <div style="display:flex;gap:3px;align-items:center">
            <button class="btn btn-xs" data-stepclk="${idx}" data-delta="-5" title="-5">-5</button>
            <button class="btn btn-xs" data-stepclk="${idx}" data-delta="-1" title="-1">-1</button>
            <button class="btn btn-xs btn-gold" data-stepclk="${idx}" data-delta="1" title="+1">+1</button>
            <button class="btn btn-xs" data-stepclk="${idx}" data-delta="5" title="+5">+5</button>
            <button class="btn btn-xs" data-togglepub="${idx}" title="Mostrar ou ocultar no 2º Monitor">${clk.public ? '👁️ 2º Mon.' : '🔒'}</button>
            <button class="btn btn-xs" data-delclock="${idx}" title="Excluir contador">✖</button>
          </div>
        </div>
        ${visualHtml}
      `;
      container.appendChild(card);
    });

    container.querySelectorAll('.clock-seg').forEach(el => {
      el.onclick = () => {
        const i = Number(el.dataset.idx);
        const v = Number(el.dataset.val);
        state.clocks[i].current = (state.clocks[i].current === v) ? v - 1 : v;
        saveState();
        renderClocks();
      };
    });

    container.querySelectorAll('.clock-bar-large').forEach(bar => {
      bar.onclick = (e) => {
        const i = Number(bar.dataset.baridx);
        const clk = state.clocks[i];
        const rect = bar.getBoundingClientRect();
        const ratio = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
        clk.current = Math.round(ratio * clk.max);
        saveState();
        renderClocks();
      };
    });

    container.querySelectorAll('[data-stepclk]').forEach(btn => {
      btn.onclick = () => {
        const i = Number(btn.dataset.stepclk);
        const delta = Number(btn.dataset.delta);
        const clk = state.clocks[i];
        clk.current = Math.max(0, Math.min(clk.max, clk.current + delta));
        saveState();
        renderClocks();
      };
    });

    container.querySelectorAll('[data-editclkname]').forEach(el => {
      el.onclick = () => {
        const i = Number(el.dataset.editclkname);
        const newName = prompt('Nome do Relógio / Contador:', state.clocks[i].name);
        if (newName && newName.trim()) {
          state.clocks[i].name = newName.trim();
          saveState();
          renderClocks();
        }
      };
    });

    container.querySelectorAll('[data-editclkval]').forEach(el => {
      el.onclick = () => {
        const i = Number(el.dataset.editclkval);
        const clk = state.clocks[i];
        const input = prompt('Digite "Atual/Máximo" (ex: 18/30 ou 45/100) ou apenas o novo valor atual:', `${clk.current}/${clk.max}`);
        if (!input || !input.trim()) return;
        if (input.includes('/')) {
          const parts = input.split('/');
          const nMax = Math.max(1, parseInt(parts[1], 10) || clk.max);
          const nCur = Math.max(0, Math.min(nMax, parseInt(parts[0], 10) || 0));
          clk.max = nMax;
          clk.current = nCur;
        } else {
          const nCur = Math.max(0, parseInt(input, 10) || 0);
          if (nCur > clk.max) clk.max = nCur;
          clk.current = nCur;
        }
        saveState();
        renderClocks();
      };
    });

    container.querySelectorAll('[data-togglepub]').forEach(btn => {
      btn.onclick = () => {
        const i = Number(btn.dataset.togglepub);
        state.clocks[i].public = !state.clocks[i].public;
        saveState();
        renderClocks();
      };
    });

    container.querySelectorAll('[data-delclock]').forEach(btn => {
      btn.onclick = () => {
        state.clocks.splice(Number(btn.dataset.delclock), 1);
        saveState();
        renderClocks();
      };
    });
  }

  $('btnAddClock').onclick = () => {
    const name = prompt('Nome do Relógio ou Contador:', 'Progresso / Contador');
    if (!name) return;
    const maxInput = prompt('Valor Máximo (qualquer número: ex. 6, 12, 20, 30, 50, 100):', '20');
    const max = Math.max(1, parseInt(maxInput, 10) || 20);
    state.clocks.push({ id: 'clk_' + Date.now(), name, current: 0, max, public: true });
    saveState();
    renderClocks();
  };

  function renderArcDeadlines() {
    const container = $('arcDeadlinesContainer');
    const arcCode = $('arcFilterSelect').value;
    const relevant = DATA.calendar.filter(d => {
      if (!arcCode || arcCode === 'ALL') return true;
      return (d.arcs || []).some(a => a.startsWith(arcCode + ' ') || a.startsWith(arcCode + '·'));
    });

    if (!relevant.length) {
      container.innerHTML = '<div style="font-size:12px;color:var(--text-muted)">Nenhum prazo neste arco.</div>';
      return;
    }

    container.innerHTML = relevant.map(d => `
      <div class="stack-box" style="font-size:12px">
        <div style="display:flex;justify-content:space-between;font-weight:700;color:#fda4af">
          <span>⏰ ${escapeHtml(d.title)}</span>
          <span class="tag">${escapeHtml(d.when || d.priority)}</span>
        </div>
        <div style="color:var(--text-muted);margin-top:3px">${escapeHtml(d.trigger || d.consequence)}</div>
      </div>
    `).join('');
  }

  function renderQuickAmber(idx) {
    const p = DATA.amber_pacts[idx];
    if (!p) return;
    $('quickAmberDetail').innerHTML = `
      <strong style="color:var(--gold)">${escapeHtml(p.title)} · ${escapeHtml(p.vestige)}</strong>
      <div style="white-space:pre-wrap;margin-top:4px">${formatInlineMarkdown(p.body)}</div>
    `;
  }

  function renderQuickRule(idx) {
    const r = DATA.rules[idx];
    if (!r) return;
    $('quickRuleDetail').innerHTML = `
      <strong style="color:var(--gold)">${escapeHtml(r.title)}</strong>
      <div style="white-space:pre-wrap;margin-top:4px">${formatInlineMarkdown(r.body)}</div>
    `;
  }

  // ==========================================================================
  // 6. SOUNDBOARD UI (46 REAL MP3 TRACKS + 180 SCENE PROFILES)
  // ==========================================================================
  function initSoundboardUI() {
    const sb = window.baroviaSound;
    if (!sb) return;

    // Populate the 180-scene audio selector
    const sndSceneSel = $('soundSceneSelect');
    const sndSceneSfxWrap = $('soundSceneRecommendedSfx');
    if (sndSceneSel) {
      sndSceneSel.innerHTML = '';
      DATA.scenes.forEach(sc => {
        const prof = sb.getSceneProfile(sc.code);
        const opt = document.createElement('option');
        opt.value = sc.code;
        opt.textContent = `${sc.code} · ${prof ? prof.name : sc.title}`;
        sndSceneSel.appendChild(opt);
      });
      sndSceneSel.value = state.activeSceneCode || 'A1';

      const updateRecommendedSfxInTab = () => {
        const code = sndSceneSel.value;
        const prof = sb.getSceneProfile(code);
        if (!sndSceneSfxWrap || !prof) return;
        sndSceneSfxWrap.innerHTML = (prof.sfx || []).map(sfxId => {
          const sm = sb.getSfxMeta(sfxId);
          return sm ? `<button class="btn btn-xs" data-tabsfx="${escapeHtml(sfxId)}">${sm.icon} ${escapeHtml(sm.name)}</button>` : '';
        }).join('');
        sndSceneSfxWrap.querySelectorAll('[data-tabsfx]').forEach(b => {
          b.onclick = () => sb.triggerSFX(b.dataset.tabsfx);
        });
      };

      sndSceneSel.onchange = () => {
        updateRecommendedSfxInTab();
        sb.playSceneAudio(sndSceneSel.value, false);
      };

      const btnPlaySel = $('btnPlaySelectedSceneAudio');
      if (btnPlaySel) {
        btnPlaySel.onclick = () => sb.playSceneAudio(sndSceneSel.value, true);
      }

      updateRecommendedSfxInTab();
    }

    const chkAuto = $('chkAutoSceneAudio');
    if (chkAuto) {
      chkAuto.checked = Boolean(sb.autoPlayOnSceneChange);
      chkAuto.onchange = () => {
        sb.autoPlayOnSceneChange = chkAuto.checked;
      };
    }

    const pGrid = $('soundPresetsGrid');
    pGrid.innerHTML = Object.entries(sb.presets).map(([k, p]) => `
      <button class="btn btn-xs" data-preset="${k}">${escapeHtml(p.name)}</button>
    `).join('');
    pGrid.querySelectorAll('[data-preset]').forEach(btn => {
      btn.onclick = () => sb.applyPreset(btn.dataset.preset, true);
    });

    const renderChannelGroup = (list, containerId) => {
      const el = $(containerId);
      el.innerHTML = list.map(ch => `
        <div class="sound-channel" id="sndcard_${ch.id}">
          <div style="display:flex;justify-content:space-between;align-items:center">
            <strong style="color:var(--gold);font-size:13px">${ch.icon} ${escapeHtml(ch.name)}</strong>
            <button class="btn btn-xs" data-togglech="${ch.id}" id="sndbtn_${ch.id}">▶</button>
          </div>
          <input type="range" min="0" max="1" step="0.02" value="${ch.defaultVol}" data-volch="${ch.id}" id="sndvol_${ch.id}" style="width:100%">
          <input type="file" accept="audio/*" data-filech="${ch.id}" style="font-size:10px" title="Substituir por outro arquivo de áudio local (opcional)">
        </div>
      `).join('');

      el.querySelectorAll('[data-togglech]').forEach(btn => {
        btn.onclick = () => {
          const id = btn.dataset.togglech;
          sb.toggleChannel(id, Number($(`sndvol_${id}`).value) || 0.5);
        };
      });
      el.querySelectorAll('[data-volch]').forEach(rng => {
        rng.oninput = () => sb.setChannelVolume(rng.dataset.volch, Number(rng.value));
      });
      el.querySelectorAll('[data-filech]').forEach(inp => {
        inp.onchange = (e) => {
          if (e.target.files[0]) sb.attachCustomFile(inp.dataset.filech, e.target.files[0]);
        };
      });
    };

    renderChannelGroup(sb.ambientChannels, 'ambientChannelsGrid');
    renderChannelGroup(sb.musicChannels, 'musicChannelsGrid');

    const sfxEl = $('sfxPadsGrid');
    sfxEl.innerHTML = sb.sfxPads.map(pad => `
      <button class="sfx-pad" data-sfx="${pad.id}">
        <span>${pad.icon}</span>
        <span>${escapeHtml(pad.name)}</span>
      </button>
    `).join('');
    sfxEl.querySelectorAll('[data-sfx]').forEach(btn => {
      btn.onclick = () => sb.triggerSFX(btn.dataset.sfx);
    });

    $('masterVolSlider').oninput = (e) => {
      const v = Number(e.target.value);
      $('masterVolText').textContent = Math.round(v * 100) + '%';
      sb.setMasterVolume(v);
    };

    $('btnStopAllAudio').onclick = () => sb.stopAll();
    $('btnMiniMute').onclick = () => sb.stopAll();

    window.onSoundboardStateChange = () => {
      [...sb.ambientChannels, ...sb.musicChannels].forEach(ch => {
        const card = $(`sndcard_${ch.id}`);
        const btn = $(`sndbtn_${ch.id}`);
        const volSlider = $(`sndvol_${ch.id}`);
        const playing = sb.activeLoops.has(ch.id);
        if (card) card.classList.toggle('playing', playing);
        if (btn) btn.textContent = playing ? '⏹' : '▶';
        if (playing && volSlider) {
          volSlider.value = sb.activeLoops.get(ch.id).volume;
        }
      });
      const count = sb.activeLoops.size;
      $('btnMiniMute').style.display = count > 0 ? 'inline-flex' : 'none';
      $('miniAudioCount').textContent = count;
      const sc = getActiveScene();
      if (sc) renderSceneAudioBar(sc);
    };
  }

  // ==========================================================================
  // 7. CATALOGS & MODAL WITH ANTI-SPOILER DRAWER
  // ==========================================================================
  function renderCatalog() {
    const q = ($('catalogSearchInput').value || '').trim().toLowerCase();
    const list = DATA[currentCatalogType] || [];
    const filtered = list.filter(item => !q || JSON.stringify(item).toLowerCase().includes(q));

    const grid = $('catalogGridContainer');
    grid.innerHTML = filtered.slice(0, 120).map(item => {
      if (currentCatalogType === 'bestiary') {
        return `<div class="cat-card">
          <div style="display:flex;justify-content:space-between;gap:6px">
            <strong style="color:var(--gold)">👹 ${escapeHtml(item.title)}</strong>
            <span class="tag">Pat. ${item.tier}</span>
          </div>
          <div style="font-size:12px;color:var(--text-muted)">Dif ${item.difficulty} · PV ${item.hp} · Est ${item.stress} · ${escapeHtml(item.role)}</div>
          <div style="display:flex;gap:6px;margin-top:auto;padding-top:4px">
            <button class="btn btn-xs" data-catopen="${escapeHtml(item.id)}">📜 Ficha</button>
            <button class="btn btn-xs btn-crimson" data-catcombat="${escapeHtml(item.id)}">+ Combate</button>
          </div>
        </div>`;
      } else if (currentCatalogType === 'encounters') {
        return `<div class="cat-card">
          <strong style="color:var(--gold)">⚔️ ${escapeHtml(item.title)}</strong>
          <div style="font-size:12px;color:var(--text-muted)">Patamar ${item.tier} · PB ${item.bp_active}/${item.budget_4pc}</div>
          <div style="display:flex;gap:6px;margin-top:auto;padding-top:4px">
            <button class="btn btn-xs" data-catopen="${escapeHtml(item.id)}">📜 Tática</button>
            <button class="btn btn-xs btn-crimson" data-catloadenc="${escapeHtml(item.id)}">⚔️ Usar na Sessão</button>
          </div>
        </div>`;
      } else {
        return `<div class="cat-card">
          <strong style="color:var(--gold)">${escapeHtml(item.title)}</strong>
          <div style="font-size:12px;color:var(--text-muted)">${escapeHtml(item.category || item.vestige || item.when || '')}</div>
          <div style="margin-top:auto;padding-top:4px">
            <button class="btn btn-xs" data-catopen="${escapeHtml(item.id)}">📖 Ler</button>
          </div>
        </div>`;
      }
    }).join('');

    grid.querySelectorAll('[data-catopen]').forEach(btn => {
      btn.onclick = () => {
        const item = list.find(x => x.id === btn.dataset.catopen || x.title === btn.dataset.catopen);
        if (item) openModal(item.title, item.body);
      };
    });

    grid.querySelectorAll('[data-catcombat]').forEach(btn => {
      btn.onclick = () => {
        const b = DATA.bestiary.find(x => x.id === btn.dataset.catcombat);
        if (b) {
          addCombatantFromBestiary(b);
          document.querySelector('[data-tab="tab-cockpit"]').click();
        }
      };
    });

    grid.querySelectorAll('[data-catloadenc]').forEach(btn => {
      btn.onclick = () => {
        loadEncounterIntoTracker(btn.dataset.catloadenc);
        document.querySelector('[data-tab="tab-cockpit"]').click();
      };
    });
  }

  document.querySelectorAll('.cat-type-btn').forEach(btn => {
    btn.onclick = () => {
      document.querySelectorAll('.cat-type-btn').forEach(b => b.classList.remove('btn-gold'));
      btn.classList.add('btn-gold');
      currentCatalogType = btn.dataset.cattype;
      renderCatalog();
    };
  });
  $('catalogSearchInput').oninput = renderCatalog;

  function openWikilinkTarget(ref) {
    const clean = String(ref || '').split('|')[0].trim();
    const sc = DATA.scenes.find(s => s.id === clean || s.title === clean || s.code === clean);
    if (sc) { selectScene(sc.code); return; }
    for (const key of ['bestiary', 'encounters', 'items_spells', 'amber_pacts', 'calendar', 'rules', 'arcs']) {
      const found = (DATA[key] || []).find(x => x.id === clean || x.title === clean);
      if (found) { openModal(found.title, found.body); return; }
    }
    const mp = DATA.maps.find(m => m.title === clean);
    if (mp) {
      document.querySelector('[data-tab="tab-atlas"]').click();
      const iframe = $('atlasIframe');
      if (iframe && iframe.contentWindow) {
        iframe.contentWindow.postMessage({ type: 'barovia-select-map', key: mp.key }, '*');
      }
    }
  }

  function openModal(title, rawBody) {
    $('modalTitle').textContent = title;
    $('modalBodyContent').innerHTML = `<div style="white-space:pre-wrap">${formatInlineMarkdown(rawBody)}</div>`;
    $('modalPlayerSafeBox').style.display = 'none';

    // Prepare sanitized anti-spoiler defaults in case GM wants to project
    const publicTitle = String(title || '').replace(/^[^·]+·\s*/, '');
    $('safeProjectTitle').value = publicTitle;
    $('safeProjectText').value = extractPlayerSafeText(rawBody);

    $('detailModal').classList.add('open');
  }

  $('btnTogglePlayerPreview').onclick = () => {
    const box = $('modalPlayerSafeBox');
    box.style.display = box.style.display === 'none' ? 'block' : 'none';
  };

  $('btnConfirmSafeProject').onclick = () => {
    const t = ($('safeProjectTitle').value || '').trim();
    const txt = ($('safeProjectText').value || '').trim();
    if (!t && !txt) return;
    broadcastCockpitState({ handout: { title: t, text: txt } });
    $('modalPlayerSafeBox').style.display = 'none';
  };

  $('btnCloseModal').onclick = () => $('detailModal').classList.remove('open');
  $('detailModal').onclick = (e) => { if (e.target === $('detailModal')) $('detailModal').classList.remove('open'); };

  function generateSessionMarkdownLog() {
    const sc = getActiveScene();
    const doneScenes = Object.entries(state.sceneStates).filter(([, st]) => st === 'Concluída').map(([c]) => c);
    const notesEntries = Object.entries(state.sceneNotes).filter(([, txt]) => txt && txt.trim());

    const md = [
      `# Registro de Sessão · Strahd Reloaded (Daggerheart)`,
      `**Data:** ${new Date().toLocaleDateString('pt-BR')} · **Cena Atual:** ${sc ? sc.title : ''} · **Medo:** ${state.fear}/12`,
      ``,
      `## Cenas Concluídas`,
      doneScenes.length ? doneScenes.join(', ') : 'Nenhuma marcada como concluída.',
      ``,
      `## Anotações por Cena`,
      notesEntries.length ? notesEntries.map(([code, txt]) => `### ${code}\n${txt}`).join('\n\n') : 'Sem notas.',
      ``,
      `## Relógios`,
      ...state.clocks.map(c => `- **${c.name}:** ${c.current}/${c.max}`),
      ``,
      `## Grupo (PJs)`,
      ...state.party.map(p => `- **${p.name}:** Esp ${p.hope}/6 · PV ${p.hp}/${p.maxHp} · Est ${p.stress}/${p.maxStress} · Âmbar ${p.corruption}/6`)
    ].join('\n');

    $('sessionLogOutput').value = md;
    return md;
  }

  $('btnRefreshSessionLog').onclick = generateSessionMarkdownLog;
  $('btnCopySessionLog').onclick = () => {
    navigator.clipboard?.writeText(generateSessionMarkdownLog());
    $('btnCopySessionLog').textContent = '✅ Copiado';
    setTimeout(() => { $('btnCopySessionLog').textContent = '📋 Copiar Markdown'; }, 1800);
  };

  // Initialize
  renderFearBar();
  initArcSelect();
  renderSceneList();
  renderClocks();
  renderArcDeadlines();
  renderActiveScene();
  initRightSelectors();
  renderCombatTracker();
  renderPartyTracker();
  initSoundboardUI();
  renderCatalog();
})();
