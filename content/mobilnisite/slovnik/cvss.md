---
slug: "cvss"
url: "/mobilnisite/slovnik/cvss/"
type: "slovnik"
title: "CVSS – Common Vulnerability Scoring System"
date: 2025-01-01
abbr: "CVSS"
fullName: "Common Vulnerability Scoring System"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/cvss/"
summary: "CVSS je standardizovaný rámec pro hodnocení a klasifikaci závažnosti bezpečnostních zranitelností v sítích 3GPP. Poskytuje konzistentní, objektivní metodiku pro vyhodnocování zranitelností na základě"
---

CVSS (Common Vulnerability Scoring System) je standardizovaný rámec pro hodnocení a klasifikaci závažnosti bezpečnostních zranitelností v sítích 3GPP.

## Popis

Common Vulnerability Scoring System (CVSS) je dodavatelsky neutrální, otevřený rámec vyvinutý organizací [FIRST](/mobilnisite/slovnik/first/) (Forum of Incident Response and Security Teams) a přijatý 3GPP pro hodnocení zranitelností v rámci telekomunikačních standardů. Ve specifikacích 3GPP slouží CVSS jako standardizovaná metodika pro vyhodnocování bezpečnostních zranitelností objevených v síťových funkcích, rozhraních, protokolech a implementacích. Systém poskytuje strukturovaný přístup ke skórování zranitelností, který umožňuje konzistentní posouzení rizik napříč různými dodavateli, nasazeními sítí a verzemi release.

CVSS funguje prostřednictvím tří skupin metrik, které společně určují konečné skóre závažnosti. Základní metriky (Base Metrics) vyhodnocují vnitřní charakteristiky zranitelnosti, které jsou v čase konstantní a nezávislé na uživatelském prostředí. Patří mezi ně Vektor útoku (síťový, sousední, lokální, fyzický), Složitost útoku (vysoká/nízká), Požadovaná oprávnění (žádná/nízká/vysoká), Interakce uživatele (není vyžadována/vyžadována), Rozsah (nezměněný/změněný) a tři metriky dopadu: Důvěrnost, Integrita a Dostupnost. Každá metrika má přiřazenou hodnotu, která přispívá k výpočtu Základního skóre v rozsahu od 0,0 do 10,0.

Časové metriky (Temporal Metrics) upravují Základní skóre na základě faktorů, které se v čase mění, včetně Zralosti kódu pro využití (nedefinováno, vysoká, funkční, proof-of-concept, neprokázaná), Úrovně nápravy (oficiální oprava, dočasná oprava, pracovní řešení, nedostupná) a Spolehlivosti hlášení (potvrzená, rozumná, neznámá). Metriky prostředí (Environmental Metrics) dále upřesňují skóre na základě konkrétního implementačního prostředí, přičemž zohledňují Bezpečnostní požadavky (požadavky na důvěrnost, integritu, dostupnost) a Modifikované základní metriky, které zahrnují zmírnění nebo zesílení vlivu prostředí.

V sítích 3GPP je skórování CVSS integrováno do procesů správy bezpečnostních zranitelností popsaných v TS 33.916. Když jsou ve specifikacích nebo implementacích 3GPP objeveny zranitelnosti, bezpečnostní výzkumníci, dodavatelé nebo operátoři vypočítají skóre CVSS pomocí standardizované metodiky. Tato skóre se pak používají ke kategorizaci zranitelností jako Kritické (9,0-10,0), Vysoké (7,0-8,9), Střední (4,0-6,9) nebo Nízké (0,1-3,9). Skórování umožňuje konzistentní komunikaci závažnosti zranitelností napříč celým telekomunikačním dodavatelským řetězcem.

Implementace CVSS v rámci 3GPP vytváří společný jazyk pro posuzování bezpečnostních rizik, který překračuje organizační hranice. Dodavatelé síťového vybavení používají skóre CVSS k stanovení priorit při vývoji a plánování vydávání záplat. Mobilní síťoví operátoři tato skóre využívají k informovanému rozhodování o nasazení nouzových záplat versus plánovaných údržbových oken. Normalizační orgány jako 3GPP používají agregovaná data CVSS k identifikaci systémových bezpečnostních slabin ve specifikacích a k vedení prací na vylepšení bezpečnosti v následujících release.

## K čemu slouží

CVSS byl zaveden do standardů 3GPP, aby řešil kritickou potřebu konzistentního hodnocení závažnosti zranitelností napříč fragmentovaným telekomunikačním ekosystémem. Před jeho přijetím používali různí dodavatelé, operátoři a bezpečnostní výzkumníci proprietární nebo nekonzistentní metody pro klasifikaci závažnosti zranitelností, což vedlo ke zmatkům, chybnému stanovení priorit při odstraňování a neefektivní komunikaci rizik. Tato nekonzistence byla obzvláště problematická v více-dodavatelských sítích 3GPP, kde zranitelnosti mohly ovlivnit propojené komponenty od různých dodavatelů.

Telekomunikační průmysl čelil rostoucím bezpečnostním výzvám, jak se sítě vyvíjely z izolovaných systémů na propojené, softwarově definované architektury. S přechodem na 5G a další generace se síťové funkce stávaly stále více virtualizovanými a vystavenými širší útočné ploše. Nedostatek standardizovaného hodnocení zranitelností ztěžoval porovnávání rizik napříč různými síťovými prvky, efektivní stanovení priorit pro omezené bezpečnostní zdroje a vytváření společných bezpečnostních postojů mezi roamingovými partnery.

3GPP přijalo CVSS ve Release 13, aby vytvořilo jednotný rámec umožňující objektivní a reprodukovatelné skórování zranitelností. Tato standardizace umožňuje všem zúčastněným stranám – včetně výrobců zařízení, dodavatelů softwaru, mobilních operátorů a bezpečnostních výzkumníků – používat stejný jazyk při diskusi o závažnosti zranitelností. Poskytnutím matematicky rigorózní metodiky skórování CVSS eliminuje subjektivní interpretace rizik a umožňuje rozhodování založená na datech pro správu zranitelností v celém ekosystému 3GPP.

## Klíčové vlastnosti

- Standardizovaná metodika skórování zranitelností
- Třívrstvá struktura metrik (Základní, Časové, Prostředí)
- Numerické skóre od 0,0 do 10,0 s kategoriemi závažnosti
- Dodavatelsky neutrální a na implementaci nezávislé hodnocení
- Časově uvědomělé skórování prostřednictvím Časových metrik
- Přizpůsobení konkrétnímu prostředí prostřednictvím Metrik prostředí

## Definující specifikace

- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)

---

📖 **Anglický originál a plná specifikace:** [CVSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cvss/)
