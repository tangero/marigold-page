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
  <li><h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
  
            <div class="post-content clearfix">
            {% if post.thumbnail %}
              {% assign thumbnail_url = post.thumbnail | replace: 'http://', 'https://' %}
              <div class="thumbnail">
                <a href="{{ site.baseurl }}{{ post.url }}">
                  <img src="https://res.cloudinary.com/dvwv5cne3/image/fetch/w_300,h_200,c_fill,g_auto,f_auto,q_auto/{{ thumbnail_url }}" alt="{{ post.title }}">
                </a>
              </div>
            {% endif %}

            <div class="excerpt">
              {{ post.excerpt | strip_html | truncatewords: 60 }} - {{ post.date | date: "%d. %m. %Y" }}
            </div>
  
   
            </li>
{% endfor %}
</ul>

## O této rubrice

Tato rubrika se zaměřuje na nejnovější trendy a vývoj v oblasti umělé inteligence. Diskutujeme zde o různých aspektech AI, od strojového učení až po etické otázky spojené s využíváním AI v každodenním životě.
