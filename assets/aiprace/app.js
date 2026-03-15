/**
 * AI Expozice české ekonomiky — D3.js Treemap Visualization
 *
 * Interactive treemap where:
 * - Area = number of employees (FTE)
 * - Color = composite AI exposure score (green=safe, red=exposed)
 * - Sliders adjust Triáda weights in real-time
 */

(function () {
  "use strict";

  // ── State ──────────────────────────────────────────────────────────
  let data = null;
  let weights = { tok: 0.4, tes: 0.35, tol: 0.25 };
  const DEFAULT_WEIGHTS = { tok: 0.4, tes: 0.35, tol: 0.25 };

  // ── Color scale: green (low exposure) → red (high exposure) ──────
  const exposureColor = d3.scaleSequential()
    .domain([0, 10])
    .interpolator(t => {
      // Custom green → yellow → orange → red
      if (t < 0.25) return d3.interpolateRgb("#2e7d32", "#689f38")(t / 0.25);
      if (t < 0.5) return d3.interpolateRgb("#689f38", "#f9a825")((t - 0.25) / 0.25);
      if (t < 0.75) return d3.interpolateRgb("#f9a825", "#ef6c00")((t - 0.5) / 0.25);
      return d3.interpolateRgb("#ef6c00", "#c62828")((t - 0.75) / 0.25);
    });

  const barColor = (score) => {
    if (score <= 3) return "#4caf50";
    if (score <= 6) return "#ffc107";
    return "#f44336";
  };

  // ── Formatting ─────────────────────────────────────────────────────
  const fmtNum = (n) => {
    if (n == null) return "—";
    if (n >= 1000000) return (n / 1000000).toFixed(1) + "M";
    if (n >= 1000) return Math.round(n).toLocaleString("cs-CZ");
    return String(n);
  };

  const fmtCZK = (n) => {
    if (n == null) return "—";
    return Math.round(n).toLocaleString("cs-CZ") + " Kč";
  };

  // ── Compute exposure from Triáda scores ────────────────────────────
  function computeExposure(occ) {
    if (occ.tokenizovatelnost == null) return null;
    return +(
      weights.tok * occ.tokenizovatelnost +
      weights.tes * occ.testovatelnost +
      weights.tol * occ.tolerance_k_chybe
    ).toFixed(1);
  }

  // ── Load data ──────────────────────────────────────────────────────
  async function loadData() {
    try {
      const resp = await fetch("/assets/aiprace/data.json");
      if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
      data = await resp.json();
      init();
    } catch (err) {
      document.getElementById("treemap").innerHTML =
        `<div style="padding:2rem;color:#ef5350;">
          <h3>Data nenalezena</h3>
          <p>Soubor <code>site/data.json</code> nebyl nalezen.
          Spusťte nejprve datovou pipeline (skripty 01–07).</p>
          <pre style="margin-top:1rem;color:#a0a8b8;font-size:0.8rem;">${err.message}</pre>
        </div>`;
    }
  }

  // ── Initialize ─────────────────────────────────────────────────────
  function init() {
    updateStats();
    setupSliders();
    renderTreemap();
    renderCohorts();
    renderSectors();
    setupSearch();
    setupDetailPanel();
    window.addEventListener("resize", debounce(renderTreemap, 250));
  }

  // ── Stats bar ──────────────────────────────────────────────────────
  function updateStats() {
    const meta = data.metadata;
    const occs = data.occupations;

    document.getElementById("stat-total-employees").textContent =
      fmtNum(meta.total_employees);
    document.getElementById("stat-occupations").textContent =
      meta.total_occupations;

    // Recalculate weighted average with current weights
    let totalFte = 0;
    let weightedSum = 0;
    for (const occ of occs) {
      const exp = computeExposure(occ);
      if (exp != null) {
        weightedSum += exp * occ.fte_thous;
        totalFte += occ.fte_thous;
      }
    }
    const avgExp = totalFte > 0 ? (weightedSum / totalFte).toFixed(1) : "—";
    document.getElementById("stat-avg-exposure").textContent = avgExp;
  }

  // ── Sliders ────────────────────────────────────────────────────────
  function setupSliders() {
    const sliderTok = document.getElementById("w-tok");
    const sliderTes = document.getElementById("w-tes");
    const sliderTol = document.getElementById("w-tol");

    function onSliderChange() {
      const raw = {
        tok: +sliderTok.value,
        tes: +sliderTes.value,
        tol: +sliderTol.value,
      };
      const sum = raw.tok + raw.tes + raw.tol || 1;
      weights.tok = raw.tok / sum;
      weights.tes = raw.tes / sum;
      weights.tol = raw.tol / sum;

      document.getElementById("w-tok-val").textContent = Math.round(weights.tok * 100) + "%";
      document.getElementById("w-tes-val").textContent = Math.round(weights.tes * 100) + "%";
      document.getElementById("w-tol-val").textContent = Math.round(weights.tol * 100) + "%";

      updateColors();
      updateStats();
      renderCohorts();
      renderSectors();
    }

    sliderTok.addEventListener("input", onSliderChange);
    sliderTes.addEventListener("input", onSliderChange);
    sliderTol.addEventListener("input", onSliderChange);

    document.getElementById("reset-weights").addEventListener("click", () => {
      sliderTok.value = DEFAULT_WEIGHTS.tok * 100;
      sliderTes.value = DEFAULT_WEIGHTS.tes * 100;
      sliderTol.value = DEFAULT_WEIGHTS.tol * 100;
      onSliderChange();
    });
  }

  // ── Treemap ────────────────────────────────────────────────────────
  function renderTreemap() {
    const container = document.getElementById("treemap");
    container.innerHTML = "";

    const width = container.clientWidth;
    const height = Math.max(600, window.innerHeight - 350);
    container.style.height = height + "px";

    // Build hierarchy from data
    const hierarchy = data.hierarchy;
    const root = d3.hierarchy(hierarchy)
      .sum(d => d.employees || 0)
      .sort((a, b) => (b.value || 0) - (a.value || 0));

    d3.treemap()
      .size([width, height])
      .padding(1)
      .paddingTop(18)
      .paddingInner(1)
      .round(true)
      .tile(d3.treemapSquarify.ratio(1.5))
      (root);

    // Render group labels
    for (const group of root.children || []) {
      const label = document.createElement("div");
      label.className = "treemap-group-label";
      label.style.left = group.x0 + "px";
      label.style.top = group.y0 + "px";
      label.style.width = (group.x1 - group.x0) + "px";
      label.textContent = group.data.name;
      container.appendChild(label);
    }

    // Render leaf cells
    const leaves = root.leaves();
    for (const leaf of leaves) {
      const d = leaf.data;
      const w = leaf.x1 - leaf.x0;
      const h = leaf.y1 - leaf.y0;

      if (w < 2 || h < 2) continue;

      const cell = document.createElement("div");
      cell.className = "treemap-cell";
      cell.style.left = leaf.x0 + "px";
      cell.style.top = leaf.y0 + "px";
      cell.style.width = w + "px";
      cell.style.height = h + "px";

      const exposure = computeExposure(d);
      cell.style.backgroundColor = exposure != null
        ? exposureColor(exposure)
        : "#3a3a5e";

      cell.dataset.code = d.code || "";

      // Label (only if cell is large enough)
      if (w > 40 && h > 18) {
        const label = document.createElement("div");
        label.className = "treemap-cell-label";
        label.textContent = d.name || "";
        cell.appendChild(label);

        // Sub-label with exposure score
        if (w > 60 && h > 32 && exposure != null) {
          const sub = document.createElement("div");
          sub.className = "treemap-cell-sub";
          sub.textContent = `${exposure}/10 · ${fmtNum(d.employees)}`;
          cell.appendChild(sub);
        }
      }

      // Events
      cell.addEventListener("mouseenter", (e) => showTooltip(e, d));
      cell.addEventListener("mousemove", moveTooltip);
      cell.addEventListener("mouseleave", hideTooltip);
      cell.addEventListener("click", () => showDetail(d));

      container.appendChild(cell);
    }
  }

  // ── Update colors (when weights change) ────────────────────────────
  function updateColors() {
    const cells = document.querySelectorAll(".treemap-cell");
    const codeToOcc = {};
    for (const occ of data.occupations) {
      codeToOcc[occ.code] = occ;
    }

    for (const cell of cells) {
      const code = cell.dataset.code;
      const occ = codeToOcc[code];
      if (!occ) continue;
      const exposure = computeExposure(occ);
      cell.style.backgroundColor = exposure != null
        ? exposureColor(exposure)
        : "#3a3a5e";

      // Update sub-label if exists
      const sub = cell.querySelector(".treemap-cell-sub");
      if (sub && exposure != null) {
        sub.textContent = `${exposure}/10 · ${fmtNum(occ.employees)}`;
      }
    }
  }

  // ── Tooltip ────────────────────────────────────────────────────────
  function showTooltip(event, d) {
    const tt = document.getElementById("tooltip");
    tt.style.display = "block";

    document.getElementById("tt-name").textContent = d.name || "";
    document.getElementById("tt-code").textContent = `CZ-ISCO ${d.code}`;
    document.getElementById("tt-employees").textContent = fmtNum(d.employees);
    document.getElementById("tt-salary").textContent = fmtCZK(d.median_salary);

    const tok = d.tokenizovatelnost;
    const tes = d.testovatelnost;
    const tol = d.tolerance_k_chybe;
    const exposure = computeExposure(d);

    setBar("tt-bar-tok", "tt-val-tok", tok);
    setBar("tt-bar-tes", "tt-val-tes", tes);
    setBar("tt-bar-tol", "tt-val-tol", tol);

    document.getElementById("tt-exposure").textContent =
      exposure != null ? exposure + "/10" : "—";
    document.getElementById("tt-exposure").style.color =
      exposure != null ? exposureColor(exposure) : "";

    document.getElementById("tt-reasoning").textContent = d.reasoning || "";

    moveTooltip(event);
  }

  function moveTooltip(event) {
    const tt = document.getElementById("tooltip");
    const pad = 12;
    let x = event.clientX + pad;
    let y = event.clientY + pad;

    const ttRect = tt.getBoundingClientRect();
    if (x + ttRect.width > window.innerWidth - pad) {
      x = event.clientX - ttRect.width - pad;
    }
    if (y + ttRect.height > window.innerHeight - pad) {
      y = event.clientY - ttRect.height - pad;
    }

    tt.style.left = x + "px";
    tt.style.top = y + "px";
  }

  function hideTooltip() {
    document.getElementById("tooltip").style.display = "none";
  }

  function setBar(barId, valId, score) {
    const bar = document.getElementById(barId);
    const val = document.getElementById(valId);
    if (score != null) {
      bar.style.width = (score * 10) + "%";
      bar.style.backgroundColor = barColor(score);
      val.textContent = score;
    } else {
      bar.style.width = "0%";
      val.textContent = "—";
    }
  }

  // ── Detail panel ───────────────────────────────────────────────────
  function setupDetailPanel() {
    document.getElementById("detail-close").addEventListener("click", () => {
      document.getElementById("detail-panel").style.display = "none";
    });

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        document.getElementById("detail-panel").style.display = "none";
      }
    });
  }

  function showDetail(d, nspItem) {
    const panel = document.getElementById("detail-panel");
    panel.style.display = "block";

    // Show NSP context if searching from NSP
    let nspNote = document.getElementById("detail-nsp-note");
    if (!nspNote) {
      nspNote = document.createElement("div");
      nspNote.id = "detail-nsp-note";
      nspNote.style.cssText = "background:var(--bg-card);border:1px solid var(--border);border-radius:6px;padding:0.8rem;margin-bottom:1rem;font-size:0.85rem;";
      panel.querySelector(".detail-stats").before(nspNote);
    }

    if (nspItem) {
      nspNote.style.display = "block";
      const exposure = computeExposure(d);
      const expStr = exposure != null ? exposure.toFixed(1) : "?";
      nspNote.innerHTML = `
        <div style="color:var(--accent);font-weight:600;font-size:1rem;margin-bottom:0.4rem">${nspItem.t}</div>
        <div style="color:var(--text-muted);font-size:0.8rem;margin-bottom:0.6rem">${nspItem.c || ""}</div>
        <div style="background:rgba(239,83,80,0.1);border:1px solid rgba(239,83,80,0.3);border-radius:6px;padding:0.6rem;margin-bottom:0.6rem;font-size:0.8rem;color:var(--text-secondary)">
          <strong style="color:#ef5350">⚠ Upozornění:</strong> Profesi „${nspItem.t}" jsme neanalyzovali samostatně.
          Zobrazená data odpovídají nadřazené kategorii <strong>${d.name}</strong> (CZ-ISCO ${d.code}),
          do které tato profese spadá. Skutečná AI expozice se může lišit.
        </div>
        <div style="display:flex;gap:0.5rem;flex-wrap:wrap">
          <a href="https://nsp.cz/jednotka-prace/${nspItem.s}" target="_blank"
             style="display:inline-block;padding:0.4rem 0.8rem;background:var(--bg-card);border:1px solid var(--border);border-radius:4px;color:var(--accent);font-size:0.8rem;text-decoration:none">
            Detail na NSP.cz →
          </a>
          <button onclick="showLLMPrompt('${nspItem.t.replace(/'/g, "\\'")}', '${nspItem.s}', '${d.code}')"
             style="padding:0.4rem 0.8rem;background:var(--accent);border:none;border-radius:4px;color:#000;font-size:0.8rem;cursor:pointer;font-weight:600">
            Vyhodnotit profesi pomocí AI
          </button>
        </div>
      `;
    } else {
      nspNote.style.display = "none";
    }

    document.getElementById("detail-name").textContent = d.name || "";
    document.getElementById("detail-code").textContent = `CZ-ISCO ${d.code}`;
    document.getElementById("detail-employees").textContent = fmtNum(d.employees);
    document.getElementById("detail-salary").textContent = fmtCZK(d.median_salary);

    const exposure = computeExposure(d);
    const expEl = document.getElementById("detail-exposure");
    expEl.textContent = exposure != null ? exposure + "/10" : "—";
    expEl.style.color = exposure != null ? exposureColor(exposure) : "";

    setDetailBar("detail-bar-tok", "detail-val-tok", d.tokenizovatelnost);
    setDetailBar("detail-bar-tes", "detail-val-tes", d.testovatelnost);
    setDetailBar("detail-bar-tol", "detail-val-tol", d.tolerance_k_chybe);

    document.getElementById("detail-reasoning-tok").textContent = d.reasoning_tok || "";
    document.getElementById("detail-reasoning-tes").textContent = d.reasoning_tes || "";
    document.getElementById("detail-reasoning-tol").textContent = d.reasoning_tol || "";

    document.getElementById("detail-reasoning").textContent =
      d.reasoning || "Hodnocení není k dispozici.";

    // Add prompt button
    const promptBtn = document.getElementById("detail-prompt-btn");
    if (!nspItem) {
      promptBtn.innerHTML = `<button onclick="showLLMPromptForISPV('${d.code}')"
        style="padding:0.4rem 1rem;background:var(--bg-card);border:1px solid var(--border);border-radius:6px;color:var(--text-secondary);cursor:pointer;font-size:0.8rem">
        Vyhodnotit tuto profesi vlastním AI →
      </button>`;
    } else {
      promptBtn.innerHTML = "";
    }
  }

  function setDetailBar(barId, valId, score) {
    const bar = document.getElementById(barId);
    const val = document.getElementById(valId);
    if (score != null) {
      bar.style.width = (score * 10) + "%";
      bar.style.backgroundColor = barColor(score);
      val.textContent = score + "/10";
    } else {
      bar.style.width = "0%";
      val.textContent = "—";
    }
  }

  // ── Cohorts ─────────────────────────────────────────────────────────

  const COHORT_DEFS = [
    { key: "minimal",  label: "Minimální",      range: "0–3",     min: 0,   max: 3,   color: "#2e7d32" },
    { key: "low",      label: "Nízká",          range: "3–4,5",   min: 3,   max: 4.5, color: "#689f38" },
    { key: "moderate", label: "Střední",        range: "4,5–6",   min: 4.5, max: 6,   color: "#f9a825" },
    { key: "high",     label: "Vysoká",         range: "6–7,5",   min: 6,   max: 7.5, color: "#ef6c00" },
    { key: "critical", label: "Velmi vysoká",   range: "7,5–10",  min: 7.5, max: 10,  color: "#c62828" },
  ];

  function computeCohorts() {
    const cohorts = COHORT_DEFS.map(d => ({
      ...d,
      occupations: [],
      employees: 0,
      fte_thous: 0,
      wage_volume: 0, // monthly wage volume in millions CZK
    }));

    for (const occ of data.occupations) {
      const exp = computeExposure(occ);
      if (exp == null) continue;

      const cohort = cohorts.find(c => exp >= c.min && exp < c.max)
        || cohorts[cohorts.length - 1]; // 10.0 goes to last bucket

      cohort.occupations.push(occ);
      cohort.employees += occ.employees || 0;
      cohort.fte_thous += occ.fte_thous || 0;

      // Monthly wage volume = employees * median salary
      if (occ.median_salary) {
        cohort.wage_volume += (occ.employees || 0) * occ.median_salary;
      }
    }

    return cohorts;
  }

  function renderCohorts() {
    const cohorts = computeCohorts();
    const totalEmployees = cohorts.reduce((s, c) => s + c.employees, 0);
    const totalWageVolume = cohorts.reduce((s, c) => s + c.wage_volume, 0);
    const maxEmployees = Math.max(...cohorts.map(c => c.employees));
    const maxWage = Math.max(...cohorts.map(c => c.wage_volume));

    // ── Cards ──
    const cardsEl = document.getElementById("cohorts-cards");
    cardsEl.innerHTML = cohorts.map(c => {
      const empPct = totalEmployees > 0 ? (c.employees / totalEmployees * 100) : 0;
      const wagePct = totalWageVolume > 0 ? (c.wage_volume / totalWageVolume * 100) : 0;
      const wageMillions = c.wage_volume / 1_000_000;
      const wageBillions = c.wage_volume / 1_000_000_000;

      return `<div class="cohort-card" style="border-top-color: ${c.color}" data-cohort-key="${c.key}">
        <div class="cohort-card-title" style="color: ${c.color}">${c.label} (${c.range})</div>
        <span class="cohort-card-value">${fmtNum(c.employees)}</span>
        <span class="cohort-card-label">zaměstnanců (${empPct.toFixed(1)}%)</span>
        <div class="cohort-card-detail">
          <span>Profesí</span>
          <span>${c.occupations.length}</span>
        </div>
        <div class="cohort-card-detail">
          <span>Mzdový objem/měs.</span>
          <span>${wageBillions >= 1 ? wageBillions.toFixed(1) + " mld" : wageMillions.toFixed(0) + " mil"} Kč</span>
        </div>
        <div class="cohort-card-detail">
          <span>Podíl mezd</span>
          <span>${wagePct.toFixed(1)}%</span>
        </div>
        <div class="cohort-card-expand" style="text-align:center;margin-top:0.5rem;font-size:0.75rem;color:var(--accent);cursor:pointer">▼ Zobrazit profese</div>
      </div>`;
    }).join("");

    // Cohort card click → expand occupation list
    cardsEl.querySelectorAll(".cohort-card").forEach(card => {
      card.querySelector(".cohort-card-expand").addEventListener("click", (e) => {
        e.stopPropagation();
        const key = card.dataset.cohortKey;
        const cohort = cohorts.find(c => c.key === key);
        if (!cohort) return;
        toggleCohortList(card, cohort);
      });
    });

    // ── Horizontal bar: Employees ──
    const empBarEl = document.getElementById("cohort-bar-employees");
    empBarEl.innerHTML = `<div class="cohort-hbar">${cohorts.map(c => {
      const pct = maxEmployees > 0 ? (c.employees / maxEmployees * 100) : 0;
      const empPct = totalEmployees > 0 ? (c.employees / totalEmployees * 100) : 0;
      return `<div class="cohort-hbar-row">
        <span class="cohort-hbar-label">${c.label}<br><small>${c.range}</small></span>
        <div class="cohort-hbar-track">
          <div class="cohort-hbar-fill" style="width:${pct}%;background:${c.color}">
            <span class="cohort-hbar-fill-text">${empPct.toFixed(1)}%</span>
          </div>
        </div>
        <span class="cohort-hbar-value">${fmtNum(c.employees)}</span>
      </div>`;
    }).join("")}</div>`;

    // ── Horizontal bar: Wage volume ──
    const wageBarEl = document.getElementById("cohort-bar-wages");
    wageBarEl.innerHTML = `<div class="cohort-hbar">${cohorts.map(c => {
      const pct = maxWage > 0 ? (c.wage_volume / maxWage * 100) : 0;
      const wagePct = totalWageVolume > 0 ? (c.wage_volume / totalWageVolume * 100) : 0;
      const wageBillions = c.wage_volume / 1_000_000_000;
      const wageMillions = c.wage_volume / 1_000_000;
      const wageLabel = wageBillions >= 1 ? wageBillions.toFixed(1) + " mld" : wageMillions.toFixed(0) + " mil";
      return `<div class="cohort-hbar-row">
        <span class="cohort-hbar-label">${c.label}<br><small>${c.range}</small></span>
        <div class="cohort-hbar-track">
          <div class="cohort-hbar-fill" style="width:${pct}%;background:${c.color}">
            <span class="cohort-hbar-fill-text">${wagePct.toFixed(1)}%</span>
          </div>
        </div>
        <span class="cohort-hbar-value">${wageLabel} Kč</span>
      </div>`;
    }).join("")}</div>`;

    // ── Summary table ──
    const summaryEl = document.getElementById("cohorts-summary");
    const totalWageBillions = totalWageVolume / 1_000_000_000;
    summaryEl.innerHTML = `
      <h3>Souhrnná tabulka kohort</h3>
      <table class="cohort-summary-table">
        <thead>
          <tr>
            <th>Kohorta</th>
            <th>Expozice</th>
            <th>Profesí</th>
            <th>Zaměstnanců</th>
            <th>% zaměstnanců</th>
            <th>Mzdy/měs.</th>
            <th>% mezd</th>
            <th>Prům. medián mzdy</th>
          </tr>
        </thead>
        <tbody>
          ${cohorts.map(c => {
            const empPct = totalEmployees > 0 ? (c.employees / totalEmployees * 100) : 0;
            const wagePct = totalWageVolume > 0 ? (c.wage_volume / totalWageVolume * 100) : 0;
            const avgSalary = c.employees > 0 ? c.wage_volume / c.employees : 0;
            const wageBillions = c.wage_volume / 1_000_000_000;
            const wageMillions = c.wage_volume / 1_000_000;
            const wageLabel = wageBillions >= 1 ? wageBillions.toFixed(1) + " mld" : wageMillions.toFixed(0) + " mil";
            return `<tr>
              <td><span class="cohort-color-dot" style="background:${c.color}"></span>${c.label}</td>
              <td>${c.range}</td>
              <td>${c.occupations.length}</td>
              <td>${fmtNum(c.employees)}</td>
              <td>${empPct.toFixed(1)}%</td>
              <td>${wageLabel} Kč</td>
              <td>${wagePct.toFixed(1)}%</td>
              <td>${fmtCZK(avgSalary)}</td>
            </tr>`;
          }).join("")}
          <tr>
            <td>Celkem</td>
            <td>0–10</td>
            <td>${data.occupations.length}</td>
            <td>${fmtNum(totalEmployees)}</td>
            <td>100%</td>
            <td>${totalWageBillions.toFixed(1)} mld Kč</td>
            <td>100%</td>
            <td>${fmtCZK(totalEmployees > 0 ? totalWageVolume / totalEmployees : 0)}</td>
          </tr>
        </tbody>
      </table>`;
  }

  // ── Search ──────────────────────────────────────────────────────────

  function setupSearch() {
    const input = document.getElementById("search-input");
    const resultsEl = document.getElementById("search-results");

    // Build NSP lookup: isco4 → parent ISPV occupation
    const nspItems = data.nsp || [];
    const occByCode = {};
    for (const occ of data.occupations) occByCode[occ.code] = occ;

    input.addEventListener("input", () => {
      const query = input.value.trim().toLowerCase();
      if (query.length < 2) {
        resultsEl.style.display = "none";
        return;
      }

      // Search ISPV occupations
      const ispvMatches = data.occupations
        .map(occ => {
          const name = (occ.name || "").toLowerCase();
          const code = occ.code || "";
          const idx = name.indexOf(query);
          const codeMatch = code.startsWith(query);
          if (idx === -1 && !codeMatch) return null;
          return { type: "ispv", occ, name: occ.name, code: occ.code, idx: codeMatch ? 0 : idx };
        })
        .filter(Boolean);

      // Search NSP occupations
      const nspMatches = nspItems
        .map(nsp => {
          const title = (nsp.t || "").toLowerCase();
          const alts = (nsp.a || []).map(a => a.toLowerCase());
          let idx = title.indexOf(query);
          if (idx === -1) {
            for (const alt of alts) {
              idx = alt.indexOf(query);
              if (idx >= 0) break;
            }
          }
          if (idx === -1) return null;
          const parentOcc = occByCode[nsp.i];
          return { type: "nsp", nsp, parentOcc, name: nsp.t, idx };
        })
        .filter(Boolean);

      // Merge and sort: ISPV first, then NSP, both by match position
      const allMatches = [
        ...ispvMatches.sort((a, b) => a.idx - b.idx).slice(0, 8),
        ...nspMatches.sort((a, b) => a.idx - b.idx).slice(0, 10),
      ].slice(0, 15);

      if (allMatches.length === 0) {
        resultsEl.innerHTML = '<div class="search-result-item"><span class="search-result-name">Nic nenalezeno</span></div>';
        resultsEl.style.display = "block";
        return;
      }

      resultsEl.innerHTML = allMatches.map(match => {
        if (match.type === "ispv") {
          const occ = match.occ;
          const exp = computeExposure(occ);
          const name = occ.name || "";
          const qi = name.toLowerCase().indexOf(query);
          let highlighted = name;
          if (qi >= 0) {
            highlighted = name.slice(0, qi) + "<mark>" + name.slice(qi, qi + query.length) + "</mark>" + name.slice(qi + query.length);
          }
          const expColor = exp != null ? exposureColor(exp) : "#555";
          return `<div class="search-result-item" data-code="${occ.code}">
            <span class="search-result-name">${highlighted} <small style="color:var(--text-muted)">(${occ.code})</small></span>
            <span class="search-result-meta">
              <span>${fmtNum(occ.employees)} zam.</span>
              <span class="search-result-exposure" style="background:${expColor};color:#fff">${exp != null ? exp.toFixed(1) : "?"}</span>
            </span>
          </div>`;
        } else {
          // NSP result
          const nsp = match.nsp;
          const parentOcc = match.parentOcc;
          const name = nsp.t || "";
          const qi = name.toLowerCase().indexOf(query);
          let highlighted = name;
          if (qi >= 0) {
            highlighted = name.slice(0, qi) + "<mark>" + name.slice(qi, qi + query.length) + "</mark>" + name.slice(qi + query.length);
          }
          const parentName = parentOcc ? parentOcc.name : nsp.i;
          const exp = parentOcc ? computeExposure(parentOcc) : null;
          const expColor = exp != null ? exposureColor(exp) : "#555";
          return `<div class="search-result-item search-result-nsp" data-code="${nsp.i}" data-nsp-slug="${nsp.s}">
            <span class="search-result-name">
              ${highlighted}
              <small style="color:var(--text-muted)">→ ${parentName}</small>
            </span>
            <span class="search-result-meta">
              <span style="font-size:0.65rem;color:var(--text-muted)">NSP</span>
              <span class="search-result-exposure" style="background:${expColor};color:#fff">${exp != null ? exp.toFixed(1) : "?"}</span>
            </span>
          </div>`;
        }
      }).join("");
      resultsEl.style.display = "block";
    });

    resultsEl.addEventListener("click", (e) => {
      const item = e.target.closest(".search-result-item");
      if (!item) return;
      const code = item.dataset.code;
      const nspSlug = item.dataset.nspSlug;
      const occ = data.occupations.find(o => o.code === code);

      if (nspSlug && occ) {
        // NSP result: show parent ISPV occupation detail with NSP note
        const nspItem = nspItems.find(n => n.s === nspSlug);
        showDetail(occ, nspItem);
      } else if (occ) {
        showDetail(occ);
      }
      resultsEl.style.display = "none";
      input.value = "";
    });

    document.addEventListener("click", (e) => {
      if (!e.target.closest("#search-container")) {
        resultsEl.style.display = "none";
      }
    });
  }

  // ── LLM Prompt Generator ────────────────────────────────────────────

  // Make it global so onclick in innerHTML works
  window.showLLMPrompt = function(occupationName, nspSlug, iscoCode) {
    const parentOcc = data.occupations.find(o => o.code === iscoCode);
    const parentExp = parentOcc ? computeExposure(parentOcc) : null;

    // Find NSP item for description
    const nspItem = (data.nsp || []).find(n => n.s === nspSlug);
    const nspDesc = nspItem ? nspItem.c : "";

    // Build context about parent occupation scores
    let parentContext = "";
    if (parentOcc) {
      parentContext = `\nPro kontext: nadřazená kategorie CZ-ISCO ${iscoCode} „${parentOcc.name}" má v naší analýze tyto skóre:
- Tokenizovatelnost: ${parentOcc.tokenizovatelnost ?? "?"}/10
- Testovatelnost: ${parentOcc.testovatelnost ?? "?"}/10
- Tolerance k chybě: ${parentOcc.tolerance_k_chybe ?? "?"}/10
- Celková AI expozice: ${parentExp ?? "?"}/10
Tvoje hodnocení konkrétní profese se může lišit.`;
    }

    const prompt = `Analyzuj profesi „${occupationName}" z hlediska náchylnosti na transformaci pomocí umělé inteligence. Použij framework Triáda AI adaptace.

## Popis profese
${nspDesc || "Viz odkaz níže pro detailní popis."}
${nspSlug ? `\nKompletní popis včetně kompetencí: https://nsp.cz/jednotka-prace/${nspSlug}` : ""}
${parentContext}

## Hodnoticí framework: Triáda AI adaptace

Vyhodnoť profesi ve třech dimenzích na škále 0–10:

### 1. Tokenizovatelnost (0–10)
Do jaké míry lze vstupy, procesy a výstupy této profese převést na digitální data (tokeny) bez ztráty podstaty?
- 10: Plně digitální práce (programátor, účetní)
- 5: Mix digitálního a fyzického (architekt, učitel)
- 0: Čistě fyzická práce (ruční zemědělství)

### 2. Testovatelnost (0–10)
Jak levné a rychlé je ověřit, že výstup AI je správný a bezpečný?
- 10: Automatická verifikace v reálném čase (unit testy, spell-check)
- 5: Vyžaduje odbornou kontrolu, hodiny až dny (právní review)
- 0: Verifikace prakticky nemožná (dlouhodobé dopady politik)

### 3. Tolerance k chybě (0–10)
Jak nízké jsou následky chyby? Vyšší = nižší následky.
- 10: Téměř žádné následky (doporučení filmu)
- 5: Střední škody, finanční ztráty (chyba v účetnictví)
- 0: Katastrofální, nevratné (chirurgická chyba)

## Výpočet celkové expozice
expozice = 0,40 × tokenizovatelnost + 0,35 × testovatelnost + 0,25 × tolerance k chybě

## Požadovaný výstup
Pro každou dimenzi uveď:
1. Skóre (celé číslo 0–10)
2. Zdůvodnění (2–3 věty česky)

Na závěr:
- Celková AI expozice (výpočet)
- Které konkrétní činnosti této profese jsou AI nejvíce nahraditelné
- Které činnosti zůstanou dlouhodobě v lidských rukou a proč
- Doporučení pro pracovníky v této profesi`;

    // Show modal
    let modal = document.getElementById("llm-prompt-modal");
    if (!modal) {
      modal = document.createElement("div");
      modal.id = "llm-prompt-modal";
      modal.style.cssText = `
        position:fixed;top:0;left:0;width:100%;height:100%;
        background:rgba(0,0,0,0.7);z-index:2000;
        display:flex;align-items:center;justify-content:center;
        padding:2rem;
      `;
      document.body.appendChild(modal);
    }

    modal.innerHTML = `
      <div style="background:var(--bg-secondary);border:1px solid var(--border);border-radius:12px;max-width:700px;width:100%;max-height:80vh;overflow-y:auto;padding:1.5rem">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem">
          <h3 style="margin:0;font-size:1.1rem">Prompt pro AI vyhodnocení: ${occupationName}</h3>
          <button onclick="document.getElementById('llm-prompt-modal').style.display='none'"
                  style="background:none;border:none;color:var(--text-secondary);font-size:1.5rem;cursor:pointer">&times;</button>
        </div>
        <p style="font-size:0.8rem;color:var(--text-muted);margin-bottom:0.8rem">
          Zkopírujte tento prompt a vložte ho do ChatGPT, Claude nebo jiného AI asistenta
          pro detailní vyhodnocení AI expozice této konkrétní profese.
        </p>
        <textarea id="llm-prompt-text" readonly
          style="width:100%;min-height:300px;background:var(--bg-card);border:1px solid var(--border);
          border-radius:6px;padding:1rem;color:var(--text-primary);font-size:0.82rem;
          font-family:var(--font-mono);line-height:1.5;resize:vertical">${prompt.replace(/</g, '&lt;')}</textarea>
        <div style="display:flex;gap:0.5rem;margin-top:0.8rem;justify-content:flex-end">
          <button onclick="navigator.clipboard.writeText(document.getElementById('llm-prompt-text').value);this.textContent='Zkopírováno!';setTimeout(()=>this.textContent='Kopírovat prompt',2000)"
            style="padding:0.5rem 1.2rem;background:var(--accent);border:none;border-radius:6px;color:#000;font-weight:600;cursor:pointer;font-size:0.85rem">
            Kopírovat prompt
          </button>
          <button onclick="document.getElementById('llm-prompt-modal').style.display='none'"
            style="padding:0.5rem 1.2rem;background:var(--bg-card);border:1px solid var(--border);border-radius:6px;color:var(--text-primary);cursor:pointer;font-size:0.85rem">
            Zavřít
          </button>
        </div>
      </div>
    `;
    modal.style.display = "flex";
    modal.addEventListener("click", (e) => {
      if (e.target === modal) modal.style.display = "none";
    });
  };

  // Also add prompt button for regular ISPV occupations in detail panel
  window.showLLMPromptForISPV = function(code) {
    const occ = data.occupations.find(o => o.code === code);
    if (!occ) return;
    window.showLLMPrompt(occ.name, "", code);
  };

  // ── Cohort expansion ────────────────────────────────────────────────

  const COHORT_PAGE_SIZE = 15;

  function toggleCohortList(cardEl, cohort) {
    // Check if already expanded
    let listEl = cardEl.parentElement.querySelector(`.cohort-list[data-key="${cohort.key}"]`);
    const expandBtn = cardEl.querySelector(".cohort-card-expand");

    if (listEl) {
      listEl.remove();
      expandBtn.textContent = "▼ Zobrazit profese";
      return;
    }

    expandBtn.textContent = "▲ Skrýt profese";

    // Sort occupations by exposure descending
    const sorted = cohort.occupations
      .map(occ => ({ ...occ, _exp: computeExposure(occ) }))
      .sort((a, b) => (b._exp || 0) - (a._exp || 0));

    listEl = document.createElement("div");
    listEl.className = "cohort-list";
    listEl.dataset.key = cohort.key;
    listEl.style.cssText = `
      grid-column: 1 / -1; background: var(--bg-secondary);
      border: 1px solid var(--border); border-radius: 8px;
      padding: 1rem; margin-top: 0.5rem;
    `;

    let page = 0;
    renderCohortPage(listEl, sorted, page, cohort);
    cardEl.parentElement.insertBefore(listEl, cardEl.nextSibling);
  }

  function renderCohortPage(container, sorted, page, cohort) {
    const start = page * COHORT_PAGE_SIZE;
    const end = Math.min(start + COHORT_PAGE_SIZE, sorted.length);
    const totalPages = Math.ceil(sorted.length / COHORT_PAGE_SIZE);

    let html = `
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.8rem">
        <strong style="color:${cohort.color}">${cohort.label} (${cohort.range}) — ${sorted.length} profesí</strong>
        <span style="font-size:0.75rem;color:var(--text-muted)">Strana ${page + 1}/${totalPages}</span>
      </div>
      <table style="width:100%;border-collapse:collapse;font-size:0.82rem">
        <thead><tr>
          <th style="text-align:left;padding:0.3rem 0.5rem;border-bottom:1px solid var(--border);color:var(--text-muted);font-size:0.7rem">ISCO</th>
          <th style="text-align:left;padding:0.3rem 0.5rem;border-bottom:1px solid var(--border);color:var(--text-muted);font-size:0.7rem">Profese</th>
          <th style="text-align:right;padding:0.3rem 0.5rem;border-bottom:1px solid var(--border);color:var(--text-muted);font-size:0.7rem">Zaměstnanců</th>
          <th style="text-align:right;padding:0.3rem 0.5rem;border-bottom:1px solid var(--border);color:var(--text-muted);font-size:0.7rem">Medián mzdy</th>
          <th style="text-align:right;padding:0.3rem 0.5rem;border-bottom:1px solid var(--border);color:var(--text-muted);font-size:0.7rem">Tok</th>
          <th style="text-align:right;padding:0.3rem 0.5rem;border-bottom:1px solid var(--border);color:var(--text-muted);font-size:0.7rem">Tes</th>
          <th style="text-align:right;padding:0.3rem 0.5rem;border-bottom:1px solid var(--border);color:var(--text-muted);font-size:0.7rem">Tol</th>
          <th style="text-align:right;padding:0.3rem 0.5rem;border-bottom:1px solid var(--border);color:var(--text-muted);font-size:0.7rem">Expozice</th>
        </tr></thead><tbody>`;

    for (let i = start; i < end; i++) {
      const occ = sorted[i];
      const exp = occ._exp;
      const expColor = exp != null ? exposureColor(exp) : "#555";
      html += `<tr style="cursor:pointer;border-bottom:1px solid rgba(42,58,94,0.3)" data-code="${occ.code}" class="cohort-list-row">
        <td style="padding:0.4rem 0.5rem;font-family:var(--font-mono);font-size:0.75rem;color:var(--text-muted)">${occ.code}</td>
        <td style="padding:0.4rem 0.5rem">${occ.name}</td>
        <td style="padding:0.4rem 0.5rem;text-align:right;font-family:var(--font-mono)">${fmtNum(occ.employees)}</td>
        <td style="padding:0.4rem 0.5rem;text-align:right;font-family:var(--font-mono)">${fmtCZK(occ.median_salary)}</td>
        <td style="padding:0.4rem 0.5rem;text-align:right;font-family:var(--font-mono)">${occ.tokenizovatelnost ?? "—"}</td>
        <td style="padding:0.4rem 0.5rem;text-align:right;font-family:var(--font-mono)">${occ.testovatelnost ?? "—"}</td>
        <td style="padding:0.4rem 0.5rem;text-align:right;font-family:var(--font-mono)">${occ.tolerance_k_chybe ?? "—"}</td>
        <td style="padding:0.4rem 0.5rem;text-align:right;font-family:var(--font-mono);font-weight:700;color:${expColor}">${exp != null ? exp.toFixed(1) : "—"}</td>
      </tr>`;
    }

    html += "</tbody></table>";

    // Pagination
    if (totalPages > 1) {
      html += `<div style="display:flex;justify-content:center;gap:0.5rem;margin-top:0.8rem">`;
      if (page > 0) {
        html += `<button class="cohort-page-btn" data-page="${page - 1}" style="background:var(--bg-card);border:1px solid var(--border);color:var(--text-primary);padding:0.3rem 0.8rem;border-radius:4px;cursor:pointer;font-size:0.8rem">← Předchozí</button>`;
      }
      if (end < sorted.length) {
        html += `<button class="cohort-page-btn" data-page="${page + 1}" style="background:var(--bg-card);border:1px solid var(--border);color:var(--text-primary);padding:0.3rem 0.8rem;border-radius:4px;cursor:pointer;font-size:0.8rem">Další →</button>`;
      }
      html += "</div>";
    }

    container.innerHTML = html;

    // Row click → detail
    container.querySelectorAll(".cohort-list-row").forEach(row => {
      row.addEventListener("click", () => {
        const occ = data.occupations.find(o => o.code === row.dataset.code);
        if (occ) showDetail(occ);
      });
      row.addEventListener("mouseenter", () => row.style.background = "var(--bg-card)");
      row.addEventListener("mouseleave", () => row.style.background = "");
    });

    // Pagination buttons
    container.querySelectorAll(".cohort-page-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        renderCohortPage(container, sorted, parseInt(btn.dataset.page), cohort);
      });
    });
  }

  // ── Sectors ────────────────────────────────────────────────────────

  const ISCO_MAJOR_NAMES = {
    "0": "Zaměstnanci v ozbrojených silách",
    "1": "Zákonodárci, vedoucí a řídící pracovníci",
    "2": "Specialisté",
    "3": "Techničtí a odborní pracovníci",
    "4": "Úředníci",
    "5": "Pracovníci ve službách a prodeji",
    "6": "Kvalifikovaní pracovníci v zemědělství",
    "7": "Řemeslníci a opraváři",
    "8": "Obsluha strojů a zařízení, montéři",
    "9": "Pomocní a nekvalifikovaní pracovníci",
  };

  function renderSectors() {
    const sectors = {};
    for (const occ of data.occupations) {
      const major = occ.isco_major || "9";
      if (!sectors[major]) {
        sectors[major] = {
          code: major,
          name: ISCO_MAJOR_NAMES[major] || `Skupina ${major}`,
          occupations: 0,
          employees: 0,
          wage_volume: 0,
          exposures: [],
          salaries: [],
        };
      }
      const s = sectors[major];
      s.occupations++;
      s.employees += occ.employees || 0;
      if (occ.median_salary) {
        s.wage_volume += (occ.employees || 0) * occ.median_salary;
        s.salaries.push(occ.median_salary);
      }
      const exp = computeExposure(occ);
      if (exp != null) s.exposures.push({ exp, fte: occ.fte_thous || 0 });
    }

    const sectorList = Object.values(sectors).sort((a, b) => a.code.localeCompare(b.code));
    const totalEmployees = sectorList.reduce((s, c) => s + c.employees, 0);
    const totalWage = sectorList.reduce((s, c) => s + c.wage_volume, 0);

    const container = document.getElementById("sectors-table-container");
    container.innerHTML = `
      <table class="sectors-table">
        <thead>
          <tr>
            <th>Obor (ISCO)</th>
            <th>Profesí</th>
            <th>Zaměstnanců</th>
            <th>% zaměst.</th>
            <th>Prům. medián mzdy</th>
            <th>Mzdy/měs.</th>
            <th>% mezd</th>
            <th>Prům. expozice</th>
            <th>Min–Max</th>
          </tr>
        </thead>
        <tbody>
          ${sectorList.map(s => {
            const empPct = totalEmployees > 0 ? (s.employees / totalEmployees * 100) : 0;
            const wagePct = totalWage > 0 ? (s.wage_volume / totalWage * 100) : 0;
            const avgSalary = s.salaries.length > 0 ? s.salaries.reduce((a, b) => a + b, 0) / s.salaries.length : 0;
            const wageBillions = s.wage_volume / 1_000_000_000;
            const wageMillions = s.wage_volume / 1_000_000;
            const wageLabel = wageBillions >= 1 ? wageBillions.toFixed(1) + " mld" : wageMillions.toFixed(0) + " mil";

            let avgExp = null, minExp = null, maxExp = null;
            if (s.exposures.length > 0) {
              const totalFte = s.exposures.reduce((a, e) => a + e.fte, 0);
              avgExp = totalFte > 0
                ? s.exposures.reduce((a, e) => a + e.exp * e.fte, 0) / totalFte
                : s.exposures.reduce((a, e) => a + e.exp, 0) / s.exposures.length;
              minExp = Math.min(...s.exposures.map(e => e.exp));
              maxExp = Math.max(...s.exposures.map(e => e.exp));
            }

            const barWidth = avgExp != null ? Math.round(avgExp * 10) : 0;
            const barColor = avgExp != null ? exposureColor(avgExp) : "#555";

            return `<tr>
              <td><span class="sector-exposure-bar" style="width:${barWidth}px;background:${barColor}"></span>${s.code} ${s.name}</td>
              <td>${s.occupations}</td>
              <td>${fmtNum(s.employees)}</td>
              <td>${empPct.toFixed(1)}%</td>
              <td>${fmtCZK(avgSalary)}</td>
              <td>${wageLabel} Kč</td>
              <td>${wagePct.toFixed(1)}%</td>
              <td style="color:${barColor};font-weight:700">${avgExp != null ? avgExp.toFixed(1) : "—"}</td>
              <td>${minExp != null ? minExp.toFixed(1) + "–" + maxExp.toFixed(1) : "—"}</td>
            </tr>`;
          }).join("")}
          <tr>
            <td>Celkem</td>
            <td>${data.occupations.length}</td>
            <td>${fmtNum(totalEmployees)}</td>
            <td>100%</td>
            <td></td>
            <td>${(totalWage / 1_000_000_000).toFixed(1)} mld Kč</td>
            <td>100%</td>
            <td></td>
            <td></td>
          </tr>
        </tbody>
      </table>`;
  }

  // ── Utilities ──────────────────────────────────────────────────────
  function debounce(fn, delay) {
    let timer;
    return function (...args) {
      clearTimeout(timer);
      timer = setTimeout(() => fn.apply(this, args), delay);
    };
  }

  // ── Start ──────────────────────────────────────────────────────────
  loadData();
})();
