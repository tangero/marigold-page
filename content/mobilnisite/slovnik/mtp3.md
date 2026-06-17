---
slug: "mtp3"
url: "/mobilnisite/slovnik/mtp3/"
type: "slovnik"
title: "MTP3 – Message Transfer Part layer 3"
date: 2025-01-01
abbr: "MTP3"
fullName: "Message Transfer Part layer 3"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mtp3/"
summary: "MTP3 je síťová vrstva protokolu SS7, zodpovědná za směrování signalizačních zpráv přes signalizační síť a za správu dostupnosti signalizačních spojů a tras. Poskytuje funkce jako rozlišování, distribu"
---

MTP3 je síťová vrstva protokolu SS7, která směruje signalizační zprávy a spravuje dostupnost signalizačních spojů a tras v síti.

## Popis

Message Transfer Part layer 3 (MTP3) funguje na síťové vrstvě zásobníku protokolu SS7. Zatímco [MTP2](/mobilnisite/slovnik/mtp2/) spravuje jednotlivé spojení, MTP3 spravuje celou signalizační síť složenou z mnoha spojů a uzlů. Jeho hlavní funkce jsou zpracování signalizačních zpráv a správa signalizační sítě. MTP3 poskytuje nespojovanou, spolehlivou přenosovou službu pro různé Uživatelské části (jako [ISUP](/mobilnisite/slovnik/isup/), SCCP a v 3GPP [MAP](/mobilnisite/slovnik/map/) a [CAP](/mobilnisite/slovnik/cap/)) napříč složitými síťovými topologiemi.

MTP3 funguje prostřednictvím několika klíčových procesů. Nejprve Rozlišování zpráv (Message Discrimination) zkoumá cílový kód bodu (Destination Point Code, [DPC](/mobilnisite/slovnik/dpc/)) ve směrovací hlavičce příchozí zprávy. Pokud DPC odpovídá kódu místního uzlu, je zpráva předána Distribuci zpráv (Message Distribution) pro doručení příslušné Uživatelské části (např. SCCP). Pokud je DPC odlišný, je zpráva předána Směrování zpráv (Message Routing), které na základě směrovacích tabulek a cílového kódu bodu vybere odchozí signalizační spoj, čímž zajišťuje předání zprávy směrem k jejímu konečnému cíli. To umožňuje více-skokové směrování přes přenosové signalizační body (Signal Transfer Points, STP).

Druhou hlavní složkou je Správa signalizační sítě (Signaling Network Management, SNM), která je klíčová pro odolnost. SNM průběžně sleduje stav signalizačních spojů a tras. Pokud MTP2 indikuje výpadek spoje, funkce SNM v MTP3 zahájí činnost. Provádějí procedury přechodu (changeover) pro přesměrování provozu z nefunkčního spoje na náhradní spoj ve stejné skupině spojů, nebo návrat (changeback) při jeho obnovení. Při závažnějších výpadcích může řídit vynucené nebo řízené přeměrování provozu na alternativní trasy přes různé STP a odpovídajícím způsobem upravovat směrovací tabulky (blokování a povolování správy). Tím je zajištěno, že signalizační síť zůstane funkční i přes poruchy.

V architektuře sítě 3GPP se MTP3 nachází v síťových prvcích jako [MSC](/mobilnisite/slovnik/msc/), SGSN, [HLR](/mobilnisite/slovnik/hlr/) a samostatných STP. Spolupracuje se Signalizační spojovací řídicí částí (Signaling Connection Control Part, SCCP), která poskytuje rozšířenou adresaci (globální tituly) a spojované služby. Společně MTP3 a SCCP tvoří kompletní signalizační přenos pro klíčové mobilní protokoly. Směrovací schopnosti MTP3 umožňují, aby se MSC v jedné zemi dotazovalo na HLR v jiné zemi prostřednictvím mezinárodních STP, což umožňuje globální roaming.

## K čemu slouží

MTP3 bylo vytvořeno k řešení problému škálovatelného a spolehlivého doručování zpráv ve velké, víceuzlové signalizační síti. [MTP2](/mobilnisite/slovnik/mtp2/) řeší pouze spojení bod-bod, ale národní nebo mezinárodní síť vyžaduje, aby byly zprávy směrovány přes mezilehlé uzly. Účelem MTP3 je poskytnout tuto schopnost směrování na síťové vrstvě, analogicky k IP směrování, ale pro oblast signalizace v okruhově komutovaných sítích.

Řeší omezení nesměrovaných signalizačních systémů zavedením hierarchické adresace pomocí Kódů bodů (Point Codes), které jednoznačně identifikují každý signalizační bod v síti. To umožňuje vytváření složitých síťových topologií typu mesh nebo hierarchických s redundancí. Jeho sofistikované funkce Správy signalizační sítě navíc řeší kritický problém odolnosti sítě. Telekomunikační signalizace musí být vysoce dostupná; výpadek jediného spoje nebo trasy nesmí způsobit rozsáhlý výpadek služeb. Automatické přeměrování provozu a správa spojů v MTP3 zajišťují samoopravu sítě a udržení kontinuity služeb.

Pro 3GPP byl účel zahrnutí MTP3 využití stávající, robustní a globálně propojené sítě SS7 pro mobilní služby. Poskytlo to osvědčené mechanismy směrování a přepojování při výpadku potřebné pro spolehlivý provoz mezi systémy (např. mezi navštíveným MSC a domácím HLR). To umožnilo mobilním operátorům bezproblémově propojit své sítě od prvního dne a podporovat nezbytné služby jako roaming a předávání mezi systémy bez nutnosti vytvářet nový směrovací protokol. Pozdější přesun k plně-IP jádru (IMS, VoLTE) motivoval vývoj IP adaptací jako M3UA v SIGTRAN, které emulují služby MTP3 přes IP.

## Klíčové vlastnosti

- Provádí směrování zpráv na základě cílového kódu bodu (Destination Point Code, DPC) a směrovacích tabulek
- Provádí rozlišování a distribuci zpráv v cílovém uzlu
- Spravuje stav signalizační sítě pomocí procedur Přechod (Changeover), Návrat (Changeback) a Přeměrování (Rerouting)
- Poskytuje řízení toku signalizačního provozu při scénářích zahlcení
- Podporuje přenos zpráv Uživatelských částí (např. do/z SCCP, ISUP)
- Udržuje a aktualizuje stav dostupnosti signalizačních tras

## Související pojmy

- [MTP2 – Message Transfer Part layer 2](/mobilnisite/slovnik/mtp2/)
- [M3UA – SS7 MTP3 – User Adaptation Layer](/mobilnisite/slovnik/m3ua/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 29.202** (Rel-19) — SS7 Signalling Transport Protocol Architectures
- **TS 29.232** (Rel-19) — Mc Interface Protocol Profile
- **TS 43.318** (Rel-19) — Generic Access Network (GAN) Stage 2
- **TR 43.902** (Rel-19) — GAN Enhancements Feasibility Study
- **TS 44.318** (Rel-19) — Generic Access Network (GAN) Interface Procedures

---

📖 **Anglický originál a plná specifikace:** [MTP3 na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtp3/)
