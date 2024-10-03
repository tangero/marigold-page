---
layout: page
title: Obrazy
permalink: /obrazy/
---

<h2>Obrazy, které mám rád</h2>

Občas mě zaujme nějaký obraz a udělám si poznámku. Tady. Třeba vás potěší, podívat se na hezký obraz! 

{% assign unsorted_posts = site.obrazy | where_exp: "post", "post.order == nil" | sort: "date" | reverse %}
{% for post in unsorted_posts %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}