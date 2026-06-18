---
slug: "ti"
url: "/mobilnisite/slovnik/ti/"
type: "slovnik"
title: "TI – Transaction Identifier"
date: 2025-01-01
abbr: "TI"
fullName: "Transaction Identifier"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ti/"
summary: "Jedinečný identifikátor používaný v různých protokolech 3GPP pro korelaci zpráv náležejících ke stejné transakci nebo proceduře mezi síťovými entitami. Je zásadní pro správu dialogu, řízení relací a z"
---

TI je jedinečný identifikátor používaný v protokolech 3GPP pro korelaci zpráv náležejících ke stejné transakci nebo proceduře mezi síťovými entitami za účelem správy dialogu a spolehlivé signalizace.

## Popis

Transaction Identifier (TI) je základní pole používané napříč více signalizačními protokoly 3GPP k jednoznačné identifikaci konkrétní transakce nebo dialogu mezi dvěma partnerskými entitami. Transakce typicky zahrnuje požadavek a k němu příslušnou odpověď (odpovědi). TI umožňuje přijímající entitě přiřadit příchozí zprávu probíhající transakci nebo identifikovat začátek nové, což umožňuje správnou činnost stavového automatu a zabraňuje záměně zpráv. Jeho implementace a velikost se liší v závislosti na konkrétní protokolové vrstvě a službě.

Jedna z jeho nejklasičtějších a nejpodrobnějších definic je v protokolech Mobility Management ([MM](/mobilnisite/slovnik/mm/)) a Call Control ([CC](/mobilnisite/slovnik/cc/)) na [NAS](/mobilnisite/slovnik/nas/) vrstvě, jak je specifikováno v TS 24.008. V tomto kontextu je TI 4bitová hodnota, která identifikuje konkrétní MM spojení nebo instanci CC entity. Používá se k multiplexování několika nezávislých transakcí (např. více současných pokusů o volání nebo přenosů [SMS](/mobilnisite/slovnik/sms/)) přes stejné signalizační spojení. TI je přiřazeno iniciující entitou na začátku transakce a je obsaženo v každé následující zprávě související s touto transakcí. Kombinace hodnoty TI a příznaku TI (který označuje, která strana, mobilní nebo síťová, transakci zahájila) poskytuje jedinečnou referenci.

Mimo TS 24.008 se koncept Transaction Identifier objevuje v mnoha dalších specifikacích. Například v [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)) pro řídicí rovinu ([GTP-C](/mobilnisite/slovnik/gtp-c/)) je v hlavičce přítomno pole Transaction ID pro párování požadavků a odpovědí mezi [GSN](/mobilnisite/slovnik/gsn/). Na rozhraních založených na Diameter (např. S6a, S13) plní podobný účel párování transakcí Hop-by-Hop Identifier. V SIP poskytuje identifikaci transakce/dialogu hlavička Call-ID v kombinaci se značkami. Zatímco tedy termín "TI" často konkrétně odkazuje na identifikátor na NAS vrstvě, širší koncept identifikátoru transakce je všudypřítomným vzorem v telekomunikační signalizaci pro zajištění spolehlivé, stavové a uspořádané interakce protokolů.

## K čemu slouží

Transaction Identifier existuje, aby řešil základní problém korelace a správy stavu v transakčně orientovaných signalizačních protokolech. Při složitých síťových interakcích, zejména mezi mobilním zařízením a síťovým jádrem, může probíhat více paralelních procedur současně – uživatel může navazovat hlasové volání, zároveň přijímat SMS a provádět aktualizaci polohy. Bez jasného identifikátoru k rozlišení zpráv náležejících každé nezávislé proceduře by síť a zařízení nemohly správně zpracovávat odpovědi a udržovat oddělené stavy, což by vedlo k přerušení hovorů, ztrátě zpráv nebo chybám protokolu.

Jeho zavedení, zejména v základních GSM protokolech (vyvinutých do 3GPP Rel-4 a dále), poskytlo jednoduchý, ale účinný mechanismus pro multiplexování. Malá 4bitová velikost v NAS protokolech odráží raná konstrukční omezení, ale ukázala se dostatečnou pro očekávaný počet souběžných transakcí na účastníka. TI umožňuje efektivní využití signalizačního kanálu a umožňuje funkce jako čekání hovoru a paralelní služby. Motivací bylo vytvořit robustní a předvídatelný rámec pro správu dialogu, který je nezbytný pro spolehlivost služeb.

Jak se protokoly vyvíjely pro 3G, 4G a 5G, základní koncept přetrval a byl adaptován. Zatímco nové protokoly jako Diameter a HTTP/2 používají jiné mechanismy (např. End-to-End ID, Stream ID), plní stejný základní účel, který původně řešil TI. Standardizace TI v dokumentech jako TS 24.008 zajistila interoperabilitu mezi zařízeními od různých výrobců a vytvořila základní koncept pro spolehlivou mobilní komunikaci. Řeší omezení bezspojové nebo bezstavové signalizace, kde je korelace odpovědí nejednoznačná, a zajišťuje, že každá zpráva může být přesně přiřazena svému zamýšlenému kontextu.

## Klíčové vlastnosti

- Jednoznačně identifikuje signalizační transakci nebo dialog v rámci relace protokolu.
- Umožňuje multiplexování více paralelních transakcí přes jediné signalizační spojení.
- Používá se ke korelaci požadavků s jejich odpovídajícími odpověďmi.
- Definován v základních protokolech jako NAS (TS 24.008) a GTP.
- Kritický pro správnou činnost stavového automatu v síťových entitách.
- Základní vzor adaptovaný napříč mnoha signalizačními rozhraními 3GPP.

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.838** (Rel-9) — IMS Service Continuity and Inter-UE Transfer Enhancements
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TR 38.810** (Rel-16) — NR OTA Test Methods Study
- **TS 44.068** (Rel-19) — Group Call Control (GCC) Protocol for VGCS

---

📖 **Anglický originál a plná specifikace:** [TI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ti/)
