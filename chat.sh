#!/bin/bash

# Barvy pro výpis
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}   OpenRouter Terminal Chat - Instalátor   ${NC}"
echo -e "${BLUE}========================================${NC}"

# Kontrola, zda je Python nainstalován
echo -e "${YELLOW}Kontroluji instalaci Pythonu...${NC}"
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Python 3 není nainstalován. Prosím, nainstalujte Python 3.${NC}"
    exit 1
fi

python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo -e "${GREEN}Nalezen Python $python_version${NC}"

# Kontrola, zda existuje .env soubor
echo -e "${YELLOW}Kontroluji soubor .env...${NC}"
if [ ! -f .env ]; then
    echo -e "${RED}Soubor .env neexistuje!${NC}"
    echo -e "${YELLOW}Vytvářím soubor .env z .env.example...${NC}"
    
    if [ -f .env.example ]; then
        cp .env.example .env
        echo -e "${GREEN}Soubor .env byl vytvořen. Upravte jej, prosím, s vaším API klíčem.${NC}"
    else
        echo -e "${RED}Soubor .env.example neexistuje. Vytvářím základní .env soubor...${NC}"
        echo "OPENROUTER_API_KEY=vaš_api_klíč_zde" > .env
        echo -e "${GREEN}Vytvořen základní .env soubor. Upravte jej, prosím, s vaším API klíčem.${NC}"
    fi
else
    echo -e "${GREEN}Soubor .env nalezen${NC}"
fi

# Vytvoření a aktivace virtuálního prostředí
VENV_DIR="chat_venv"
echo -e "${YELLOW}Vytvářím virtuální prostředí v adresáři '$VENV_DIR'...${NC}"

# Kontrola, zda virtuální prostředí již existuje
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo -e "${RED}Chyba při vytváření virtuálního prostředí${NC}"
        exit 1
    fi
    echo -e "${GREEN}Virtuální prostředí úspěšně vytvořeno${NC}"
else
    echo -e "${GREEN}Virtuální prostředí již existuje${NC}"
fi

# Aktivace virtuálního prostředí
echo -e "${YELLOW}Aktivuji virtuální prostředí...${NC}"
if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # macOS nebo Linux
    source "$VENV_DIR/bin/activate"
else
    # Windows
    source "$VENV_DIR/Scripts/activate"
fi

if [ $? -ne 0 ]; then
    echo -e "${RED}Chyba při aktivaci virtuálního prostředí${NC}"
    exit 1
fi
echo -e "${GREEN}Virtuální prostředí aktivováno${NC}"

# Instalace požadovaných knihoven ve virtuálním prostředí
echo -e "${YELLOW}Instaluji potřebné knihovny do virtuálního prostředí...${NC}"
if [ -f chat_requirements.txt ]; then
    python -m pip install -r chat_requirements.txt
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Knihovny úspěšně nainstalovány do virtuálního prostředí${NC}"
    else
        echo -e "${RED}Chyba při instalaci knihoven${NC}"
        exit 1
    fi
else
    echo -e "${RED}Soubor chat_requirements.txt neexistuje!${NC}"
    echo -e "${YELLOW}Instaluji základní knihovny...${NC}"
    python -m pip install requests python-dotenv
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Základní knihovny úspěšně nainstalovány do virtuálního prostředí${NC}"
    else
        echo -e "${RED}Chyba při instalaci základních knihoven${NC}"
        exit 1
    fi
fi

# Spuštění terminálové aplikace z virtuálního prostředí
echo -e "${YELLOW}Spouštím chatovací aplikaci...${NC}"
echo -e "${BLUE}========================================${NC}"
python chat_terminal.py

# Deaktivace virtuálního prostředí a kontrola, zda aplikace byla ukončena správně
exit_code=$?
deactivate
if [ $exit_code -ne 0 ]; then
    echo -e "${RED}Aplikace byla ukončena s chybou${NC}"
    exit 1
fi 