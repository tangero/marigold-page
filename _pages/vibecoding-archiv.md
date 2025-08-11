---
layout: vibecoding-default
title: Archiv Vibecoding článků
permalink: /archiv/
---

<h1>📚 Archiv Vibecoding článků</h1>

<p><a href="/">← Zpět na titulní stránku</a></p>

<p>Kompletní přehled všech článků o AI nástrojích pro programování, seřazený od nejnovějších.</p>

{% assign vibecoding_posts = site.vibecoding | sort: "date" | reverse %}
{% assign skip_count = 20 %}

{% for post in vibecoding_posts offset: skip_count %}
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
      {% when "Gemini CLI" %}
        {% assign software_name = "🔵 Gemini CLI" %}
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
      {% when "gemini-cli" %}
        {% assign software_name = "🔵 Gemini CLI" %}
      {% else %}
        {% assign software_name = folder_name | capitalize %}
    {% endcase %}
  {% endif %}

  <article class="archive-article">
    <div class="article-software">
      {% assign link_name = post.sw | default: folder_name %}
      {% comment %} Mapování názvů složek na správné URL {% endcomment %}
      {% case link_name %}
        {% when "claude-code" %}
          {% assign final_link = "claude-code" %}
        {% when "openai-codex" %}
          {% assign final_link = "openai-codex" %}
        {% when "lovable-dev" %}
          {% assign final_link = "lovable-dev" %}
        {% when "gemini-cli" %}
          {% assign final_link = "gemini-cli" %}
        {% when "Gemini CLI" %}
          {% assign final_link = "gemini-cli" %}
        {% when "ostatni" %}
          {% assign final_link = "ostatni" %}
        {% else %}
          {% assign final_link = link_name %}
      {% endcase %}
      <a href="/vibecoding/{{ final_link }}/" class="software-name">{{ software_name }}</a>
      <span class="article-date">{{ post.date | date: "%d. %m. %Y" }}</span>
    </div>

    <h3 class="article-title">
      <a href="{{ post.url | relative_url }}">
        {{ post.title }}
      </a>
    </h3>

    <div class="article-excerpt">
      {% if post.excerpt and post.excerpt != "" %}
        {{ post.excerpt | strip_html | truncatewords: 30 }}
      {% else %}
        {% assign first_paragraph = post.content | split: "</p>" | first | append: "</p>" %}
        {{ first_paragraph | strip_html | truncatewords: 30 }}
      {% endif %}
      <a href="{{ post.url | relative_url }}" class="read-more-inline">→ číst více</a>
    </div>

    {% if post.tags and post.tags.size > 0 %}
      <div class="article-tags-small">
        🏷️ 
        {% for tag in post.tags limit: 2 %}
          <span class="tag-small">{{ tag }}</span>{% unless forloop.last %}, {% endunless %}
        {% endfor %}
      </div>
    {% endif %}
  </article>
{% endfor %}

{% if vibecoding_posts.size <= 20 %}
  <div class="no-more-articles">
    <p>📝 <em>To je všechno! Více článků najdete na <a href="/">titulní stránce</a>.</em></p>
  </div>
{% endif %}

<div class="back-to-top">
  <a href="/">← Zpět na titulní stránku</a>
</div>

<style>
.archive-article {
  margin-bottom: 25px;
  padding-bottom: 15px;
  border-bottom: 1px solid #f0f0f0;
}

.archive-article:last-child {
  border-bottom: none;
}

.article-software {
  margin-bottom: 8px;
  font-size: 0.85em;
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
  color: #888;
  font-size: 0.9em;
}

.article-title {
  margin: 0 0 8px 0;
  font-size: 1.1em;
}

.article-title a {
  text-decoration: none;
  color: #333;
  transition: color 0.2s ease;
}

.article-title a:hover {
  color: #007acc;
}

.article-excerpt {
  color: #555;
  line-height: 1.4;
  font-size: 0.95em;
  margin-bottom: 8px;
}

.read-more-inline {
  color: #007acc;
  text-decoration: none;
  font-weight: 500;
  margin-left: 5px;
}

.read-more-inline:hover {
  color: #005999;
  text-decoration: underline;
}

.article-tags-small {
  color: #888;
  font-size: 0.8em;
}

.tag-small {
  background: #f5f5f5;
  padding: 1px 6px;
  border-radius: 8px;
  color: #666;
}

.no-more-articles {
  text-align: center;
  padding: 30px 0;
  color: #666;
}

.back-to-top {
  text-align: center;
  margin: 30px 0;
  padding: 20px 0;
  border-top: 1px solid #eee;
}

.back-to-top a {
  color: #007acc;
  text-decoration: none;
  font-weight: 500;
  padding: 8px 15px;
  border: 1px solid #007acc;
  border-radius: 6px;
  transition: all 0.2s ease;
}

.back-to-top a:hover {
  background-color: #007acc;
  color: white;
  text-decoration: none;
}
</style>