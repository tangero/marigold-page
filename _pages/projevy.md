---
layout: page
title: Projevy
permalink: /projevy/
---

<div class="post-list">
  {% for post in site.categories.projev %}
    <article class="post-item">
      <h2 class="post-title">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h2>
      <div class="post-meta">
        <time datetime="{{ post.date | date_to_xmlschema }}">
          {{ post.date | date: "%-d. %-m. %Y" }}
        </time>
        {% if post.author %}
          • {{ post.author }}
        {% endif %}
      </div>
      {% if post.post_excerpt %}
        <p class="post-excerpt">{{ post.post_excerpt }}</p>
      {% endif %}
    </article>
  {% endfor %}
</div> 