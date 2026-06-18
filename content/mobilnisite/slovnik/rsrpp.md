---
slug: "rsrpp"
url: "/mobilnisite/slovnik/rsrpp/"
type: "slovnik"
title: "RSRPP – Reference Signal Received Path Power"
date: 2025-01-01
abbr: "RSRPP"
fullName: "Reference Signal Received Path Power"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rsrpp/"
summary: "RSRPP je měření přijímaného výkonu konkrétní dráhy referenčního signálu v NR. Je klíčové pro pokročilé operace s více anténami a správu paprsků, což síti umožňuje posoudit kvalitu jednotlivých šířicíc"
---

RSRPP je měření přijímaného výkonu pro konkrétní dráhu referenčního signálu v NR, používané k posouzení kvality jednotlivých šířicích drah pro operace s více anténami a pro správu paprsků.

## Popis

Reference Signal Received Path Power (RSRPP) je klíčové měření na fyzické vrstvě zavedené v 5G New Radio (NR) pro podporu pokročilých anténních systémů a scénářů s více konektivitami. Na rozdíl od tradičního [RSRP](/mobilnisite/slovnik/rsrp/), které poskytuje širokopásmové měření výkonu referenčních signálů, je RSRPP navrženo k měření přijímaného výkonu konkrétní, identifikovatelné signálové dráhy. Tato granularita je zásadní v prostředích, kde se současně nebo koordinovaně používá více bodů vysílání a příjmu ([TRP](/mobilnisite/slovnik/trp/)) nebo více paprsků ze stejného TRP. Měření se provádí na specifických referenčních signálech, jako jsou Channel State Information Reference Signals ([CSI-RS](/mobilnisite/slovnik/csi-rs/)) nebo Synchronization Signal Blocks (SSB), které jsou nakonfigurovány pro operace s více TRP nebo více paprsky.

Z architektonického hlediska jsou měření a hlášení RSRPP řízeny fyzickou vrstvou UE a protokoly vrstvy 2/3 pod konfigurací sítě. gNB nakonfiguruje UE pomocí signalizace [RRC](/mobilnisite/slovnik/rrc/), aby měřila specifické zdroje CSI-RS nebo SSB spojené s různými TRP nebo paprsky. UE poté změří lineární průměrný výkon prvků nesoucích tyto specifické referenční signály pro nakonfigurovanou dráhu. Výsledek měření, typicky v dBm, je filtrován a hlášen síti, která tyto informace používá pro dynamické plánování, správu paprsků a rozhodování o adaptaci spoje.

Role RSRPP je klíčová pro umožnění funkcí jako Non-Coherent Joint Transmission (NC-JT), kde jsou data přenášena z více TRP do jednoho UE, a pro sofistikované postupy správy a obnovy paprsků. Díky pochopení přijímaného výkonu na úrovni jednotlivých drah může síť činit inteligentní rozhodnutí o tom, které TRP nebo paprsky aktivovat, jak vyvážit výkon a jak udržet robustní konektivitu v náročných rádiových podmínkách. Poskytuje základní metriku pro scénáře s více konektivitami a pro komunikaci s ultra-spolehlivým nízkým zpožděním ([URLLC](/mobilnisite/slovnik/urllc/)) definované v 5G.

## K čemu slouží

RSRPP bylo vytvořeno, aby řešilo omezení tradičního [RSRP](/mobilnisite/slovnik/rsrp/) v kontextu pokročilých anténních technologií 5G a architektur s více konektivitami. Před NR poskytovalo RSRP v LTE agregované měření výkonu užitečné pro výběr buňky a mobilitu, ale postrádalo granularitu potřebnou k rozlišení mezi více souběžnými přenosovými drahami z různých [TRP](/mobilnisite/slovnik/trp/) nebo vysoce směrových paprsků. Když 5G zavedlo koncepty jako operace s více TRP, integrovaný přístup a přenos ([IAB](/mobilnisite/slovnik/iab/)) a sofistikovaný beamforming, bylo vyžadováno nové měření pro posouzení kvality jednotlivých prostorových drah.

Primární problém, který RSRPP řeší, je umožnění síti provádět přesnou analýzu rozpočtu spoje a správu zdrojů pro specifické přenosové dráhy. To je kritické pro maximalizaci zisků ve spektrální účinnosti a spolehlivosti, které slibují systémy s více anténami. Například ve scénáři koordinovaného vícebodového přenosu (CoMP) síť potřebuje znát přesný přijímaný výkon od každého účastnícího se TRP, aby se mohla rozhodnout o přidělení výkonu a schématech modulace a kódování (MCS) pro každý proud. RSRPP poskytuje tato zásadní data a usnadňuje funkce, které zlepšují výkon na okraji buňky, zvyšují kapacitu sítě a posilují odolnost proti překážkám – klíčové požadavky pro služby 5G jako rozšířené mobilní širokopásmové připojení (eMBB) a URLLC.

## Klíčové vlastnosti

- Měří přijímaný výkon pro konkrétní, nakonfigurovanou dráhu referenčního signálu (např. od konkrétního TRP nebo paprsku).
- Podporuje měření na zdrojích CSI-RS i SSB pro flexibilitu.
- Zásadní pro umožnění schémat přenosu s více TRP, jako je Non-Coherent Joint Transmission (NC-JT).
- Poskytuje detailní vstup pro pokročilé postupy správy paprsků a obnovy po selhání paprsku.
- Nakonfigurováno a hlášeno prostřednictvím signalizace RRC, integrováno do měřicího rámce NR.
- Zlepšuje výkon sítě ve vysokofrekvenčních pásmech a scénářích hustého nasazení.

## Související pojmy

- [RSRP – Reference Signal Received Power](/mobilnisite/slovnik/rsrp/)
- [RSRQ – Reference Signal Receiving Quality](/mobilnisite/slovnik/rsrq/)
- [CSI-RS – Channel State Information Reference Signal](/mobilnisite/slovnik/csi-rs/)

## Definující specifikace

- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [RSRPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rsrpp/)
