---
slug: "pl"
url: "/mobilnisite/slovnik/pl/"
type: "slovnik"
title: "PL – Puncturing Limit"
date: 2025-01-01
abbr: "PL"
fullName: "Puncturing Limit"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pl/"
summary: "Parametr pro uplink, který definuje maximální povolené propírání transportních kanálů. Signalizuje se z vyšších vrstev do fyzické vrstvy za účelem řízení procesu přizpůsobení přenosové rychlosti, čímž"
---

PL je parametr, který definuje maximální povolené propírání (puncturing) transportních kanálů v uplinku. Signalizuje se z vyšších vrstev a slouží k řízení přizpůsobení přenosové rychlosti (rate matching) a k vyvážení spektrální účinnosti s přenosovou spolehlivostí.

## Popis

Limit propírání (Puncturing Limit, PL) je klíčový parametr v procesu přizpůsobení přenosové rychlosti (rate matching) v uplinku v systémech 3GPP UMTS a LTE. Přizpůsobení přenosové rychlosti je procedura, která upravuje počet bitů z transportních kanálů tak, aby odpovídaly dostupné kapacitě fyzického kanálu. To zahrnuje buď opakování bitů (pro zvýšení redundance), nebo jejich propírání (odstranění) k dosažení požadované datové rychlosti. PL konkrétně omezuje maximální množství propírání, které lze aplikovat na daný transportní kanál. Jde o bezrozměrnou hodnotu, typicky vyjádřenou jako limit poměru propírání, která je signalizována z vyšších vrstev (např. z [RRC](/mobilnisite/slovnik/rrc/) vrstvy) do fyzické vrstvy prostřednictvím indikátorů kombinace transportního formátu.

PL funguje v rámci řetězce kanálového kódování a multiplexování. Po kanálovém kódování (např. konvolučním nebo turbokódování) jsou zakódované bity podrobeny přizpůsobení přenosové rychlosti. Algoritmus vypočítá potřebný počet bitů k přenosu. Pokud počet zakódovaných bitů překročí kapacitu fyzického kanálu, je aplikováno propírání. PL slouží jako pojistka, která brání nadměrnému propírání, jež by kriticky snížilo schopnost kódu opravovat chyby, a tím udržuje minimální úroveň výkonu spoje. Hodnota je zohledňována při výběru kombinace transportního formátu ([TFC](/mobilnisite/slovnik/tfc/)), což zajišťuje, že zvolená kombinace neporušuje limit propírání.

Jeho role je nedílnou součástí řízení výkonu v uplinku a správy kvality služeb (QoS). Tím, že omezuje propírání, PL nepřímo ovlivňuje spektrální hustotu vysílaného výkonu. Nadměrné propírání by vyžadovalo vyšší výkon pro udržení stejné chybovosti bloků ([BLER](/mobilnisite/slovnik/bler/)), což je neefektivní. PL proto pomáhá udržovat stabilní a předvídatelný výkon spoje, což je zásadní pro služby s přísnými požadavky na chybovost. Je klíčovou součástí algoritmů správy rádiových zdrojů, které vyvažují datovou propustnost, vysílací výkon a kvalitu signálu.

## K čemu slouží

Limit propírání byl zaveden, aby řešil výzvu efektivního využití zdrojů v uplinku při současném zaručení přenosové spolehlivosti. V raných verzích UMTS bylo dynamické přizpůsobení přenosové rychlosti zásadní pro podporu služeb s proměnnou datovou rychlostí na vyhrazených kanálech. Bez limitu propírání by teoreticky mohl algoritmus přizpůsobení přenosové rychlosti propírat velmi vysoké procento zakódovaných bitů, aby se vešly do malého slotu fyzického kanálu. To by vážně narušilo zisk z kódování, vedlo k vysoké chybovosti bloků a vyžadovalo nadměrné retransmise nebo zvýšený vysílací výkon, což jsou obojí neefektivní přístupy.

PL tento problém řeší tím, že poskytuje řízený kompromis. Umožňuje síti vynutit politiku minimálního kódového poměru, čímž zajišťuje, že vnitřní schopnost kanálového kódu opravovat chyby není narušena za prakticky únosnou mez. To je obzvláště důležité pro služby s vysokými nároky na spolehlivost, jako je signalizace nebo hlas přes [HSPA](/mobilnisite/slovnik/hspa/). Jeho zavedení umožnilo robustnější a předvídatelnější výkon v uplinku a vytvořilo základní část rámce adaptace spoje. Umožňuje systému optimalizovat spektrální účinnost bez rizika nepřijatelného zhoršení kvality spoje, což je klíčový požadavek pro podporu různorodých profilů QoS v sítích 3G a 4G.

## Klíčové vlastnosti

- Definuje maximální povolený poměr propírání pro transportní kanály v uplinku
- Signalizován z vyšší RRC vrstvy do fyzické vrstvy
- Nedílná součást procesů přizpůsobení přenosové rychlosti (rate matching) a výběru TFC v uplinku
- Chrání schopnost kanálových kódů opravovat chyby
- Podporuje stabilitu řízení výkonu v uplinku
- Umožňuje správu rádiových zdrojů s ohledem na QoS

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.346** (Rel-19) — MBMS in UTRA Technical Specification
- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report
- **TR 25.996** (Rel-19) — 3GPP-3GPP2 Spatial Channel Model Specification
- **TR 26.935** (Rel-19) — Speech Codec Performance for Packet Switched Multimedia
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- … a dalších 4 specifikací

---

📖 **Anglický originál a plná specifikace:** [PL na 3GPP Explorer](https://3gpp-explorer.com/glossary/pl/)
