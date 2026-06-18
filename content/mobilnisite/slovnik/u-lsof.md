---
slug: "u-lsof"
url: "/mobilnisite/slovnik/u-lsof/"
type: "slovnik"
title: "U-LSOF – UTRAN Location System Operations Function"
date: 2025-01-01
abbr: "U-LSOF"
fullName: "UTRAN Location System Operations Function"
category: "Management"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/u-lsof/"
summary: "U-LSOF je funkce provozu a údržby lokalizačních služeb UTRAN. Zajišťuje správu výkonu, správu poruch a provisioning infrastruktury pro určování polohy, včetně U-LSCF a jednotek pro měření polohy (LMU)"
---

U-LSOF je funkce provozu a údržby (OAM) UTRAN, která spravuje výkon, poruchy a provisioning infrastruktury pro určování polohy, aby zajistila spolehlivé a přesné síťové lokalizační služby.

## Popis

[UTRAN](/mobilnisite/slovnik/utran/) Location System Operations Function (U-LSOF) je komponenta provozu, správy a údržby ([OAM](/mobilnisite/slovnik/oam/)) architektury lokalizačních služeb ([LCS](/mobilnisite/slovnik/lcs/)) UTRAN. Jedná se o logickou funkci odpovědnou za správu všech zdrojů a entit podílejících se na poskytování služeb určování polohy v UTRAN. Zatímco [U-LSCF](/mobilnisite/slovnik/u-lscf/) zajišťuje řízení lokalizačních relací v reálném čase, U-LSOF se zaměřuje na zázemí úkolů nezbytných pro přesný a efektivní chod lokalizačního systému. Typicky komunikuje s celkovým Operation and Support System ([OSS](/mobilnisite/slovnik/oss/)) nebo Element Management System ([EMS](/mobilnisite/slovnik/ems/)) operátora sítě.

U-LSOF plní několik klíčových provozních rolí. V rámci správy výkonu shromažďuje klíčové ukazatele výkonu ([KPI](/mobilnisite/slovnik/kpi/)) týkající se lokalizačních služeb, jako je úspěšnost určení polohy, dosažená přesnost podle použité metody, latence lokalizačních odpovědí a vytížení jednotek pro měření polohy ([LMU](/mobilnisite/slovnik/lmu/)). Tyto metriky sleduje, aby zajistila plnění smluv o úrovni služeb (SLA) a identifikovala oblasti pro optimalizaci sítě. Pro správu poruch přijímá U-LSOF alarmy a hlášení poruch od spravovaných entit, jako jsou U-LSCF/U-LSCFS a LMU. Může spouštět diagnostiku, aktivovat procedury obnovy a vést záznamy o poruchových událostech. Dále U-LSOF zajišťuje provisioning a správu konfigurace lokalizačního systému. To zahrnuje správu databáze zeměpisných souřadnic a schopností LMU, konfiguraci parametrů pro různé metody určování polohy a nastavování prahových hodnot pro monitorování výkonu.

Z architektonického hlediska může být U-LSOF integrována v rámci řídicí roviny RNC (pro integrovaná nasazení U-LSCF) nebo může sídlit v samostatném správním systému pro architekturu SAS. Ke komunikaci se spravovanými síťovými prvky používá standardizovaná nebo výrobcem specifická rozhraní pro správu, například založená na SNMP nebo CORBA. Díky poskytování centralizovaného pohledu na stav a výkon infrastruktury lokalizačních služeb umožňuje U-LSOF síťovým inženýrům systém proaktivně udržovat, plánovat kapacitní rozšíření pro LMU a řešit problémy, které by mohly ovlivnit kritické služby, jako je tísňové volání. Její role je zásadní pro přeměnu schopnosti určování polohy z pouhé technické funkce na spolehlivou službu úrovně operátora.

## K čemu slouží

U-LSOF byla vytvořena, aby řešila provozní složitosti vznikající při nasazení sofistikovaného síťového systému pro určování polohy, jako je UTRAN LCS. Bez vyhrazené provozní funkce by byla správa výkonu, poruch a konfigurace distribuovaných entit, jako jsou LMU a řídicí logika určování polohy, roztříštěná a neefektivní, což by vedlo k nízké spolehlivosti služeb. Jak se lokalizační služby staly povinnými pro tísňová volání a klíčovým prvkem komerčních aplikací, zajištění jejich konzistentního provozu se stalo kritickým obchodním a regulatorním požadavkem pro operátory.

Tato funkce řeší problém provozní přehlednosti a kontroly nad vrstvou lokalizačních služeb. Před její standardizací se operátoři spoléhali na nesourodé, na prvek specifické nástroje pro správu, což ztěžovalo získání celkového pohledu na výkon lokalizačních služeb nebo korelaci poruch napříč různými komponentami. U-LSOF poskytuje jednotný rámec pro správu přímo uzpůsobený pro LCS. Umožňuje operátorům monitorovat kvalitu služeb end-to-end, rychle izolovat poruchy (např. určit, zda je selhání určení polohy způsobeno výpadkem LMU nebo softwarovou chybou v U-LSCF) a efektivně provizovat nové LMU při rozšiřování sítě. Její zavedení bylo motivováno potřebou snížit provozní výdaje (OPEX) a zajistit, aby lokalizační služba splňovala přísné požadavky na dostupnost a přesnost kladené na služby veřejné bezpečnosti a komerční aplikace.

## Klíčové vlastnosti

- Centralizovaná správa výkonu pro lokalizační služby UTRAN, včetně sběru KPI jako je úspěšnost a přesnost
- Správa poruch komponent lokalizačního systému včetně U-LSCF/U-LSCFS a jednotek pro měření polohy (LMU)
- Provisioning a správa konfigurace databáze LMU a parametrů pro určování polohy
- Rozhraní k Operation Support System (OSS) operátora pro integrovanou správu sítě
- Podpora zajištění služeb a monitorování pro regulatorní shodu (např. E911)
- Umožňuje plánování kapacity a optimalizaci infrastruktury pro určování polohy

## Související pojmy

- [U-LSCF – UTRAN Location System Control Function](/mobilnisite/slovnik/u-lscf/)
- [OSS – Operations and Supervisory System](/mobilnisite/slovnik/oss/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2

---

📖 **Anglický originál a plná specifikace:** [U-LSOF na 3GPP Explorer](https://3gpp-explorer.com/glossary/u-lsof/)
