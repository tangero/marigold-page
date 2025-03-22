#!/usr/bin/env python3
import os
import re
import html
from pathlib import Path

def process_md_files(directory):
    """
    Process all .md files in the given directory and its subdirectories
    to clean title values in YAML front matter:
    - Remove HTML entities and replace with Unicode characters
    - Remove quotes and apostrophes
    - Replace colons with spaced hyphens
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
    
    # Split content to get front matter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    front_matter = parts[1]
    body = parts[2]
    
    # Find the title line in front matter
    title_match = re.search(r'title:\s*(.*?)(\n[a-zA-Z]|\n$|\n\n|$)', front_matter, re.DOTALL)
    if not title_match:
        return False
    
    title_line = title_match.group(0)
    title_value = title_match.group(1).strip()
    
    # Remove any existing quotes
    if (title_value.startswith('"') and title_value.endswith('"')) or (title_value.startswith("'") and title_value.endswith("'")):
        title_value = title_value[1:-1]
    elif title_value.startswith("'") or title_value.startswith('"'):
        # Handle unclosed quotes
        title_value = title_value[1:]
    
    # Handle multi-line titles
    title_value = re.sub(r'\s+', ' ', title_value.strip())
    
    # Decode HTML entities
    title_value = html.unescape(title_value)
    
    # Remove any remaining quotes or apostrophes
    title_value = title_value.replace('"', '').replace("'", '')
    
    # Replace colons with spaced hyphens
    title_value = title_value.replace(':', ' - ')
    
    # Create new title line
    new_title_line = f'title: {title_value}'
    
    # Replace the title line in front matter
    new_front_matter = front_matter.replace(title_line, new_title_line + '\n')
    
    # Reconstruct the content
    new_content = f"---{new_front_matter}---{body}"
    
    # Check if content actually changed
    if new_content == content:
        return False
    
    # Write the updated content back to the file
    try:
        print(f"Updating {file_path}")
        print(f"  Old title: {title_line.strip()}")
        print(f"  New title: {new_title_line}")
        
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