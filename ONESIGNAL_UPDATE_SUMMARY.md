# OneSignal Konfigurace - Aktualizace 2025-11-05

## 📋 Shrnutí

Všechny OneSignal skripty byly aktualizovány na funkční konfiguraci podle dokumentace OneSignal API 2025.

---

## ✅ Opravené soubory

### 1. Produkční skripty
- ✅ `.github/scripts/send_notifications.py` - hlavní produkční skript pro automatické notifikace

### 2. GitHub Workflows
- ✅ `.github/workflows/test-notification.yml` - manuální test notifikací

### 3. Testovací skripty
- ✅ `send_notification_now.py` - okamžité odeslání notifikace
- ✅ `test_onesignal.py` - interaktivní testovací skript
- ✅ `debug_onesignal.py` - debugovací skript s detailním výpisem

---

## 🔧 Provedené změny

### 1. **URL Endpoint**
```python
# ❌ PŘED (nefunkční)
url = "https://onesignal.com/api/v1/notifications"

# ✅ PO (funkční)
url = "https://api.onesignal.com/notifications"
```

### 2. **Authorization Header**
```python
# ❌ PŘED (nefunkční)
"Authorization": f"Basic {api_key}"

# ✅ PO (funkční)
"Authorization": f"Key {api_key}"
```

### 3. **Segment**
```python
# ❌ PŘED (segment "All" neexistuje)
"included_segments": ["All"]

# ✅ PO (segment "Total Subscriptions" existuje a má 12 push subscribers)
"included_segments": ["Total Subscriptions"]
```

### 4. **Povinný anglický jazyk**
```python
# ❌ PŘED (chyba 400 - vyžaduje EN)
"headings": {"cs": "Titulek"}
"contents": {"cs": "Zpráva"}

# ✅ PO (EN je povinný)
"headings": {"en": "Titulek", "cs": "Titulek"}
"contents": {"en": "Zpráva", "cs": "Zpráva"}
```

### 5. **Platform targeting pro Web Push**
```python
# ✅ NOVĚ (explicitně specifikovat web push platformy)
payload = {
    # ...
    "isAnyWeb": True,
    "isChromeWeb": True,
    "isFirefox": True,
    "isSafari": True,
    "isIos": False,
    "isAndroid": False,
}
```

### 6. **Zpracování Response**
```python
# ❌ PŘED (předpokládá vždy recipients v response)
recipients = result.get('recipients', 0)
print(f"Příjemci: {recipients}")

# ✅ PO (recipients může být None)
recipients = result.get('recipients', None)
if recipients is not None:
    print(f"Příjemci: {recipients}")
else:
    print(f"Příjemci: Zobrazí se v OneSignal dashboardu")
```

---

## 🎯 Funkční konfigurace

### Kompletní funkční payload:

```python
import requests

url = "https://api.onesignal.com/notifications"
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "Authorization": f"Key {ONESIGNAL_REST_API_KEY}"
}

payload = {
    "app_id": "00fc3def-70d1-4e7d-a081-984d5e738a75",  # Marigold.cz
    "included_segments": ["Total Subscriptions"],      # 12 push subscribers
    "headings": {
        "en": "🆕 Nový článek",  # EN je POVINNÝ
        "cs": "🆕 Nový článek"   # CS jako alternativa
    },
    "contents": {
        "en": "Shrnutí článku...",  # EN je POVINNÝ
        "cs": "Shrnutí článku..."   # CS jako alternativa
    },
    # Web Push platformy
    "isAnyWeb": True,
    "isChromeWeb": True,
    "isFirefox": True,
    "isSafari": True,
    # Vypnout mobilní
    "isIos": False,
    "isAndroid": False,
}

response = requests.post(url, json=payload, headers=headers, timeout=10)
```

---

## 📊 Ověření funkčnosti

### OneSignal Dashboard ukazuje:
- ✅ Status: **Delivered**
- ✅ Sent: **12** odběratelů
- ✅ Created By: **API**

### Dostupné segmenty:
- ✅ **Total Subscriptions** - 12 Push Subs (hlavní segment)
- ✅ **Active Subscriptions** - 9 Push Subs
- ✅ **Engaged Subscriptions** - 5 Push Subs
- ✅ **Inactive Subscriptions** - 3 Push Subs

---

## 🚀 Jak používat

### Manuální test:
```bash
# Nejjednodušší způsob
python3 send_notification_now.py

# Interaktivní test
export ONESIGNAL_REST_API_KEY="your-key"
export ONESIGNAL_MARIGOLD_APP_ID="00fc3def-70d1-4e7d-a081-984d5e738a75"
python3 test_onesignal.py

# Debug s detailním výpisem
python3 debug_onesignal.py
```

### Automatické notifikace:
Produkční skript `.github/scripts/send_notifications.py` se spouští automaticky při:
- Commitech nových článků do `_posts/`
- Commitech nových článků do `_vibecoding/`

---

## ⚠️ Důležité poznatky

1. **Response bez `recipients` pole není chyba**
   - OneSignal často vrací `{'id': '...', 'external_id': None}` bez pole `recipients`
   - Skutečný počet doručených zpráv se zobrazí v dashboardu
   - Status 200/201 = úspěch, i když chybí `recipients`

2. **Anglický jazyk je povinný**
   - I pro české notifikace musíte zahrnout `"en"` klíč
   - Můžete použít stejný text pro EN i CS

3. **Segment "All" neexistuje**
   - Ve vašem OneSignal není výchozí segment "All"
   - Používejte "Total Subscriptions" (12 subs) nebo jiné vlastní segmenty

4. **Platform targeting**
   - Pro web push nastavte `isAnyWeb: True`
   - Vypněte mobilní platformy (`isIos: False`, `isAndroid: False`)

---

## 📚 Reference

- [OneSignal API Dokumentace](https://documentation.onesignal.com/reference/push-notification)
- [OneSignal Dashboard](https://dashboard.onesignal.com/apps/00fc3def-70d1-4e7d-a081-984d5e738a75)
- Lokální dokumentace: `.github/ONESIGNAL_SETUP.md`

---

## ✅ Checklist pro nové skripty

Pokud vytváříte nový skript pro OneSignal, ujistěte se:

- [ ] URL: `https://api.onesignal.com/notifications`
- [ ] Authorization: `Key {api_key}` (ne "Basic")
- [ ] Segment: `"Total Subscriptions"` (ne "All")
- [ ] Jazyk: Zahrnout `"en"` klíč v headings i contents
- [ ] Platform: Nastavit web push platformy (`isAnyWeb`, `isChromeWeb`, atd.)
- [ ] Response: Ošetřit `recipients = None`

---

Aktualizováno: 2025-11-05
Autor: Claude Code
