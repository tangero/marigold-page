---
slug: "a-gnss"
url: "/mobilnisite/slovnik/a-gnss/"
type: "slovnik"
title: "A-GNSS – Assisted Global Navigation Satellite Systems"
date: 2025-01-01
abbr: "A-GNSS"
fullName: "Assisted Global Navigation Satellite Systems"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/a-gnss/"
summary: "A-GNSS je síťově asistovaná lokalizační technologie, která zvyšuje rychlost a přesnost určení polohy mobilních zařízení. Poskytuje asistenční data ze satelitů (např. efemeridy, almanach) přes mobilní"
---

A-GNSS je síťově asistovaná lokalizační technologie, která zvyšuje rychlost a přesnost určení polohy mobilních zařízení tím, že poskytuje asistenční data ze satelitů přes mobilní sítě.

## Popis

A-GNSS je hybridní lokalizační metoda standardizovaná organizací 3GPP, která kombinuje globální navigační satelitní systémy (GNSS), jako jsou GPS, GLONASS, Galileo nebo BeiDou, s asistencí mobilní sítě. Základní princip spočívá v tom, že síť doručuje předzpracovaná satelitní data uživatelskému zařízení (UE), což umožňuje zařízení vypočítat svou polohu rychleji a s nižší spotřebou energie než v případě samostatného GNSS. Architektura typicky zahrnuje lokalizační server (např. Secure User Plane Location (SUPL) Enabled Location Server - SLP nebo řídicí rovinné entity jako E-SMLC), který shromažďuje asistenční data z referenčních přijímačů GNSS a distribuuje je k UE pomocí protokolů řídicí nebo uživatelské roviny. UE tato data, která mohou zahrnovat přesné satelitní dráhy (efemeridy), korekce hodin, ionosférické modely a přibližný čas a polohu, využívá ke zrychlení příjmu satelitních signálů a výpočtu polohy.

Operačně proces začíná, když je spuštěn požadavek na určení polohy, ať už sítí (např. pro tísňové služby) nebo UE (např. pro navigační aplikaci). UE naváže spojení s lokalizačním serverem, který následně poskytne asistenční data přizpůsobená přibližné poloze a schopnostem UE. Tato data umožňují přijímači GNSS v UE předpovědět, které satelity jsou viditelné a jaké mají očekávané parametry signálu, což drasticky zmenšuje prohledávaný prostor pro satelitní signály. Následně se čas do prvního určení polohy (TTFF) zkrátí z desítek sekund (v samostatném režimu) na několik sekund a citlivost se zlepší, což umožňuje určení polohy i při slabším signálu, například uvnitř budov nebo pod hustým porostem.

Klíčové součásti zahrnují UE s přijímačem podporujícím A-GNSS, rádiový přístupový síť (RAN) a jádrovou síť (CN) mobilní sítě a lokalizační server. Lokalizační server komunikuje s referenčními sítěmi GNSS, aby získal aktuální satelitní data. Protokoly jako Radio Resource Location Protocol (RRLP) pro GSM, Radio Resource Control (RRC) pro UMTS/LTE nebo LTE Positioning Protocol (LPP) pro LTE/NR se používají přes řídicí rovinu, zatímco Secure User Plane Location (SUPL) využívá IP transport přes uživatelskou rovinu. A-GNSS podporuje různé režimy: UE-asistovaný, kde UE měří satelitní signály a odesílá surová měření do sítě pro výpočet polohy; a UE-bázi, kde UE vypočítává svou vlastní polohu pomocí asistenčních dat. Tato technologie je nedílnou součástí lokalizačního rámce 3GPP a často je kombinována s jinými metodami, jako je Observed Time Difference of Arrival (OTDOA) nebo Enhanced Cell ID, pro hybridní lokalizační řešení.

## K čemu slouží

A-GNSS byl zaveden, aby řešil omezení samostatných přijímačů GNSS v mobilních zařízeních, zejména pomalý čas do prvního určení polohy (TTFF), vysokou spotřebu energie a špatný výkon v náročných podmínkách příjmu signálu. Samostatný GNSS vyžaduje, aby přijímač stáhl satelitní efemeridy a data almanachu přímo ze satelitů, což může trvat 30 sekund nebo více kvůli nízké přenosové rychlosti (50 bps pro GPS), a selhává v oblastech se slabým signálem. Pro tísňové služby jako E911 v USA nebo E112 v Evropě je rychlé a spolehlivé určení polohy zákonem vyžadováno, což činí samostatný GNSS nedostatečným. A-GNSS tyto problémy řeší využitím šířky pásma mobilní sítě pro rychlé doručení asistenčních dat, což umožňuje rychlejší určení polohy a rozšiřuje provozní rozsah na scénáře uvnitř budov a městských kaňonů.

Historicky se A-GNSS objevil v 3GPP Release 7 jako součást širšího rámce Location Services (LCS), poháněn regulatorními požadavky na lokalizaci tísňových volajících a rostoucí poptávkou po komerčních službách založených na poloze (např. navigace, geotagging). Předchozí přístupy spoléhaly na síťové metody jako Cell ID nebo časové posuny, které nabízely omezenou přesnost (stovky metrů až kilometry), nebo vyžadovaly dedikovaný GPS hardware s dlouhou dobou příjmu. A-GNSS poskytl nákladově efektivní, standardizovaný způsob, jak vylepšit stávající schopnosti GNSS bez zásadních změn hardwaru, což usnadnilo jeho rozšířené přijetí ve smartphonech a IoT zařízeních. Také snižuje vybíjení baterie UE zkrácením doby aktivního zpracování GNSS a umožňuje přijímači častěji přecházet do stavů s nízkou spotřebou.

Technologie se dále vyvíjí, aby podporovala nové konstelace GNSS, zlepšovala přesnost pomocí asistence typu real-time kinematic (RTK) nebo precise point positioning (PPP) a integrovala se s lokalizací v 5G NR. Řeší potřebu vysoké přesnosti lokalizace v aplikacích jako autonomní vozidla, navigace dronů a průmyslové IoT, kde je vyžadována přesnost na úrovni pod metr. Přenesením složitých výpočtů a získávání dat na síť umožňuje A-GNSS tenčí a energeticky účinnější návrhy UE při zachování robustního výkonu v různorodých prostředích.

## Klíčové vlastnosti

- Snižuje čas do prvního určení polohy (TTFF) z ~30 sekund na méně než 10 sekund poskytnutím předvypočítaných satelitních efemerid a dat almanachu
- Zlepšuje citlivost přijímače až o 20 dB, což umožňuje lokalizaci v podmínkách slabého signálu, jako jsou vnitřní prostory nebo městské kaňony
- Podporuje více konstelací GNSS včetně GPS, GLONASS, Galileo a BeiDou prostřednictvím standardizovaných formátů asistenčních dat
- Umožňuje jak UE-bázi (autonomní výpočet), tak UE-asistovaný (výpočet sítí) lokalizační režimy pro flexibilitu
- Využívá protokoly řídicí roviny (např. RRLP, LPP) nebo uživatelské roviny (SUPL) pro doručování asistenčních dat napříč generacemi 3GPP
- Integruje se s jinými lokalizačními metodami (např. OTDOA, WLAN) pro hybridní lokalizační řešení za účelem zvýšení přesnosti a dostupnosti

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 34.171** (Rel-9) — A-GPS FDD UE Conformance Testing Procedures
- **TS 36.171** (Rel-19) — A-GNSS Minimum Performance Requirements for UE
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 37.857** (Rel-13) — Study on Indoor Positioning Enhancements
- **TS 38.171** (Rel-19) — 5G A-GNSS UE Positioning Requirements
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification
- **TS 45.005** (Rel-19) — GSM RF Requirements for MS and BSS
- **TS 51.010** (Rel-19) — SIM Application Toolkit Conformance Testing

---

📖 **Anglický originál a plná specifikace:** [A-GNSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/a-gnss/)
