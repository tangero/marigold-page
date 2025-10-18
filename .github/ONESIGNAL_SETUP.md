# OneSignal Setup Guide

## Přehled

OneSignal push notifikace jsou v tomto repozitáři integrované na dvou místech:

1. **marigold.cz** - Push notifikace pro nové články
2. **vibecoding.cz** - Push notifikace pro nové AI nástroje a tutoriály

## Konfigurace

### 1. Marigold.cz (Hlavní web)

**Soubory:**
- `_includes/onesignal.html` - OneSignal SDK inicializace
- `_layouts/default.html` - Zahrnutí OneSignal (line 30)
- `.github/scripts/send_onesignal_notification.py` - Odesílání notifikací na nové články
- `manifest-marigold.json` - Web app manifest pro iOS
- `.github/IOS_PUSH_SETUP.md` - iOS setup průvodce

**App ID:**
```
00fc3def-70d1-4e7d-a081-984d5e738a75
```

**Safari Web ID:**
```
web.onesignal.auto.0e731bf1-0f8d-4c8c-8593-03e4c907000a
```

**Service Worker:**
- `OneSignalSDKWorker.js` v kořenovém adresáři

**Platform Support:**
- ✅ Desktop (Chrome, Firefox, Safari, Edge)
- ✅ Android (Chrome, Firefox, Edge)
- ✅ iOS/iPadOS 16.4+ (Safari, Chrome, Edge - vyžaduje web app na home screen)

**Features:**
- Subscribe button v dolním rohu
- Slidedown prompt na 3. návštěvu
- Automatické notifikace při nových příspěvcích (via GitHub Actions)
- Sledování počtu návštěv přes localStorage
- iOS web app podpora s manifest.json

---

### 2. Vibecoding.cz (Separátní web)

**Soubory:**
- `_includes/onesignal-vibecoding.html` - OneSignal SDK inicializace
- `_layouts/vibecoding-default.html` - Zahrnutí OneSignal
- `_config_vibecoding.yml` - Konfigurace App ID
- `manifest.json` - Web app manifest pro iOS
- `.github/IOS_PUSH_SETUP.md` - Detailní iOS setup průvodce

**App ID:**
```
0c413930-f7f6-4d73-9438-36ec057acb7d
```

**Platform Support:**
- ✅ Desktop (Chrome, Firefox, Safari, Edge)
- ✅ Android (Chrome, Firefox, Edge)
- ✅ iOS/iPadOS 16.4+ (Safari, Chrome, Edge - vyžaduje web app na home screen)

**Aktivace:**

Aby vibecoding.cz měl push notifikace, je třeba:

1. **Vytvořit nový OneSignal projekt** pro vibecoding.cz:
   - Jít na https://onesignal.com/
   - Kliknout "Create a new app"
   - Nastavit doménu: `www.vibecoding.cz`
   - Zkopírovat App ID

2. **Uložit App ID jako GitHub Secret:**
   ```
   Settings → Secrets and variables → Actions
   New repository secret:
   Name: ONESIGNAL_VIBECODING_APP_ID
   Value: [zkopírovaný App ID z OneSignal]
   ```

3. **Přidat Service Worker** pro vibecoding (opakovat pro Safari):
   - Nahrát `OneSignalSDKWorker.js` na vibecoding.cz (Cloudflare Pages root)
   - Nebo: Nakonfigurovat v OneSignal dashboardu

4. **Ověřit doménu** v OneSignal:
   - OneSignal → Settings → Web Push
   - Add domain: `www.vibecoding.cz`

5. **Redeploy:**
   ```bash
   git push origin main
   # Cloudflare Pages automaticky builduje s novým App ID
   ```

---

## Odesílání Notifikací

### Marigold.cz

Notifikace se odesílají **automaticky** když je nový článek publikován.

**Workflow:** `.github/workflows/generate_podcast.yml`
- Trigger: Push do `_posts/**.md`
- Skript: `.github/scripts/send_onesignal_notification.py`

**Manuální odeslání:**
```bash
python .github/scripts/send_onesignal_notification.py \
  --app-id "00fc3def-70d1-4e7d-a081-984d5e738a75" \
  --rest-api-key "YOUR_REST_API_KEY"
```

### Vibecoding.cz

Notifikace lze odesílat:

1. **Přes OneSignal Dashboard** - Kliknout "Send a message"
2. **Přes REST API** - Vytvořit nový skript (viz příklad níže)
3. **Automaticky** - Přidat trigger do GitHub Actions workflow

**Příklad REST API:**
```bash
curl -X POST \
  https://onesignal.com/api/v1/notifications \
  --header "Authorization: Basic YOUR_REST_API_KEY" \
  --header "Content-Type: application/json; charset=utf-8" \
  --data-raw '{
    "app_id": "YOUR_APP_ID",
    "included_segments": ["All"],
    "contents": {
      "cs": "Nový nástroj: AI Editor pro kód"
    },
    "headings": {
      "cs": "Vibecoding - nová aktualizace"
    },
    "url": "https://www.vibecoding.cz/"
  }'
```

---

## Testování

### Local Testing

1. **Marigold.cz:**
   ```bash
   # Build lokálně
   bundle exec jekyll serve --config _config.yml
   # Vstoupit na http://localhost:4000
   # OneSignal by měl být inicializován (check DevTools Console)
   ```

2. **Vibecoding.cz:**
   ```bash
   # Build lokálně
   bundle exec jekyll serve --config _config_vibecoding.yml
   # Vstoupit na http://localhost:4000
   # OneSignal by měl být inicializován s vibecoding App ID
   ```

### Production Testing

1. Jít na https://www.marigold.cz/ nebo https://www.vibecoding.cz/
2. Otevřít DevTools → Console
3. Měl by se zobrazit `[OneSignal] Initializing OneSignal SDK`
4. Měl by se zobrazit subscribe button v dolním rohu
5. Na 3. návštěvu by se měl zobrazit slidedown prompt

---

## Environment Variables

**GitHub Actions Secrets (Settings → Secrets and variables):**

```
ONESIGNAL_REST_API_KEY         - API klíč pro odesílání notifikací
ONESIGNAL_APP_ID               - App ID pro marigold.cz
ONESIGNAL_VIBECODING_APP_ID    - App ID pro vibecoding.cz (pokud je aktivní)
```

---

## Troubleshooting

### OneSignal se nenačítá

1. Zkontrolovat DevTools Console → Network tab
2. Ověřit, že App ID je správný
3. Ověřit HTTPS (OneSignal vyžaduje HTTPS)
4. Ověřit, že Service Worker je dostupný na `/OneSignalSDKWorker.js`

### Notifikace se neposílají

1. Zkontrolovat, že REST API Key je správný
2. Ověřit, že App ID je správný
3. Zkontrolovat OneSignal dashboard → Activity log pro chyby
4. Ověřit, že uživatel má push notifikace povoleny

### Slidedown se nezobrazuje

1. Vyčistit localStorage: `localStorage.clear()`
2. Obnovit stránku 3x (počítač od 1)
3. Na 3. návštěvu by se měl slidedown zobrazit

---

---

## iOS Web Push Setup

Pro iOS/iPadOS 16.4+ je potřeba speciální konfigurace. Kompletní průvodce je v `.github/IOS_PUSH_SETUP.md`.

**Klíčové body:**
- iOS vyžaduje web app přidanou na home screen
- Manifest.json musí být správně nastaven
- Permission prompt se zobrazí jen po kliknutí na subscribe button v rámci web appu
- Funguje v Safari, Chrome a Edge prohlížečích

**Pro uživatele:**
1. Jdi na vibecoding.cz
2. Klikni Sdílení → Přidat na home screen
3. Otevři app z home screenu
4. Klikni "Odebírat aktuality"
5. Schvál notifikace

**Implementace v kódu:**
- `manifest.json` - Web app manifest s icons a nastavením
- iOS meta tagy v `_layouts/vibecoding-default.html`
- OneSignal SDK konfigurace v `_includes/onesignal-vibecoding.html`

---

---

## Poznámky pro marigold.cz

Marigold.cz má stejnou iOS konfiguraci jako vibecoding.cz:
- Web app manifest: `manifest-marigold.json`
- iOS meta tagy v `_layouts/default.html`
- OneSignal SDK s iOS supportem

Uživatelé marigold.cz mohou stejně jako u vibecoding.cz přidat web na home screen a dostávat notifikace o nových článcích.

---

## Další Resourcy

- [OneSignal Documentation](https://documentation.onesignal.com/)
- [Web Push Setup](https://documentation.onesignal.com/docs/web-push-setup)
- [iOS Web Push Setup](https://documentation.onesignal.com/docs/ios-web-push-setup)
- [REST API Reference](https://documentation.onesignal.com/reference)
- [Web App Manifest - MDN](https://developer.mozilla.org/en-US/docs/Web/Manifest)
