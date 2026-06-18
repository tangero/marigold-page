---
slug: "cgf"
url: "/mobilnisite/slovnik/cgf/"
type: "slovnik"
title: "CGF – Charging Gateway Functionality"
date: 2026-01-01
abbr: "CGF"
fullName: "Charging Gateway Functionality"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cgf/"
summary: "CGF je síťová funkce, která shromažďuje, koreluje a předává záznamy o účtovacích datech (CDR) ze síťových prvků do fakturační domény. Funguje jako brána a zajišťuje spolehlivý a standardizovaný přenos"
---

CGF je síťová funkce, která shromažďuje, koreluje a předává záznamy o účtovacích datech ze síťových prvků do fakturační domény za účelem přesného účtování služeb a účetnictví.

## Popis

Charging Gateway Functionality (CGF) je klíčová součást architektury účtování 3GPP, konkrétně definovaná pro offline účtování. Funguje jako prostředník mezi síťovými prvky, které generují účtovací události, a fakturačním systémem (nebo fakturační doménou). Síťové prvky, jako jsou [SGSN](/mobilnisite/slovnik/sgsn/), GGSN, [P-GW](/mobilnisite/slovnik/p-gw/) nebo [S-GW](/mobilnisite/slovnik/s-gw/), generují nezpracovaná účtovací data ve formě záznamů o účtovacích datech ([CDR](/mobilnisite/slovnik/cdr/)) nebo jejich částí. Tyto prvky odesílají tato data na CGF pomocí standardizovaných rozhraní, primárně referenčního bodu Ga. Primární technickou rolí CGF je fungovat jako koncentrátor a mediátor. Přijímá tyto CDR, provádí korelaci, pokud více dílčích záznamů patří k jedné servisní relaci (např. korelace záznamů ze SGSN a GGSN pro jeden [PDP](/mobilnisite/slovnik/pdp/) kontext), a skládá je do kompletních, ověřených CDR. Také ukládá záznamy do vyrovnávací paměti, aby zajistila spolehlivé doručení, řeší chyby a opakované přenosy a předává konsolidované soubory CDR do fakturačního systému prostřednictvím referenčního bodu Bx, obvykle za použití protokolů jako [FTP](/mobilnisite/slovnik/ftp/) nebo FTPS.

Architektonicky může být CGF implementována jako samostatný síťový uzel nebo integrována s dalšími účtovacími funkcemi. V raných vydáních 3GPP to byla samostatná logická funkce. Její vnitřní komponenty zahrnují rozhraní pro Ga a Bx, procesní a korelační engine pro CDR, trvalé úložiště pro vyrovnávací paměť a řídicí funkce pro sledování jejího výkonu a zatížení. CGF zajišťuje integritu a posloupnost dat, což je zásadní pro přesné účtování. Může také provádět konverzi formátu, převádějící CDR z formátu kódovaného v ASN.1 používaného přes Ga do formátu vhodného pro fakturační doménu, jako je soubor s hodnotami oddělenými čárkami ([CSV](/mobilnisite/slovnik/csv/)) nebo specifický proprietární formát.

Provoz CGF je klíčový pro paradigma offline účtování, kde se informace o účtování shromažďují až po poskytnutí služby. Poskytuje síti jediný sběrný bod, což zjednodušuje integraci fakturačního systému. Tím, že řeší spolehlivost a korelaci, chrání fakturační doménu před složitostmi a potenciálními nestabilitami síťových prvků v reálném čase. Toto oddělení odpovědností umožňuje síťovým prvkům soustředit se na poskytování služeb, zatímco CGF spravuje logistiku účtovacích dat. V moderních sítích, zejména se zavedením 5G a Charging Function ([CHF](/mobilnisite/slovnik/chf/)), jsou principy CGF vtěleny do Charging Trigger Function (CTF) a Charging Data Function (CDF) pro offline účtování, ale koncept CGF jako samostatné brány zůstává základním pro legacy a konvergentní fakturační systémy.

## K čemu slouží

CGF byla vytvořena, aby řešila rostoucí složitost účtování v mobilních paketových sítích zavedených s GPRS a 3G. Před její standardizací čelili síťoví operátoři významným výzvám při spolehlivém shromažďování údajů o využití z více distribuovaných síťových prvků (jako jsou SGSN a GGSN). Tyto prvky mohly generovat obrovská množství účtovacích dat a přímé, bod-bod spojení z každého prvku do fakturačního systému bylo neefektivní, nespolehlivé a obtížně škálovatelné. Fakturační systémy nebyly navrženy tak, aby zvládly potenciální ztrátu dat, zahlcení sítě nebo potřebu korelace záznamů z různých uzlů. CGF tento problém vyřešila zavedením specializované bránové funkce.

K jejímu vytvoření vedla potřeba standardizovaného, robustního a škálovatelného prostředníka. CGF centralizuje sběrný bod, což umožňuje síťovým prvkům odesílat data na blízkou nebo logicky centralizovanou bránu pomocí odlehčeného protokolu (jako GTP' přes Ga). Tím se snižuje zatížení a složitost spojení na samotném fakturačním systému. Řeší problém spolehlivosti dat prostřednictvím mechanismů vyrovnávací paměti a opakovaného přenosu, čímž zajišťuje, že se žádná účtovací data neztratí kvůli dočasným výpadkům sítě nebo fakturačního systému. Dále řeší kritický problém korelace. Jedna uživatelská relace (jako prohlížení webu) často zahrnuje více síťových uzlů; CGF koreluje dílčí CDR z těchto uzlů do jediného souvislého záznamu, který přesně reprezentuje celé využití služby, což je nezbytné pro správné účtování.

Historicky CGF umožnila komerční životaschopnost datových služeb tím, že poskytla spolehlivý mechanismus pro zpeněžení využití paketových dat. Oddělila přenos a mediaci účtovacích dat od samotné fakturační logiky, což umožnilo oběma doménám (síťové a systémy obchodní podpory) se vyvíjet nezávisle. Toto architektonické rozhodnutí zajistilo budoucí odolnost účtovací infrastruktury, podpořilo explozi datových služeb od 2.5G až po 4G a vytvořilo konceptuální základ pro účtování v systémech 5G.

## Klíčové vlastnosti

- Shromažďování a koncentrace CDR přes rozhraní Ga
- Korelace a skládání CDR z více síťových prvků
- Spolehlivé ukládání do vyrovnávací paměti a předávání s mechanismy opakování
- Mediace protokolů mezi GTP' a protokoly fakturačního systému (např. FTP)
- Standardizované rozhraní (Bx) k fakturační doméně
- Podpora zpracování vysokých objemů dat s tolerancí k poruchám

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 23.815** (Rel-5) — IMS Charging Implications
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 28.201** (Rel-19) — 5G Network Slice Performance Analytics Charging
- **TS 28.203** (Rel-18) — Charging management
- **TS 28.204** (Rel-18) — Charging management
- **TS 28.702** (Rel-19) — Core Network NRM IRP Information Service
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.253** (Rel-19) — Charging for Control Plane Data Transfer
- **TS 32.254** (Rel-19) — Charging for Northbound APIs
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [CGF na 3GPP Explorer](https://3gpp-explorer.com/glossary/cgf/)
