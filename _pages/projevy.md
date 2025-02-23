---
layout: page
title: Projevy
permalink: /projevy/
---

Některé projevy či přednášky zahraničních autorů, které jsem považoval za důležité a přeložil jsem je do češtiny. To, že jsou tady, neznamená, že s nimi musím souhlasit, ale pokud s nimi vedu polemiku, tak ve vyhrazeném článku, nikoliv v textu přepisu přednášky či projevu. 

<div class="post-list">
  {% for post in site.categories.projev %}
    <article class="post">
      <h1 class="post-title">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h1>
      
      <div class="post-content clearfix">
        {% if post.thumbnail %}
          {% assign thumbnail_url = post.thumbnail | replace: 'http://', 'https://' %}
          <div class="thumbnail">
            <a href="{{ post.url | relative_url }}">
              <img src="https://res.cloudinary.com/dvwv5cne3/image/fetch/w_300,h_200,c_fill,g_auto,f_auto,q_auto/{{ thumbnail_url }}" alt="{{ post.title }}">
            </a>
          </div>
        {% endif %}
        
        {% if post.post_excerpt %}
          <div class="excerpt">
            {{ post.post_excerpt | strip_html | truncatewords: 60 }}
          </div>
        {% endif %}
      </div>
      
      {% if post.summary_points %}
        <div class="quick-summary">
          <div class="quick-summary-header">
            <svg class="summary-icon" viewBox="0 0 24 24" width="24" height="24">
              <path fill="currentColor" d="M14,17H7V15H14M17,13H7V11H17M17,9H7V7H17M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3Z" />
            </svg>
            <span>Rychlé shrnutí článku</span>
          </div>
          <ul class="summary-points">
            {% for point in post.summary_points %}
              <li>{{ point }}</li>
            {% endfor %}
          </ul>
        </div>
      {% endif %}
      
      <div class="post-meta">
        <time datetime="{{ post.date | date_to_xmlschema }}">
          {{ post.date | date: "%-d. %-m. %Y" }}
        </time>
      </div>
    </article>
    <hr>
  {% endfor %}
</div> 