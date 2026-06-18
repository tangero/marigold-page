---
slug: "mushra"
url: "/mobilnisite/slovnik/mushra/"
type: "slovnik"
title: "MUSHRA – Multiple Stimulus with Hidden Reference and Anchors method"
date: 2025-01-01
abbr: "MUSHRA"
fullName: "Multiple Stimulus with Hidden Reference and Anchors method"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mushra/"
summary: "Standardizovaná metodologie subjektivního hodnocení kvality zvuku definovaná organizacemi 3GPP a ITU. Posluchači hodnotí kvalitu několika zpracovaných audio vzorků proti skryté referenci a explicitním"
---

MUSHRA je standardizovaná subjektivní metoda hodnocení kvality zvuku, při které posluchači hodnotí více zpracovaných vzorků proti skryté referenci a explicitním kotvícím vzorkům za účelem vyhodnocení kvality řečových a audio kodeků.

## Popis

Metoda Multiple Stimulus with Hidden Reference and Anchors (MUSHRA) je rigorózní, řízený postup pro subjektivní hodnocení percepční kvality středně až vysoce kvalitních audio kodeků a zpracovatelských systémů. V testu MUSHRA je panelu posluchačů s normálním sluchem předložena série zvukových sekvencí. Pro každou testovanou položku posluchač slyší několik verzí (stimulů) stejného zdrojového audia: jedna je skrytá, nezpracovaná reference (originální vysoce kvalitní signál), další jsou testované výstupy kodeků/zpracování a jsou zahrnuty také explicitní kotvící stimuly – kotva vysoké kvality (např. mírný dolní propust) a kotva nízké kvality (např. výrazné omezení šířky pásma). Všechny stimuly včetně reference jsou prezentovány v náhodném pořadí a označeny anonymně (např. A, B, C). Úkolem posluchače je ohodnotit každý stimul na spojité škále od 0 (špatné) do 100 (výborné) vzhledem k jeho vnímání ideální kvality. Skrytá reference slouží jako interní kontrola spolehlivosti posluchače, zatímco kotvy poskytují pevný kvalitativní rámec, který zajišťuje konzistentnost skóre napříč různými testy a laboratořemi. Konečným výsledkem pro kodek je průměrné skóre všech posluchačů a testovaných položek, které poskytuje Mean Opinion Score ([MOS](/mobilnisite/slovnik/mos/)) spolehlivě odrážející jeho percepční výkon.

## K čemu slouží

Metoda MUSHRA byla vyvinuta, aby řešila omezení jednodušších poslechových testů, jako je Absolute Category Rating ([ACR](/mobilnisite/slovnik/acr/)), které jsou nedostatečné pro hodnocení vysoce kvalitního audia, kde jsou degradace často jemné. Před zavedením MUSHRA bylo porovnávání pokročilých širokopásmových nebo plnopásmových kodeků obtížné kvůli nedostatečné citlivosti a kontextu ve hodnocení. Metoda byla vytvořena, aby poskytla vysoce spolehlivý a opakovatelný způsob řazení výkonu řečových a audio kodeků, jako jsou [EVS](/mobilnisite/slovnik/evs/), [AMR-WB](/mobilnisite/slovnik/amr-wb/) a audio standardy 3GPP pro multimediální služby. Řeší problém subjektivního zkreslení skrytím reference a zahrnutím kalibrovaných kotev, které stabilizují hodnotící škálu napříč různými panely posluchačů a testovacími sezeními. To je klíčové pro standardizaci v 3GPP, kde jsou objektivní metriky (jako [PESQ](/mobilnisite/slovnik/pesq/)) nedostatečné a jsou potřeba definitivní, na člověka zaměřená rozhodnutí o kvalitě, aby bylo možné vybrat nejlepší kodek z konkurenčních návrhů pro zařazení do specifikací a zajistit tak optimální kvalitu zážitku pro koncové uživatele.

## Klíčové vlastnosti

- Používá skrytý, nezpracovaný referenční signál pro kalibraci posluchače
- Zahrnuje explicitní kotvy vysoké a nízké kvality pro stabilizaci hodnotící škály
- Využívá spojitou hodnotící škálu od 0 do 100 pro jemně odstupňované hodnocení
- Stimuly jsou prezentovány v náhodném, zaslepeném pořadí, aby se zabránilo zkreslení
- Navrženo pro hodnocení středně až vysoce kvalitních audio systémů (šířka pásma > 3,5 kHz)
- Výsledkem je robustní Mean Opinion Score (MOS) pro spolehlivé porovnání kodeků

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TR 26.936** (Rel-19) — Audio Codec Characterization Technical Report
- **TR 26.950** (Rel-19) — Surround Sound in 3GPP Services Study
- **TR 26.996** (Rel-19) — ISAR Split Rendering Audio Characterization

---

📖 **Anglický originál a plná specifikace:** [MUSHRA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mushra/)
