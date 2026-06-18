---
slug: "rdi"
url: "/mobilnisite/slovnik/rdi/"
type: "slovnik"
title: "RDI – Reflective QoS flow to DRB mapping Indication"
date: 2025-01-01
abbr: "RDI"
fullName: "Reflective QoS flow to DRB mapping Indication"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rdi/"
summary: "Mechanismus v systémech 5G a novějších, ve kterém UE autonomně mapuje uplinkové QoS toky na datové rádiové přenosové cesty (DRB) odrazem downlinkového mapování signalizovaného sítí. Snižuje signalizač"
---

RDI je mechanismus, ve kterém UE autonomně mapuje uplinkové QoS toky na DRB odrazem downlinkového mapování signalizovaného sítí, čímž se snižuje signalizační režie.

## Popis

Indikace odrazného mapování QoS toku na [DRB](/mobilnisite/slovnik/drb/) (RDI) je základním konceptem v rámci rámce kvality služeb (QoS) 5G, konkrétně definovaným pro uživatelskou rovinu. Funguje na principu, že charakteristiky a požadavky QoS pro danou službu jsou často symetrické mezi uplinkovým a downlinkovým směrem. Síť explicitně konfiguruje mapování downlinkových QoS toků na datové rádiové přenosové cesty (DRB) pro UE prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/). Mechanismus RDI umožňuje UE pozorovat toto downlinkové mapování a následně autonomně aplikovat identické neboli 'odrazné' mapování pro odpovídající uplinkové QoS toky na stejné DRB, aniž by vyžadovala další explicitní konfigurační zprávy RRC od gNB pro uplink. Tento proces je řízen odraznou QoS, kde je QoS tok označen indikátorem odrazné QoS ([RQI](/mobilnisite/slovnik/rqi/)) v hlavičkách downlinkových paketů (prostřednictvím značek [QFI](/mobilnisite/slovnik/qfi/) a RQI v zapouzdřovacím protokolu, jako je [GTP-U](/mobilnisite/slovnik/gtp-u/)). Když UE přijímá downlinkové pakety pro tok s nastaveným RQI, spustí se interní operace odrazné QoS, která zahrnuje i aspekt mapování DRB indikovaný RDI. Přístupová vrstva UE monitoruje tato downlinková mapování a udržuje odrazné mapování pro uplink. Toto mapování zůstává platné po dobu životnostního časovače; pokud nejsou před jeho vypršením přijaty žádné downlinkové pakety pro daný tok, UE odrazné mapování uvolní. Koncept RDI je těsně integrován s celkovým modelem QoS 5G definovaným v TS 23.501, kde QoS toky představují nejjemnější granularitu pro diferenciaci QoS a DRB jsou rádiové přenosové cesty, které data skutečně přenášejí. Využitím RDI systém dosahuje efektivního a dynamického vynucování QoS s minimální signalizací v řídicí rovině, což je klíčové pro podporu obrovského počtu zařízení a služeb s nízkou latencí, kde musí být signalizační zpoždění minimalizováno. Mechanismus zajišťuje, že přísné požadavky na latenci, spolehlivost a šířku pásma pro uplinkový provoz (např. pro interaktivní služby nebo [URLLC](/mobilnisite/slovnik/urllc/)) jsou splněny použitím stejné konfigurace přenosové cesty, která se osvědčila pro downlinkovou část.

## K čemu slouží

RDI bylo zavedeno, aby řešilo problémy škálovatelnosti a efektivity signalizace v sítích 5G, které podporují nebývalou hustotu zařízení a rozmanité požadavky služeb. Před 5G vyžadovala správa QoS přenosových cest často explicitní obousměrnou konfiguraci, což vedlo k významné režii signalizace [RRC](/mobilnisite/slovnik/rrc/), zejména ve scénářích s častým vytvářením nebo modifikací QoS toků, jako je síťové segmentování nebo dynamická adaptace služeb. Koncept odrazné QoS, včetně RDI, to řeší přesunutím části inteligence na UE. Umožňuje síti komplexně nakonfigurovat downlinkovou cestu a spoléhat na to, že UE toto nastavení odrazí pro uplink na základě pozorovaného chování sítě. To je zvláště cenné pro služby jako Voice over NR (VoNR), rozšířená realita nebo řídicí průmyslový IoT, kde jsou uplinkové a downlinkové proudy inherentně spárované a mají symetrické požadavky na QoS. Snížení počtu explicitních signalizačních příkazů urychluje vytváření a modifikaci relací, snižuje latenci pro časově kritické aplikace a odlehčuje zpracování jak na gNB, tak na vrstvě RRC v UE. Historicky LTE využívalo dedikované přenosové cesty s explicitním propojením, ale odrazný model 5G, umožněný mechanismy jako RDI, představuje posun k autonomnějšímu, štíhlejšímu a na služby zaměřenému řízení rádiových zdrojů, což je základním konstrukčním principem flexibilní architektury 5G.

## Klíčové vlastnosti

- Umožňuje UE autonomní mapování uplinkových QoS toků na DRB na základě pozorovaného downlinkového mapování
- Snižuje režii signalizace RRC pro správu QoS a přenosových cest
- Funguje ve spojení s indikátorem odrazné QoS (RQI) v uživatelské rovině
- Používá časovač životnosti pro zajištění platnosti mapování a umožnění jeho odstranění
- Integruje se s modelem QoS 5G pro granulární diferenciaci služeb
- Podporuje dynamickou adaptaci služeb s nízkou latencí pro symetrické uplinkové/downlinkové toky

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification
- **TS 37.324** (Rel-19) — Service Data Adaptation Protocol (SDAP)

---

📖 **Anglický originál a plná specifikace:** [RDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/rdi/)
