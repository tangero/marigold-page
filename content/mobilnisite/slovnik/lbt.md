---
slug: "lbt"
url: "/mobilnisite/slovnik/lbt/"
type: "slovnik"
title: "LBT – Listen Before Talk"
date: 2025-01-01
abbr: "LBT"
fullName: "Listen Before Talk"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lbt/"
summary: "Mechanismus přístupu k kanálu pro nelicencovaný spektrum, používaný primárně pro LTE-LAA, eLAA a NR-U. Vyžaduje, aby zařízení před zahájením vlastního vysílání detekovalo rádiový kanál pro případné pr"
---

LBT je mechanismus přístupu k kanálu pro nelicencovaný spektrum, kde zařízení musí před zahájením vlastního vysílání detekovat kanál pro případné probíhající přenosy, což zajišťuje rovnoměrné koexistenci s ostatními systémy.

## Popis

Listen Before Talk (LBT) je základní procedura přístupu k kanálu, která je vyžadována pro provoz v nelicencovaných nebo sdílených spektrálních pásmech, jako jsou pásma 5 GHz a 6 GHz. Je formou Carrier Sense [Multiple Access](/mobilnisite/slovnik/multiple-access/) s prevencí kolizí ([CSMA/CA](/mobilnisite/slovnik/csma-ca/)), kde vysílající node musí nejprve provést Clear Channel Assessment ([CCA](/mobilnisite/slovnik/cca/)) k detekci energetických hladin na zamýšleném kanálu. Pokud je kanál detekován jako volný po specifickou dobu (která se liší na základě priority přístupu k kanálu a regionálních regulací), node může zahájit vysílání na omezený čas, známý jako Channel Occupancy Time ([COT](/mobilnisite/slovnik/cot/)). Pokud je kanál obsazený, node musí vysílání odložit a provést proceduru náhodného odložení před pokusem o další detekci. Tento proces je klíčový pro zajištění harmonické a rovnoměrné koexistence s existujícími systémy, jako je Wi-Fi a další technologie na základě LBT, prevenci kolizí a řízení interference decentralizovaným způsobem.

Ve specifikacích 3GPP jsou procedury LBT detailně popsány pro LTE-based License Assisted Access ([LAA](/mobilnisite/slovnik/laa/)), enhanced LAA (eLAA) i NR-based [NR-U](/mobilnisite/slovnik/nr-u/) (New Radio in Unlicensed Spectrum). Implementace zahrnuje režimy provozu Frame-Based Equipment (FBE) a Load-Based Equipment (LBE), jak jsou definovány regulátory, například [ETSI](/mobilnisite/slovnik/etsi/) v Evropě. Pro LBE, který je běžnější, proces zahrnuje inicialní CCA (ICCA) a, pokud je kanál obsazený, extended CCA (ECCA) zahrnující náhodný odložkový counter. Transmitter musí také implementovat 'duty cycle' nebo dodržet idle period po svém COT, aby umožnil přístup ostatních zařízení. Detekce může být provedena pomocí prahových hodnot detekce energie ([ED](/mobilnisite/slovnik/ed/)) nebo, ve pokročilých implementacích, signálově-specifické detekce.

Role LBT v architektuře 3GPP je integrována do procedur Medium Access Control (MAC) layer a physical layer. Specifikace jako TS 38.321 a TS 38.331 definují MAC control elements a Radio Resource Control (RRC) parametry pro konfiguraci parametrů LBT. Physical layer specifikace (např. TS 38.215) detailně popisují skutečné detekční mechanismy a měření signálů. Z pohledu sítě LBT umožňuje operátorům rozšířit kapacitu licencovaného spektra nelicencovanými pásmy, podporující vyšší datové rychlosti a zlepšený výkon sítě prostřednictvím carrier aggregation nebo dual connectivity, kde primární cell na licencovaném spektru kotví spojení, zatímco secondary cells na nelicencovaném spektru poskytují dodatečnou šířku pásma.

## K čemu slouží

LBT bylo zavedeno k řešení výzvy nasazení buněčných technologií 3GPP v globálně dostupných, ale přeplněných nelicencovaných spektrálních pásmech. Před LAA a NR-U buněčné sítě fungovaly pouze v licencovaném spektru, které je omezené a drahé. Motivací bylo využití bohatého nelicencovaného spektra (např. 5 GHz) ke zvýšení kapacity a datových rychlostí, koncept známý jako Licensed Assisted Access. Tyto pásma však již jsou obsazeny jinými technologiemi, nejvýznamněji IEEE 802.11 (Wi-Fi), které používají CSMA/CA pro koexistenci. Nasazení buněčných signálů bez listen-before-talk protokolu by způsobilo nadměrnou interferenci a degradaci výkonu pro všechny uživatele, porušující regulatorní požadavky a principy rovného přístupu.

Vytvoření LBT v 3GPP, počínaje Release 13, bylo hnané potřebou regulatorní compliance v regionách jako Evropa a Japonsko, kde LBT je legislativní podmínkou pro provoz v určitých nelicencovaných pásmech. Řešilo kritický problém, jak učinit buněčné přenosy 'slušnými' sousedy. Bez LBT by base station nebo UE mohly vysílat bez detekce, způsobující trvalé kolize a znemožňující použití spektra pro Wi-Fi zařízení. LBT zajišťuje rovné podmínky uplatňováním pravidla 'detekuj před vysláním', sladěním systémů 3GPP s existující etiketou nelicencovaného ekosystému. Toto umožnilo mobilním operátorům úspěšně nasadit LTE a následně 5G NR ve sdíleném spektru, umožňující funkce jako carrier aggregation přes licencované a nelicencované nosiče pro dosažení throughputů na gigabitové úrovni.

## Klíčové vlastnosti

- Clear Channel Assessment (CCA) využívající detekci energie
- Channel Access Priority Classes (CAPC) pro diferenciaci QoS
- Procedura náhodného odložení pro prevenci kolizí
- Definované limity Channel Occupancy Time (COT)
- Podpora režimů Frame-Based i Load-Based equipment
- Integrace s frameworky carrier aggregation a dual connectivity

## Související pojmy

- [LAA – Licensed-Assisted Access](/mobilnisite/slovnik/laa/)
- [NR-U – New Radio Unlicensed](/mobilnisite/slovnik/nr-u/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.789** (Rel-13) — LAA Multi-Node Coexistence Test Methodology
- **TS 36.790** (Rel-15) — LAA/eLAA for CBRS 3.5GHz Band in US
- **TS 38.215** (Rel-19) — NR Physical Layer Measurements
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.523** (Rel-19) — 5G NR UE Conformance Testing: Idle/Inactive
- **TR 38.786** (Rel-18) — Technical Report for NR Sidelink Evolution
- **TR 38.805** (Rel-14) — Study on New Radio Access Technology; 60 GHz unlicensed spectrum
- **TS 38.807** (Rel-16) — NR beyond 52.6 GHz Study
- **TR 38.808** (Rel-17) — Study on NR above 52.6 GHz to 71 GHz
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [LBT na 3GPP Explorer](https://3gpp-explorer.com/glossary/lbt/)
