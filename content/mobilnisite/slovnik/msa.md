---
slug: "msa"
url: "/mobilnisite/slovnik/msa/"
type: "slovnik"
title: "MSA – Mobile Station of the A subscriber"
date: 2025-01-01
abbr: "MSA"
fullName: "Mobile Station of the A subscriber"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/msa/"
summary: "Mobilní stanice (MS) reprezentující volajícího (účastníka A) v telefonním spojení s přepojováním okruhů, například při hlasovém hovoru. Jde o základní koncept pro řízení hovoru, účtování a obsluhu dop"
---

MSA je mobilní stanice (Mobile Station) reprezentující volajícího (účastníka A) v přepojování okruhů (circuit-switched) pro řízení hovoru, účtování a služby v legacy sítích GSM a UMTS.

## Popis

Mobilní stanice účastníka A (MSA) je logická entita definovaná ve specifikacích 3GPP pro telekomunikační služby s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)), primárně v sítích GSM a UMTS. Konkrétně odkazuje na mobilní koncové zařízení (nebo uživatelské zařízení), které iniciuje hovor nebo relaci – tedy na volajícího. V rámci síťové architektury není MSA samostatným fyzickým zařízením, ale rolí, kterou mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) přebírá během procedur navazování a řízení hovoru. Tato role je klíčová pro entity řízení hovoru ([CC](/mobilnisite/slovnik/cc/)) a správy mobility ([MM](/mobilnisite/slovnik/mm/)) v jádru sítě, jako je ústředna mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)), aby správně směrovala hovor, aplikovala zásady pro účastníka iniciujícího hovor a spustila odpovídající záznamy pro účtování.

Operační identifikace MSA je vázána na mezinárodní identifikaci mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)) a přidružené telefonní číslo [MSISDN](/mobilnisite/slovnik/msisdn/). Když je hovor iniciován, obsluhující MSC identifikuje MS jako účastníka A. Toto spouští specifické signalizační toky na rozhraní A (mezi řadičem základnových stanic a MSC) a uvnitř jádra sítě za použití protokolů jako [ISDN](/mobilnisite/slovnik/isdn/) User Part (ISUP) nebo Bearer Independent Call Control (BICC). Role MSA ovlivňuje provádění screeningu odchozích hovorů, služeb informace o ceně hovoru a aplikaci jakýchkoli služeb zákazu nebo přesměrování specifických pro účastníka, definovaných v domovském registru polohy (HLR).

V kontextu doplňkových služeb je MSA entita, na které jsou služby jako bezpodmínečné přesměrování hovoru (CFU) nebo explicitní přenos hovoru (ECT) vyvolány jako podmínka iniciování. Rozlišení mezi účastníkem A a účastníkem B (MSB) je architektonicky významné pro správnou aplikaci větví hovoru a stavů uvnitř MSC. Zatímco je tento koncept hluboce zakořeněn v tradiční telefonii, jeho principy tvoří základ modelů stavů hovoru a generování záznamů o účtovaných datech (CDR), kde jsou parametry jako 'číslo volajícího' a 'identifikátor účtování pro stranu A' vyplněny na základě MSA. S vývojem směrem k plně IP sítím a IP multimediální podsystému (IMS) je funkční role účastníka A spravována uživatelským zařízením (UE) a funkcí S-CSCF za použití protokolů SIP, ale legacy koncept MSA zůstává relevantní pro scénáře CS fallback a pro vzájemné propojování sítí.

## K čemu slouží

Koncept MSA byl vytvořen, aby poskytl jasný, standardizovaný model pro obsluhu iniciující strany v mobilním hovoru s přepojováním okruhů. V raných systémech GSM byla telefonie primární službou a síťové prvky potřebovaly jednoznačný způsob identifikace volajícího pro základní operace jako směrování, vyvolání služeb a účtování. Definice role účastníka A umožnila konzistentní implementaci logiky řízení hovoru napříč MSC různých výrobců a zajistila, že systémy účtování mohly přesně přiřadit náklady iniciující straně.

Před standardizovanými buněčnými systémy se telefonní komutace spoléhala na podobné koncepty (např. identifikace volajícího v PSTN), ale aspekt mobility přinesl komplexitu. MSA jako součást abstrakce mobilní stanice vyřešila problém spojení hovoru s konkrétní, potenciálně roamující, identitou účastníka a jeho profilem služeb. Umožnila správné provádění pokročilých doplňkových služeb (jako čekání hovoru nebo konferenční hovory) na základě toho, zda byl účastník iniciátorem nebo příjemcem hovoru. Toto rozlišení bylo nezbytné pro komerční nasazení mobilních sítí, neboť tvořilo základ pro podrobné záznamy o účtování a povinnosti zákonného odposlechu související s iniciací hovoru.

Motivace vychází z potřeby robustního administrativního a provozního rámce. Logickým oddělením účastníka A a účastníka B mohly specifikace 3GPP definovat přesné chování pro navázání hovoru, jeho ukončení a změny během hovoru. Tento model podpořil růst mobilní telefonie zajištěním interoperability a objasněním odpovědností sítě vůči každé straně ve dvoustranném hovoru, což byl základ, který se později rozšířil na konferenční hovory a rané datové služby přes přepojování okruhů.

## Klíčové vlastnosti

- Identifikuje volajícího (iniciátora) v mobilním spojení s přepojováním okruhů
- Spouští specifické procedury řízení hovoru a správy mobility v iniciující MSC
- Určuje aplikaci odchozích doplňkových služeb a screeningu hovorů
- Poskytuje klíčové parametry pro generování záznamů o účtovaných datech (CDR) pro stranu A
- Používá se v postupech zákonného odposlechu pro identifikaci původu hovoru
- Základní pro model stavu hovoru v GSM/UMTS MSC pro správu větví hovoru

## Související pojmy

- [MSB – Mobile Station of the B subscriber](/mobilnisite/slovnik/msb/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TR 26.981** (Rel-19) — MBMS Provisioning & Content Ingestion Interface Study
- **TS 29.116** (Rel-19) — REST-based protocol for xMB reference point
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview

---

📖 **Anglický originál a plná specifikace:** [MSA na 3GPP Explorer](https://3gpp-explorer.com/glossary/msa/)
