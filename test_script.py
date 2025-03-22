#!/usr/bin/env python3
import os
import re
import html
from pathlib import Path

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
    title_match = re.search(r'title:\s*(.*?)(\n\n|\n|$)', front_matter, re.DOTALL)
    if not title_match:
        return False
    
    title_line = title_match.group(0)
    title_value = title_match.group(1).strip()
    
    print(f"Original title line: '{title_line}'")
    print(f"Original title value: '{title_value}'")
    
    # Remove any existing quotes
    if (title_value.startswith('"') and title_value.endswith('"')) or (title_value.startswith("'") and title_value.endswith("'")):
        if title_value.startswith('"'):
            title_value = title_value[1:-1]
        else:
            # Handle multi-line quoted strings
            if title_value.endswith("'"):
                title_value = title_value[1:-1]
            else:
                # Handle special case of multi-line strings with quotes
                title_value = title_value[1:]
    
    # Handle multi-line titles
    title_value = title_value.replace('\n', ' ').strip()
    
    # Decode HTML entities
    new_title_value = html.unescape(title_value)
    
    print(f"Processed title value: '{new_title_value}'")
    
    # Create a proper YAML string with double quotes and escaping
    new_title_line = f'title: "{new_title_value.replace('"', '\\"')}"'
    
    print(f"New title line: '{new_title_line}'")
    
    # Replace the title line in front matter
    new_front_matter = front_matter.replace(title_line, new_title_line)
    
    # Reconstruct the content
    new_content = f"---{new_front_matter}---{body}"
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    return True

if __name__ == "__main__":
    # Test just one file
    test_file = "/Users/imac/Documents/GitHub/zastupitelstvo/test_title.md"
    process_file(test_file)
    print("Processing complete!")