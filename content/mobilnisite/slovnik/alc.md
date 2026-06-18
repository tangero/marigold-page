---
slug: "alc"
url: "/mobilnisite/slovnik/alc/"
type: "slovnik"
title: "ALC – Asynchronous Layered Coding"
date: 2025-01-01
abbr: "ALC"
fullName: "Asynchronous Layered Coding"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/alc/"
summary: "Asynchronous Layered Coding je spolehlivý multicastový transportní protokol pro multimediální vysílací/multicastové služby (MBMS). Umožňuje efektivní doručování obsahu více uživatelům současně pomocí"
---

ALC je spolehlivý multicastový transportní protokol pro multimediální vysílací služby, který využívá vrstvové kódování a asynchronní přenos k efektivnímu doručování obsahu více uživatelům současně.

## Popis

Asynchronous Layered Coding je protokol navržený v rámci architektury 3GPP Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) pro zajištění spolehlivého multicastového transportu pro služby doručování souborů a streamování. Funguje jako aplikační protokol nad vrstvou [UDP](/mobilnisite/slovnik/udp/)/IP a pod vrstvou MBMS uživatelských služeb, konkrétně navržený k překonání omezení tradičního IP multicastu v bezdrátových prostředích. ALC využívá kombinaci vrstvového kódování, řízení zahlcení a asynchronního přenosu k umožnění efektivního, škálovatelného šíření obsahu potenciálně milionům mobilních zařízení současně.

Architektura protokolu se skládá z několika klíčových komponent: samotného protokolu ALC, který definuje formáty paketů a popis relace; stavebního bloku Layered Coding Transport ([LCT](/mobilnisite/slovnik/lct/)), který poskytuje správu relací a řízení zahlcení; a stavebních bloků Forward Error Correction ([FEC](/mobilnisite/slovnik/fec/)), které umožňují spolehlivé doručení bez nutnosti zpětné vazby od přijímačů. Relace ALC jsou identifikovány kombinací zdrojové IP adresy, cílového portu a Transport Session Identifier ([TSI](/mobilnisite/slovnik/tsi/)). Protokol využívá více vrstev neboli kanálů, k nimž se mohou přijímače nezávisle přihlásit, což umožňuje adaptaci šířky pásma a diferenciaci služeb.

ALC funguje tak, že rozděluje obsah na objekty, které jsou vysílány pomocí více vrstev. Každá vrstva nese kódovaná data pomocí technik FEC, typicky kódů Raptor nebo RaptorQ specifikovaných v 3GPP. Přijímače se mohou přihlásit k různým kombinacím vrstev na základě svých možností, stavu sítě nebo úrovně předplatného. Asynchronní povaha znamená, že přijímače se mohou k relacím připojit kdykoli a stále přijmout kompletní obsah, protože přenos využívá opakování založené na karuselu, kde se obsahové objekty opakovaně vysílají. Tím odpadá potřeba synchronizace mezi vysílačem a přijímači.

V architektuře MBMS ALC funguje v rámci [BM-SC](/mobilnisite/slovnik/bm-sc/) (Broadcast Multicast Service Center) pro doručování obsahu a v UE pro příjem. BM-SC používá ALC k zabalení obsahu do paketů ALC, které jsou pak předávány přes přenosovou síť MBMS. Protokol zahrnuje vestavěné mechanismy řízení zahlcení, které přizpůsobují přenosovou rychlost na základě stavu sítě, čímž zajišťují efektivní využití rádiových prostředků. ALC také podporuje procedury opravy souborů prostřednictvím dodatečných opravných symbolů vysílaných v samostatných vrstvách, což umožňuje spolehlivé doručení i v náročných rádiových podmínkách.

Návrh protokolu specificky řeší výzvy bezdrátového multicastu: proměnlivé podmínky kanálu mezi různými přijímači, omezené možnosti zpětné vazby (aby se zabránilo zhroucení zpětné vazby) a efektivní využití vysílacích rádiových prostředků. Kombinací vrstvového kódování s FEC umožňuje ALC přijímačům v oblastech se špatným pokrytím přijmout obsah díky delší době příjmu, zatímco přijímače v dobrém pokrytí získají obsah rychle. Tato vlastnost pozvolné degradace činí ALC zvláště vhodným pro mobilní vysílací služby, kde uživatelská zařízení zažívají značně rozdílné podmínky signálu.

## K čemu slouží

ALC byl vytvořen k řešení základních výzev spolehlivého multicastového doručování obsahu v mobilních sítích, zejména pro služby [MBMS](/mobilnisite/slovnik/mbms/). Tradiční protokoly IP multicastu byly navrženy pro drátové sítě a nezohledňovaly specifické charakteristiky bezdrátových prostředí: vysokou míru ztráty paketů, různé podmínky kanálu mezi přijímači, omezenou kapacitu uplinku pro zpětnou vazbu a potřebu efektivního využití rádiových prostředků. Před ALC pokusy o doručení vysílacího obsahu do mobilních zařízení využívaly buď unicastové přístupy (které se neškálují), nebo jednoduché vysílání bez záruk spolehlivosti.

Primární motivací pro vývoj ALC bylo umožnit komerční vysílací služby, jako je mobilní [TV](/mobilnisite/slovnik/tv/), kde poskytovatelé služeb potřebují garantovat doručení obsahu platícím předplatitelům. Předchozí přístupy vyžadovaly buď nadměrné rádiové prostředky (prostřednictvím opakování), nebo nemohly garantovat doručení v podmínkách na okraji buňky. ALC tyto problémy řeší prostřednictvím kombinace vrstvového kódování a FEC, což umožňuje přijímačům akumulovat data v čase a obnovit je ze ztrát bez nutnosti retransmise od zdroje.

Dalším klíčovým problémem, který ALC řeší, je problém 'zhroucení zpětné vazby' u tradičních spolehlivých multicastových protokolů. V mobilních sítích s potenciálně miliony přijímačů by vysílání potvrzení nebo negativních potvrzení od každého zařízení zahltilo síť. Návrh ALC eliminuje potřebu zpětné vazby od přijímačů díky využití proaktivního FEC a přenosu založeného na karuselu. To činí protokol škálovatelným pro velmi velké populace přijímačů při zachování záruk spolehlivosti. Protokol také umožňuje diferenciaci služeb prostřednictvím svého vrstvového přístupu, což umožňuje prémiovým uživatelům přijímat obsah vyšší kvality nebo rychlejší doručení přihlášením k dalším vrstvám.

## Klíčové vlastnosti

- Vrstvové kódování umožňující adaptaci šířky pásma a diferenciaci služeb
- Asynchronní provoz umožňující přijímačům připojit se k relacím kdykoli
- Vestavěné Forward Error Correction využívající kódy Raptor/RaptorQ
- Opakování obsahu založené na karuselu pro spolehlivé doručení
- Mechanismy řízení zahlcení pro efektivní využití sítě
- Škálovatelný návrh podporující miliony současných přijímačů bez zhroucení zpětné vazby

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)

## Definující specifikace

- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TR 26.947** (Rel-19) — FEC Evaluation for MBMS Enhancement
- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols

---

📖 **Anglický originál a plná specifikace:** [ALC na 3GPP Explorer](https://3gpp-explorer.com/glossary/alc/)
