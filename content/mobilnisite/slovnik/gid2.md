---
slug: "gid2"
url: "/mobilnisite/slovnik/gid2/"
type: "slovnik"
title: "GID2 – Group Identifier (level 2)"
date: 2025-01-01
abbr: "GID2"
fullName: "Group Identifier (level 2)"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gid2/"
summary: "GID2 je sekundární skupinový identifikátor uložený na kartě USIM/UICC v souboru EF(GID2). Poskytuje dodatečné, operátorem definované kritérium pro seskupení nad rámec GID1, což umožňuje podrobnější ka"
---

GID2 je sekundární, operátorem definovaný skupinový identifikátor uložený na kartě USIM, který umožňuje podrobnější kategorizaci účastníků nebo samostatné klasifikační schémata nad rámec primárního GID1.

## Popis

Group Identifier level 2 (GID2) je doplňkový identifikátor k [GID1](/mobilnisite/slovnik/gid1/), definovaný v rámci specifikací UICC a USIM od 3GPP. Nachází se ve vlastním vyhrazeném elementárním souboru, [EF](/mobilnisite/slovnik/ef/)(GID2), v rámci souborového systému aplikace USIM na UICC. Stejně jako GID1 je GID2 datové pole zřízené sítí, zapsané mobilním operátorem, a jeho formát a význam jsou specifické pro operátora. Přítomnost dvou skupinových identifikátorů umožňuje vícerozměrné nebo hierarchické seskupování účastníků.

Z technického pohledu funguje GID2 stejně jako GID1 z hlediska přístupových mechanismů. Mobilní zařízení nebo síť k němu přistupuje vydáním příkazu READ BINARY pro identifikátor souboru EF(GID2). Aplikace USIM načte uložená data a vrátí je. Síťová infrastruktura, jako je [MSC](/mobilnisite/slovnik/msc/), SGSN nebo [MME](/mobilnisite/slovnik/mme/), může tento identifikátor přečíst během procedur připojení a zahrnout jej do signalizačních zpráv směrem k [HSS](/mobilnisite/slovnik/hss/). HSS pak může použít kombinaci GID1 a GID2, nebo každý zvlášť, k odkazování na profil účastníka, který určuje parametry služeb.

Z architektonického hlediska přidává GID2 druhou osu pro klasifikaci účastníků v rámci servisní logiky jádra sítě. Například operátor může použít GID1 k označení typu tarifního plánu (např. spotřebitelský, firemní, M2M) a GID2 k označení podskupiny v rámci tohoto plánu, jako je konkrétní ID korporátního zákazníka, kategorie typu zařízení nebo geografická servisní zóna. To umožňuje složitější a podrobnější rozhodování o politikách. Síťové funkce, jako je Policy and Charging Rules Function (PCRF), mohou tyto identifikátory použít k výběru příslušných pravidel kvality služeb (QoS) a účtování.

Její role v síti spočívá v poskytnutí větší flexibility pro správu účastníků a diferenciaci služeb. Zatímco GID1 nabízí primární seskupení, GID2 umožňuje sekundární, nezávislou klasifikaci. To je klíčové pro sofistikované nabídky služeb, vrstvené řízení přístupu a podrobné analýzy. Podporuje scénáře, kdy účastník patří do více překrývajících se skupin (např. vozidlo patřící jak do skupiny 'řízení vozového parku', tak do skupiny 'data s vysokou prioritou'), aniž by bylo nutné tyto koncepty slučovat do jediného identifikátoru, čímž se zachovává přehlednost v provozních a obchodních podpůrných systémech.

## K čemu slouží

GID2 byl vytvořen, aby řešil omezení spočívající v existenci pouze jediného skupinového identifikátoru ([GID1](/mobilnisite/slovnik/gid1/)), které se ukázalo jako nedostatečné pro složité balíčky služeb a víceúrovňové strategie správy účastníků, které se objevily s vývojem mobilních sítí. Operátoři potřebovali způsob, jak uplatnit více nezávislých klasifikačních kritérií na jedno předplatné. Například předplatné mohlo být součástí firemního účtu (první skupina) a zároveň mít povolený konkrétní balíček funkcí, jako je mezinárodní roaming (druhá skupina). Použití pouze GID1 by nutilo zakódovat oba atributy do jedné hodnoty, což by činilo logiku těžkopádnou a nepružnou.

Zavedení GID2 poskytlo přímočaré řešení: druhé nezávislé pole na SIM kartě pro kategorizaci. Toto bylo motivováno rostoucí rozmanitostí mobilních služeb a zařízení v rané éře 3G (Release 4). Vyřešilo problém vytváření hierarchických nebo vícerozměrných skupinových politik. Se dvěma identifikátory mohli operátoři navrhnout logičtější a škálovatelnější skupinovou strukturu – používat jeden pro primární obchodní vztah a druhý pro technickou nebo služebně specifickou klasifikaci.

Tento vývoj odrážel potřebu větší výraznosti v profilech účastníků přímo na SIM kartě. GID2 spolu s GID1 umožnily operátorům implementovat sofistikovanou servisní logiku bez neustálých dotazů na backendové databáze během rutinních procedur. Umožnily efektivní, SIM-kartou řízené spouštění síťových funkcí pro složité komerční nabídky, nasazení komunikace typu stroj-stroj s různými úrovněmi služeb a partnerství, kde účastníci potřebovali identity v několika překrývajících se doménách. V podstatě GID2 poskytl úroveň podrobnosti potřebnou pro novou generaci segmentovaných mobilních služeb.

## Klíčové vlastnosti

- Uložen v samostatném elementárním souboru EF(GID2) na USIM/UICC
- Poskytuje sekundární, operátorem definované kritérium pro seskupení nezávislé na GID1
- Přístupný prostřednictvím standardního rozhraní příkazů UICC pro čtení elementárních souborů
- Umožňuje vícerozměrnou nebo hierarchickou kategorizaci účastníků
- Umožňuje složitou servisní logiku a pravidla politik založená na členství ve více skupinách
- Podporuje podrobné rozlišování služeb pro pokročilé komerční nabídky a nabídky M2M

## Související pojmy

- [GID1 – Group Identifier (level 1)](/mobilnisite/slovnik/gid1/)
- [EF – Elementary File](/mobilnisite/slovnik/ef/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.022** (Rel-19) — ME Personalisation Features for GSM/3G

---

📖 **Anglický originál a plná specifikace:** [GID2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/gid2/)
