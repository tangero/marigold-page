#!/bin/bash
# Build skript pro Cloudflare Pages - vibecoding.cz

set -e  # Exit on error

echo "=== Starting Vibecoding build ==="

# Instalace Ruby a Jekyll
echo "Installing Ruby..."
curl -fsSL https://github.com/rbenv/rbenv-installer/raw/HEAD/bin/rbenv-installer | bash || true
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"

# Použij Ruby 3.0
rbenv install -s 3.0.6
rbenv global 3.0.6

# Instalace bundler
gem install bundler

# Instalace Jekyll závislostí
echo "Installing Jekyll dependencies..."
bundle install

# Build Jekyll site s vibecoding konfigurací
echo "Building Vibecoding site with Jekyll..."
bundle exec jekyll build --config _config_vibecoding.yml

# Zkopíruj index stránku
echo "Setting up index page..."
cp vibecoding-index.html _site/index.html

echo "=== Build completed successfully ==="