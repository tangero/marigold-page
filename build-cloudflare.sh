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

echo "Build completed!"