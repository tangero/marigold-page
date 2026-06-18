---
slug: "ldi"
url: "/mobilnisite/slovnik/ldi/"
type: "slovnik"
title: "LDI – Location Dependent Interception"
date: 2025-01-01
abbr: "LDI"
fullName: "Location Dependent Interception"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/ldi/"
summary: "Schopnost zákonného odposlechu (LI), která umožňuje orgánům odposlouchávat komunikaci na základě konkrétní geografické polohy uživatele. Umožňuje cílené sledování, když uživatel vstoupí do předdefinov"
---

LDI je schopnost zákonného odposlechu, která umožňuje orgánům odposlouchávat komunikaci na základě konkrétní geografické polohy uživatele; aktivuje se pouze při vstupu uživatele do předdefinované oblasti.

## Popis

Location Dependent Interception (LDI) je specializovaná funkce v rámci architektury zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)) podle 3GPP, definovaná primárně v řadě specifikací 33.1xx (např. 33.106, 33.107, 33.126). Rozšiřuje standardní možnosti LI o geografický spouštěč. Ve standardním LI se odposlech komunikace cíle (obsah komunikace, [IRI](/mobilnisite/slovnik/iri/)) typicky aktivuje na základě identifikátoru cíle a zůstává aktivní bez ohledu na polohu. LDI přidává prostorový rozměr: odposlech se provádí pouze tehdy, když se cíl nachází v určené geografické oblasti, jako je buňka, skupina buněk nebo definovaná geografická zóna (např. pomocí zeměpisných souřadnic).

Architektonická implementace LDI zahrnuje několik síťových entit. Jádrová funkce sídlí ve funkci zákonného odposlechu ([LIF](/mobilnisite/slovnik/lif/)) a v řídicím prvku odposlechu ([ICE](/mobilnisite/slovnik/ice/)), což je síťový uzel (jako [SGSN](/mobilnisite/slovnik/sgsn/), [MME](/mobilnisite/slovnik/mme/) nebo [S-CSCF](/mobilnisite/slovnik/s-cscf/)), který provádí vlastní odposlech. Zařízení pro monitorování orgánů činných v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)) poskytuje soudní příkaz specifikující cíl a oblast zájmu. Tyto informace o oblasti jsou zřízeny v síti. ICE tedy musí být schopen přijímat a zpracovávat informace o poloze cíle (např. od MSC, SGSN nebo MME) a korelovat je se zřízenou geografickou oblastí. Když poloha cíle odpovídá oblasti, ICE aktivuje odposlech a začne doručovat odposlechnuté informace mediační funkci (MF) a dále do LEMF. Když cíl oblast opustí, je odposlech deaktivován.

Klíčové technické komponenty zahrnují definici geografické oblasti (která může být založena na buňce, směrovací oblasti nebo používat zeměpisné souřadnice), mechanismy hlášení polohy z rádiového přístupového a jádrové sítě a stavový automat v ICE, který spravuje aktivaci a deaktivaci relace odposlechu. LDI funguje v rámci striktní architektury LI podle 3GPP, což zajišťuje oddělení funkce odposlechu od normálního síťového provozu a zachovává požadovaná rozhraní předávání (HI1, HI2, HI3). Jeho úlohou je poskytnout přesnější a zdrojově efektivnější nástroj odposlechu, který sladí sledovací aktivity s právními mandáty, jež mohou být územně omezené.

## K čemu slouží

LDI bylo vytvořeno pro řešení právních a provozních požadavků, kdy je oprávnění k zákonnému odposlechu uděleno pouze pro konkrétní geografické lokality. Například soudní příkaz může povolit odposlech pouze tehdy, když je podezřelý v konkrétním městě nebo budově. Před zavedením LDI byly systémy zákonného odposlechu obecně na poloze nezávislé; jakmile byly pro cíl aktivovány, odposlouchávaly komunikaci globálně, což mohlo překročit právní mandát a plýtvat zpracovatelskými a úložnými zdroji. Tento nedostatek podrobnosti představoval právní rizika pro operátory a orgány činné v trestním řízení.

Motivace vycházela z vývoje právních rámců, zejména v Evropě, které požadují přesnější a přiměřenější sledovací opatření. Řeší také efektivitu sítě. Odposlech a zpracování veškeré komunikace cíle, i když je mimo relevantní oblast, spotřebovává významnou šířku pásma a úložný prostor v mediačních a doručovacích funkcích. LDI to optimalizuje tím, že činí odposlech podmíněným. Historicky rané systémy mobilního odposlechu tuto jemně nastavitelnou kontrolu postrádaly, což vedlo k vývoji LDI jako standardizované funkce počínaje 3GPP Release 8, což umožnilo interoperabilní a právně shodné implementace napříč zařízeními různých dodavatelů a síťovými generacemi.

## Klíčové vlastnosti

- Geografické spouštění: Odposlech se aktivuje/deaktivuje na základě polohy cíle v reálném čase.
- Flexibilita definice oblasti: Podporuje definici oblastí odposlechu pomocí Cell ID, Routing Area ID nebo zeměpisných souřadnic (např. polygon).
- Správa stavových relací: ICE udržuje stav (aktivní/neaktivní) relace LDI na základě událostí souvisejících s polohou.
- Integrace se standardní architekturou LI: Funguje v rámci stávajícího rozhraní předávání (HI) 3GPP bez změny základních protokolů LI.
- Korelace s informacemi o poloze: Rozhraní se síťovými službami polohy (např. od MME, SGSN, GMLC) pro získání polohy cíle.
- Podpora právní shody: Poskytuje technické prostředky k přesnému omezení odposlechu na rozsah povolený soudním příkazem.

## Definující specifikace

- **TS 33.106** (Rel-19) — Lawful Interception Requirements (Pre-Rel-15)
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.126** (Rel-19) — Lawful Interception Requirements

---

📖 **Anglický originál a plná specifikace:** [LDI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ldi/)
