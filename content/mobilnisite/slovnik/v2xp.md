---
slug: "v2xp"
url: "/mobilnisite/slovnik/v2xp/"
type: "slovnik"
title: "V2XP – Vehicle-to-Everything Policy"
date: 2026-01-01
abbr: "V2XP"
fullName: "Vehicle-to-Everything Policy"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/v2xp/"
summary: "Vehicle-to-Everything Policy (V2XP) je rámec pro definování a vynucování pravidel řídících komunikační relace V2X. Určuje, jak jsou síťové prostředky přidělovány a spravovány pro služby V2X na základě"
---

V2XP je rámec pro definování a vynucování pravidel, která řídí komunikační relace V2X, určuje, jak jsou síťové prostředky přidělovány a spravovány na základě parametrů služby, aby kritické bezpečnostní zprávy obdržely potřebné zacházení.

## Popis

Vehicle-to-Everything Policy (V2XP) označuje soubor pravidel a parametrů, které řídí chování a přidělování prostředků pro komunikaci [V2X](/mobilnisite/slovnik/v2x/) v rámci sítě 3GPP. Jedná se o specializovanou podmnožinu širšího rámce Policy and Charging Control ([PCC](/mobilnisite/slovnik/pcc/)), přizpůsobenou specificky pro jedinečné požadavky služeb V2X, které často zahrnují nízkou latenci, vysokou spolehlivost a dynamická geografická omezení. Rámec V2XP je implementován a vynucován funkcí Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) v 5G jádru sítě. PCF generuje pravidla V2XP na základě vstupů od aplikačního serveru V2X (V2X [AS](/mobilnisite/slovnik/as/)), konfigurací síťového operátora a informací o účastníkovi z Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)).

Tyto politiky jsou následně doručeny příslušným síťovým funkcím a uživatelskému zařízení (UE). Pro síťovou komunikaci (Uu) jsou pravidla V2XP poskytnuta funkcím Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)), aby ovlivnily QoS toky, přeposílání paketů a správu relací. Pro přímou komunikaci přes postranní spoj PC5 jsou pravidla V2XP poskytnuta UE, aby řídila jeho chování na rozhraní postranního spoje. Klíčové parametry v rámci pravidla V2XP zahrnují [ProSe](/mobilnisite/slovnik/prose/) Per-Packet Priority (PPPP), ProSe Per-Packet Reliability (PPPR), povolené oblasti služeb V2X, maximální vysílací výkon a režimy přidělování prostředků (naplánované vs. autonomní). PCF může také poskytovat specifická pravidla Policy and Charging Control (PCC) pro V2X, která zahrnují parametry pro účtování a vynucování QoS.

Fungování V2XP zahrnuje dynamická rozhodnutí o politice. Například, když UE zahájí službu V2X, může V2X AS požadovat od PCF konkrétní politiku na základě typu služby (např. základní bezpečnost vs. pokročilá teleoperace). PCF vyhodnotí tento požadavek s ohledem na uživatelský předplatitelský profil a síťové podmínky a sestaví odpovídající V2XP. Tato politika je následně aktivována a vynucována po dobu trvání relace V2X. V2XP je klíčová pro zvládání rádiového zahlcení, zejména v hustých dopravních scénářích, tím, že upřednostňuje bezpečnostní zprávy a efektivně přiděluje prostředky postranního spoje. Poskytuje standardizovaný mechanismus pro síť, aby mohla řídit a optimalizovat komunikaci V2X, a zajišťuje tak, že různorodé a přísné požadavky různých aplikací V2X jsou v síti konzistentně naplňovány.

## K čemu slouží

V2XP byla vytvořena, aby řešila potřebu podrobné, dynamické a na službu zaměřené kontroly nad komunikací V2X v rámci politického rámce 3GPP. Rané implementace V2X, včetně počátečních specifikací Release 14, měly mechanismy politiky, ale formalizovaný rámec V2XP, zdůrazňovaný od Release 16 dále, byl hnán zavedením pokročilejších a rozmanitějších služeb eV2X. Tyto nové služby (např. formování jízdních pruhů, dálkové řízení) mají ve srovnání se základními bezpečnostními zprávami značně odlišné požadavky z hlediska latence, spolehlivosti, přenosové rychlosti a dosahu komunikace. Univerzální přístup k politice byl nedostatečný.

Rámec V2XP řeší problém, jak efektivně mapovat různorodé požadavky aplikací V2X na síťové a rádiové prostředky. Umožňuje síťovému operátorovi a poskytovateli služeb definovat politiky, které například určují, že zpráva pro zabránění kolize musí mít vyšší prioritu a nižší latenci než aktualizace V2X související s infotainmentem. To je klíčové pro správu omezeného rádiového spektra, prevenci zahlcení a zajištění, že zprávy týkající se bezpečnosti života nejsou nikdy zpožděny kvůli soupeření o síťové prostředky. V2XP také umožňuje diferenciaci služeb a jejich zpoplatnění, protože operátoři mohou nabízet různé úrovně služeb V2X s odpovídajícími garancemi politiky. Integrací politiky V2X do architektury jádra PCC zajistil 3GPP, že komunikace V2X může být řízena se stejnou robustností, bezpečností a škálovatelností jako tradiční mobilní služby.

## Klíčové vlastnosti

- Definuje parametry QoS pro toky V2X (např. PPPP, PPPR, latenci, spolehlivost)
- Řídí přidělování prostředků pro komunikační rozhraní V2X Uu i PC5
- Dynamicky poskytována funkcí PCF na základě požadavku služby a předplatného
- Zahrnuje geografická omezení, jako je autorizace oblasti služby V2X
- Integruje se s jádrovým rámcem PCC pro jednotné vynucování politiky
- Podporuje diferenciaci politiky pro různé typy služeb eV2X

## Definující specifikace

- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 24.587** (Rel-19) — V2X Services Protocols for 5G System
- **TS 24.588** (Rel-19) — UE Policies for V2X Services in 5GS
- **TR 26.941** (Rel-19) — 5G Media Slicing Extensions
- **TS 29.513** (Rel-19) — 5G PCC Signalling Flows & QoS Mapping
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3

---

📖 **Anglický originál a plná specifikace:** [V2XP na 3GPP Explorer](https://3gpp-explorer.com/glossary/v2xp/)
