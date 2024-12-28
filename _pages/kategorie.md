---
layout: page
permalink: /kategorie/
title: Seznam kategorií
---

<h1>Seznam kategorií a jejich počet článků</h1>

<p>Seznam kategorií ve formátu YAML:</p>

<pre>
categories_count:
  {% assign other_categories = "" %}
  {% for category in site.categories %}
    {% capture category_name %}{{ category | first }}{% endcapture %}
    {% assign count = site.categories[category_name].size %}
    
    {% if count > 2 %}
      - {{ category_name }}: {{ count }}
    {% else %}
      {% assign other_categories = other_categories | append: category_name | append: "," %}
    {% endif %}
  {% endfor %}

  {% if other_categories != "" %}
    - Ostatní:
      {% assign other_categories_list = other_categories | split: "," %}
      {% for category in other_categories_list %}
        {% if category != "" %}
          - {{ category }}: {{ site.categories[category].size }}
        {% endif %}
      {% endfor %}
  {% endif %}
</pre>