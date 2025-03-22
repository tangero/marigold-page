#!/usr/bin/env python3
import os
import re
import html
from pathlib import Path

def process_md_files(directory):
    """
    Process all .md files in the given directory and its subdirectories
    to replace HTML entities in title with Unicode characters and add
    quotes around the title.
    """
    # Find all .md files
    md_files = list(Path(directory).glob('**/*.md'))
    print(f"Found {len(md_files)} .md files")
    
    modified_count = 0
    for file_path in md_files:
        if process_file(file_path):
            modified_count += 1
    
    print(f"Modified {modified_count} files")

def process_file(file_path):
    """Process a single markdown file. Returns True if file was modified."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False
    
    # Check if file has YAML front matter
    if not content.startswith('---'):
        return False
    
    # Find the title in front matter (with different formatting possibilities)
    title_match = re.search(r'title:\s*(.*?)(\n|$)', content)
    if not title_match:
        return False
    
    title = title_match.group(1).strip()
    original_title = title
    
    # Check if title already has quotes
    has_quotes = (title.startswith('"') and title.endswith('"')) or (title.startswith("'") and title.endswith("'"))
    
    # If title has quotes, extract the content inside quotes
    if has_quotes:
        if title.startswith('"'):
            title = title[1:-1]
        else:
            title = title[1:-1]
    
    # Decode HTML entities
    new_title = html.unescape(title)
    
    # Skip if no changes needed
    if new_title == title and has_quotes:
        return False
    
    # Add double quotes
    new_title_formatted = f'"{new_title}"'
    
    # Replace the title in the content
    new_content = content.replace(f'title: {original_title}', f'title: {new_title_formatted}')
    
    # Check if content actually changed
    if new_content == content:
        return False
    
    # Write the updated content back to the file
    try:
        print(f"Updating {file_path}")
        print(f"  Old title: {original_title}")
        print(f"  New title: {new_title_formatted}")
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        return True
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")
        return False

if __name__ == "__main__":
    # Použití absolutní cesty k adresáři _posts
    posts_dir = "/Users/imac/Documents/GitHub/zastupitelstvo/_posts"
    process_md_files(posts_dir)
    print("Processing complete!")