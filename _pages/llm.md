---
layout: page
title: Přehled LLM modelů
permalink: /llm/
---

<div class="llm-overview">
  <header class="llm-page-header">
    <h1>Přehled LLM modelů</h1>
    <p class="subtitle">Automaticky generované recenze jazykových modelů z OpenRouter API</p>
    <div class="stats">
      <span class="stat-item">{{ site.llm.size }} modelů</span>
      <span class="stat-divider">|</span>
      <span class="stat-item">Aktualizováno denně</span>
    </div>
  </header>

  <!-- Filtry -->
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

      <div class="card-id">
        <code>{{ model.model_id }}</code>
      </div>

      <div class="card-pricing">
        <span class="price {% if model.pricing.prompt_per_m == 0 %}free{% endif %}">
          {% if model.pricing.prompt_per_m == 0 %}Zdarma{% else %}${{ model.pricing.prompt_per_m }}/1M{% endif %}
        </span>
        <span class="arrow">→</span>
        <span class="price {% if model.pricing.completion_per_m == 0 %}free{% endif %}">
          {% if model.pricing.completion_per_m == 0 %}Zdarma{% else %}${{ model.pricing.completion_per_m }}/1M{% endif %}
        </span>
      </div>

      <div class="card-tags">
        {% for focus in model.focus limit:3 %}
          <span class="tag">{{ focus }}</span>
        {% endfor %}
      </div>

      {% if model.verdict %}
      <p class="card-verdict">{{ model.verdict | truncate: 150 }}</p>
      {% endif %}

      <a href="{{ model.url }}" class="card-link">Zobrazit detail →</a>
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
});
</script>
