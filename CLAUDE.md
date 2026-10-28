# CLAUDE.md — Marigold.cz

Osobní web Patricka Zandla (od 2002) o technologiích, AI a mobilních sítích. Statický web v Hugo, hosting GitHub Pages, doména https://www.marigold.cz. Repozitář `tangero/marigold-page` (lokálně ve složce `zastupitelstvo`).

## Příkazy projektu

```
hugo server              # lokální server s live reload (-D i s drafty)
hugo --minify            # produkční build do public/
hugo --minify --config hugo.toml,sec.toml   # build s Hugem 0.169+ (viz docs/gotchas.md)
```

- Hugo v CI: **0.159.1 extended** (`.github/workflows/hugo-build.yml`). Lokální Hugo z brew je novější.
- Po změně šablon nebo obsahu spusť build a zkontroluj, že projde bez `ERROR`.

## Struktura

- `content/` — obsah: `posts/YYYY/` (blog), `ai/`, `mobilnisite/` (včetně slovníku 3GPP v `mobilnisite/slovnik/`, ~2750 pojmů), `obrazy/`, `en/` (anglické posty), stránky v kořeni (`aiprace.html`, `zebricek.md`, `vibecoding*.md`…).
- `layouts/` — Hugo šablony (`_default/`, `partials/`, sekce `posts/`, `ai/`, `mobilnisite/`, `obrazy/`, `slovnik/`).
- `static/` — kopíruje se 1:1 na web. Obrázky k článkům v `static/assets/` (na webu `/assets/…`).
- `assets/scss/` — jediné, co Hugo bere z `assets/`: `main.scss` přes `resources.Get`. Obrázky sem nepatří, nepublikují se.
- `data/` — data pro šablony (`pojmy.json` pro slovník, LLM katalog, klíčová slova).
- `scripts/` — Python skripty (infografiky slovníku, LLM katalog, migrace front matter). Závislosti v `requirements.txt`, API klíče v `.env` (vzor `.env.example`), prostředí `.venv/`.
- Kořen repa drží jen konfiguraci (`hugo.toml`, `.gitignore`, `CNAME`) a dokumenty (`README.md`, `CHANGELOG.md`, `CLAUDE.md`, `LICENSE`). Jednorázové skripty a poznámky sem nepatří: skript do `scripts/`, dokument do `docs/`.
- Jekyll verze webu (`_posts/` atd.) byla smazána 2026-10-28; najdeš ji v historii gitu.

## Záměrná rozhodnutí (nepřepisovat)

- **Datum článku je z názvu souboru** (`YYYY-MM-DD-slug.md`), ne z front matter (`hugo.toml`: `date = [":filename", ":default"]`). Permalink postů `/item/:slug/`.
- **Diskuse, reakce, hodnocení, žebříček a promo zóna běží na API vibecoding.cz** (`mg-comments.js`, `/api/engagement`, `/api/rating/top`, `/api/active-promotion`). Logika a data jsou v repu `~/Github/vibecoding-site`, tady jsou jen partialy, které je vkládají.
- **Substack promo** (`partials/substack-promo.html`) stahuje RSS při buildu (`resources.GetRemote`, cache 1 h). Proto workflow běží i denně v 5:15 UTC. Při výpadku feedu build projde a blok se nevykreslí.
- **Velká média nejsou v repu.** Audio je v Cloudflare R2: bucket `vibecoding-assets` (sdílený s vibecoding.cz), prefix `marigold/audio/`, URL `https://media.vibecoding.cz/marigold/audio/<soubor>`. Nahrání: `wrangler r2 object put vibecoding-assets/marigold/audio/<soubor> --file=<soubor> --content-type=audio/mpeg --remote`, v článku `audio_url:`.
- **Obrázky ve WebP**, max. šířka 2000 px: `magick vstup.jpg -auto-orient -colorspace sRGB -resize '2000x>' -strip -quality 82 -define webp:method=6 static/assets/nazev.webp`. Když by WebP vyšel větší než originál, nech originál. Název souboru bez mezer a diakritiky.
- **Checkout v CI je `fetch-depth: 1`.** Build nepoužívá `.GitInfo` a plná historie má 6,5 GB. Kdyby se zapínalo `enableGitInfo`, je potřeba `fetch-depth: 0`.

## Front matter postu

```yaml
---
slug: karpathy-llm-knowledgebase
title: Název článku
author: Patrick Zandl
categories:
  - AI
post_excerpt: Stručný popis
summary_points:
  - První bod
thumbnail: https://www.marigold.cz/assets/obrazek.webp
audio_url: https://media.vibecoding.cz/marigold/audio/soubor.mp3   # volitelné
---
```

## Konvence

- Kód, obsah a commit messages česky. Hugo šablony s mezerami kolem výrazů: `{{ .Title }}`, ne `{{.Title}}`.
- Python: type hints, Google docstrings, `logging` místo `print()`, formátování Black.
- **Po každém commitu aktualizuj `CHANGELOG.md`** (sekce `[Unreleased]`, Keep a Changelog: Added / Changed / Fixed / Removed). Popiš co a proč, s cestami k souborům.

## Pracovní dohoda

- **Push do `main` = okamžitý produkční deploy** (GitHub Actions → GitHub Pages, ~1,5–2,5 min). Před pushem build lokálně.
- **Minimální zásah.** Jen soubory relevantní k zadání, stávající styl. Zásah mimo zadání: nejdřív se zeptej.
- **Souhlas si vyžádej u** mazání obsahu, hromadných úprav napříč články a destruktivních git operací.
- **Ověř, než řekneš hotovo.** Po nasazení zkontroluj běh workflow (`gh run list --workflow=hugo-build.yml`) a živý web (`curl`).
- **Učení.** Po korekci od uživatele nebo po nečekaném problému zapiš vzorec a pravidlo do `docs/gotchas.md`.

## Dokumentace

- Index dokumentace: `docs/index.md`. Nový dokument do `docs/` a odkaz z indexu.
- `docs/gotchas.md` se nenačítá automaticky. U deploye, obrázků, odkazů a buildu v něm nejdřív hledej (grep).
- Historie změn: `CHANGELOG.md`.
