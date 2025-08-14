#!/bin/bash
# Build skript pro vibecoding.cz na Cloudflare Pages

echo "Starting Vibecoding build..."

# Instalace závislostí
echo "Installing dependencies..."
bundle install

# Build Jekyll s vibecoding konfigurací
echo "Building Jekyll site..."
bundle exec jekyll build --config _config_vibecoding.yml

echo "Build completed successfully!"