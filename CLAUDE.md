# CLAUDE.md - Agent Guide for Marigold.cz

## Commands
- Development: `jekyll serve --livereload` (spouští Jekyll server s automatickým obnovením)
- Build: `jekyll build` (produkce) nebo `jekyll build --drafts` (vývoj)
- Test: `pytest` nebo `python -m unittest discover`
- Test single file: `pytest tests/path/to/test.py` nebo `python -m unittest tests.path.to.test`
- Code style: `black .` (formátování Python kódu) a `pylint` (statická analýza kódu)

## Python Code Conventions
- **Python**: Dodržujte PEP 8, používejte Black formátování, správné typové anotace (`str`, `int`, `List[str]`, atd.)
- **Moduly**: Používejte typované funkce, dokumentujte pomocí docstringů s návratovými typy
- **Třídy**: Používejte dataclasses pro datové struktury, @property pro gettery
- **API**: Preferujte FastAPI pro REST API, Pydantic pro validaci dat
- **Asynchronní kód**: Využívejte async/await vzory pro I/O operace, nikoli threading
- **Importy**: Organizujte importy s isort, standardní knihovny první, třetí strany druhé, vlastní moduly třetí

## Jekyll Patterns
- Používejte Liquid šablonování konzistentně, vždy s mezerami: `{{ variable }}` nikoliv `{{variable}}`
- Preferujte kolekce před jednotlivými stránkami pro související obsah
- Používejte front matter důsledně pro metadata stránek
- Struktura _layouts, _includes a _data adresářů by měla být logicky organizovaná
- CSS implementujte přes Sass (.scss soubory) v _sass adresáři
- Využívejte Jekyll pluginy pouze pokud jsou podporovány GitHub Pages

## YAML Conventions
- Používejte 2 mezery pro odsazení, nikoli tabulátory
- Složité datové struktury umisťujte do samostatných souborů v _data adresáři
- Používejte pomlčku a mezeru `- item` pro položky seznamu, ne samotnou pomlčku
- Dlouhé řetězce zapisujte pomocí blokového stylu `|` pro zachování nových řádků
- Používejte explicitní YAML typy kde je to potřeba (např. !!str, !!int)
- Vyhněte se používání speciálních znaků v klíčích, používejte snake_case
- Komentáře začínejte znakem # a mezerou: `# Komentář`

## Python Best Practices
- Preferujte generátory a iterátory před vytváření velkých seznamů v paměti
- Používejte kontextové manažery (`with` statement) pro správu zdrojů
- Implementujte logování místo print() pro debugování
- Používejte virtuální prostředí (venv nebo poetry) pro správu závislostí
- Testujte kód pomocí pytest s alespoň 80% pokrytím
- Zpracovávejte výjimky specificky, ne `except Exception:`
- Pro webové aplikace implementujte správné CORS a bezpečnostní hlavičky

## Build Commands
- `bundle install` - Install dependencies
- `bundle exec jekyll serve` - Run local development server
- `bundle exec jekyll build` - Build site for production
- `python generate_summaries.py` - Generate summaries for posts (requires DEEPSEEK_API_KEY)

## LLM Cost Monitoring
Pro sledování nákladů za OpenRouter API volání:

- **Cost Tracker**: `scripts/llm_cost_tracker.py` - automaticky loguje všechna API volání
  - Ukládá data do SQLite databáze: `_data/llm_costs.db`
  - Sleduje tokeny, ceny, časy odpovědí a chyby
  - Integrováno do `scripts/generate_tech_news_newsapi.py`

- **Reporting**: `python3 scripts/generate_llm_cost_report.py`
  - `--summary-only` - Jen konzolový výpis statistik
  - `--output FILE` - Název výstupního Markdown souboru
  - `--db PATH` - Vlastní cesta k databázi
  - Generuje přehledy: denní, týdenní, měsíční
  - Výstup: `_data/llm_costs_report.md`

Příklady použití:
```bash
# Zobrazit summary v konzoli
python3 scripts/generate_llm_cost_report.py --summary-only

# Vygenerovat plný Markdown report
python3 scripts/generate_llm_cost_report.py

# Vlastní výstupní soubor
python3 scripts/generate_llm_cost_report.py --output costs_$(date +%Y%m).md
```

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