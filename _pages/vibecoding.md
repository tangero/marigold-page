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

{% include vibecoding-articles.html tool_folder="vibecoding" tool_sw="vibecoding" %}

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