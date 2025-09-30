#!/bin/bash
# Build script pro Cloudflare Pages

echo "Starting build process..."

# Pokus o instalaci bundle pokud není dostupný
if ! command -v bundle &> /dev/null; then
    echo "Bundle not found, installing..."
    gem install bundler
fi

# Instalace závislostí
echo "Installing dependencies..."
bundle install

# Build Jekyll site pro vibecoding
echo "Building Jekyll site with vibecoding config..."
bundle exec jekyll build --config _config_vibecoding.yml

# Zkopírování vibecoding-feed jako hlavní feed
# (vibecoding-index.md se generuje přímo jako index.html díky permalink: /)
if [ -f "_site/vibecoding-feed.xml" ]; then
    echo "Copying vibecoding feed..."
    cp _site/vibecoding-feed.xml _site/feed.xml
fi

echo "Build completed!"