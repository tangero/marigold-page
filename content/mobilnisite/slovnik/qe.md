---
slug: "qe"
url: "/mobilnisite/slovnik/qe/"
type: "slovnik"
title: "QE – Quality Estimate"
date: 2025-01-01
abbr: "QE"
fullName: "Quality Estimate"
category: "QoS"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/qe/"
summary: "Quality Estimate (QE, odhad kvality) je parametr používaný ve specifikacích 3GPP k vyjádření odhadované úrovně kvality pro toky uživatelských dat, zejména v kontextu transportních kanálů. Používá se v"
---

QE je parametr používaný ve specifikacích 3GPP k vyjádření odhadované úrovně kvality pro toky uživatelských dat, který podporuje plánování a správu prostředků v přístupové rádiové síti s ohledem na kvalitu.

## Popis

Quality Estimate (QE, odhad kvality) je metrika definovaná v architektuře přístupové rádiové sítě (RAN) 3GPP, konkrétně v kontextu rozhraní Iur a Iub pro [UTRAN](/mobilnisite/slovnik/utran/). Funguje v rámci vrstev Frame Protocol ([FP](/mobilnisite/slovnik/fp/)) a Radio Network Subsystem Application Part ([RNSAP](/mobilnisite/slovnik/rnsap/)), jak je podrobně popsáno ve specifikacích 25.423, 25.427 a 25.435. QE poskytuje kvantitativní vyhodnocení očekávané kvality pro datový tok, které síťové uzly jako Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) a Node B používají k informovanému rozhodování o konfiguraci transportního kanálu a plánování dat.

Technicky je QE často spojován s konkrétními transportními kanály, jako je Dedicated Channel ([DCH](/mobilnisite/slovnik/dch/)) nebo High-Speed Downlink Shared Channel ([HS-DSCH](/mobilnisite/slovnik/hs-dsch/)). Vypočítává se na základě různých rádiových podmínek a síťových měření, včetně poměru signálu k šumu, chybovosti bloků a dostupného výkonu. Hodnota je typicky komunikována mezi RNC a Node B prostřednictvím signalizace řídicí roviny, což umožňuje dynamické přizpůsobení přenosových parametrů, jako je Transport Format Combination ([TFC](/mobilnisite/slovnik/tfc/)) nebo profil Hybrid Automatic Repeat Request ([HARQ](/mobilnisite/slovnik/harq/)).

Hlavní úlohou QE je umožnit diferenciaci kvality služeb (QoS) a efektivní správu rádiových prostředků. Poskytnutím odhadu dosažitelné kvality může RAN upřednostnit toky s přísnějšími požadavky na QoS, jako je hlas nebo video v reálném čase, před daty s best-effort přístupem. To je klíčové pro udržení smluv o úrovni služeb a uživatelského komfortu, zejména v přetížených síťových scénářích. Mechanismus QE je nedílnou součástí schopnosti UTRAN podporovat více simultánních služeb s různými požadavky na kvalitu na sdílených rádiových prostředcích.

## K čemu slouží

Quality Estimate (QE, odhad kvality) byl zaveden ve vydání 3GPP Release 8, aby řešil potřebu sofistikovanější správy prostředí s ohledem na kvalitu v sítích UMTS a HSPA. Předchozí přístupy se často spoléhaly na jednodušší metriky, jako je hrubá datová rychlost nebo statické QoS profily, které nedostatečně zachycovaly dynamickou a pravděpodobnostní povahu podmínek rádiového kanálu. Toto omezení ztěžovalo optimalizaci využití vzácného rádiového spektra při současném plnění různorodých požadavků na kvalitu služeb.

Vznik QE byl motivován rostoucí poptávkou po smíšených typech provozu, včetně hlasu, streamování videa a interaktivních dat, z nichž každý má odlišnou citlivost na zpoždění, kolísání a chybovost. Poskytnutím standardizovaného odhadu vnímané kvality umožňuje QE RAN činit proaktivní rozhodnutí, jako je výběr vhodných transportních formátů nebo zahájení předávání spojení, ještě předtím, než dojde ke zhoršení služby. Tato proaktivní správa je nezbytná pro udržení konzistentního uživatelského komfortu a efektivity sítě.

Historicky QE zaplnil mezeru v řídicí rovině UTRAN tím, že nabídl společný jazyk pro odhad kvality mezi řídicím RNC a vykonávajícím Node B. Podporuje vývoj směrem k autonomnějším a distribuovanějším architekturám RAN tím, že poskytuje klíčový vstup pro lokální plánovací algoritmy. Zatímco jeho použití je specifické pro určitá rozhraní UTRAN a bylo z velké části nahrazeno pokročilejšími QoS mechanismy v LTE a 5G, QE představoval důležitý krok při zavádění povědomí o kvalitě do správy prostředků RAN.

## Klíčové vlastnosti

- Poskytuje kvantifikovatelný odhad očekávané kvality datového toku pro transportní kanály
- Používá se v signalizaci řídicí roviny mezi RNC a Node B přes rozhraní Iur/Iub
- Podporuje dynamické přizpůsobení transportních formátů a rozhodnutí o plánování
- Umožňuje diferenciaci QoS upřednostňováním toků na základě požadavků na kvalitu
- Integruje se s UTRAN Frame Protocol a RNSAP pro standardizovanou komunikaci
- Napomáhá efektivní správě rádiových prostředků za proměnných podmínek kanálu

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols

---

📖 **Anglický originál a plná specifikace:** [QE na 3GPP Explorer](https://3gpp-explorer.com/glossary/qe/)
