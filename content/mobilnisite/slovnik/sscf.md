---
slug: "sscf"
url: "/mobilnisite/slovnik/sscf/"
type: "slovnik"
title: "SSCF – Service Specific Co-ordination Function"
date: 2025-01-01
abbr: "SSCF"
fullName: "Service Specific Co-ordination Function"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sscf/"
summary: "Service Specific Co-ordination Function (SSCF) je protokolová adaptační vrstva definovaná pro rozhraní Iu v UMTS a rozhraní Iur mezi RNC. Mapuje služebně specifické požadavky nadřazené vrstvy (SSCOP –"
---

SSCF je protokolová adaptační vrstva v rozhraních UMTS Iu a Iur, která mapuje služebně specifické požadavky nadřazené vrstvy SSCOP na obecné schopnosti podkladové síťové vrstvy pro spolehlivou signalizaci řídicí roviny.

## Popis

Service Specific Co-ordination Function (SSCF) je podvrstva v rámci zásobníku protokolů řídicí roviny pozemských rozhraní UMTS, především rozhraní Iu (mezi [RNC](/mobilnisite/slovnik/rnc/) a jádrem sítě) a rozhraní Iur (mezi dvěma RNC). Je definována v 3GPP specifikacích TS 25.412 (Iu), TS 25.422 (Iur) a souvisejících dokumentech. SSCF se nachází mezi nadřazeným protokolem Service Specific Connection Oriented Protocol ([SSCOP](/mobilnisite/slovnik/sscop/)) a podkladovou vrstvou síťových služeb, kterou může být Message Transfer Part level 3 Broadband ([MTP3-B](/mobilnisite/slovnik/mtp3-b/)) pro přenos založený na [ATM](/mobilnisite/slovnik/atm/) nebo Signalizační adaptační vrstva ATM ([SAAL](/mobilnisite/slovnik/saal/)). Jejím hlavním úkolem je přizpůsobit služební primitiva a požadavky protokolu SSCOP konkrétním charakteristikám a služebním primitivům poskytovaným spodní vrstvou.

Z architektonického hlediska je SSCF součástí adaptační vrstvy ATM pro signalizaci (SAAL), která je rozdělena na společnou část ([SSCS](/mobilnisite/slovnik/sscs/)) a služebně specifickou část. SSCF je právě tato služebně specifická část. Nenabízí segmentaci/skládání ani opravu chyb – tyto funkce zajišťuje SSCOP. Místo toho SSCF řeší koordinační úlohy, jako je správa lokálního stavu, řízení provozu a mapování spojově orientované, zabezpečené přenosové služby SSCOP na potenciálně odlišný servisní model MTP3-B. Například SSCOP poskytuje spolehlivý, sekvenovaný datový kanál, zatímco MTP3-B nabízí nespojovou, zprávami orientovanou službu s vlastním směrováním a správou. SSCF zprostředkovává převod mezi těmito dvěma světy a zajišťuje, že procedury SSCOP pro navázání, uvolnění a údržbu spojení jsou správně aktivovány na základě stavu signalizačního spoje MTP3-B.

Princip činnosti: SSCF přijímá služební primitiva od SSCOP (např. požadavek na navázání spojení SSCOP, požadavek na přenos dat). Následně vydá odpovídající primitiva spodní vrstvě, aby tohoto cíle dosáhla, například iniciuje zřízení signalizačního spoje MTP3-B nebo zabalí data do zpráv MTP3-B. Naopak přijímá indikace ze spodní vrstvy (např. porucha spoje, zahlcení) a převádí je na vhodné indikace pro SSCOP, které pak může podniknout nápravné akce. Tato koordinace je zásadní pro udržení integrity signalizačního spojení, zejména při výpadcích sítě nebo při zahlcení. SSCF pro rozhraní mezi sítěmi (SSCF-NNI) se používá na rozhraních Iu a Iur, zatímco odlišná verze (SSCF-UNI) je definována pro rozhraní uživatel-síť, ale v rozhraních 3GPP RAN se typicky nepoužívá.

## K čemu slouží

SSCF byla vytvořena, aby vyřešila nesoulad mezi servisními požadavky signalizačních protokolů vyšších vrstev a službami poskytovanými podkladovou transportní technologií v sítích UMTS, které zpočátku výrazně spoléhaly na [ATM](/mobilnisite/slovnik/atm/). Protokoly jako [RANAP](/mobilnisite/slovnik/ranap/) (na Iu) a RNSAP (na Iur) vyžadují pro své signalizační zprávy spolehlivou, spojově orientovanou přenosovou službu. Protokol SSCOP byl navržen tak, aby právě tuto službu přes ATM síť poskytoval. Nicméně nativní signalizační vrstva ATM (SAAL a MTP3-B) přímo nenabízela rozhraní, které by SSCOP mohl použít.

Účelem SSCF je tedy fungovat jako nezbytný spojovací člen neboli adaptační vrstva. Řeší problém vzájemné spolupráce mezi abstraktním servisním rozhraním SSCOP a konkrétními primitivy a procedurami MTP3-B v rámci SAAL. Bez SSCF by SSCOP nemohl fungovat nad signalizační sítí založenou na ATM. Toto bylo klíčové konstrukční rozhodnutí v raném UMTS (R99) s cílem využít záruky kvality služeb (QoS) a spolehlivosti ATM pro klíčovou signalizaci řídicí roviny v RAN.

Její vytvoření bylo motivováno potřebou robustní, standardizované signalizační přenosové cesty pro novou, rozdělenou architekturu RAN-CN v UMTS. Rozhraní Iu a Iur vyžadovala sofistikovanější transport než TDM-based SS7 používané v rozhraní A sítě GSM. SSCF jako součást zásobníku SAAL toto umožnila tím, že poskytla nezbytnou koordinaci pro vybudování spolehlivého signalizačního přenosového kanálu nad virtuálními spojeními ATM, a zajistila tak, že řídicí zprávy pro správu mobility, řízení hovorů a správu rádiových zdrojů byly doručeny přesně a ve správném pořadí, což je zásadní pro stabilitu a výkon sítě.

## Klíčové vlastnosti

- Adaptační vrstva mezi SSCOP a spodní síťovou vrstvou (MTP3-B/SAAL)
- Mapuje služební primitiva SSCOP na primitiva MTP3-B/SAAL a naopak
- Spravuje lokální stav a koordinuje procedury navázání a uvolnění spojení
- Zpracovává řízení provozu a indikace zahlcení mezi vrstvami
- Nezbytná pro spolehlivý signalizační transport na rozhraních Iu a Iur založených na ATM
- Definována jako součást služebně specifické adaptační vrstvy ATM (SAAL)

## Související pojmy

- [SSCOP – Service Specific Connection Oriented Protocol](/mobilnisite/slovnik/sscop/)
- [MTP3-B – Message Transfer Part level 3 (for Q.2140)](/mobilnisite/slovnik/mtp3-b/)
- [SAAL – Signalling ATM Adaptation Layer](/mobilnisite/slovnik/saal/)
- [RANAP – Radio Access Network Application Protocol](/mobilnisite/slovnik/ranap/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.412** (Rel-19) — Iu Interface Signalling Transport Specification
- **TS 25.422** (Rel-19) — Signalling Transport for Iur Interface
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.432** (Rel-19) — Iub NBAP Signalling Transport Specification
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TS 29.202** (Rel-19) — SS7 Signalling Transport Protocol Architectures

---

📖 **Anglický originál a plná specifikace:** [SSCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/sscf/)
