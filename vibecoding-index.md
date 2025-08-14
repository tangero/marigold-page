---
layout: vibecoding-default
permalink: /
---

<div class="vibecoding-homepage">
  <div class="hero-section">
    <h1>Vibecoding.cz</h1>
    <p class="hero-subtitle">Průvodce světem AI nástrojů pro programování a vývoj software</p>
  </div>

  <div class="quick-links">
    <a href="/claude-code/" class="quick-link">🟣 Claude Code</a>
    <a href="/cursor/" class="quick-link">⚡ Cursor</a>
    <a href="/windsurf/" class="quick-link">🌊 Windsurf</a>
    <a href="/lovable-dev/" class="quick-link">💖 Lovable.dev</a>
    <a href="/replit/" class="quick-link">🚀 Replit</a>
  </div>

  <h2 class="section-title">📰 Nejnovější články</h2>

  <div class="articles-list" id="articles-container">
    {% assign all_posts = site.vibecoding | sort: "date" | reverse %}
    
    {% for post in all_posts %}
      {% comment %} Získání názvu softwaru z cesty {% endcomment %}
      {% assign path_parts = post.path | split: "/" %}
      {% assign folder_name = path_parts[1] %}
      {% assign software_name = "" %}
      
      {% case folder_name %}
        {% when "claude-code" %}
          {% assign software_name = "🟣 Claude Code" %}
        {% when "cursor" %}
          {% assign software_name = "⚡ Cursor" %}
        {% when "windsurf" %}
          {% assign software_name = "🌊 Windsurf" %}
        {% when "lovable-dev" %}
          {% assign software_name = "💖 Lovable.dev" %}
        {% when "databutton" %}
          {% assign software_name = "📊 Databutton" %}
        {% when "replit" %}
          {% assign software_name = "🚀 Replit" %}
        {% when "gemini-cli" %}
          {% assign software_name = "💎 Gemini CLI" %}
        {% when "openai-codex" %}
          {% assign software_name = "🤖 OpenAI Codex" %}
        {% when "tempolabs" %}
          {% assign software_name = "⚡ Tempolabs" %}
        {% when "memex" %}
          {% assign software_name = "🧠 Memex" %}
        {% else %}
          {% assign software_name = folder_name | capitalize %}
      {% endcase %}

      <article class="article-preview" data-index="{{ forloop.index }}">
        <div class="article-meta">
          <span class="article-software">{{ software_name }}</span>
          <time class="article-date">{{ post.date | date: "%d. %m. %Y" }}</time>
        </div>
        
        <h3 class="article-title">
          <a href="{{ post.url }}">{{ post.title }}</a>
        </h3>
        
        {% if post.post_excerpt %}
          <p class="article-excerpt">{{ post.post_excerpt }}</p>
        {% elsif post.excerpt %}
          <p class="article-excerpt">{{ post.excerpt | strip_html | truncatewords: 50 }}</p>
        {% else %}
          <p class="article-excerpt">{{ post.content | strip_html | truncatewords: 50 }}</p>
        {% endif %}
        
        <a href="{{ post.url }}" class="read-more">Číst více →</a>
      </article>
    {% endfor %}
  </div>

  <div class="pagination" id="pagination-container"></div>
</div>

<style>
.vibecoding-homepage {
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

.hero-section {
  text-align: center;
  margin-bottom: 3rem;
  padding: 2rem 0;
}

.hero-section h1 {
  font-size: 3rem;
  margin-bottom: 0.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 1.2rem;
  color: #666;
}

.quick-links {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 3rem;
}

.quick-link {
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%);
  border-radius: 25px;
  text-decoration: none;
  color: #333;
  transition: all 0.3s ease;
  border: 1px solid #ddd;
}

.quick-link:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  background: linear-gradient(135deg, #fff 0%, #f0f0f0 100%);
}

.section-title {
  font-size: 1.8rem;
  margin: 2rem 0 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid #eee;
}

.articles-list {
  margin-bottom: 3rem;
}

.article-preview {
  margin-bottom: 2.5rem;
  padding-bottom: 2rem;
  border-bottom: 1px solid #eee;
  display: none;
}

.article-preview.active {
  display: block;
}

.article-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.article-software {
  font-weight: 600;
  color: #667eea;
  font-size: 0.9rem;
}

.article-date {
  color: #999;
  font-size: 0.9rem;
}

.article-title {
  margin: 0.5rem 0 1rem;
  font-size: 1.5rem;
}

.article-title a {
  color: #333;
  text-decoration: none;
  transition: color 0.2s ease;
}

.article-title a:hover {
  color: #667eea;
}

.article-excerpt {
  color: #666;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.read-more {
  color: #667eea;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.2s ease;
}

.read-more:hover {
  color: #764ba2;
  text-decoration: underline;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 0.5rem;
  margin-top: 3rem;
  padding: 1.5rem 0;
  border-top: 2px solid #eee;
}

.pagination-btn {
  padding: 0.5rem 1rem;
  background: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
  color: #333;
}

.pagination-btn:hover:not(:disabled) {
  background: #667eea;
  color: white;
  border-color: #667eea;
}

.pagination-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination-btn.active {
  background: #667eea;
  color: white;
  border-color: #667eea;
}

.pagination-dots {
  color: #999;
  padding: 0 0.5rem;
}

.pagination-info {
  color: #666;
  font-weight: 500;
  margin: 0 1rem;
}

@media (max-width: 768px) {
  .hero-section h1 {
    font-size: 2rem;
  }
  
  .hero-subtitle {
    font-size: 1rem;
  }
  
  .quick-links {
    flex-direction: column;
    align-items: stretch;
  }
  
  .article-meta {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.3rem;
  }
  
  .pagination {
    flex-wrap: wrap;
  }
}
</style>

<script>
(function() {
  const ITEMS_PER_PAGE = 10;
  let currentPage = 1;
  let totalPages = 1;
  let articles = [];

  function initPagination() {
    articles = document.querySelectorAll('.article-preview');
    totalPages = Math.ceil(articles.length / ITEMS_PER_PAGE);
    
    // Získání čísla stránky z URL
    const urlParams = new URLSearchParams(window.location.search);
    const pageParam = urlParams.get('strana');
    if (pageParam) {
      currentPage = parseInt(pageParam) || 1;
    }
    
    showPage(currentPage);
    renderPagination();
  }

  function showPage(page) {
    const start = (page - 1) * ITEMS_PER_PAGE;
    const end = start + ITEMS_PER_PAGE;
    
    articles.forEach((article, index) => {
      if (index >= start && index < end) {
        article.classList.add('active');
      } else {
        article.classList.remove('active');
      }
    });
    
    // Scroll nahoru při změně stránky
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function renderPagination() {
    const container = document.getElementById('pagination-container');
    if (totalPages <= 1) {
      container.style.display = 'none';
      return;
    }
    
    let html = '';
    
    // Tlačítko Předchozí
    if (currentPage > 1) {
      html += `<button class="pagination-btn" onclick="changePage(${currentPage - 1})">← Předchozí</button>`;
    }
    
    // Čísla stránek
    let startPage = Math.max(1, currentPage - 2);
    let endPage = Math.min(totalPages, currentPage + 2);
    
    if (startPage > 1) {
      html += `<button class="pagination-btn" onclick="changePage(1)">1</button>`;
      if (startPage > 2) {
        html += `<span class="pagination-dots">...</span>`;
      }
    }
    
    for (let i = startPage; i <= endPage; i++) {
      html += `<button class="pagination-btn ${i === currentPage ? 'active' : ''}" onclick="changePage(${i})">${i}</button>`;
    }
    
    if (endPage < totalPages) {
      if (endPage < totalPages - 1) {
        html += `<span class="pagination-dots">...</span>`;
      }
      html += `<button class="pagination-btn" onclick="changePage(${totalPages})">${totalPages}</button>`;
    }
    
    // Tlačítko Další
    if (currentPage < totalPages) {
      html += `<button class="pagination-btn" onclick="changePage(${currentPage + 1})">Další →</button>`;
    }
    
    // Info o stránce
    html += `<span class="pagination-info">Strana ${currentPage} z ${totalPages}</span>`;
    
    container.innerHTML = html;
  }

  window.changePage = function(page) {
    if (page < 1 || page > totalPages) return;
    
    currentPage = page;
    showPage(currentPage);
    renderPagination();
    
    // Aktualizace URL bez reloadu stránky
    const url = new URL(window.location);
    if (page === 1) {
      url.searchParams.delete('strana');
    } else {
      url.searchParams.set('strana', page);
    }
    window.history.pushState({}, '', url);
  }

  // Inicializace při načtení stránky
  document.addEventListener('DOMContentLoaded', initPagination);
})();
</script>