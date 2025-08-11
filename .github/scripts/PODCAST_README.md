# Podcast Automation Script

Automatické generování audio verzí článků pomocí ElevenLabs API.

## Požadavky

1. **ElevenLabs účet** s API klíčem
2. **GitHub token** s právy zápisu do repository
3. **Python 3.8+** s knihovnami: PyGithub, requests, pyyaml

## Nastavení

### 1. GitHub Secrets

V repository nastavte tyto secrets:
- `ELEVENLABS_API_KEY` - váš API klíč z ElevenLabs
- `GITHUB_TOKEN` - automaticky dostupný v GitHub Actions

### 2. Konfigurace v článku

Pro vygenerování audio musí mít článek v YAML hlavičce:

```yaml
---
title: Název článku
date: 2024-01-01
audio: true  # <-- POVINNÉ pro generování audio
excerpt: Krátký popis článku
---
```

### 3. Vypnutí audio generování

Pro článek, který NEMÁ mít audio:

```yaml
---
title: Název článku
audio: false  # nebo vůbec neuvedeno
---
```

## Jak to funguje

1. **Automatické spuštění:**
   - Při push nového článku do `_posts/`
   - Denně v 10:00 UTC (kontrola nových článků)
   - Ručně přes GitHub Actions

2. **Proces:**
   - Script najde články s `audio: true` bez `audio_url`
   - Vygeneruje audio pomocí ElevenLabs API
   - Uloží MP3 do `/audio/` adresáře
   - Aktualizuje článek s `audio_url`
   - Přidá položku do RSS feedu

3. **Výstup:**
   - Audio soubor: `/audio/YYYY-MM-DD-nazev-clanku.mp3`
   - RSS feed: `/podcast-feed.xml`
   - URL: `https://www.marigold.cz/audio/YYYY-MM-DD-nazev-clanku.mp3`

## Limity

- **Text délka:** Maximum 5000 znaků (lze upravit v scriptu)
- **API limity:** Závisí na vašem ElevenLabs plánu
- **Zpracování:** Pouze 1 článek za běh (ochrana API limitů)

## Ruční spuštění

### Lokálně:
```bash
export ELEVENLABS_API_KEY="váš-api-klíč"
export GITHUB_TOKEN="váš-github-token"
python .github/scripts/podcast-automation-script.py
```

### GitHub Actions:
1. Jděte do Actions tab
2. Vyberte "Generate Podcast Audio"
3. Klikněte "Run workflow"

## Troubleshooting

### Audio se negeneruje
- Zkontrolujte, že článek má `audio: true`
- Ověřte, že nemá již `audio_url` v hlavičce
- Zkontrolujte logs v GitHub Actions

### API chyby
- Ověřte platnost ELEVENLABS_API_KEY
- Zkontrolujte API limity na ElevenLabs dashboardu

### Encoding problémy
- Script používá UTF-8
- Články musí být v UTF-8 kódování

## Struktura výsledného článku

Po zpracování bude článek vypadat takto:

```yaml
---
title: Název článku
date: 2024-01-01
audio: true
audio_url: https://www.marigold.cz/audio/2024-01-01-nazev-clanku.mp3
audio_generated: 2024-01-15T10:30:00
excerpt: Krátký popis
---

Obsah článku...
```

## RSS Feed

Podcast feed je dostupný na:
- `https://www.marigold.cz/podcast-feed.xml`

Obsahuje všechny vygenerované audio články s metadaty.