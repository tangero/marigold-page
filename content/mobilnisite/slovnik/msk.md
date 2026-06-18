---
slug: "msk"
url: "/mobilnisite/slovnik/msk/"
type: "slovnik"
title: "MSK – Minimum-shift keying"
date: 2026-01-01
abbr: "MSK"
fullName: "Minimum-shift keying"
category: "Physical Layer"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/msk/"
summary: "MSK je modulační schéma frekvenční manipulace s konstantní obálkou a spojitou fází (CPFSK). Je spektrálně účinné a odolné vůči nelineárnímu zesílení, což z něj činilo historicky důležitou modulaci pro"
---

MSK je modulační schéma frekvenční manipulace s konstantní obálkou a spojitou fází, které je spektrálně účinné a odolné vůči nelineárnímu zesílení; historicky bylo používáno v GSM a mobilních komunikacích.

## Popis

Minimum-shift keying (MSK) je specifický typ frekvenční manipulace se spojitou fází (CPFSK) charakterizovaný modulačním indexem 0,5. Tato volba indexu vede k minimální frekvenční vzdálenosti mezi dvěma symbolovými stavy (typicky reprezentujícími binární 0 a 1), která umožňuje jejich ortogonalitu během periody symbolu, odtud název 'minimum-shift'. Konstantní obálka a spojitá fáze modulovaného signálu jsou jeho definující vlastnosti. Konstantní obálka znamená, že amplituda signálu se nemění s modulujícími daty, což umožňuje jeho zesílení vysoce účinnými, nelineárními výkonovými zesilovači (jako jsou zesilovače třídy C) bez významného spektrálního návratu nebo zkreslení. Spojitá fáze zajišťuje, že nedochází k náhlým fázovým přechodům, což vede ke kompaktní výkonové spektrální hustotě s nízkým vyzařováním mimo pásmo.

Matematicky lze signál MSK reprezentovat jako formu offset kvadraturní fázové manipulace (OQPSK) se sinusovým tvarováním impulsu. Tato ekvivalence je cenná pro pochopení jeho generování a detekce. V praxi lze MSK generovat pomocí napětím řízeného oscilátoru ([VCO](/mobilnisite/slovnik/vco/)) přímo modulovaného daty, nebo stabilněji pomocí struktury modulátoru podobného OQPSK se sinusovou váhovou funkcí na fázové (I) a kvadraturní (Q) datové větvi. Demodulace MSK může být provedena pomocí koherentní detekce, podobně jako u [PSK](/mobilnisite/slovnik/psk/), nebo pomocí nekoherentní detekce, jako je diskriminátorová detekce, což bylo výhodné v dřívějších, jednodušších přijímačích.

V systémech 3GPP byla nejvýznamnější aplikací MSK standard GSM pro modulaci 0,3 [GMSK](/mobilnisite/slovnik/gmsk/) (Gaussian Minimum Shift Keying) používanou na rádiovém rozhraní. GMSK je MSK s Gaussovským předmodulačním filtrováním pro další vyhlazení fázových přechodů a ještě těsnější omezení spektrálního obsazení, což bylo klíčové pro splnění přísných požadavků GSM na výkon v sousedním kanále. Zatímco pozdější systémy 3GPP (UMTS, LTE, 5G NR) přešly na lineární modulační schémata jako [QPSK](/mobilnisite/slovnik/qpsk/) a [QAM](/mobilnisite/slovnik/qam/) pro vyšší spektrální účinnost, principy MSK/GMSK zůstávají relevantní pro pochopení modulace s konstantní obálkou a samotné MSK se stále používá v jiných bezdrátových standardech, jako je Bluetooth (pomocí GFSK, zobecnění) a satelitní komunikace.

## K čemu slouží

MSK bylo vyvinuto pro potřeby výkonově a spektrálně účinného digitálního modulačního schématu pro kanály s nelineárními charakteristikami, zejména v mobilní rádiové a satelitní komunikaci. Lineární modulační schémata jako [QPSK](/mobilnisite/slovnik/qpsk/), ačkoli jsou spektrálně účinná, mají proměnnou obálku. Při průchodu nelineárními výkonovými zesilovači (které jsou výkonově účinnější) tyto variace způsobují spektrální rozprostření do sousedních kanálů (spektrální návrat) a zkreslení signálu. Vlastnost konstantní obálky MSK ji činí přirozeně imunní vůči těmto efektům, což umožňuje použití účinných, saturovaných zesilovačů bez nutnosti nákladných a neúčinných linearizačních technik.

Vlastnost 'minimum-shift' (modulační index = 0,5) byla zvolena pro maximalizaci spektrální účinnosti při daném výkonu bitové chybovosti při nekoherentní detekci, která byla v dřívějších mobilních přijímačích jednodušší na implementaci. Představuje optimální kompromis v CPFSK: menší index by snížil šířku pásma, ale na úkor odolnosti proti šumu, zatímco větší index by zlepšil odolnost proti šumu za cenu větší šířky pásma. MSK poskytovalo dobrou rovnovhu, umožňující spolehlivou komunikaci v omezeném rádiovém spektru. Jeho evoluce na [GMSK](/mobilnisite/slovnik/gmsk/) v GSM byla přímou reakcí na potřebu ještě těsnější kontroly spektra pro podporu vysokokapacitních celulárních sítí s minimálním rušením mezi sousedními rádiovými kanály.

## Klíčové vlastnosti

- Signál s konstantní obálkou, umožňující použití s nelineárními, vysoce účinnými výkonovými zesilovači
- Spojitá fázová trajektorie, eliminující náhlé fázové skoky
- Modulační index 0,5, zajišťující ortogonalitu mezi symboly
- Kompaktní výkonová spektrální hustota s nízkými postranními spektrálními laloky
- Lze reprezentovat a generovat jako formu OQPSK se sinusovým tvarováním impulsu
- Vhodné pro koherentní i nekoherentní detekční schémata

## Související pojmy

- [GMSK – Gaussian Minimum Shift Keying](/mobilnisite/slovnik/gmsk/)

## Definující specifikace

- **TS 23.247** (Rel-19) — 5G Multicast/Broadcast Service Architecture
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 33.246** (Rel-19) — MBMS Security Specification
- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture
- **TS 33.402** (Rel-19) — Security for non-3GPP access to EPS
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.545** (Rel-19) — Security for NR Femto Subsystem
- **TR 33.882** (Rel-18) — Technical Report on 5G Security for Personal IoT Networks
- **TS 33.888** (Rel-12) — Security Study for Group Communication in LTE
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR

---

📖 **Anglický originál a plná specifikace:** [MSK na 3GPP Explorer](https://3gpp-explorer.com/glossary/msk/)
