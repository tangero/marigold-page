---
slug: "d-gps"
url: "/mobilnisite/slovnik/d-gps/"
type: "slovnik"
title: "D-GPS – Differential Global Positioning System"
date: 2025-01-01
abbr: "D-GPS"
fullName: "Differential Global Positioning System"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/d-gps/"
summary: "D-GPS je technika vylepšení polohového určení, která zvyšuje přesnost GPS využitím referenčních stanic k výpočtu a vysílání korekčních dat. Snižuje chyby způsobené atmosférickými zpožděními, nepřesnos"
---

D-GPS je technika vylepšení polohového určení, která zvyšuje přesnost GPS využitím referenčních stanic k vysílání korekčních dat, čímž snižuje chyby a poskytuje přesné polohové služby v sítích 3GPP.

## Popis

Diferencovaný [GPS](/mobilnisite/slovnik/gps/) (D-GPS) funguje jako korekční systém, který zvyšuje přesnost standardního polohování GPS v sítích 3GPP. Architektura se skládá ze dvou hlavních komponent: referenčních stanic s přesně známou polohou a mobilních přijímačů v uživatelském zařízení (UE). Referenční stanice nepřetržitě přijímají GPS signály, vypočítávají rozdíl mezi svou známou polohou a polohou získanou z GPS a generují korekční data pro různé zdroje chyb, včetně ionosférického a troposférického zpoždění, chyb satelitních hodin a nepřesností orbitálních efemerid. Tyto korekce jsou formátovány do standardizovaných zpráv a vysílány do mobilních zařízení prostřednictvím mobilních sítí pomocí polohových protokolů řídicí nebo uživatelské roviny.

V mobilním přijímači zpracování D-GPS zahrnuje přijímání jak nezpracovaných GPS měření (pseudovzdálenosti, fáze nosné vlny), tak proudu korekčních dat ze sítě. UE tyto korekce v reálném čase aplikuje na vlastní GPS měření, čímž efektivně potlačí chyby společného režimu, které ovlivňují jak referenční stanici, tak mobilní přijímač v určité geografické oblasti. Korekční data lze použít různými metodami, včetně korekcí v polohové doméně (kde referenční stanice počítá opravené polohy) nebo korekcí v měřicí doméně (kde se přenášejí korekce nezpracovaných pseudovzdáleností). Specifikace 3GPP definují, jak jsou tyto korekce doručovány prostřednictvím polohových protokolů, jako jsou RRLP (Radio Resource Location Protocol), [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control) nebo [LPP](/mobilnisite/slovnik/lpp/) (LTE Positioning Protocol).

D-GPS dosahuje výrazného zlepšení přesnosti tím, že řeší prostorovou a časovou korelaci GPS chyb. Atmosférická zpoždění (ionosférická a troposférická) se v čase a prostoru mění pomalu, což je činí vysoce korelovanými mezi blízkými přijímači. Chyby satelitních hodin a nepřesnosti efemerid jsou společné pro všechny přijímače na celém světě. Díky vysílání korekcí vypočtených na referenčních stanicích mohou mobilní přijímače dosáhnout přesnosti polohování 1–5 metrů v reálném čase ve srovnání s 10–15 metry pro samostatný GPS. Účinnost systému závisí na vzdálenosti mezi mobilním přijímačem a referenční stanicí (s degradací se zvětšující se vzdáleností), stáří korekcí (latence) a integritě přenosu korekčních dat.

V sítích 3GPP se D-GPS integruje do celkové polohové architektury definované v TS 43.059 a následných specifikacích. Serving Mobile Location Center (SMLC) nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) mohou spravovat sítě referenčních stanic, agregovat korekční data a distribuovat je do UE prostřednictvím mobilní infrastruktury. D-GPS může pracovat v různých režimech, včetně síťově asistovaného (kde síť poskytuje korekce) a síťově založeného (kde síť zpracovává polohování s využitím korekcí). Tato technologie umožňuje přesné polohové služby pro tísňová volání (E911/E112), navigační aplikace, sledování majetku a polohové služby, které vyžadují vyšší přesnost, než může poskytnout samostatný GPS.

## K čemu slouží

D-GPS byl vyvinut za účelem řešení základních omezení přesnosti samostatného polohování [GPS](/mobilnisite/slovnik/gps/), které trpí různými zdroji chyb snižujícími přesnost polohy na 10–15 metrů za normálních podmínek. Mezi tyto chyby patří ionosférická a troposférická zpoždění signálu (která zpomalují GPS signály při průchodu atmosférou), nepřesnosti satelitních hodin (i přes atomové hodiny dochází k časovým chybám), chyby efemerid (nepřesnosti v datech o orbitální poloze satelitů) a selektivní dostupnost (pokud aktivní, záměrně degradované civilní GPS signály). Pro mnohé polohové služby v mobilních sítích – zejména pro tísňové služby, navigaci a komerční aplikace – byla tato úroveň přesnosti nedostatečná, což vedlo k potřebě technik vylepšení.

Integrace D-GPS do norem 3GPP počínaje Release 8 byla motivována regulatorními požadavky na rozšířené tísňové služby (E911 v USA, E112 v Evropě), které stanovovaly konkrétní prahové hodnoty přesnosti pro mobilní polohování. Samostatný GPS nemohl tyto požadavky spolehlivě splnit, zejména v městském prostředí s vícecestným šířením a omezenou viditelností satelitů. D-GPS poskytl nákladově efektivní vylepšení, které využívalo stávající hardwarové vybavení GPS přijímačů v mobilních zařízeních a přidávalo pouze přenos korekčních dat prostřednictvím mobilních sítí. Tento přístup se vyhnul potřebě zcela nového polohovacího hardwaru v koncových zařízeních a zároveň významně zlepšil přesnost.

Mezi předchozí přístupy ke zlepšení přesnosti GPS patřily WAAS (Wide Area Augmentation System) a další satelitní augmentační systémy, ale ty vyžadovaly specializované přijímače a nebyly všeobecně dostupné. D-GPS nabídl pozemní korekční systém, který mohl být nasazen regionálně nebo národně pomocí mobilní infrastruktury. Tato technologie řešila problém poskytování přesnosti na úrovni metrů bez nutnosti dvoufrekvenčních GPS přijímačů (což by zvýšilo cenu a složitost koncového zařízení) nebo rozsáhlé pozemní infrastruktury nad rámec referenčních stanic. Korekcí chyb společného režimu ovlivňujících všechny GPS přijímače v regionu umožnil D-GPS přesné polohování pro širokou škálu aplikací od navigace po jednotlivých krocích až po polohovou reklamu a správu vozových parků.

## Klíčové vlastnosti

- Síť referenčních stanic s přesně zaměřenými polohami
- Generování korekčních dat pro GPS chyby v reálném čase
- Doručování korekcí přes mobilní síť pomocí polohových protokolů
- Metody korekcí v měřicí a polohové doméně
- Integrace s polohováním v řídicí a uživatelské rovině 3GPP
- Zlepšení přesnosti z rozsahu 10–15 m na rozsah 1–5 m

## Definující specifikace

- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [D-GPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/d-gps/)
