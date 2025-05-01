import os
import sys
import json
import requests
# Readline je na macOS součástí standardní knihovny, na jiných platformách může být potřeba doinstalovat
import platform
if platform.system() != 'Darwin':  # Není macOS
    try:
        import readline
    except ImportError:
        pass  # Readline není kritická komponenta
from dotenv import load_dotenv

# Načtení API klíče z .env souboru
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Seznam dostupných modelů
AVAILABLE_MODELS = [
    "anthropic/claude-3-sonnet-20240229",
    "google/gemini-2.5-pro-preview-03-25",
    "openrouter/optimus-alpha",
    "openrouter/quasar-alpha",
]

class TerminalColors:
    """Barvy pro terminál"""
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class TerminalChatApp:
    def __init__(self):
        self.conversation_history = []
        
        # Kontrola API klíče
        if not OPENROUTER_API_KEY:
            print(f"{TerminalColors.RED}Chybí API klíč! Přidejte OPENROUTER_API_KEY do souboru .env{TerminalColors.END}")
            sys.exit(1)
        
        # Úvodní zpráva
        print(f"\n{TerminalColors.BOLD}=== OpenRouter Terminal Chat ==={TerminalColors.END}")
        print(f"{TerminalColors.BLUE}Pro ukončení napište 'exit' nebo stiskněte Ctrl+C{TerminalColors.END}")
        
        # Výběr modelu
        self.selected_model = self.select_model()
        print(f"\n{TerminalColors.GREEN}Vybrán model: {self.selected_model}{TerminalColors.END}")
    
    def select_model(self):
        """Umožní uživateli vybrat model z dostupných možností"""
        print(f"\n{TerminalColors.BOLD}Dostupné modely:{TerminalColors.END}")
        for i, model in enumerate(AVAILABLE_MODELS, 1):
            print(f"{i}. {model}")
        
        while True:
            try:
                choice = input(f"\n{TerminalColors.YELLOW}Vyberte číslo modelu (1-{len(AVAILABLE_MODELS)}): {TerminalColors.END}")
                index = int(choice) - 1
                if 0 <= index < len(AVAILABLE_MODELS):
                    return AVAILABLE_MODELS[index]
                else:
                    print(f"{TerminalColors.RED}Neplatná volba. Zadejte číslo 1-{len(AVAILABLE_MODELS)}.{TerminalColors.END}")
            except ValueError:
                print(f"{TerminalColors.RED}Neplatný vstup. Zadejte číslo.{TerminalColors.END}")
            except KeyboardInterrupt:
                print("\nUkončuji...")
                sys.exit(0)
    
    def get_ai_response(self, user_input):
        """Získá odpověď z OpenRouter API"""
        print(f"\n{TerminalColors.YELLOW}Zpracovávám dotaz...{TerminalColors.END}")
        
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://chat.openrouter.ai/"
        }
        
        data = {
            "model": self.selected_model,
            "messages": self.conversation_history
        }
        
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=60  # 60 sekund timeout
            )
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                return f"API chyba: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Chyba: {str(e)}"
    
    def run(self):
        """Spustí chatovací smyčku"""
        try:
            while True:
                # Získat vstup od uživatele
                user_input = input(f"\n{TerminalColors.BOLD}Vy: {TerminalColors.END}")
                
                # Kontrola ukončení
                if user_input.lower() in ['exit', 'quit', 'konec']:
                    print(f"\n{TerminalColors.BLUE}Ukončuji chat. Na shledanou!{TerminalColors.END}")
                    break
                
                # Přidat zprávu do historie
                self.conversation_history.append({"role": "user", "content": user_input})
                
                # Získat a zobrazit odpověď
                response = self.get_ai_response(user_input)
                print(f"\n{TerminalColors.BOLD}{TerminalColors.GREEN}AI: {TerminalColors.END}{response}")
                
                # Přidat odpověď do historie
                self.conversation_history.append({"role": "assistant", "content": response})
        
        except KeyboardInterrupt:
            print(f"\n\n{TerminalColors.BLUE}Ukončuji chat. Na shledanou!{TerminalColors.END}")
            sys.exit(0)

if __name__ == "__main__":
    app = TerminalChatApp()
    app.run() 