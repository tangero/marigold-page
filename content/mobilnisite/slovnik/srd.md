---
slug: "srd"
url: "/mobilnisite/slovnik/srd/"
type: "slovnik"
title: "SRD – Short Range Device"
date: 2025-01-01
abbr: "SRD"
fullName: "Short Range Device"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/srd/"
summary: "SRD označuje nízkovýkonové rádiové zařízení pracující v neregulovaném (volném) kmitočtovém pásmu pro komunikaci na krátkou vzdálenost. Zahrnuje zařízení jako RFID tagy, senzory a řadiče používané v Io"
---

SRD je nízkovýkonové rádiové zařízení pracující v neregulovaném (volném) kmitočtovém pásmu pro komunikaci na krátkou vzdálenost, jako jsou RFID tagy a senzory používané v IoT a automatizaci.

## Popis

Ve standardech 3GPP je Short Range Device (SRD) definován jako rádiový vysílač nebo přijímač poskytující nízkovýkonovou komunikaci na krátkou vzdálenost, typicky pracující v harmonizovaných neregulovaných (volných) kmitočtových pásmech. Tato zařízení nejsou součástí infrastruktury mobilní sítě, ale jsou v rámci studií 3GPP zvažována z hlediska koexistence a komplementárních případů užití, zejména pro Internet věcí (IoT) a služby založené na blízkosti. SRD pracují za specifických regulačních technických parametrů, jako je omezený efektivní izotropní vyzářený výkon ([EIRP](/mobilnisite/slovnik/eirp/)) a omezení pracovního cyklu, aby se minimalizovalo rušení a umožnilo sdílené využití spektra. Příklady zahrnují bezdrátové senzory, čtečky radiofrekvenční identifikace ([RFID](/mobilnisite/slovnik/rfid/)), systémy bezkontaktního vstupu a jednotky průmyslové telemetrie.

Z perspektivy architektury 3GPP jsou SRD často externí zařízení, která mohou komunikovat s uživatelským zařízením (UE) nebo síťovými prvky. Běžným scénářem je, kdy UE (jako smartphone) funguje jako brána nebo řadič pro SRD využívající technologii krátkého dosahu, jako je Bluetooth Low Energy ([BLE](/mobilnisite/slovnik/ble/)) nebo [IEEE](/mobilnisite/slovnik/ieee/) 802.15.4 (např. Zigbee). Síť 3GPP může poskytovat páteřní konektivitu a služby pro data shromážděná z těchto SRD. Specifikace 3GPP studují koexistenci mezi mobilními sítěmi (jako LTE nebo NR) a SRD pracujícími v přilehlých nebo stejných kmitočtových pásmech, analyzují potenciální scénáře rušení a definují techniky zmírnění, jako je kmitočtová separace, řízení výkonu a adaptivní plánování.

Technický provoz SRD se řídí regionálními regulacemi (např. [ETSI](/mobilnisite/slovnik/etsi/) v Evropě, [FCC](/mobilnisite/slovnik/fcc/) v USA), které definují povolená kmitočtová pásma, úrovně výkonu, modulační techniky a pravidla přístupu ke spektru, jako je Listen-Before-Talk ([LBT](/mobilnisite/slovnik/lbt/)). Úlohou 3GPP není standardizovat vnitřní provoz SRD, ale zajistit, aby mobilní sítě mohly spolehlivě fungovat v prostředí nasyceném takovými zařízeními, a definovat, jak mohou mobilní UE efektivně integrovat a spravovat připojení k SRD. Studie ve specifikacích jako TR 37.890 a TR 38.805 vyhodnocují dopad vysílání SRD na výkonnost LTE a NR v uplinku/downlinku a naopak, a poskytují pokyny pro nasazení sítí a certifikaci zařízení.

## K čemu slouží

Koncept SRD je v rámci 3GPP řešen za účelem správy stále přeplněného rádiového prostředí a zajištění robustního provozu mobilních služeb. Rozmach bezdrátových IoT zařízení, chytrých domácích spotřebičů a průmyslových senzorů pracujících v neregulovaných (volných) pásmech (jako 2,4 GHz a 5 GHz) vytváří potenciální zdroj rušení pro licencované mobilní sítě. Studie 3GPP o koexistenci SRD byly motivovány potřebou chránit kritické služby mobilního širokopásmového připojení a IoT před degradací způsobenou nekontrolovanými emisemi z nesčetných blízkých nízkovýkonových zařízení.

Historicky, jak mobilní sítě začaly využívat vyšší kmitočtová pásma a složitější modulační schémata (citlivá na rušení), se zvýšilo riziko z provozu SRD v přilehlých pásmech. Před formálními studiemi bylo rušení reaktivním problémem řešeným až po nasazení. Práce 3GPP poskytuje proaktivní standardizovaný rámec pro analýzu, který umožňuje výrobcům síťových zařízení a koncových zařízení navrhovat produkty s vestavěnými mechanismy koexistence. To je zvláště důležité pro kritické mobilní aplikace a pro scénáře sdílení spektra, jako je provoz [NR-U](/mobilnisite/slovnik/nr-u/) (NR v neregulovaném spektru) v pásmech využívaných také SRD.

Navíc zahrnutí úvah o SRD do práce 3GPP podporuje širší vizi integrovaného IoT, kde mobilní sítě poskytují celoplošnou konektivitu a správu pro množství lokálních zařízení krátkého dosahu. Porozuměním charakteristikám SRD může 3GPP lépe definovat schopnosti UE fungovat jako agregační body (např. prostřednictvím zařízení 5G RedCap nebo LTE-M) pro senzorová data z osobních sítí, čímž vytváří efektivní vícevrstvé komunikační architektury. Tím se řeší omezení použití mobilní konektivity pro každý jednotlivý nízkovýkonový senzor, což by bylo neefektivní z hlediska energie a síťových zdrojů.

## Klíčové vlastnosti

- Provoz v neregulovaném (volném) kmitočtovém pásmu za přísných limitů výkonu a pracovního cyklu
- Definováno pro studie koexistence se systémy 3GPP LTE a NR
- Zahrnuje širokou škálu typů zařízení (senzory, RFID, řadiče)
- Podléhá regionálním regulačním požadavkům (ETSI, FCC)
- Často využívá neradiotechnologie 3GPP (Bluetooth, Zigbee, Wi-Fi)
- Může být integrováno s mobilními sítěmi prostřednictvím bran UE

## Související pojmy

- [NR-U – New Radio Unlicensed](/mobilnisite/slovnik/nr-u/)

## Definující specifikace

- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR
- **TR 38.805** (Rel-14) — Study on New Radio Access Technology; 60 GHz unlicensed spectrum
- **TS 38.807** (Rel-16) — NR beyond 52.6 GHz Study

---

📖 **Anglický originál a plná specifikace:** [SRD na 3GPP Explorer](https://3gpp-explorer.com/glossary/srd/)
