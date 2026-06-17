---
slug: "e-slp"
url: "/mobilnisite/slovnik/e-slp/"
type: "slovnik"
title: "E-SLP – Emergency SUPL Location Platform"
date: 2025-01-01
abbr: "E-SLP"
fullName: "Emergency SUPL Location Platform"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/e-slp/"
summary: "Specializovaná lokalizační platforma v sítích 3GPP, která podporuje tísňové služby poskytováním přesných polohových informací pro tísňová volání. Integruje se s SUPL, aby umožnila služby založené na p"
---

E-SLP je specializovaná lokalizační platforma podle 3GPP, která podporuje tísňové služby poskytováním přesných polohových informací pro tísňová volání. Integruje se s architekturou SUPL (Secure User Plane Location) a umožňuje tak služby založené na poloze pro účely veřejné bezpečnosti.

## Popis

Emergency SUPL Location Platform (E-SLP) je síťová entita definovaná ve specifikacích 3GPP, která poskytuje lokalizační služby speciálně pro tísňové scénáře. Je součástí architektury Secure User Plane Location (SUPL), která pro určování polohy využívá signalizaci na uživatelské rovině (user plane) založenou na IP namísto tradičních metod na řídicí rovině (control plane). E-SLP funguje jako vyhrazený server, který komunikuje s uživatelským zařízením (UE), přístupovými sítěmi a sítěmi tísňových služeb za účelem určení a doručení zeměpisné polohy volajícího během tísňového volání, jako je 911 nebo 112. Podporuje různé lokalizační technologie včetně [GPS](/mobilnisite/slovnik/gps/), [A-GPS](/mobilnisite/slovnik/a-gps/) a síťových metod jako [OTDOA](/mobilnisite/slovnik/otdoa/), aby dosáhla vysoké přesnosti a spolehlivosti.

Z architektonického hlediska se E-SLP skládá z klíčových komponent, jako je SUPL Location Center (SLC) a SUPL Positioning Center (SPC). SLC zajišťuje správu relací, autentizaci a komunikaci s UE, zatímco SPC provádí vlastní výpočet polohy na základě měření z UE a sítě. Během tísňového volání UE naváže zabezpečené IP spojení s E-SLP pomocí protokolů SUPL (např. SUPL INIT, SUPL POS). E-SLP koordinuje s UE sběr polohových dat, jako jsou satelitní signály nebo měření z mobilní sítě, tato data zpracuje pro výpočet polohy a následně je předá do Public Safety Answering Point (PSAP) nebo jiným tísňovým subjektům. Tento proces probíhá na uživatelské rovině a využívá existující datová spojení pro vyšší efektivitu.

Jak to funguje: Když uživatel uskuteční tísňové volání, síť spustí získání polohy prostřednictvím E-SLP. UE obdrží od E-SLP inicializační zprávu SUPL, která zahájí lokalizační relaci. UE a E-SLP si vyměňují zprávy za účelem shromáždění potřebných měření, což může zahrnovi asistenční data od E-SLP pro zlepšení rychlosti a přesnosti. Jakmile je poloha vypočtena, E-SLP ji zabezpečeně přenese do infrastruktury tísňových služeb. To umožňuje dispečerům přesně určit polohu volajícího, i když ji volající nemůže sdělit slovně. Role E-SLP je v moderní telekomunikaci klíčová, protože zajišťuje, aby byly polohové informace dostupné rychle a přesně pro záchranné zásahy, a splňuje tak regulatorní požadavky na tísňové služby.

## K čemu slouží

E-SLP byl vyvinut pro řešení potřeby spolehlivého a přesného určování polohy v tísňových situacích v sítích 3GPP. Před jeho zavedením se tísňové lokalizační služby často opíraly o metody na řídicí rovině, které mohly být pomalejší, méně škálovatelné a omezené co do přesnosti. S růstem mobilní komunikace a regulatorními požadavky (např. E911 v USA, E112 v Evropě) vzrůstal tlak na poskytování přesné polohy volajícího pro veřejnou bezpečnost. Architektura SUPL nabídla alternativu na uživatelské rovině, která mohla využít IP sítě pro rychlejší a flexibilnější určování polohy, ale pro specifické požadavky tísňových služeb byla potřeba vyhrazená platforma.

Vytvoření E-SLP ve verzi 8 (Release 8) bylo motivováno snahou vylepšit tísňové služby integrací schopností SUPL upravených pro kritické scénáře. Řeší problémy jako zpožděné získání polohy, problémy s interoperabilitou mezi různými sítěmi a potřebu zabezpečených, standardizovaných procedur. Poskytnutím specializované platformy zajišťuje, že tísňová volání mohou těžit z pokročilých lokalizačních technologií bez zatížení obecných lokalizačních služeb. To podporuje rychlé časy odezvy, zlepšuje záchranné operace a plní zákonné povinnosti týkající se přesnosti polohy při tísňových voláních, což v konečném důsledku zachraňuje životy a posiluje infrastrukturu veřejné bezpečnosti.

## Klíčové vlastnosti

- Poskytuje lokalizační služby pro tísňová volání využívající architekturu SUPL
- Podporuje více lokalizačních technologií (např. GPS, A-GPS, OTDOA)
- Integruje se s Public Safety Answering Points (PSAP) pro dispečink
- Používá signalizaci na uživatelské rovině (user plane) pro rychlé a efektivní získání polohy
- Zahrnuje komponenty SUPL Location Center (SLC) a SUPL Positioning Center (SPC)
- Zajišťuje zabezpečený a přesný přenos polohových dat pro veřejnou bezpečnost

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.868** (Rel-9) — Study on IMS Emergency Calls

---

📖 **Anglický originál a plná specifikace:** [E-SLP na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-slp/)
