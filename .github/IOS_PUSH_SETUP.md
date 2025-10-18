# iOS Web Push Setup pro vibecoding.cz

Komplexní průvodce aktivací push notifikací na iOS a iPadOS zařízeních pro web app přidaný na home screen.

## Přehled

Apple přidal podporu web push notifikací v iOS/iPadOS 16.4+ pro webové aplikace přidané na home screen uživatele. Tato funkce funguje přes Safari, Chrome a Edge prohlížeče a otevírá nové možnosti pro engagement s uživateli.

**Důležité**: Na rozdíl od desktopových prohlížečů, iOS vyžaduje, aby byl web přidán jako web app na home screen. Běžné browsování v Safari notifikace nepodporuje.

## Systémové požadavky

- **iOS/iPadOS 16.4 nebo vyšší**
- **HTTPS** - vibecoding.cz běží na HTTPS ✅
- **Web Application Manifest** - `manifest.json` ✅
- **Service Worker** - OneSignal SDK ✅
- **Responzivní design** ✅

## Jak funguje iOS web push

### Architektura

Web push na iOS funguje následovně:

1. Uživatel navštíví vibecoding.cz na Safari, Chrome nebo Edge
2. Uživatel klikne na **Sdílení** a vybere **Přidat na home screen**
3. Web app se uloží na home screen
4. Uživatel otevře app z home screenu (nikoliv z prohlížeče!)
5. App zaregistruje Service Worker a OneSignal SDK
6. Uživatel klikne na tlačítko "Odebírat aktuality"
7. Objeví se nativní iOS prompt pro povolení notifikací
8. Po schválení bude uživatel dostávat notifikace

### Klíčový rozdíl oproti ostatním zařízením

Na desktopech (Windows, macOS, Linux) se permission prompt objevuje automaticky na základě OneSignal nastavení.

Na iOS **musí být uživatel v rámci web appu** přidaného na home screen a **musí sám iniciovat** permission prompt kliknutím na naše tlačítko.

## Krok za krokem pro uživatele

Níže je návod, který by měl vidět uživatel na vibecoding.cz.

### Krok 1: Otevři web na iOS

- Jdi na **https://www.vibecoding.cz/**
- Používej Safari, Chrome nebo Edge
- Měla by to být nejnovější verze (iOS 16.4+)

<img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='400'%3E%3Crect fill='%23f0f0f0' width='200' height='400'/%3E%3Ctext x='100' y='200' text-anchor='middle' font-size='14' fill='%23999'%3EiPhone screen: vibecoding.cz otevřeno%3C/text%3E%3C/svg%3E" alt="iPhone screen">

### Krok 2: Klikni na Sdílení (Share)

- Najdi ikonu **Sdílení** v dolní lišté (vypadá jako obdélník se šipkou)
- Na Androidu je to obdélník s šipkou nahoru
- Klikni na ni

<img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='100'%3E%3Crect fill='%23f0f0f0' width='200' height='100'/%3E%3Ctext x='100' y='50' text-anchor='middle' font-size='12' fill='%23999'%3ESdílení menu%3C/text%3E%3C/svg%3E" alt="Share menu">

### Krok 3: Vyberi "Přidat na home screen"

V menu, které se objeví, hledej možnost:
- **"Přidat na home screen"** (Safari/Chrome)
- Nebo **"Instalovat"** (Edge)

Posuň si menu dolů, pokud je skrytá.

<img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Crect fill='%23f0f0f0' width='200' height='200'/%3E%3Ctext x='100' y='100' text-anchor='middle' font-size='12' fill='%23999'%3E%22Přidat na home screen%22%3C/text%3E%3C/svg%3E" alt="Add to Home Screen option">

### Krok 4: Potvrď název a přidej

Aplikace se zeptá na název. Ponech **"Vibecoding"** nebo zadej vlastní.

Klikni **Přidat** nebo **OK**.

App se nyní zobrazí na home screenu.

### Krok 5: Otevři app z home screenu

**DŮLEŽITÉ!** Musíš app otevřít z home screenu, ne z prohlížeče!

- Najdi ikonu **Vibecoding** na home screenu
- Klikni na ni
- App se otevře v full-screen režimu (bez prohlížečové lišty nahoře)

App se bude chovat jako nativní aplikace, nikoliv jako web v prohlížeči.

### Krok 6: Přihlas se k odběru notifikací

Když je app otevřena z home screenu:

- Měl by se zobrazit **modrý button "Odebírat aktuality"** v dolním pravém rohu
- Klikni na něj
- Na 3. návštěvě se může zobrazit i **slidedown prompt** s otázkou

### Krok 7: Schvál notifikace

Když klikneš na subscribe button, iOS se tě zeptá:

**"Chcete dovolit vibecoding.cz posílat vám notifikace?"**

- Klikni **"Povolit"** (Allow)
- V iOS nastavení se objeví notifikace jako povolená pro tuto web app

### Hotovo! ✅

Nyní budeš dostávat notifikace o nových AI nástrojích na vibecoding.cz.

Notifikace se budou zobrazovat v:
- **Notification Center** (tažení dolů z horní lišty)
- **Lock Screenu** (když je phone zamčený)
- **Na home screenu** (badge s počtem)

## Troubleshooting

### Tlačítko "Přidat na home screen" nevidím

- Používáš Safari, Chrome nebo Edge?
- Je tvůj iOS aspoň 16.4?
- Je webová stránka přístupná přes HTTPS? (vibecoding.cz je ✅)
- Zkus otevřít v Safarim (má nejlepší podporu)

### Povolení se nezobrazuje

**Nejčastější problém:** Jsi v prohlížeči, ne v web appu!

- Ujisti se, že používáš app z home screenu
- App se musí otevřít v **standalone režimu** (bez prohlížečové lišty)
- Na home screenu by měla být ikona s názvem "Vibecoding"

Pokud jsi app smazal(a) z home screenu a přidáš ji znovu:
- Jdi do Nastavení → Safari/Chrome/Edge → Vymaž cache
- Smaž app z home screenu
- Přidej ji znovu

### Notifikace se neposílají

1. Zkontroluj, že máš notifikace povolené:
   - Nastavení → Vibecoding (v sekci Aplikace)
   - Ujisti se, že jsou zapnuty

2. Zkontroluj OneSignal audience:
   - Jdi na https://onesignal.com/
   - Otevři vibecoding projekt
   - Zkontroluj, že máš abonenty v Audience sekci

3. Zkontroluj server:
   - Jsou notifikace opravdu poslány?
   - Zkontroluj OneSignal Activity log

### Permission je "denied" a nemohu se odhlásit

Pokud si omylem klikneš "Nepovolit":

1. Smaž app z home screenu
2. Vymaž cache: Nastavení → Safari/Chrome/Edge → Vymaž cache
3. Přidej app znovu
4. Tentokrát vyber "Povolit"

## Pro správce - interní implementace

### Manifest.json

Soubor `/manifest.json` obsahuje:
- Název a popis aplikace
- Icons pro různé velikosti (192x192, 256x256, 384x384, 512x512)
- Display mode: `"standalone"` - nutné pro iOS
- Theme color a background color
- Scope a start_url

```json
{
  "name": "Vibecoding - AI nástroje pro programování",
  "short_name": "Vibecoding",
  "display": "standalone",
  "start_url": "/",
  "icons": [...]
}
```

### OneSignal nastavení

OneSignal je konfigurován v `_includes/onesignal-vibecoding.html`:

```javascript
const config = {
  appId: "0c413930-f7f6-4d73-9438-36ec057acb7d",
  notifyButton: {
    enable: true,
    position: "bottom-right",
    size: "medium",
    text: {
      "button.subscribe": "Odebírat aktuality",
      "button.unsubscribe": "Již neodebírat",
    },
  }
};
```

### iOS Meta Tags

V `_layouts/vibecoding-default.html` jsou přidány:

```html
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Vibecoding">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

Tyto meta tagy říkají iOS, že:
- Aplikace je schopná běhat jako web app
- Status bar má mít černý vzhled
- Název v home screenu je "Vibecoding"
- Viewport by měl pokrýt i notch/safe areas

### Service Worker

OneSignal SDK automaticky registruje Service Worker ze svého CDN na `/OneSignalSDKWorker.js`.

Při prvním přidání na home screen iOS si ho stáhne a zaregistruje.

## Testování

### Na fyzickém iOS zařízení

1. Otevři https://www.vibecoding.cz/ na Safari/Chrome/Edge
2. Klikni Sdílení → Přidat na home screen
3. Ulož app
4. Otevři app z home screenu
5. Klikni "Odebírat aktuality"
6. Schvál notifikace
7. Zkontroluj OneSignal dashboard - měl bys vidět nového subscribenta

### V Chrome DevTools (simulace)

```javascript
// V DevTools Console můžeš zkontrolovat:
window.OneSignal
// Vrátí objekt OneSignal API

OneSignal.Notifications.permission
// Vrátí "granted", "denied", nebo "default"
```

## Odesílání notifikací pro iOS

### Via OneSignal Dashboard

1. Jdi na https://onesignal.com/
2. Otevři vibecoding projekt
3. Klikni **Messages** → **New Push**
4. Vyplň:
   - **Heading (CS)**: "Vibecoding - novinka"
   - **Message (CS)**: "Nový AI nástroj pro programování!"
   - **Message Action URL**: `https://www.vibecoding.cz/cursor/`
5. V **Targeting** vyber **"All Subscribers"** nebo konkrétní segment
6. Klikni **Send**

iOS uživatelé tuto notifikaci dostanou na svou home screen app!

### Via REST API

```bash
curl -X POST https://onesignal.com/api/v1/notifications \
  -H "Authorization: Basic YOUR_REST_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "app_id": "0c413930-f7f6-4d73-9438-36ec057acb7d",
    "included_segments": ["All"],
    "contents": {"cs": "Nový AI nástroj pro programování"},
    "headings": {"cs": "Vibecoding - novinka"},
    "url": "https://www.vibecoding.cz/"
  }'
```

## Poznámky pro 2025

- **Spolehlivost**: Někteří vývojáři hlásí občasné problémy, kdy notifikace fungují začátku, ale pak se zastaví. Monitoruj delivery rate.
- **Cross-browser**: Notifikace nyní fungují v Safari, Chrome a Edge - vynikající pokrytí
- **Fallback strategie**: Měj připravenou alternativní komunikaci (email, feed) na případy, kdy notifikace nefungují

## FAQ

**Q: Budou notifikace fungovat v běžném Safari browseru (ne jako web app)?**
A: Ne, iOS to nepodporuje. Web app musí být přidána na home screen.

**Q: A co Android?**
A: Android podporuje web push v Chromu normálně bez přidání na home screen. Permission prompt se zobrazí při prvé návštěvě.

**Q: Budou notifikace přijaté více iOS zařízeními toho samého uživatele?**
A: Ano, pokud si uživatel přidá web app na víc iOS zařízení (iPhone + iPad), budou dostávat notifikace na obou - každé zařízení má vlastní subscription.

**Q: Co když uživatel web app smaže?**
A: Unsubscribne se automaticky. Notifikace se mu nebudou posílat.

**Q: Fungují notifikace i v Chromu na iOS?**
A: Ano, Chrome na iOS od verze XYZ podporuje web push stejně jako Safari.

## Důležité odkazy

- [OneSignal iOS Setup](https://documentation.onesignal.com/docs/ios-push-setup) - Nativní iOS app notifikace
- [Web Push iOS Setup](https://documentation.onesignal.com/docs/ios-web-push-setup) - Web push na iOS
- [Web.dev - Web App Manifest](https://web.dev/add-manifest/)
- [MDN - Web App Manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest)
- [Safari dokumentace](https://developer.apple.com/safari/resources/)
