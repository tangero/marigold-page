#!/usr/bin/env python3
import os
import sys
from pathlib import Path
from generate_local_summaries import MarkdownValidator
import argparse

def fix_files_in_directory(directory_path, dry_run=True):
    """Validate and optionally fix YAML front matter issues in Markdown files in the specified directory."""
    # Create validator instance
    validator = MarkdownValidator(fix_issues=not dry_run)
    
    # Find all Markdown files
    directory = Path(directory_path)
    md_files = list(directory.glob('**/*.md'))
    print(f"Found {len(md_files)} Markdown files in {directory}")
    
    # Statistics
    stats = {
        'total': 0,
        'valid': 0,
        'invalid': 0,
        'fixed': 0,
    }
    
    invalid_files = []
    
    # Process each file
    for file_path in md_files:
        stats['total'] += 1
        print(f"\nProcessing: {file_path}")
        
        # Validate the file
        is_valid, issues, yaml_data = validator.validate_yaml_file(file_path)
        
        if is_valid:
            stats['valid'] += 1
            print(f"✅ Valid YAML front matter")
        else:
            stats['invalid'] += 1
            print(f"❌ Invalid YAML front matter:")
            for issue in issues:
                print(f"  - {issue}")
            
            if not dry_run:
                # Fix issues
                print("\nAttempting to fix issues...")
                fixed, message = validator.fix_yaml_issues(file_path, yaml_data)
                
                if fixed:
                    stats['fixed'] += 1
                    print(f"🔧 {message}")
                    
                    # Validate again after fixing
                    is_valid, issues, yaml_data = validator.validate_yaml_file(file_path)
                    if is_valid:
                        print("✅ All issues fixed successfully!")
                    else:
                        print("⚠️ Some issues remain after fixing:")
                        for issue in issues:
                            print(f"  - {issue}")
                        invalid_files.append((file_path, issues))
                else:
                    print(f"❌ Failed to fix: {message}")
                    invalid_files.append((file_path, issues))
            else:
                # In dry run mode, just add to the list of invalid files
                invalid_files.append((file_path, issues))
    
    # Print summary
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"Total files processed: {stats['total']}")
    print(f"Valid files: {stats['valid']}")
    print(f"Invalid files: {stats['invalid']}")
    
    if not dry_run:
        print(f"Fixed files: {stats['fixed']}")
        print(f"Remaining invalid files: {len(invalid_files)}")
    
    if invalid_files:
        print("\nInvalid files:")
        for file_path, issues in invalid_files:
            print(f"  - {file_path}: {', '.join(issues)}")
    
    return stats, invalid_files

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Validate and fix YAML front matter in Markdown files')
    parser.add_argument('directory', help='Directory containing Markdown files to process')
    parser.add_argument('--fix', action='store_true', help='Fix issues rather than just validating')
    args = parser.parse_args()
    
    # Run the validator
    fix_files_in_directory(args.directory, dry_run=not args.fix)

if __name__ == '__main__':
    main()