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
    <p>AI-powered platforma pro vytváření aplikací a analytických nástrojů bez kódování</p>
  </div>
  
  <div class="service-card">
    <h3><a href="/vibecoding/claude-code/">🟣 Claude Code</a></h3>
    <p>Pokročilý AI asistent pro programování a analýzu kódu od Anthropic</p>
  </div>
  
  <div class="service-card">
    <h3><a href="/vibecoding/openai-codex/">🟢 OpenAI Codex</a></h3>
    <p>Revolučný AI model pro generování a porozumění kódu od OpenAI</p>
  </div>
  
  <div class="service-card">
    <h3><a href="/vibecoding/cursor/">🖱️ Cursor</a></h3>
    <p>AI-first editor s pokročilými funkcemi pro rychlý vývoj a refactoring kódu</p>
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
    <p>Rychlý AI nástroj pro prototypování a vývoj aplikací</p>
  </div>
</div>

## 📰 Nejnovější články

{% assign vibecoding_posts = site.vibecoding | sort: "date" | reverse %}
{% for post in vibecoding_posts limit: 10 %}
<h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
<div class="post-content clearfix">
{% if post.thumbnail %}
{% assign thumbnail_url = post.thumbnail | replace: 'http://', 'https://' %}
<div class="thumbnail">
<a href="{{ site.baseurl }}{{ post.url }}">
 <img src="https://res.cloudinary.com/dvwv5cne3/image/fetch/w_300,h_200,c_fill,g_auto,f_auto,q_auto/{{ thumbnail_url }}" alt="{{ post.title }}">
</a>
</div>
{% endif %}
</div>

<div class="excerpt">
{{ post.excerpt | strip_html | truncatewords: 60 }} - {{ post.date | date: "%d. %m. %Y" }}
</div>
{% endfor %}

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
</style> 