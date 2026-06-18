---
slug: "phs"
url: "/mobilnisite/slovnik/phs/"
type: "slovnik"
title: "PHS – Personal Handy-phone System"
date: 2025-01-01
abbr: "PHS"
fullName: "Personal Handy-phone System"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/phs/"
summary: "Personal Handy-phone System (PHS) je digitální standard bezdrátové telekomunikace, který se primárně nasadil v Japonsku a částech Asie. Pracuje v pásmu 1,9 GHz a nabízí hlasové služby s nízkou mobilit"
---

PHS je digitální standard bezdrátové telekomunikace (Personal Handy-phone System), který se primárně nasadil v Japonsku a Asii, pracuje v pásmu 1,9 GHz a nabízí hlasové služby s nízkou mobilitou a vysokou hustotou uživatelů a omezené datové služby.

## Popis

Personal Handy-phone System (PHS) je standard digitálního bezdrátového telefonního systému, který funguje jako bezdrátový přístupový systém s nízkou mobilitou a vysokou kapacitou. Architektonicky se skládá z PHS terminálů (ručních přístrojů), základnových stanic Cell Stations ([CS](/mobilnisite/slovnik/cs/)) a síťového řadiče, který často rozhraní s veřejnou telefonní sítí ([PSTN](/mobilnisite/slovnik/pstn/)). Pro rádiový přenos používá vícenásobný přístup s časovým dělením ([TDMA](/mobilnisite/slovnik/tdma/)) a duplex s časovým dělením ([TDD](/mobilnisite/slovnik/tdd/)), které rozdělují frekvenční pásmo na časové sloty pro uplink a downlink komunikaci. Systém pracuje ve frekvenčním pásmu 1880-1930 MHz a využívá mikrobunky s typickým poloměrem buňky 100-500 metrů k dosažení vysoké hustoty uživatelů v městských oblastech.

PHS funguje tak, že naváže spojení mezi PHS terminálem a základnovou stanicí Cell Station. Terminál skenuje řídicí kanály vysílané blízkými stanicemi CS a vybere nejlepší z nich pro registraci a sestavení hovoru. Pro hovor iniciovaný mobilním zařízením odešle terminál žádost o kanál na uplink řídicím kanálu. Stanice CS přidělí provozní kanál (konkrétní časový slot na frekvenci) a hovor je směrován přes CS k síťovému řadiči a dále do sítě PSTN nebo k jinému PHS terminálu. Předávání hovoru mezi stanicemi Cell Stations je podporováno, ale bylo relativně pomalé ve srovnání s buněčnými systémy, což omezovalo jeho vhodnost pro vysokorychlostní mobilitu.

Klíčové komponenty zahrnují PHS terminál (který integruje rádiový transceiver, řídicí jednotku a uživatelské rozhraní), základnovou stanici Cell Station (která zvládá správu rádiových zdrojů, přidělování kanálů a vysílání/příjem signálu) a síťový řadič (který spravuje autentizaci, mobilitu a propojení s pevnými sítěmi). Jeho úlohou bylo poskytovat nákladově efektivní, kvalitní hlasovou službu s delší výdrží baterie přístroje ve srovnání s ranými buněčnými systémy, primárně v hustých pěších prostředích. Byly také zavedeny datové služby jako [PIAFS](/mobilnisite/slovnik/piafs/) (PHS Internet Access Forum Standard), které umožňovaly vytáčené připojení k internetu.

## K čemu slouží

PHS byl vytvořen, aby uspokojil potřebu nízkonákladového bezdrátového komunikačního systému s vysokou kapacitou pro pěší uživatele a uživatele s nízkou mobilitou, zejména v hustě obydlených městských oblastech Japonska. Byl vyvinut na počátku 90. let 20. století jako alternativa k tradičním buněčným sítím, které byly drahé a zaměřené na vozidlovou mobilitu. Motivací bylo využít technologii bezdrátových telefonů k poskytování osobních komunikačních služeb s lepší hlasovou kvalitou než analogové buněčné sítě (jako 1G) a s nižšími náklady na infrastrukturu a terminály.

Historický kontext představovalo rychlé přijetí mobilních služeb v Japonsku a hledání systému, který by mohl obsloužit masivní populace dojíždějících v městech jako Tokio. PHS vyřešil problém efektivity spektra a hustoty uživatelů použitím mikrobuněk a dynamického přidělování kanálů, což umožnilo více současných hovorů na plochu než tehdejší buněčné systémy. Odstranil omezení dřívějších bezdrátových telefonů (jako CT2) tím, že nabídl obousměrné volání, předávání hovoru a lepší integraci s veřejnou sítí.

Jeho omezení však vyšla najevo, když dospěly plnohodnotné buněčné sítě (2G jako [PDC](/mobilnisite/slovnik/pdc/) a GSM), nabízející bezproblémovou vysokorychlostní mobilitu a širší pokrytí. Mikrobuněčná architektura PHS, ačkoli byla výborná pro hustotu, vedla ke složitému předávání hovorů a špatnému pronikání do budov ve srovnání s pozdějšími buněčnými technologiemi používajícími nižší frekvence. Jeho hlavní odkaz v řešení problémů představovala demonstrace proveditelnosti vysokohustotního bezdrátového přístupu s nízkým výkonem, koncepty později zdokonalené ve standardech 3GPP pro femtobunky a nasazení v hustě obydlených městských oblastech.

## Klíčové vlastnosti

- Mikrobuněčná architektura s malými poloměry buněk (100-500 m) pro vysokou hustotu uživatelů
- Používá TDMA/TDD v pásmu 1,9 GHz pro efektivní využití spektra
- Dynamické přidělování kanálů ke snížení interference a optimalizaci kapacity
- Podporuje obousměrné volání, předávání hovoru a identifikaci volajícího
- Nízký vysílací výkon (průměrně 10 mW) umožňující dlouhou výdrž baterie přístrojů
- Schopnost datových služeb přes PIAFS pro přístup k internetu (až 64 kbps)

## Související pojmy

- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)
- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [PIAFS – PHS Internet Access Forum Standard](/mobilnisite/slovnik/piafs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 27.001** (Rel-19) — Terminal Adaptation Functions for PLMN
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.802** (Rel-10) — MSR BS RF Requirements for Non-Contiguous Spectrum
- **TS 37.812** (Rel-11) — Multi-band Multi-standard Radio BS Requirements
- **TS 37.814** (Rel-12) — L-band Supplemental Downlink for UTRA/E-UTRA
- **TR 37.900** (Rel-19) — Multi-Standard Radio (MSR) Base Station Requirements

---

📖 **Anglický originál a plná specifikace:** [PHS na 3GPP Explorer](https://3gpp-explorer.com/glossary/phs/)
