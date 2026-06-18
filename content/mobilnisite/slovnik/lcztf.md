---
slug: "lcztf"
url: "/mobilnisite/slovnik/lcztf/"
type: "slovnik"
title: "LCZTF – Location Client Zone Transformation Function"
date: 2025-01-01
abbr: "LCZTF"
fullName: "Location Client Zone Transformation Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lcztf/"
summary: "Síťová funkce v architektuře služeb polohy (LCS), která transformuje požadavek klienta na geografickou zónu na odpovídající síťovou oblast. Je nezbytná pro poskytování služeb založených na poloze, jak"
---

LCZTF je síťová funkce v architektuře LCS podle 3GPP, která transformuje požadavek klienta na geografickou zónu na odpovídající síťovou oblast, aby umožnila služby založené na poloze.

## Popis

Funkce transformace zóny polohového klienta (LCZTF) je klíčová komponenta v standardizované architektuře služeb polohy ([LCS](/mobilnisite/slovnik/lcs/)) podle 3GPP, konkrétně definovaná pro rozhraní Mobilního polohového protokolu ([MLP](/mobilnisite/slovnik/mlp/)). Funguje jako logická funkce, často integrovaná v rámci Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) nebo vyhrazeného LCS serveru. Jejím hlavním úkolem je sloužit jako překladač mezi geografickými koncepty servisní vrstvy a interními identifikátory oblastí sítě. Když aplikace služby založené na poloze (LCS klient) požaduje upozornění pro mobilního účastníka vstupujícího do nebo opouštějícího definovanou geografickou zónu (např. polygon nebo kruh), odešle tento popis zóny LCZTF přes rozhraní MLP. LCZTF následně zpracuje tuto geografickou informaci a transformuje ji na odpovídající sadu identifikátorů síťových oblastí, jako jsou ID buněk (Cell IDs), identity směrovacích oblastí ([RAI](/mobilnisite/slovnik/rai/)) nebo identity servisních oblastí ([SAI](/mobilnisite/slovnik/sai/)), které nejlépe aproximují požadovanou zónu. Tato transformace je nezbytná, protože funkce správy mobility a pagingu v jádru sítě pracují na základě těchto síťově definovaných oblastí, nikoli libovolných zeměpisných souřadnic. Výstup LCZTF umožňuje síti efektivně sledovat polohu účastníka monitorováním jeho pohybu mezi těmito předdefinovanými síťovými oblastmi a spustit hlášení o poloze pro LCS klienta pouze při detekci překročení hranice relevantní pro transformovanou zónu. Tato architektura abstrahuje komplexní detaily radiového určování polohy od servisní aplikace a poskytuje čistý mechanismus spouštění založený na oblastech. Funkce hraje klíčovou roli při umožňování služeb, jako je účtování založené na poloze, kde se sazby mění podle zóny, nebo upozornění na blízkost. Její specifikace zajišťují interoperabilitu mezi síťovými dodavateli a poskytovateli služeb a vytvářejí standardizovaný most pro požadavky na služby polohy založené na zónách.

## K čemu slouží

LCZTF byla zavedena za účelem standardizace a usnadnění implementace proaktivních služeb polohy založených na zónách v rámci buněčných sítí. Před její standardizací bylo zavádění služeb vyžadujících upozornění na vstup nebo výstup účastníka z konkrétní oblasti složité a závislé na dodavateli. Servisní aplikace musely rozumět nízkopodlažní topologii sítě a plánování buněk nebo se spoléhat na nepřetržité, vysokofrekvenční požadavky na určení polohy, což bylo neefektivní a náročné na zdroje. LCZTF tento problém řeší tím, že poskytuje standardizovanou síťovou funkci, která zajišťuje překlad ze servisně definované geografické zóny na operační oblasti sítě. Toto oddělení odpovědností umožňuje vývojářům aplikací definovat služby pomocí jednoduchých geografických tvarů, zatímco síťový operátor spravuje komplexní mapování na podkladové, případně nepravidelné, rozložení rádiových buněk. Motivací byl rostoucí komerční zájem o služby založené na poloze ([LBS](/mobilnisite/slovnik/lbs/)) na počátku 21. století, jako jsou aplikace pro vyhledání přátel, sledování majetku a diferencované zóny účtování. Její vytvoření v rámci architektury [LCS](/mobilnisite/slovnik/lcs/) poskytlo škálovatelnou a síťově efektivní metodu pro spouštění událostí, která je mnohem lepší než periodické dotazování, protože minimalizuje signalizační zátěž a využití zdrojů pro určování polohy tím, že jedná pouze při překročení významné hranice účastníkem. To umožnilo novou třídu síťově spouštěných služeb polohy, které byly výkonné a standardizované napříč odvětvím.

## Klíčové vlastnosti

- Překlad geografické oblasti na síťovou: Převádí geografické zóny ve tvaru polygonu nebo kruhu definované LCS klienty na sadu ID buněk (Cell IDs), RAI nebo SAI.
- Proaktivní spouštění událostí: Umožňuje síťově iniciované hlášení polohy, když účastník vstoupí do nebo opustí transformovanou síťovou oblast, čímž podporuje triggery typu 'Area Event'.
- Podpora rozhraní MLP: Funguje jako definovaná komponenta v rámci servisní vrstvy Mobilního polohového protokolu (MLP) pro standardizovanou komunikaci s LCS klienty.
- Integrace s GMLC: Typicky implementována jako logická funkce v rámci nebo v úzkém spojení s Gateway Mobile Location Centre.
- Síťová efektivita: Snižuje signalizační zátěž a zátěž spojenou s určováním polohy ve srovnání s periodickým dotazováním tím, že spouští hlášení pouze při překročení hranic.
- Abstrakce služeb: Skrývá složitosti topologie rádiové sítě a plánování buněk před externími servisními aplikacemi.

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [MLP – Mobile Location Protocol](/mobilnisite/slovnik/mlp/)
- [SAI – Service Area Identifier](/mobilnisite/slovnik/sai/)

## Definující specifikace

- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [LCZTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lcztf/)
