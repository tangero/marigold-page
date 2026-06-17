---
slug: "eoc"
url: "/mobilnisite/slovnik/eoc/"
type: "slovnik"
title: "EOC – Emergency Operations Center"
date: 2026-01-01
abbr: "EOC"
fullName: "Emergency Operations Center"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/eoc/"
summary: "Centrální koordinační bod pro řízení komunikací veřejné bezpečnosti během mimořádných událostí. Umožňuje orgánům přijímat, zpracovávat a vysílat kritické informace a zajišťuje tak účinnou koordinaci z"
---

EOC je centrální koordinační bod pro řízení komunikací veřejné bezpečnosti během mimořádných událostí, který umožňuje orgánům přijímat, zpracovávat a vysílat kritické informace pro účinnou koordinaci zásahu.

## Popis

Emergency Operations Center (EOC) je klíčová funkční entita v architektuře 3GPP pro komunikace veřejné bezpečnosti a pro misně-kritické služby. Slouží jako centrální uzel pro koordinaci operací při zásahu při mimořádných událostech a komunikuje s různými sítěmi včetně systémů založených na 3GPP, staršími sítěmi veřejné bezpečnosti a dalšími platformami pro tísňové služby. EOC je zodpovědný za příjem, agregaci a distribuci dat souvisejících s mimořádnou událostí, jako jsou informace o poloze, hlášení o situaci a multimédia z místa zásahu. Poskytuje potřebné nástroje a rozhraní pro operátory ke správě zdrojů, komunikaci s prvními zasahujícími jednotkami a udržování přehledu o situaci.

Z architektonického hlediska EOC komunikuje s prvky core sítě, jako je IP Multimedia Subsystem (IMS) pro misně-kritické služby, včetně Mission Critical Push-to-Talk ([MCPTT](/mobilnisite/slovnik/mcptt/)), Mission Critical Video ([MCVideo](/mobilnisite/slovnik/mcvideo/)) a Mission Critical Data (MCData). Může být také připojen ke klientovi Location Services ([LCS](/mobilnisite/slovnik/lcs/)) pro získání přesné polohy uživatelů nebo zařízení zapojených do události. EOC může být implementován jako samostatný systém nebo integrován do širší infrastruktury místa příjmu tísňových volání (PSAP). Jeho návrh upřednostňuje spolehlivost, zabezpečení a interoperabilitu, aby mohl fungovat ve vysoce stresových podmínkách během katastrof.

Klíčové součásti EOC zahrnují pracovní stanice operátorů se specializovaným softwarem pro obsluhu hovorů, mapování a sledování zdrojů, databáze pro ukládání záznamů o událostech a informací o zasahujících jednotkách a brány pro propojení s dalšími sítěmi tísňových služeb. Úlohou EOC je zajistit, aby komunikace při mimořádných událostech byly prioritizovány, zabezpečeny a efektivně směrovány, a podporovat tak funkce jako skupinová komunikace, dynamické přeskupování zasahujících jednotek a vysílání tísňových výstrah. Je to základní kámen vize 3GPP pro moderní, IP-based komunikace veřejné bezpečnosti, která překračuje tradiční systémy zaměřené pouze na hlas.

## K čemu slouží

EOC byl zaveden, aby řešil potřebu standardizovaného, interoperabilního velícího a řídicího střediska v sítích veřejné bezpečnosti nové generace. Před prací 3GPP se koordinace zásahu při mimořádných událostech často spoléhala na proprietární, izolované systémy, které bránily komunikaci mezi různými složkami (např. policie, hasiči, záchranná služba). Toto rozdělení mohlo vést ke zpožděným zásahům a špatnému přehledu o situaci během rozsáhlých událostí. Vývoj směrem k misně-kritickým službám založeným na LTE a 5G vytvořil příležitost k definování společného architektonického rámce pro operace při mimořádných událostech.

Hlavním problémem, který EOC řeší, je koordinace zásahů více složek během složitých mimořádných událostí. Poskytuje jednotnou platformu pro příjem tísňových hovorů a dat, správu nasazení zasahujících jednotek a sdílení kritických informací v reálném čase. Díky využití standardů 3GPP zajišťuje, že komunikace při mimořádných událostech mohou bezproblémově fungovat napříč komerčními a vyhrazenými sítěmi veřejné bezpečnosti a podporovat pokročilé funkce, jako je vysílání videa vysoké kvality, sdílení dat a přesné lokalizační služby, které byly ve starších systémech, jako je TETRA nebo P25, omezené.

## Klíčové vlastnosti

- Centralizované řízení událostí a koordinace zdrojů
- Rozhraní k misně-kritickým službám 3GPP (MCPTT, MCVideo, MCData)
- Integrace se službami určování polohy (LCS) pro sledování zasahujících jednotek
- Podpora multimediální komunikace při mimořádných událostech (hlas, video, data)
- Interoperabilita se staršími sítěmi veřejné bezpečnosti a dalšími PSAP
- Provoz s vysokou dostupností a zabezpečením pro kritické situace

## Související pojmy

- [MCPTT – Mission Critical Push to Talk Identity](/mobilnisite/slovnik/mcptt/)

## Definující specifikace

- **TS 22.268** (Rel-20) — Public Warning System (PWS) Requirements

---

📖 **Anglický originál a plná specifikace:** [EOC na 3GPP Explorer](https://3gpp-explorer.com/glossary/eoc/)
