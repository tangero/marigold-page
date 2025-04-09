#!/bin/bash

# Nastavení barev pro výpis
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}       OPRAVA .ENV SOUBORU              ${NC}"
echo -e "${GREEN}=========================================${NC}"

# Zkontrolujeme, zda existuje původní .env soubor
ORIG_ENV=".env"
TARGET_ENV=".env"

if [ -f "$ORIG_ENV" ]; then
    echo -e "${YELLOW}Našel jsem existující .env soubor v aktuálním adresáři.${NC}"
    
    # Přečteme hodnoty API klíčů ze souboru
    OPENROUTER_KEY=""
    DEEPSEEK_KEY=""
    
    while IFS= read -r line; do
        if [[ $line == OPENROUTER_API_KEY=* ]]; then
            OPENROUTER_KEY="${line#*=}"
        elif [[ $line == DEEPSEEK_API_KEY=* ]]; then
            DEEPSEEK_KEY="${line#*=}"
        fi
    done < "$ORIG_ENV"
    
    echo -e "${YELLOW}Nalezeny klíče:${NC}"
    if [ -n "$OPENROUTER_KEY" ]; then
        echo -e "OPENROUTER_API_KEY=${OPENROUTER_KEY:0:10}..."
    else
        echo -e "${RED}OPENROUTER_API_KEY nebyl nalezen!${NC}"
    fi
    
    if [ -n "$DEEPSEEK_KEY" ]; then
        echo -e "DEEPSEEK_API_KEY=${DEEPSEEK_KEY:0:10}..."
    else
        echo -e "${RED}DEEPSEEK_API_KEY nebyl nalezen!${NC}"
    fi
else
    echo -e "${RED}Nenašel jsem žádný .env soubor v aktuálním adresáři.${NC}"
    echo -e "${YELLOW}Vytvářím nový .env soubor...${NC}"
    
    echo -e "${YELLOW}Zadejte váš OpenRouter API klíč:${NC}"
    read -r OPENROUTER_KEY
    
    echo -e "${YELLOW}Zadejte váš DeepSeek API klíč (nebo nechte prázdné):${NC}"
    read -r DEEPSEEK_KEY
fi

# Vytvořit nebo přepsat .env soubor
cat > "$TARGET_ENV" << EOF
# Konfigurační soubor pro API klíče
# Vygenerováno pomocí fix_env.sh

# API klíč pro OpenRouter
OPENROUTER_API_KEY=$OPENROUTER_KEY

# API klíč pro DeepSeek
DEEPSEEK_API_KEY=$DEEPSEEK_KEY

# Model LLM 
LLM_MODEL=google/gemini-2.0-flash-001
EOF

echo -e "${GREEN}Vytvořen nový .env soubor v aktuálním adresáři.${NC}"

# Nastavení oprávnění
chmod 600 "$TARGET_ENV"
echo -e "${YELLOW}Nastavena oprávnění 600 (čtení a zápis pouze pro vlastníka).${NC}"

echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}       OPRAVA DOKONČENA                 ${NC}"
echo -e "${GREEN}=========================================${NC}"

echo -e "${YELLOW}Pro otestování spusťte:${NC}"
echo -e "python3 debug_env.py" 