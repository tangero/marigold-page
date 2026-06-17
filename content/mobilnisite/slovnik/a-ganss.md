---
slug: "a-ganss"
url: "/mobilnisite/slovnik/a-ganss/"
type: "slovnik"
title: "A-GANSS – Assisted - Galileo and Additional Navigation Satellite Systems"
date: 2025-01-01
abbr: "A-GANSS"
fullName: "Assisted - Galileo and Additional Navigation Satellite Systems"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/a-ganss/"
summary: "A-GANSS je standard 3GPP pro poskytování asistenčních dat mobilním zařízením za účelem zlepšení výkonu určování polohy s využitím systému Galileo a dalších globálních navigačních satelitních systémů ("
---

A-GANSS je standard 3GPP, který poskytuje mobilním zařízením asistenční data přes buněčné sítě za účelem zlepšení výkonu určování polohy s využitím systému Galileo a dalších globálních navigačních satelitních systémů mimo GPS.

## Popis

A-GANSS je standardizovaná technologie určování polohy v rámci 3GPP, která rozšiřuje Assisted-GPS ([A-GPS](/mobilnisite/slovnik/a-gps/)) o začlenění asistenčních dat pro evropský systém Galileo a další globální navigační satelitní systémy ([GNSS](/mobilnisite/slovnik/gnss/)), jako jsou [GLONASS](/mobilnisite/slovnik/glonass/), BeiDou a QZSS. Funguje jako část architektury lokalizačních služeb v řídicí nebo uživatelské rovině, kde Location Server s podporou Secure User Plane Location (SUPL) (např. SLP) nebo Mobile Location Center ([MLC](/mobilnisite/slovnik/mlc/)) v řídicí rovině doručuje asistenční data uživatelskému zařízení (UE). Tato asistenční data zahrnují informace o satelitních drahách v reálném čase nebo předpovězené (efemeridy), hrubá data satelitního almanachu, ionosférické korekční parametry, data UTC modelu a parametry asistence pro příjem přizpůsobené konkrétním GNSS konstelacím. UE využívají tato předem dodaná data k výraznému zkrácení času do prvního určení polohy (TTFF) a ke zlepšení citlivosti, protože nemusí tuto pomalu se měnící informaci dekódovat přímo ze satelitních signálů, které mohou být slabé v interiérech nebo městských kaňonech.

Architektura zahrnuje několik klíčových síťových prvků: UE s přijímačem schopným více GNSS, přístupovou rádiovou síť (RAN), která přenáší asistenční data, a lokalizační server v jádru sítě. Lokalizační server, jako je Evolved Serving Mobile Location Center ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5G, generuje nebo získává GNSS asistenční data. Tato data jsou formátována podle protokolů 3GPP (např. zprávy [RRC](/mobilnisite/slovnik/rrc/) nebo [LPP](/mobilnisite/slovnik/lpp/)/LPPa) a jsou doručena UE na požádání nebo proaktivně. UE provádí měření satelitních signálů (pseudovzdálenosti, Dopplerův jev) s využitím asistenčních dat ke zúžení vyhledávacího okna. Tato surová měření nebo vypočtená poloha pak mohou být odeslána zpět do sítě pro další zpracování nebo ověření v hybridních metodách určování polohy.

A-GANSS podporuje více operačních režimů: UE-based, kde UE vypočítává svou vlastní polohu; UE-assisted, kde UE odesílá měření do sítě pro výpočet; a standalone, přičemž hlavní hodnota spočívá v asistovaných režimech. Asistenční data jsou standardizována v binárních formátech v rámci 3GPP TS 25.453 a 25.173, což zajišťuje interoperabilitu mezi síťovými zařízeními a koncovými zařízeními od různých výrobců. Využitím více konstelací A-GANSS zvyšuje dostupnost, přesnost a integritu polohového řešení. V náročných prostředích je viditelných více satelitů, což umožňuje lepší geometrické zředění přesnosti (GDOP). Tato podpora více konstelací je základní schopností pro moderní služby vysoce přesného určování polohy, včetně těch požadovaných pro automobilové aplikace, logistiku a aplikace veřejné bezpečnosti.

## K čemu slouží

A-GANSS byl vytvořen, aby řešil omezení spočívající v závislosti pouze na americkém globálním polohovém systému (GPS) pro určování polohy asistované buněčnou sítí. Před jeho zavedením standardy 3GPP primárně podporovaly A-GPS (Assisted GPS). Závislost na jediné satelitní konstelaci však představovala rizika spojená s dostupností služby, geopolitickou kontrolou a výkonem v prostředích s překážkami, kde samotné GPS signály nemusely stačit. Vývoj systému Galileo, nezávislého evropského globálního satelitního navigačního systému, spolu s modernizací dalších systémů, jako je ruský GLONASS a čínský BeiDou, motivovaly 3GPP ke standardizaci obecného rámce pro asistování jakémukoli současnému nebo budoucímu GNSS.

Základním problémem, který A-GANSS řeší, je zlepšení výkonu, spolehlivosti a univerzálnosti určování polohy mobilních zařízení. Začleněním asistence pro více konstelací zajišťuje rychlejší a robustnější určení polohy, což je prvořadé pro regulované nouzové služby jako E911 v USA a E112 v Evropě. Tyto požadavky vyžadují od operátorů poskytnutí přesné polohy volajícího, často v řádu desítek metrů, a A-GANSS pomáhá těmto požadavkům vyhovět v městských a vnitřních scénářích, kde řešení pouze s GPS mohou selhávat nebo být příliš pomalá. Dále snižuje spotřebu energie na UE zkrácením aktivní doby vyhledávání satelitů, čímž prodlužuje výdrž baterie pro aplikace založené na poloze.

Historicky se zavedení A-GANSS v 3GPP Release 8 časově shodovalo s počáteční fází nasazení systému Galileo a rostoucím uznáním výhod více GNSS v odvětví. Zajistilo budoucí kompatibilitu standardů 3GPP pro určování polohy, což umožňuje bezproblémovou integraci nových satelitních systémů bez nutnosti zcela nového návrhu protokolů. Tato rozšiřitelnost řešila omezení dřívějšího rámce A-GPS, který byl pevně naprogramován pro konkrétní konstelaci, a tím umožnila globální interoperabilitu a podpořila inovace v ekosystému lokalizačních služeb.

## Klíčové vlastnosti

- Poskytuje síťově generovaná asistenční data pro konstelace Galileo, GLONASS, BeiDou, QZSS a dalších GNSS
- Významně snižuje čas do prvního určení polohy (TTFF) a zlepšuje citlivost příjmu ve srovnání se samostatným GNSS
- Podporuje jak UE-based, tak UE-assisted režimy určování polohy pro flexibilitu
- Umožňuje provoz v náročných signálových prostředích (městské kaňony, interiéry) díky viditelnosti více konstelací
- Standardizované formáty asistenčních dat (např. v RRC a LPP) zajišťují interoperabilitu mezi více výrobci
- Snižuje spotřebu energie UE poskytováním předem uložených dat o satelitních drahách a čase

## Související pojmy

- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 25.172** (Rel-19) — A-GANSS UE Minimum Performance Requirements (FDD)
- **TS 25.173** (Rel-19) — A-GANSS Performance Requirements (TDD)
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 45.005** (Rel-19) — GSM RF Requirements for MS and BSS

---

📖 **Anglický originál a plná specifikace:** [A-GANSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/a-ganss/)
