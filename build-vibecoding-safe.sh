#!/bin/bash
# Safe build script for Cloudflare Pages with UTF-8 encoding

# Set UTF-8 locale for Czech content
export LANG=cs_CZ.UTF-8
export LC_ALL=C.UTF-8
export LC_CTYPE=cs_CZ.UTF-8

echo "Building Vibecoding site with UTF-8 encoding..."

# Install dependencies
bundle install

# Build Jekyll with vibecoding config
bundle exec jekyll build --config _config_vibecoding.yml --trace

# Copy index file
if [ -f "_site" ]; then
    cp vibecoding-index.html _site/index.html
    echo "Build completed successfully!"
else
    echo "Build failed - _site directory not created"
    exit 1
fi