---
layout: page
title: Databutton - Vibe Coding
permalink: /vibecoding/databutton/
---

# 🔴 Databutton

**AI-powered platforma pro vytváření aplikací a analytických nástrojů bez kódování**

🔗 [Navštívit Databutton →](https://databutton.com)

Databutton umožňuje vytvářet aplikace pomocí přirozeného jazyka. Platforma se specializuje na datovou analýzu a vizualizaci s podporou Python ekosystému. 

Pro mne je zajímavá jak dobře zvládnutým plánovám, tak tím, že jde o projekt evropské firmy. Uživatelé mohou rychle prototypovat datové aplikace, vytvářet dashboardy a automatizovat analytické procesy bez nutnosti hlubokých programátorských znalostí.

<div class="vibecoding-details">
  <button class="vibecoding-toggle collapsed" onclick="toggleDetails(this)">
    📋 Detailní informace o Databutton
  </button>
  <div class="vibecoding-content" markdown="1">

### Klíčové vlastnosti:
- **No-code přístup** - vytváření aplikací bez programování
- **Python ekosystém** - podpora populárních knihoven
- **Datová vizualizace** - integrované nástroje pro grafy a dashboardy
- **AI asistent** - pomáhá s návrhem a optimalizací aplikací
- **Cloud deployment** - automatické nasazení do cloudu

### Pro koho je určen:
- **Data analytici** - rychlé prototypy analytických nástrojů
- **Business uživatelé** - vytváření dashboardů bez IT podpory
- **Výzkumníci** - sdílení a vizualizace výsledků
- **Startups** - rychlý vývoj MVP datových produktů

  </div>
</div>

---

## 📰 Články a novinky

{% assign folder_posts = site.vibecoding | where_exp: "post", "post.path contains '/databutton/'" %}
{% assign main_posts = site.posts | where: "sw", "databutton" %}

{% for post in main_posts %}
<article class="vibecoding-article excerpt-article">
  {% if post.thumbnail %}
    <img src="{{ post.thumbnail }}" alt="{{ post.title }}" class="article-thumbnail">
  {% endif %}
  <h3>{{ post.date | date: "%d. %m. %Y" }} - <a href="{{ post.url }}">{{ post.title }}</a></h3>
  <div class="article-excerpt">
    {% if post.excerpt %}
      {{ post.excerpt | strip_html | truncate: 200 }}
    {% else %}
      {{ post.content | strip_html | truncate: 200 }}
    {% endif %}
  </div>
  <a href="{{ post.url }}" class="article-read-more">Číst článek →</a>
  <div class="article-separator"></div>
</article>
{% endfor %}

{% for post in folder_posts %}
<article class="vibecoding-article full-article">
  <h3>{{ post.date | date: "%d. %m. %Y" }} - {{ post.title }}</h3>
  <div class="article-content">
    {{ post.content }}
  </div>
</article>
{% endfor %}

{% if main_posts.size == 0 and folder_posts.size == 0 %}
<p><em>Zatím zde nejsou žádné články. Sledujte novinky!</em></p>
{% endif %} 