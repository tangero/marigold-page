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
echo "Running Jekyll build..."
bundle exec jekyll build --config _config_vibecoding.yml --trace

# Debug - check what was created
echo "Checking build output..."
ls -la
echo "Contents of current directory after build:"

# Copy index file and verify build
if [ -d "_site" ]; then
    echo "_site directory exists, copying index..."
    
    # Create index.html from vibecoding-index.html  
    if [ -f "vibecoding-index.html" ]; then
        cp vibecoding-index.html _site/index.html
        echo "Index copied successfully"
    else
        echo "Warning: vibecoding-index.html not found"
    fi
    
    # List what was built
    echo "Listing _site contents:"
    ls -la _site/
    
    # Check if we have any content
    if [ -n "$(ls -A _site 2>/dev/null)" ]; then
        echo "Build completed successfully!"
    else
        echo "Warning: _site directory is empty"
        exit 1
    fi
else
    echo "Build failed - _site directory not created"
    echo "Current directory contents:"
    ls -la
    exit 1
fi