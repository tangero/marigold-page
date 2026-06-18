---
slug: "lwaap"
url: "/mobilnisite/slovnik/lwaap/"
type: "slovnik"
title: "LWAAP – LTE-WLAN Aggregation Adaptation Protocol"
date: 2025-01-01
abbr: "LWAAP"
fullName: "LTE-WLAN Aggregation Adaptation Protocol"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lwaap/"
summary: "LWAAP je protokolová vrstva v agregaci LTE-WLAN (LWA), která adaptuje PDCP PDU pro přenos přes WLAN spojení. Umožňuje eNB rozdělovat a směrovat datový provoz uživatele současně přes rádiové přenašeče"
---

LWAAP je vrstva protokolu pro adaptaci agregace LTE-WLAN (LTE-WLAN Aggregation Adaptation Protocol), která adaptuje pakety PDCP pro přenos přes WLAN za účelem umožnění rozdělování dat přes rádiové přenašeče LTE a WLAN.

## Popis

Protokol pro adaptaci agregace LTE-WLAN (LTE-WLAN Aggregation Adaptation Protocol, LWAAP) je klíčová protokolová vrstva definovaná v architektuře 3GPP pro agregaci LTE-WLAN ([LWA](/mobilnisite/slovnik/lwa/)), zavedená ve vydání 13. Funguje jako podvrstva v eNodeB ([eNB](/mobilnisite/slovnik/enb/)) a je zodpovědná za adaptaci datových jednotek protokolu [PDCP](/mobilnisite/slovnik/pdcp/) (PDCP [PDU](/mobilnisite/slovnik/pdu/)) pro přenos přes důvěryhodnou přístupovou síť [WLAN](/mobilnisite/slovnik/wlan/). Vrstva LWAAP přidává k PDCP PDU malou hlavičku, která obsahuje nezbytné informace, jako je identita přenašeče a pořadové číslo. Tato adaptace je nutná, protože WLAN spojení nativně nepodporuje mechanismy QoS a správy přenašečů rozhraní LTE rádiového rozhraní; hlavička LWAAP umožňuje přijímající entitě, [WT](/mobilnisite/slovnik/wt/) (WLAN Termination), správně znovu sestavit a přeposlat data, čímž zachovává integritu a pořadí datového toku spojeného s konkrétním EPS přenašečem.

Architektonicky se LWAAP nachází mezi vrstvou PDCP a spodními vrstvami zodpovědnými za přenos přes rozhraní Xw (rozhraní mezi eNB a WT). eNB, fungující jako vysílající entita LWAAP, provádí rozhodnutí o rozdělování dat na vrstvě PDCP. Pro přenašeče nakonfigurované pro LWA může eNB směrovat některá PDCP PDU přímo přes rádiové rozhraní LTE-Uu a jiná do vrstvy LWAAP. Vrstva LWAAP pak tato PDCP PDU zpracuje, zapouzdří je pomocí hlavičky LWAAP a přepošle je přes protokolový zásobník uživatelské roviny Xw (typicky přes [GTP-U](/mobilnisite/slovnik/gtp-u/)/[UDP](/mobilnisite/slovnik/udp/)/IP) k WT. WT po přijetí odstraní hlavičku LWAAP a doručí původní PDCP PDU WLAN modemu pro přenos k UE přes IEEE 802.11 spojení.

Návrh protokolu zajišťuje bezproblémovou agregaci z pohledu UE. UE přijímá PDCP PDU z obou rádiových spojení a doručuje je své jediné entitě PDCP pro přerovnání a doručení ve správném pořadí vyšším vrstvám. Tento proces je transparentní pro core network, protože rozhraní S1-U zůstává ukončeno v eNB. Klíčovými zapojenými komponentami jsou entita LWAAP v eNB, odpovídající entita v WT a signalizace řídicí roviny přes rozhraní Xw-C pro zřizování a správu LWA přenašečů. Role LWAAP je zásadní pro dosažení výhod LWA, protože umožňuje operátorům zvýšit kapacitu a uživatelský komfort využitím WLAN jako komplementárního rádiového zdroje pod přísnou kontrolou sítě LTE.

## K čemu slouží

LWAAP byl vytvořen jako odpověď na rostoucí poptávku po vyšších přenosových rychlostech a lepším uživatelském komfortu v mobilních sítích, zejména v hustě obydlených městských oblastech a vnitřních prostorech, kde je WLAN široce dostupné. Před integrací v rámci 3GPP fungovaly LTE a WLAN nezávisle, s řešeními jako ANDSF (Access Network Discovery and Selection Function) poskytujícími řízení založené na politikách, což bylo pomalé a reaktivní. To vedlo k neefektivnímu využití obou sítí, protože UE mohlo být pro daný IP tok připojeno vždy pouze k jedné z nich a core network nemohl zdroj WLAN přímo spravovat.

Hlavním problémem, který LWAAP řeší, je umožnění síti LTE využívat WLAN jako bezproblémovou, agregovanou datovou trubici na rádiové úrovni. Umožňuje eNB provádět plánování a rozdělování provozu v reálném čase a na úrovni jednotlivých paketů, což nebylo možné s dřívějšími technikami odlehčování. Tato těsná integrace řeší omezení volného propojení tím, že poskytuje lepší mobilní výkon, vylepšenou podporu QoS a efektivnější využití rádiových zdrojů. Motivací bylo vytvořit standardizovanou, operátorem řízenou metodu pro využití nelicencovaného spektra (Wi-Fi) k rozšíření kapacity licencovaného LTE, čímž se zlepší propustnost a efektivita sítě bez nutnosti změn v core networku nebo IP vrstvě UE.

## Klíčové vlastnosti

- Adaptuje PDCP PDU pro přenos přes WLAN přidáním hlavičky LWAAP
- Podporuje identifikaci specifickou pro přenašeč prostřednictvím Logical Channel ID v hlavičce
- Obsahuje pořadová čísla pro pomoc s doručováním ve správném pořadí přes WLAN spojení
- Umožňuje rozdělování a agregaci na úrovni jednotlivých paketů řízené eNB
- Funguje transparentně vůči core networku (S1-U ukončeno v eNB)
- Pracuje s nasazovacími scénáři WT jak spolokalizovanými, tak nespolokalizovanými

## Související pojmy

- [LWA – LTE-WLAN Radio Level Aggregation](/mobilnisite/slovnik/lwa/)
- [LWIP – LTE WLAN Radio Level Integration with IPsec Tunnel](/mobilnisite/slovnik/lwip/)
- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [WT – WLAN Termination](/mobilnisite/slovnik/wt/)
- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.360** (Rel-19) — LTE-WLAN Aggregation Adaptation Protocol

---

📖 **Anglický originál a plná specifikace:** [LWAAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lwaap/)
