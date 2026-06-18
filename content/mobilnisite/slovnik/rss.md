---
slug: "rss"
url: "/mobilnisite/slovnik/rss/"
type: "slovnik"
title: "RSS – Rich Site Summary (Really Simple Syndication)"
date: 2025-01-01
abbr: "RSS"
fullName: "Rich Site Summary (Really Simple Syndication)"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rss/"
summary: "RSS je formát webového kanálu používaný k publikování často aktualizovaného obsahu, jako jsou titulek zpráv nebo blogové příspěvky. V kontextech 3GPP je odkazován v servisních požadavcích a schopnoste"
---

RSS je formát webového kanálu používaný k publikování často aktualizovaného obsahu, který umožňuje efektivní distribuci webových informací odběratelům přes mobilní sítě.

## Popis

Rich Site Summary (RSS), známé také jako Really Simple Syndication, je na [XML](/mobilnisite/slovnik/xml/) založený formát pro syndikaci webového obsahu. Ačkoli se nejedná o protokol definovaný 3GPP, je v rámci specifikací 3GPP odkazován, zejména v servisních požadavcích (např. TS 22.140 pro multimediální broadcast/multicast služby) a schopnostech pro doručování obsahu. RSS kanál obsahuje strukturovaná metadata o obsahu webové stránky, včetně titulků, souhrnů, dat publikace a odkazů na celé články. Uživatelé se k těmto kanálům přihlašují pomocí RSS čtečky (nebo agregátoru), která periodicky dotazuje [URI](/mobilnisite/slovnik/uri/) kanálu pro aktualizace, což umožňuje centralizovaný přístup k obsahu z více zdrojů bez nutnosti manuální návštěvy každé stránky.

V rámci architektury 3GPP je RSS považována za službu aplikační vrstvy, která může být doručována přes mobilní sítě. Úlohou sítě je poskytnout základní IP konektivitu, kvalitu služeb a potenciálně optimalizované mechanismy doručování. Například 3GPP zkoumalo a standardizovalo mechanismy pro efektivní doručování obsahu, jako je Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a evolved MBMS (eMBMS), které by mohly být použity k push aktualizacím RSS kanálů pro velké skupiny uživatelů současně, čímž se šetří síťové prostředky ve srovnání s individuálními unicast [HTTP](/mobilnisite/slovnik/http/) požadavky. Specifikace odkazující na RSS (jako TS 26.093 pro testování řečových kodeků nebo TS 37.842 pro rádiový výkon) tak často činí v kontextu definování servisních požadavků, testovacích metodologií nebo případů užití, které zahrnují periodické doručování nebo konzumaci webových médií a informací.

Z pohledu sítě interaguje doručování RSS kanálů s několika základními funkcemi. Framework Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)) může být aplikován pro správu QoS pro aktualizace kanálů. Aplikační vrstva User Equipment zpracovává parsování a prezentaci RSS XML. Schopnost sítě podporovat efektivní push notifikace (např. přes [SIP](/mobilnisite/slovnik/sip/) Push nebo APNs) může vylepšit uživatelský zážitek poskytováním včasných aktualizací při současné optimalizaci výdrže baterie zařízení. Tudíž, ačkoli je RSS samo o sobě internetovým standardem, jeho zahrnutí do specifikací 3GPP zdůrazňuje, že standardizační orgán bere v úvahu reálné aplikace a potřebu, aby je sítě efektivně podporovaly.

## K čemu slouží

RSS, jako internetová technologie, bylo vytvořeno k řešení problému informačního přetížení a neefektivní konzumace obsahu na webu. Před RSS museli uživatelé manuálně kontrolovat své oblíbené webové stránky kvůli aktualizacím. RSS tento proces automatizovalo, což uživatelům umožnilo přihlásit se k odběru zdrojů obsahu a přijímat aktualizace ve standardizovaném, agregovaném formátu. To významně zlepšilo efektivitu vyhledávání a konzumace informací.

Zařazení odkazů na RSS do specifikací 3GPP vychází z potřeby definovat, jak by mobilní sítě měly podporovat populární internetové služby a modely doručování obsahu. Jak se mobilní zařízení stala primárními přístupovými body pro zprávy a média, pracovní skupiny 3GPP zvažovaly servisní požadavky pro spolehlivé a efektivní doručování takového obsahu přes buněčné spoje. Účelem nebylo standardizovat samotné RSS, ale zajistit, aby schopnosti sítě definované 3GPP (jako broadcast/multicast, QoS, účtování a schopnosti zařízení) mohly adekvátně podporovat služby postavené na technologiích jako RSS. Toto zajišťuje konzistentní a kvalitní uživatelský zážitek pro služby agregace obsahu napříč různými mobilními operátory a typy zařízení a sladění vývoje buněčných sítí s převažujícími trendy internetových aplikací.

## Klíčové vlastnosti

- Formát založený na XML pro syndikaci webového obsahu (titulky, odkazy, souhrny, data publikace).
- Umožňuje uživatelům přihlásit se k odběru aktualizací obsahu z více zdrojů v jednom agregátoru.
- Funguje na pull modelu (klient dotazuje server), ale může být kombinováno se síťovými push mechanismy.
- Odkazováno v 3GPP specifikacích servisních požadavků pro doručování obsahu a multimediální služby.
- Může být doručováno přes unicast nebo optimalizováno pomocí multicast/broadcast (MBMS/eMBMS) síťových funkcí.
- Představuje třídu periodických služeb aktualizace obsahu s nízkou šířkou pásma podporovaných mobilními sítěmi.

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 25.143** (Rel-19) — UTRA FDD Repeater RF Test Requirements
- **TS 26.093** (Rel-19) — SCR operation of AMR codec for UMTS
- **TS 26.150** (Rel-19) — Syndicated Feed Reception (SFR) Specification
- **TS 26.192** (Rel-19) — AMR-WB Comfort Noise Requirements
- **TS 26.193** (Rel-19) — AMR-WB Source Controlled Rate (SCR) Operation
- **TS 26.849** (Rel-12) — MBMS Operation on Demand (MooD)
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TR 38.903** (Rel-19) — Test Tolerances & Measurement Uncertainties
- **TS 46.002** (Rel-19) — Introduction to GSM Half-Rate Speech Processing
- **TS 46.021** (Rel-19) — GSM Half Rate DTX Frame Substitution & Muting
- **TS 46.041** (Rel-19) — GSM Half Rate Speech DTX Operation
- **TS 46.051** (Rel-19) — GSM Enhanced Full Rate Speech Processing Intro
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [RSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rss/)
