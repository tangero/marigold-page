# Bridgy Fed - Propojení Marigold.cz a Vibecoding.cz do Fediverse

## Přehled

Tento dokument popisuje nastavení automatického publikování článků z Marigold.cz a Vibecoding.cz do fediverse (Mastodon) a Bluesky přes službu Bridgy Fed.

## Stav konfigurace

### RSS Feedy

**Marigold.cz:**
- ✅ Český RSS feed: `https://www.marigold.cz/feed.xml`
- ✅ Anglický RSS feed: `https://www.marigold.cz/feed-en.xml`
- ✅ Jekyll-feed plugin nakonfigurován
- ✅ Feed obsahuje 20 nejnovějších článků s excerptem
- ✅ Feed je discoverable z homepage (link rel="alternate" v HTML hlavičce)

**Vibecoding.cz:**
- ✅ RSS feed: `https://www.vibecoding.cz/vibecoding-feed.xml`
- ✅ Vlastní feed template
- ✅ Feed obsahuje články o AI nástrojích pro programování

## Aktivace Bridgy Fed

### Metoda 1: Webové rozhraní (doporučeno)

1. **Pro Marigold.cz:**
   - Otevřete https://fed.brid.gy/
   - Do pole zadejte: `marigold.cz` nebo `https://www.marigold.cz`
   - Klikněte na tlačítko "Go" nebo "Bridge"
   - Bridgy Fed automaticky najde váš RSS feed a začne ho sledovat

2. **Pro Vibecoding.cz:**
   - Otevřete https://fed.brid.gy/
   - Do pole zadejte: `vibecoding.cz` nebo `https://www.vibecoding.cz`
   - Klikněte na tlačítko "Go" nebo "Bridge"

### Metoda 2: API (alternativa)

Pokud preferujete API, můžete použít curl:

```bash
# Pro Marigold.cz
curl -X POST "https://fed.brid.gy/web-site" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "url=https://www.marigold.cz"

# Pro Vibecoding.cz
curl -X POST "https://fed.brid.gy/web-site" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "url=https://www.vibecoding.cz"
```

## Vaše bridgované účty

Po aktivaci budete mít následující účty:

### Marigold.cz
- **Mastodon/Fediverse:** `@marigold.cz@web.brid.gy`
- **Bluesky:** `marigold.cz.web.brid.gy`

### Vibecoding.cz
- **Mastodon/Fediverse:** `@vibecoding.cz@web.brid.gy`
- **Bluesky:** `vibecoding.cz.web.brid.gy`

## Jak to funguje

1. **První synchronizace:**
   - Bridgy Fed najde RSS feed na vaší homepage
   - Extrahuje a publikuje existující příspěvky z feedu
   - Obvykle začne s několika nejnovějšími články

2. **Průběžná synchronizace:**
   - Bridgy Fed periodicky kontroluje váš RSS feed (několikrát denně)
   - Když najde nový článek, automaticky ho publikuje do fediverse a Bluesky
   - Publikace obsahuje název, excerpt a odkaz na původní článek

3. **Formát publikace:**
   - Název článku
   - Krátký excerpt (z RSS feedu)
   - Odkaz na plný článek
   - Datum publikace

## Monitoring a správa

### Dashboard

Po aktivaci můžete sledovat stav na:
- Marigold.cz: https://fed.brid.gy/web/marigold.cz
- Vibecoding.cz: https://fed.brid.gy/web/vibecoding.cz

Dashboard zobrazuje:
- Počet publikovaných příspěvků
- Poslední synchronizaci
- Případné chyby

### Vyhledání vašich účtů

Lidé vás mohou najít zadáním vaší domény do vyhledávání:

**V Mastodon/Fediverse aplikacích:**
- Vyhledejte: `@marigold.cz@web.brid.gy`
- Nebo jen: `marigold.cz`

**V Bluesky:**
- Vyhledejte: `marigold.cz.web.brid.gy`
- Nebo jen: `marigold.cz`

### Kontrola funkčnosti

Po aktivaci počkejte 5-10 minut a zkontrolujte:

1. Otevřete Mastodon klienta (např. https://mastodon.social)
2. V vyhledávání zadejte: `@marigold.cz@web.brid.gy`
3. Měli byste vidět váš bridgovaný účet s několika nejnovějšími články

## Propagace

Po aktivaci můžete propagovat své nové účty:

### Text pro propagaci

```
🎉 Marigold.cz je teď i na fediverse a Bluesky!

Sledujte nás:
🐘 Mastodon: @marigold.cz@web.brid.gy
🦋 Bluesky: marigold.cz.web.brid.gy

Všechny nové články se automaticky publikují. Stačí zadat "marigold.cz"
do vyhledávání ve vašem oblíbeném fediverse klientu.
```

### Přidání odkazů na web

Můžete přidat odkazy na bridgované účty do footer-links v `_config.yml`:

```yaml
footer-links:
  mastodon: "@marigold.cz@web.brid.gy"
  bluesky: "marigold.cz.web.brid.gy"
```

## Časté dotazy

### Jak často se synchronizuje?
Bridgy Fed kontroluje RSS feed několikrát denně. Nové články se obvykle objeví do několika hodin.

### Co se stane s existujícími články?
Při první aktivaci Bridgy Fed publikuje několik nejnovějších článků z RSS feedu (obvykle 5-10).

### Můžu ovlivnit, které články se publikují?
Ano, články v RSS feedu (feed.xml) se publikují. Můžete upravit konfiguraci jekyll-feed pluginu v `_config.yml`.

### Co když chci přestat publikovat?
Můžete deaktivovat bridging na dashboardu Bridgy Fed nebo kontaktovat jejich podporu.

### Vidím interakce (lajky, odpovědi) na webu?
Ne, toto je jednoduchá RSS integrace pouze pro publikování. Pro přijímání interakcí zpět byste potřebovali webmentions (složitější).

### Můžu změnit formát příspěvků?
Formát je dán obsahem RSS feedu. Můžete upravit `excerpt_length` v `_config.yml` pro délku excerptů.

## Řešení problémů

### Bridgy Fed nenašel můj feed
- Zkontrolujte, že je feed dostupný na produkci: https://www.marigold.cz/feed.xml
- Ověřte, že homepage obsahuje `<link rel="alternate" type="application/rss+xml">` v hlavičce

### Články se nepublikují
- Zkontrolujte dashboard: https://fed.brid.gy/web/marigold.cz
- Počkejte alespoň 24 hodin po aktivaci
- Ověřte, že nové články mají správné datum (ne v budoucnosti)

### Nemohu najít bridgovaný účet
- Ujistěte se, že jste správně zadali `@marigold.cz@web.brid.gy` (včetně obou @)
- Zkuste vyhledávání v jiném fediverse klientu
- Počkejte alespoň 1 hodinu po aktivaci

## Další kroky (volitelné)

Pokud v budoucnu budete chtít více funkcí:

1. **Webmentions integrace:**
   - Přijímání lajků, repostů a odpovědí zpět na web
   - Vyžaduje přidání microformats2 do HTML
   - Dokumentace: https://indieweb.org/Webmention

2. **Vlastní Mastodon/Bluesky účty:**
   - Můžete si založit nativní účty místo bridgovaných
   - Pro automatické publikování použijte RSS-to-Mastodon služby nebo GitHub Actions

3. **Zobrazování sociálních interakcí:**
   - Použijte webmention.io pro sběr interakcí
   - Zobrazte počty lajků/repostů pod články

## Kontakt a podpora

- Bridgy Fed dokumentace: https://fed.brid.gy/docs
- GitHub: https://github.com/snarfed/bridgy-fed
- Podpora: https://github.com/snarfed/bridgy-fed/issues

---

**Datum vytvoření:** 21. října 2025
**Poslední aktualizace:** 21. října 2025
**Stav:** RSS integrace připravena, čeká na aktivaci
