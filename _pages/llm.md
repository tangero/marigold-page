---
layout: page
title: Přehled LLM modelů
permalink: /llm/
---

<div class="llm-overview">
  <header class="llm-page-header">
    <p class="subtitle">Jaké LLM máte pro jaký úkol použít? Nejobsáhlejší 🇨🇿 přehled a doporučení.</p>
    <div class="stats">
      <span class="stat-item">{{ site.llm.size }} modelů</span>
      <span class="stat-divider">|</span>
      <span class="stat-item">Aktualizováno denně</span>
    </div>
  </header>

  <!-- Taby podle kategorií -->
  <section class="llm-category-section">
    <h2>Top modely podle kategorie</h2>
    <div class="category-tabs">
      <button class="cat-tab active" data-category="coding">💻 Programování</button>
      <button class="cat-tab" data-category="science">🧮 Věda & Matematika</button>
      <button class="cat-tab" data-category="agentic">🤖 Agenti</button>
      <button class="cat-tab" data-category="intelligence">🧠 Inteligence</button>
      <button class="cat-tab" data-category="speed">⚡ Rychlost</button>
    </div>

    <!-- Tabulka: Programování (kurátorovaný seznam) -->
    <div class="cat-table-container" data-category="coding">
      <table class="cat-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Model</th>
            <th>Proč v TOP</th>
            <th>Cena</th>
          </tr>
        </thead>
        <tbody>
          {% for top_item in site.data.top_models.coding %}
            {% assign m = site.llm | where: "slug", top_item.slug | first %}
            {% if m %}
          <tr {% if forloop.first %}class="top-score"{% endif %}>
            <td>{% if forloop.first %}🥇{% elsif forloop.index == 2 %}🥈{% elsif forloop.index == 3 %}🥉{% else %}{{ forloop.index }}{% endif %}</td>
            <td><a href="{{ m.url }}">{{ m.title }}</a></td>
            <td class="note-cell">{{ top_item.note }}</td>
            <td>${{ m.pricing.blend_per_m }}/1M</td>
          </tr>
            {% endif %}
          {% endfor %}
        </tbody>
      </table>
      <p class="curated-note">Kurátorovaný výběr redakce na základě benchmark dat a praktických zkušeností.</p>
    </div>

    <!-- Tabulka: Věda & Matematika (kurátorovaný seznam) -->
    <div class="cat-table-container hidden" data-category="science">
      <table class="cat-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Model</th>
            <th>Proč v TOP</th>
            <th>Cena</th>
          </tr>
        </thead>
        <tbody>
          {% for top_item in site.data.top_models.science %}
            {% assign m = site.llm | where: "slug", top_item.slug | first %}
            {% if m %}
          <tr {% if forloop.first %}class="top-score"{% endif %}>
            <td>{% if forloop.first %}🥇{% elsif forloop.index == 2 %}🥈{% elsif forloop.index == 3 %}🥉{% else %}{{ forloop.index }}{% endif %}</td>
            <td><a href="{{ m.url }}">{{ m.title }}</a></td>
            <td class="note-cell">{{ top_item.note }}</td>
            <td>${{ m.pricing.blend_per_m }}/1M</td>
          </tr>
            {% endif %}
          {% endfor %}
        </tbody>
      </table>
      <p class="curated-note">Kurátorovaný výběr redakce na základě benchmark dat a praktických zkušeností.</p>
    </div>

    <!-- Tabulka: Agenti (kurátorovaný seznam) -->
    <div class="cat-table-container hidden" data-category="agentic">
      <table class="cat-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Model</th>
            <th>Proč v TOP</th>
            <th>Cena</th>
          </tr>
        </thead>
        <tbody>
          {% for top_item in site.data.top_models.agentic %}
            {% assign m = site.llm | where: "slug", top_item.slug | first %}
            {% if m %}
          <tr {% if forloop.first %}class="top-score"{% endif %}>
            <td>{% if forloop.first %}🥇{% elsif forloop.index == 2 %}🥈{% elsif forloop.index == 3 %}🥉{% else %}{{ forloop.index }}{% endif %}</td>
            <td><a href="{{ m.url }}">{{ m.title }}</a></td>
            <td class="note-cell">{{ top_item.note }}</td>
            <td>${{ m.pricing.blend_per_m }}/1M</td>
          </tr>
            {% endif %}
          {% endfor %}
        </tbody>
      </table>
      <p class="curated-note">Kurátorovaný výběr redakce na základě benchmark dat a praktických zkušeností.</p>
    </div>

    <!-- Tabulka: Inteligence (kurátorovaný seznam) -->
    <div class="cat-table-container hidden" data-category="intelligence">
      <table class="cat-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Model</th>
            <th>Proč v TOP</th>
            <th>Cena</th>
          </tr>
        </thead>
        <tbody>
          {% for top_item in site.data.top_models.intelligence %}
            {% assign m = site.llm | where: "slug", top_item.slug | first %}
            {% if m %}
          <tr {% if forloop.first %}class="top-score"{% endif %}>
            <td>{% if forloop.first %}🥇{% elsif forloop.index == 2 %}🥈{% elsif forloop.index == 3 %}🥉{% else %}{{ forloop.index }}{% endif %}</td>
            <td><a href="{{ m.url }}">{{ m.title }}</a></td>
            <td class="note-cell">{{ top_item.note }}</td>
            <td>${{ m.pricing.blend_per_m }}/1M</td>
          </tr>
            {% endif %}
          {% endfor %}
        </tbody>
      </table>
      <p class="curated-note">Kurátorovaný výběr redakce na základě benchmark dat a praktických zkušeností.</p>
    </div>

    <!-- Tabulka: Rychlost (kurátorovaný seznam) -->
    <div class="cat-table-container hidden" data-category="speed">
      <table class="cat-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Model</th>
            <th>Proč v TOP</th>
            <th>Cena</th>
          </tr>
        </thead>
        <tbody>
          {% for top_item in site.data.top_models.speed %}
            {% assign m = site.llm | where: "slug", top_item.slug | first %}
            {% if m %}
          <tr {% if forloop.first %}class="top-score"{% endif %}>
            <td>{% if forloop.first %}🥇{% elsif forloop.index == 2 %}🥈{% elsif forloop.index == 3 %}🥉{% else %}{{ forloop.index }}{% endif %}</td>
            <td><a href="{{ m.url }}">{{ m.title }}</a></td>
            <td class="note-cell">{{ top_item.note }}</td>
            <td>${{ m.pricing.blend_per_m }}/1M</td>
          </tr>
            {% endif %}
          {% endfor %}
        </tbody>
      </table>
      <p class="curated-note">Kurátorovaný výběr redakce na základě benchmark dat a praktických zkušeností.</p>
    </div>
  </section>

  <!-- Filtry podle providera -->
  <h2 class="all-models-header">Všechny modely</h2>
  <div class="llm-filters">
    <button class="filter-btn active" data-filter="all">Všechny</button>
    <button class="filter-btn" data-filter="anthropic">Anthropic</button>
    <button class="filter-btn" data-filter="openai">OpenAI</button>
    <button class="filter-btn" data-filter="google">Google</button>
    <button class="filter-btn" data-filter="x-ai">xAI</button>
    <button class="filter-btn" data-filter="deepseek">DeepSeek</button>
    <button class="filter-btn" data-filter="mistralai">Mistral</button>
  </div>

  <!-- Seznam modelu -->
  <div class="llm-grid">
    {% assign sorted_models = site.llm | sort: 'date' | reverse %}
    {% for model in sorted_models %}
    <article class="llm-card" data-provider="{{ model.provider | downcase }}">
      <!-- Header s providerem a benchmark badge -->
      <div class="card-header-new">
        <div class="provider-badge">
          {% assign provider_lower = model.provider | downcase %}
          {% if provider_lower contains 'anthropic' %}
            <span class="provider-emoji">🤖</span>
          {% elsif provider_lower contains 'openai' %}
            <span class="provider-emoji">🔮</span>
          {% elsif provider_lower contains 'google' %}
            <span class="provider-emoji">🔍</span>
          {% elsif provider_lower contains 'x-ai' or provider_lower contains 'xai' %}
            <span class="provider-emoji">🚀</span>
          {% elsif provider_lower contains 'deepseek' %}
            <span class="provider-emoji">🌊</span>
          {% elsif provider_lower contains 'mistral' %}
            <span class="provider-emoji">💨</span>
          {% elsif provider_lower contains 'meta' %}
            <span class="provider-emoji">🦙</span>
          {% else %}
            <span class="provider-emoji">🤖</span>
          {% endif %}
          <span class="provider-name">{{ model.provider }}</span>
        </div>

      </div>

      <!-- Název modelu -->
      <h2 class="card-title-new">
        <a href="{{ model.url }}">{{ model.title }}</a>
      </h2>

      <!-- Focus tagy -->
      <div class="card-tags-new">
        {% for focus in model.focus limit:3 %}
          <span class="tag-new">{{ focus }}</span>
        {% endfor %}
      </div>

      <!-- Verdict/popis -->
      {% if model.verdict %}
      <p class="card-verdict-new">{{ model.verdict | truncate: 150 }}</p>
      {% endif %}

      <!-- Pricing box - nový design -->
      <div class="pricing-box">
        <div class="pricing-row">
          <div class="pricing-label">Cena vstup/výstup</div>
          <div class="cost-emoji">
          {% if model.pricing.blend_per_m %}
            {% if model.pricing.blend_per_m == 0 %}
              <span class="cost-free-label">Zdarma</span>
            {% elsif model.pricing.blend_per_m < 1 %}
              💰
            {% elsif model.pricing.blend_per_m < 5 %}
              💰💰
            {% elsif model.pricing.blend_per_m < 15 %}
              💰💰💰
            {% else %}
              💰💰💰💰
            {% endif %}
          {% else %}
            💰💰
          {% endif %}
          </div>
        </div>
        <div class="pricing-values">
          <span class="price-item">
            <span class="price-icon">↓</span>
            {% if model.pricing.prompt_per_m == 0 %}
              <strong>Zdarma</strong>
            {% else %}
              <strong>${{ model.pricing.prompt_per_m }}</strong>/1M
            {% endif %}
          </span>
          <span class="price-divider">→</span>
          <span class="price-item">
            <span class="price-icon">↑</span>
            {% if model.pricing.completion_per_m == 0 %}
              <strong>Zdarma</strong>
            {% else %}
              <strong>${{ model.pricing.completion_per_m }}</strong>/1M
            {% endif %}
          </span>
        </div>
        {% if model.pricing.blend_per_m %}
        <div class="pricing-blend">
          Průměr: <strong>${{ model.pricing.blend_per_m }}/1M</strong>
        </div>
        {% endif %}
      </div>

      <!-- Datum a detail link -->
      <div class="card-footer-new">
        <time datetime="{{ model.date | date_to_xmlschema }}">{{ model.date | date: "%d. %m. %Y" }}</time>
        <a href="{{ model.url }}" class="detail-link">Detail modelu →</a>
      </div>
    </article>
    {% endfor %}
  </div>

  {% if site.llm.size == 0 %}
  <div class="empty-state">
    <p>Zatím nejsou k dispozici žádné recenze LLM modelů.</p>
    <p class="hint">Recenze se generují automaticky každé ráno.</p>
  </div>
  {% endif %}
</div>

<style>
.llm-overview {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.llm-page-header {
  text-align: center;
  margin-bottom: 2rem;
  padding-bottom: 2rem;
  border-bottom: 2px solid #e5e7eb;
}

.llm-page-header h1 {
  font-size: 2.5rem;
  font-weight: 700;
  color: #111827;
  margin-bottom: 0.5rem;
}

.subtitle {
  color: #6b7280;
  font-size: 1.1rem;
}

.stats {
  margin-top: 1rem;
  display: flex;
  justify-content: center;
  gap: 1rem;
  font-size: 0.9rem;
  color: #6b7280;
}

.stat-divider {
  color: #d1d5db;
}

/* Kategorie sekce */
.llm-category-section {
  margin-bottom: 3rem;
  padding-bottom: 2rem;
  border-bottom: 2px solid #e5e7eb;
}

.llm-category-section h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #111827;
  margin-bottom: 1.5rem;
  text-align: center;
}

.all-models-header {
  font-size: 1.5rem;
  font-weight: 700;
  color: #111827;
  margin-bottom: 1rem;
  text-align: center;
}

/* Taby kategorií */
.category-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.cat-tab {
  padding: 0.6rem 1.2rem;
  border: 2px solid #e5e7eb;
  background: white;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  transition: all 0.2s;
}

.cat-tab:hover {
  border-color: #3b82f6;
  color: #3b82f6;
}

.cat-tab.active {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-color: transparent;
}

/* Tabulky kategorií */
.cat-table-container {
  overflow-x: auto;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.cat-table-container.hidden {
  display: none;
}

.cat-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}

.cat-table th {
  background: #f9fafb;
  padding: 0.75rem 1rem;
  text-align: left;
  font-weight: 600;
  color: #374151;
  border-bottom: 2px solid #e5e7eb;
}

.cat-table td {
  padding: 0.75rem 1rem;
  border-bottom: 1px solid #f3f4f6;
}

.cat-table tr:hover {
  background: #f9fafb;
}

.cat-table tr.top-score {
  background: linear-gradient(90deg, #ecfdf5 0%, white 100%);
}

.cat-table tr.best-value {
  background: linear-gradient(90deg, #fef3c7 0%, white 100%);
}

.cat-table a {
  color: #3b82f6;
  text-decoration: none;
  font-weight: 500;
}

.cat-table a:hover {
  text-decoration: underline;
}

/* Tier badge v tabulce */
.tier-badge {
  display: inline-block;
  padding: 0.2rem 0.6rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 600;
  color: white;
}

.tier-badge.tier-excelentní { background: #10b981; }
.tier-badge.tier-výborný { background: #3b82f6; }
.tier-badge.tier-dobrý { background: #f59e0b; }
.tier-badge.tier-průměrný { background: #6b7280; }
.tier-badge.tier-slabý { background: #ef4444; }

/* Kurátorované tabulky */
.note-cell {
  font-size: 0.85rem;
  color: #4b5563;
  font-style: italic;
}

.curated-note {
  text-align: center;
  font-size: 0.8rem;
  color: #9ca3af;
  margin-top: 0.75rem;
  padding-top: 0.75rem;
  border-top: 1px dashed #e5e7eb;
}

/* Filtry */
.llm-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 2rem;
  justify-content: center;
}

.filter-btn {
  padding: 0.5rem 1rem;
  border: 1px solid #e5e7eb;
  background: white;
  border-radius: 2rem;
  cursor: pointer;
  font-size: 0.875rem;
  transition: all 0.2s;
}

.filter-btn:hover {
  border-color: #3b82f6;
  color: #3b82f6;
}

.filter-btn.active {
  background: #3b82f6;
  color: white;
  border-color: #3b82f6;
}

/* Grid */
.llm-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
  gap: 1.5rem;
}

/* Nový design karty */
.llm-card {
  background: white;
  border-radius: 16px;
  padding: 1.5rem;
  border: 1px solid #e5e7eb;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
}

.llm-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
  opacity: 0;
  transition: opacity 0.3s;
}

.llm-card:hover {
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.12);
  transform: translateY(-4px);
  border-color: #667eea;
}

.llm-card:hover::before {
  opacity: 1;
}

.llm-card.hidden {
  display: none;
}

/* Nový header s providerem a score badge */
.card-header-new {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
  gap: 1rem;
}

.provider-badge {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: linear-gradient(135deg, #f3f4f6 0%, #e5e7eb 100%);
  padding: 0.4rem 0.8rem;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 600;
  color: #374151;
}

.provider-emoji {
  font-size: 1.1rem;
}

.provider-name {
  white-space: nowrap;
}

/* Název modelu */
.card-title-new {
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 0.75rem;
  line-height: 1.3;
}

.card-title-new a {
  color: #111827;
  text-decoration: none;
  transition: color 0.2s;
}

.card-title-new a:hover {
  color: #667eea;
}

/* Tagy */
.card-tags-new {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-bottom: 0.75rem;
}

.tag-new {
  background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
  color: #1e40af;
  padding: 0.25rem 0.65rem;
  border-radius: 6px;
  font-size: 0.7rem;
  font-weight: 600;
  transition: all 0.2s;
}

.tag-new:hover {
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(30, 64, 175, 0.2);
}

/* Verdict */
.card-verdict-new {
  font-size: 0.9rem;
  color: #4b5563;
  line-height: 1.5;
  margin-bottom: 1rem;
}

/* Nový pricing box */
.pricing-box {
  background: linear-gradient(135deg, #f9fafb 0%, #f3f4f6 100%);
  border: 1px solid #e5e7eb;
  border-radius: 10px;
  padding: 1rem;
  margin-bottom: 1rem;
}

.pricing-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.pricing-label {
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  color: #6b7280;
  letter-spacing: 0.5px;
}

/* Cost emoji indicator */
.cost-emoji {
  font-size: 1rem;
  letter-spacing: -2px;
}

.cost-free-label {
  color: #10b981;
  font-weight: 600;
  font-size: 0.8rem;
}

.pricing-values {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.75rem;
  margin-bottom: 0.5rem;
}

.price-item {
  display: flex;
  align-items: center;
  gap: 0.3rem;
  font-size: 0.9rem;
  color: #374151;
}

.price-icon {
  font-size: 1rem;
  color: #9ca3af;
}

.price-item strong {
  font-weight: 700;
  color: #111827;
}

.price-divider {
  color: #d1d5db;
  font-weight: 300;
}

.pricing-blend {
  text-align: center;
  font-size: 0.8rem;
  color: #6b7280;
  padding-top: 0.5rem;
  border-top: 1px solid #e5e7eb;
}

.pricing-blend strong {
  color: #111827;
  font-weight: 600;
}

/* Footer karty */
.card-footer-new {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 0.75rem;
  border-top: 1px solid #e5e7eb;
}

.card-footer-new time {
  font-size: 0.8rem;
  color: #9ca3af;
}

.detail-link {
  color: #667eea;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 600;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 0.3rem;
}

.detail-link:hover {
  color: #764ba2;
  transform: translateX(3px);
}

/* Empty state */
.empty-state {
  text-align: center;
  padding: 3rem;
  background: #f9fafb;
  border-radius: 12px;
}

.empty-state p {
  color: #6b7280;
  margin: 0.5rem 0;
}

.empty-state .hint {
  font-size: 0.9rem;
}

/* Responsive */
@media (max-width: 768px) {
  .llm-overview {
    padding: 1rem;
  }

  .llm-page-header h1 {
    font-size: 1.75rem;
  }

  .llm-grid {
    grid-template-columns: 1fr;
  }

  .card-header-new {
    flex-direction: column;
    gap: 0.75rem;
  }

  .pricing-values {
    flex-direction: column;
    gap: 0.5rem;
  }

  .price-divider {
    transform: rotate(90deg);
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  // Provider filter
  const filterBtns = document.querySelectorAll('.filter-btn');
  const cards = document.querySelectorAll('.llm-card');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      const filter = this.dataset.filter;

      // Update active button
      filterBtns.forEach(b => b.classList.remove('active'));
      this.classList.add('active');

      // Filter cards
      cards.forEach(card => {
        if (filter === 'all' || card.dataset.provider === filter) {
          card.classList.remove('hidden');
        } else {
          card.classList.add('hidden');
        }
      });
    });
  });

  // Category tabs
  const catTabs = document.querySelectorAll('.cat-tab');
  const catTables = document.querySelectorAll('.cat-table-container');

  catTabs.forEach(tab => {
    tab.addEventListener('click', function() {
      const category = this.dataset.category;

      // Update active tab
      catTabs.forEach(t => t.classList.remove('active'));
      this.classList.add('active');

      // Show corresponding table
      catTables.forEach(table => {
        if (table.dataset.category === category) {
          table.classList.remove('hidden');
        } else {
          table.classList.add('hidden');
        }
      });
    });
  });
});
</script>
