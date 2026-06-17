---
slug: "mmco"
url: "/mobilnisite/slovnik/mmco/"
type: "slovnik"
title: "MMCO – Memory Management Control Operation"
date: 2025-01-01
abbr: "MMCO"
fullName: "Memory Management Control Operation"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mmco/"
summary: "Řídicí operace definovaná standardem 3GPP pro správu paměťových prostředků v síťových funkcích, zejména pro samoorganizující se sítě (SON) a analytiku managementu dat. Standardizuje postupy pro alokac"
---

MMCO je řídicí operace definovaná standardem 3GPP pro správu paměťových prostředků v síťových funkcích, která standardizuje postupy pro alokaci, dealokaci a optimalizaci za účelem zajištění stability a výkonu sítě.

## Popis

Memory Management Control Operation (MMCO, operace řízení správy paměti) je standardizovaný postup v rámci architektury 3GPP, specifikovaný v TS 26.906, který řídí správu paměťových prostředků v síťových prvcích. Je klíčovou součástí pro spolehlivý provoz síťových funkcí, zejména těch zapojených do komplexního zpracování dat, analytiky a funkcí samoorganizujících se sítí (SON). Tato operace poskytuje formalizovaný mechanismus, kterým síťový software řízeným způsobem žádá, alokuje, monitoruje a uvolňuje bloky paměti, čímž předchází problémům, jako jsou úniky paměti, fragmentace nebo její vyčerpání, které mohou vést k degradaci služeb nebo výpadkům uzlu.

Z architektonického hlediska je MMCO implementována v rámci managementové roviny síťových funkcí a komunikuje s operačním systémem nebo vyhrazeným správcem prostředků. Definuje sadu primitiv nebo [API](/mobilnisite/slovnik/api/), která aplikační logika používá pro interakci se základním paměťovým subsystémem. Tyto operace typicky zahrnují žádosti o paměť specifické velikosti a typu (např. volatilní, perzistentní), oznámení o úrovni využití paměti a příkazy pro uvolňování nebo kompaktaci paměti. Řídicí logika zajišťuje, že využití paměti zůstává v rámci nastavených prahových hodnot a politik, a často komunikuje s vyššími systémy správy, jako je Network Management System ([NMS](/mobilnisite/slovnik/nms/)) nebo Element Management System ([EMS](/mobilnisite/slovnik/ems/)), pro účely reportování a orchestraci.

Její role je zásadní v moderních softwarově definovaných síťových funkcích, včetně virtualizovaných síťových funkcí (VNF) a cloud-nativních funkcí ([CNF](/mobilnisite/slovnik/cnf/)), kde je efektivní využití prostředků prvořadé. Díky standardizovanému přístupu umožňuje MMCO konzistentní chování napříč více-dodavatelskými nasazeními, napomáhá správě poruch korelací paměťových událostí s výkonnostními problémy a podporuje pokročilé funkce, jako je prediktivní škálování. V kontextu služeb analytiky managementu dat ([MDAS](/mobilnisite/slovnik/mdas/)) a SON, které zpracovávají obrovská množství výkonnostních a konfiguračních dat, je robustní správa paměti nezbytná pro udržení schopností real-time optimalizace a zajištění kvality.

## K čemu slouží

MMCO byla zavedena jako odpověď na rostoucí komplexitu a softwarovou náročnost telekomunikačních síťových funkcí. Před její standardizací byla správa paměti z velké části záležitostí specifickou pro implementaci každého dodavatele zařízení. To vedlo k nekonzistentnostem v tom, jak síťové uzly zvládaly paměťovou zátěž, což ztěžovalo celosíťový management, diagnostiku poruch a zajištění výkonu. Nekontrolovaná spotřeba paměti mohla způsobit nepředvídatelné restartování uzlů nebo skrytou degradaci výkonu, což ovlivňovalo kvalitu služeb.

Vytvoření MMCO bylo motivováno přechodem odvětví k více softwarově orientovaným a automatizovaným sítím, zejména s nasazením LTE-Advanced a důrazem na funkce SON ve verzi 3GPP Release 12. Funkce SON, jako je Mobility Robustness Optimization ([MRO](/mobilnisite/slovnik/mro/)) a Capacity and Coverage Optimization ([CCO](/mobilnisite/slovnik/cco/)), vyžadují nepřetržité sbírání a zpracování dat, což je náročné na paměť. Standardizovaná řídicí operace zajišťuje, že tyto funkce mohou spolehlivě fungovat, aniž by způsobovaly nestabilitu hostitelské síťové funkce.

MMCO navíc poskytuje základ pro správu životního cyklu v virtualizovaných a cloud-nativních prostředích. Umožňuje systémům správy a orchestraci (např. [NFV](/mobilnisite/slovnik/nfv/) MANO) mít standardizovaný přehled o spotřebě prostředků síťových funkcí, což umožňuje inteligentnější škálování a ozdravné akce. Řeší problém neprůhledného využití prostředků a mění správu paměti z černé skříňky na spravovatelný a pozorovatelný aspekt síťového provozu, což je klíčové pro dosažení vysoké dostupnosti a spolehlivosti očekávané u operátorských sítí.

## Klíčové vlastnosti

- Standardizovaná primitiva pro žádosti o alokaci a dealokaci paměti
- Mechanismy pro monitorování využití paměti v reálném čase a prahových hodnot
- Podpora různých typů paměti (např. halda, perzistentní úložiště)
- Integrace se systémy správy poruch a výkonu pro hlášení událostí
- Postupy pro řízené snížení výkonu nebo obnovu při vyčerpání paměti
- Definovaná rozhraní pro interakci s entitami síťového managementu a orchestraci

## Související pojmy

- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [MDAS – Management Data Analytics Service](/mobilnisite/slovnik/mdas/)

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services

---

📖 **Anglický originál a plná specifikace:** [MMCO na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmco/)
