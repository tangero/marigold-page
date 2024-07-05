---
layout: page
title: AI Rubrika
permalink: /ai/
---

# Vítejte v AI rubrice

Zde najdete články zaměřené na umělou inteligenci a její využití v různých oblastech.

## AI články

<h2>Vybrané příspěvky</h2>
   {% assign sorted_posts = site.ai | where_exp: "post", "post.order" | sort: "order" %}
   {% for post in sorted_posts %}
     - [{{ post.title }}]({{ post.url }})
   {% endfor %}

<h2>Další příspěvky</h2>
   {% assign unsorted_posts = site.ai | where_exp: "post", "post.order == nil" | sort: "date" | reverse %}
   {% for post in unsorted_posts %}
     - [{{ post.title }}]({{ post.url }})
   {% endfor %}

## O této rubrice

Tato rubrika se zaměřuje na nejnovější trendy a vývoj v oblasti umělé inteligence. Diskutujeme zde o různých aspektech AI, od strojového učení až po etické otázky spojené s využíváním AI v každodenním životě.
