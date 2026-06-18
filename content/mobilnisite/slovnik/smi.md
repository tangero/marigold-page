---
slug: "smi"
url: "/mobilnisite/slovnik/smi/"
type: "slovnik"
title: "SMI – Structure of Management Information"
date: 2025-01-01
abbr: "SMI"
fullName: "Structure of Management Information"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/smi/"
summary: "Rámec pro definici spravovaných objektů v systému správy sítě, standardizovaný IETF v RFC 1155 a přijatý 3GPP. Poskytuje hierarchickou strukturu pojmenování a datové typy pro reprezentaci síťových prv"
---

SMI je standardizovaný rámec pro definici spravovaných objektů v systému správy sítě, který poskytuje hierarchickou strukturu pojmenování a datové typy pro umožnění standardizované správy síťových prvků.

## Popis

Struktura informací pro správu (SMI) je základní rámec používaný v systémech správy sítí, zejména těch založených na protokolu [SNMP](/mobilnisite/slovnik/snmp/) (Simple Network Management Protocol). Definuje pravidla pro popis, pojmenování a organizaci spravovaných objektů, které reprezentují síťové prostředky, jako jsou rozhraní, protokoly nebo hardwarové komponenty. SMI používá hierarchickou stromovou strukturu známou jako strom [MIB](/mobilnisite/slovnik/mib/) (Management Information Base), kde je každý objekt jednoznačně identifikován identifikátorem objektu ([OID](/mobilnisite/slovnik/oid/)). Tento OID je posloupnost celých čísel, která sleduje cestu od kořene stromu ke konkrétnímu objektu, čímž zajišťuje globální jedinečnost. Rámec také specifikuje sadu základních datových typů (jako INTEGER, OCTET STRING nebo Counter32) a složitějších konstruovaných typů (jako SEQUENCE) pro modelování atributů a stavů spravovaných entit.

V sítích 3GPP je SMI přijato pro usnadnění správy telekomunikačních zařízení a služeb. Tvoří základ pro definici standardizovaných MIB modulů pro síťové prvky specifické pro 3GPP, jako jsou NodeB, eNodeB, gNB a funkce jádra sítě. Použitím SMI zajišťuje 3GPP, že informace pro správu od různých výrobců mohou být systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)) nebo systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)) přistupovány a interpretovány konzistentně. To je klíčové pro úkoly provozu, správy a údržby ([OAM](/mobilnisite/slovnik/oam/)), včetně správy poruch, konfigurace, monitorování výkonu a správy zabezpečení. Rámec SMI umožňuje vytváření MIB modulů, které definují objekty pro sledování klíčových ukazatelů výkonu ([KPI](/mobilnisite/slovnik/kpi/)), konfiguraci parametrů a přijímání notifikací (trapů) o síťových událostech.

Architektura správy založené na SMI zahrnuje několik klíčových komponent. Spravované zařízení (např. základnová stanice) hostuje SNMP agenta, který udržuje lokální MIB, což je kolekce spravovaných objektů definovaných podle pravidel SMI. Stanice správy sítě (NMS) funguje jako SNMP manažer, komunikuje s agenty pro získání (GET) nebo změnu ([SET](/mobilnisite/slovnik/set/)) hodnot objektů. SMI definuje syntaxi a sémantiku těchto objektů pomocí maker ASN.1 (Abstract Syntax Notation One), čímž zajišťuje, že data jsou pro přenos kódována nezávisle na platformě. V 3GPP je SMI odkazováno ve specifikacích jako 32.102 pro architekturu správy a 32.622 pro správu výkonu, čímž poskytuje základ pro interoperabilní rozhraní správy. Jeho role přesahuje SNMP, protože principy strukturovaných informací pro správu ovlivňují další protokoly a datové modely používané v 3GPP, což přispívá k automatizovaným a efektivním síťovým operacím.

## K čemu slouží

SMI bylo vytvořeno, aby řešilo výzvu správy heterogenních síťových zařízení od více výrobců standardizovaným způsobem. Před jeho přijetím byla správa sítě často proprietární, vyžadující vlastní nástroje a rozhraní pro každý typ zařízení, což vedlo k vysoké provozní složitosti a nákladům. IETF vyvinulo SMI jako součást rámce SNMP, aby poskytlo společný jazyk pro popis spravovaných objektů, což umožnilo interoperabilitu a zjednodušilo správu sítě. Definováním konzistentní struktury pro informace o správě umožňuje SMI síťovým operátorům používat obecné systémy správy pro monitorování a řízení různorodých síťových prvků, od směrovačů po telekomunikační infrastrukturu.

V kontextu 3GPP bylo přijetí SMI motivováno potřebou jednotné správy napříč vyvíjejícími se mobilními sítěmi, od 3G UMTS přes 4G LTE až po 5G NR. Jak sítě rostly v měřítku a složitosti a zahrnovaly zařízení od různých dodavatelů, se standardizovaný rámec správy stal nezbytným pro efektivní OAM. SMI poskytuje základní pravidla pro vytváření MIB modulů specifických pro 3GPP, což zajišťuje konzistentní definici dat pro správu pro prvky rádiové přístupové sítě (RAN) a jádra sítě. To podporuje kritické funkce, jako je měření výkonu, detekce poruch a správa konfigurace, které jsou zásadní pro udržení kvality a spolehlivosti služeb. Zatímco se objevily novější technologie správy, jako je NETCONF/YANG, SMI zůstává v 3GPP relevantní pro scénáře správy založené na SNMP, zejména v legacy systémech a určitých aplikacích monitorování výkonu.

## Klíčové vlastnosti

- Hierarchické pojmenování objektů pomocí identifikátorů objektů (OID)
- Definice základních a konstruovaných datových typů pro spravované objekty
- Použití maker ASN.1 pro definici syntaxe
- Podpora pro vytváření standardizovaných MIB modulů
- Umožňuje interoperabilitu v síťové správě založené na SNMP
- Usnadňuje konzistentní reprezentaci síťových prostředků

## Související pojmy

- [SNMP – Simple Network Management Protocol](/mobilnisite/slovnik/snmp/)
- [MIB – Management Information Base](/mobilnisite/slovnik/mib/)
- [OID – Organisation Identifier](/mobilnisite/slovnik/oid/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.622** (Rel-11) — Generic Network Resources IRP NRM

---

📖 **Anglický originál a plná specifikace:** [SMI na 3GPP Explorer](https://3gpp-explorer.com/glossary/smi/)
