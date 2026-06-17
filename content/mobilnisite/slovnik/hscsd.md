---
slug: "hscsd"
url: "/mobilnisite/slovnik/hscsd/"
type: "slovnik"
title: "HSCSD – High Speed Circuit Switched Data"
date: 2025-01-01
abbr: "HSCSD"
fullName: "High Speed Circuit Switched Data"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hscsd/"
summary: "Okruhově přepínaná datová služba pro sítě GSM, která zvyšuje přenosové rychlosti tím, že umožňuje mobilní stanici současně využívat více časových slotů v rámci TDMA rámce. Šlo o rané vylepšení pro pos"
---

HSCSD je okruhově přepínaná datová služba pro sítě GSM, která zvyšuje přenosové rychlosti tím, že umožňuje mobilní stanici současně využívat více časových slotů v rámci TDMA rámce.

## Popis

High Speed Circuit Switched Data (HSCSD) je vylepšení okruhově přepínané datové služby pro sítě GSM, standardizované v 3GPP Release 4 (a dřívějších fázích GSM). Na rozdíl od základní datové služby GSM, která byla omezena na jeden časový slot na TDMA rámec (s maximem 9,6 kbps nebo 14,4 kbps s vylepšeným kódováním), HSCSD umožňuje mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) agregovat více časových slotů pro jedno datové spojení. Toho je dosaženo technikou zvanou více-slotový provoz, kdy je MS na dobu hovoru přiděleno dva nebo více z osmi časových slotů v TDMA rámci, čímž se úměrně násobí dosažitelná datová rychlost.

Architektonicky HSCSD funguje v rámci stávající okruhově přepínané jádrové sítě GSM. HSCSD hovor vytváří vyhrazený okruh (nebo více okruhů, odpovídajících časovým slotům) mezi MS a Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)), podobně jako hlasový hovor. Klíčové funkční doplňky jsou v řízení rádiových prostředků a v možnostech terminálu. Síť musí být schopna přidělit a spravovat více traffic kanálů (TCH/F nebo TCH/H) pro jedno spojení. MS a Base Transceiver Station ([BTS](/mobilnisite/slovnik/bts/)) musí podporovat více-slotový provoz, který definuje maximální počet časových slotů, které zařízení může použít pro vysílání a příjem. Data z vyšších vrstev jsou na rádiovém rozhraní rozdělena mezi přidělené časové sloty.

Jak to funguje, zahrnuje vyjednávání během sestavování hovoru. MS oznamuje síti svou více-slotovou třídu a požadovanou datovou rychlost. Řízení rádiových prostředků sítě se následně pokusí přidělit požadovaný počet časových slotů na jednom rádiovém kmitočtovém nosiči. Přidělení může být asymetrické, což umožňuje více slotů pro downlink než pro uplink (nebo naopak), což je výhodné pro aplikace jako prohlížení webu. Data jsou přenášena přes A-rozhraní k MSC pomocí více 64 kbps časových slotů v PCM lince, které jsou pak namapovány na odpovídající časové sloty vzdušného rozhraní. Korekce chyb využívá stejných konvolučních kódovacích schémat jako standardní GSM, ale aplikovaných napříč agregovaným kanálem.

Role HSCSD v síti spočívala v poskytnutí migrační cesty k vyšším datovým rychlostem v rámci okruhově přepínaného paradigmatu předtím, než se paketově přepínaná řešení jako [GPRS](/mobilnisite/slovnik/gprs/) stala zralá a široce nasazená. Využívala stávající infrastrukturu pro okruhové přepínání, vyžadující především softwarové upgrady v síti a nové více-slotové telefony. Ačkoli poskytovala hmatatelné zvýšení rychlosti, trpěla inherentní neefektivitou okruhového přepínání pro trhavý datový provoz, protože vyhrazené prostředky byly drženy po celou dobu hovoru bez ohledu na skutečnou datovou aktivitu. Primárně byla používána pro raný mobilní přístup k internetu, fax a aplikace vysokorychlostního přenosu souborů na konci 90. let a začátku 21. století.

## K čemu slouží

HSCSD bylo vyvinuto, aby reagovalo na rostoucí poptávku po vyšších rychlostech mobilních datových služeb v polovině až konci 90. let, kdy se GSM stalo dominantním globálním buněčným standardem. Standardní datová služba GSM s rychlostí 9,6 kbps byla dostačující pro základní fax a emulaci vytáčeného modemu, ale byla bolestně pomalá pro vznikající světovou síť a podnikové datové aplikace. Průmysl potřeboval způsob, jak nabídnout datové rychlosti podobné [ISDN](/mobilnisite/slovnik/isdn/) (např. 28,8 kbps, 43,2 kbps nebo dokonce 57,6 kbps) přes stávající infrastrukturu GSM bez kompletní architektonické přestavby.

Motivací bylo prodloužit životnost a zvýšit schopnosti masivních investic do sítí GSM poskytnutím relativně přímočaré cesty upgradu. Základní koncept byl jednoduchý, ale účinný: místo vynalézání nové rádiové technologie agregovat stávající základní zdroj – TDMA časový slot. Tento přístup vyřešil problém nízkých datových rychlostí využitím volné kapacity sítě (více časových slotů), která byla často dostupná, ale nevyužitá. Umožnil operátorům nabízet datové služby na různých úrovních (např. '2-slotová' nebo '4-slotová' spojení) s odpovídajícím účtováním.

HSCSD řešilo omezení jedno-slotového okruhově přepínaného modelu. Zároveň však také poukázalo na neefektivitu aplikace okruhově přepínaného modelu, navrženého pro hlas s konstantní přenosovou rychlostí, na trhavý datový provoz. Právě toto omezení pomohlo motivovat souběžný vývoj paketově přepínaného [GPRS](/mobilnisite/slovnik/gprs/), který nabídl efektivnější 'vždy připojený' model. HSCSD sloužilo jako důležitý technologický přechodový stupeň, který demonstroval tržní poptávku po mobilních datech a prokázal proveditelnost vyšších rychlostí na GSM, zatímco se průmysl připravoval na paketově přepínanou budoucnost.

## Klíčové vlastnosti

- Zvyšuje datové rychlosti agregací více GSM časových slotů (více-slotový provoz)
- Funguje jako okruhově přepínaná služba, vytvářející vyhrazené spojení
- Podporuje asymetrické přidělování slotů (různý počet pro uplink a downlink)
- Vyžaduje více-slotové mobilní stanice a podporu sítě
- Používá stávající schémata kanálového kódování GSM (např. TCH/F9.6, TCH/F14.4)
- Datové rychlosti škálovatelné až na ~57,6 kbps (čtyři sloty po 14,4 kbps)

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.034** (Rel-19) — High Speed Circuit Switched Data (HSCSD) Stage 1
- **TS 23.034** (Rel-19) — HSCSD Stage 2 Service Description
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)

---

📖 **Anglický originál a plná specifikace:** [HSCSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/hscsd/)
