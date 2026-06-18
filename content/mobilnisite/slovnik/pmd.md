---
slug: "pmd"
url: "/mobilnisite/slovnik/pmd/"
type: "slovnik"
title: "PMD – Pseudonym Mediation Device functionality"
date: 2025-01-01
abbr: "PMD"
fullName: "Pseudonym Mediation Device functionality"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pmd/"
summary: "Funkce Pseudonym Mediation Device (PMD) je síťový prvek pro ochranu soukromí definovaný pro sítě 3GPP. Působí jako zprostředkovatel, který v jádrové síti překládá dočasné identifikátory (pseudonymy) p"
---

PMD je síťová funkce zajišťující soukromí, která v jádrové síti překládá dočasné pseudonymy z rádiového rozhraní na trvalé identifikátory účastníka, čímž chrání identitu uživatele před odposloucháváním.

## Popis

Funkce Pseudonym Mediation Device (PMD) je bezpečnostní a soukromí zajišťující mechanismus specifikovaný ve standardech 3GPP, konkrétně v TS 23.271 (Location Services) a TS 33.117 (Lawful Interception architecture). Není nutně samostatným fyzickým uzlem, ale logickou funkcí, která může být integrována v prvcích jádrové sítě, jako je Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)), Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo specializovaný uzel. Jejím hlavním úkolem je udržovat oddělení mezi trvalou dlouhodobou identitou uživatele a dočasnými, často se měnícími identitami používanými na rádiovém rozhraní, aby se zabránilo sledování.

Během provozu, když se účastník připojí k síti, jádrová síť přiřadí dočasný identifikátor, jako je Temporary Mobile Subscriber Identity ([TMSI](/mobilnisite/slovnik/tmsi/)) v GSM/UMTS nebo Globally Unique Temporary Identity ([GUTI](/mobilnisite/slovnik/guti/)) v LTE/5G. Tento pseudonym se používá ve většině signalizačních zpráv přes síť rádiového přístupu, aby se zabránilo přenosu trvalého International Mobile Subscriber Identity ([IMSI](/mobilnisite/slovnik/imsi/)). V zabezpečené doméně jádrové sítě však různé funkce (např. účtování, lawful interception, služby polohy) vyžadují zpětné mapování na trvalou identitu účastníka.

Funkce PMD tuto mediaci provádí. Udržuje vazbu mezi aktuálně přiděleným pseudonymem (TMSI/GUTI) a odpovídajícím IMSI. Když síťová funkce obdrží požadavek nebo záznam obsahující pouze pseudonym, může dotazovat PMD, aby jej přeložila na IMSI. Zásadní je, že k tomuto překladu dochází pouze v rámci chráněné jádrové sítě, což zajišťuje, že IMSI není nikdy vystaveno na rádiovém spojení. PMD musí být vysoce zabezpečenou a důvěryhodnou entitou s přísnými přístupovými kontrolami, protože uchovává klíčové mapování pro soukromí uživatele.

Její architektura zahrnuje rozhraní s dalšími entitami jádrové sítě. Pro lawful interception poskytuje PMD (nebo Mediační funkce zahrnující schopnosti PMD) mapování identity systému Lawful Interception, což oprávněným orgánům umožňuje korelovat odposlechnuté komunikace s trvalou identitou konkrétního účastníka, jak vyžadují právní rámce. Ve službách polohy umožňuje, aby byly požadavky na polohu založené na pseudonymu správně směrovány na obslužný uzel, který má kontext daného účastníka.

## K čemu slouží

Funkce PMD byla vytvořena k vyřešení základního napětí v návrhu mobilních sítí: potřeby síťových operací a lawful interception jednoznačně identifikovat účastníky versus požadavek na soukromí chránit účastníky před sledováním nebo identifikací odposlouchávači na rádiovém rozhraní. Bez takového mechanismu by muselo být trvalé [IMSI](/mobilnisite/slovnik/imsi/) často přenášeno, což by účastníky činilo zranitelnými vůči sledování polohy a krádeži identity prostřednictvím IMSI catcherů.

Problém, který řeší, je zachování důvěrnosti identity účastníka při současném zachování nezbytné funkčnosti sítě. Rané mobilní systémy měly omezené využití dočasných identifikátorů a mapování bylo často řešeno distribuovaným, nestandardizovaným způsobem. Standardizace funkce PMD, zejména v kontextu lawful interception ([LI](/mobilnisite/slovnik/li/)), poskytla jasnou, bezpečnou a standardizovanou metodu pro oprávněné entity k překladu pseudonymů. To bylo klíčové pro splnění právních požadavků na LI v různých zemích a síťových architekturách.

Historicky byl její vývoj poháněn vývojem funkcí pro ochranu soukromí (jako je [TMSI](/mobilnisite/slovnik/tmsi/)) ve 2G/3G a následnou potřebou standardizovaného mediačního bodu pro požadavky lawful interception zavedené koncem 90. let a počátkem 21. století. Zajišťuje, že i když sítě používají silnější techniky ochrany soukromí na rádiovém rozhraní, schopnost zákonného, autorizovaného překladu identity pro právní, provozní a účely nouzových služeb zůstává zachována a je prováděna řízeným, auditovatelným způsobem v rámci zabezpečeného jádra sítě.

## Klíčové vlastnosti

- Zprostředkovává překlad mezi dočasnými rádiovými identifikátory (TMSI, GUTI) a trvalými identitami účastníka (IMSI)
- Funguje v rámci zabezpečené domény jádrové sítě, aby ochránila IMSI před vystavením na rádiovém rozhraní
- Nezbytná pro Lawful Interception (LI) k poskytnutí překladu identity systémům pro odposlech
- Podporuje služby založené na poloze tím, že umožňuje mapovat požadavky s pseudonymy na účastníky
- Může být implementována jako samostatný uzel nebo integrována do funkcí HLR/HSS/mediačních funkcí
- Vynucuje přísnou kontrolu přístupu a bezpečnostní politiky kvůli své citlivé roli

## Související pojmy

- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [TMSI – Temporary Mobile Subscriber Identifier](/mobilnisite/slovnik/tmsi/)
- [GUTI – Globally Unique Temporary UE Identity](/mobilnisite/slovnik/guti/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 25.411** (Rel-19) — Iu Interface Layer 1 Specification
- **TS 29.173** (Rel-19) — Diameter-based SLh Interface for LCS
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification

---

📖 **Anglický originál a plná specifikace:** [PMD na 3GPP Explorer](https://3gpp-explorer.com/glossary/pmd/)
