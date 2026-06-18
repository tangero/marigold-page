---
slug: "rfsp"
url: "/mobilnisite/slovnik/rfsp/"
type: "slovnik"
title: "RFSP – RAT/Frequency Selection Priority"
date: 2026-01-01
abbr: "RFSP"
fullName: "RAT/Frequency Selection Priority"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rfsp/"
summary: "RAT/Frequency Selection Priority (RFSP) je index řízený sítí, který ovlivňuje chování UE při výběru a převýběru buňky. Umožňuje síti nasměrovat UE na preferované rádiové přístupové technologie (RAT) a"
---

RFSP je index řízený sítí, který slouží k nasměrování uživatelského zařízení na preferované rádiové přístupové technologie a frekvenční vrstvy za účelem správy provozu, vyvážení zátěže a mobility zohledňující službu.

## Popis

[RAT](/mobilnisite/slovnik/rat/)/Frequency Selection Priority (RFSP) je parametr jádra sítě, definovaný jako index (RFSP Index), který je namapován na specifické chování UE pro mobilitu v režimu volnoběhu a připojení. Jádro sítě, konkrétně Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v EPS nebo funkce Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5GC, přiřadí UE RFSP Index na základě jejího profilu předplatného (z Unified Data Management, [UDM](/mobilnisite/slovnik/udm/)), požadovaného síťového řezu nebo lokálních provozovatelských politik. Tento index je následně poskytnut rádiové přístupové síti ([E-UTRAN](/mobilnisite/slovnik/e-utran/) nebo NG-RAN) přes rozhraní S1 nebo [N2](/mobilnisite/slovnik/n2/). RAN použije RFSP Index k výběru a aplikaci konkrétní sady mobilních politik, známých jako RFSP in Mobility Control (RFSP-in-MC), které jsou předem nakonfigurovány v uzlech RAN (např. [eNB](/mobilnisite/slovnik/enb/), gNB).

Tyto politiky RFSP-in-MC určují, jak má RAN zacházet s UE z hlediska priorit převýběru buňky (pro UE v režimu volnoběhu/nečinnosti) a parametrů předávání spojení (pro připojené UE). Pro režim volnoběhu RFSP Index ovlivňuje absolutní priority vysílané v blocích systémových informací ([SIB](/mobilnisite/slovnik/sib/)) pro různé frekvenční vrstvy a RAT (např. přiřazení vyšší priority NR než LTE pro prémiového účastníka). Pro režim připojení může ovlivnit prahové hodnoty a hysterezi používané při měření a rozhodování o předání spojení, čímž efektivně směruje UE k určitým buňkám nebo od nich. RAN převádí abstraktní RFSP Index na konkrétní parametry řízení rádiových prostředků (RRC) zaslané UE.

Architektura zahrnuje úzkou interakci mezi databází účastníků jádra sítě, síťovými funkcemi řídicí roviny (MME/AMF) a RAN. UDM/HSS ukládá Subscribed RFSP Index jako součást uživatelských dat předplatného. Během připojování nebo vytváření relace může MME/AMF odvodit nový RFSP Index na základě indexu z předplatného, výběru síťového řezu a lokální politiky. Toto dynamické odvozování umožňuje řízení provozu v reálném čase. Samotný index je celé číslo (obvykle v rozsahu např. 1–256), kde každá hodnota odpovídá konkrétní sadě politik nakonfigurovaných operátorem jak v jádře, tak v RAN.

Jak to funguje v praxi, zahrnuje několik kroků. Nejprve při připojení UE AMF/MME určí RFSP Index. Poté tento index zahrne do kontextu UE vytvořeného s gNB/eNB. gNB/eNB, který má lokálně nakonfigurovanou tabulku mapující hodnoty RFSP Indexu na konkrétní parametry řízení mobility, aplikuje odpovídající politiku. Například RFSP Index 5 může být namapován na politiku, která nastaví prioritu pásma 5G NR n78 na '7' (vysoká) a pásma LTE 3 na '3' (nízká) pro převýběr v režimu volnoběhu. To směruje UE s tímto indexem k preferenci 5G. Síť může také aktualizovat RFSP Index pro připojené UE pomocí procedury Úprava kontextu UE, což umožňuje dynamické změny politik na základě měnících se podmínek sítě nebo požadavků služby.

## K čemu slouží

RFSP bylo vytvořeno, aby poskytlo síti výkonný a standardizovaný nástroj pro inteligentní řízení provozu a správu mobility. Před mechanismy jako RFSP bylo síťové řízení výběru buňky UE z velké části omezeno na vysílání statických priorit v SIB, které platily jednotně pro všechna UE v buňce. To bylo nedostatečné pro implementaci služeb rozlišujících účastníky, efektivní vyvážení zátěže nebo síťové řezy zohledňující službu. RFSP to řeší zavedením specifického indexu politiky přiřazeného síti pro každé UE, který může být přizpůsoben jednotlivým účastníkům nebo tokům služeb.

Primární problémy, které RFSP řeší, jsou neefektivní využití prostředků a neschopnost sladit mobilitu s obchodní nebo služební logikou. Například operátor může chtít nasměrovat zařízení pro komunikaci typu stroj-stroj (MTC) na robustní, ale nízkokapacitní vrstvy 2G/3G, zatímco prémiové uživatele smartphonů nasměruje na vysokokapacitní vrstvy 4G/5G. Bez RFSP by to vyžadovalo složité a nestandardní řešení. RFSP poskytuje čisté, standardizované rozhraní mezi povědomím jádra sítě o účastníkovi/službě a řízením rádiových prostředků v RAN.

Historicky zavedeno ve 3GPP Release 9 pro LTE/EPS, význam RFSP vzrostl s příchodem síťových řezů a služební architektury 5G. Umožňuje jádru sítě komunikovat „kontext“ UE (např. že je součástí řezu pro hromadný IoT nebo řezu pro rozšířené mobilní širokopásmové připojení) do RAN, aby RAN mohl aplikovat odpovídající chování mobility. To umožňuje síti optimalizovat současně pro různé, často protichůdné cíle – jako je maximalizace propustnosti pro některé uživatele při maximalizaci výdrže baterie nebo pokrytí pro jiné – vše v rámci jedné sdílené infrastruktury RAN.

## Klíčové vlastnosti

- Index přiřazený sítí (RFSP Index) odvozený z předplatného, řezu a politiky
- Umožňuje specifické řízení parametrů převýběru buňky a předání spojení pro každé UE
- Rozhraní mezi politikou jádra sítě (MME/AMF) a prováděním mobility v RAN
- Podporuje dynamické aktualizace během připojení UE
- Základní pro realizaci mobility zohledňující službu a síťových řezů
- Používá předem nakonfigurované mapování (RFSP-in-MC) v uzlech RAN k převodu indexu na parametry RRC

## Související pojmy

- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.523** (Rel-19) — 5G Policy Control Event Exposure Service
- **TS 29.534** (Rel-19) — 5G Access & Mobility Policy Authorization Service
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report

---

📖 **Anglický originál a plná specifikace:** [RFSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/rfsp/)
