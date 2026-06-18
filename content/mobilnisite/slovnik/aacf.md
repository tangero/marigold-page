---
slug: "aacf"
url: "/mobilnisite/slovnik/aacf/"
type: "slovnik"
title: "AACF – Auxiliary Advice of Charge Function"
date: 2025-01-01
abbr: "AACF"
fullName: "Auxiliary Advice of Charge Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aacf/"
summary: "Funkce Auxiliary Advice of Charge (AACF) je funkce správy podle 3GPP, která podporuje operace účtování poskytováním doplňujících údajů o účtování a zpracovatelských schopností. Funguje v rámci archite"
---

AACF je funkce správy v rámci architektury TMN podle 3GPP, která poskytuje doplňující údaje o účtování a zpracovatelské schopnosti pro zvýšení přesnosti fakturace a podporu složitých scénářů účtování.

## Popis

Funkce Auxiliary Advice of Charge (AACF) je standardizovaná síťová funkce definovaná v architektuře Telecommunication Management Network ([TMN](/mobilnisite/slovnik/tmn/)) podle 3GPP, konkrétně v rámci domény správy účtování. Slouží jako doplňující komponenta, která spolupracuje s primárními funkcemi účtování, jako je Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) a Charging Gateway Function ([CGF](/mobilnisite/slovnik/cgf/)), a poskytuje rozšířené schopnosti účtování. AACF funguje v rámci architektury definované v 3GPP TS 32.280, která specifikuje referenční architekturu a rozhraní pro správu účtování.

Architektonicky se AACF nachází v řídicí rovině sítě, nikoli v uživatelské nebo řídicí rovině. Propojuje se s různými síťovými prvky souvisejícími s účtováním prostřednictvím standardizovaných referenčních bodů, především referenčního bodu Rf pro offline účtování a referenčního bodu Ro pro systémy online účtování. Tato funkce slouží jako pomocný procesor, který dokáže zpracovávat specializované scénáře účtování, provádět dodatečnou validaci záznamů o účtovacích údajích ([CDR](/mobilnisite/slovnik/cdr/)) a podporovat složité ratingové funkce, které primární účtovací komponenty nemusí zvládat efektivně.

Při provozu přijímá AACF účtovací události a data ze síťových funkcí, jako je Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), nebo přímo ze síťových prvků generujících účtovací spouštěče. Tyto informace zpracovává podle nastavených obchodních pravidel a politik, případně aplikuje doplňující účtovací logiku, provádí převody měn, aplikuje daňové výpočty nebo implementuje zákaznické specifické účtovací algoritmy. Zpracovaná data jsou následně předána příslušným systémům pro sběr účtovacích údajů nebo fakturaci.

Klíčovými součástmi AACF jsou zpracovatelský engine pro účtovací data, subsystém správy pravidel a adaptéry rozhraní pro různé účtovací protokoly. Zpracovatelský engine provádí účtovací algoritmy a obchodní logiku, zatímco subsystém správy pravidel udržuje a aplikuje účtovací politiky. Adaptéry rozhraní zajišťují kompatibilitu s různými účtovacími systémy a protokoly používanými v síti. Role AACF je obzvláště důležitá v prostředích s více dodavateli, kde musí účtovací systémy od různých výrobců bezproblémově spolupracovat.

Tato funkce hraje klíčovou roli při zajišťování přesnosti a flexibility účtování v moderních telekomunikačních sítích. Odlehčením specializovaného zpracování účtování od primárních účtovacích funkcí pomáhá AACF udržovat výkon systému během špiček v účtování. Operátorům také umožňuje implementovat složité scénáře účtování bez nutnosti úprav základní účtovací infrastruktury, čímž podporuje inovativní služby při zachování integrity fakturace.

## K čemu slouží

Funkce Auxiliary Advice of Charge byla vytvořena, aby řešila rostoucí složitost scénářů účtování v moderních telekomunikačních sítích. Jak se sítě 3GPP vyvíjely od jednoduchých hlasových služeb k zahrnutí datových, multimediálních a přidaných služeb, tradiční účtovací systémy narážely na omezení při zvládání různorodých účtovacích modelů, složitých ratingových scénářů a specializovaných požadavků na fakturaci. AACF poskytuje standardizovaný přístup k rozšíření účtovacích schopností bez nutnosti zásadních změn základní účtovací infrastruktury.

Historicky operátoři čelili výzvám při zavádění nových služeb s jedinečnými požadavky na účtování. Každá nová služba často vyžadovala úpravy primárních účtovacích funkcí, což vedlo k prodloužení vývojových cyklů, zvýšení složitosti testování a potenciální nestabilitě systému. AACF tyto nedostatky řeší tím, že poskytuje modulární pomocnou funkci, kterou lze nezávisle aktualizovat pro podporu nových scénářů účtování. Toto oddělení zájmů umožňuje operátorům inovovat v nabídkách služeb při zachování stabilních základních účtovacích systémů.

Vytvoření AACF bylo motivováno potřebou větší flexibility v účtovacích architekturách, zejména při přechodu sítí na plně IP architektury a při začátku podpory různých úrovní kvality služeb (QoS), síťového řezání a služeb IoT. Tyto pokročilé služby přinesly požadavky na účtování, které bylo obtížné předvídat během počátečního návrhu sítě. AACF poskytuje standardizovaný mechanismus pro zvládání těchto vyvíjejících se požadavků a podporuje vše od jednoduchého účtování hlasu za minutu po složité účtování založené na událostech pro zařízení IoT a dynamické účtování založené na QoS pro síťové řezy.

## Klíčové vlastnosti

- Zpracování doplňujících údajů o účtování
- Podpora složitých ratingových algoritmů
- Validace a obohacení účtovacích údajů
- Schopnosti výpočtů s více měnami a daněmi
- Adaptace rozhraní pro heterogenní účtovací systémy
- Provedení účtovacích politik založených na pravidlech

## Definující specifikace

- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework

---

📖 **Anglický originál a plná specifikace:** [AACF na 3GPP Explorer](https://3gpp-explorer.com/glossary/aacf/)
