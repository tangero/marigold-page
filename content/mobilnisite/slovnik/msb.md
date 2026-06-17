---
slug: "msb"
url: "/mobilnisite/slovnik/msb/"
type: "slovnik"
title: "MSB – Mobile Station of the B subscriber"
date: 2025-01-01
abbr: "MSB"
fullName: "Mobile Station of the B subscriber"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/msb/"
summary: "Mobilní stanice (MS) představující volanou stranu (B-subscribera) v okruhově spínaném telefonním spojení, jako je hovor. Je to základní koncept pro dokončování hovorů, účtování a obsluhu doplňkových s"
---

MSB je mobilní stanice představující volanou stranu, neboli B-subscribera, v okruhově spínaném telefonním spojení v rámci starších sítí GSM a UMTS.

## Popis

Mobilní stanice B-subscribera (MSB) je logická entita definovaná ve specifikacích 3GPP pro okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) telekomunikační služby, primárně v sítích GSM a UMTS. Konkrétně odkazuje na mobilní terminál (nebo uživatelské zařízení), který je cílem hovoru nebo relace – volanou stranou. V rámci síťové architektury není MSB samostatným fyzickým zařízením, ale rolí, kterou mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) přebírá během procedur dokončování a řízení hovoru. Tato role je klíčová pro entity Řízení hovoru ([CC](/mobilnisite/slovnik/cc/)) a Řízení mobility ([MM](/mobilnisite/slovnik/mm/)) v síti, jako je Gateway [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)) a koncový MSC, aby správně směrovaly hovor, uplatnily zásady pro koncového účastníka a spustily odpovídající záznamy pro účtování.

Operační identifikace MSB je vázána na Mezinárodní identifikaci mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)) a přidružené telefonní číslo [MSISDN](/mobilnisite/slovnik/msisdn/). Při směrování hovoru GMSC dotazuje Home Location Register (HLR), aby získal směrovací informace (Mobile Station Roaming Number, MSRN) pro dosažení obsluhujícího MSC MSB. Koncový MSC následně identifikuje MS jako B-subscribera. To spouští specifické signalizační toky na rozhraní A a uvnitř Core Networku s využitím protokolů jako ISUP/BICC. Role MSB ovlivňuje provedení screeningu koncových hovorů, služeb přesměrování hovoru (CFB, CFNRy) a uplatnění jakýchkoli služeb blokování nebo přijímání specifických pro účastníka.

V kontextu doplňkových služeb je MSB entita, na které se služby jako Přesměrování při obsazení (CFB), Přesměrování při nezvednutí (CFNRy) nebo Přidržení hovoru spouštějí jako koncová podmínka. Rozlišení mezi B-subscriberem a A-subscriberem (MSA) je architektonicky významné pro správnou aplikaci větví hovoru a stavů v rámci MSC, zejména u funkcí jako Čekání na hovor a Konference. Zatímco je tento koncept hluboce zakořeněn v tradiční telefonii, jeho principy jsou základem modelů stavů hovoru a generování záznamů o účtování (CDR), kde jsou parametry jako 'číslo volané strany' a 'identifikátor účtování B-strany' vyplňovány na základě MSB. S vývojem směrem k all-IP sítím a IMS je funkční role B-subscribera řízena UE a S-CSCF pomocí protokolů SIP, ale legacy koncept MSB zůstává relevantní pro CS fallback, propojování a emulaci starších služeb.

## K čemu slouží

Koncept MSB byl vytvořen, aby poskytl jasný, standardizovaný model pro obsluhu koncové strany v okruhově spínaném mobilním hovoru. V raných systémech GSM byla telefonie primární službou a síťové prvky potřebovaly jednoznačný způsob identifikace volaného pro základní operace jako směrování, vyvolání služeb a účtování. Definice role B-subscribera umožnila konzistentní implementaci logiky dokončování hovorů napříč MSC různých výrobců a zajistila, že účtovací systémy mohou přesně přiřadit náklady nebo uplatnit koncové poplatky.

Před standardizovanými buněčnými systémy se telefonní komutace spoléhala na podobné koncepty, ale mobilita přinesla výzvu lokalizovat účastníka, který mohl být kdekoli. MSB jako součást abstrakce mobilní stanice vyřešila problém dynamického směrování hovoru k aktuální poloze účastníka prostřednictvím dotazů HLR a přidělení MSRN. Umožnila správné provedení pokročilých doplňkových služeb na základě toho, zda byl účastník příjemcem hovoru, například vyvolání přesměrování hovoru, když je MSB obsazena nebo nedostupná. Toto rozlišení bylo zásadní pro komerční nasazení mobilních sítí a vytvořilo základ pro podrobné záznamy o účtování (např. za dokončení hovoru) a povinnosti zákonného odposlechu související s příjmem hovoru.

Motivace vychází z potřeby robustního administrativního a provozního rámce symetrického k A-subscriberovi. Logickým oddělením B-subscribera mohly specifikace 3GPP definovat přesné chování pro doručování hovoru, vyzvání a procedury přijetí/položení. Tento model podpořil růst mobilní telefonie zajištěním interoperability a objasněním odpovědností sítě vůči přijímající straně, což je základ, který se později rozšířil na služby jako hlasová schránka (která funguje jako proxy B-subscribera) a řešení přenositelnosti čísel.

## Klíčové vlastnosti

- Identifikuje volanou stranu (příjemce) v okruhově spínaném mobilním spojení
- Spouští specifické procedury řízení hovoru a řízení mobility na koncovém MSC
- Určuje uplatnění koncových doplňkových služeb, jako je přesměrování hovoru a blokování
- Poskytuje klíčové parametry pro generování záznamů o účtování B-strany (CDR)
- Používá se v postupech zákonného odposlechu pro identifikaci cíle hovoru
- Základní pro model stavů hovoru v GSM/UMTS MSC při správě větví dokončování hovoru

## Související pojmy

- [MSA – Mobile Station of the A subscriber](/mobilnisite/slovnik/msa/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 24.244** (Rel-19) — Wireless LAN Control Plane Protocol
- **TS 24.554** (Rel-19) — 5G Proximity Services (ProSe) Protocols
- **TS 24.587** (Rel-19) — V2X Services Protocols for 5G System
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 26.101** (Rel-19) — Generic frame format for AMR and GSM-EFR speech codecs
- **TS 26.201** (Rel-19) — AMR-WB Speech Codec Frame Format
- **TS 26.441** (Rel-19) — EVS Audio Processing Introduction
- **TS 26.442** (Rel-19) — EVS Codec Fixed Point ANSI-C Code
- **TS 26.443** (Rel-19) — EVS Codec Floating-Point C Code
- **TS 26.444** (Rel-19) — EVS Codec Conformance Test Sequences
- **TS 26.450** (Rel-19) — EVS Codec DTX System Level Aspects
- **TS 26.451** (Rel-19) — EVS Codec Voice Activity Detector (VAD) Specification
- **TS 26.452** (Rel-19) — EVS Codec Fixed-Point C Code Implementation
- … a dalších 16 specifikací

---

📖 **Anglický originál a plná specifikace:** [MSB na 3GPP Explorer](https://3gpp-explorer.com/glossary/msb/)
