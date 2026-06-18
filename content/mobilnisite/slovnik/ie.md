---
slug: "ie"
url: "/mobilnisite/slovnik/ie/"
type: "slovnik"
title: "IE – Information Element"
date: 2025-01-01
abbr: "IE"
fullName: "Information Element"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ie/"
summary: "Základní datová struktura v protokolech 3GPP používaná k zapouzdření konkrétních informací vyměňovaných mezi síťovými entitami. Je základním stavebním prvkem protokolových zpráv, který umožňuje přenos"
---

IE (Information Element) je základní, standardizovaná datová struktura, která zapouzdřuje specifické informace a slouží jako stavební prvek protokolových zpráv vyměňovaných mezi síťovými entitami v systémech 3GPP.

## Popis

Information Element (IE) je strukturovaný datový kontejner definovaný v rámci specifikací protokolů 3GPP. Slouží jako atomická jednotka informace přenášená v protokolových zprávách napříč různými rozhraními, jako je rozhraní rádiové (Uu), rozhraní mezi RAN a jádrem sítě (např. S1, [N2](/mobilnisite/slovnik/n2/)) nebo uvnitř jádra sítě samotného (např. N4, N11). Každá IE je detailně definována konkrétní syntaxí, sémantikou a pravidly kódování. Syntaxe definuje strukturu IE, která typicky zahrnuje identifikátor ([IEI](/mobilnisite/slovnik/iei/)), indikátor délky a samotný obsah či hodnotu. Sémantika definuje přesný význam a interpretaci obsahu, jako je například identita sledované oblasti (Tracking Area Identity), profil QoS nebo hlášení rádiového měření. Pravidla kódování specifikují, jak je IE serializována do bitového toku pro přenos, často s využitím ASN.1 [PER](/mobilnisite/slovnik/per/) (Packed Encoding Rules) nebo jiných binárních formátů.

IE jsou seskupovány dohromady, aby vytvořily kompletní protokolové zprávy. Například zpráva [RRC](/mobilnisite/slovnik/rrc/) Connection Setup obsahuje více IE, které přenášejí novou konfiguraci rádiových prostředků k UE. Podobně zpráva [GTP-C](/mobilnisite/slovnik/gtp-c/) Create Session Request obsahuje IE pro IP adresu UE, parametry QoS a kontext přenosového kanálu. Přítomnost či nepřítomnost IE a její konkrétní hodnota určují chování přijímající entity. Některé IE jsou pro danou zprávu povinné (M), zatímco jiné jsou podmíněné (C) nebo volitelné (O) v závislosti na scénáři. Tato flexibilita umožňuje protokolům podporovat širokou škálu funkcionalit a síťových konfigurací bez nutnosti vytvářet jedinečný typ zprávy pro každou možnou kombinaci parametrů.

Návrh a správa IE jsou klíčové pro vývoj protokolů. Nové funkce zaváděné v pozdějších vydáních 3GPP často vyžadují definici nových IE nebo rozšíření stávajících. Pro zachování zpětné kompatibility jsou protokoly navrženy tak, aby starší síťové uzly nebo UE mohly ignorovat IE, kterým nerozumí (pokud daná IE není pro proceduru kritická). Rozsáhlý katalog IE je dokumentován ve stovkách technických specifikací 3GPP, přičemž každá specifikace detailně popisuje IE relevantní pro konkrétní protokolovou vrstvu nebo rozhraní. Hlavní glosáře jako TS 21.905 poskytují centrální referenci pro definice IE a jejich přidružené specifikace.

## K čemu slouží

Information Element existuje, aby poskytla standardizovanou, modulární a rozšiřitelnou metodu pro kódování informací v telekomunikačních protokolech. Před takovou standardizací používaly proprietární protokoly ad-hoc datové formáty, což vedlo k závažným problémům s interoperabilitou mezi zařízeními různých výrobců. Koncept IE tento problém řeší definováním společného 'jazyka' a gramatiky pro síťovou komunikaci. Umožňuje, aby byla komplexní informace – od jednoduchých celých čísel po vnořené struktury – jednoznačně definována, přenesena a interpretována oběma konci komunikačního spojení.

Tato modularita je klíčová pro podporu rozsáhlé sady funkcí a vývojové cesty buněčných sítí. Namísto vytváření zcela nových typů zpráv pro každý nový parametr nebo funkci mohou inženýři jednoduše definovat novou IE nebo rozšířit stávající. Tento přístup udržuje základní sadu protokolových zpráv relativně stabilní, zároveň však umožňuje obrovskou flexibilitu. Například stejná zpráva [RRC](/mobilnisite/slovnik/rrc/) Connection Reconfiguration může být použita k navázání hlasového hovoru v 3G, konfiguraci agregace nosných v 4G nebo zřízení síťového řezu (network slice) v 5G, a to prostým zahrnutím různých sad IE. Odděluje účel zprávy od jejího konkrétního obsahu, což protokoly činí připravenými na budoucnost.

Dále IE umožňují efektivní a kompaktní kódování. Použitím binárních formátů a pečlivě navržených indikátorů délky minimalizují režii protokolu, což je kritické pro rádiová rozhraní, kde je přenosová kapacita vzácným zdrojem. Přísné typování a struktura také usnadňují automatizované generování kódu, testování a validaci, což snižuje implementační chyby a urychluje vývojové cykly síťového vybavení a zařízení.

## Klíčové vlastnosti

- Modulární datová struktura s definovanými komponentami Identifikátor, Délka a Hodnota (TLV nebo podobné).
- Přísně definovaná syntaxe a sémantika v rámci technických specifikací 3GPP.
- Podpora více datových typů včetně celých čísel, řetězců oktetů, výčtových seznamů a vnořených struktur.
- Podmíněná přítomnost (Povinná, Podmíněná, Volitelná) umožňující flexibilní skládání zpráv.
- Mechanismy zpětné a dopředné kompatibility (např. indikátory kritičnosti, značky rozšíření).
- Efektivní binární kódování, často s využitím ASN.1 Packed Encoding Rules (PER).

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [NG-AP – NG Application Protocol](/mobilnisite/slovnik/ng-ap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.078** (Rel-19) — CAMEL Phase 4 Stage 2 Specification
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 23.172** (Rel-19) — Service Change and UDI Fallback (SCUDIF)
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TR 23.979** (Rel-19) — PoC over 3GPP Systems Architectural Requirements
- **TS 24.161** (Rel-19) — Network-Based IP Flow Mobility (NBIFOM)
- **TS 24.171** (Rel-19) — NAS Protocol for LCS in E-UTRAN
- **TS 24.244** (Rel-19) — Wireless LAN Control Plane Protocol
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.571** (Rel-19) — Control Plane LCS Procedures
- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- … a dalších 37 specifikací

---

📖 **Anglický originál a plná specifikace:** [IE na 3GPP Explorer](https://3gpp-explorer.com/glossary/ie/)
