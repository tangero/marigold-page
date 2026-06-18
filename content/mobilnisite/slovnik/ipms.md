---
slug: "ipms"
url: "/mobilnisite/slovnik/ipms/"
type: "slovnik"
title: "IPMS – IP Mobility management Selection"
date: 2025-01-01
abbr: "IPMS"
fullName: "IP Mobility management Selection"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ipms/"
summary: "IPMS je síťová funkce, která na základě provozovatelských politik a schopností uživatelského zařízení (UE) vybere vhodný protokol pro správu IP mobility (např. DSMIPv6, PMIPv6). Zajišťuje bezproblémov"
---

IPMS je síťová funkce, která na základě provozovatelských politik a schopností uživatelského zařízení (UE) vybere vhodný protokol pro správu IP mobility, aby zajistila bezproblémovou kontinuitu IP relace při přechodu mezi různými přístupovými sítěmi.

## Popis

IP Mobility management Selection (IPMS, výběr správy IP mobility) je kritická rozhodovací funkce v architektuře 3GPP Evolved Packet Core (EPC), konkrétně definovaná pro scénáře mobility mezi 3GPP a důvěryhodnými či nedůvěryhodnými ne-3GPP přístupovými sítěmi. Jejím hlavním úkolem je určit pro uživatelské zařízení (UE) nejvhodnější protokol pro správu IP mobility k zachování kontinuity relace. Tento výběr není libovolný; řídí se kombinací statických provozovatelských politik nastavených v síti a dynamických informací, jako jsou hlášené schopnosti UE a typ přístupové sítě, kterou UE právě používá nebo se k ní pokouší připojit. Funkce IPMS se typicky nachází v rámci síťové architektury pro řízení politik, často je spojena s funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo s vyhrazenou výběrovou funkcí, která vyhodnocuje vstupní parametry vůči sadě předdefinovaných pravidel.

Operační postup IPMS je spuštěn během klíčových událostí mobility, jako je počáteční připojení, procedury předání služby (handover) nebo když se UE registruje přes nový typ přístupu. Proces začíná tím, že síťový uzel (např. Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) nebo síťová brána) obdrží žádost UE o připojení, která obsahuje indikátory podporovaných protokolů mobility (např. podporu klienta Dual-Stack Mobile IPv6 (DSMIPv6) nebo podporu síťové mobility jako Proxy Mobile IPv6 (PMIPv6)). Současně funkce IPMS konzultuje profil účastníka a provozovatelské politiky, které jsou přednastaveny tak, aby odrážely strategické preference sítě – například upřednostňování síťové mobility za účelem snížení složitosti UE a spotřeby baterie, nebo vyžadování klientovské mobility pro určité typy služeb nebo roamingové dohody.

Na základě tohoto vyhodnocení IPMS vydá rozhodnutí o vazbě (binding decision), které příslušným síťovým entitám – primárně bráně Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v EPC nebo odpovídající bráně v ne-3GPP přístupu – určí, který mechanismus mobility se má pro IP relaci daného UE nastavit. Například, pokud to politika určuje a UE to podporuje, síť může vytvořit tunel PMIPv6 mezi Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a PGW, nebo tunel DSMIPv6 přímo z UE na Home Agent ([HA](/mobilnisite/slovnik/ha/)). Toto rozhodnutí přímo ovlivňuje architekturu datové cesty a signalizační procedury pro následná předání služby. Centralizací této logiky poskytuje IPMS flexibilní a politikami řízený rámec, který operátorům umožňuje efektivně nasazovat heterogenní sítě, spravovat různých generací UE a optimalizovat síťové zdroje a výkon bez nutnosti změn na každém jednotlivém UE.

## K čemu slouží

IPMS byl zaveden, aby řešil rostoucí složitost mobilních sítí vyvíjejících se mimo čistě 3GPP rádiový přístup. Se začleněním Wi-Fi (jako důvěryhodného či nedůvěryhodného ne-3GPP přístupu) a později dalších rádiových technologií do systémové architektury 3GPP byl potřebný standardizovaný mechanismus pro správu toho, jak je IP relace UE udržována napříč těmito heterogenními typy přístupu. Před jeho specifikací byla správa mobility z velké části implicitní nebo vázaná na jediný protokol, což bylo nedostatečné pro prostředí s více přístupy, kde různá UE mají rozdílné schopnosti a kde operátoři mohou mít pro různé scénáře (např. domácí síť vs. roaming) různé strategické nebo technické preference.

Vytvoření IPMS vyřešilo problém, jak bezproblémově integrovat různé protokoly IP mobility – konkrétně klientovský DSMIPv6 a síťový PMIPv6 – do jednotného rámce řízeného politikami. Bez IPMS by síti chyběl deterministický způsob výběru vhodného kotviště mobility (mobility anchor) a tunelovacího mechanismu, což by mohlo vést k problémům s kompatibilitou, neúspěšným předáním služby nebo suboptimálnímu využití zdrojů. Jeho účelem je oddělit schopnosti UE od politiky sítě, čímž dává operátorům kontrolu nad strategií správy mobility. To umožňuje efektivní nasazení sítě, podporuje postupný zavádění nových protokolů mobility a je zásadní pro realizaci vize 'Access Agnostic' (přístupově agnostického) Evolved Packet System (EPS), kde jsou služby jádrové sítě poskytovány konzistentně bez ohledu na podkladovou rádiovou technologii.

## Klíčové vlastnosti

- Výběr protokolu pro správu IP mobility založený na politikách (např. DSMIPv6, PMIPv6)
- Zohledňuje jak statické provozovatelské politiky, tak dynamické schopnosti UE
- Nedílná součást mobility mezi 3GPP a ne-3GPP přístupovými sítěmi
- Centralizovaná rozhodovací funkce, často s rozhraním k PCRF nebo architektuře politik
- Umožňuje bezproblémovou kontinuitu IP relace při předání služby mezi systémy
- Podporuje flexibilní strategie nasazení pro heterogenní sítě

## Související pojmy

- [EPC – Evolved Packet Core Network](/mobilnisite/slovnik/epc/)
- [PCRF – Policy and Charging Rules Function](/mobilnisite/slovnik/pcrf/)

## Definující specifikace

- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3

---

📖 **Anglický originál a plná specifikace:** [IPMS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ipms/)
