---
slug: "dbi"
url: "/mobilnisite/slovnik/dbi/"
type: "slovnik"
title: "DBI – Delay Budget Information"
date: 2025-01-01
abbr: "DBI"
fullName: "Delay Budget Information"
category: "QoS"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dbi/"
summary: "Delay Budget Information (DBI) je parametr QoS zavedený ve specifikaci 3GPP Release 16, který kvantifikuje maximální přípustné zpoždění paketu pro datový tok. Je klíčovou součástí pro umožnění determi"
---

DBI je parametr QoS, který kvantifikuje maximální přípustné zpoždění paketu pro datový tok, což umožňuje síti splnit přísné požadavky na latenci.

## Popis

Delay Budget Information (DBI) je standardizovaný parametr kvality služeb (QoS) definovaný v rámci architektury 5G systému (5GS). Představuje maximální povolený rozpočet zpoždění paketu, vyjádřený v milisekundách, pro konkrétní relaci protokolové datové jednotky ([PDU](/mobilnisite/slovnik/pdu/)) nebo QoS tok. DBI je skalární hodnota, která tvoří součást charakteristik identifikátoru QoS 5G ([5QI](/mobilnisite/slovnik/5qi/)), nebo může být explicitně signalizována jako součást profilu QoS. Je klíčovým vstupem pro síťové funkce, zejména funkci správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)), funkci správy relací ([SMF](/mobilnisite/slovnik/smf/)) a rádiovou přístupovou síť (RAN), pro vynucování záruk latence.

Z architektonického hlediska je DBI propagováno prostřednictvím core sítě a do RAN přes referenční body [N2](/mobilnisite/slovnik/n2/) a N11. Při zřízení nebo modifikaci PDU relace SMF určuje požadované parametry QoS, včetně DBI, na základě abonentních dat, pravidel řízení politik od funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) a požadavků aplikační funkce. SMF následně tyto informace poskytne AMF, která je přepošle uzlu (R)[AN](/mobilnisite/slovnik/an/) (gNB) během procedury zřizování PDU relace. RAN využívá DBI spolu s dalšími parametry, jako je míra chybovosti paketů ([PER](/mobilnisite/slovnik/per/)) a garantovaný přenosový tok (GFBR), k provádění plánování paketů, řízení přístupu a správy rádiových prostředků. Například tok s velmi malým DBI (např. 1 ms pro tovární automatizaci) bude mít při plánování vyšší prioritu než tok s větším DBI (např. 100 ms pro streamování videa).

V RAN je DBI klíčové pro implementaci algoritmů plánování citlivých na latenci. Plánovač gNB bere v úvahu zbývající rozpočet zpoždění pro každý zařazený paket. Paketům, které se blíží svému limitu rozpočtu zpoždění, je přiřazena vyšší priorita pro přenos přes rozhraní vzduchového rozhraní. Tento mechanismus je zásadní pro podporu časově citlivé komunikace (TSC) a služeb URLLC definovaných v 3GPP. DBI je navíc nedílnou součástí end-to-end síťového řezání. Instance síťového řezu vytvořená pro vertikálu, jako je průmyslový IoT, může mít QoS profil s přísným DBI, což zajišťuje, že prostředky řezu jsou konfigurovány a spravovány tak, aby konzistentně dosahovaly tohoto cíle latence napříč funkcemi uživatelské roviny.

DBI funguje v součinnosti s dalšími mechanismy QoS. Zatímco 5QI poskytuje standardizované mapování na výchozí charakteristiky QoS (včetně výchozího DBI), QoS profil pro konkrétní tok to může přepsat explicitní hodnotou DBI. To umožňuje jemně odlišenou diferenciaci služeb. Správa DBI je také spojena s funkcí reflexivního QoS v modelu QoS 5G, kde uživatelské zařízení (UE) může odvodit pravidla QoS pro uplink, včetně implicitního porozumění požadavkům na latenci, z pozorování provozu v downlinku. DBI tedy není jen statickým popisovačem, ale aktivním parametrem, který řídí dynamické chování sítě za účelem plnění smluvních dohod o úrovni služeb (SLA) pro aplikace citlivé na latenci.

## K čemu slouží

DBI bylo vytvořeno, aby řešilo zásadní výzvu podpory deterministické latence a ultra-spolehlivé komunikace s nízkou latencí (URLLC) v 5G a dalších generacích. Předchozí generace mobilních sítí (4G/LTE) byly primárně optimalizovány pro vysoké přenosové rychlosti a best-effort mobilní širokopásmový přístup. Jejich QoS rámec, soustředěný kolem QCI (identifikátor třídy QoS), sice obsahoval rozpočet zpoždění paketu, nebyl však navržen ani signalizován způsobem, který by mohl garantovat extrémní spolehlivost a latence pod 10 ms požadované novými vertikálními odvětvími, jako je tovární automatizace, vzdálená chirurgie, autonomní vozidla a chytré sítě.

Motivace pro standardizaci DBI jako explicitního, akčního informačního prvku vychází z potřeby end-to-end garance služeb. Aplikace v průmyslovém IoT a taktilním internetu mají přísné, nevyjednatelné lhůty pro doručení dat. Bez jasného, kvantifikovaného rozpočtu zpoždění komunikovaného od core sítě k RAN nemůže plánovač gNB inteligentně upřednostňovat časově kritické pakety před méně naléhavými. DBI poskytuje tento společný jazyk. Řeší problém nejasných požadavků na latenci tím, že z časového omezení aplikace učiní rovnoprávnou součást řetězce vyjednávání a vynucování QoS, což umožňuje proaktivní, nikoli reaktivní chování sítě.

Historicky bylo řízení latence často až druhotnou záležitostí nebo bylo řešeno nadměrnou dimenzací. DBI jako součást vylepšeného QoS rámce 5G zavedeného ve verzi Release 16 pro vertikály a TSC představuje posun směrem k přesným, kvantifikovatelným a vynutitelným garancím latence. Řeší omezení předchozích přístupů tím, že je nedílnou součástí signalizace při zřizování PDU relace a QoS toku, což zajišťuje, že každý síťový uzel zapojený do datové cesty je si vědom rozpočtu latence a může přispět k jeho splnění. Tato evoluce byla nezbytná k transformaci 5G z platformy pro konektivitu na spolehlivou servisní platformu pro kritickou komunikaci.

## Klíčové vlastnosti

- Kvantifikuje maximální přípustné zpoždění paketu pro QoS tok v milisekundách
- Je klíčovou součástí charakteristik identifikátoru QoS 5G (5QI) a QoS profilů
- Dynamicky ovlivňuje rozhodnutí RAN o plánování paketů a řízení přístupu
- Umožňuje end-to-end garanci latence pro URLLC a časově citlivou komunikaci (TSC)
- Podporováno explicitní signalizací přes rozhraní N2 (AMF k RAN) a N11 (SMF k AMF)
- Nezbytné pro realizaci síťového řezání se specifickými garancemi výkonnosti z hlediska latence

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [DBI na 3GPP Explorer](https://3gpp-explorer.com/glossary/dbi/)
