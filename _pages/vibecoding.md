---
layout: page
title: Vibe Coding
permalink: /vibecoding/
---

# Vibe Coding - AI nástroje pro programování

Přehled nejmodernějších AI nástrojů a služeb pro vibe coding a programování s pomocí umělé inteligence.

## 🛠️ Služby a nástroje

<div class="tools-categories-row">
  
  <!-- Desktop IDE -->
  <div class="category-box">
    <button class="category-toggle collapsed" onclick="toggleCategory(this)">
      💻 Desktop IDE <span class="toggle-icon">▼</span>
    </button>
    <div class="category-content">
      <div class="service-card">
        <h4><a href="/vibecoding/cursor/">🖱️ Cursor</a></h4>
        <p>Kompletní IDE založené na VS CODE s AI funkcemi pro rychlý vývoj a refactoring kódu</p>
      </div>
      <div class="service-card">
        <h4><a href="/vibecoding/windsurf/">🌊 Windsurf</a></h4>
        <p>Inteligentní IDE s pokročilými AI funkcemi pro vývoj</p>
      </div>
      <div class="service-card">
        <h4><a href="/vibecoding/memex/">🧠 Memex</a></h4>
        <p>Desktop aplikace pro vývoj software, velmi autonomní a za dobré peníze</p>
      </div>
    </div>
  </div>

  <!-- Cloudové nástroje -->
  <div class="category-box">
    <button class="category-toggle collapsed" onclick="toggleCategory(this)">
      ☁️ Cloudové nástroje <span class="toggle-icon">▼</span>
    </button>
    <div class="category-content">
      <div class="service-card">
        <h4><a href="/vibecoding/databutton/">🔴 Databutton</a></h4>
        <p>Evropská AI-powered web platforma pro vytváření aplikací bez kódování</p>
      </div>
      <div class="service-card">
        <h4><a href="/vibecoding/lovable-dev/">💖 Lovable.dev</a></h4>
        <p>AI nástroj pro rychlý vývoj moderních webových aplikací</p>
      </div>
      <div class="service-card">
        <h4><a href="/vibecoding/tempolabs/">⚡ Tempolabs</a></h4>
        <p>Rychlý webový AI nástroj pro prototypování a vývoj aplikací</p>
      </div>
      <div class="service-card">
        <h4><a href="/vibecoding/replit/">🟠 Replit</a></h4>
        <p>AI-powered cloudová platforma pro vývoj a nasazení aplikací s Replit Agent</p>
      </div>
    </div>
  </div>

  <!-- Terminálové a chat nástroje -->
  <div class="category-box">
    <button class="category-toggle collapsed" onclick="toggleCategory(this)">
      🤖 Terminálové a chat nástroje <span class="toggle-icon">▼</span>
    </button>
    <div class="category-content">
      <div class="service-card">
        <h4><a href="/vibecoding/claude-code/">�� Claude Code</a></h4>
        <p>Pokročilý terminálový asistent pro programování a analýzu kódu od Anthropicu</p>
      </div>
      <div class="service-card">
        <h4><a href="/vibecoding/openai-codex/">🟢 OpenAI Codex</a></h4>
        <p>AI model pro generování a porozumění kódu od OpenAI</p>
      </div>
    </div>
  </div>

</div>

<style>
.tools-categories-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin: 30px 0;
}

.category-box {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  background: #f8f9fa;
}

.category-toggle {
  width: 100%;
  padding: 15px 20px;
  background: #f8f9fa;
  border: none;
  text-align: left;
  font-size: 16px;
  font-weight: 600;
  color: #333;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: background 0.2s ease;
}

.category-toggle:hover {
  background: #e9ecef;
}

.category-toggle.collapsed .toggle-icon {
  transform: rotate(-90deg);
}

.toggle-icon {
  transition: transform 0.3s ease;
}

.category-content {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease;
  background: white;
}

.category-toggle:not(.collapsed) + .category-content {
  max-height: 500px;
  padding: 20px;
}

.service-card {
  margin-bottom: 15px;
  padding: 15px;
  background: #fafafa;
  border-radius: 6px;
  border: 1px solid #eee;
}

.service-card:last-child {
  margin-bottom: 0;
}

.service-card h4 {
  margin: 0 0 8px 0;
  font-size: 16px;
}

.service-card h4 a {
  text-decoration: none;
  color: #333;
}

.service-card h4 a:hover {
  color: #007acc;
}

.service-card p {
  margin: 0;
  font-size: 14px;
  color: #666;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .tools-categories-row {
    grid-template-columns: 1fr;
  }
}
</style>

<script>
function toggleCategory(button) {
  button.classList.toggle('collapsed');
}
</script>

## 📰 Nejnovější články

{% assign vibecoding_posts = site.vibecoding | sort: "date" | reverse %}
{% assign category_posts = site.posts | where_exp: "post", "post.categories contains 'vibecoding'" | sort: "date" | reverse %}
{% assign all_posts = vibecoding_posts | concat: category_posts | sort: "date" | reverse %}

{% for post in all_posts %}
  {% assign content_length = post.content | strip_html | size %}
  {% assign is_short = false %}
  {% if content_length < 1000 %}
    {% assign is_short = true %}
  {% endif %}

  {% comment %} Získání názvu softwaru z URL nebo front matter {% endcomment %}
  {% assign software_name = "" %}
  {% if post.sw %}
    {% case post.sw %}
      {% when "databutton" %}
        {% assign software_name = "🔴 Databutton" %}
      {% when "claude-code" %}
        {% assign software_name = "🟣 Claude Code" %}
      {% when "openai-codex" %}
        {% assign software_name = "🟢 OpenAI Codex" %}
      {% when "cursor" %}
        {% assign software_name = "🖱️ Cursor" %}
      {% when "lovable-dev" %}
        {% assign software_name = "💖 Lovable.dev" %}
      {% when "windsurf" %}
        {% assign software_name = "🌊 Windsurf" %}
      {% when "tempolabs" %}
        {% assign software_name = "⚡ Tempolabs" %}
      {% when "memex" %}
        {% assign software_name = "🧠 Memex" %}
      {% when "replit" %}
        {% assign software_name = "🟠 Replit" %}
      {% else %}
        {% assign software_name = post.sw | capitalize %}
    {% endcase %}
  {% else %}
    {% assign path_parts = post.path | split: "/" %}
    {% assign folder_name = path_parts[1] %}
    {% case folder_name %}
      {% when "databutton" %}
        {% assign software_name = "🔴 Databutton" %}
      {% when "claude-code" %}
        {% assign software_name = "🟣 Claude Code" %}
      {% when "openai-codex" %}
        {% assign software_name = "🟢 OpenAI Codex" %}
      {% when "cursor" %}
        {% assign software_name = "🖱️ Cursor" %}
      {% when "lovable-dev" %}
        {% assign software_name = "💖 Lovable.dev" %}
      {% when "windsurf" %}
        {% assign software_name = "🌊 Windsurf" %}
      {% when "tempolabs" %}
        {% assign software_name = "⚡ Tempolabs" %}
      {% when "memex" %}
        {% assign software_name = "🧠 Memex" %}
      {% when "replit" %}
        {% assign software_name = "🟠 Replit" %}
      {% else %}
        {% assign software_name = folder_name | capitalize %}
    {% endcase %}
  {% endif %}

  <article class="vibecoding-article {% if is_short %}full-article{% else %}excerpt-article{% endif %}">
    <div class="article-software">
      <a href="/vibecoding/{{ post.sw | default: folder_name }}/" class="software-name">{{ software_name }}</a>
      <span class="article-date">{{ post.date | date: "%d. %m. %Y" }}</span>
    </div>

    {% if post.thumbnail %}
      {% assign thumbnail_url = post.thumbnail | replace: 'http://', 'https://' %}
      <div class="article-thumbnail">
        <a href="{{ post.url | relative_url }}">
          <img src="https://res.cloudinary.com/dvwv5cne3/image/fetch/w_300,h_200,c_fill,g_auto,f_auto,q_auto/{{ thumbnail_url }}" alt="{{ post.title }}">
        </a>
      </div>
    {% endif %}

    <h3 class="article-title">
      <a href="{{ post.url | relative_url }}">
        {{ post.title }}
      </a>
    </h3>

    <div class="article-content">
      {% if is_short %}
        {{ post.content }}
      {% else %}
        <div class="article-excerpt">
          {% if post.excerpt and post.excerpt != "" %}
            {{ post.excerpt | strip_html | truncatewords: 50 }}
          {% else %}
            {% assign first_paragraph = post.content | split: "</p>" | first | append: "</p>" %}
            {{ first_paragraph | strip_html | truncatewords: 50 }}
          {% endif %}
        </div>
        
        <div class="article-read-more-wrapper">
          <a href="{{ post.url | relative_url }}" class="article-read-more">
            📖 Pokračování... →
          </a>
        </div>
      {% endif %}
    </div>

    {% if post.tags and post.tags.size > 0 %}
      <div class="article-meta">
        <span class="article-tags">
          🏷️ 
          {% for tag in post.tags limit: 3 %}
            <span class="tag">{{ tag }}</span>{% unless forloop.last %}, {% endunless %}
          {% endfor %}
        </span>
      </div>
    {% endif %}

    <div class="article-separator"></div>
  </article>
{% endfor %}

{% if all_posts.size == 0 %}
  <div class="no-articles">
    <p>📝 <em>Zatím zde nejsou žádné články. Sledujte novinky!</em></p>
  </div>
{% endif %}

<style>
.vibecoding-matrix {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin: 30px 0;
}

.service-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  background: #f9f9f9;
  transition: box-shadow 0.3s ease;
}

.service-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.service-card h3 {
  margin-top: 0;
  margin-bottom: 10px;
}

.service-card h3 a {
  text-decoration: none;
  color: #333;
}

.service-card h3 a:hover {
  color: #007acc;
}

.vibecoding-article {
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 1px solid #eee;
}

.article-meta {
  color: #666;
  font-size: 0.9em;
  margin-top: 10px;
}

.article-thumbnail {
  margin-bottom: 15px;
}

.article-thumbnail img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
}

.article-title {
  margin: 0 0 10px 0;
}

.article-title a {
  text-decoration: none;
  color: #333;
}

.article-date {
  color: #666;
  font-size: 0.9em;
}

.article-excerpt {
  color: #444;
  line-height: 1.6;
  margin-bottom: 15px;
}

.article-read-more-wrapper {
  margin-top: 10px;
}

.article-read-more {
  display: inline-block;
  color: #999;
  text-decoration: none;
  font-weight: 500;
  transition: all 0.2s ease;
  background-color: #f8f8f8;
  padding: 4px 8px;
  border-radius: 4px;
}

.article-read-more:hover {
  color: #666;
  background-color: #fff3cd;
  text-decoration: none;
}

.article-separator {
  margin-top: 20px;
  border-bottom: 1px solid #eee;
}

.tag {
  background: #f0f0f0;
  padding: 2px 8px;
  border-radius: 12px;
  font-size: 0.85em;
  color: #666;
}

.no-articles {
  text-align: center;
  padding: 40px 0;
  color: #666;
}

.article-software {
  margin-bottom: 10px;
  font-size: 0.9em;
  color: #666;
}

.software-name {
  font-weight: 600;
  color: #007acc;
  margin-right: 10px;
  text-decoration: none;
  transition: color 0.2s ease;
}

.software-name:hover {
  color: #005999;
  text-decoration: underline;
}

.article-date {
  color: #666;
}
</style> 