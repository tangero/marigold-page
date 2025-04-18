#!/bin/bash

# Nastavení barev pro výpis
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}=========================================${NC}"
echo -e "${GREEN}       MARIGOLD.CZ SHRNUTÍ              ${NC}"
echo -e "${GREEN}=========================================${NC}"

# Kontrola existence .env souboru
if [ ! -f ".env" ]; then
    echo -e "${RED}Soubor .env nebyl nalezen v aktuálním adresáři!${NC}"
    echo -e "${YELLOW}Nejprve spusťte ./fix_env.sh pro vytvoření .env souboru.${NC}"
    exit 1
fi

# Vytvoříme dočasný soubor pro spuštění
TMP_FILE=$(mktemp)
cat > "$TMP_FILE" << 'EOF'
#!/usr/bin/env python3
import os
import sys
from dotenv import load_dotenv
import importlib.util

# Explicitně načteme .env soubor
env_path = os.path.join(os.getcwd(), ".env")
print(f"Načítám .env z: {env_path}")
load_dotenv(env_path)

# Zkontrolujeme, zda je API klíč nastaven
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    print("❌ API klíč OPENROUTER_API_KEY nebyl nalezen v .env souboru!")
    sys.exit(1)

print(f"✅ API klíč OPENROUTER_API_KEY nalezen (začíná na: {api_key[:10]}...)")

# Importujeme a spustíme hlavní modul
try:
    spec = importlib.util.spec_from_file_location("generator", "generate_local_summaries.py")
    generator = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(generator)
    
    # Spustíme hlavní funkci
    print("Spouštím generování shrnutí...")
    generator.main()
except Exception as e:
    print(f"❌ Došlo k chybě: {e}")
    import traceback
    print(traceback.format_exc())
    sys.exit(1)
EOF

echo -e "${YELLOW}Nastavuji oprávnění pro spouštěcí soubor...${NC}"
chmod +x "$TMP_FILE"

echo -e "${GREEN}Spouštím generování shrnutí s explicitním načtením .env souboru...${NC}"
# Aktivace virtuálního prostředí, pokud existuje
if [ -d ".venv" ]; then
    echo -e "${YELLOW}Aktivuji virtuální prostředí...${NC}"
    if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # macOS nebo Linux
        source .venv/bin/activate
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
        # Windows
        source .venv/Scripts/activate
    fi
fi

# Spuštění skriptu
python3 "$TMP_FILE"
EXIT_CODE=$?

# Úklid
rm "$TMP_FILE"

if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}=========================================${NC}"
    echo -e "${GREEN}       GENEROVÁNÍ DOKONČENO             ${NC}"
    echo -e "${GREEN}=========================================${NC}"
else
    echo -e "${RED}=========================================${NC}"
    echo -e "${RED}       GENEROVÁNÍ SELHALO                ${NC}"
    echo -e "${RED}=========================================${NC}"
fi 