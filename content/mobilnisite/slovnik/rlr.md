---
slug: "rlr"
url: "/mobilnisite/slovnik/rlr/"
type: "slovnik"
title: "RLR – Receiver Loudness Rating"
date: 2025-01-01
abbr: "RLR"
fullName: "Receiver Loudness Rating"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/rlr/"
summary: "Objektivní, standardizovaná metrika, která kvantifikuje hlasitostní výkon přijímací cesty (sluchátka) v telekomunikačním koncovém zařízení, jako je mobilní telefon. Je klíčovým parametrem v celkovém ř"
---

RLR je standardizovaná metrika kvantifikující hlasitostní výkon přijímací cesty v telekomunikačním koncovém zařízení za účelem zajištění konzistentní poslechové hlasitosti.

## Popis

Receiver Loudness Rating (RLR) je základní akustický parametr definovaný ve specifikacích 3GPP a [ITU-T](/mobilnisite/slovnik/itu-t/) (např. ITU-T P.79) pro koncová zařízení. Je součástí rodiny 'Hlasitostních hodnocení' (Loudness Ratings), která modelují ztrátu přenosu na koncích telefonního spojení. Konkrétně RLR charakterizuje citlivost přijímací cesty zařízení – od elektrického vstupu na přijímači (sluchátku nebo reproduktoru) k akustickému výstupu u uživatelova ucha. Je vyjádřeno v decibelech (dB) a představuje ztrátu (nebo zesílení) hlasitosti; nižší hodnota RLR znamená hlasitější přijímaný zvuk. Měření se provádí za standardizovaných podmínek pomocí umělého ucha ([IEC](/mobilnisite/slovnik/iec/) 60318-4) a specifických testovacích signálů (např. růžový šum nebo šum tvarovaný podle spektra řeči), aby byla zajištěna reprodukovatelnost. RLR se vypočítá porovnáním naměřené hladiny akustického tlaku na umělém uchu s referenční úrovní. Je to kritická složka celkového výpočtu hlasitosti, který zahrnuje Send Loudness Rating (SLR) pro mikrofonní cestu a Overall Loudness Rating ([OLR](/mobilnisite/slovnik/olr/)) pro kompletní spojení. Plánovači sítí a výrobci terminálů používají hodnoty RLR spolu s předpokládanými úrovněmi sidetonu a ztrátami v síti k návrhu systémů, které splňují cílové hlasitostní parametry, a zajišťují tak uživatelům komfortní a srozumitelnou úroveň konverzace. Dodržování limitů RLR je často součástí procesu schvalování typu terminálu a certifikace, což zaručuje minimální kvalitu služby a interoperabilitu v celosvětové síti.

## K čemu slouží

RLR existuje proto, aby poskytlo objektivní, kvantifikovatelnou míru kritického aspektu kvality hlasového terminálu: jak hlasitě zní sluchátko uživateli. Před standardizovanými hlasitostními hodnoceními se akustika terminálů značně lišila, což vedlo k nekonzistentní uživatelské zkušenosti – některé telefony byly příliš tiché a jiné příliš hlasité, což mohlo způsobovat nepohodlí nebo poškození sluchu. Koncept Loudness Ratings byl vyvinut pro řízení celkové hlasitosti telefonních spojení a zajištění srozumitelnosti a komfortu. RLR se konkrétně zabývá přijímací stranou a umožňuje inženýrům navrhovat terminály a sítě tak, aby splňovaly specifické hlasitostní cíle (např. [OLR](/mobilnisite/slovnik/olr/) přibližně 10 dB pro dobré spojení). Řeší problém subjektivního hodnocení tím, že poskytuje reprodukovatelné laboratorní měření, které koreluje s vnímanou hlasitostí. Jeho vytvoření bylo motivováno potřebou interoperability v globální telekomunikační síti, kde se zařízení od různých výrobců spojují přes sítě s různými ztrátami. Definováním RLR umožnily normalizační orgány předvídatelné inženýrství kvality hlasu, což je zásadní pro spokojenost uživatelů a efektivní komunikaci, zejména v hlučném prostředí.

## Klíčové vlastnosti

- Objektivní měření akustické citlivosti přijímací cesty v decibelech (dB).
- Měření se provádí pomocí standardizovaného umělého ucha a testovacích signálů pro reprodukovatelnost.
- Integrální součást celkového výpočtu hlasitosti přenosu (spolu s SLR a OLR).
- Používá se pro návrh terminálů, schvalování typu a plánování přenosu v síti.
- Definováno v souboru doporučení 3GPP i ITU-T (např. P.79, G.121).
- Pomáhá zajistit konzistentní poslechovou hlasitost a kvalitu hlasu napříč zařízeními.

## Související pojmy

- [OLR – Overall Loudness Rating](/mobilnisite/slovnik/olr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.131** (Rel-19) — Terminal Acoustic Performance Requirements
- **TS 26.132** (Rel-19) — Terminal Acoustic Test Methods
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.261** (Rel-19) — Electro-acoustic specs for immersive terminals
- **TS 26.801** (Rel-19) — Testing UEs with Non-Traditional Earpieces
- **TS 43.050** (Rel-19) — GSM Transmission Planning for Speech Services
- **TS 43.058** (Rel-19) — Handsfree MS Transmission Quality Guidelines

---

📖 **Anglický originál a plná specifikace:** [RLR na 3GPP Explorer](https://3gpp-explorer.com/glossary/rlr/)
