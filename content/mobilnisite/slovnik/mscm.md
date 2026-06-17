---
slug: "mscm"
url: "/mobilnisite/slovnik/mscm/"
type: "slovnik"
title: "MSCM – Mobile Station Class Mark"
date: 2025-01-01
abbr: "MSCM"
fullName: "Mobile Station Class Mark"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mscm/"
summary: "Zastaralý identifikátor používaný v GSM a raných vydáních 3GPP ke klasifikaci schopností mobilní stanice, jako je její výkonová třída a podporovaná kmitočtová pásma. Byl vysílán MS (mobilní stanicí) d"
---

MSCM je zastaralý identifikátor používaný v GSM a raných vydáních 3GPP ke klasifikaci schopností mobilní stanice, jako je její výkonová třída a podporovaná kmitočtová pásma, pro poskytování služeb a správu rádiových prostředků.

## Popis

Mobile Station Class Mark (MSCM) je parametr definovaný v raných specifikacích 3GPP, primárně pro GSM a jeho vývoj. Jedná se o informaci uloženou v mobilní stanici ([MS](/mobilnisite/slovnik/ms/)) a předávanou síti, konkrétně základnové stanici ([BSS](/mobilnisite/slovnik/bss/)) a jádru sítě. MSCM slouží jako identifikátor schopností, který kategorizuje mobilní zařízení na základě jeho technických charakteristik. Tato klasifikace umožňuje síti pochopit omezení a vlastnosti zařízení bez nutnosti rozsáhlé výměny informací o schopnostech pro každou transakci.

Z architektonického hlediska je MSCM součástí nevolatilní paměti mobilního zařízení a je zahrnut v určitých signalizačních zprávách během procedur, jako je aktualizace polohy, navázání hovoru nebo správa mobility. Když MS přistupuje k síti, poskytne svůj MSCM, který může [BSC](/mobilnisite/slovnik/bsc/) (Base Station Controller) a [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre) zpracovat. Síť tyto informace využívá k rozhodnutím týkajícím se přidělování rádiových kanálů, parametrů předávání hovoru (handover) a dostupnosti služeb. Například mobil s konkrétní výkonovou třídou uvedenou v MSCM by měl přiděleny odpovídající prahové hodnoty pro převýběr buňky.

MSCM typicky kóduje informace jako výkonová třída mobilu (definující jeho maximální vysílací výkon), podporovaná kmitočtová pásma (např. 900 MHz, 1800 MHz) a případně další rané funkce specifické pro GSM. Jedná se o relativně statický identifikátor, na rozdíl od dynamických informací o relaci. Jeho role byla klíčová v éře jednodušších mobilních zařízení a sítí, neboť poskytovala přímočarý mechanismus pro optimalizaci sítě a zajišťovala, že služby nebyly požadovány od zařízení, které je nebylo schopno podporovat. Jak se sítě vyvíjely směrem k UMTS a LTE, byly zavedeny sofistikovanější a flexibilnější mechanismy výměny informací o schopnostech, jako je UE Capability Information, což učinilo MSCM z velké části zastaralým.

## K čemu slouží

MSCM byl vytvořen pro uspokojení potřeby základní informovanosti o schopnostech zařízení v raných digitálních celulárních sítích, konkrétně GSM. Před standardizovanými identifikátory schopností měly sítě omezené znalosti o připojených mobilních stanicích, což mohlo vést k neefektivnímu využití prostředků nebo selhání služeb. Síť se například mohla pokusit předat hovor do kmitočtového pásma, na kterém mobil nemohl vysílat, nebo přidělit výkonovou úroveň, které zařízení nemohlo dosáhnout.

Jeho účelem bylo tyto problémy řešit poskytnutím kompaktní, standardizované třídní značky (class mark), která kategorizuje mobily do skupin s podobnými schopnostmi. To umožnilo síťové infrastruktuře přizpůsobit své chování odpovídajícím způsobem. Historickým kontextem byl přechod od analogových k digitálním GSM systémům, kde byl vyžadován strukturovanější přístup ke správě mobilů. MSCM umožnil základní optimalizaci sítě a pomáhal zajistit spolehlivé poskytování služeb tím, že přizpůsoboval síťové akce omezením zařízení.

Omezení, která řešil, byla nedostatek podrobných znalostí o zařízení a neefektivita zacházení se všemi mobily stejně. MSCM však byl relativně hrubozrnným řešením. Seskupoval zařízení do tříd spíše než aby vyjmenovával jednotlivé schopnosti. To motivovalo vývoj podrobnějších a flexibilnějších procedur informací o schopnostech UE (UE capability) v pozdějších vydáních 3GPP, které mohly popsat široké spektrum funkcí pro komplexní smartphony a datové služby, čímž koncept MSCM v konečném důsledku nahradily.

## Klíčové vlastnosti

- Klasifikuje výkonové schopnosti mobilní stanice
- Udává podporovaná rádiová kmitočtová pásma
- Přenášen v signalizačních zprávách do sítě
- Používán pro rozhodování v rámci správy rádiových prostředků
- Statický identifikátor uložený v mobilním zařízení
- Umožňuje základní přizpůsobení síťových služeb

## Související pojmy

- [MS – Mobile Station](/mobilnisite/slovnik/ms/)
- [BSS – Base Station Subsystem](/mobilnisite/slovnik/bss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [MSCM na 3GPP Explorer](https://3gpp-explorer.com/glossary/mscm/)
