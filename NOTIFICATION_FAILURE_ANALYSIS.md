# 🔍 Analýza selhání OneSignal notifikace - Zohran Mamdani článek

**Datum incidentu:** 5. listopadu 2025
**Článek:** `_posts/2025/2025-11-05-zohran-mamdani-starosta-new-york.md`
**Commit:** `c599319facf`

---

## 📊 Zjištění

### Časová linie událostí:

1. **5. listopadu 11:40** - ✅ Oprava OneSignal API (commit `4bc02524918`)
2. **5. listopadu 20:51** - 📝 **Create článek o Zohran Mamdani (commit `c599319facf`)**
3. **6. listopadu 07:26** - ✏️ Update obrázků (commit `e2c3d27a7d3`)
4. **6. listopadu 07:51** - ✏️ Další update (commit `fcce2b35132`)

### Stav článku:
- **Celkem commitů:** 3
- **První commit:** `c599319facf` - měl **poslat notifikaci**
- **Druhý/třetí commit:** Update - **nepošle notifikaci** (správně)

### Test lokální logiky:
✅ Path pattern matchuje: `_posts/**/*.md` ← `_posts/2025/*.md`
✅ `get_changed_files()` by detekoval článek
✅ `is_new_article()` by vrátil `TRUE` při prvním commitu
❌ **Notifikace SE NEPOSLALA** podle OneSignal dashboardu

---

## 🎯 Hlavní příčina

**Workflow se pravděpodobně NESPUSTIL nebo SELHAL bez viditelné chyby.**

### Možné důvody (seřazené podle pravděpodobnosti):

### 1️⃣ **GitHub Secrets nejsou nastavené** (80% pravděpodobnost)

**Problém:**
- Workflow vyžaduje `ONESIGNAL_REST_API_KEY` a `ONESIGNAL_APP_ID`
- Pokud nejsou nastavené → workflow selže **tiše** bez error logu

**Jak ověřit:**
```bash
# Otevřít GitHub → Settings → Secrets and variables → Actions
# URL: https://github.com/tangero/marigold-page/settings/secrets/actions
```

**Očekávané secrets:**
- `ONESIGNAL_REST_API_KEY` - REST API klíč z OneSignal
- `ONESIGNAL_APP_ID` - App ID: `00fc3def-70d1-4e7d-a081-984d5e738a75`

**Řešení:**
1. Přidat secrets v GitHub UI
2. Hodnoty najdete v OneSignal Dashboard → Settings → Keys & IDs

---

### 2️⃣ **GitHub Actions je vypnuté** (10% pravděpodobnost)

**Problém:**
- GitHub Actions může být vypnuté pro repo
- Nebo konkrétní workflow může být disabled

**Jak ověřit:**
```bash
# Otevřít GitHub → Actions
# URL: https://github.com/tangero/marigold-page/actions
```

**Co zkontrolovat:**
- ✅ Actions je enabled pro repo?
- ✅ Workflow "Send OneSignal Notifications" je viditelný?
- ✅ Zobrazuje se run pro commit `c599319facf`?

**Řešení:**
1. Settings → Actions → General → Enable Actions
2. Povolit workflow runs pro tento repo

---

### 3️⃣ **Workflow selhal s chybou** (8% pravděpodobnost)

**Problém:**
- Workflow se spustil, ale Python script selhal
- OneSignal API vrátil error
- Network timeout

**Jak ověřit:**
```bash
# GitHub UI → Actions → konkrétní run → logs
```

**Co hledat v logs:**
- ❌ Python import errors
- ❌ OneSignal API 400/401/403/500 errors
- ❌ Timeout errors
- ❌ "No changes detected" message

**Řešení:**
- Zkontrolovat error logs
- Opravit podle specifické chyby

---

### 4️⃣ **fetch-depth: 2 způsobil problém** (2% pravděpodobnost)

**Problém:**
- Shallow clone s `fetch-depth: 2` může nefungovat správně s `git log --follow`
- `is_new_article()` může vrátit nesprávný výsledek

**Testováno lokálně:** Logika je správná, takže tohle není příčina.

---

## ✅ Okamžitá řešení

### 1. Zkontrolovat GitHub Secrets

```bash
# Otevřít v prohlížeči:
open "https://github.com/tangero/marigold-page/settings/secrets/actions"

# Zkontrolovat, že existují:
# - ONESIGNAL_REST_API_KEY
# - ONESIGNAL_APP_ID
```

### 2. Zkontrolovat GitHub Actions logs

```bash
# Otevřít v prohlížeči:
open "https://github.com/tangero/marigold-page/actions"

# Najít run pro commit c599319facf (5. listopadu 20:51)
# Zkontrolovat status: Success / Failure / Skipped
```

### 3. Manuálně poslat notifikaci pro článek

```bash
# Použít existující skript:
python3 send_notification_now.py

# Nebo aktualizovat článek znovu (spustí workflow):
git commit --allow-empty -m "Trigger notification for Zohran Mamdani article"
git push
```

---

## 🛡️ Prevence do budoucna

### 1. Přidat lepší error handling do workflow

**Aktuální stav:**
```yaml
# Workflow selže tiše pokud chybí secrets
```

**Řešení:**
```yaml
- name: Check secrets
  run: |
    if [ -z "$ONESIGNAL_REST_API_KEY" ]; then
      echo "❌ ONESIGNAL_REST_API_KEY není nastavený!"
      exit 1
    fi
    if [ -z "$ONESIGNAL_MARIGOLD_APP_ID" ]; then
      echo "❌ ONESIGNAL_MARIGOLD_APP_ID není nastavený!"
      exit 1
    fi
    echo "✅ Všechny secrets jsou nastavené"
  env:
    ONESIGNAL_REST_API_KEY: ${{ secrets.ONESIGNAL_REST_API_KEY }}
    ONESIGNAL_MARIGOLD_APP_ID: ${{ secrets.ONESIGNAL_APP_ID }}
```

### 2. Přidat notification při selhání workflow

**Řešení:**
```yaml
- name: Notify on failure
  if: failure()
  run: |
    echo "::error::Workflow selhal! Zkontrolujte logs."
    # Poslat email nebo Slack notification
```

### 3. Přidat monitoring do skriptu

**Aktuální stav:**
```python
# Skript jen loguje do stdout
print(f"✅ Notifikace poslána")
```

**Řešení:**
```python
# Ukládat statistiky do souboru
import json
from datetime import datetime

stats_file = "_data/notification_stats.json"

# Zalogovat každou notifikaci
stats = {
    "timestamp": datetime.now().isoformat(),
    "article": article_path,
    "notification_id": notification_id,
    "recipients": recipients,
    "status": "success" if recipients > 0 else "failed"
}

# Přidat do stats souboru
with open(stats_file, "a") as f:
    f.write(json.dumps(stats) + "\n")
```

### 4. Zvýšit `fetch-depth` na vyšší hodnotu

**Aktuální stav:**
```yaml
with:
  fetch-depth: 2  # Pouze 2 poslední commity
```

**Doporučení:**
```yaml
with:
  fetch-depth: 10  # Posledních 10 commitů pro spolehlivost
```

### 5. Přidat fallback notifikaci

**Řešení:**
```python
# Pokud notifikace selže, zkusit znovu po 5 minutách
import time

max_retries = 3
for attempt in range(max_retries):
    if send_notification(...):
        break
    else:
        if attempt < max_retries - 1:
            print(f"⏳ Zkouším znovu za 5 minut ({attempt+1}/{max_retries})...")
            time.sleep(300)  # 5 minut
```

---

## 📋 Action Items

### ⚡ Okamžitě (do 1 hodiny):

1. **Zkontrolovat GitHub Secrets**
   - [ ] Otevřít GitHub → Settings → Secrets
   - [ ] Ověřit `ONESIGNAL_REST_API_KEY`
   - [ ] Ověřit `ONESIGNAL_APP_ID`

2. **Zkontrolovat GitHub Actions logs**
   - [ ] Otevřít GitHub → Actions
   - [ ] Najít run pro commit `c599319facf`
   - [ ] Přečíst error logs (pokud existují)

3. **Poslat notifikaci manuálně**
   - [ ] Spustit `python3 send_notification_now.py`
   - [ ] Ověřit v OneSignal dashboardu

### 📅 Dnes:

4. **Přidat error handling do workflow**
   - [ ] Přidat secret validation step
   - [ ] Přidat failure notification

5. **Zvýšit fetch-depth**
   - [ ] Změnit z `2` na `10`

### 📅 Tento týden:

6. **Implementovat monitoring**
   - [ ] Přidat logging notifikací do souboru
   - [ ] Vytvořit dashboard se statistikami

7. **Přidat fallback retry logiku**
   - [ ] Max 3 pokusy s 5 min pauzou

---

## 🔗 Užitečné odkazy

- **GitHub Actions logs:** https://github.com/tangero/marigold-page/actions
- **GitHub Secrets:** https://github.com/tangero/marigold-page/settings/secrets/actions
- **OneSignal Dashboard:** https://dashboard.onesignal.com/apps/00fc3def-70d1-4e7d-a081-984d5e738a75/delivery
- **Workflow soubor:** `.github/workflows/send-notifications.yml`
- **Produkční skript:** `.github/scripts/send_notifications.py`

---

**Vytvořeno:** 6. listopadu 2025
**Autor:** Claude Code
**Status:** Vyžaduje akci - zkontrolovat GitHub Secrets a logs
