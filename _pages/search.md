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
  // Inicializace prázdného store objektu
  window.store = {};
  
  // Funkce pro bezpečné přidání položky do store objektu
  function addToStore(key, data) {
    try {
      window.store[key] = {
        title: data.title || "",
        content: data.content || "",
        url: data.url || "",
        category: data.category || "",
        tags: data.tags || "",
        date: data.date || ""
      };
    } catch(e) {
      console.error("Error adding item to store:", key, e);
    }
  }
  
  // Postupné přidávání položek z postů
  {% for post in site.posts %}
    addToStore(
      "{{ post.url | slugify }}",
      {
        title: "{{ post.title | replace: '"', '\"' | strip_newlines | escape }}",
        content: "{{ post.content | strip_html | truncatewords: 50 | replace: '"', '\"' | strip_newlines | escape }}",
        url: "{{ site.baseurl }}{{ post.url }}",
        category: "{{ post.categories | join: ', ' | replace: '"', '\"' | escape }}",
        tags: "{{ post.tags | join: ', ' | replace: '"', '\"' | escape }}",
        date: "{{ post.date | date: '%-d.%-m.%Y' }}"
      }
    );
  {% endfor %}
  
  // Přidání stránek
  {% for page in site.pages %}
    {% if page.title and page.exclude_from_search != true %}
      addToStore(
        "{{ page.url | slugify }}",
        {
          title: "{{ page.title | replace: '"', '\"' | strip_newlines | escape }}",
          content: "{{ page.content | strip_html | truncatewords: 50 | replace: '"', '\"' | strip_newlines | escape }}",
          url: "{{ site.baseurl }}{{ page.url }}",
          category: "stránka",
          date: ""
        }
      );
    {% endif %}
  {% endfor %}
  
  // Přidání kolekcí
  {% for collection in site.collections %}
    {% unless collection.label == "posts" %}
      {% for item in site[collection.label] %}
        addToStore(
          "{{ item.url | slugify }}",
          {
            title: "{{ item.title | replace: '"', '\"' | strip_newlines | escape }}",
            content: "{{ item.content | strip_html | truncatewords: 50 | replace: '"', '\"' | strip_newlines | escape }}",
            url: "{{ site.baseurl }}{{ item.url }}",
            category: "{{ collection.label | escape }}",
            date: "{{ item.date | date: '%-d.%-m.%Y' }}"
          }
        );
      {% endfor %}
    {% endunless %}
  {% endfor %}
</script>
<script src="{{ "/assets/js/search/simple-search.js" | relative_url }}"></script>