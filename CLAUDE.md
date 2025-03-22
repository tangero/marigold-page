# CLAUDE.md - Agent Guide for Marigold.cz

## Build Commands
- `bundle install` - Install dependencies
- `bundle exec jekyll serve` - Run local development server
- `bundle exec jekyll build` - Build site for production
- `python generate_summaries.py` - Generate summaries for posts (requires DEEPSEEK_API_KEY)

## Project Structure
- `_posts/` - Blog posts (format: YYYY-MM-DD-title.md)
- `_ai/`, `_mobilnisite/`, `_obrazy/` - Collection content
- `_pages/` - Static pages
- `assets/`, `images/` - Media files

## Style Guidelines
- **Markdown**: Use GitHub Flavored Markdown
- **Frontmatter**: Include title, summary_points, categories as needed
- **Image paths**: Use absolute paths from root (e.g., `/images/example.jpg`)
- **Code blocks**: Use triple backticks with language specified
- **Czech language**: Primary content language is Czech
- **Error handling**: Use try/except blocks with specific error messages in Python code

## Content Formatting
- Keep paragraphs concise and focused
- Use proper hierarchical heading structure (h2, h3, etc.)
- Maintain consistent voice throughout content