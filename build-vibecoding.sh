#!/bin/bash
# Build skript pro vibecoding.cz na Cloudflare Pages

echo "Building Vibecoding site..."

# Build Jekyll s vibecoding konfigurací
bundle exec jekyll build --config _config_vibecoding.yml

# Zkopíruj vibecoding-index.html jako hlavní index
cp vibecoding-index.html _site/index.html

echo "Build completed!"