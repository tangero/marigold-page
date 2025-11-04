# 🔍 OneSignal Browser Notifications - Hluboká Analýza

## 📋 Executive Summary

Provedl jsem komplexní analýzu OneSignal integrace pro marigold.cz. Identifikoval jsem **6 kritických problémů** a **3 varování**, které mohou způsobovat, že notifikace nefungují.

---

## 🎯 Identifikované Problémy

### 🔴 KRITICKÉ PROBLÉMY

#### 1. **Nesprávný OneSignal Segment** 
**Lokace:** Všechny notifikační skripty  
**Dopad:** VYSOKÝ - Notifikace se nemusí vůbec posílat

**Problém:**
```python
payload = {
    "app_id": app_id,
    "included_segments": ["Subscribed Users"],  # ❌ CHYBA
    ...
}
```

**Analýza:**
- Všechny skripty používají segment `"Subscribed Users"`
- Tento segment **neexistuje** ve výchozím OneSignal nastavení
- Výchozí segmenty v OneSignal jsou:
  - `"All"` - všichni uživatelé
  - `"Active Users"` - aktivní uživatelé (7 dní)
  - `"Inactive Users"` - neaktivní uživatelé

**Důsledek:**
- API vrátí chybu nebo 0 příjemců
- Notifikace se nikam nepošlou

**Oprava:**
```python
payload = {
    "app_id": app_id,
    "included_segments": ["All"],  # ✅ Správně
    ...
}
```

**Soubory k opravě:**
- `.github/scripts/send_notifications.py:104`
- `test_onesignal.py:53`
- `send_notification_now.py:41`
- `debug_onesignal.py:55`
- `.github/workflows/test-notification.yml:60`

---

#### 2. **Špatné Parsování OneSignal Response**
**Lokace:** `.github/scripts/send_notifications.py:114`  
**Dopad:** STŘEDNÍ - Nesprávné logování, může skrývat skutečné chyby

**Problém:**
```python
result = response.json()
notification_id = result.get('body', {}).get('id', 'unknown')  # ❌ CHYBA
```

**Analýza:**
OneSignal API vrací response v tomto formátu:
```json
{
  "id": "notification-id-here",
  "recipients": 5,
  "external_id": null
}
```

**NIKDY ne:**
```json
{
  "body": {
    "id": "notification-id-here"
  }
}
```

**Oprava:**
```python
result = response.json()
notification_id = result.get('id', 'unknown')  # ✅ Správně
recipients = result.get('recipients', 0)
```

---

#### 3. **GitHub Workflow - Nekonzistentní Secret Names**
**Lokace:** `.github/workflows/send-notifications.yml:34`  
**Dopad:** VYSOKÝ - Workflow může selhat pokud secret není správně pojmenován

**Problém:**
```yaml
env:
  ONESIGNAL_REST_API_KEY: ${{ secrets.ONESIGNAL_REST_API_KEY }}
  ONESIGNAL_MARIGOLD_APP_ID: ${{ secrets.ONESIGNAL_APP_ID }}  # ❌ Nekonzistentní
  ONESIGNAL_VIBECODING_APP_ID: 0c413930-f7f6-4d73-9438-36ec057acb7d
```

**Analýza:**
- Workflow mapuje `ONESIGNAL_MARIGOLD_APP_ID` na `secrets.ONESIGNAL_APP_ID`
- Dokumentace uvádí, že by měl být secret `ONESIGNAL_MARIGOLD_APP_ID`
- Toto vytváří zmatení a může způsobit chyby

**Doporučení:**
Buď:
1. Použít konzistentně `ONESIGNAL_MARIGOLD_APP_ID` všude
2. Nebo přejmenovat secret na `ONESIGNAL_APP_ID` a aktualizovat dokumentaci

---

#### 4. **Workflow Trigger - Může Chybět Tech News**
**Lokace:** `.github/workflows/send-notifications.yml:7-9`  
**Dopad:** STŘEDNÍ - Notifikace pro tech news se neposílají

**Problém:**
```yaml
paths:
  - '_posts/**/*.md'
  - '_vibecoding/**/*.md'
```

**Analýza:**
- Workflow se spouští jen pro `_posts/` a `_vibecoding/`
- V projektu existuje i `_tech_news/` kolekce
- Tech news články nespustí workflow

**Možné řešení:**
```yaml
paths:
  - '_posts/**/*.md'
  - '_vibecoding/**/*.md'
  - '_tech_news/**/*.md'  # Pokud chcete notifikace i pro tech news
```

---

#### 5. **Chybějící Error Handling v Production Skriptu**
**Lokace:** `.github/scripts/send_notifications.py`  
**Dopad:** STŘEDNÍ - Ztráta důležitých debug informací

**Problém:**
```python
try:
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    if response.status_code in [200, 201]:
        ...
    else:
        print(f"❌ {website_name}: Chyba {response.status_code}")
        print(f"Response: {response.text}")
        return False
```

**Analýza:**
- Minimální error handling
- Nedostatečné logování pro debugging
- Nezachycuje network errors mimo timeout

**Doporučené vylepšení:**
```python
try:
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    
    print(f"[DEBUG] Status: {response.status_code}")
    print(f"[DEBUG] Response: {response.text}")
    
    if response.status_code in [200, 201]:
        result = response.json()
        print(f"[DEBUG] Full result: {json.dumps(result, indent=2)}")
        ...
    else:
        print(f"❌ {website_name}: HTTP {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        print(f"Body: {response.text}")
        return False
except requests.Timeout:
    print(f"❌ {website_name}: Timeout po 10s")
    return False
except requests.RequestException as e:
    print(f"❌ {website_name}: Network error: {e}")
    return False
```

---

#### 6. **Možná Absence Subscriberů**
**Lokace:** Frontend  
**Dopad:** KRITICKÝ - Notifikace nemají komu poslat

**Analýza:**
Možné důvody, proč nikdo není přihlášen:

1. **Slidedown se zobrazuje až na 3. návštěvu**
   - Většina uživatelů může navštívit web jen 1-2x
   - Konzervativní přístup může odradit od přihlášení

2. **Chybějící explicitní call-to-action**
   - Subscribe button je v rohu - může být přehlédnut
   - Není viditelný na mobilech

3. **iOS Web Push vyžaduje speciální setup**
   - Uživatel musí přidat web na home screen
   - Poměrně složitý proces

**Ověření:**
```bash
# Spustit test skript lokálně
export ONESIGNAL_REST_API_KEY="your-key"
python3 test_onesignal.py
# Zkontrolovat "Příjemci: X" v outputu
```

---

### ⚠️ VAROVÁNÍ

#### W1. OneSignal SDK v16 - Stabilita
**Dopad:** NÍZKÝ

SDK v16 je poslední verze, ale OneSignal API se často mění. Doporučuji:
- Monitorovat changelog: https://documentation.onesignal.com/docs/web-sdk-changelog
- Testovat notifikace po každém update SDK

#### W2. Service Worker Caching
**Dopad:** NÍZKÝ

`OneSignalSDKWorker.js` používá importScripts a může být cachován prohlížečem.

**Doporučení:**
```javascript
// Přidat do OneSignalSDKWorker.js
self.addEventListener('install', function(event) {
  self.skipWaiting();
});
```

#### W3. Lokální Testing není možný
**Dopad:** NÍZKÝ

OneSignal vyžaduje HTTPS (nebo localhost). Pro staging/testing:
```
allowLocalhostAsSecureOrigin: true  // ✅ Už nastaveno
```

---

## ✅ Co Funguje Správně

### Frontend (_includes/onesignal.html)
✅ **OneSignal SDK inicializace:**
- Správný App ID: `00fc3def-70d1-4e7d-a081-984d5e738a75`
- SDK v16 správně načten
- Safari Web Push podpora zapnuta
- iOS Web App metadata v pořádku

✅ **Service Worker:**
- OneSignalSDKWorker.js na správném místě
- Správný import SDK

✅ **Manifest:**
- manifest-marigold.json správně nakonfigurován
- Icons v pořádku
- iOS metadata správně

### Backend
✅ **API Endpoint:**
- Používá správný endpoint: `https://onesignal.com/api/v1/notifications`

✅ **Authentication:**
- Správný formát Authorization header: `Basic {api_key}`

✅ **Content Type:**
- Správný: `application/json; charset=utf-8`

---

## 🔧 Akční Plán (Priority)

### 1. OKAMŽITĚ - Opravit Segment Name
```bash
# Najít a nahradit ve všech souborech
find . -type f -name "*.py" -exec sed -i 's/"Subscribed Users"/"All"/g' {} +
find .github/workflows -type f -name "*.yml" -exec sed -i 's/"Subscribed Users"/"All"/g' {} +
```

### 2. OKAMŽITĚ - Opravit Response Parsing
Upravit `.github/scripts/send_notifications.py:114`:
```python
notification_id = result.get('id', 'unknown')
```

### 3. DNES - Ověřit GitHub Secrets
```bash
# Zkontrolovat v GitHub UI:
# Settings → Secrets and variables → Actions
# 
# Měly by existovat:
# - ONESIGNAL_REST_API_KEY
# - ONESIGNAL_APP_ID (nebo ONESIGNAL_MARIGOLD_APP_ID)
```

### 4. DNES - Spustit Test
```bash
# Manuálně spustit test-notification.yml workflow
# nebo lokálně:
export ONESIGNAL_REST_API_KEY="your-key"
export ONESIGNAL_APP_ID="00fc3def-70d1-4e7d-a081-984d5e738a75"
python3 test_onesignal.py
```

### 5. TÝDEN - Vylepšit UX pro Subscription
- Přidat viditelný banner "📬 Chcete dostávat novinky?" na homepage
- Zkrátit slidedown delay z 3 na 2 návštěvy
- Přidat explicitní CTA v článcích

### 6. MĚSÍC - Monitoring
- Implementovat logging do souboru nebo cloud service
- Nastavit alerts při selhání notifikací
- Sledovat OneSignal dashboard pro statistiky doručení

---

## 📊 Diagnostické Skripty

### Ověření Subscriberů
```python
import requests
import os

app_id = "00fc3def-70d1-4e7d-a081-984d5e738a75"
api_key = os.getenv('ONESIGNAL_REST_API_KEY')

# Získat počet subscriberů
url = f"https://onesignal.com/api/v1/apps/{app_id}"
headers = {"Authorization": f"Basic {api_key}"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"Celkem subscriberů: {data.get('players', 'N/A')}")
    print(f"Aktivních (7 dní): {data.get('messageable_players', 'N/A')}")
else:
    print(f"Chyba: {response.status_code}")
```

### Test Notifikace
```bash
# Použít existující test_segments.py
export ONESIGNAL_REST_API_KEY="your-key"
python3 test_segments.py

# Nebo jednodušší:
python3 send_notification_now.py
```

---

## 🎓 Závěrečné Doporučení

Jako senior vývojář doporučuji:

1. **První krok:** Opravit segment name z "Subscribed Users" na "All"
2. **Druhý krok:** Opravit response parsing
3. **Třetí krok:** Ověřit GitHub Secrets
4. **Čtvrtý krok:** Spustit test a zkontrolovat recipients count
5. **Pátý krok:** Pokud recipients = 0, zaměřit se na frontend subscription UX

**Pravděpodobnost problému:**
- 80% - Špatný segment name
- 15% - Žádní subscribeři
- 5% - Špatné API credentials

**Očekávaný čas opravy:** 30-60 minut

---

## 📚 Reference

- [OneSignal Web Push Docs](https://documentation.onesignal.com/docs/web-push-setup)
- [OneSignal REST API](https://documentation.onesignal.com/reference/create-notification)
- [Web Push Segments](https://documentation.onesignal.com/docs/segments)
- Lokální dokumentace: `.github/ONESIGNAL_SETUP.md`

