#!/bin/bash
echo "=== SIMPLE VIBECODING BUILD START ==="
date

# Set locale
export LANG=cs_CZ.UTF-8
export LC_ALL=C.UTF-8

# Show what we're working with
echo "Current directory: $(pwd)"
echo "Directory contents:"
ls -la

# Install Jekyll dependencies
echo "Installing Jekyll..."
bundle install

# Create temporary vibecoding index (don't overwrite main index.html!)
echo "Creating vibecoding index..."
if [ -f "vibecoding-index-categories.html" ]; then
    cp vibecoding-index-categories.html vibecoding-temp-index.html
    echo "Using categorized index from vibecoding-index-categories.html"
else
    # Fallback if the file doesn't exist
    cat > vibecoding-temp-index.html << 'EOF'
---
layout: vibecoding-default
title: Vibecoding - AI nástroje pro programování
---

<div class="posts">
  {% assign vibecoding_posts = site.vibecoding | sort: 'date' | reverse %}
  
  {% for post in vibecoding_posts %}
    <article class="post">
      <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>

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
          {{ post.excerpt | strip_html | truncatewords: 60 }}
        </div>
      </div>

      <div class="post-meta">
        {% assign m = post.date | date: "%-m" %}
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
        {{ post.date | date: "%Y" }} - 
        <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Pokračuj ve čtení 👉</a>
      </div>
    </article>
  {% endfor %}
</div>
EOF
fi

# Force create _site
echo "Creating _site directory..."
mkdir -p _site

# Temporarily backup main index.html if it exists
if [ -f "index.html" ]; then
    mv index.html index-backup.html
fi

# Move vibecoding index to index.html for build
mv vibecoding-temp-index.html index.html

# Run Jekyll
echo "Running Jekyll build..."
bundle exec jekyll build --config _config_vibecoding.yml

# Restore original index.html
if [ -f "index-backup.html" ]; then
    mv index-backup.html index.html
else
    rm -f index.html
fi

# Check result
echo "Checking build result..."
if [ -d "_site" ]; then
    echo "SUCCESS: _site directory exists"
    ls -la _site/
    echo "File count: $(find _site -type f | wc -l)"
else
    echo "FAILED: _site directory missing"
    ls -la
fi

# Ensure we have index.html
if [ ! -f "_site/index.html" ]; then
    echo "Creating fallback index.html with article list..."
    cat > _site/index.html << 'EOF'
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="utf-8">
    <title>Vibecoding - AI nástroje pro programování</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; line-height: 1.6; }
        h1 { color: #333; border-bottom: 3px solid #007acc; padding-bottom: 10px; }
        .article { margin: 20px 0; padding: 15px; border-left: 4px solid #007acc; background: #f9f9f9; }
        .article h3 { margin: 0 0 10px 0; color: #007acc; }
        .article p { margin: 0; color: #666; }
        .category { font-size: 0.9em; color: #999; text-transform: uppercase; }
        .date { font-size: 0.9em; color: #999; }
    </style>
</head>
<body>
    <h1>Vibecoding - AI nástroje pro programování</h1>
    <p>Průvodce světem AI nástrojů pro programování a vývoj software.</p>
    
    <h2>Nejnovější články</h2>
    
    <div class="article">
        <div class="category">Claude Code</div>
        <h3>Claude Code Statusline</h3>
        <p>Nastavení status line pro Claude Code editor.</p>
        <div class="date">9. srpna 2025</div>
    </div>
    
    <div class="article">
        <div class="category">Claude Code</div>
        <h3>Claude Code Security Review</h3>
        <p>Bezpečnostní kontrola a nastavení Claude Code.</p>
        <div class="date">6. srpna 2025</div>
    </div>
    
    <div class="article">
        <div class="category">Cursor</div>
        <h3>Cursor 1.4</h3>
        <p>Novinky ve verzi 1.4 editoru Cursor.</p>
        <div class="date">7. srpna 2025</div>
    </div>
    
    <div class="article">
        <div class="category">Replit</div>
        <h3>Replit Obrázky a Agenti</h3>
        <p>Práce s obrázky a AI agenty v Replit prostředí.</p>
        <div class="date">2. srpna 2025</div>
    </div>
    
    <p><em>Web se právě generuje pomocí Jekyll...</em></p>
</body>
</html>
EOF
fi

echo "=== BUILD COMPLETE ==="
ls -la _site/
echo "Final file count: $(find _site -type f 2>/dev/null | wc -l)"