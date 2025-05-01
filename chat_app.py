import os
import sys
import json
import requests
import tkinter as tk
from tkinter import scrolledtext, ttk
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

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OpenRouter Chat")
        self.root.geometry("800x600")
        
        # Konfigurace gridu
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=0)
        
        # Horní panel s výběrem modelu
        top_frame = ttk.Frame(root)
        top_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
        
        ttk.Label(top_frame, text="Model:").pack(side=tk.LEFT, padx=(0, 5))
        
        self.model_var = tk.StringVar(value=AVAILABLE_MODELS[0])
        model_dropdown = ttk.Combobox(top_frame, textvariable=self.model_var, values=AVAILABLE_MODELS, width=40)
        model_dropdown.pack(side=tk.LEFT, padx=(0, 10))
        
        # Hlavní oblast chatu
        chat_frame = ttk.Frame(root)
        chat_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        
        self.chat_display = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, height=20)
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        self.chat_display.config(state=tk.DISABLED)
        
        # Spodní panel pro vstup
        input_frame = ttk.Frame(root)
        input_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
        
        self.input_field = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, height=3)
        self.input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        self.input_field.bind("<Return>", self.on_enter)
        self.input_field.bind("<Shift-Return>", self.new_line)
        
        send_button = ttk.Button(input_frame, text="Odeslat", command=self.send_message)
        send_button.pack(side=tk.RIGHT)

        # Historie konverzace
        self.conversation_history = []
        
        # Vizuální oddělení
        ttk.Separator(chat_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=5)
        
        # Informace o zpracování
        self.status_var = tk.StringVar(value="Připraven")
        ttk.Label(chat_frame, textvariable=self.status_var).pack(anchor=tk.W)
        
        # Kontrola API klíče
        if not OPENROUTER_API_KEY:
            self.update_chat("Systém", "Chybí API klíč! Přidejte OPENROUTER_API_KEY do souboru .env")
    
    def new_line(self, event):
        """Vložení nového řádku při stisku Shift+Enter"""
        return "break"
    
    def on_enter(self, event):
        """Zpracování stisku klávesy Enter"""
        self.send_message()
        return "break"
    
    def update_chat(self, sender, message):
        """Přidá zprávu do chat boxu"""
        self.chat_display.config(state=tk.NORMAL)
        if self.chat_display.get("1.0", tk.END).strip():
            self.chat_display.insert(tk.END, "\n\n")
        
        if sender == "Uživatel":
            self.chat_display.insert(tk.END, f"{sender}: ", "user")
        elif sender == "AI":
            self.chat_display.insert(tk.END, f"{sender}: ", "ai")
        else:
            self.chat_display.insert(tk.END, f"{sender}: ", "system")
        
        self.chat_display.insert(tk.END, message)
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
        
        # Přidání tagů pro formátování
        self.chat_display.tag_config("user", foreground="blue")
        self.chat_display.tag_config("ai", foreground="green")
        self.chat_display.tag_config("system", foreground="red")
    
    def send_message(self):
        """Odeslání zprávy do OpenRouter API"""
        user_input = self.input_field.get("1.0", tk.END).strip()
        if not user_input:
            return
        
        # Zobrazt uživatelskou zprávu v chatu
        self.update_chat("Uživatel", user_input)
        
        # Vymazat vstupní pole
        self.input_field.delete("1.0", tk.END)
        
        # Přidat zprávu do historie
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Pokud nemáme API klíč, nevykonáme API volání
        if not OPENROUTER_API_KEY:
            self.update_chat("Systém", "Nelze odeslat dotaz bez API klíče. Přidejte OPENROUTER_API_KEY do souboru .env")
            return
        
        # Aktualizace stavu
        self.status_var.set("Zpracovávám dotaz...")
        self.root.update_idletasks()
        
        # Získání odpovědi z API
        try:
            response = self.get_ai_response(user_input)
            self.update_chat("AI", response)
            self.conversation_history.append({"role": "assistant", "content": response})
        except Exception as e:
            self.update_chat("Systém", f"Chyba: {str(e)}")
        finally:
            self.status_var.set("Připraven")
    
    def get_ai_response(self, user_input):
        """Získá odpověď z OpenRouter API"""
        selected_model = self.model_var.get()
        
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://chat.openrouter.ai/"
        }
        
        data = {
            "model": selected_model,
            "messages": self.conversation_history
        }
        
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data
        )
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            raise Exception(f"API chyba: {response.status_code} - {response.text}")

if __name__ == "__main__":
    # Kontrola, zda je nainstalován tkinter
    try:
        root = tk.Tk()
        app = ChatApp(root)
        root.mainloop()
    except Exception as e:
        print(f"Chyba při spuštění aplikace: {str(e)}") 