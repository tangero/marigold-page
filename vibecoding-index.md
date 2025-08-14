---
layout: page
title: Vibecoding.cz
permalink: /
---

# Vibecoding.cz - AI nástroje pro programování

Průvodce světem AI nástrojů pro programování a vývoj software.

<div style="text-align: center; margin: 2em 0;">
  <a href="/vibecoding/" class="button-primary">📚 Přehled všech nástrojů</a>
</div>

## 🔥 Nejnovější články

{% assign vibecoding_posts = site.vibecoding | sort: "date" | reverse | limit: 10 %}

{% for post in vibecoding_posts %}
<article class="post-preview">
  <h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
  <time>{{ post.date | date: "%d. %m. %Y" }}</time>
  {% if post.post_excerpt %}
    <p>{{ post.post_excerpt }}</p>
  {% endif %}
</article>
{% endfor %}

## 🛠️ Populární nástroje

<div class="tools-grid">
  <div class="tool-card">
    <h3><a href="/vibecoding/claude-code/">🟣 Claude Code</a></h3>
    <p>Terminálový AI asistent od Anthropic</p>
  </div>
  
  <div class="tool-card">
    <h3><a href="/vibecoding/cursor/">⚡ Cursor</a></h3>
    <p>IDE s vestavěnými AI funkcemi</p>
  </div>
  
  <div class="tool-card">
    <h3><a href="/vibecoding/windsurf/">🌊 Windsurf</a></h3>
    <p>Pokročilé IDE pro AI vývoj</p>
  </div>
  
  <div class="tool-card">
    <h3><a href="/vibecoding/lovable-dev/">💖 Lovable.dev</a></h3>
    <p>Rychlý vývoj webových aplikací</p>
  </div>
</div>

<style>
.button-primary {
  display: inline-block;
  padding: 12px 24px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-decoration: none;
  border-radius: 8px;
  font-weight: bold;
  transition: transform 0.2s;
}

.button-primary:hover {
  transform: translateY(-2px);
}

.post-preview {
  margin-bottom: 2em;
  padding-bottom: 1em;
  border-bottom: 1px solid #eee;
}

.post-preview h3 {
  margin: 0 0 0.5em 0;
}

.post-preview time {
  color: #666;
  font-size: 0.9em;
}

.tools-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin: 2em 0;
}

.tool-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 1.5em;
  background: #f9f9f9;
  transition: box-shadow 0.3s;
}

.tool-card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.tool-card h3 {
  margin-top: 0;
}

.tool-card p {
  color: #666;
  margin: 0;
}
</style>