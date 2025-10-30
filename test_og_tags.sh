#!/bin/bash
# Test skript pro kontrolu Open Graph tagů

echo "🔍 Test Open Graph tagů"
echo "======================================"

# Počkat na dokončení buildu
echo "⏳ Čekám na dokončení Jekyll buildu..."
bundle exec jekyll build --quiet

echo ""
echo "======================================"
echo "📰 Test 1: Běžný článek s thumbnail"
echo "======================================"
echo "Soubor: _posts/2025/2025-10-21-openai-prohlizec-atlas.md"
echo "Očekáváno: page.thumbnail → Cloudinary"
echo ""
grep -A 3 "og-image source" _site/2025/10/21/openai-prohlizec-atlas.html | head -5
echo ""
grep "og:image" _site/2025/10/21/openai-prohlizec-atlas.html | head -2

echo ""
echo "======================================"
echo "📱 Test 2: Tech-news článek"
echo "======================================"
echo "Soubor: _tech_news/2025-09-23-A-6-samsung-one-ui-8-settings-hiding-in-plain-sigh.md"
echo "Očekáváno: page.urlToImage → Cloudinary"
echo ""

# Najít vygenerovaný HTML soubor
TECH_NEWS_FILE=$(find _site/tech-news -name "*samsung*" -type f | head -1)
if [ -n "$TECH_NEWS_FILE" ]; then
    echo "Nalezen: $TECH_NEWS_FILE"
    grep -A 3 "og-image source" "$TECH_NEWS_FILE" | head -5
    echo ""
    grep "og:image" "$TECH_NEWS_FILE" | head -2
else
    echo "❌ Tech-news článek nenalezen"
fi

echo ""
echo "======================================"
echo "🏠 Test 3: Hlavní stránka (fallback)"
echo "======================================"
echo "Soubor: index.html"
echo "Očekáváno: site.avatar (fallback)"
echo ""
grep -A 3 "og-image source" _site/index.html | head -5
echo ""
grep "og:image" _site/index.html | head -2

echo ""
echo "======================================"
echo "✅ Test dokončen!"
echo "======================================"
