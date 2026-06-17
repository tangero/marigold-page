---
slug: "aoc-e"
url: "/mobilnisite/slovnik/aoc-e/"
type: "slovnik"
title: "AOC-E – Advice Of Charge - at the End of the communication"
date: 2026-01-01
abbr: "AOC-E"
fullName: "Advice Of Charge - at the End of the communication"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aoc-e/"
summary: "AOC-E je služba účtování podle specifikací 3GPP, která poskytuje uživatelům podrobné informace o nákladech po dokončení komunikačních relací. Umožňuje přesné fakturační vyúčtování po relaci shromažďov"
---

AOC-E je služba účtování podle specifikací 3GPP, která poskytuje uživatelům podrobné informace o nákladech po ukončení komunikační relace za účelem zvýšení transparentnosti fakturace.

## Popis

Advice Of Charge - at the End of the communication (AOC-E, tedy Oznámení o poplatku na konci komunikace) je standardizovaná služba 3GPP, která poskytuje účastníkům komplexní účtovací informace po ukončení jejich komunikačních relací. Služba funguje v rámci účtovací architektury definované specifikacemi 3GPP a shromažďuje účtovací data z různých síťových prvků, včetně Serving Call Session Control Function (S-CSCF), Application Servers a Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) v sítích IMS. Tyto prvky generují Charging Data Records ([CDR](/mobilnisite/slovnik/cdr/)) nebo účtovací zprávy založené na protokolu Diameter, které obsahují podrobné informace o komunikační relaci, včetně její délky, cíle, typu služby a použitelných tarifů.

Architektura služby AOC-E zahrnuje několik funkčních komponent pracujících ve vzájemné koordinaci. Charging Trigger Function ([CTF](/mobilnisite/slovnik/ctf/)) detekuje zpoplatnitelné události během komunikačních relací a předává účtovací informace Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)) nebo Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)). V offline účtovacích scénářích CDF přijímá účtovací události a generuje CDR, které jsou uloženy v Charging Gateway Function ([CGF](/mobilnisite/slovnik/cgf/)). CGF následně tyto záznamy předává do fakturačního systému ke zpracování. V online účtovacích scénářích OCS provádí kontrolu kreditu v reálném čase a generuje účtovací data, která lze využít pro AOC-E.

Po ukončení komunikační relace síť zpracovává nashromážděná účtovací data prostřednictvím fakturačního systému, který aplikuje příslušné tarifní politiky a vypočítá konečný poplatek. Služba AOC-E následně tyto informace naformátuje podle preferencí účastníka a doručí je prostřednictvím různých oznamovacích mechanismů. Mezi tyto mechanismy mohou patřit SMS zprávy, multimediální zprávy, oznámení e-mailem nebo push oznámení prostřednictvím dedikovaných aplikací. Formátované oznámení o poplatku typicky zahrnuje celkovou cenu, rozpis nákladů podle jednotlivých komponent služby, příslušné daně a případné uplatněné propagační slevy.

Služba podporuje více účtovacích modelů včetně časového, objemového, událostního a obsahového účtování. Dokáže zvládnout komplexní účtovací scénáře, jako jsou hovory s více účastníky, konferenční hovory a balíčky sdružených služeb. AOC-E se také integruje se systémy správy profilů účastníků, aby respektovala uživatelské preference týkající se frekvence, formátu a způsobu doručování oznámení o poplatcích. Služba zachovává zpětnou kompatibilitu se staršími účtovacími systémy a zároveň podporuje pokročilé funkce v novějších síťových architekturách, což z ní činí univerzální řešení pro operátory přecházející mezi generacemi sítí.

## K čemu slouží

AOC-E byla vyvinuta, aby řešila rostoucí potřebu transparentního a přesného účtování v telekomunikačních sítích. Před její standardizací operátoři používali proprietární systémy oznamování poplatků, kterým chyběla interoperabilita a konzistence mezi různými sítěmi a poskytovateli služeb. To vytvářelo zmatek u účastníků, kteří přecházeli mezi sítěmi nebo využívali služby roamingu, protože dostávali nekonzistentní účtovací informace v různých formátech a s různou mírou podrobností. Nedostatek standardizace také ztěžoval operátorům s více sítěmi poskytovat jednotný zážitek z účtování svým zákazníkům.

Hlavní motivací pro vytvoření AOC-E bylo zvýšení spokojenosti zákazníků poskytováním spolehlivých, standardizovaných účtovacích informací po relaci. Tím se řeší několik klíčových problémů: snižuje se počet fakturačních sporů tím, že účastníci dostávají jasnou dokumentaci poplatků, pomáhá uživatelům spravovat své komunikační rozpočty poskytováním včasných informací o nákladech a zvyšuje důvěru v fakturační postupy operátora. Služba také podporuje regulatorní požadavky v mnoha jurisdikcích, které nařizují transparentní fakturační postupy a právo spotřebitelů na podrobné účtovací informace.

Z technického hlediska AOC-E řeší problém fragmentovaných systémů oznamování poplatků tím, že poskytuje standardizovaný rámec fungující napříč různými síťovými architekturami (komutovaná okruhová, komutovaná paketová a IMS) a typy služeb (hlas, video, zasílání zpráv, data). Umožňuje operátorům implementovat konzistentní politiky oznamování poplatků bez ohledu na podkladovou síťovou technologii nebo platformu pro poskytování služeb. Tato standardizace snižuje provozní složitost a umožňuje efektivnější integraci fakturačních systémů, zejména v síťových prostředích s více dodavateli, kde různí výrobci zařízení mohou implementovat účtovací funkce odlišně.

## Klíčové vlastnosti

- Standardizované doručování oznámení o poplatcích po relaci
- Podpora více oznamovacích metod včetně SMS a e-mailu
- Integrace s offline i online účtovacími systémy
- Flexibilní možnosti formátování pro prezentaci poplatků
- Kompatibilita s více síťovými architekturami (CS, PS, IMS)
- Správa preferencí účastníka pro přizpůsobení oznámení

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.647** (Rel-19) — Advice of Charge (AOC) service protocol
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony

---

📖 **Anglický originál a plná specifikace:** [AOC-E na 3GPP Explorer](https://3gpp-explorer.com/glossary/aoc-e/)
