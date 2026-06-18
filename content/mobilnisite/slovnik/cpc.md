---
slug: "cpc"
url: "/mobilnisite/slovnik/cpc/"
type: "slovnik"
title: "CPC – Continuous Packet Connectivity"
date: 2026-01-01
abbr: "CPC"
fullName: "Continuous Packet Connectivity"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cpc/"
summary: "Continuous Packet Connectivity (CPC) je soubor technik správy rádiových prostředků pro UMTS/HSPA, navržený k výraznému zvýšení počtu současných uživatelů paketových dat, které buňka dokáže obsloužit."
---

CPC je soubor technik správy rádiových prostředků pro UMTS/HSPA, navržený k výraznému zvýšení počtu současných uživatelů paketových dat, které buňka dokáže obsloužit, prostřednictvím zvýšení efektivity uplinku, snížení interference a minimalizace spotřeby baterie.

## Popis

Continuous Packet Connectivity (CPC) je komplexní soubor funkcí pro sítě UMTS/[HSPA](/mobilnisite/slovnik/hspa/), primárně definovaný ve 3GPP Release 7, který optimalizuje rádiové rozhraní pro velký počet trvale připojených („always-on“) uživatelů paketových služeb. Jeho hlavním cílem je maximalizovat počet uživatelů, kteří mohou být udržováni v připojeném stavu – konkrétně ve stavu CELL_[DCH](/mobilnisite/slovnik/dch/) – bez způsobení nadměrné interference v uplinku nebo vyčerpání baterie zařízení. Před zavedením CPC vyžadovalo udržení uživatele ve stavu CELL_DCH nepřetržitý přenos pilotních a řídicích signálů, což spotřebovávalo značnou část kapacity uplinku a výkonu. CPC zavádí mechanismy, které umožňují síti udržet uživatele v tomto vysoce výkonném stavu, zatímco drasticky snižují režii, když uživatel aktivně nepřenáší data.

Z architektonického hlediska CPC funguje v rámci Node B (základnové stanice) a uživatelského zařízení (UE), řízeno [RNC](/mobilnisite/slovnik/rnc/) (Radio Network Controller) prostřednictvím specifických konfigurací [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control). Nejde o jeden protokol, ale o soubor doplňujících se technik. Klíčovou součástí je nespojitý přenos ([DTX](/mobilnisite/slovnik/dtx/)) v uplinku, který umožňuje UE zastavit přenos na vyhrazeném fyzickém řídicím kanálu ([DPCCH](/mobilnisite/slovnik/dpcch/)) během období nečinnosti. DPCCH přenáší zásadní pilotní bity a bity pro řízení výkonu. Jeho přenosem pouze v předdefinovaných krátkých dávkách se snižuje interference v uplinku a prodlužuje se výdrž baterie UE. Podobně nespojitý příjem ([DRX](/mobilnisite/slovnik/drx/)) v downlinku umožňuje UE podle plánovaného vzoru vypínat přijímací obvody, čímž dále šetří energii.

Dalším základním mechanismem je vylepšený vyhrazený kanál ([E-DCH](/mobilnisite/slovnik/e-dch/)) v uplinku, který je součástí HSPA. CPC optimalizuje jeho provoz. Řídicí kanál pro vysokorychlostní přenos (HS-DPCCH), který přenáší zpětnou vazbu o kvalitě kanálu (CQI) a potvrzení HARQ, lze také nakonfigurovat se sníženou aktivitou. Dále CPC zavádí koncept „CPC aktivního souboru“ pro scénáře měkčího předávání spojení (softer handover), což optimalizuje způsob, jakým více Node B spravuje spojení jednoho UE. RNC konfiguruje všechny tyto parametry – délky cyklů DTX/DRX, prahové hodnoty aktivace a konfigurace kanálů – na základě služebního profilu uživatele a zatížení sítě. To umožňuje síti vyvážit mírně zvýšené zpoždění při sestavování paketového hovoru s výrazně lepší kapacitou a výdrží baterie, což je ideální pro trhané, interaktivní aplikace jako prohlížení webu a instant messaging.

## K čemu slouží

CPC bylo vyvinuto k řešení kritických omezení kapacity a výdrže baterie v raných sítích UMTS/HSPA, když začala prudce narůstat spotřeba mobilních dat. Tradiční přístup udržování datového uživatele ve stavu CELL_DCH zajišťoval nízkou latenci, ale byl velmi neefektivní. UE nepřetržitě vysílalo pilotní signál DPCCH, což vytvářelo stálou interferenci v uplinku a omezovalo počet současných uživatelů, které buňka mohla podporovat. Toto „vždy zapnuté“ signalizační zatížení také rychle vyčerpávalo baterie zařízení, což činilo trvale připojené služby pro uživatele nepraktické. Operátoři sítí čelili dilematu: buď udržovat uživatele v nižších stavech (jako CELL_FACH nebo CELL_PCH) s vyšší latencí a horším uživatelským zážitkem, nebo přijmout výrazně omezenou kapacitu sítě.

Motivací pro CPC bylo toto kompromisní řešení překonat. Bylo to hnací silou potřeby podpořit masivní nárůst trvale připojených aplikací a služeb pro chytré telefony, které se očekávaly na konci první dekády tohoto století. Minimalizací režie řídicích kanálů během období nečinnosti v rámci aktivní relace CPC přímo řeší hlavní příčinu interference v uplinku. To umožňuje síti udržovat mnohem více uživatelů ve vysoce výkonném stavu CELL_DCH, připravených přenášet data s minimálním zpožděním, aniž by došlo ke kolapsu systémové kapacity. Z pohledu uživatele umožňuje zážitek „vždy připojeného“ internetu – kde zůstávají připojeny e-mailové a messagingové aplikace – bez katastrofického dopadu na výdrž baterie. CPC tak představovalo zásadní evoluční krok pro HSPA, který zvýšil jeho konkurenceschopnost jako mobilní širokopásmové technologie před rozšířeným nasazením LTE.

## Klíčové vlastnosti

- Nespojitý přenos (DTX) v uplinku pro kanál DPCCH
- Nespojitý příjem (DRX) v downlinku pro úsporu výkonu UE
- Optimalizovaná konfigurace pro provoz E-DCH (uplink HSPA)
- Snížená aktivita zpětnovazebního kanálu HS-DPCCH
- Specifická správa aktivního souboru pro CPC pro měkčí předání spojení
- Konfigurace časovačů nečinnosti a délek cyklů řízená protokolem RRC

## Související pojmy

- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)

## Definující specifikace

- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 25.824** (Rel-8) — HSPA Evolution for 1.28Mcps TDD Study
- **TR 25.903** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 32.280** (Rel-19) — Advice of Charge (AoC) Framework
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 37.483** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [CPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpc/)
