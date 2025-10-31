# Open Graph Image - Implementace

## 📋 Přehled

Robustní řešení pro automatický výběr Open Graph obrázků na Marigold.cz s podporou běžných článků i tech-news.

## 🎯 Funkce

### Hierarchie výběru obrázků

1. **post.thumbnail** - Priorita při iteraci přes kolekci postů
2. **page.thumbnail** - Explicitně nastavený thumbnail v článku
3. **page.urlToImage** - Externí obrázky z tech-news (NewsAPI)
4. **page.image** - Explicitně nastavený image
5. **První obrázek z content** - Automatická extrakce z markdown/HTML
6. **site.avatar** - Fallback pro stránky bez obrázků

### Optimalizace přes Cloudinary

Všechny externí obrázky procházejí přes Cloudinary CDN s automatickou optimalizací:
- Open Graph: 1200×630px, auto kvalita, auto formát
- Twitter Card: 1024×512px, auto kvalita, auto formát

## 📁 Soubory

### `_includes/og-image.html`

Hlavní include pro výběr a generování OG tagů.

**Vstupní proměnné:**
- `post.thumbnail` (string, URL)
- `page.thumbnail` (string, URL)
- `page.urlToImage` (string, URL) - tech-news
- `page.image` (string, cesta nebo URL)
- `content` (HTML/markdown obsah)
- `site.avatar` (string, cesta)
- `site.url` (string, base URL)

**Výstupní meta tagy:**
```html
<!-- og-image source: [zdroj] -->
<meta property="og:image" content="[URL]"/>
<meta property="twitter:image" content="[URL]"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta name="twitter:card" content="summary_large_image"/>
```

### `_includes/meta.html`

Aktualizováno pro použití nového include:
```liquid
{% include og-image.html %}
```

## 🔧 Použití

### Běžný článek s thumbnail

```yaml
---
title: "Název článku"
thumbnail: https://example.com/image.jpg
---
```

**Výsledek:** Cloudinary optimalizace → `og:image`

### Tech-news článek

```yaml
---
title: "Tech news"
urlToImage: https://newssite.com/photo.jpg
layout: tech_news_article
---
```

**Výsledek:** Cloudinary optimalizace → `og:image`

### Článek bez thumbnail

```markdown
---
title: "Článek"
---

![Popis](https://example.com/photo.jpg)

Obsah článku...
```

**Výsledek:** První obrázek extrahován z markdown → Cloudinary → `og:image`

### Lokální obrázek

```yaml
---
title: "Článek"
image: /assets/images/local.jpg
---
```

**Výsledek:** `{{ site.url }}/assets/images/local.jpg` → `og:image`

## 🧪 Testování

```bash
# Spustit test skript
chmod +x test_og_tags.sh
./test_og_tags.sh
```

Test ověřuje:
1. Článek s thumbnail (page.thumbnail)
2. Tech-news článek (page.urlToImage)
3. Hlavní stránka (fallback na site.avatar)

### Manuální kontrola

```bash
# Build webu
bundle exec jekyll build

# Zkontrolovat konkrétní článek
grep "og:image" _site/2025/10/21/openai-prohlizec-atlas.html

# Zkontrolovat tech-news
grep "og:image" _site/tech-news/*/index.html | head -5
```

## 🐛 Debug

Include obsahuje HTML komentář se zdrojem obrázku:
```html
<!-- og-image source: page.thumbnail -->
```

Možné hodnoty:
- `post.thumbnail`
- `page.thumbnail`
- `page.urlToImage (tech-news)`
- `page.image`
- `extracted from content`
- `site.avatar (fallback)`

## 📊 Podpora formátů

### Markdown obrázky
```markdown
![Alt text](/assets/image.jpg)
![Alt text](https://external.com/image.jpg)
```

### HTML obrázky
```html
<img src="/assets/image.jpg" alt="Alt text">
<img src="https://external.com/image.jpg" alt="Alt text">
```

## 🔗 Odkazy

- [Open Graph Protocol](https://ogp.me/)
- [Twitter Cards](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards)
- [Cloudinary Image Transformations](https://cloudinary.com/documentation/image_transformations)

## 📅 Historie změn

### 2025-10-25
- ✅ Vytvořen separátní `_includes/og-image.html`
- ✅ Přidána podpora `page.urlToImage` pro tech-news
- ✅ Automatická extrakce prvního obrázku z content
- ✅ Cloudinary optimalizace pro všechny externí obrázky
- ✅ Debug komentáře pro snadné zjištění zdroje
