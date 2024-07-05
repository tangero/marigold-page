---
layout: page
title: AI čili Umělá Inteligence
permalink: /ai/
---

Zde najdete články zaměřené na umělou inteligenci a její využití v různých oblastech.

<h2>Vybrané příspěvky</h2>

{% assign emoji_chars = "⌚️⌨️📱📲💻⌨️🖥️🖨️🖱️🖲️🕹️🗜️💽💾💿📀📼📷📸📹🎥📽️" | split: '' %}
{% assign sorted_posts = site.ai | where_exp: "post", "post.order" | sort: "order" %}
<ul>
{% for post in site.posts %}
  {% assign random_index = forloop.index | plus: post.title.size | modulo: emoji_chars.size %}
  {% assign random_emoji = emoji_chars[random_index] %}
  <li>{{ random_emoji }} <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>


<h2>Další příspěvky</h2>
{% assign unsorted_posts = site.ai | where_exp: "post", "post.order == nil" | sort: "date" | reverse %}
{% for post in unsorted_posts %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}

## O této rubrice

Tato rubrika se zaměřuje na nejnovější trendy a vývoj v oblasti umělé inteligence. Diskutujeme zde o různých aspektech AI, od strojového učení až po etické otázky spojené s využíváním AI v každodenním životě.
