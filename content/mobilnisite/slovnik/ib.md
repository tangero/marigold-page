---
slug: "ib"
url: "/mobilnisite/slovnik/ib/"
type: "slovnik"
title: "IB – Information Block"
date: 2025-01-01
abbr: "IB"
fullName: "Information Block"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ib/"
summary: "Strukturovaný kontejner systémových informací vysílaných základnovou stanicí UMTS Node B na logickém kanálu BCCH (Broadcast Control Channel). Nese základní parametry, které UEs potřebují pro přístup a"
---

IB (informační blok) je strukturovaný kontejner systémových informací vysílaných základnovou stanicí UMTS Node B, který poskytuje základní parametry, jako je identita buňky a řízení přístupu, pro uživatelské zařízení.

## Popis

V kontextu 3GPP Universal Mobile Telecommunications System (UMTS) je Information Block (IB) základní datová struktura používaná pro vysílání systémových informací z Radio Access Network (RAN), konkrétně z Node B (základnové stanice), ke všem User Equipments (UEs) v její pokrytí. Tyto bloky jsou periodicky vysílány na logickém kanálu Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)), který je mapován na fyzický kanál Primary Common Control Physical Channel ([P-CCPCH](/mobilnisite/slovnik/p-ccpch/)). Systémové informace jsou klíčové pro UEs, aby mohly provést počáteční výběr buňky, připojit se k vhodné buňce a správně komunikovat se sítí pro služby. Informace jsou organizovány do hierarchie bloků pro optimalizaci efektivity čtení; UEs nemusí neustále dekódovat všechny informace, ale mohou podle potřeby číst konkrétní bloky.

Architektura šíření systémových informací v UMTS zahrnuje několik typů Information Blocks, z nichž každý má specifický účel. Master Information Block ([MIB](/mobilnisite/slovnik/mib/)) je první blok, který UE přečte po synchronizaci s buňkou. MIB obsahuje odkazy (plánovací informace) na jeden nebo více Scheduling Blocks (SBs), které následně poskytují plánování pro sadu System Information Blocks (SIBs). SIBs jsou hlavními nosiči skutečných parametrů systémových informací. Existuje více typů SIBs ([SIB1](/mobilnisite/slovnik/sib1/), SIB2 atd.), z nichž každý sdružuje související parametry. Například SIB1 obsahuje [NAS](/mobilnisite/slovnik/nas/) systémové informace a plánovací informace pro ostatní SIBs, SIB3 obsahuje parametry pro výběr a převýběr buňky, SIB5 obsahuje parametry pro společné fyzické kanály, SIB11 obsahuje informace pro řízení měření sousedních buněk atd. Tato modulární struktura umožňuje síti nezávisle aktualizovat různé parametry na základě jejich rychlosti změny.

Jak mechanismus IB funguje: jde o plánovaný vysílací proces. Síť určuje opakovací frekvenci a hodnotovou značku (value tag) pro každý [SIB](/mobilnisite/slovnik/sib/). MIB, který má pevný plán, ukazuje UE, kdy budou SBs a SIBs vysílány. Když se UE připojí k buňce, nejprve přečte MIB a odkazovaný SIB1. Pomocí plánovacích informací pak může selektivně číst další SIBs potřebné pro svůj stav (např. pro převýběr buňky v idle módu nebo pro navázání spojení). Pokud UE v connected módu potřebuje aktualizované systémové informace, může Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) také poslat některé SIBs přímo UE na vyhrazeném kanálu pomocí zprávy SYSTEM INFORMATION. Obsah IBs je podrobně definován ve specifikaci 3GPP 25.331 ([RRC](/mobilnisite/slovnik/rrc/) protokol), zatímco jejich přenos je popsán v 25.423 pro rozhraní Iur mezi RNCs.

## K čemu slouží

Struktura Information Block byla vyvinuta pro efektivní správu vysílání základních, ale rozsáhlých systémových informací v sítích UMTS. V dřívějších mobilních systémech byly systémové informace často vysílány méně strukturovaně, což mohlo vést k neefektivnímu využití rádiových zdrojů a zvýšené spotřebě baterie UE, protože UEs mohly potřebovat poslouchat dlouhé, monolitické vysílání, aby našly konkrétní parametr. Hierarchický systém IB to řeší tím, že umožňuje UEs rychle najít a dekódovat pouze informace relevantní pro jejich bezprostřední úkol, například najít seznam sousedních buněk pro převýběr namísto opětovného čtení všech přístupových parametrů.

Primární problém, který IBs řeší, je spolehlivé a škálovatelné šíření kritických konfiguračních dat sítě potenciálně velkému počtu UEs. Tato data zahrnují parametry nezbytné pro přístup k buňce (jako jsou informace pro řízení RACH), výběr/převýběr buňky (prahové hodnoty, frekvence sousedních buněk) a provoz v connected módu (řízení měření, konfigurace kanálů). Bez standardizovaného, dobře strukturovaného vysílacího mechanismu by UEs nemohly autonomně vybrat nejlepší buňku, což by vedlo ke špatnému výkonu sítě, přerušeným hovorům a neefektivnímu využití rádiových zdrojů. Systém IB poskytuje předvídatelný plán a jasnou strukturu, což umožňuje UEs od různých výrobců bezproblémově spolupracovat se sítí.

Představený se specifikacemi UMTS v 3GPP Release 99 (často seskupený pod Rel-8 pro přehlednost v některých kontextech) koncept IB vycházel ze zkušeností s GSM, ale byl navržen pro složitější rozhraní Wideband CDMA (W-CDMA) a rozdělenou architekturu RAN s Node B a RNC. Vytvořil základ pro vysílání systémových informací, který se ukázal jako robustní a přizpůsobivý, ovlivňující pozdější generace; koncepčně podobná, ale vylepšená struktura system information block (SIB) se používá v LTE a NR (5G), ačkoli s odlišným mapováním kanálů a obsahem přizpůsobeným těmto technologiím. Systém IB v UMTS byl klíčový pro umožnění funkcí, jako je efektivní mobilita v idle módu, hierarchické buněčné struktury a zavádění nových služeb tím, že poskytoval flexibilní kontejner pro vysílání nových parametrů s vývojem standardu.

## Klíčové vlastnosti

- Hierarchická struktura zahrnující Master IB, Scheduling Blocks a System Information Blocks (SIBs)
- Periodické vysílání na BCCH/P-CCPCH pro všechna UEs v buňce
- Nese základní parametry pro výběr buňky, přístup, převýběr a provoz v connected módu
- Modulární návrh umožňuje nezávislé plánování a aktualizaci různých skupin parametrů
- Obsahuje plánovací informace uvnitř bloků pro zefektivnění čtení UE
- Může být také zasílán na vyhrazených kanálech UEs v connected módu prostřednictvím signalizace RNC

## Související pojmy

- [SIB – System Information Block](/mobilnisite/slovnik/sib/)
- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification

---

📖 **Anglický originál a plná specifikace:** [IB na 3GPP Explorer](https://3gpp-explorer.com/glossary/ib/)
