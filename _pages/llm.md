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

    <!-- Tabulka: Programování -->
    <div class="cat-table-container" data-category="coding">
      <table class="cat-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Model</th>
            <th>Skóre</th>
            <th>Tier</th>
            <th>Cena</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {% assign coding_models = site.llm | where_exp: "m", "m.benchmark_categories.coding.score" | sort: "benchmark_categories.coding.score" | reverse %}
          {% assign best_value = 0 %}
          {% assign best_value_model = "" %}
          {% for m in coding_models limit: 10 %}
            {% if m.pricing.blend_per_m > 0 %}
              {% assign value = m.benchmark_categories.coding.score | divided_by: m.pricing.blend_per_m %}
              {% if value > best_value %}
                {% assign best_value = value %}
                {% assign best_value_model = m.slug %}
              {% endif %}
            {% endif %}
          {% endfor %}
          {% for m in coding_models limit: 10 %}
          <tr {% if forloop.first %}class="top-score"{% endif %}{% if m.slug == best_value_model %} class="best-value"{% endif %}>
            <td>{% if forloop.first %}🥇{% else %}{{ forloop.index }}{% endif %}</td>
            <td><a href="{{ m.url }}">{{ m.title }}</a></td>
            <td><strong>{{ m.benchmark_categories.coding.score | round: 1 }}</strong></td>
            <td><span class="tier-badge tier-{{ m.benchmark_categories.coding.tier | downcase | replace: ' ', '-' }}">{{ m.benchmark_categories.coding.tier }}</span></td>
            <td>${{ m.pricing.blend_per_m }}/1M</td>
            <td>{% if m.slug == best_value_model %}💰{% endif %}{% if m.pricing.blend_per_m > 0 %}{{ m.benchmark_categories.coding.score | divided_by: m.pricing.blend_per_m | round: 1 }}{% else %}∞{% endif %}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>

    <!-- Tabulka: Věda & Matematika -->
    <div class="cat-table-container hidden" data-category="science">
      <table class="cat-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Model</th>
            <th>Skóre</th>
            <th>Tier</th>
            <th>Cena</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {% assign science_models = site.llm | where_exp: "m", "m.benchmark_categories.science.score" | sort: "benchmark_categories.science.score" | reverse %}
          {% assign best_value = 0 %}
          {% assign best_value_model = "" %}
          {% for m in science_models limit: 10 %}
            {% if m.pricing.blend_per_m > 0 %}
              {% assign value = m.benchmark_categories.science.score | divided_by: m.pricing.blend_per_m %}
              {% if value > best_value %}
                {% assign best_value = value %}
                {% assign best_value_model = m.slug %}
              {% endif %}
            {% endif %}
          {% endfor %}
          {% for m in science_models limit: 10 %}
          <tr {% if forloop.first %}class="top-score"{% endif %}{% if m.slug == best_value_model %} class="best-value"{% endif %}>
            <td>{% if forloop.first %}🥇{% else %}{{ forloop.index }}{% endif %}</td>
            <td><a href="{{ m.url }}">{{ m.title }}</a></td>
            <td><strong>{{ m.benchmark_categories.science.score | round: 1 }}</strong></td>
            <td><span class="tier-badge tier-{{ m.benchmark_categories.science.tier | downcase | replace: ' ', '-' }}">{{ m.benchmark_categories.science.tier }}</span></td>
            <td>${{ m.pricing.blend_per_m }}/1M</td>
            <td>{% if m.slug == best_value_model %}💰{% endif %}{% if m.pricing.blend_per_m > 0 %}{{ m.benchmark_categories.science.score | divided_by: m.pricing.blend_per_m | round: 1 }}{% else %}∞{% endif %}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>

    <!-- Tabulka: Agenti -->
    <div class="cat-table-container hidden" data-category="agentic">
      <table class="cat-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Model</th>
            <th>Skóre</th>
            <th>Tier</th>
            <th>Cena</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {% assign agentic_models = site.llm | where_exp: "m", "m.benchmark_categories.agentic.score" | sort: "benchmark_categories.agentic.score" | reverse %}
          {% assign best_value = 0 %}
          {% assign best_value_model = "" %}
          {% for m in agentic_models limit: 10 %}
            {% if m.pricing.blend_per_m > 0 %}
              {% assign value = m.benchmark_categories.agentic.score | divided_by: m.pricing.blend_per_m %}
              {% if value > best_value %}
                {% assign best_value = value %}
                {% assign best_value_model = m.slug %}
              {% endif %}
            {% endif %}
          {% endfor %}
          {% for m in agentic_models limit: 10 %}
          <tr {% if forloop.first %}class="top-score"{% endif %}{% if m.slug == best_value_model %} class="best-value"{% endif %}>
            <td>{% if forloop.first %}🥇{% else %}{{ forloop.index }}{% endif %}</td>
            <td><a href="{{ m.url }}">{{ m.title }}</a></td>
            <td><strong>{{ m.benchmark_categories.agentic.score | round: 1 }}</strong></td>
            <td><span class="tier-badge tier-{{ m.benchmark_categories.agentic.tier | downcase | replace: ' ', '-' }}">{{ m.benchmark_categories.agentic.tier }}</span></td>
            <td>${{ m.pricing.blend_per_m }}/1M</td>
            <td>{% if m.slug == best_value_model %}💰{% endif %}{% if m.pricing.blend_per_m > 0 %}{{ m.benchmark_categories.agentic.score | divided_by: m.pricing.blend_per_m | round: 1 }}{% else %}∞{% endif %}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>

    <!-- Tabulka: Inteligence -->
    <div class="cat-table-container hidden" data-category="intelligence">
      <table class="cat-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Model</th>
            <th>Skóre</th>
            <th>Tier</th>
            <th>Cena</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {% assign intelligence_models = site.llm | where_exp: "m", "m.benchmark_categories.intelligence.score" | sort: "benchmark_categories.intelligence.score" | reverse %}
          {% assign best_value = 0 %}
          {% assign best_value_model = "" %}
          {% for m in intelligence_models limit: 10 %}
            {% if m.pricing.blend_per_m > 0 %}
              {% assign value = m.benchmark_categories.intelligence.score | divided_by: m.pricing.blend_per_m %}
              {% if value > best_value %}
                {% assign best_value = value %}
                {% assign best_value_model = m.slug %}
              {% endif %}
            {% endif %}
          {% endfor %}
          {% for m in intelligence_models limit: 10 %}
          <tr {% if forloop.first %}class="top-score"{% endif %}{% if m.slug == best_value_model %} class="best-value"{% endif %}>
            <td>{% if forloop.first %}🥇{% else %}{{ forloop.index }}{% endif %}</td>
            <td><a href="{{ m.url }}">{{ m.title }}</a></td>
            <td><strong>{{ m.benchmark_categories.intelligence.score | round: 1 }}</strong></td>
            <td><span class="tier-badge tier-{{ m.benchmark_categories.intelligence.tier | downcase | replace: ' ', '-' }}">{{ m.benchmark_categories.intelligence.tier }}</span></td>
            <td>${{ m.pricing.blend_per_m }}/1M</td>
            <td>{% if m.slug == best_value_model %}💰{% endif %}{% if m.pricing.blend_per_m > 0 %}{{ m.benchmark_categories.intelligence.score | divided_by: m.pricing.blend_per_m | round: 1 }}{% else %}∞{% endif %}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>

    <!-- Tabulka: Rychlost -->
    <div class="cat-table-container hidden" data-category="speed">
      <table class="cat-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Model</th>
            <th>Skóre</th>
            <th>Tier</th>
            <th>Cena</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {% assign speed_models = site.llm | where_exp: "m", "m.benchmark_categories.speed.score" | sort: "benchmark_categories.speed.score" | reverse %}
          {% assign best_value = 0 %}
          {% assign best_value_model = "" %}
          {% for m in speed_models limit: 10 %}
            {% if m.pricing.blend_per_m > 0 %}
              {% assign value = m.benchmark_categories.speed.score | divided_by: m.pricing.blend_per_m %}
              {% if value > best_value %}
                {% assign best_value = value %}
                {% assign best_value_model = m.slug %}
              {% endif %}
            {% endif %}
          {% endfor %}
          {% for m in speed_models limit: 10 %}
          <tr {% if forloop.first %}class="top-score"{% endif %}{% if m.slug == best_value_model %} class="best-value"{% endif %}>
            <td>{% if forloop.first %}🥇{% else %}{{ forloop.index }}{% endif %}</td>
            <td><a href="{{ m.url }}">{{ m.title }}</a></td>
            <td><strong>{{ m.benchmark_categories.speed.score | round: 1 }}</strong></td>
            <td><span class="tier-badge tier-{{ m.benchmark_categories.speed.tier | downcase | replace: ' ', '-' }}">{{ m.benchmark_categories.speed.tier }}</span></td>
            <td>${{ m.pricing.blend_per_m }}/1M</td>
            <td>{% if m.slug == best_value_model %}💰{% endif %}{% if m.pricing.blend_per_m > 0 %}{{ m.benchmark_categories.speed.score | divided_by: m.pricing.blend_per_m | round: 1 }}{% else %}∞{% endif %}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
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
      <div class="card-header">
        <span class="provider">{{ model.provider }}</span>
        <time datetime="{{ model.date | date_to_xmlschema }}">{{ model.date | date: "%d. %m. %Y" }}</time>
      </div>

      <h2 class="card-title">
        <a href="{{ model.url }}">{{ model.title }}</a>
      </h2>


      <div class="card-tags">
        {% for focus in model.focus limit:3 %}
          <span class="tag">{{ focus }}</span>
        {% endfor %}
      </div>

      {% if model.verdict %}
      <p class="card-verdict">{{ model.verdict | truncate: 150 }}</p>
      {% endif %}


      <div class="card-pricing">
        <span class="price {% if model.pricing.prompt_per_m == 0 %}free{% endif %}">
          {% if model.pricing.prompt_per_m == 0 %}Zdarma{% else %}${{ model.pricing.prompt_per_m }}/1M{% endif %} -       <a href="{{ model.url }}" class="card-link">Detail modelu →</a>
        </span>
        <span class="arrow">→</span>
        <span class="price {% if model.pricing.completion_per_m == 0 %}free{% endif %}">
          {% if model.pricing.completion_per_m == 0 %}Zdarma{% else %}${{ model.pricing.completion_per_m }}/1M{% endif %} -       <a href="{{ model.url }}" class="card-link">Detail modelu →</a>
        </span>
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
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

/* Karty */
.llm-card {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  border: 1px solid #e5e7eb;
  transition: all 0.2s;
}

.llm-card:hover {
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

.llm-card.hidden {
  display: none;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}

.provider {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 1rem;
  font-size: 0.75rem;
  font-weight: 600;
}

.card-header time {
  font-size: 0.8rem;
  color: #6b7280;
}

.card-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
  line-height: 1.3;
}

.card-title a {
  color: #111827;
  text-decoration: none;
}

.card-title a:hover {
  color: #3b82f6;
}

.card-id code {
  background: #f3f4f6;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-size: 0.75rem;
  color: #6b7280;
}

.card-pricing {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin: 0.75rem 0;
}

.card-pricing .price {
  font-weight: 600;
  font-size: 0.9rem;
  color: #374151;
}

.card-pricing .price.free {
  color: #10b981;
}

.card-pricing .arrow {
  color: #9ca3af;
}

.card-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem;
  margin-bottom: 0.75rem;
}

.tag {
  background: #dbeafe;
  color: #1e40af;
  padding: 0.15rem 0.5rem;
  border-radius: 1rem;
  font-size: 0.7rem;
}

.card-verdict {
  font-size: 0.9rem;
  color: #4b5563;
  line-height: 1.5;
  margin-bottom: 1rem;
}

.card-link {
  color: #3b82f6;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
}

.card-link:hover {
  text-decoration: underline;
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
