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

# Seznam potřebných balíčků a jejich importních názvů
declare -A PACKAGES=(
    ["PyYAML"]="yaml"
    ["python-frontmatter"]="frontmatter"
    ["requests"]="requests"
    ["openai"]="openai"
    ["python-dotenv"]="dotenv"
    ["pathlib"]="pathlib"
    ["regex"]="regex"
)

# Kontrola, zda jsme ve virtuálním prostředí
if [ -n "$VIRTUAL_ENV" ]; then
    echo -e "${YELLOW}Detekováno aktivní virtuální prostředí: $VIRTUAL_ENV${NC}"
    echo -e "${YELLOW}Instaluji balíčky do virtuálního prostředí...${NC}"
    pip install --upgrade pip
    pip install "${!PACKAGES[@]}"
else
    # Vytvoříme a aktivujeme virtuální prostředí
    echo -e "${YELLOW}Vytvářím virtuální prostředí Python...${NC}"
    python3 -m venv .venv
    
    # Aktivace virtuálního prostředí
    if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # macOS nebo Linux
        source .venv/bin/activate
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        # Windows
        source .venv/Scripts/activate
    else
        echo -e "${RED}Nepodporovaný operační systém pro aktivaci virtuálního prostředí.${NC}"
        exit 1
    fi
    
    # Instalace balíčků ve virtuálním prostředí
    echo -e "${YELLOW}Instaluji balíčky ve virtuálním prostředí...${NC}"
    pip install --upgrade pip
    pip install "${!PACKAGES[@]}"
fi

# Kontrola instalace balíčků
echo -e "${YELLOW}Kontroluji instalaci balíčků...${NC}"
for pkg in "${!PACKAGES[@]}"; do
    import_name="${PACKAGES[$pkg]}"
    if ! python3 -c "import ${import_name}" 2>/dev/null; then
        echo -e "${RED}Chyba: Balíček ${pkg} (import: ${import_name}) se nepodařilo nainstalovat!${NC}"
        exit 1
    fi
done

echo -e "${GREEN}Všechny potřebné balíčky jsou nainstalovány.${NC}"

# Kontrola a vytvoření adresáře pro pojmy, pokud neexistuje
if [ ! -d "_data" ]; then
    echo -e "${YELLOW}Vytvářím adresář _data...${NC}"
    mkdir -p _data
fi

# Kontrola existence souboru keywords.yml
if [ ! -f "_data/keywords.yml" ]; then
    echo -e "${YELLOW}Soubor _data/keywords.yml neexistuje, vytvářím základní strukturu...${NC}"
    echo '---
# Klíčová slova a jejich metadata
# Formát:
# id-klíčového-slova:
#   name: "Název klíčového slova"
#   description: "Popis klíčového slova"
#   url: "URL odkazu"
#   category: "Kategorie (Firma/Produkt/Technologie/Osoba)"
#   count: 0
#   created: "YYYY-MM-DD"
#   last_found: "YYYY-MM-DD"
' > _data/keywords.yml
    echo -e "${GREEN}Soubor _data/keywords.yml byl vytvořen s ukázkovou strukturou${NC}"
fi

# Kontrola existence .env souboru
if [ ! -f ".env" ]; then
    echo -e "${RED}Soubor .env nebyl nalezen!${NC}"
    echo -e "${YELLOW}Vytvářím základní .env soubor...${NC}"
    # Vytvoříme základní .env soubor
    cat > ".env" << EOF
# Konfigurační soubor pro API klíče

# API klíč pro OpenRouter
OPENROUTER_API_KEY=

# API klíč pro DeepSeek
DEEPSEEK_API_KEY=

# Model LLM
LLM_MODEL=google/gemini-2.0-flash-001
EOF
    echo -e "${YELLOW}Zadejte váš OpenRouter API klíč:${NC}"
    read OPENROUTER_KEY
    # Nahradíme prázdný klíč zadaným
    sed -i '' "s/OPENROUTER_API_KEY=/OPENROUTER_API_KEY=$OPENROUTER_KEY/" .env
    echo -e "${GREEN}API klíč byl uložen do .env souboru${NC}"
fi

# Spuštění hlavního skriptu s explicitním načtením .env
echo -e "${GREEN}Spouštím hlavní skript s explicitním načtením .env...${NC}"
python3 -c "
import os
from dotenv import load_dotenv
import importlib.util

# Explicitně načteme .env soubor
env_path = os.path.join(os.getcwd(), '.env')
print(f'Načítám .env z: {env_path}')
load_dotenv(env_path)

# Importujeme a spustíme hlavní modul
try:
    spec = importlib.util.spec_from_file_location('generator', 'generate_local_summaries.py')
    generator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(generator)
    
    # Spustíme hlavní funkci
    generator.main()
except Exception as e:
    print(f'Chyba: {e}')
    import traceback
    print(traceback.format_exc())
"

echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}       ZPRACOVÁNÍ DOKONČENO              ${NC}"
echo -e "${GREEN}=========================================${NC}"