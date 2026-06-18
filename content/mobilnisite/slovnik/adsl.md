---
slug: "adsl"
url: "/mobilnisite/slovnik/adsl/"
type: "slovnik"
title: "ADSL – Asymmetric Digital Subscriber Line"
date: 2025-01-01
abbr: "ADSL"
fullName: "Asymmetric Digital Subscriber Line"
category: "Other"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/adsl/"
summary: "ADSL je širokopásmová přístupová technologie, která poskytuje vysokorychlostní internet přes stávající měděné telefonní linky. Nabízí asymetrickou šířku pásma s vyšší rychlostí stahování než odesílání"
---

ADSL je širokopásmová přístupová technologie, která poskytuje vysokorychlostní internet přes stávající měděné telefonní linky s vyšší rychlostí stahování než odesílání. V 3GPP je referencována v kontextu konvergence pevných a mobilních sítí.

## Popis

Asymmetric Digital Subscriber Line (ADSL) je technologie digitální účastnické linky ([DSL](/mobilnisite/slovnik/dsl/)), která umožňuje vysokorychlostní přenos dat přes konvenční měděné telefonní linky. Technologie funguje tak, že rozděluje frekvenční spektrum měděné linky na samostatné kanály: jeden pro hlas (Plain Old Telephone Service nebo [POTS](/mobilnisite/slovnik/pots/)) a několik pro přenos dat. Toto frekvenční dělení umožňuje současné poskytování hlasových a datových služeb bez vzájemného rušení, přičemž pro přenos dat využívá frekvence nad hlasovým pásmem (typicky od 25 kHz do 1,1 MHz), zatímco pásmo 0–4 kHz je zachováno pro tradiční telefonní službu.

ADSL využívá modulaci diskrétním multitonem (DMT), která rozděluje dostupnou šířku pásma na 256 samostatných podnosných neboli tónů, každý široký 4,3125 kHz. Každý tón může nezávisle přenášet data a modulační schéma (počet bitů na tón) se dynamicky přizpůsobuje na základě stavu linky a poměru signálu k šumu. Tato adaptivní schopnost umožňuje ADSL optimalizovat výkon pro různé délky linek a kvalitativní podmínky. Asymetrie v přidělování šířky pásma vychází z typických vzorců využití internetu, kde provoz ve směru dolů (od sítě k uživateli) výrazně převyšuje provoz ve směru nahoru (od uživatele k síti).

Klíčové komponenty systému ADSL zahrnují ADSL transceiverovou jednotku na straně zákazníka (ATU-R), ADSL transceiverovou jednotku na centrále (ATU-C), rozdělovače (splitters) pro oddělení hlasových a datových signálů a DSL přístupový multiplexor (DSLAM) v centrále poskytovatele služeb. DSLAM agreguje více ADSL připojení a směruje datový provoz k páteřní síti internetu, zatímco hlasový provoz udržuje na veřejné telefonní komutované síti ([PSTN](/mobilnisite/slovnik/pstn/)). ADSL podporuje různé datové rychlosti v závislosti na podmínkách linky, s teoretickými maximy až 24 Mbps ve směru dolů a 3,5 Mbps ve směru nahoru za ideálních podmínek s technologií ADSL2+.

V kontextech 3GPP se ADSL objevuje především v dokumentech souvisejících s konvergencí pevných a mobilních sítí, správou sítí a rámci kvality služeb. Zatímco 3GPP se zaměřuje na standardy mobilní telekomunikace, odkazy na ADSL uznávají souběžnou existenci pevných a mobilních sítí v konvergovaných nabídkách služeb. Tato technologie představuje důležitou historickou širokopásmovou přístupovou metodu, která koexistuje s mobilními sítěmi v heterogenních síťových prostředích, což je zvláště relevantní pro operátory poskytující jak pevné, tak mobilní služby.

## K čemu slouží

ADSL byl vyvinut za účelem poskytování širokopásmového přístupu k internetu přes stávající měděnou telefonní infrastrukturu bez nutnosti nákladných nových kabelových instalací. Před ADSL byl přístup k internetu přes telefonní linky omezen na vytáčené modemy pracující rychlostmi pod 56 kbps, které blokovaly hlasovou linku a nabízely nedostatečnou šířku pásma pro nové multimediální aplikace. ADSL tato omezení vyřešil tím, že umožnil trvalá širokopásmová připojení, která nenarušovala hlasovou službu, dramaticky zvýšil dostupnou šířku pásma a zároveň využil stávající infrastrukturní investice.

Technologie reagovala na rostoucí poptávku po vysokorychlostním přístupu k internetu na konci 90. let a začátku 21. století, zejména u rezidenčních uživatelů. Její asymetrický návrh byl specificky cílen na spotřebitelské vzorce využití internetu, kde stahování webových stránek, streamování médií a přijímání souborů vyžadovalo výrazně větší šířku pásma než odesílání obsahu. Tato optimalizace umožnila poskytovatelům služeb maximalizovat efektivitu využití šířky pásma a obsloužit více zákazníků přes stávající infrastrukturu při zachování zpětné kompatibility s tradičními telefonními službami.

V dokumentaci 3GPP se ADSL objevuje v kontextech, kde mobilní sítě rozhraní s pevnými širokopásmovými sítěmi nebo je doplňují. Dokumenty jako 32.833 (Charging management) a 33.812 (Security) odkazují na ADSL ve scénářích zahrnujících konvergované služby, zatímco 43.901 (Network Management) zahrnuje ADSL do rámců monitorování výkonu sítě. Tyto odkazy uznávají, že mobilní operátoři často také poskytují pevné služby a potřebují integrované systémy správy, přestože ADSL samo o sobě není mobilní technologií definovanou 3GPP.

## Klíčové vlastnosti

- Frekvenční dělení multiplexem oddělující hlasové a datové pásmo
- Modulace diskrétním multitonem (DMT) s adaptivním přidělováním bitů
- Asymetrické přidělování šířky pásma ve prospěch provozu ve směru dolů
- Současný přenos hlasu a dat přes jediný měděný pár
- Podpora různých datových rychlostí až do 24 Mbps ve směru dolů s ADSL2+
- Kompatibilita se stávající telefonní infrastrukturou bez přezkouvání

## Související pojmy

- [DSL – Digital Subscriber Line](/mobilnisite/slovnik/dsl/)

## Definující specifikace

- **TS 32.833** (Rel-11) — Converged OSS End-to-End Management Study
- **TS 33.812** (Rel-9) — M2M Remote Subscription Management Security
- **TR 43.901** (Rel-19) — Generic Access to A/Gb Interface Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [ADSL na 3GPP Explorer](https://3gpp-explorer.com/glossary/adsl/)
