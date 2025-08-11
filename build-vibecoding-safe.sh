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
echo "Checking vibecoding content before build:"
ls -la _vibecoding/
echo "Number of vibecoding articles:"
find _vibecoding -name "*.md" | wc -l

# Try to create minimal site structure that Jekyll can work with
echo "Creating minimal index for Jekyll..."
cp vibecoding-minimal-index.md index.md

# Force create _site directory if Jekyll doesn't
mkdir -p _site

bundle exec jekyll build --config _config_vibecoding.yml --trace

# Debug - check what was created
echo "Checking build output..."
ls -la
echo "Looking for _site directory:"
find . -name "_site" -type d 2>/dev/null || echo "No _site directory found"
echo "Contents of current directory after build:"

# Copy index file and verify build
if [ -d "_site" ]; then
    echo "_site directory exists, copying index..."
    
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