---
layout: page
title: Databutton - Vibe Coding
permalink: /vibecoding/databutton/
---

# 🔴 Databutton

**AI-powered platforma pro vytváření aplikací a analytických nástrojů bez kódování**

🔗 [Navštívit Databutton →](https://databutton.com)

Databutton umožňuje vytvářet aplikace pomocí přirozeného jazyka. Platforma se specializuje na datovou analýzu a vizualizaci s podporou Python ekosystému. Uživatelé mohou rychle prototypovat datové aplikace, vytvářet dashboardy a automatizovat analytické procesy bez nutnosti hlubokých programátorských znalostí. Pro mne je zajímavá jak dobře zvládnutým plánovám, tak tím, že jde o projekt evropské firmy. 

## Nejnovější funkce a články

{% assign databutton_posts = site.vibecoding | where_exp: "post", "post.path contains '/databutton/'" | sort: "date" | reverse %}
{% for post in databutton_posts %}
<article class="vibecoding-article">
  <h3>    {{ post.date | date: "%d. %m. %Y" }} - {{ post.title }}</h3>
  <div class="article-content">
    {{ post.content }}
  </div>
</article>
{% endfor %}

{% if databutton_posts.size == 0 %}
<p><em>Zatím zde nejsou žádné články. Sledujte novinky!</em></p>
{% endif %} 