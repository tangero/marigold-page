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
        self.api_key = api_key
        self.model_choice = model_choice
        self.posts_dir = Path(posts_dir)
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
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
        """Generuje shrnutí pomocí OpenRouter API s automatickým retry."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "https://www.marigold.cz/",
            "X-Title": "Marigold.cz",
            "Content-Type": "application/json"
        }
        
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
                "model": "deepseek/deepseek-chat:free",
                "max_tokens": 500,
                "temperature": 0.3
            }
        else:  # gemini
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
                
                response = requests.post(
                    self.api_url,
                    headers=headers,
                    json=payload,
                    timeout=60
                )
                
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


def main():
    print("\nVítejte v nástroji pro práci s Markdown články!")
    
    # Výběr režimu
    print("Vyberte režim:")
    print("1. Generování shrnutí článků")
    print("2. Validace Markdown souborů")
    print("3. Oprava problémů s YAML hlavičkami")
    
    while True:
        mode = input("Zadejte režim (1-3): ").strip()
        if mode in ["1", "2", "3"]:
            break
        print("Neplatná volba. Zadejte číslo 1-3.")
    
    # Režim generování shrnutí
    if mode == "1":
        # Načtení API klíče
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            api_key = "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"
        
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


if __name__ == "__main__":
    main()