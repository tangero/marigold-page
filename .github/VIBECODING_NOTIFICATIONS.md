# OneSignal Setup pro vibecoding.cz

Průvodce krok za krokem pro aktivaci push notifikací na vibecoding.cz.

## Quick Start

### Krok 1: Vytvořit OneSignal projekt pro vibecoding.cz

1. Jít na https://onesignal.com/
2. Přihlásit se s účtem, který vlastní projekt marigold.cz
3. Kliknout "Create a new app"
4. Vyplnit:
   - **App Name**: "Vibecoding.cz Notifications"
   - **App Icon**: Použít stejný jako marigold.cz
5. V kroku "Choose a platform" vybrat **"Web Push"**
6. V kroku "Website Setup" vyplnit:
   - **Website Name**: "Vibecoding"
   - **Website URL**: `https://www.vibecoding.cz`
   - **Default Notification Title**: "Vibecoding"
   - **Default Notification Icon**: Použít vibecoding logo
   - **Default Action URL**: `https://www.vibecoding.cz`

### Krok 2: Zkopírovat App ID

1. V OneSignal dashboardu pro vibecoding.cz:
   - Jít na **Settings** → **Keys & IDs**
   - Zkopírovat **App ID** (vypadá jako: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`)

### Krok 3: Přidat GitHub Secret

1. Jít na https://github.com/tangero/marigold-page
2. Settings → Secrets and variables → Actions
3. Kliknout **New repository secret**
4. Vyplnit:
   ```
   Name: ONESIGNAL_VIBECODING_APP_ID
   Value: [zkopírovaný App ID]
   ```
5. Kliknout **Add secret**

### Krok 4: Nahrát Service Worker (volitelné, ale doporučeno)

OneSignal vyžaduje service worker na `https://www.vibecoding.cz/OneSignalSDKWorker.js`

Máte dvě možnosti:

**Možnost A: Ruční nahrání (Cloudflare Pages)**
1. Soubor `/OneSignalSDKWorker.js` v repo kořenu
2. Obsah souboru:
   ```javascript
   importScripts('https://cdn.onesignal.com/sdks/web/v16/OneSignalSDK.sw.js');
   ```
3. Git push → Cloudflare Pages automaticky deployuje

**Možnost B: Automatické (OneSignal CORS nastavení)**
1. V OneSignal → Settings → Web Push
2. Kliknout "Enable HTTPS Web Push Delivery"
3. OneSignal si postará o service worker

### Krok 5: Ověřit doménu v OneSignal

1. V OneSignal dashboardu → Settings → Web Push
2. Najít **"Add Domain"**
3. Kliknout a vybrat: `www.vibecoding.cz`
4. OneSignal pošle ověřovací soubor
5. Soubor bude v `/.well-known/onesignal/` (Cloudflare to řeší automaticky)

### Krok 6: Redeploy

```bash
git pull
git add .
git commit -m "Enable OneSignal notifications for vibecoding.cz"
git push origin main
```

Cloudflare Pages se automaticky rebuilduje s novým App ID.

### Krok 7: Ověřit

1. Jít na https://www.vibecoding.cz/
2. Otevřít DevTools (F12) → Console
3. Měly by se zobrazit:
   ```
   [OneSignal-Vibecoding] Script starting...
   [OneSignal-Vibecoding] Initializing OneSignal SDK for vibecoding.cz
   [OneSignal-Vibecoding] Initialization complete
   [OneSignal-Vibecoding] Page visit count: 1
   ```
4. Měl by se zobrazit subscribe button v dolním rohu
5. Na 3. návštěvu se zobrazí slidedown prompt

## Odesílání Notifikací

### Via OneSignal Dashboard

Nejsnazší způsob:

1. OneSignal dashboard → **Messages** → **New Push**
2. Vyplnit:
   - **Heading (CS)**: "Nový obsah na Vibecoding!"
   - **Message (CS)**: "Podívej se na nový AI nástroj pro programování"
   - **Message Action URL**: Cílový link
3. Pod "Targeting": Vybrat **"All Users"**
4. Kliknout **Send**

### Via REST API

Pokud chceš automatizovat odesílání (např. při přidání nového nástroje):

```bash
curl -X POST https://onesignal.com/api/v1/notifications \
  -H "Authorization: Basic $ONESIGNAL_REST_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "app_id": "YOUR_APP_ID",
    "included_segments": ["All"],
    "contents": {
      "cs": "Nový tutoriál: Jak používat Claude Code"
    },
    "headings": {
      "cs": "Vibecoding - nový tutoriál"
    },
    "url": "https://www.vibecoding.cz/claude-code/"
  }'
```

### Via GitHub Actions Workflow

Pokud chceš automatické notifikace při přidání nového obsahu do vibecoding:

Vytvor nový workflow `.github/workflows/vibecoding-notify.yml`:

```yaml
name: Send Vibecoding Notification
on:
  push:
    paths:
      - '_vibecoding/**'
jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Send OneSignal Notification
        run: |
          curl -X POST https://onesignal.com/api/v1/notifications \
            -H "Authorization: Basic ${{ secrets.ONESIGNAL_REST_API_KEY }}" \
            -H "Content-Type: application/json" \
            -d '{
              "app_id": "${{ secrets.ONESIGNAL_VIBECODING_APP_ID }}",
              "included_segments": ["All"],
              "contents": {
                "cs": "Nový obsah na Vibecoding!"
              },
              "headings": {
                "cs": "Vibecoding - aktualizace"
              },
              "url": "https://www.vibecoding.cz/"
            }'
```

## Obsah OneSignal Include

Soubor `_includes/onesignal-vibecoding.html` obsahuje:

- **SDK inicializace** - Načítá OneSignal SDK z CDN
- **App ID** - Načítá z `site.onesignal_vibecoding_app_id`
- **Subscribe button** - "Odebírat aktuality" v dolním rohu
- **Slidedown prompt** - Zobrazí se na 3. návštěvu
- **Lokální tracking** - Počítá návštěvy v localStorage
- **Czech UI** - Všechny texty v češtině

## Troubleshooting

### "OneSignal nedejá se inicializovat"

```javascript
// V DevTools Console zkus:
window.OneSignal
// Měl by vrátit objekt
```

Pokud vrátí `undefined`:
- Zkontrolovat, že App ID je správný v `_config_vibecoding.yml`
- Zkontrolovat síťové chyby v Network tab
- Ověřit HTTPS (OneSignal vyžaduje)

### "Service Worker error"

OneSignal si automaticky postará o Service Worker. Pokud máš problém:

1. Ověřit, že `/OneSignalSDKWorker.js` existuje a je dostupný
2. Zkontrolovat Cloudflare Pages → Deployments → Worker logs
3. Obnovit Cloudflare Pages cache (Purge Cache button)

### "Notifikace se neposílají"

1. Ověřit v OneSignal → Activity log
2. Zkontrolovat, že `ONESIGNAL_REST_API_KEY` je správný
3. Zkontrolovat, že `ONESIGNAL_VIBECODING_APP_ID` je správný
4. Ověřit, že jsou uživatelé subscribnutí (Audience tab)

### "Slidedown se nezobrazuje"

```javascript
// V DevTools Console:
localStorage.removeItem('onesignal_vibecoding_visit_count')
// Obnovit stránku 3x a na 3. návštěvu by se měl slidedown zobrazit
```

## Costs

OneSignal má free tier pro do 30,000 notifikací/měsíc, což je dostatek pro vibecoding.cz.

Pokud se přiblížíš limitu, můžeš upgradovat na paid plan.

## FAQ

**Q: Bude vibecoding.cz brát notifikace stejně jako marigold.cz?**
A: Ne, každá doména má svůj OneSignal projekt s vlastním App ID. Uživatelé si budou muset subscribnout zvlášť pro vibecoding.cz.

**Q: Mohu sdílet seznam subscribentů mezi marigold.cz a vibecoding.cz?**
A: Technicky ano, ale OneSignal to nedoporučuje. Lépe udržovat oddělené projekty.

**Q: Co se stane, když vibecoding.cz zmizí/přejede?**
A: OneSignal projekt zůstane, ale notifikace se nebudou posílat. Projekt lze smazat v OneSignal dashboardu.

**Q: Jak trackuji statistiky notifikací?**
A: OneSignal dashboard → Analytics. Vidíš delivery rate, click rate, conversions, atd.
