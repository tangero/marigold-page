---
slug: "bc"
url: "/mobilnisite/slovnik/bc/"
type: "slovnik"
title: "BC – Backward Compatibility"
date: 2025-01-01
abbr: "BC"
fullName: "Backward Compatibility"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bc/"
summary: "Zpětná kompatibilita (BC) je základní konstrukční princip v 3GPP, který zajišťuje, že novější síťové verze, zařízení a funkce mohou spolupracovat se staršími systémy. Zabránuje fragmentaci sítě a chrá"
---

BC je konstrukční princip 3GPP zajišťující, že novější síťové verze a zařízení mohou spolupracovat se staršími systémy, což umožňuje postupný, nerušící přechod od starších technologií k novějším, jako je 5G.

## Popis

Zpětná kompatibilita v 3GPP je mnohostranné konstrukční omezení i faktor umožňující pokrok, který prostupuje všechny vrstvy systémové architektury, od rádiového rozhraní po protokoly jádra sítě a služební platformy. Není to jediný protokol nebo rozhraní, ale řídící princip uplatňovaný při specifikaci nových verzí standardů. Technicky zajišťuje, že uživatelské zařízení (UE) vyhovující pozdější verzi 3GPP se stále může připojit k síti pracující s dřívější verzí, a naopak, že síť nasazující nové funkce může stále obsluhovat starší UE, aniž by došlo k výpadku služeb. Toho je dosaženo pečlivou specifikací záložních mechanismů, vyjednávání verzí a příznaků označujících funkce v signalizaci řídicí roviny.

Na úrovni rádiové přístupové sítě (RAN) je zpětná kompatibilita implementována prostřednictvím návrhu kanálů a signalizačních procedur. Například při přechodu z LTE na 5G NR vyžadovaly počáteční nasazení (nestandalone architektura), aby NR koexistovalo s kotvícími buňkami LTE. Systém LTE vysílá hlavní informační bloky ([MIB](/mobilnisite/slovnik/mib/)) a systémové informační bloky ([SIB](/mobilnisite/slovnik/sib/)), které jsou dekódovatelné staršími UE, zatímco pro UE schopná NR jsou zavedeny nové SIB nebo informační elementy. Struktura rámců fyzické vrstvy, referenční signály a synchronizační signály jsou navrženy tak, aby se starší UE mohlo připojit k buňce, přečíst její základní systémové informace a navázat spojení, i když nemůže využívat nová pásma pro agregaci nosných nebo funkce masivního [MIMO](/mobilnisite/slovnik/mimo/) zavedené v pozdějších verzích.

V jádru sítě je zpětná kompatibilita řízena prostřednictvím verzování protokolů a vyjednávání na rozhraních jako N1, [N2](/mobilnisite/slovnik/n2/) a N4. Například během registrační procedury v 5G si funkce pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a UE vyměňují informace o podporovaných funkcích a možnostech síťového řezání. Pokud se starší 5G UE (z Rel-15) zaregistruje v síti upgradované na Rel-16, AMF rozpozná sadu schopností UE a omezí svou nabídku služeb na funkce, kterým UE rozumí, například se zdrží použití vylepených funkcí ultra-spolehlivé nízkolatenční komunikace (eURLLC) definovaných v Rel-16. Podobně jsou specifikovány funkce pro vzájemnou spolupráci ([IWF](/mobilnisite/slovnik/iwf/)), které umožňují plynulou mobilitu a kontinuitu relace mezi 4G EPC a 5G jádrem (5GC), a zajišťují, že předání spojení z 5G na 4G nepřeruší hovor nebo datovou relaci.

Role zpětné kompatibility se rozšiřuje na služby a správu sítě. Servisně orientované architektury ([SBA](/mobilnisite/slovnik/sba/)) v 5GC používají [HTTP](/mobilnisite/slovnik/http/)/2 s datovou částí JSON nebo Protobuf; definice API jsou verzované, což umožňuje novým síťovým funkcím (NF) komunikovat se staršími dodržováním společného základního protokolu. V systémech správy se datové modely pro správu výkonu (PM) a správu poruch (FM) vyvíjejí při zachování schopnosti sbírat klíčové ukazatele výkonu (KPI) z dřívějších verzí síťových prvků. Tento komplexní přístup zajišťuje, že celý ekosystém – zařízení, rádiové uzly, funkce jádra sítě a systémy provozní podpory – se může vyvíjet různým tempem, aniž by se narušila interoperabilita, což je nezbytné pro více než desetiletý životní cyklus telekomunikační infrastruktury.

## K čemu slouží

Hlavním účelem požadavku na zpětnou kompatibilitu ve standardech 3GPP je ekonomický a provozní. Telekomunikační sítě představují pro operátory obrovské kapitálové investice a infrastruktura se očekává v provozu po dobu 10–20 let. Absence zpětné kompatibility by si vynutila 'výměnu naráz' – kompletní, současnou výměnu všech síťových prvků a uživatelských zařízení – což je finančně neúnosné a provozně katastrofické. Také by fragmentovala globální trh, zabránila zařízením z jedné oblasti pracovat v jiné a zničila užitečnost globálního roamingu. Zpětná kompatibilita umožňuje elegantní, fázovanou migraci, při které lze zavádět nová spektra, nové funkce a nové síťové řezy, zatímco starší služby pro hlas a základní data pokračují bez přerušení.

Historicky se potřeba zpětné kompatibility jasně ukázala při přechodu z 2G GSM na 3G UMTS. I když nebyly plně zpětně kompatibilní na rádiové úrovni (jiná rádiová rozhraní), vývoj jádra sítě použil jádro GPRS jako kotvu pro obě a byly vyvinuty dvou režimová zařízení. Tato zkušenost ovlivnila přísnější požadavky pro 4G LTE a 5G NR. LTE bylo navrženo jako zpětně kompatibilní se systémy 3GPP 3G prostřednictvím robustních procedur mobility mezi RAT a společného vývoje paketového jádra (EPC). Pro 5G byl tento princip povýšen s explicitním konstrukčním cílem dopředné a zpětné kompatibility, což zajišťuje, že 5G NR může být nasazeno v existujícím spektru LTE (prostřednictvím dynamického sdílení spektra) a že 5GC může spolupracovat s EPC.

Řeší kritické technické problémy, jako je kontinuita služeb během předání spojení, návrat pro kritické služby jako tísňová volání a efektivní přerozdělování spektra. Bez BC by operátor nemohl přerozdělit 3G pásmo pro použití 4G nebo 5G a zároveň stále podporovat zbývající populaci zařízení pouze pro 3G (např. IoT senzory nebo starší telefony). Řeší omezení přístupů 'od čistého stolu', které jsou sice technicky elegantní, ale v praktické realitě nasazené infrastruktury selhávají. Zpětná kompatibilita je technický kompromis, který vyvažuje inovace s praktickými omezeními globálně nasazeného heterogenního ekosystému, a zajišťuje, že technologický pokrok neopustí stávající uživatele ani nevytvoří nepřekonatelné bariéry vstupu pro nové operátory.

## Klíčové vlastnosti

- Zajišťuje, že UE nové verze se může připojit a pracovat v sítích starší verze.
- Umožňuje starším UE přístup k sítím, které byly upgradovány novými funkcemi, typicky se sníženými schopnostmi služeb.
- Umožňuje mobilitu a předání spojení mezi různými RAT a generacemi (např. 5G na 4G, 4G na 3G) bez přerušení relací.
- Podporuje přerozdělování a koexistenci spektra (např. Dynamické sdílení spektra mezi 4G LTE a 5G NR).
- Ukládá vyjednávání verzí a výměnu informací o schopnostech v protokolech řídicí roviny (NAS, RRC, HTTP/2 NFs).
- Poskytuje rámec pro zastarávání starých funkcí v průběhu více verzí při zachování provozuschopných sítí.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.867** (Rel-18) — Study on 5G Smart Energy and Infrastructure
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.050** (R99) — UMTS Network Principles and Architecture
- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2
- **TS 23.172** (Rel-19) — Service Change and UDI Fallback (SCUDIF)
- **TS 23.202** (Rel-19) — CS Bearer Services Architecture in UMTS
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 32.154** (Rel-19) — Backward Compatibility for 3GPP IRP Specifications
- **TS 37.104** (Rel-19) — MSR Base Station RF Characteristics
- **TS 37.105** (Rel-19) — AAS Base Station Transmission & Reception Requirements
- **TS 37.113** (Rel-19) — EMC Requirements for Multi-Standard Radio Base Stations
- **TS 37.141** (Rel-19) — RF Test Methods for Multi-Standard Radio Base Stations
- **TS 37.145** (Rel-19) — AAS Base Station Conducted Conformance Testing
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [BC na 3GPP Explorer](https://3gpp-explorer.com/glossary/bc/)
