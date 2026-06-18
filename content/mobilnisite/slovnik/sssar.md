---
slug: "sssar"
url: "/mobilnisite/slovnik/sssar/"
type: "slovnik"
title: "SSSAR – Service Specific Segmentation and Re-assembly sublayer"
date: 2025-01-01
abbr: "SSSAR"
fullName: "Service Specific Segmentation and Re-assembly sublayer"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sssar/"
summary: "Protokolová podsložka v uživatelské rovině rozhraní Iu, součást UMTS. Segmentuje a opětovně skládá datové jednotky služby (SDU) z vyšších vrstev (např. RLC) do paketů vhodných pro přenos podkladovou s"
---

SSSAR je podsložka pro služebně specifickou segmentaci a opětovné složení v uživatelské rovině rozhraní Iu v UMTS, která segmentuje a opětovně skládá SDU z vyšších vrstev pro efektivní přenos podkladovou sítí ATM/AAL2.

## Popis

Podsložka pro služebně specifickou segmentaci a opětovné složení (SSSAR) je protokolová entita definovaná ve standardech 3GPP pro UMTS v doméně spojového přepojování ([CS](/mobilnisite/slovnik/cs/)). Působí v zásobníku protokolů uživatelské roviny rozhraní Iu, konkrétně mezi rádiovou přístupovou sítí (RAN) a jádrem sítě (CN). Rozhraní Iu spojuje řadič rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) s ústřednou pro mobilní služby ([MSC](/mobilnisite/slovnik/msc/)) pro CS služby. Hlavní úlohou SSSAR je přizpůsobit proměnlivě nebo pevně velké datové jednotky služby ([SDU](/mobilnisite/slovnik/sdu/)) přijaté z vyšší vrstvy (typicky vrstvy řízení rádiového spoje neboli [RLC](/mobilnisite/slovnik/rlc/)) do formátu vhodného pro přenos podkladovou sítí asynchronního přenosového režimu ([ATM](/mobilnisite/slovnik/atm/)) s využitím adaptační vrstvy ATM typu 2 ([AAL2](/mobilnisite/slovnik/aal2/)).

Z architektonického hlediska se podsložka SSSAR nachází nad vrstvou AAL2 a pod uživatelskými protokoly pro konkrétní službu (např. datový proud hlasového kodeku). Poskytuje své vyšší vrstvě službu, kterou je transparentní přenos SDU. Její klíčová činnost zahrnuje dvě funkce: segmentaci a opětovné složení. Na vysílací straně (např. v RNC) podsložka SSSAR vezme SDU, což může být například hlasový rámec z kodeku [AMR](/mobilnisite/slovnik/amr/), a pokud je SDU větší než maximální povolená velikost užitečného zatížení vrstvy AAL2 CPS (Common Part Sublayer), segmentuje jej na menší pakety pevné velikosti nazývané SSSAR-PDU (protokolové datové jednotky). Každému SSSAR-PDU je přidána hlavička SSSAR. Tato hlavička obsahuje řídicí informace, jako jsou pořadová čísla pro doručení ve správném pořadí a příznaky označující začátek a konec původního SDU. Tyto SSSAR-PDU jsou poté předány vrstvě AAL2 k dalšímu zpracování a přenosu.

Na přijímací straně (např. v MSC) je proces obrácený. Podsložka SSSAR přijímá SSSAR-PDU z vrstvy AAL2. Pomocí pořadových čísel a příznaků segmentace v hlavičkách opětovně složí původní SDU. Musí zvládnout případný příchod PDU mimo pořadí a jejich ztrátu, ačkoli podkladové sítě AAL2 a ATM obvykle pro CS provoz poskytují spojení se zachováním pořadí a spolehlivé. Po opětovném složení je kompletní SDU doručeno aplikační službě vyšší vrstvy. Tento proces je „služebně specifický“, protože může být konfigurován s parametry (jako je maximální velikost PDU) přizpůsobenými požadavkům přenášené konkrétní CS služby, jako je hlas nebo spojově orientovaná data.

## K čemu slouží

Podsložka SSSAR byla vytvořena, aby vyřešila zásadní nesoulad mezi datovými jednotkami generovanými spojově orientovanými službami (jako jsou hlasové rámce) a transportním mechanismem definovaným pro rozhraní Iu v raných vydáních UMTS: ATM/AAL2. Sítě ATM jsou navrženy pro přenos buněk pevné velikosti (53bajtových ATM buněk). AAL2 bylo zavedeno pro efektivní zabalení proměnlivě dlouhých paketů citlivých na zpoždění (jako je hlas) do těchto ATM buněk za účelem minimalizace paketizačního zpoždění a efektivního využití šířky pásma.

Bez segmentační vrstvy by musel být celý hlasový rámec (např. 244bitový rámec AMR) přenášen jako jediný paket AAL2. AAL2 má však omezení velikosti paketu a efektivnější je multiplexování mnoha malých paketů od různých uživatelů do jedné ATM buňky. SSSAR umožňuje volitelnou segmentaci větších SDU z vyšších vrstev na menší jednotky, které lze optimálně zabalit do paketů AAL2. Tím se zvyšuje využití šířky pásma na nákladných spojovacích linkách mezi RNC a MSC. Poskytuje také standardizovaný mechanismus pro přijímač, aby spolehlivě rekonstruoval původní datový proud.

Před standardizovanou segmentací v uživatelské rovině mohly být používány neefektivní transportní metody nebo proprietární řešení. SSSAR poskytla standardizovanou metodu podle 3GPP, která zajišťuje interoperabilitu mezi zařízeními různých výrobců v síti UMTS. Vyřešila problém přizpůsobení přerušované povahy kódovaného hlasového provozu s proměnlivou rychlostí spojově orientovanému, na buňkách založenému ATM transportu, který byl dominantní technologií pro rozhraní jádra sítě v době návrhu UMTS R99.

## Klíčové vlastnosti

- Segmentuje SDU z vyšších vrstev na menší SSSAR-PDU pro efektivní přenos AAL2.
- Opětovně skládá SSSAR-PDU zpět na původní SDU na přijímací straně.
- Přidává ke každému PDU řídicí hlavičku obsahující pořadová čísla a příznaky segmentace.
- Poskytuje doručení ve správném pořadí a identifikaci hranic SDU pro datový proud služby.
- Působí v uživatelské rovině rozhraní Iu-CS mezi RNC a MSC.
- Konfigurace je služebně specifická, což umožňuje optimalizaci pro různé typy provozu (např. hlas).

## Související pojmy

- [AAL2 – ATM Adaptation Layer type 2](/mobilnisite/slovnik/aal2/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols

---

📖 **Anglický originál a plná specifikace:** [SSSAR na 3GPP Explorer](https://3gpp-explorer.com/glossary/sssar/)
