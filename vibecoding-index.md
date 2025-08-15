---
layout: vibecoding-default
permalink: /
custom_css: /assets/vibecoding-index.css
---

<div class="homepage">


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

<link rel="stylesheet" href="/assets/vibecoding-index.css">

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

// Dropdown menu funkce
function toggleDropdown() {
  const dropdown = document.getElementById('platformsDropdown');
  const arrow = document.querySelector('.dropdown-arrow');
  
  if (dropdown.classList.contains('show')) {
    dropdown.classList.remove('show');
    arrow.textContent = '▼';
  } else {
    dropdown.classList.add('show');
    arrow.textContent = '▲';
  }
}

// Zavření dropdown při kliknutí mimo
document.addEventListener('click', function(e) {
  const dropdown = document.getElementById('platformsDropdown');
  const btn = document.querySelector('.dropdown-btn');
  
  if (!btn.contains(e.target) && !dropdown.contains(e.target)) {
    dropdown.classList.remove('show');
    document.querySelector('.dropdown-arrow').textContent = '▼';
  }
});
</script>