---
slug: "hdop"
url: "/mobilnisite/slovnik/hdop/"
type: "slovnik"
title: "HDOP – Horizontal Dilution Of Precision"
date: 2025-01-01
abbr: "HDOP"
fullName: "Horizontal Dilution Of Precision"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/hdop/"
summary: "Bezrozměrná metrika v satelitní navigaci, která kvantifikuje geometrickou kvalitu satelitních konstelací používaných pro určení polohy. Nižší hodnota HDOP označuje lepší geometrii satelitů a vyšší pot"
---

HDOP je bezrozměrná metrika v satelitní navigaci, která kvantifikuje geometrickou kvalitu satelitních konstelací, přičemž nižší hodnota označuje lepší geometrii a vyšší potenciální přesnost horizontálního určení polohy.

## Popis

Horizontal Dilution of Precision (HDOP) je klíčový parametr v globálních navigačních satelitních systémech ([GNSS](/mobilnisite/slovnik/gnss/)), jako jsou [GPS](/mobilnisite/slovnik/gps/), Galileo nebo [GLONASS](/mobilnisite/slovnik/glonass/), který měří geometrickou kvalitu satelitní konstelace vzhledem k poloze přijímače. Jde o bezrozměrný škálovací faktor, který ovlivňuje přesnost výpočtu horizontální polohy (zeměpisné šířky a délky). HDOP vyplývá z geometrie satelitů použitých při výpočtu polohy; když jsou satelity na obloze těsně seskupeny, je geometrie slabá, což vede k vyššímu HDOP a větším potenciálním chybám polohy. Naopak, když jsou satelity rozptýleny, je geometrie silná, což vede k nižšímu HDOP a lepší horizontální přesnosti. Matematicky je HDOP odvozen z kovarianční matice odhadu metodou nejmenších čtverců používaného při výpočtu polohy, konkrétně odráží nejistotu v horizontální rovině.

Ve specifikacích 3GPP je HDOP zmíněn v kontextu služeb určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) a lokalizačních metod pro mobilní zařízení. Používá se k posouzení kvality určení polohy založeného na GNSS, což je nedílnou součástí služeb, jako je nouzové volání (např. E911), navigace a aplikace založené na poloze. Normy 3GPP definují požadavky a testovací postupy pro výkon určování polohy UE, přičemž HDOP je kritickým faktorem pro dosažitelnou přesnost. Například specifikace mohou stanovovat minimální prahové hodnoty HDOP během testování shody, aby bylo zajištěno, že zařízení mohou poskytovat spolehlivé informace o poloze za různých satelitních geometrií. Hodnoty HDOP jsou typicky hlášeny spolu s odhady polohy, aby poskytly indikaci spolehlivosti horizontální přesnosti.

Úloha HDOP v sítích 3GPP spočívá v umožnění přesného a spolehlivého určování polohy tím, že kvantifikuje dopad satelitní geometrie na lokalizační fixy. Je součástí širší skupiny parametrů Dilution of Precision (DOP), která zahrnuje Vertical DOP (VDOP) pro přesnost nadmořské výšky a Position DOP (PDOP) pro celkovou 3D přesnost. Sledováním HDOP mohou síťové prvky a aplikace činit informovaná rozhodnutí, například vyžádat si další lokalizační metody (např. asistovaný GNSS nebo síťové techniky), když je HDOP vysoký, aby byla zachována kvalita služby. To je zvláště důležité pro aplikace kritické z hlediska bezpečnosti, kde je přesná poloha prvořadá.

## K čemu slouží

HDOP byl vyvinut jako součást analýzy chyb [GNSS](/mobilnisite/slovnik/gnss/) za účelem kvantifikace toho, jak satelitní geometrie ovlivňuje přesnost určování polohy. Před jeho formalizací měli uživatelé satelitní navigace omezený vhled do toho, proč se chyby polohy liší, a často připisovali nepřesnosti výhradně problémům se signálem. HDOP poskytl matematický rámec pro vysvětlení a predikci těchto variací na základě prostorového rozložení satelitů, což umožnilo lepší návrh systému a větší povědomí uživatelů o spolehlivosti polohy.

V rámci 3GPP je HDOP začleněn za účelem vylepšení služeb založených na poloze a splnění regulatorních požadavků na mobilní lokalizaci, jako je určení polohy nouzového volajícího. Jak se mobilní sítě vyvíjely, aby podporovaly pokročilé [LCS](/mobilnisite/slovnik/lcs/), přesné určování polohy zařízení se stalo klíčovým pro aplikace od navigace až po veřejnou bezpečnost. HDOP umožňuje sítím a zařízením vyhodnocovat kvalitu GNSS fixů a řešit omezení, kdy špatná satelitní geometrie může vést k nepřijatelným chybám polohy. Specifikací HDOP v testovacích a výkonnostních kritériích 3GPP zajišťuje, že UE mohou poskytovat konzistentní přesnost polohy v reálných podmínkách.

Motivace pro zahrnutí HDOP do norem 3GPP vychází z potřeby spolehlivého určování polohy v různorodých prostředích, kde může být viditelnost satelitů omezena. Řeší problém nepředvídatelné přesnosti polohy tím, že poskytuje měřitelnou metriku, která usměrňuje použití hybridních lokalizačních metod. To podporuje vytváření robustních architektur LCS, které využívají více technologií k dosažení požadovaných úrovní přesnosti, což nakonec zlepšuje uživatelský zážitek a soulad s požadavky na lokalizaci.

## Klíčové vlastnosti

- Kvantifikuje geometrickou kvalitu satelitních konstelací pro horizontální určení polohy
- Bezrozměrný škálovací faktor ovlivňující přesnost zeměpisné šířky a délky
- Odvozeno z kovarianční matice při odhadu polohy v GNSS
- Používá se k posouzení spolehlivosti lokalizačních fixů pro služby určování polohy 3GPP
- Nižší hodnoty označují lepší satelitní geometrii a vyšší potenciální přesnost
- Nedílná část rodiny Dilution of Precision (DOP), která zahrnuje VDOP a PDOP

## Související pojmy

- [GNSS – Global Navigation Satellite System](/mobilnisite/slovnik/gnss/)

## Definující specifikace

- **TS 25.171** (Rel-19) — A-GPS Minimum Performance Requirements for UTRA FDD UE
- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements
- **TS 45.005** (Rel-19) — GSM RF Requirements for MS and BSS

---

📖 **Anglický originál a plná specifikace:** [HDOP na 3GPP Explorer](https://3gpp-explorer.com/glossary/hdop/)
