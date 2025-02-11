import os
import yaml
import frontmatter
from pathlib import Path
import requests
import json
from time import sleep

class PostSummaryGenerator:
    def __init__(self, api_key, posts_dir="_posts"):
        self.api_key = api_key
        self.posts_dir = posts_dir
        
    def get_post_content(self, post_path):
        """Načte obsah článku a jeho front matter."""
        try:
            with open(post_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            return post
        except Exception as e:
            print(f"Chyba při čtení souboru {post_path}: {str(e)}")
            return None
        
    def generate_summary(self, content):
        """Generuje shrnutí pomocí Deepseek API."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        prompt = """Vytvoř 3-4 krátké body shrnující hlavní myšlenky následujícího českého textu.
        Každý bod by měl:
        - Být stručný (max 10 slov)
        - Obsahovat konkrétní informaci
        - Být v čistém textu BEZ formátování (žádné hvězdičky, pomlčky, backticky, odkazy)
        
        Text k shrnutí:
        
        Text k shrnutí:
        
        {content}"""
        
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt.format(content=content)
                }
            ],
            "model": "deepseek-chat",
            "temperature": 0.7,
            "max_tokens": 150
        }
        
        try:
            response = requests.post(
                "https://api.deepseek.com/v1/chat/completions",
                headers=headers,
                json=payload
            )
            
            if response.status_code == 200:
                response_json = response.json()
                if "choices" in response_json and len(response_json["choices"]) > 0:
                    summary = response_json["choices"][0]["message"]["content"]
                    # Rozdělíme na řádky a očistíme
                    bullet_points = []
                    for line in summary.split('\n'):
                        line = line.strip()
                        if line:
                            # Odstranění markdown formátování
                            line = line.replace('*', '').replace('**', '')  # Odstranění hvězdiček
                            line = line.replace('`', '')  # Odstranění code blocks
                            line = line.replace('#', '')  # Odstranění nadpisů
                            line = line.replace('[', '').replace(']', '')  # Odstranění částí odkazů
                            # Odstranění pomlček na začátku
                            line = line.lstrip('- ').strip()
                            if line:  # Přidáme pouze neprázdné řádky
                                bullet_points.append(line)
                    return bullet_points
                else:
                    raise Exception("Neplatná odpověď z API: " + str(response_json))
            else:
                raise Exception(f"API vrátilo status code: {response.status_code}")
                
        except Exception as e:
            print(f"Chyba při generování shrnutí: {str(e)}")
            return None
            
    def get_latest_posts(self):
        """Získá nejnovější články seřazené podle data"""
        posts_path = Path(self.posts_dir)
        posts = []
        
        for post_file in posts_path.glob("*.md"):
            try:
                post_date = self.get_post_date(post_file.name)
                if post_date:
                    posts.append((post_date, post_file))
            except Exception as e:
                print(f"Chyba při zpracování souboru {post_file}: {str(e)}")
                continue
                
        return [post[1] for post in sorted(posts, reverse=True)[:10]]
            
    def get_post_date(self, filename):
        """Extrahuje datum z názvu souboru Jekyll článku (YYYY-MM-DD-title.md)"""
        import re
        from datetime import datetime
        
        date_pattern = r'(\d{4}-\d{2}-\d{2})'
        match = re.match(date_pattern, filename)
        if match:
            return datetime.strptime(match.group(1), '%Y-%m-%d')
        return None
        
    def process_posts(self):
        """Zpracuje nejnovější články a přidá k nim shrnutí."""
        latest_posts = self.get_latest_posts()
        print(f"Zpracovávám {len(latest_posts)} nejnovějších článků...")
        
        for post_file in latest_posts:
            print(f"Zpracovávám článek: {post_file.name}")
            post = self.get_post_content(post_file)
            
            if not post:
                continue
                
            try:
                # Generujeme shrnutí z obsahu článku
                if not post.content.strip():
                    print(f"Článek {post_file.name} je prázdný, přeskakuji.")
                    continue
                    
                summary_points = self.generate_summary(post.content)
                
                if summary_points:
                    # Přidáme shrnutí do front matter jako seznam
                    post.metadata["summary_points"] = summary_points
                    
                    # Uložíme aktualizovaný článek
                    with open(post_file, 'w', encoding='utf-8') as f:
                        f.write(frontmatter.dumps(post))
                    print(f"Shrnutí úspěšně vygenerováno pro: {post_file.name}")
                    
                    # Počkáme chvíli mezi API požadavky
                    sleep(1)
                    
            except Exception as e:
                print(f"Chyba při zpracování článku {post_file.name}: {str(e)}")
                continue
                
if __name__ == "__main__":
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("Prosím nastavte DEEPSEEK_API_KEY v prostředí")
        
    generator = PostSummaryGenerator(api_key)
    generator.process_posts()