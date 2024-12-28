---
layout: default
title: Seznam rubrik a tagů
permalink: /rubriky/
---
<h1>Seznam rubrik a tagů</h1>

<ul>
  {% assign tag_count = "" %}

  {% for post in site.posts %}
    {% for tag in post.tags %}
      {% capture tag_key %}{{ tag }}{% endcapture %}
      {% if tag_count contains tag_key %}
        {% assign tag_count[tag_key] = tag_count[tag_key] | plus: 1 %}
      {% else %}
        {% assign tag_count = tag_count | merge: tag_key %}
      {% endif %}
    {% endfor %}
  {% endfor %}
</ul>