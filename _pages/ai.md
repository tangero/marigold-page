---
layout: page
title: AI čili Umělá Inteligence
permalink: /ai/
---

Zde najdete články zaměřené na umělou inteligenci a její využití v různých oblastech.

<h2>Základy fungování AI</h2>

{% assign emoji_chars = "⌚️⌨️📱📲💻⌨️🖥️🖨️🖱️🖲️🕹️🗜️💽💾💿📀📼📷📸📹🎥📽️" | split: '' %}
{% assign sorted_posts = site.ai | where_exp: "post", "post.order" | sort: "order" %}

<ul>
{% for post in sorted_posts %}
  {% assign random_index = forloop.index | plus: post.title.size | modulo: emoji_chars.size %}
  {% assign random_emoji = emoji_chars[random_index] %}
  <li>{{ random_emoji }} <a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}
</ul>


<h2>Rady, tipy a triky</h2>
{% assign unsorted_posts = site.ai | where_exp: "post", "post.order == nil" | sort: "date" | reverse %}
{% for post in unsorted_posts %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}

<h2>Články a aktuality z oblasti Umělé inteligence</h2>
{% assign ai_posts = site.posts | where: "categories", "AI" %}
{% assign ui_posts = site.posts | where: "categories", "Umělá inteligence" %}
{% assign combined_posts = ai_posts | concat: ui_posts | uniq | sort: "date" | reverse %}

<ul>
{% for post in combined_posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date: "%d. %m. %Y" }} (            {% assign m = post.date | date: "%-m" %}
            {{ post.date | date: "%-d." }}
            {% case m %}
              {% when '1' %}leden
              {% when '2' %}únor
              {% when '3' %}březen
              {% when '4' %}duben
              {% when '5' %}květen
              {% when '6' %}červen
              {% when '7' %}červenec
              {% when '8' %}srpen
              {% when '9' %}září
              {% when '10' %}říjen
              {% when '11' %}listopad
              {% when '12' %}prosinec
            {% endcase %}
            {{ post.date | date: "%Y" }})
            </li>
{% endfor %}
</ul>

## O této rubrice

Tato rubrika se zaměřuje na nejnovější trendy a vývoj v oblasti umělé inteligence. Diskutujeme zde o různých aspektech AI, od strojového učení až po etické otázky spojené s využíváním AI v každodenním životě.
