---
layout: page
title: Vibe Coding
permalink: /vibecoding/
---

# Vibe Coding - AI nástroje pro programování

Přehled nejmodernějších AI nástrojů a služeb pro vibe coding a programování s pomocí umělé inteligence.

## 🛠️ Služby a nástroje

<div class="vibecoding-matrix">
  <div class="service-card">
    <h3><a href="/vibecoding/databutton/">🔴 Databutton</a></h3>
    <p>Evropská AI-powered web platforma pro vytváření aplikací bez kódování</p>
  </div>
  
  <div class="service-card">
    <h3><a href="/vibecoding/claude-code/">🟣 Claude Code</a></h3>
    <p>Pokročilý terminálový asistent pro programování a analýzu kódu od Anthropicu</p>
  </div>
  
  <div class="service-card">
    <h3><a href="/vibecoding/openai-codex/">🟢 OpenAI Codex</a></h3>
    <p>AI model pro generování a porozumění kódu od OpenAI</p>
  </div>
  
  <div class="service-card">
    <h3><a href="/vibecoding/cursor/">🖱️ Cursor</a></h3>
    <p>Kompletní IDE založené na VS CODE s AI funkcemi pro rychlý vývoj a refactoring kódu</p>
  </div>
  
  <div class="service-card">
    <h3><a href="/vibecoding/lovable-dev/">💖 Lovable.dev</a></h3>
    <p>AI nástroj pro rychlý vývoj moderních webových aplikací</p>
  </div>
  
  <div class="service-card">
    <h3><a href="/vibecoding/windsurf/">🌊 Windsurf</a></h3>
    <p>Inteligentní IDE s pokročilými AI funkcemi pro vývoj</p>
  </div>
  
  <div class="service-card">
    <h3><a href="/vibecoding/tempolabs/">⚡ Tempolabs</a></h3>
    <p>Rychlý webový AI nástroj pro prototypování a vývoj aplikací</p>
  </div>
  
  <div class="service-card">
    <h3><a href="/vibecoding/memex/">🧠 Memex</a></h3>
    <p>Desktop aplikace pro vývoj software, velmi autonomní a za dobré peníze</p>
  </div>
</div>

## 📰 Nejnovější články

{% assign all_posts = site.vibecoding | sort: "date" | reverse %}
{% for post in all_posts %}
  {% assign content_length = post.content | strip_html | size %}
  {% assign is_short = false %}
  {% if content_length < 1000 %}
    {% assign is_short = true %}
  {% endif %}

  <article class="vibecoding-article {% if is_short %}full-article{% else %}excerpt-article{% endif %}">
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
        <span class="article-date">{{ post.date | date: "%d. %m. %Y" }}</span> - {{ post.title }}
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
  color: #007acc;
  text-decoration: none;
  font-weight: 500;
}

.article-read-more:hover {
  text-decoration: underline;
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
</style> 