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

# Seznam potřebných balíčků a jejich importních názvů (jako pole)
PACKAGES=(
    "PyYAML:yaml"
    "python-frontmatter:frontmatter"
    "requests:requests"
    "openai:openai"
    "python-dotenv:dotenv"
    "pathlib:pathlib"
    "regex:regex"
)

# Kontrola, zda jsme ve virtuálním prostředí
if [ -n "$VIRTUAL_ENV" ]; then
    echo -e "${YELLOW}Detekováno aktivní virtuální prostředí: $VIRTUAL_ENV${NC}"
    echo -e "${YELLOW}Instaluji balíčky do virtuálního prostředí...${NC}"
    pip install --upgrade pip
    for pkg in "${PACKAGES[@]}"; do
        pip install "${pkg%%:*}"
    done
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
    for pkg in "${PACKAGES[@]}"; do
        pip install "${pkg%%:*}"
    done
fi

# Kontrola instalace balíčků
echo -e "${YELLOW}Kontroluji instalaci balíčků...${NC}"
for pkg in "${PACKAGES[@]}"; do
    pkg_name="${pkg%%:*}"
    import_name="${pkg##*:}"
    if ! python3 -c "import ${import_name}" 2>/dev/null; then
        echo -e "${RED}Chyba: Balíček ${pkg_name} (import: ${import_name}) se nepodařilo nainstalovat!${NC}"
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

# Model LLM (např. google/gemini-2.0-flash-001)
LLM_MODEL=google/gemini-2.0-flash-001

# Datum první dávky generování shrnutí (YYYY-MM-DD), optional
CUTOFF_DATE=2025-05-15
EOF
    echo -e "${YELLOW}Zadejte váš OpenRouter API klíč:${NC}"
    read OPENROUTER_KEY
    # Nahradíme prázdný klíč zadaným
    sed -i '' "s/OPENROUTER_API_KEY=/OPENROUTER_API_KEY=$OPENROUTER_KEY/" .env
    echo -e "${GREEN}API klíč byl uložen do .env souboru${NC}"
fi
# Načtení proměnných prostředí z .env do shellu
if [ -f ".env" ]; then
    echo -e "${YELLOW}Načítám proměnné prostředí z .env...${NC}"
    set -a
    source .env
    set +a
fi

# Zajistíme, že je proměnná CUTOFF_DATE nastavena pro automatické generování shrnutí
if [ -z "$CUTOFF_DATE" ]; then
    echo -e "${YELLOW}Proměnná CUTOFF_DATE není nastavena. Nastavuji výchozí hodnotu 2025-05-15${NC}"
    echo "CUTOFF_DATE=2025-05-15" >> .env
    export CUTOFF_DATE=2025-05-15
fi

# Spuštění generování shrnutí článků
echo -e "${GREEN}Spouštím generování shrnutí článků...${NC}"
bash run_with_env.sh

echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}       Shrnutí dokončeno                  ${NC}"
echo -e "${GREEN}=========================================${NC}"

# Validace a oprava YAML front matter
echo -e "${GREEN}Validuji a opravuji YAML front matter...${NC}"
python3 fix_yaml.py _posts --fix

# Generování audio verze
echo -e "${GREEN}Generuji audio verzi...${NC}"
python3 .github/scripts/podcast-automation-script.py

# Prolinkování klíčových pojmů
echo -e "${GREEN}Prolinkovávám klíčová spojení...${NC}"
python3 concept_links.py

# Překlad označených článků
echo -e "${GREEN}Překládám články označené pro překlad...${NC}"
python3 .github/scripts/translate_posts.py

echo -e "${GREEN}Všechny kroky dokončeny.${NC}"