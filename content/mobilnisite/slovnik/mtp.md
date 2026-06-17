---
slug: "mtp"
url: "/mobilnisite/slovnik/mtp/"
type: "slovnik"
title: "MTP – Message Transfer Part"
date: 2025-01-01
abbr: "MTP"
fullName: "Message Transfer Part"
category: "Protocol"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mtp/"
summary: "Základní signalizační protokol v architektuře SS7 (Signalizační systém č. 7) zodpovědný za spolehlivý, spojově orientovaný přenos signalizačních zpráv mezi síťovými uzly. Poskytuje směrování, detekci/"
---

MTP je základní signalizační protokol systému SS7 zodpovědný za spolehlivý, spojově orientovaný přenos signalizačních zpráv mezi síťovými uzly, který zajišťuje směrování, řízení chyb a řízení toku.

## Popis

Message Transfer Part (MTP) představuje úroveň 2 a 3 signalizačního protokolového zásobníku SS7, definovanou [ITU-T](/mobilnisite/slovnik/itu-t/) a přijatou 3GPP pro signalizaci v circuit-switched jádrové síti. Funguje jako transportní mechanismus pro signalizační protokoly vyšších vrstev, jako je [ISUP](/mobilnisite/slovnik/isup/) ([ISDN](/mobilnisite/slovnik/isdn/) User Part) a [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part). MTP pracuje tak, že mezi signalizačními body (SP) vytváří signalizační spoje a přenáší signalizační zprávy ve formě signálových jednotek. Jeho architektura je rozdělena do tří úrovní: MTP úroveň 1 definuje fyzikální charakteristiky (např. 64 kbps časový slot); MTP úroveň 2 poskytuje detekci chyb na úrovni spoje, korekci prostřednictvím retransmise a řazení za účelem zajištění spolehlivého doručení přes jeden signalizační spoj; MTP úroveň 3 zajišťuje směrování, diskriminaci a distribuci zpráv, stejně jako funkce správy sítě, jako je převzetí služeb při výpadku spoje a přesměrování provozu v reakci na poruchy. Mezi klíčové komponenty patří Signalizační spoj (Signaling Link), Signalizační trasa (Signaling Route) a Kód signalizačního bodu (Signaling Point Code, jedinečná síťová adresa). MTP spolupracuje s Signalizačním spojovacím řídícím subsystémem (SCCP) a poskytuje tak rozšířené možnosti směrování. V mobilní síti MTP spolehlivě přenáší kritické signalizační zprávy pro řízení hovorů, správu mobility (např. aktualizace polohy prostřednictvím MAP) a doručování SMS mezi síťovými elementy, jako jsou [MSC](/mobilnisite/slovnik/msc/), [HLR](/mobilnisite/slovnik/hlr/) a VLR. Jeho robustní funkce správy sítě zajišťují vysokou dostupnost a odolnost signalizační sítě.

## K čemu slouží

MTP byl vytvořen jako základ signalizačního systému SS7, aby řešil omezení přenosu signalizace ve stejném pásmu (in-band), používaného v dřívějších telefonních sítích. Tento způsob signalizace trpěl neefektivitou, náchylností k podvodům a omezenou funkcionalitou pro pokročilé služby. Vývoj digitálního přepojování a potřeba inteligentních síťových služeb (jako bezplatná čísla, roaming) si vyžádaly samostatnou, spolehlivou a výkonnou signalizační síť mimo hlasový přenos (out-of-band). MTP toto zajišťuje vytvořením vyhrazené paketové sítě pro signalizační zprávy, oddělené od kanálů pro přenos hovorů. Řeší kritický problém spolehlivého doručování signalizačních zpráv – které řídí vytáčení, ukončování hovorů a mobilitu – přes komplexní síť ústředen. Jeho spojově orientovaná povaha s korekcí chyb zajišťuje integritu signalizace, zatímco jeho hierarchické směrování a možnosti správy sítě umožňují, aby byla signalizační síť odolná vůči výpadkům spojů a uzlů. Přijetí MTP ve standardech 3GPP pro circuit-switched domény 2G (GSM) a 3G (UMTS) bylo zásadní pro umožnění automatického roamingu, plynulých předávání hovorů a široké škály doplňkových služeb. Vytvořil nepostradatelnou transportní vrstvu, na které byly vybudovány mobilní aplikační protokoly ([MAP](/mobilnisite/slovnik/map/), [CAP](/mobilnisite/slovnik/cap/)).

## Klíčové vlastnosti

- Poskytuje spolehlivý, spojově orientovaný přenos signalizačních zpráv s detekcí/korekcí chyb (MTP úroveň 2)
- Provádí směrování zpráv na základě cílových kódů bodů (Destination Point Codes) (MTP úroveň 3)
- Obsahuje komplexní funkce správy signalizační sítě pro zvládání poruch a přesměrování provozu
- Podporuje jak asociovaný (přímý), tak kvaziasociovaný (přes STP) režim signalizace
- Spolupracuje s fyzickými rozhraními, jako jsou časové sloty E1/T1 (64 kbps signalizační spoje)
- Tvoří transportní základ pro protokoly vyšších vrstev, jako jsou ISUP, TCAP a MAP

## Související pojmy

- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 28.734** (Rel-19) — STN Interface NRM IRP Requirements
- **TS 28.735** (Rel-19) — STN Interface NRM IRP Information Service
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification
- **TS 29.202** (Rel-19) — SS7 Signalling Transport Protocol Architectures
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 32.741** (Rel-11) — STN Interface NRM IRP Requirements
- **TS 32.742** (Rel-11) — STN NRM for Configuration Management
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [MTP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtp/)
