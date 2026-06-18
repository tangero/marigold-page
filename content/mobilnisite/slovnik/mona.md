---
slug: "mona"
url: "/mobilnisite/slovnik/mona/"
type: "slovnik"
title: "MONA – Media Orientation Negotiation Acceleration"
date: 2025-01-01
abbr: "MONA"
fullName: "Media Orientation Negotiation Acceleration"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mona/"
summary: "Rozšíření protokolu v rámci architektury IMS, které urychluje navazování mediálních relací, zejména u hlasových a videohovorů. Snižuje zpoždění při navazování hovoru optimalizací výměny nabídky a odpo"
---

MONA je rozšíření protokolu v IMS, které urychluje navázání hlasových a videohovorů optimalizací výměny SDP nabídky/odpovědi za účelem snížení zpoždění při vyjednávání relace.

## Popis

Media Orientation Negotiation Acceleration (MONA, urychlení vyjednávání mediální orientace) je protokolový mechanismus standardizovaný 3GPP, primárně popsaný v TS 29.163 (Interworking between the IMS and [CS](/mobilnisite/slovnik/cs/) networks) a TS 29.863 (Protocols for IMS interworking). Je navržen k optimalizaci fáze mediálního vyjednávání během navazování relace založené na IMS, jako je hovor VoLTE nebo ViLTE. Standardní navázání relace s použitím [SIP](/mobilnisite/slovnik/sip/) a protokolu pro popis relace ([SDP](/mobilnisite/slovnik/sdp/)) zahrnuje model nabídky/odpovědi, kde volající strana (UE-A) odešle SDP nabídku v SIP INVITE s výčtem podporovaných mediálních kodeků a parametrů. Volaná strana (UE-B) odpoví SDP odpovědí ve zprávě 183 Session Progress nebo 200 OK, ve které zvolí dohodnutý kodek. Tato výměna může procházet více síťovými uzly a může zahrnovat několik kol přenosu, což zavádí zpoždění. MONA funguje tak, že umožňuje síti, konkrétně zprostředkujícímu uzlu jako je Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) nebo IMS Media Gateway ([IM-MGW](/mobilnisite/slovnik/im-mgw/)) ve scénářích propojování sítí, vygenerovat a odeslat prozatímní, urychlenou SDP odpověď jménem koncové strany dříve, než je přijata konečná odpověď ze vzdáleného koncového bodu. Tato prozatímní odpověď umožňuje iniciující straně začít rezervovat prostředky a, což je klíčové, začít odesílat média (např. hlasové pakety) dříve v průběhu hovoru. Síťový uzel generující urychlenou odpověď využívá předem nakonfigurované znalosti nebo politiky o očekávaných mediálních schopnostech. Později, když dorazí skutečná SDP odpověď od koncového UE, síť vyřeší případné rozdíly a v případě potřeby může spustit aktualizaci. Tento proces významně zkracuje zpoždění po vytočení, které vnímá uživatel. Z architektonického hlediska MONA zahrnuje vylepšení logiky pro zpracování SIP/SDP v aplikačních serverech IMS, MGCF a někdy i v [P-CSCF](/mobilnisite/slovnik/p-cscf/).

## K čemu slouží

MONA byla vytvořena k řešení klíčového problému uživatelského zážitku v IP telefonii: pomalého času navazování hovoru, který je obzvláště patrný ve scénářích mezisíťových hovorů nebo hovorů mezi IMS a komutovanou sítí ([CS](/mobilnisite/slovnik/cs/)). Při tradičním navazování [SIP](/mobilnisite/slovnik/sip/) hovoru nemůže začít vytváření mediální cesty dříve, než je přijata kompletní SDP odpověď ze vzdáleného konce, což může zahrnovat několik přeskoků signalizace a zpoždění zpracování. To vede k delší době mezi stisknutím tlačítka pro volání a slyšením zpětného vyzváněcího tónu nebo hlasu volaného účastníka. MONA to řeší tím, že umožňuje zprostředkujícímu síťovému uzlu poskytnout časnou, předpokládanou SDP odpověď, což umožňuje alokovat prostředky v mediální rovině a potenciálně spustit tok médií paralelně s probíhajícím vyjednáváním signalizace. Primární motivací bylo dosáhnout toho, aby služby hlasu a videa založené na IMS (VoLTE) byly alespoň stejně rychlé, ne-li rychlejší, než tradiční hovory v komutovaných sítích. Konkrétně řeší omezení ve scénářích propojování sítí, kde jsou signalizační cesty delší, jako jsou hovory ze sítě IMS do starší sítě CS nebo mezi různými síťovými operátory IMS. Snížením zpoždění při navazování hovoru MONA zlepšuje spokojenost uživatelů a představuje klíčovou optimalizaci výkonu pro komerční úspěch služeb VoLTE a VoNR.

## Klíčové vlastnosti

- Umožňuje generování prozatímních SDP odpovědí síťovými zprostředkovateli (např. MGCF)
- Urychluje rezervaci mediálních prostředků a časné navázání toku médií
- Snižuje zpoždění po vytočení a čas do zahájení přenosu médií pro relace IMS
- Zvláště účinná pro hovory při propojování sítí IMS-to-CS
- Zachovává zpětnou kompatibilitu; konečná SDP odpověď od koncového bodu je stále zpracována
- Lze aplikovat na navazování hlasových i videoreláci

## Související pojmy

- [SDP – Service Discovery Protocol](/mobilnisite/slovnik/sdp/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.863** (Rel-8) — IMS-CS Multimedia Interworking Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [MONA na 3GPP Explorer](https://3gpp-explorer.com/glossary/mona/)
