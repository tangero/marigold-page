#!/bin/bash

# Nastavení barev pro výpis
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}       MARIGOLD.CZ NÁSTROJE             ${NC}"
echo -e "${GREEN}=========================================${NC}"

# Kontrola a instalace závislostí Python
echo -e "${YELLOW}Kontrola a instalace Python závislostí...${NC}"

# Pokusíme se nainstalovat balíčky do uživatelského adresáře bez potřeby oprávnění správce
echo -e "${YELLOW}Instaluji balíčky pro uživatele...${NC}"
python3 -m pip install --user --upgrade pip
python3 -m pip install --user PyYAML python-frontmatter requests openai

# Zkusíme ověřit přítomnost yaml modulu
if ! python3 -c "import yaml" 2>/dev/null; then
    echo -e "${RED}Nepodařilo se nainstalovat PyYAML standardním způsobem, zkouším alternativní řešení...${NC}"
    
    # Vytvoříme a aktivujeme virtuální prostředí
    echo -e "${YELLOW}Vytvářím virtuální prostředí Python...${NC}"
    python3 -m venv marigold_env
    
    # Aktivace virtuálního prostředí závisí na operačním systému
    if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # macOS nebo Linux
        source marigold_env/bin/activate
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        # Windows
        source marigold_env/Scripts/activate
    else
        echo -e "${RED}Nepodporovaný operační systém pro aktivaci virtuálního prostředí.${NC}"
        exit 1
    fi
    
    # Instalace balíčků ve virtuálním prostředí
    echo -e "${YELLOW}Instaluji balíčky ve virtuálním prostředí...${NC}"
    pip install PyYAML python-frontmatter requests openai
    
    # Spustíme skript ve virtuálním prostředí
    echo -e "${GREEN}Spouštím skript ve virtuálním prostředí...${NC}"
    python generate_local_summaries.py
    
    # Deaktivace virtuálního prostředí
    deactivate
    
    # Ukončíme script, protože jsme skript už spustili ve virtuálním prostředí
    exit 0
fi

# Pokud jsme se dostali sem, znamená to, že balíčky byly úspěšně nainstalovány
echo -e "${GREEN}Všechny potřebné balíčky jsou nainstalovány.${NC}"

# Kontrola a vytvoření adresáře pro pojmy, pokud neexistuje
if [ ! -d "_data" ]; then
    echo -e "${YELLOW}Vytvářím adresář _data...${NC}"
    mkdir -p _data
fi

# Kontrola existence souboru pojmy.json
if [ ! -f "_data/pojmy.json" ]; then
    echo -e "${YELLOW}Soubor _data/pojmy.json neexistuje, vytvářím základní strukturu...${NC}"
    echo '[
  {
    "keyword": "Wi-Fi",
    "variations": ["WiFi", "WIFI", "wifi", "Wi-Fi síť", "WiFi síť", "bezdrátová síť"],
    "link": "/search?q=wifi"
  },
  {
    "keyword": "mobilní síť",
    "variations": ["mobilní sítě", "mobilní telefonní síť", "mobilní datová síť"],
    "link": "/mobilni-site"
  },
  {
    "keyword": "5G",
    "variations": ["5G síť", "5G sítě", "5G technologie"],
    "link": "/search?q=5G"
  },
  {
    "keyword": "umělá inteligence",
    "variations": ["AI", "strojové učení", "machine learning", "LLM", "velký jazykový model"],
    "link": "/ai"
  },
  {
    "keyword": "ChatGPT",
    "variations": ["chat GPT", "GPT", "GPT-4"],
    "link": "/search?q=chatgpt"
  },
  {
    "keyword": "Model Context Protocol",
    "link": "/ai/2025-03-15-mcp"
  }
]' > _data/pojmy.json
    echo -e "${GREEN}Soubor _data/pojmy.json byl vytvořen s ukázkovými pojmy${NC}"
fi

# Zkontrolujeme, zda existuje generate_local_summaries.py
if [ ! -f "generate_local_summaries.py" ]; then
    echo -e "${RED}Skript generate_local_summaries.py nebyl nalezen!${NC}"
    exit 1
fi

# Nastavení správných oprávnění pro spuštění
chmod +x generate_local_summaries.py

# Kontrola a instalace Jekyll závislostí (pokud je to Jekyll projekt)
if [ -f "Gemfile" ]; then
    echo -e "${YELLOW}Kontrola a instalace Jekyll závislostí...${NC}"
    bundle check || bundle install
fi

# Spuštění generate_local_summaries.py
echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}       SPOUŠTÍM GENERÁTOR SHRNUTÍ        ${NC}"
echo -e "${GREEN}=========================================${NC}"
python3 generate_local_summaries.py

echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}       ZPRACOVÁNÍ DOKONČENO              ${NC}"
echo -e "${GREEN}=========================================${NC}"