---
title: Vyhledávání na Marigold.cz
description: "Vyhledávání na webu Marigold.cz"
layout: page
permalink: /search/
exclude_from_search: true
---

<div class="search-container">
  <h3>Vyhledávání na Marigoldovi</h3>

  <form action="/search/" method="get">
    <div class="search-box">
      <input type="text" id="search-box" name="query" placeholder="Hledat..." />
      <button type="submit">Hledat</button>
    </div>
  </form>

  <div id="search-results"></div>
</div>

<style>
  .search-container {
    max-width: 800px;
    margin: 0 auto;
  }
  .search-box {
    display: flex;
    margin-bottom: 2rem;
  }
  .search-box input {
    flex: 1;
    padding: 0.7rem;
    font-size: 1rem;
    border: 1px solid #ddd;
    border-radius: 3px 0 0 3px;
  }
  .search-box button {
    padding: 0.7rem 1.5rem;
    background: #4183C4;
    color: white;
    border: none;
    border-radius: 0 3px 3px 0;
    cursor: pointer;
  }
  .search-result-item {
    margin-bottom: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #eee;
  }
  .search-result-item h3 {
    margin-bottom: 0.5rem;
  }
  .search-result-meta {
    display: flex;
    margin-top: 0.5rem;
    font-size: 0.85rem;
    color: #777;
  }
  .search-result-category {
    background: #f0f0f0;
    padding: 0.2rem 0.5rem;
    border-radius: 3px;
    margin-right: 0.5rem;
  }
</style>

<script>
  window.store = {
    {% for post in site.posts %}
      "{{ post.url | slugify }}": {
        "title": "{{ post.title | xml_escape }}",
        "content": {{ post.content | strip_html | strip_newlines | jsonify }},
        "url": "{{ site.baseurl }}{{ post.url | xml_escape }}",
        "category": "{{ post.categories | join: ', ' | xml_escape }}",
        "tags": "{{ post.tags | join: ', ' | xml_escape }}",
        "date": "{{ post.date | date: '%-d.%-m.%Y' }}"
      }{% unless forloop.last %},{% endunless %}
    {% endfor %}
    {% for page in site.pages %}
      {% if page.title and page.exclude_from_search != true %}
        ,
        "{{ page.url | slugify }}": {
          "title": "{{ page.title | xml_escape }}",
          "content": {{ page.content | strip_html | strip_newlines | jsonify }},
          "url": "{{ site.baseurl }}{{ page.url | xml_escape }}",
          "category": "stránka",
          "date": ""
        }
      {% endif %}
    {% endfor %}
    {% for collection in site.collections %}
      {% unless collection.label == "posts" %}
        {% for item in site[collection.label] %}
          ,
          "{{ item.url | slugify }}": {
            "title": "{{ item.title | xml_escape }}",
            "content": {{ item.content | strip_html | strip_newlines | jsonify }},
            "url": "{{ site.baseurl }}{{ item.url | xml_escape }}",
            "category": "{{ collection.label | xml_escape }}",
            "date": "{{ item.date | date: '%-d.%-m.%Y' }}"
          }
        {% endfor %}
      {% endunless %}
    {% endfor %}
  };
</script>
<script src="{{ "/assets/js/search/lunr.min.js" | relative_url }}"></script>
<script src="{{ "/assets/js/search/lunr.stemmer.support.js" | relative_url }}"></script>
<script src="{{ "/assets/js/search/lunr.cs.js" | relative_url }}"></script>
<script src="{{ "/assets/js/search/search.js" | relative_url }}"></script>