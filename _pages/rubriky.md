---
layout: default
title: Seznam rubrik a tagů
permalink: /rubriky/
---
<h1>Seznam rubrik a tagů</h1>

<ul>
  {% assign tag_count = {} %}

  {% for post in site.posts %}
    {% for tag in post.tags %}
      {% if tag_count[tag] %}
        {% assign tag_count[tag] = tag_count[tag] | plus: 1 %}
      {% else %}
        {% assign tag_count[tag] = 1 %}
      {% endif %}
    {% endfor %}
  {% endfor %}

  {% for tag, count in tag_count %}
    <li>{{ tag }}: {{ count }} příspěvků</li>
  {% endfor %}
</ul>