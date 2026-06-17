---
slug: "anbr"
url: "/mobilnisite/slovnik/anbr/"
type: "slovnik"
title: "ANBR – Access Network Bit rate Recommendation"
date: 2025-01-01
abbr: "ANBR"
fullName: "Access Network Bit rate Recommendation"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/anbr/"
summary: "ANBR je mechanismus QoS v sítích 3GPP, který poskytuje aplikační vrstvě doporučenou maximální přenosovou rychlost pro mediální toky v přístupové síti. Umožňuje dynamickou adaptaci mediálního kódování"
---

ANBR je mechanismus QoS, který aplikační vrstvě poskytuje doporučenou maximální přenosovou rychlost pro mediální toky v přístupové síti, aby umožnil dynamickou adaptaci a zabránil zahlcení.

## Popis

Access Network Bit rate Recommendation (ANBR, doporučení přenosové rychlosti přístupové sítě) je signalizační mechanismus kvality služeb (QoS) definovaný v rámci standardů 3GPP, konkrétně pro služby IP Multimedia Subsystem (IMS) a Packet Switched Streaming (PSS). Funguje tak, že umožňuje jádru sítě, konkrétně funkci Policy and Charging Rules Function (PCRF) nebo funkci Access Network Discovery and Selection Function ([ANDSF](/mobilnisite/slovnik/andsf/)) v určitých architekturách, komunikovat doporučenou maximální přenosovou rychlost k aplikační funkci ([AF](/mobilnisite/slovnik/af/)) nebo přímo k uživatelskému zařízení (UE). Toto doporučení se týká přenosové rychlosti pro mediální toky (např. hlas, video) při jejich průchodu rádiovou přístupovou sítí (RAN). Hodnota ANBR není zaručená ani vynucená přenosová rychlost, ale pouze doporučení, které je typicky odvozeno od síťových politik, profilů předplatného a aktuálních nebo předpokládaných rádiových podmínek. Hlavní architektonická interakce zahrnuje rozhraní Rx mezi AF (např. [P-CSCF](/mobilnisite/slovnik/p-cscf/) v IMS) a PCRF, kde je ANBR přenášeno v rámci Diameter zpráv Authentication and Authorization Request (AAR) a Answer ([AAA](/mobilnisite/slovnik/aaa/)). Pro scénáře s asistencí UE lze informaci předat prostřednictvím signalizace SIP nebo v rámci popisů médií.

Po přijetí ANBR jej aplikační vrstva – například mediální kodér v UE nebo funkce mediálních zdrojů v síti – použije k úpravě charakteristik přenosu média. Například klient pro streamování videa může vybrat profil videokodeku s nižší přenosovou rychlostí nebo upravit své kódovací parametry, aby zajistil, že generovaný mediální proud nepřekročí doporučenou rychlost. Tato adaptace je dynamická; ANBR může být aktualizováno během probíhající relace v reakci na změny síťových podmínek, jako jsou změny vytížení buňky nebo události mobility uživatele vedoucí k předání spojení do buňky s odlišnou kapacitou. Mechanismus je nedílnou součástí architektury QoS pro Evolved Packet System (EPS) a 5G System (5GS) a spolupracuje s dalšími parametry QoS, jako je Guaranteed Bit Rate ([GBR](/mobilnisite/slovnik/gbr/)) a Maximum Bit Rate ([MBR](/mobilnisite/slovnik/mbr/)), k efektivní správě rádiových a přenosových prostředků.

Role ANBR je klíčová pro optimalizaci využití často omezeného rádiového rozhraní při zachování uspokojivého uživatelského komfortu (QoE). Tím, že zabraňuje aplikaci v odesílání média rychlostí vyšší, než jakou může přístupová síť udržitelně podporovat, pomáhá ANBR předcházet ztrátám paketů, chvění (jitteru) a nadměrným zpožděním, která zhoršují komunikaci v reálném čase. Umožňuje inteligentnější, síťově asistovanou adaptaci ve srovnání s čistě koncově-koncovými aplikačními adaptačními protokoly, jako jsou [DASH](/mobilnisite/slovnik/dash/) nebo WebRTC, protože zahrnuje síťové politiky a informace z rádiové vrstvy. Mechanismus podporuje oba směry, uplink i downlink, a umožňuje nezávislé hodnoty ANBR pro každý z nich, což pokrývá asymetrické síťové podmínky. Jeho implementace je specifikována v řadě technických specifikací 3GPP pokrývajících IMS, multimediální telefonii a streamovací služby, což zajišťuje interoperabilitu mezi síťovými prvky a klientskými zařízeními.

## K čemu slouží

ANBR bylo zavedeno jako odpověď na výzvu efektivního poskytování kvalitních multimediálních služeb přes buněčné sítě s proměnlivými a někdy omezenými rádiovými prostředky. Před jeho standardizací byla adaptace média primárně řešena koncově-koncovými protokoly nebo na základě pasivního pozorování ztráty paketů a zpoždění, což mohlo být reaktivní a neefektivní. To často vedlo k neoptimálnímu uživatelskému zážitku, jako je zamrznutí videa nebo výpadky hovorů při síťovém zahlcení, protože aplikace si nebyla vědoma konkrétních kapacitních omezení rádiového přístupového spoje. Motivací pro ANBR byla potřeba síťově asistovaného mechanismu, který by mohl proaktivně usměrňovat chování aplikace a sladit přenosové rychlosti médií s dostupnou šířkou pásma přístupové sítě podle síťových politik a podmínek.

Vytvoření ANBR bylo hnáno vývojem směrem k plně IP sítím a rozšířením služeb založených na IMS, jako je Voice over LTE (VoLTE) a Video over LTE (ViLTE). Tyto služby v reálném čase mají striktní požadavky na latenci a chvění, což činí efektivní správu rádiových prostředků kritickou. Tradiční mechanismy QoS v 3GPP, jako jsou vyhrazené přenosy s [GBR](/mobilnisite/slovnik/gbr/), poskytují rezervaci prostředků, ale jsou poměrně statické a náročné na prostředky. ANBR je doplňuje tím, že nabízí flexibilnější, politikou řízené doporučení, které nevyžaduje zřízení vyhrazeného přenosu, snižuje signalizační režii a umožňuje dynamickou adaptaci pro velký počet souběžných relací. Řeší problém síťového zahlcení způsobeného nekoordinovanými mediálními toky s vysokou přenosovou rychlostí, čímž zlepšuje celkovou kapacitu a stabilitu sítě.

ANBR dále umožňuje diferenciaci služeb a personalizovanou QoS. Operátoři jej mohou použít k prosazování politik založených na předplatném a doporučovat různé přenosové rychlosti prémiovým a standardním uživatelům i za stejných rádiových podmínek. Usnadňuje také plynulou mobilitu; když se uživatel pohybuje, síť může aktualizovat ANBR tak, aby odráželo možnosti nové obsluhující buňky, což umožní mediální relaci se plynule přizpůsobit bez přerušení služby. Tím řeší omezení předchozích přístupů, kterým chyběla přímá vstupní informace ze sítě, a poskytuje standardizované rozhraní pro optimalizaci mezi vrstvami (cross-layer) mezi aplikací a rádiovou přístupovou sítí.

## Klíčové vlastnosti

- Poskytuje síťově generovaná doporučení přenosové rychlosti pro mediální toky
- Umožňuje dynamickou adaptaci přenosových rychlostí mediálního kódování během relace
- Funguje nezávisle pro směry uplink i downlink
- Operuje přes standardizovaná rozhraní, jako je Rx mezi AF a PCRF
- Doplňuje stávající mechanismy QoS (GBR, MBR) bez nutnosti zřízení vyhrazeného přenosu
- Podporuje politikou řízenou diferenciaci služeb na základě předplatného a síťových podmínek

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.910** (Rel-19) — MTSI enhancements for RAN delay budget reporting
- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation

---

📖 **Anglický originál a plná specifikace:** [ANBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/anbr/)
