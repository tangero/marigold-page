---
layout: page
title: Obrazy
permalink: /obrazy/
---

<h2>Obrazy, které mám rád</h2>

Občas mě zaujme nějaký obraz a udělám si poznámku. Tady. Třeba vás potěší, podívat se na hezký obraz. Nehledejte v tom větší smysl, než si říct něco k obrazu, který mne zaujal. Není v tom ani struktura podle období, ani snaha/možnost vám obraz prodat. Jediná struktura je, že jsem obraz viděl na vlastní oči v originále, tzn. zpravidla s ohledem na to, že jsem byl na výstavě, kde byl presentován. 

{% assign unsorted_posts = site.obrazy | where_exp: "post", "post.order == nil" | sort: "date" | reverse %}
{% for post in unsorted_posts %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}