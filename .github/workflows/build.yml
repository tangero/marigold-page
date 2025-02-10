import os
import yaml
import frontmatter
from pathlib import Path
import requests
import json
from datetime import datetime
import re

class PostSummaryGenerator:
    def __init__(self, api_key, posts_dir="_posts", max_posts=10):
        self.api_key = api_key
        self.posts_dir = posts_dir
        self.max_posts = max_posts
        
    def get_post_date(self, filename):
        """Extrahuje datum z názvu souboru Jekyll článku (YYYY-MM-DD-title.md)"""
        date_pattern = r'(\d{4}-\d{2}-\d{2})'
        match = re.match(date_pattern, filename)
        if match:
            return datetime.strptime(match.group(1), '%Y-%m-%d')
        return None
        
    def get_post_content(self, post_path):
        """Načte obsah článku a jeho front matter."""
        with open(post_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        return post
        
    def generate_summary(self, content):
        """Generuje bodové shrnutí pomocí Deepseek API."""
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        prompt = """Vytvoř stručné shrnutí následujícího českého textu ve 3-4 klíčových bodech. 
        Každý bod by měl být krátký (max 10 slov) a začínat pomlčkou.
        Zaměř se na hlavní myšlenky a konkrétní informace.
        
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
        
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            summary = response.json()["choices"][0]["message"]["content"]
            bullet_points = [line.strip() for line in summary.split('\n') if line.strip()]
            return bullet_points
        else:
            raise Exception(f"API Error: {response.status_code}")
            
    def get_latest_posts(self):
        """Získá nejnovější články seřazené podle data"""
        posts_path = Path(self.posts_dir)
        posts = []
        
        for post_file in posts_path.glob("*.md"):
            post_date = self.get_post_date(post_file.name)
            if post_date:
                posts.append((post_date, post_file))
                
        # Seřadí články podle data sestupně a vezme nejnovějších X
        return [post[1] for post in sorted(posts, reverse=True)[:self.max_posts]]
            
    def process_posts(self):
        """Zpracuje nejnovější články a přidá k nim shrnutí."""
        latest_posts = self.get_latest_posts()
        print(f"Zpracovávám {len(latest_posts)} nejnovějších článků...")
        
        for post_file in latest_posts:
            print(f"Zpracovávám článek: {post_file.name}")
            post = self.get_post_content(post_file)
            
            # Pokud už shrnutí existuje, přeskočíme
            if "summary_points" in post.metadata:
                print(f"Článek již má shrnutí, přeskakuji: {post_file.name}")
                continue
                
            try:
                # Generujeme shrnutí z obsahu článku
                summary_points = self.generate_summary(post.content)
                
                # Přidáme shrnutí do front matter jako seznam
                post.metadata["summary_points"] = summary_points
                
                # Uložíme aktualizovaný článek
                with open(post_file, 'w', encoding='utf-8') as f:
                    f.write(frontmatter.dumps(post))
                print(f"Shrnutí úspěšně vygenerováno pro: {post_file.name}")
                
            except Exception as e:
                print(f"Chyba při zpracování článku {post_file.name}: {str(e)}")
                continue
                
if __name__ == "__main__":
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("Prosím nastavte DEEPSEEK_API_KEY v prostředí")
        
    generator = PostSummaryGenerator(api_key)
    generator.process_posts()