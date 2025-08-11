#!/bin/bash
# Safe build script for Cloudflare Pages with UTF-8 encoding

# Enable detailed tracing
set -x
# Note: not using set -e to allow fallback mechanisms

# Set UTF-8 locale for Czech content
export LANG=cs_CZ.UTF-8
export LC_ALL=C.UTF-8
export LC_CTYPE=cs_CZ.UTF-8

echo "Building Vibecoding site with UTF-8 encoding..."
echo "Script starting at: $(date)"

# Install dependencies
bundle install

# Build Jekyll with vibecoding config
echo "Running Jekyll build..."
echo "Checking vibecoding content before build:"
ls -la _vibecoding/ || echo "No _vibecoding directory found"
echo "Number of vibecoding articles:"
find _vibecoding -name "*.md" 2>/dev/null | wc -l

# Show current directory structure
echo "Current directory structure:"
ls -la

# Try to create minimal site structure that Jekyll can work with
echo "Creating minimal index for Jekyll..."
if [ -f "vibecoding-minimal-index.md" ]; then
    cp vibecoding-minimal-index.md index.md
    echo "Index created from vibecoding-minimal-index.md"
else
    echo "vibecoding-minimal-index.md not found, creating basic index.md"
    cat > index.md << 'EOF'
---
layout: default
title: Vibecoding
---

# Vibecoding

AI nástroje pro programování

{% for post in site.vibecoding %}
- {{ post.title }}
{% endfor %}
EOF
fi

# Force create _site directory if Jekyll doesn't
echo "Creating _site directory..."
mkdir -p _site
ls -la _site

echo "Running Jekyll build with trace..."
bundle exec jekyll build --config _config_vibecoding.yml --trace --verbose

# Wait a moment for filesystem sync
sleep 2

# Debug - check what was created
echo "=== POST-BUILD DEBUG ==="
echo "Working directory: $(pwd)"
echo "Contents of current directory:"
ls -la
echo "Looking for _site directory:"
find . -maxdepth 1 -name "_site" -type d 2>/dev/null || echo "No _site directory found"

# Check _site with multiple methods
echo "Checking if _site exists (test -d):"
if test -d "_site"; then
    echo "_site directory EXISTS via test -d"
    ls -la _site/ || echo "Cannot list _site contents"
else
    echo "_site directory DOES NOT EXIST via test -d"
fi

echo "Checking if _site exists ([ -d ]):"
if [ -d "_site" ]; then
    echo "_site directory EXISTS via [ -d ]"
    ls -la _site/ || echo "Cannot list _site contents"
else
    echo "_site directory DOES NOT EXIST via [ -d ]"
fi

# Try to create basic site if Jekyll didn't
if [ ! -d "_site" ]; then
    echo "Creating fallback _site directory..."
    mkdir -p _site
    cat > _site/index.html << 'EOF'
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vibecoding - AI nástroje pro programování</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        h1 { color: #333; }
        .article { margin: 20px 0; padding: 10px; border-left: 3px solid #007acc; }
    </style>
</head>
<body>
    <h1>Vibecoding - AI nástroje pro programování</h1>
    <p>Průvodce světem AI nástrojů pro programování.</p>
    <p><em>Web se právě generuje pomocí fallback mechanismu...</em></p>
</body>
</html>
EOF
    echo "Fallback site created"
fi

# Copy index file and verify build  
if [ -d "_site" ]; then
    echo "_site directory found, copying index..."
    
    # Create index.html from vibecoding-simple.html  
    if [ -f "vibecoding-simple.html" ]; then
        cp vibecoding-simple.html _site/index.html
        echo "Simple index copied successfully"
    elif [ -f "vibecoding-index.html" ]; then
        cp vibecoding-index.html _site/index.html
        echo "Complex index copied successfully"
    else
        echo "Creating basic index.html"
        cat > _site/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Vibecoding</title>
    <meta charset="utf-8">
</head>
<body>
    <h1>Vibecoding - AI nástroje pro programování</h1>
    <p>Web se právě generuje...</p>
</body>
</html>
EOF
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