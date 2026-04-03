# Migrace Marigold.cz z Jekyll na Hugo

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrovat Marigold.cz z Jekyll (build ~500s) na Hugo (build ~5-10s) bez zmeny URL, domeny a hostingu (GitHub Pages + Actions).

**Architecture:** Hugo pouziva Go templates misto Liquid, content organizuje do sections misto collections. Staticke soubory, markdown obsah a front matter zustavaji kompatibilni. Migrace probiha na samostatnem branchi `hugo-migration` -- kdykoli se lze vratit na `main` s puvodnim Jekyll setupem.

**Tech Stack:** Hugo (extended), Go templates, SCSS via Hugo Pipes, GitHub Actions, GitHub Pages

**Rollback strategie:** Puvodni Jekyll setup zustava nedotceny na `main` branchi. Hugo migrace probiha na `hugo-migration` branchi. Merge do `main` az po overeni, ze vsechny URL funguji a web vypada spravne. V pripade problemu staci prepnout zpet na `main`.

---

## Prehled struktury

### Jekyll (soucasny stav)
```
_posts/           -> 2977 markdown souboru
_tech_news/       -> 194 souboru
_ai/              -> 21 souboru
_mobilnisite/     -> 25 souboru
_obrazy/          -> 62 souboru
_layouts/         -> 9 layoutu (Liquid templates)
_includes/        -> 15 includes
_sass/            -> 5 SCSS souboru
_pages/           -> 22 stranek
_data/            -> data soubory (YAML, JSON)
assets/           -> staticke soubory (CSS, JS, images)
audio/            -> 44 MP3 souboru
images/           -> favicony, loga
_config.yml       -> konfigurace
```

### Hugo (cilovy stav)
```
content/
  posts/          <- _posts/ (presunuty, upraven front matter)
  tech-news/      <- _tech_news/
  ai/             <- _ai/
  mobilnisite/    <- _mobilnisite/
  obrazy/         <- _obrazy/
layouts/
  _default/       <- baseof.html, single.html, list.html
  posts/          <- single.html (post layout)
  tech-news/      <- single.html, list.html
  partials/       <- _includes/ prevod
themes/           (nepouzivame - custom layouts)
assets/
  scss/           <- _sass/ soubory
  js/             <- JavaScript
static/
  images/         <- images/
  audio/          <- audio/
  assets/         <- ostatni staticke soubory (obrazky v clancich)
data/             <- _data/ soubory
hugo.toml         <- _config.yml prevod
```

---

## Task 0: Priprava -- vytvoreni migracniho branche

**Files:**
- Create: `.github/workflows/hugo-build.yml`

- [ ] **Step 1: Vytvorit migracni branch**

```bash
git checkout main
git pull origin main
git checkout -b hugo-migration
```

- [ ] **Step 2: Overit vychozi stav**

```bash
# Zaznamenat aktualni pocty pro pozdejsi verifikaci
echo "Posts: $(find _posts -name '*.md' | wc -l)"
echo "Tech news: $(find _tech_news -name '*.md' | wc -l)"
echo "AI: $(find _ai -name '*.md' | wc -l)"
echo "Mobilnisite: $(find _mobilnisite -name '*.md' | wc -l)"
echo "Obrazy: $(find _obrazy -name '*.md' | wc -l)"
```

Ocekavany vystup:
```
Posts: 2977
Tech news: 194
AI: 21
Mobilnisite: 25
Obrazy: 62
```

- [ ] **Step 3: Commit**

```bash
git commit --allow-empty -m "chore: start Hugo migration branch"
```

---

## Task 1: Instalace Hugo a zakladni konfigurace

**Files:**
- Create: `hugo.toml`
- Create: `.hugo_build.lock` (do .gitignore)

- [ ] **Step 1: Nainstalovat Hugo**

```bash
# macOS
brew install hugo

# Overit verzi
hugo version
# Ocekavano: hugo v0.14x.x+extended
```

- [ ] **Step 2: Vytvorit hugo.toml**

```toml
baseURL = "https://www.marigold.cz"
languageCode = "cs"
title = "Marigold.cz"
theme = ""

# Zakladni nastaveni
[params]
  author = "Patrick Zandl"
  description = "Technologie a Svet"
  avatar = "/images/patrick-avatar.jpg"
  github_repo = "https://github.com/tangero/marigold-page"

# Footer links
[params.footer]
  email = "patrick.zandl@marigold.cz"
  facebook = "patrick.zandl"
  twitter = "tangero"
  linkedin = "patrickzandl"
  rss = true

# Permalinks -- KRITICKE: musi odpovidat Jekyll URL
[permalinks]
  posts = "/item/:slug/"
  ai = "/ai/:slug/"
  mobilnisite = "/mobilnisite/:slug/"
  obrazy = "/obrazy/:slug/"

[permalinks.tech-news]
  page = "/tech-news/:year-:month-:day/:slug/"

# Vystupy
[outputs]
  home = ["HTML", "RSS"]
  section = ["HTML", "RSS"]

# RSS feed
[outputFormats.RSS]
  mediaType = "application/rss+xml"
  baseName = "feed"

# Markup
[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true
  [markup.highlight]
    style = "darcula"
    lineNos = false

# Sass
[module]
  [module.hugoVersion]
    extended = true

# Pagination
[pagination]
  pagerSize = 15
  path = "page"

# Sitemap
[sitemap]
  changeFreq = ""
  filename = "sitemap.xml"
  priority = -1
```

- [ ] **Step 3: Pridat do .gitignore**

Pridat na konec `.gitignore`:
```
# Hugo
public/
resources/
.hugo_build.lock
```

- [ ] **Step 4: Commit**

```bash
git add hugo.toml .gitignore
git commit -m "feat: add Hugo configuration"
```

---

## Task 2: Migrace obsahu -- posts

**Files:**
- Move: `_posts/**/*.md` -> `content/posts/**/*.md`
- Create: `content/posts/_index.md`

- [ ] **Step 1: Vytvorit content strukturu**

```bash
mkdir -p content/posts
```

- [ ] **Step 2: Zkopirovat posty (zachovat adresarovou strukturu)**

```bash
# Kopirovat vsechny posty krome anglickych
rsync -av --exclude='en/' _posts/ content/posts/

# Anglicke posty do vlastni sekce
mkdir -p content/en/posts
cp -r _posts/en/* content/en/posts/ 2>/dev/null || true
```

- [ ] **Step 3: Vytvorit skript pro upravu front matter**

Vytvorit `scripts/hugo_migrate_frontmatter.py`:

```python
#!/usr/bin/env python3
"""
Upravi front matter v markdown souborech pro kompatibilitu s Hugo.
Hlavni zmeny:
- layout: post -> odstranit (Hugo pouziva adresarovou strukturu)
- Zajistit 'slug' odpovida puvodni Jekyll URL
- Prevest date format
"""
import os
import re
import sys
import yaml
from pathlib import Path

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return False

    # Rozdelit front matter a obsah
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False

    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        print(f"  WARN: Cannot parse YAML in {filepath}")
        return False

    if fm is None:
        fm = {}

    changed = False

    # Odstranit layout (Hugo ho nepotrebuje -- pouziva _default/single.html)
    if 'layout' in fm:
        del fm['layout']
        changed = True

    # Zajistit slug odpovida nazvu souboru (pro zachovani URL)
    filename = Path(filepath).stem
    # Jekyll format: YYYY-MM-DD-title-slug
    match = re.match(r'\d{4}-\d{2}-\d{2}-(.*)', filename)
    if match:
        slug = match.group(1)
        if 'slug' not in fm or fm['slug'] != slug:
            fm['slug'] = slug
            changed = True

    # Odstranit Jekyll-specificke fieldy
    for key in ['ID', 'oldlink', 'post_date', 'post_excerpt']:
        if key in fm:
            del fm[key]
            changed = True

    if changed:
        new_fm = yaml.dump(fm, default_flow_style=False,
                          allow_unicode=True, sort_keys=False)
        new_content = f"---\n{new_fm}---\n{parts[2]}"
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return changed

def main():
    content_dir = sys.argv[1] if len(sys.argv) > 1 else 'content/posts'
    count = 0
    total = 0

    for root, dirs, files in os.walk(content_dir):
        for fname in files:
            if fname.endswith('.md'):
                total += 1
                filepath = os.path.join(root, fname)
                if process_file(filepath):
                    count += 1

    print(f"Zpracovano {total} souboru, upraveno {count}")

if __name__ == '__main__':
    main()
```

- [ ] **Step 4: Spustit migraci front matter**

```bash
python3 scripts/hugo_migrate_frontmatter.py content/posts
```

Ocekavany vystup: `Zpracovano 2977 souboru, upraveno ~2900`

- [ ] **Step 5: Vytvorit _index.md pro posts sekci**

Vytvorit `content/posts/_index.md`:
```markdown
---
title: "Clanky"
---
```

- [ ] **Step 6: Overit pocty**

```bash
find content/posts -name '*.md' -not -name '_index.md' | wc -l
# Ocekavano: 2977
```

- [ ] **Step 7: Commit**

```bash
git add content/posts/ scripts/hugo_migrate_frontmatter.py
git commit -m "feat: migrate posts to Hugo content structure"
```

---

## Task 3: Migrace obsahu -- kolekce (ai, mobilnisite, obrazy, tech_news)

**Files:**
- Move: `_ai/` -> `content/ai/`
- Move: `_mobilnisite/` -> `content/mobilnisite/`
- Move: `_obrazy/` -> `content/obrazy/`
- Move: `_tech_news/` -> `content/tech-news/`
- Create: `content/*/index.md` pro kazdou sekci

- [ ] **Step 1: Zkopirovat kolekce**

```bash
mkdir -p content/ai content/mobilnisite content/obrazy content/tech-news

cp _ai/*.md content/ai/
cp _mobilnisite/*.md content/mobilnisite/
cp _obrazy/*.md content/obrazy/
cp _tech_news/*.md content/tech-news/
```

- [ ] **Step 2: Spustit front matter migraci pro vsechny kolekce**

```bash
python3 scripts/hugo_migrate_frontmatter.py content/ai
python3 scripts/hugo_migrate_frontmatter.py content/mobilnisite
python3 scripts/hugo_migrate_frontmatter.py content/obrazy
python3 scripts/hugo_migrate_frontmatter.py content/tech-news
```

- [ ] **Step 3: Vytvorit _index.md pro kazdou sekci**

`content/ai/_index.md`:
```markdown
---
title: "Umela inteligence"
url: /ai/
---
```

`content/mobilnisite/_index.md`:
```markdown
---
title: "Mobilni site"
url: /mobilnisite/
---
```

`content/obrazy/_index.md`:
```markdown
---
title: "Obrazy"
url: /obrazy/
---
```

`content/tech-news/_index.md`:
```markdown
---
title: "Technologicke zpravy"
url: /tech-news/
---
```

- [ ] **Step 4: Overit pocty**

```bash
echo "AI: $(find content/ai -name '*.md' -not -name '_index.md' | wc -l)"
echo "Mobilnisite: $(find content/mobilnisite -name '*.md' -not -name '_index.md' | wc -l)"
echo "Obrazy: $(find content/obrazy -name '*.md' -not -name '_index.md' | wc -l)"
echo "Tech-news: $(find content/tech-news -name '*.md' -not -name '_index.md' | wc -l)"
```

Ocekavano: AI: 21, Mobilnisite: 25, Obrazy: 62, Tech-news: 194

- [ ] **Step 5: Commit**

```bash
git add content/ai/ content/mobilnisite/ content/obrazy/ content/tech-news/
git commit -m "feat: migrate collections to Hugo sections"
```

---

## Task 4: Migrace statickych souboru a dat

**Files:**
- Move: `images/` -> `static/images/`
- Move: `audio/` -> `static/audio/`
- Move: `assets/` (staticke) -> `static/assets/`
- Move: `_data/` -> `data/`
- Move: `_sass/` -> `assets/scss/`

- [ ] **Step 1: Presunout staticke soubory**

```bash
mkdir -p static

# Images, audio, manifest, service worker
cp -r images/ static/images/
cp -r audio/ static/audio/
cp manifest-marigold.json static/
cp firebase-messaging-sw.js static/ 2>/dev/null || true

# Assets (obrazky v clancich, ebook, JS)
# Pozor: NEKOPIROVAT style.scss (ten pujde do Hugo Pipes)
mkdir -p static/assets
cp -r assets/obrazy/ static/assets/obrazy/ 2>/dev/null || true
cp -r assets/ebook/ static/assets/ebook/ 2>/dev/null || true
cp -r assets/js/ static/assets/js/ 2>/dev/null || true
cp -r assets/tipuesearch/ static/assets/tipuesearch/ 2>/dev/null || true
cp -r assets/aiprace/ static/assets/aiprace/ 2>/dev/null || true

# Vsechny ostatni asset soubory (obrazky primo v assets/)
find assets/ -maxdepth 1 -type f \( -name '*.jpg' -o -name '*.png' -o -name '*.gif' -o -name '*.webp' -o -name '*.pdf' -o -name '*.svg' \) -exec cp {} static/assets/ \;
```

- [ ] **Step 2: Presunout data soubory**

```bash
mkdir -p data
cp _data/*.yml data/ 2>/dev/null || true
cp _data/*.yaml data/ 2>/dev/null || true
cp _data/*.json data/ 2>/dev/null || true
```

- [ ] **Step 3: Pripravit SCSS pro Hugo Pipes**

```bash
mkdir -p assets/scss
cp _sass/_variables.scss assets/scss/
cp _sass/_reset.scss assets/scss/
cp _sass/_darcula.scss assets/scss/
cp _sass/_highlights.scss assets/scss/
cp _sass/_svg-icons.scss assets/scss/

# Hlavni stylesheet -- odstranit Jekyll front matter (---\n---)
tail -n +3 assets/style.scss > assets/scss/main.scss
```

- [ ] **Step 4: Commit**

```bash
git add static/ data/ assets/scss/
git commit -m "feat: migrate static files, data, and SCSS"
```

---

## Task 5: Zakladni layouty -- baseof.html a partials

**Files:**
- Create: `layouts/_default/baseof.html`
- Create: `layouts/partials/meta.html`
- Create: `layouts/partials/footer.html`
- Create: `layouts/partials/analytics.html`
- Create: `layouts/partials/fcm.html`
- Create: `layouts/partials/nav.html`
- Create: `layouts/partials/szn-discussion.html`

Toto je nejvetsi task -- prevod Liquid na Go templates. Kazdy soubor nize obsahuje kompletni kod.

- [ ] **Step 1: Vytvorit baseof.html**

Vytvorit `layouts/_default/baseof.html`:

```html
<!DOCTYPE html>
<html lang="cs">
  <head>
    <title>{{ if .Title }}{{ .Title }} | {{ end }}Marigold.cz - Site a Technologie</title>
    {{ partial "meta.html" . }}

    {{ if or (eq .Layout "post") (eq .Layout "tech_news_article") (eq .Layout "tech_news") }}
      {{ partial "szn-discussion-meta.html" . }}
    {{ end }}

    {{ $style := resources.Get "scss/main.scss" | toCSS (dict "outputStyle" "compressed") }}
    <link rel="stylesheet" href="{{ $style.RelPermalink }}" />

    <link rel="alternate" type="application/rss+xml" title="{{ .Site.Title }} - {{ .Site.Params.description }}" href="/feed.xml" />
    <meta name="theme-color" content="#ffffff">

    <link rel="apple-touch-icon" sizes="180x180" href="/images/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="/images/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/images/favicon-16x16.png">
    <link rel="manifest" href="/manifest-marigold.json">
    <link rel="mask-icon" href="/images/safari-pinned-tab.svg" color="#5bbad5">
    <link rel="shortcut icon" href="/images/favicon.ico">
    <meta name="msapplication-TileColor" content="#2d89ef">
    <meta name="msapplication-config" content="/images/browserconfig.xml">

    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Marigold">

    <link rel="preconnect" href="https://res.cloudinary.com">
    <link rel="dns-prefetch" href="https://d21-a.sdn.cz">
    <link rel="dns-prefetch" href="https://cdn.us.heap-api.com">

    <script type="text/javascript" src="https://d21-a.sdn.cz/d_21/sl/3/loader.js" async></script>
  </head>

  <body>
    <div id="bar"></div>
    <div class="wrapper-container">
      <div class="wrapper-masthead">
        <div class="container">
          {{ partial "nav.html" . }}
        </div>
      </div>

      <div class="wrapper-main">
        <div id="main" role="main" class="container">
          {{ block "main" . }}{{ end }}
        </div>
      </div>

      <div class="wrapper-footer">
        <div class="container">
          {{ partial "footer.html" . }}
        </div>
      </div>
    </div>

    {{ partial "analytics.html" . }}
    {{ partial "fcm.html" . }}

    <script>
      window.heapReadyCb=window.heapReadyCb||[],window.heap=window.heap||[],heap.load=function(e,t){window.heap.envId=e,window.heap.clientConfig=t=t||{},window.heap.clientConfig.shouldFetchServerConfig=!1;var a=document.createElement("script");a.type="text/javascript",a.async=!0,a.src="https://cdn.us.heap-api.com/config/"+e+"/heap_config.js";var r=document.getElementsByTagName("script")[0];r.parentNode.insertBefore(a,r);var n=["init","startTracking","stopTracking","track","resetIdentity","identify","getSessionId","getUserId","getIdentity","addUserProperties","addEventProperties","removeEventProperty","clearEventProperties","addAccountProperties","addAdapter","addTransformer","addTransformerFn","onReady","addPageviewProperties","removePageviewProperty","clearPageviewProperties","trackPageview"],i=function(e){return function(){var t=Array.prototype.slice.call(arguments,0);window.heapReadyCb.push({name:e,fn:function(){heap[e]&&heap[e].apply(heap,t)}})}};for(var p=0;p<n.length;p++)heap[n[p]]=i(n[p])};
      heap.load("2219710997");
    </script>

    {{ partial "nav-dropdown.html" . }}
  </body>
</html>
```

- [ ] **Step 2: Vytvorit nav.html partial**

Vytvorit `layouts/partials/nav.html`:

```html
<header class="masthead">
  <a href="/" class="site-avatar"><img src="{{ .Site.Params.avatar }}" alt="{{ .Site.Title }}" /></a>

  <div class="site-info">
    <h1 class="site-name"><a href="/">{{ .Site.Title }}</a></h1>
    <p class="site-description">{{ .Site.Params.description }}</p>
  </div>

  <nav aria-label="Hlavni navigace">
    <ul>
      <li><a href="/search">&#x1F50D;</a></li>
      <li class="nav-separator" aria-hidden="true">|</li>
      <li><a href="https://www.prolnuto.cz/">&#x1F9D1;&#x200D;&#x1F4BB; Kurzy AI</a></li>
      <li class="nav-separator" aria-hidden="true">|</li>
      <li><a href="https://www.vibecoding.cz/">&#x1F5A5;&#xFE0F; Vibecoding</a></li>
      <li class="nav-separator" aria-hidden="true">|</li>
      <li><a href="/mobilnisite">&#x1F5FC; 4G/5G</a></li>
      <li class="nav-separator" aria-hidden="true">|</li>
      <li><a href="/ai">&#x1F916; AI</a></li>
      <li class="nav-separator" aria-hidden="true">|</li>
      <li>
        <span class="nav-dropdown">
          <button class="nav-dropdown-toggle" aria-expanded="false" aria-label="Dalsi menu">
            Dalsi &#x2630;
          </button>
          <div class="nav-dropdown-menu" role="menu">
            <a href="/tech-news/" role="menuitem">&#x1F4BB; Zpravy</a>
            <a href="/obrazy" role="menuitem">&#x1F5BC;&#xFE0F; Obrazy</a>
          </div>
        </span>
      </li>
    </ul>
  </nav>
</header>
```

- [ ] **Step 3: Prevest dalsi partials z Jekyll includes**

Kazdý include prevest 1:1 z Liquid na Go templates. Klicove zmeny syntaxe:

| Jekyll (Liquid) | Hugo (Go) |
|-----------------|-----------|
| `{{ site.url }}` | `{{ .Site.BaseURL }}` |
| `{{ page.title }}` | `{{ .Title }}` |
| `{{ page.url }}` | `{{ .RelPermalink }}` |
| `{{ page.date \| date: "%Y-%m-%d" }}` | `{{ .Date.Format "2006-01-02" }}` |
| `{{ page.content }}` | `{{ .Content }}` |
| `{% if page.thumbnail %}` | `{{ if .Params.thumbnail }}` |
| `{% for post in site.posts %}` | `{{ range where .Site.RegularPages "Section" "posts" }}` |
| `{% include footer.html %}` | `{{ partial "footer.html" . }}` |
| `{{ post.excerpt \| strip_html \| truncate: 160 }}` | `{{ .Summary \| plainify \| truncate 160 }}` |

Vytvorit vsechny partials: `meta.html`, `footer.html`, `analytics.html`, `fcm.html`, `szn-discussion.html`, `szn-discussion-meta.html`, `og-image.html`, `nav-dropdown.html`, `pagination.html`.

Kazdy partial je primy prevod z odpovídajiciho `_includes/*.html` s vyse uvedenou tabulkou zmen.

- [ ] **Step 4: Commit**

```bash
git add layouts/
git commit -m "feat: add Hugo base layout and partials"
```

---

## Task 6: Layout -- single post (post.html)

**Files:**
- Create: `layouts/posts/single.html`

- [ ] **Step 1: Vytvorit post layout**

Vytvorit `layouts/posts/single.html`:

```html
{{ define "main" }}
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/+esm'
  mermaid.initialize({startOnLoad:true,theme:'neutral'})
  await mermaid.run({querySelector:'code.language-mermaid'})
</script>

<article class="post detailed">
  <h1>{{ .Title }}</h1>

  <!-- Workshop banner (pokud je aktivni) -->
  {{ partial "workshop-banner.html" . }}

  {{ if ne .Section "obrazy" }}
  <div>
    <p class="author_title">{{ .Site.Params.author }} &middot;
      {{ .Date.Format "2." }}
      {{ index (dict
        "January" "leden" "February" "unor" "March" "brezen"
        "April" "duben" "May" "kveten" "June" "cerven"
        "July" "cervenec" "August" "srpen" "September" "zari"
        "October" "rijen" "November" "listopad" "December" "prosinec"
      ) (.Date.Format "January") }}
      {{ .Date.Format "2006" }}
    </p>

    {{ with .Params.last_modified_at }}
    <p class="author_title">(Aktualizovano: {{ . }})</p>
    {{ end }}

    <div class="post-tags">
      {{ range .Params.categories }}
        <a href="/rubrika/#{{ . | urlize }}">{{ . }}</a>&nbsp;
      {{ end }}
    </div>
  </div>

  {{ with .Params.thumbnail }}
    {{ $thumb := replace . "http://" "https://" }}
    <div class="thumbnail-strip">
      <img src="https://res.cloudinary.com/dvwv5cne3/image/fetch/w_1200,h_300,c_fill,g_auto,f_auto,q_auto/{{ $thumb }}" alt="{{ $.Title }}">
    </div>
  {{ end }}
  {{ end }}

  {{ with .Params.summary_points }}
  <div class="quick-summary">
    <div class="quick-summary-header">
      <svg class="summary-icon" viewBox="0 0 24 24" width="24" height="24">
        <path fill="currentColor" d="M14,17H7V15H14M17,13H7V11H17M17,9H7V7H17M19,3H5C3.89,3 3,3.89 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V5C21,3.89 20.1,3 19,3Z" />
      </svg>
      <span>Rychle shrnuti clanku</span>
    </div>
    <ul class="summary-points">
      {{ range . }}
        <li>{{ . }}</li>
      {{ end }}
    </ul>
  </div>
  {{ end }}

  {{ with .Params.audio_url }}
  <div class="audio-container">
    <p class="audio-title">Prehrat clanek:</p>
    <audio class="custom-audio" controls>
      <source src="{{ . }}" type="audio/mpeg">
      <p><a href="{{ . }}" target="_blank">&#x1F3A7; Poslechnout audio verzi clanku</a></p>
    </audio>
  </div>
  {{ end }}

  <div class="entry">
    {{ .Content }}
  </div>

  {{ partial "szn-discussion.html" . }}

  <!-- Featured posts -->
  {{ $featured := where (where .Site.RegularPages "Section" "posts") ".Params.featured" true }}
  {{ $featured = where $featured ".RelPermalink" "ne" .RelPermalink }}
  {{ if gt (len $featured) 0 }}
  <div class="featured-posts">
    <h3>&#x1F4A1; Co je tu dalsiho zajimaveho ke cteni?</h3>
    <table>
      <tbody>
        {{ range first 2 (shuffle $featured) }}
        <tr>
          <td>
            <a href="{{ .RelPermalink }}">&#x1F449;{{ .Title }}</a>
            <p class="excerpt">{{ .Summary | plainify | truncate 160 }}</p>
          </td>
        </tr>
        {{ end }}
      </tbody>
    </table>
  </div>
  {{ end }}

  <div class="posts">
    <h3>Chcete tyto clanky emailem?</h3>
    <iframe src="https://zandl.substack.com/embed" width="480" height="150" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no" title="Odber newsletteru"></iframe>
  </div>

  <div>
    <p><span class="share-box">Sdilejte clanek:</span>
      <a href="https://twitter.com/share?text={{ .Title }}&url={{ .Permalink }}" target="_blank">Twitter</a>,
      <a href="https://www.facebook.com/sharer.php?u={{ .Permalink }}" target="_blank">Facebook</a>,
      {{ with .File }}
      <a href="{{ $.Site.Params.github_repo }}/blob/main/{{ .Path }}" target="_blank">Opravit &#x1F4C3;</a>
      {{ end }}
    </p>
    <div class="PageNavigation">
      {{ with .PrevInSection }}
        <a class="prev" href="{{ .RelPermalink }}">&laquo; {{ .Title }}</a> |
      {{ end }}
      {{ with .NextInSection }}
        <a class="next" href="{{ .RelPermalink }}">{{ .Title }} &raquo;</a>
      {{ end }}
    </div>
  </div>
</article>

<!-- Toast notifikace -->
<div class="toast" id="toast">Zkopirovano do schranky!</div>

<!-- Code copy button script -->
{{ partial "code-copy.html" . }}
{{ end }}
```

- [ ] **Step 2: Commit**

```bash
git add layouts/posts/
git commit -m "feat: add Hugo post layout"
```

---

## Task 7: Layout -- homepage s paginaci

**Files:**
- Create: `layouts/index.html`
- Create: `content/_index.md`

- [ ] **Step 1: Vytvorit homepage layout**

Vytvorit `layouts/index.html`:

```html
{{ define "main" }}

<!-- Kombinovany feed vsech sekci, serazeny podle data -->
{{ $posts := where .Site.RegularPages "Section" "posts" }}
{{ $ai := where .Site.RegularPages "Section" "ai" }}
{{ $mobilni := where .Site.RegularPages "Section" "mobilnisite" }}

{{ $all := union $posts (union $ai $mobilni) }}
{{ $all = where $all ".Params.hide" "ne" true }}
{{ $all = sort $all ".Date" "desc" }}

<!-- Paginace -->
{{ $paginator := .Paginate $all 15 }}

<div class="posts">
  {{ range $paginator.Pages }}
  <div class="post">
    <div class="post-content">
      {{ with .Params.thumbnail }}
      <div class="thumbnail">
        <a href="{{ $.RelPermalink }}">
          <img src="https://res.cloudinary.com/dvwv5cne3/image/fetch/w_300,h_200,c_fill,g_auto,f_auto,q_auto/{{ replace . `http://` `https://` }}"
               alt="{{ $.Title }}" loading="lazy">
        </a>
      </div>
      {{ end }}
      <div class="excerpt">
        <h2><a href="{{ .RelPermalink }}">{{ .Title }}</a></h2>
        <p class="date">{{ .Date.Format "2.1.2006" }}</p>
        {{ .Summary | plainify | truncate 300 }}
      </div>
    </div>
  </div>
  {{ end }}
</div>

{{ partial "pagination.html" . }}

{{ end }}
```

- [ ] **Step 2: Vytvorit content/_index.md**

```markdown
---
title: "Marigold.cz"
---
```

- [ ] **Step 3: Commit**

```bash
git add layouts/index.html content/_index.md
git commit -m "feat: add Hugo homepage with pagination"
```

---

## Task 8: Layout -- tech-news, stranky, search

**Files:**
- Create: `layouts/tech-news/single.html`
- Create: `layouts/tech-news/list.html`
- Create: `layouts/_default/single.html` (genericka stranka)
- Create: `layouts/_default/list.html`
- Move: `_pages/*.md` -> `content/*.md` (staticke stranky)

- [ ] **Step 1: Vytvorit tech-news layouty**

Prevest `_layouts/tech_news.html` a `_layouts/tech_news_article.html` na Go templates. Klicovy rozdil: `site.tech_news` se nahradi za `where .Site.RegularPages "Section" "tech-news"`.

- [ ] **Step 2: Vytvorit defaultni single/list layouty**

`layouts/_default/single.html` -- pro staticke stranky:
```html
{{ define "main" }}
<article class="page">
  <h1>{{ .Title }}</h1>
  <div class="entry">
    {{ .Content }}
  </div>
</article>
{{ end }}
```

- [ ] **Step 3: Migrovat staticke stranky**

```bash
# Presunout stranky z _pages/ do content/
for f in _pages/*.md _pages/*.html; do
  [ -f "$f" ] && cp "$f" content/
done
```

Kazdá stranka si zachova svuj `url:` z front matter.

- [ ] **Step 4: Search stranka**

Prevest `_pages/search.md` -- JavaScript store se naplni pomoci Hugo range misto Liquid for loop:

```javascript
{{ range .Site.RegularPages }}
addToStore("{{ .RelPermalink | urlize }}", {
  title: {{ .Title | jsonify }},
  content: {{ .Summary | plainify | truncate 200 | jsonify }},
  url: "{{ .RelPermalink }}",
  category: {{ delimit .Params.categories ", " | jsonify }},
  tags: {{ delimit .Params.tags ", " | jsonify }},
  date: "{{ .Date.Format "2.1.2006" }}"
});
{{ end }}
```

- [ ] **Step 5: Commit**

```bash
git add layouts/ content/
git commit -m "feat: add tech-news layouts, default layouts, and static pages"
```

---

## Task 9: GitHub Actions workflow pro Hugo

**Files:**
- Create: `.github/workflows/hugo-build.yml`

- [ ] **Step 1: Vytvorit Hugo build workflow**

Vytvorit `.github/workflows/hugo-build.yml`:

```yaml
name: Build and Deploy (Hugo)
on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      HUGO_VERSION: "0.147.0"
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v3
        with:
          hugo-version: ${{ env.HUGO_VERSION }}
          extended: true

      - name: Build site
        run: hugo --minify

      - name: Upload Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./public

  deploy:
    runs-on: ubuntu-latest
    needs: build
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/hugo-build.yml
git commit -m "feat: add Hugo GitHub Actions workflow"
```

---

## Task 10: Lokalni testovani a verifikace URL

**Files:** zadne nove

- [ ] **Step 1: Spustit Hugo lokalne**

```bash
hugo server -D
# Ocekavano: spusti se behem ~5s na http://localhost:1313
```

- [ ] **Step 2: Overit kriticke URL**

Zkontrolovat tyto URL v prohlizeci:

```
http://localhost:1313/                              # Homepage s paginaci
http://localhost:1313/item/deepseek/                # Post
http://localhost:1313/ai/                           # AI sekce
http://localhost:1313/mobilnisite/                   # Mobilni site
http://localhost:1313/obrazy/                        # Obrazy
http://localhost:1313/tech-news/                     # Tech news
http://localhost:1313/tech-news/2026-02-23/slug/    # Tech news clanek
http://localhost:1313/search/                        # Search
http://localhost:1313/feed.xml                       # RSS feed
http://localhost:1313/page/2/                        # Paginace
```

- [ ] **Step 3: Automaticka verifikace URL**

Vytvorit skript `scripts/verify_urls.sh`:

```bash
#!/bin/bash
# Porovna URL z Jekyll _site/ s Hugo public/
# Spustit az po obou buildech

echo "=== Verifikace URL ==="
ERRORS=0

# Najit vsechny HTML soubory v Jekyll _site
find _site -name 'index.html' | sed 's|_site||' | sort > /tmp/jekyll_urls.txt

# Najit vsechny HTML soubory v Hugo public
find public -name 'index.html' | sed 's|public||' | sort > /tmp/hugo_urls.txt

# Porovnat
MISSING=$(comm -23 /tmp/jekyll_urls.txt /tmp/hugo_urls.txt | wc -l)
EXTRA=$(comm -13 /tmp/jekyll_urls.txt /tmp/hugo_urls.txt | wc -l)

echo "Jekyll stranek: $(wc -l < /tmp/jekyll_urls.txt)"
echo "Hugo stranek: $(wc -l < /tmp/hugo_urls.txt)"
echo "Chybejici v Hugo: $MISSING"
echo "Nove v Hugo: $EXTRA"

if [ "$MISSING" -gt 0 ]; then
  echo ""
  echo "=== Chybejici URL (prvnich 20) ==="
  comm -23 /tmp/jekyll_urls.txt /tmp/hugo_urls.txt | head -20
fi
```

```bash
chmod +x scripts/verify_urls.sh

# Nejdrive Jekyll build (na main branchi, uz existuje)
# Pak Hugo build
hugo
./scripts/verify_urls.sh
```

Ocekavany vystup: 0 chybejicich URL (nebo seznam k oprave).

- [ ] **Step 4: Commit verifikacniho skriptu**

```bash
git add scripts/verify_urls.sh
git commit -m "feat: add URL verification script for migration"
```

---

## Task 11: Finalizace a merge

- [ ] **Step 1: Odstranit puvodni Jekyll soubory (az po overeni!)**

```bash
# POUZE po uspesne verifikaci URL
rm -rf _layouts/ _includes/ _sass/
rm -f _config.yml Gemfile Gemfile.lock
rm -f assets/style.scss
```

- [ ] **Step 2: Prejmenovat workflow**

```bash
# Deaktivovat Jekyll build
mv .github/workflows/build.yml .github/workflows/build-jekyll.yml.disabled

# Hugo build jako primarni
# (uz existuje jako hugo-build.yml, pri merge prepsat build.yml)
```

- [ ] **Step 3: Finalny build a mereni casu**

```bash
time hugo --minify
# Ocekavano: < 10s
```

- [ ] **Step 4: Commit a push**

```bash
git add -A
git commit -m "feat: complete Hugo migration, remove Jekyll files"
git push origin hugo-migration
```

- [ ] **Step 5: Vytvorit PR pro review**

```bash
gh pr create \
  --title "Migrace Jekyll -> Hugo" \
  --body "## Migrace z Jekyll na Hugo

- Build cas: ~500s -> ~5-10s
- Vsechny URL zachovany
- Dark mode, a11y opravy zachovany
- Rollback: revert tento PR

## Testovano
- [ ] Vsechny kriticke URL fungují
- [ ] RSS feed funguje
- [ ] Search funguje
- [ ] Dark mode funguje
- [ ] Mobile layout funguje"
```

- [ ] **Step 6: Po merge -- overit produkci**

Po merge PR zkontrolovat:
1. GitHub Actions build probehne uspesne
2. https://www.marigold.cz/ se nacte
3. Nahodny vyber 10 starych URL funguje
4. RSS feed na /feed.xml funguje

---

## Rollback plan

Pokud cokoli selze po merge:

```bash
# Varianta 1: Revert commit
git revert HEAD
git push

# Varianta 2: Obnovit Jekyll branch
git checkout main
git reset --hard <posledni-jekyll-commit>
git push --force

# Varianta 3: Re-enable Jekyll workflow
mv .github/workflows/build-jekyll.yml.disabled .github/workflows/build.yml
git add .github/workflows/build.yml
git commit -m "revert: restore Jekyll build"
git push
```

Puvodni Jekyll soubory zustavaji v git historii a lze je obnovit kdykoli.

---

## Casovy odhad

| Task | Popis | Odhad |
|------|-------|-------|
| 0 | Priprava branche | 5 min |
| 1 | Hugo konfigurace | 15 min |
| 2 | Migrace posts | 20 min |
| 3 | Migrace kolekci | 15 min |
| 4 | Staticke soubory | 15 min |
| 5 | Zakladni layouty + partials | 60 min |
| 6 | Post layout | 30 min |
| 7 | Homepage + paginace | 30 min |
| 8 | Tech-news + stranky + search | 45 min |
| 9 | GitHub Actions | 10 min |
| 10 | Testovani + verifikace | 30 min |
| 11 | Finalizace | 15 min |
| **Celkem** | | **~5 hodin** |
