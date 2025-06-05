---
layout: page
title: Lovable.dev - Vibe Coding
permalink: /vibecoding/lovable-dev/
---

# 💖 Lovable.dev

**AI nástroj pro rychlý vývoj moderních webových aplikací**

🔗 [Navštívit Lovable.dev →](https://lovable.dev)

Lovable.dev se specializuje na rychlé vytváření webových aplikací pomocí AI. Platforma umožňuje vývoj responsive designu, implementaci komplexních funkcionalit a integraci s moderními frameworky. Ideální pro rychlé prototypování a MVP vývoj.

## Nejnovější funkce a články

{% assign lovable_posts = site.vibecoding | where_exp: "post", "post.path contains '/lovable-dev/'" | sort: "date" | reverse %}
{% for post in lovable_posts %}
<article class="vibecoding-article">
  <h3>    {{ post.date | date: "%d. %m. %Y" }} - {{ post.title }}</h3>
  <div class="article-content">
    {{ post.content }}
  </div>

</article>
{% endfor %}

{% if lovable_posts.size == 0 %}
<p><em>Zatím zde nejsou žádné články. Sledujte novinky!</em></p>
{% endif %} 