---
slug: "lpwa"
url: "/mobilnisite/slovnik/lpwa/"
type: "slovnik"
title: "LPWA – Low-Power Wide-Area"
date: 2026-01-01
abbr: "LPWA"
fullName: "Low-Power Wide-Area"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/lpwa/"
summary: "LPWA označuje třídu bezdrátových technologií navržených pro IoT zařízení, která vyžadují komunikaci na dlouhou vzdálenost, mnohaletou výdrž baterie a nízké náklady na zařízení. Mezi standardizovaná LP"
---

LPWA je třída standardizovaných bezdrátových technologií 3GPP, jako jsou NB-IoT a LTE-M, navržená pro IoT zařízení, která potřebují dlouhý dosah, roky provozu na baterii a nízkou cenu.

## Popis

Low-Power Wide-Area (LPWA) není jediná technologie, ale kategorie síťových konektivitních řešení charakterizovaných několika klíčovými atributy: velmi nízká spotřeba energie (umožňující výdrž baterie 10+ let), rozšířené pokrytí (často o 20+ dB lepší než tradiční mobilní sítě, dosahující hluboko do interiérů a sklepů), nízká složitost a cena zařízení a podpora pro masivní počet připojení. V rámci ekosystému 3GPP je LPWA realizováno prostřednictvím dvou hlavních standardů: Narrowband Internet of Things (NB-IoT) a LTE for Machine-Type Communications (LTE-M, známé také jako eMTC). Nejde o samostatné sítě, ale o optimalizované režimy provozu nasazené v rámci stávajícího spektra LTE a 5G NR, které využívají speciální návrh fyzické vrstvy a protokoly vyšších vrstev k dosažení cílů LPWA.

NB-IoT je nejextrémnější variantou LPWA, využívá velmi úzké pásmo 180 kHz (jeden zdrojový blok v LTE). Lze jej nasadit třemi způsoby: in-band uvnitř nosiče LTE, v ochranném pásmu nosiče LTE nebo jako samostatný nosič. Jeho architektura radikálně zjednodušuje návrh UE: používá jedinou anténu, poloduplexní provoz a velmi nízké špičkové datové rychlosti (~250 kbps pro downlink, ~20 kbps pro uplink v pozdějších verzích). Používá techniky jako úrovně rozšíření pokrytí (Coverage Enhancement, [CE](/mobilnisite/slovnik/ce/)), které využívají rozsáhlého opakování signálů pro zvýšení link budgetu zařízení v náročných lokalitách. Režim úspory energie (Power Saving Mode, PSM) a rozšířený přerušovaný příjem (Extended Discontinuous Reception, eDRX) jsou klíčové funkce, které umožňují zařízení spát po dlouhá období a probouzet se pouze na krátkou dobu pro odeslání nebo přijetí dat, což je základním kamenem jeho provozu s ultra nízkou spotřebou.

LTE-M nabízí schopnější LPWA řešení využívající pásmo šířky 1,4 MHz. Poskytuje vyšší datové rychlosti (až ~1 Mbps), podporu mobility a předávání hovoru mezi buňkami (handover) a hlasové služby (VoLTE). Je vhodnější pro aplikace jako nositelná elektronika, sledovací zařízení pro majetek nebo zdravotní monitory, které se mohou pohybovat nebo vyžadují mírně vyšší datový propust. Z architektonického hlediska se jak NB-IoT, tak LTE-M připojují ke stejnému paketovému jádru (evolved packet core, EPC) nebo 5G core síti jako běžná LTE zařízení, ale používají optimalizované signalizační procedury (např. optimalizace Cellular IoT EPS přes řídicí rovinu) ke snížení režie pro malé a nepravidelné přenosy dat. Síť tato zařízení efektivně spravuje pomocí funkcí jako doručování ne-IP dat (Non-IP Data Delivery, [NIDD](/mobilnisite/slovnik/nidd/)) a podpora komunikace s vysokou latencí, která uvolňuje časové požadavky za účelem další úspory energie zařízení. V 5G jsou schopnosti LPWA integrovány do frameworku 5G NR, přičemž zařízení NR light (RedCap) přebírají a rozšiřují principy LPWA pro éru 5G.

## K čemu slouží

Koncept LPWA vznikl, aby řešil potřeby konektivity pro masivní internet věcí (IoT), což je segment trhu, který tradiční mobilní sítě (příliš energeticky náročné a drahé) a nelicencované LPWA technologie jako LoRa a Sigfox (kterým chybí garantovaná kvalita služby, zabezpečení a bezproblémová integrace do sítí operátorů) obsluhují nedostatečně. Před standardy LPWA od 3GPP neměli operátoři konkurenceschopné, standardizované řešení pro připojení miliard nízkonákladových senzorů pro chytrá města, utility, zemědělství a průmyslový monitoring.

Motivací 3GPP pro standardizaci NB-IoT a LTE-M bylo využít stávající globální mobilní infrastrukturu – s jejími inherentními vlastnostmi, jako je zabezpečení, spolehlivost a škálovatelnost – k uchopení příležitosti IoT. Tyto technologie řeší základní triádu výzev IoT: náklady (levné moduly a zjednodušené nasazení sítě), pokrytí (dosah na vzdálené a hluboko vnitřní senzory) a výdrž baterie (umožnění provozu bez údržby po desetiletí). Jejich vznik byl hnán jasnými případy užití: chytré měřiče, které hlásí jednou denně ze sklepa, environmentální senzory v odlehlých polích nebo sledovací zařízení na přepravních kontejnerech. Tím, že poskytují standardizované řešení v licencovaném spektru, zajišťuje LPWA od 3GPP globální interoperabilitu, robustní zabezpečení děděné z mobilních standardů a jasnou cestu vývoje v rámci frameworku 5G, což chrání investice do IoT do budoucna.

## Klíčové vlastnosti

- Ultra nízká spotřeba energie umožňující výdrž baterie přes 10 let (pomocí PSM, eDRX)
- Rozšířené pokrytí, se ziskem až 20 dB oproti LTE, pro hluboké vnitřní/odlehlé oblasti
- Nízká složitost a cena zařízení (jedna anténa, poloduplex, snížená špičková rychlost)
- Masivní hustota připojení (podpora >50 000 zařízení na buňku)
- Flexibilita nasazení v rámci stávajícího spektra LTE/5G (in-band, guard-band, standalone)
- Bezpečné a spolehlivé připojení využívající autentizaci a šifrování na úrovni 3GPP

## Definující specifikace

- **TR 22.840** (Rel-19) — Study on Ambient power-enabled IoT
- **TS 38.191** (Rel-19) — NR Ambient IoT RF Characteristics
- **TS 38.769** (Rel-20) — Ambient IoT Solutions in NR
- **TR 38.848** (Rel-18) — Technical Report on Ambient IoT

---

📖 **Anglický originál a plná specifikace:** [LPWA na 3GPP Explorer](https://3gpp-explorer.com/glossary/lpwa/)
