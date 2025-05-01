import os
import yaml
import frontmatter
from pathlib import Path
import requests
import json
from time import sleep
from datetime import datetime
import re
import sys
import html
from dotenv import load_dotenv

# Načtení proměnných z .env souboru
env_path = "/Users/imac/Documents/GitHub/zastupitelstvo/.env"
load_dotenv(env_path)

class MarkdownValidator:
    """Třída pro validaci Markdown souborů s YAML front matter."""
    
    def __init__(self, fix_issues=False):
        self.fix_issues = fix_issues
        self.validation_stats = {
            'total': 0,
            'valid': 0,
            'fixed': 0,
            'invalid': 0,
            'errors': {}
        }
    
    def validate_yaml_file(self, file_path):
        """Validuje YAML front matter v Markdown souboru."""
        self.validation_stats['total'] += 1
        issues = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.validation_stats['invalid'] += 1
            error_type = "file_read_error"
            if error_type not in self.validation_stats['errors']:
                self.validation_stats['errors'][error_type] = 0
            self.validation_stats['errors'][error_type] += 1
            return False, [f"Chyba při čtení souboru: {e}"], None
        
        # Kontrola YAML front matter
        if not content.startswith('---'):
            self.validation_stats['invalid'] += 1
            error_type = "no_front_matter"
            if error_type not in self.validation_stats['errors']:
                self.validation_stats['errors'][error_type] = 0
            self.validation_stats['errors'][error_type] += 1
            return False, ["Chybí YAML front matter"], None
        
        # Extrakce front matter
        match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not match:
            self.validation_stats['invalid'] += 1
            error_type = "invalid_front_matter_format"
            if error_type not in self.validation_stats['errors']:
                self.validation_stats['errors'][error_type] = 0
            self.validation_stats['errors'][error_type] += 1
            return False, ["Neplatný formát YAML front matter"], None
        
        # Parsování YAML
        try:
            yaml_content = match.group(1)
            yaml_data = yaml.safe_load(yaml_content)
            
            if yaml_data is None:
                self.validation_stats['invalid'] += 1
                error_type = "empty_front_matter"
                if error_type not in self.validation_stats['errors']:
                    self.validation_stats['errors'][error_type] = 0
                self.validation_stats['errors'][error_type] += 1
                return False, ["Prázdný YAML front matter"], None
            
            # Kontrola požadovaných polí
            if 'title' not in yaml_data:
                issues.append("Chybí povinné pole: 'title'")
            
            # Pokud máme title, kontrolujeme jeho formát
            if 'title' in yaml_data:
                title = yaml_data['title']
                
                # Kontrola HTML entit v title
                if any(entity in str(title) for entity in ['&nbsp;', '&#', '&quot;', '&amp;']):
                    issues.append(f"Title obsahuje HTML entity: {title}")
                
                # Kontrola uvozovek kolem title
                if isinstance(title, str) and ((title.startswith('"') and title.endswith('"')) or 
                                             (title.startswith("'") and title.endswith("'"))):
                    issues.append(f"Title má uvozovky kolem: {title}")
                
                # Kontrola na dvojtečky v title
                if isinstance(title, str) and ':' in title:
                    issues.append(f"Title obsahuje dvojtečku, což může způsobit problémy v YAML: {title}")
        except yaml.YAMLError as e:
            self.validation_stats['invalid'] += 1
            error_type = "yaml_syntax_error"
            if error_type not in self.validation_stats['errors']:
                self.validation_stats['errors'][error_type] = 0
            self.validation_stats['errors'][error_type] += 1
            return False, [f"Chyba syntaxe YAML: {e}"], None
        
        # Pokud nejsou žádné problémy, soubor je platný
        if not issues:
            self.validation_stats['valid'] += 1
            return True, [], yaml_data
        
        # Jinak máme neplatný soubor
        self.validation_stats['invalid'] += 1
        for issue in issues:
            error_type = issue.split(":")[0].strip().lower().replace(" ", "_")
            if error_type not in self.validation_stats['errors']:
                self.validation_stats['errors'][error_type] = 0
            self.validation_stats['errors'][error_type] += 1
        
        return False, issues, yaml_data
    
    def fix_yaml_issues(self, file_path, yaml_data):
        """Opravuje problémy v YAML front matter."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extrakce front matter a obsahu
            parts = content.split('---', 2)
            if len(parts) < 3:
                return False, "Neplatný formát pro opravu"
            
            front_matter = parts[1]
            body = parts[2]
            
            # Najít title v front matter pomocí přesnějšího regex vzoru
            # Hledáme řádek začínající "title:" následovaný hodnotou
            title_match = re.search(r'^title:.*?$', front_matter, re.MULTILINE)
            if not title_match:
                return False, "Nelze najít title v YAML front matter"
            
            title_line = title_match.group(0)
            # Extrahujeme hodnotu po "title:"
            title_value = re.sub(r'^title:\s*', '', title_line).strip()
            
            # Odstranit existující uvozovky
            if (title_value.startswith('"') and title_value.endswith('"')) or (title_value.startswith("'") and title_value.endswith("'")):
                if title_value.startswith('"'):
                    title_value = title_value[1:-1]
                else:
                    title_value = title_value[1:-1]
            
            # Opravit víceřádkové nadpisy
            title_value = re.sub(r'\s+', ' ', title_value.strip())
            
            # Dekódovat HTML entity
            title_value = html.unescape(title_value)
            
            # Odstranit zbývající uvozovky nebo apostrofy
            title_value = title_value.replace('"', '').replace("'", '')
            
            # Nahradit dvojtečky pomlčkami s mezerami
            title_value = title_value.replace(':', ' - ')
            
            # Vytvořit nový title
            new_title_line = f'title: {title_value}'
            
            # Nahradit title v front matter - použijeme pouze přesný řádek s title
            new_front_matter = front_matter.replace(title_line, new_title_line)
            
            # Rekonstruovat obsah
            new_content = f"---{new_front_matter}---{body}"
            
            # Zapsat zpět do souboru
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            self.validation_stats['fixed'] += 1
            return True, "Soubor opraven"
        except Exception as e:
            return False, f"Chyba při opravě souboru: {e}"
    
    def validate_all_md_files(self, directory):
        """Validuje všechny Markdown soubory v daném adresáři a jeho podadresářích."""
        md_files = list(Path(directory).glob('**/*.md'))
        print(f"Nalezeno {len(md_files)} .md souborů")
        
        invalid_files = []
        
        for file_path in md_files:
            is_valid, issues, yaml_data = self.validate_yaml_file(file_path)
            if not is_valid:
                if self.fix_issues:
                    fixed, message = self.fix_yaml_issues(file_path, yaml_data)
                    if fixed:
                        print(f"🔧 {file_path}: Opraveno")
                    else:
                        invalid_files.append((file_path, issues))
                        print(f"❌ {file_path}: {', '.join(issues)} - {message}")
                else:
                    invalid_files.append((file_path, issues))
                    print(f"❌ {file_path}: {', '.join(issues)}")
            else:
                print(f"✅ {file_path}")
        
        if invalid_files:
            print(f"\n❌ Nalezeno {len(invalid_files)} neplatných souborů:")
            for file_path, issues in invalid_files:
                print(f"  - {file_path}: {', '.join(issues)}")
        else:
            print("\n✅ Všechny soubory jsou platné!")
        
        print("\nStatistika validace:")
        print(f"Celkem souborů: {self.validation_stats['total']}")
        print(f"Platných souborů: {self.validation_stats['valid']}")
        if self.fix_issues:
            print(f"Opravených souborů: {self.validation_stats['fixed']}")
        print(f"Neplatných souborů: {self.validation_stats['invalid'] - self.validation_stats['fixed'] if self.fix_issues else self.validation_stats['invalid']}")
        
        print("\nTypy chyb:")
        for error_type, count in self.validation_stats['errors'].items():
            print(f"  - {error_type}: {count}")
        
        return len(invalid_files) == 0


class LocalSummaryGenerator:
    def __init__(self, api_key, model_choice, posts_dir="_posts"):
        # Ověříme, že API klíč byl správně načten
        if not api_key or len(api_key) < 10:
            print(f"⚠️ VAROVÁNÍ: API klíč se nezdá být validní: '{api_key}'")
            print("Zkouším načíst API klíč přímo z env proměnných...")
            api_key = os.getenv("OPENROUTER_API_KEY")
            print(f"API klíč načtený z env: {api_key[:10]}... (délka: {len(api_key) if api_key else 0})")
        
        self.api_key = api_key
        self.model_choice = model_choice
        self.posts_dir = Path(posts_dir)
        
        # DeepSeek má vlastní API endpoint a klíč
        if model_choice == "deepseek":
            self.api_key = os.getenv("DEEPSEEK_API_KEY") or api_key
            self.api_url = "https://api.deepseek.com/v1/chat/completions"
            print(f"Používám DeepSeek API klíč: {self.api_key[:10]}... (délka: {len(self.api_key) if self.api_key else 0})")
        else:  # Pro OpenRouter (Gemini model)
            self.api_url = "https://openrouter.ai/api/v1/chat/completions"
            print(f"Používám OpenRouter API klíč: {self.api_key[:10]}... (délka: {len(self.api_key) if self.api_key else 0})")
            
        self.newsletter_processed = False  # newsletter zpracujeme pouze jednou

    def truncate_content(self, content, max_chars=10000):
        """Zkrátí obsah článku na maximální délku při zachování celých vět."""
        if len(content) <= max_chars:
            return content
        more_split = content.split('<!-- more -->')
        if len(more_split) > 1:
            content = more_split[0]
            if len(content) <= max_chars:
                return content
        truncated = content[:max_chars]
        last_period = truncated.rfind('.')
        if last_period > 0:
            return truncated[:last_period + 1]
        return truncated

    def get_post_date(self, filename):
        """Extrahuje datum z názvu souboru Jekyll článku (YYYY-MM-DD-title.md)"""
        date_pattern = r'(\d{4}-\d{2}-\d{2})'
        match = re.match(date_pattern, filename)
        if match:
            return datetime.strptime(match.group(1), '%Y-%m-%d')
        return None

    def generate_summary(self, content, max_retries=5):
        """Generuje shrnutí pomocí API s automatickým retry."""
        # Nastavení API hlaviček podle typu modelu
        if self.model_choice == "deepseek":
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        else:  # OpenRouter
            # Upravené hlavičky s různými formáty autorizace
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://www.marigold.cz/",
                "X-Title": "Marigold.cz"
            }
        
        print(f"Model: {self.model_choice}")
        print(f"API URL: {self.api_url}")
        print(f"Použitý API klíč (prvních 10 znaků): {self.api_key[:10]}...")
        print(f"Kompletní hlavičky: {headers}")
        
        prompt = """Vytvoř 3-4 krátké body shrnující hlavní myšlenky následujícího českého textu.
Každý bod by měl:
- Být stručný (max 15 slov)
- Obsahovat konkrétní informaci
- Být v čistém textu BEZ formátování, číslování nebo pomlček
- Začínat přímo klíčovou informací

Text k shrnutí:

{content}"""
        if self.model_choice == "deepseek":
            payload = {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt.format(content=content)
                    }
                ],
                "model": "deepseek-chat",  # DeepSeek API používá jiný formát modelů
                "max_tokens": 500,
                "temperature": 0.3
            }
        else:  # gemini přes OpenRouter
            payload = {
                "messages": [
                    {
                        "role": "user",
                        "content": prompt.format(content=content)
                    }
                ],
                "model": "google/gemini-2.0-flash-001",
                "max_tokens": 500,
                "temperature": 0.3
            }
        
        # Výpis ekvivalentního CURL příkazu pro debugging
        curl_command = f"curl -X POST {self.api_url} \\\n"
        for header, value in headers.items():
            curl_command += f"  -H '{header}: {value}' \\\n"
        curl_command += f"  -d '{json.dumps(payload)}'"
        print(f"Ekvivalentní CURL příkaz (pro debug):\n{curl_command}")
        
        base_wait_time = 10
        
        for attempt in range(max_retries):
            try:
                if attempt > 0:
                    wait_time = base_wait_time * (1.5 ** attempt)
                    print(f"\nPokus {attempt + 1}/{max_retries}, čekám {int(wait_time)} sekund...")
                    print("Stiskněte Ctrl+C pro přeskočení článku...")
                    try:
                        sleep(wait_time)
                    except KeyboardInterrupt:
                        print("\nPřeskakuji tento článek...")
                        return None

                model_info = "Deepseek (zdarma)" if self.model_choice == "deepseek" else "Gemini"
                print(f"Používám model: {model_info}")
                
                # Přímé nastavení API klíče přes Bearer token
                headers["Authorization"] = f"Bearer {self.api_key.strip()}"
                
                response = requests.post(
                    self.api_url,
                    headers=headers,
                    json=payload,
                    timeout=60
                )
                
                print(f"Status kód odpovědi: {response.status_code}")
                
                try:
                    response_json = response.json()
                except Exception as e:
                    print("Chyba při čtení odpovědi API:", str(e))
                    continue

                # Výpis celé odpovědi pro ladění
                print("API odpověď:", response_json)
                
                if response.status_code == 200 and "choices" in response_json:
                    choices = response_json["choices"]
                    if choices and "message" in choices[0]:
                        message = choices[0]["message"]["content"].strip()
                        # Očekáváme, že body budou oddělené novým řádkem
                        summary_points = [line.strip() for line in message.split("\n") if line.strip()]
                        if summary_points:
                            return summary_points
                print("Nebyly získány žádné body shrnutí.")
            except Exception as e:
                print(f"Chyba při komunikaci s API: {str(e)}")
                import traceback
                print(traceback.format_exc())
        return None

    def process_post(self, post_path, stats):
        """Zpracuje jeden článek a aktualizuje statistiku."""
        try:
            with open(post_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            stats['total'] += 1
            if post.metadata.get("summary_points"):
                print(f"\n✓ Článek již má shrnutí: {post_path.name}")
                stats['already_summarized'] += 1
                return stats

            print(f"\n⚙️ Generuji shrnutí pro: {post_path.name}")
            text = post.content.strip()
            if not text and post.metadata.get("excerpt"):
                text = post.metadata.get("excerpt").strip()
                print(f"\n⚠️ Používám excerpt, protože content je prázdný: {post_path.name}")
            if not text:
                print(f"\n❌ Článek {post_path.name} nemá textový obsah, přeskočuji.")
                stats['failed'] += 1
                return stats

            print(f"Ukázka textu (prvních 100 znaků): {text[:100]}")
            summary_points = self.generate_summary(text)
            if summary_points:
                print("\nVygenerované shrnutí:")
                for point in summary_points:
                    print(f"  • {point}")
                post.metadata["summary_points"] = summary_points
                with open(post_path, 'w', encoding='utf-8') as f:
                    f.write(frontmatter.dumps(post))
                print("✓ Shrnutí uloženo.")
                stats['newly_summarized'] += 1
                print("\nČekám 2 sekundy před dalším článkem...")
                sleep(2)
            else:
                print("❌ Nepodařilo se vygenerovat shrnutí pro: " + post_path.name)
                stats['failed'] += 1
        except Exception as e:
            print(f"❌ Chyba při zpracování {post_path.name}: {str(e)}")
            stats['failed'] += 1
        return stats

    def process_year(self, year):
        """
        Zpracuje články z adresáře _posts pro daný rok a také články z podadresáře newsletter (v _posts/newsletter)
        – u newsletter článků se datum neověřuje.
        """
        stats = { 'total': 0, 'already_summarized': 0, 'newly_summarized': 0, 'failed': 0 }
        
        # Zpracování článků z _posts/<rok>
        year_dir = self.posts_dir / str(year)
        if year_dir.exists():
            posts = list(year_dir.glob("*.md"))
            print(f"\nNalezeno {len(posts)} článků pro rok {year} v adresáři {year_dir}")
            for post_path in posts:
                stats = self.process_post(post_path, stats)
        else:
            print(f"\nAdresář pro rok {year} neexistuje v {self.posts_dir}")
        
        # Zpracování článků z podadresáře newsletter (v _posts/newsletter) – datum se nekontroluje.
        newsletter_path = self.posts_dir / "newsletter"
        if newsletter_path.exists() and not self.newsletter_processed:
            posts = list(newsletter_path.glob("*.md"))
            print(f"\nNalezeno {len(posts)} článků v adresáři {newsletter_path} (bez kontroly data)")
            for post_path in posts:
                stats = self.process_post(post_path, stats)
            self.newsletter_processed = True
        elif not newsletter_path.exists():
            print(f"\nAdresář {newsletter_path} neexistuje.")
        
        print(f"\n{'='*50}")
        print(f"Statistika pro rok {year} (včetně newsletteru):")
        print(f"Celkem článků: {stats['total']}")
        print(f"Již mělo shrnutí: {stats['already_summarized']}")
        print(f"Nově přidáno shrnutí: {stats['newly_summarized']}")
        print(f"Selhalo: {stats['failed']}")
        return stats


class KeywordManager:
    def __init__(self, posts_dir="_posts", data_dir="_data"):
        self.posts_dir = Path(posts_dir)
        self.data_file = Path(data_dir) / "pojmy.json"
        print(f"Inicializace s data_file: {self.data_file}")
        self.known_keywords = self.load_or_create_keywords_file()
        self.setup_patterns()

    def setup_patterns(self):
        """Nastaví regulární výrazy pro detekci klíčových slov."""
        # Vytvoříme pattern pro každé klíčové slovo
        self.patterns = {}
        for keyword in self.known_keywords:
            if isinstance(keyword, str):
                self.patterns[keyword] = re.compile(rf"\b{re.escape(keyword)}\b")

    def load_or_create_keywords_file(self):
        print(f"Načítám soubor s klíčovými slovy: {self.data_file}")
        if self.data_file.exists():
            print("Soubor existuje, načítám...")
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Načteme klíčová slova z pole keywords
                keywords = []
                if "keywords" in data:
                    for item in data["keywords"]:
                        if "keyword" in item:
                            keywords.append(item["keyword"])
                            # Přidáme i variace, pokud existují
                            if "variations" in item:
                                keywords.extend(item["variations"])
                print(f"Načteno {len(keywords)} klíčových slov")
                return keywords
        else:
            print("Soubor neexistuje, vytvářím nový...")
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            return []

    def save_keywords(self):
        print(f"Ukládám klíčová slova do {self.data_file}")
        print(f"Počet klíčových slov k uložení: {len(self.known_keywords)}")
        
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(self.known_keywords, f, ensure_ascii=False, indent=2)
        
        print("Soubor byl úspěšně uložen")
        
        if self.data_file.exists():
            print(f"Soubor existuje a má velikost {self.data_file.stat().st_size} bajtů")
        else:
            print("CHYBA: Soubor nebyl vytvořen!")

    def get_posts_files(self):
        """Vrátí seznam všech markdown souborů v adresáři _posts a jeho podadresářích."""
        print(f"\nKontroluji adresář: {self.posts_dir.absolute()}")
        
        if not self.posts_dir.exists():
            print(f"Chyba: Adresář '{self.posts_dir.absolute()}' neexistuje!")
            return []
            
        # Vypíšeme obsah adresáře pro debug
        print("\nObsah adresáře _posts:")
        for item in self.posts_dir.iterdir():
            print(f"  - {item.name} ({'složka' if item.is_dir() else 'soubor'})")
            
        # Hledáme všechny .md soubory rekurzivně
        print("\nHledám .md soubory v podadresářích...")
        files = []
        for path in self.posts_dir.rglob("*.md"):
            if path.is_file():
                files.append(path)
                print(f"  Nalezen: {path.relative_to(self.posts_dir)}")
        
        if not files:
            print(f"\nVarování: V adresáři '{self.posts_dir.absolute()}' a jeho podadresářích nebyly nalezeny žádné .md soubory!")
            return []
            
        print(f"\nCelkem nalezeno {len(files)} .md souborů")
        return files

    def validate_files(self, files):
        if not self.posts_dir.exists():
            print(f"Chyba: Adresář '{self.posts_dir}' neexistuje!")
            return False

        if not files:
            print(f"Chyba: V adresáři '{self.posts_dir}' a jeho podadresářích nebyly nalezeny žádné markdown soubory!")
            return False

        return True

    def analyze_posts(self):
        """Projde články a najde výskyty klíčových slov z pojmy.json."""
        files = self.get_posts_files()
        if not self.validate_files(files):
            return

        print(f"Nalezeno {len(files)} souborů ke zpracování...")
        total_found = 0
        
        for file in files:
            relative_path = str(file.relative_to(self.posts_dir))
            print(f"\nAnalyzuji: {relative_path}")
            
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Rozdělíme obsah na YAML Front Matter a tělo článku
                parts = content.split('---', 2)
                if len(parts) < 3:
                    print(f"Chyba: Neplatný formát souboru {relative_path} - chybí YAML Front Matter")
                    continue
                
                front_matter = parts[1]
                body = parts[2]
                
                # Načteme data z pojmy.json pro kontrolu cest
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    keywords_data = json.load(f)
                
                for keyword_item in keywords_data.get("keywords", []):
                    keyword = keyword_item.get("keyword")
                    if not keyword:
                        continue
                        
                    # Získáme cestu odkazu
                    link = keyword_item.get("link", "")
                    if not link:
                        continue
                        
                    # Kontrola, zda článek není ve stejné cestě jako cíl odkazu
                    if link.startswith("/"):
                        # Odstraníme počáteční a koncové lomítko
                        link_path = link.strip("/")
                        # Získáme cestu článku bez přípony .md
                        article_path = str(file.relative_to(self.posts_dir)).replace(".md", "")
                        # Kontrola, zda cesta článku obsahuje cestu odkazu
                        if link_path in article_path:
                            print(f"Přeskočeno '{keyword}' - článek je ve stejné cestě jako cíl odkazu")
                            continue
                    
                    # Kontrola, zda slovo není již prolinkované v těle článku
                    # 1. Kontrola HTML odkazů
                    if f"<a href=" in body and keyword in body:
                        # Pokud je v HTML odkazu, přeskočíme
                        continue
                        
                    # 2. Kontrola Markdown odkazů
                    if f"[{keyword}](" in body or f"[{keyword}][" in body:
                        # Pokud je v Markdown odkazu, přeskočíme
                        continue
                    
                    # 3. Kontrola, zda slovo není součástí jiného odkazu
                    # Hledáme pattern [text](url) nebo [text][ref]
                    if re.search(rf"\[[^\]]*{re.escape(keyword)}[^\]]*\]\([^)]*\)", body) or \
                       re.search(rf"\[[^\]]*{re.escape(keyword)}[^\]]*\]\[[^\]]*\]", body):
                        continue
                    
                    # Hledáme celé slovo v těle článku
                    pattern = rf"\b{re.escape(keyword)}\b"
                    
                    # Najdeme první výskyt slova
                    match = re.search(pattern, body)
                    if match:
                        print(f"\nNalezeno '{keyword}' v {relative_path}")
                        print("Přidat odkaz? (a/n): ", end='')
                        if input().lower() == 'a':
                            # Nahradíme pouze první výskyt slova Markdown odkazem v těle článku
                            new_body = body[:match.start()] + f"[{keyword}]({link})" + body[match.end():]
                            # Složíme obsah zpět dohromady
                            new_content = f"---{front_matter}---{new_body}"
                            with open(file, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            print(f"✓ Odkaz přidán")
                            total_found += 1
                            
            except Exception as e:
                print(f"Chyba při zpracování souboru {relative_path}: {str(e)}")
        
        print(f"\nHotovo! Nalezeno a zpracováno {total_found} výskytů klíčových slov.")

    def add_links_to_posts(self):
        """Přidá odkazy na klíčová slova do markdown souborů."""
        if not self.known_keywords:
            print("Žádná klíčová slova nejsou definována v pojmy.json")
            return

        print("\nPřidávám odkazy do článků...")
        files = self.get_posts_files()
        if not files:
            return

        total_modified = 0
        for file_path in files:
            print(f"\nZpracovávám soubor: {file_path}")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                modified = False
                
                for keyword in self.known_keywords:
                    if not isinstance(keyword, str):
                        continue
                        
                    # Kontrola, zda slovo není již prolinkované
                    # 1. HTML odkaz
                    html_pattern = f"(?<!<[^>]*)({re.escape(keyword)})(?![^<]*>)"
                    # 2. Markdown inline odkaz
                    md_inline_pattern = f"(?<!\\[)({re.escape(keyword)})(?!\\]\\([^)]*\\))"
                    # 3. Markdown reference odkaz
                    md_ref_pattern = f"(?<!\\[)({re.escape(keyword)})(?!\\]\\[[^\\]]*\\]|\\])"
                    
                    # Kombinovaný pattern pro kontrolu všech typů odkazů
                    combined_pattern = f"(?<!<[^>]*|\\[)({re.escape(keyword)})(?![^<]*>|\\]\\([^)]*\\)|\\]\\[[^\\]]*\\]|\\])"
                    
                    if re.search(combined_pattern, content):
                        print(f"\nNalezeno '{keyword}' v {file_path}")
                        print("Přidat odkaz? (a/n): ", end='')
                        if input().lower() == 'a':
                            # Nahradíme slovo HTML odkazem
                            content = re.sub(
                                combined_pattern,
                                f"<a href='/{keyword.lower().replace(' ', '-')}/' class='keyword-link'>{keyword}</a>",
                                content
                            )
                            modified = True
                
                if modified:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"✓ Soubor {file_path} byl upraven")
                    total_modified += 1
                else:
                    print("Žádné změny nebyly provedeny")
                    
            except Exception as e:
                print(f"Chyba při zpracování souboru {file_path}: {str(e)}")
        
        print(f"\nHotovo! Upraveno {total_modified} souborů.")

    def show_keywords(self):
        if not self.known_keywords:
            print("Žádná klíčová spojení nejsou definována")
            return

        sorted_keywords = sorted(
            self.known_keywords.items(),
            key=lambda x: (x[1].get('category', 'Nezařazeno'), -x[1].get('count', 0))
        )
        
        current_category = None
        print("\nExistující klíčová spojení:")
        for id, data in sorted_keywords:
            category = data.get('category', 'Nezařazeno')
            if current_category != category:
                current_category = category
                print(f"\n=== {current_category} ===")
            
            print(f"\nID: {id}")
            print(f"Název: {data.get('name', 'Není definován')}")
            print(f"Popis: {data.get('description', 'Není definován')}")
            print(f"URL: {data.get('url', 'Není definována')}")
            print(f"Počet výskytů: {data.get('count', 0)}")
            print(f"Vytvořeno: {data.get('created', 'Není definováno')}")
            print(f"Naposledy nalezeno: {data.get('last_found', 'Není definováno')}")

    def edit_keyword(self):
        self.show_keywords()
        
        print("\nZadejte ID klíčového spojení pro úpravu: ")
        id = input().strip()
        
        if id not in self.known_keywords:
            print("Klíčové spojení nebylo nalezeno")
            return
        
        keyword = self.known_keywords[id]
        print(f"\nÚprava: {keyword['name']}")
        print("1. Upravit název")
        print("2. Upravit popis")
        print("3. Upravit URL")
        print("4. Smazat")
        
        print("Vyberte akci (1-4): ")
        choice = input().strip()
        
        if choice == '1':
            print("Nový název: ")
            keyword['name'] = input().strip()
        elif choice == '2':
            print("Nový popis: ")
            keyword['description'] = input().strip()
        elif choice == '3':
            print("Nové URL: ")
            keyword['url'] = input().strip()
        elif choice == '4':
            del self.known_keywords[id]
        
        self.save_keywords()
        print("Změny byly uloženy")

    def show_main_menu(self):
        print("\n=== Správce klíčových spojení ===")
        print("1. Analyzovat články a najít nová klíčová spojení")
        print("2. Spravovat existující klíčová spojení")
        print("3. Konec")
        print("\nVyberte akci (1-3): ")

    def show_editor_menu(self):
        while True:
            print("\n=== Editor klíčových spojení ===")
            print("1. Zobrazit existující klíčová spojení")
            print("2. Přidat odkazy do článků")
            print("3. Upravit existující klíčové spojení")
            print("4. Zpět do hlavního menu")
            
            print("\nVyberte akci (1-4): ")
            choice = input().strip()
            
            if choice == '1':
                self.show_keywords()
            elif choice == '2':
                self.add_links_to_posts()
            elif choice == '3':
                self.edit_keyword()
            elif choice == '4':
                break
            else:
                print("Neplatná volba")

    def run(self):
        while True:
            self.show_main_menu()
            choice = input().strip()

            if choice == '1':
                print("Spouštím automatickou analýzu článků...")
                self.analyze_posts()
            elif choice == '2':
                self.show_editor_menu()
            elif choice == '3':
                print("Ukončuji program...")
                break
            else:
                print(f"Neplatná volba: '{choice}'")

def main():
    print("\nVítejte v nástroji pro práci s Markdown články!")
    
    # Výběr režimu
    print("Vyberte režim:")
    print("1. Generování shrnutí článků")
    print("2. Validace Markdown souborů")
    print("3. Oprava problémů s YAML hlavičkami")
    print("4. Správa klíčových spojení")
    
    while True:
        mode = input("Zadejte režim (1-4): ").strip()
        if mode in ["1", "2", "3", "4"]:
            break
        print("Neplatná volba. Zadejte číslo 1-4.")
    
    # Režim generování shrnutí
    if mode == "1":
        # Načtení API klíče
        api_key = os.getenv("OPENROUTER_API_KEY")
        print(f"Načítání .env souboru z: {env_path}")
        print(f"Existuje soubor .env: {os.path.exists(env_path)}")
        print(f"Dostupné proměnné prostředí: {list(os.environ.keys())}")
        
        if not api_key:
            print("⚠️ API klíč OPENROUTER_API_KEY nebyl nalezen v proměnných prostředí!")
            api_key = input("Zadejte váš OpenRouter API klíč: ").strip()
        else:
            print(f"Nalezen API klíč OPENROUTER_API_KEY: {api_key[:10]}... (délka: {len(api_key)})")
        
        # Výběr modelu
        while True:
            model_choice = input("Vyberte model (1 = DeepSeek, 2 = Gemini): ").strip()
            if model_choice in ["1", "2"]:
                break
            print("Neplatná volba. Zadejte 1 nebo 2.")
        
        model_choice = "deepseek" if model_choice == "1" else "gemini"
        generator = LocalSummaryGenerator(api_key, model_choice)
        
        try:
            year = int(input("Zadejte rok, od kterého chcete začít (2002-2025): "))
        except ValueError:
            print("Neplatný vstup pro rok.")
            return
        if not 2002 <= year <= 2025:
            print("Rok musí být mezi 2002 a 2025")
            return
        
        while year >= 2002:
            print(f"\n{'='*50}")
            print(f"Zpracovávám rok {year}")
            print(f"{'='*50}")
            generator.process_year(year)
            year -= 1
        print("\nGenerování shrnutí dokončeno.")
    
    # Režim validace nebo opravy Markdown souborů
    elif mode in ["2", "3"]:
        fix_issues = (mode == "3")
        
        # Určení adresáře pro validaci
        while True:
            dir_choice = input("Vyberte adresář (1 = _posts, 2 = vlastní cesta): ").strip()
            if dir_choice in ["1", "2"]:
                break
            print("Neplatná volba. Zadejte 1 nebo 2.")
        
        if dir_choice == "1":
            directory = Path("_posts")
        else:
            directory = Path(input("Zadejte absolutní cestu k adresáři: ").strip())
        
        if not directory.exists():
            print(f"Adresář {directory} neexistuje.")
            return
        
        validator = MarkdownValidator(fix_issues=fix_issues)
        
        action_text = "Opravuji" if fix_issues else "Validuji"
        print(f"\n{action_text} Markdown soubory v adresáři {directory}...")
        
        success = validator.validate_all_md_files(directory)
        
        if success:
            print(f"\n✅ {action_text} dokončena úspěšně.")
        else:
            print(f"\n❌ {action_text} dokončena s chybami.")
            if not fix_issues:
                print("\nPro automatickou opravu chyb spusťte program znovu v režimu opravy (3).")
    
    # Režim správy klíčových spojení
    elif mode == "4":
        try:
            print("Spouštím správce klíčových spojení...")
            manager = KeywordManager()
            manager.run()
        except Exception as e:
            print(f"CHYBA v hlavním programu: {str(e)}")
            import traceback
            print(traceback.format_exc())

if __name__ == "__main__":
    main()