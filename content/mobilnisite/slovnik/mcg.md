---
slug: "mcg"
url: "/mobilnisite/slovnik/mcg/"
type: "slovnik"
title: "MCG – Master Cell Group"
date: 2025-01-01
abbr: "MCG"
fullName: "Master Cell Group"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mcg/"
summary: "V duální konektivitě je MCG skupina obsluhujících buněk asociovaných s hlavním uzlem (Master Node, např. LTE eNB nebo NR gNB), která poskytuje primární buňku (PCell) a případně sekundární buňky (SCell"
---

MCG je skupina obsluhujících buněk asociovaných s hlavním uzlem (Master Node) v režimu duální konektivity, která poskytuje primární buňku a případně i sekundární buňky pro UE připojené současně ke dvěma uzlům.

## Popis

Skupina hlavních buněk (Master Cell Group, MCG) je klíčový koncept v rámcích duální konektivity ([DC](/mobilnisite/slovnik/dc/)) a multi-radio duální konektivity ([MR-DC](/mobilnisite/slovnik/mr-dc/)) podle 3GPP, zavedený ve vydání 12. Definuje soubor obsluhujících buněk asociovaných s hlavním uzlem (Master Node, [MN](/mobilnisite/slovnik/mn/)). Hlavní uzel je rádiový přístupový uzel, který ukončuje alespoň spojení řídicí roviny k jádru sítě (např. přes rozhraní S1-MME nebo NG-C). V rámci MCG je jedna buňka určena jako primární buňka (Primary Cell, PCell). PCell je kotvou pro spojení UE; zajišťuje klíčovou signalizaci řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)), získávání systémových informací a slouží jako primární bod pro správu mobility a bezpečnostní procedury. MCG může také zahrnovat jednu nebo více sekundárních buněk (Secondary Cells, SCells) pro poskytnutí dodatečné šířky pásma prostřednictvím agregace nosných, přičemž všechny jsou řízeny stejným hlavním uzlem. MCG funguje ve spojení se skupinou sekundárních buněk (Secondary Cell Group, SCG), která je asociována s vedlejším uzlem (Secondary Node, SN). UE udržuje jediné RRC spojení, řízené hlavním uzlem, ale může využívat rádiové prostředky jak z MCG, tak ze SCG pro zvýšené přenosové rychlosti a spolehlivost.

Z architektonické perspektivy je fungování MCG definováno napříč více protokolovými vrstvami. Na vrstvě RRC (specifikované v TS 36.331 pro LTE a TS 38.331 pro NR) hlavní uzel generuje RRC zprávy, které konfigurují MCG a SCG, včetně přidání, modifikace nebo uvolnění SCells v rámci MCG. Na vrstvě konvergenčního protokolu paketových dat (Packet Data Convergence Protocol, PDCP) může hlavní uzel hostovat PDCP entity pro rozdělené přenašeče (split bearers), kde jsou data směrována jak do MCG, tak do SCG pro přenos. Vrstvy řízení rádiového spoje (Radio Link Control, RLC) a řízení přístupu k médiu (Medium Access Control, [MAC](/mobilnisite/slovnik/mac/)) v hlavním uzlu spravují logické kanály, hybridní [ARQ](/mobilnisite/slovnik/arq/) a plánování specificky pro buňky v rámci MCG. Specifikace fyzické vrstvy (např. TS 36.101, 38.101) definují požadavky na RF pro provoz UE na nosných MCG.

Role MCG je klíčová pro zajištění plynulé mobility a kontinuity relace. Během procedur předávání v MR-DC scénářích se MCG může změnit, pokud je změněn hlavní uzel, což zahrnuje předání PCell. Síť může rekonfigurovat složení MCG (např. přidáním nebo odebráním SCells) na základě rádiových podmínek, vytížení a schopností UE. Ve scénářích jako [EN-DC](/mobilnisite/slovnik/en-dc/) (E-UTRA-NR Dual Connectivity), kde hlavním uzlem je LTE [eNB](/mobilnisite/slovnik/enb/) a SCG je asociována s NR gNB, poskytuje MCG založená na LTE kotvu řídicí roviny a často přenáší kritickou signalizaci a potenciálně i některá data uživatelské roviny. Správa a výkon MCG jsou kritické pro celkový výkon duální konektivity, ovlivňují propustnost, latenci a odolnost spojení.

## K čemu slouží

Skupina hlavních buněk (MCG) byla zavedena, aby řešila rostoucí poptávku po vyšších přenosových rychlostech, lepší spektrální účinnosti a robustnější konektivitě, než jakou mohla poskytnout agregace nosných v rámci jediného uzlu. Před duální konektivitou bylo UE připojeno k jedné základnové stanici (eNodeB v LTE) a využívalo agregaci nosných v rámci buněk této stanice. Tento přístup měl omezení ve využití oddělených pásem spektra vlastněných různými síťovými uzly nebo v hustých nasazeních, kde mohlo být UE v dosahu více vysílacích bodů. Duální konektivita a následně rozdělení MCG/SCG byly vytvořeny, aby umožnily UE současně využívat rádiové prostředky ze dvou různých uzlů propojených přes neideální přenosovou síť (backhaul, např. rozhraní X2 nebo Xn).

Primární problém, který řeší, je agregace prostředků napříč geograficky oddělenými uzly, což je zvláště cenné pro využití jak makro, tak small cell vrstev. MCG, ukotvená k hlavnímu uzlu (často makro buňce), poskytuje stabilní spojení řídicí roviny a spolehlivost pokrytí. To umožňuje vedlejšímu uzlu (často small cell) soustředit se na doručování uživatelských dat s vysokou kapacitou. Toto oddělení funkcí zlepšuje výkon sítě bez kompromisů ve správě mobility. Koncept byl zásadní pro plynulou evoluci z LTE na 5G NR, umožňující architektury jako EN-DC, kde stávající LTE síť (jako MCG) poskytuje kotvu řídicí roviny pro počáteční nasazení 5G NR, zajišťuje pokrytí a možnost návratu, zatímco NR SCG poskytuje vylepšenou mobilní širokopásmovou službu.

Dále framework MCG poskytuje strukturovaný způsob správy složitosti. Jasně vymezuje odpovědnosti za řízení (hlavní uzel zpracovává RRC) a umožňuje flexibilní architektury uživatelské roviny (MCG bearer, SCG bearer, split bearer). Tím řeší omezení dřívějších schémat koordinovaného vícebodového přenosu (CoMP), která vyžadovala velmi nízkolatenční, ideální backhaul. Tolerancí vyšší latence backhaulu mezi hlavním a vedlejším uzlem se duální konektivita s MCG/SCG stala praktičtějším a nasaditelnějším řešením pro zvýšení kapacity v reálných sítích.

## Klíčové vlastnosti

- Obsahuje primární buňku (PCell), která je kotvou řídicí roviny pro RRC spojení UE.
- Může zahrnovat jednu nebo více sekundárních buněk (SCells) pro agregaci nosných v rámci spektra hlavního uzlu.
- Asociovaný hlavní uzel (Master Node) ukončuje spojení řídicí roviny k jádru sítě (např. NG-C nebo S1-MME).
- Spolupracuje se skupinou sekundárních buněk (SCG) v režimu duální konektivity nebo MR-DC.
- Podporuje architekturu rozděleného přenašeče (split bearer), kde vrstva PDCP v hlavním uzlu může směrovat data na rádiová spojení MCG i SCG.
- Je klíčová pro procedury mobility; předání hlavního uzlu zahrnuje znovuustavení nové MCG.

## Související pojmy

- [MR-DC – Multi-Radio Dual Connectivity](/mobilnisite/slovnik/mr-dc/)

## Definující specifikace

- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 33.825** (Rel-16) — Security for 5G URLLC Services
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.323** (Rel-19) — PDCP Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 36.842** (Rel-12) — Small Cell Enhancements for LTE Higher Layers
- **TS 36.875** (Rel-13) — Dual Connectivity Extension Requirements
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 37.483** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [MCG na 3GPP Explorer](https://3gpp-explorer.com/glossary/mcg/)
