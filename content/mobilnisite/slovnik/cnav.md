---
slug: "cnav"
url: "/mobilnisite/slovnik/cnav/"
type: "slovnik"
title: "CNAV – Civil Navigation"
date: 2025-01-01
abbr: "CNAV"
fullName: "Civil Navigation"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cnav/"
summary: "CNAV je služba 3GPP poskytující schopnosti civilní navigace, primárně pro satelitní polohovací systémy jako GPS a Galileo, integrované do mobilních sítí. Umožňuje zařízením přijímat a zpracovávat navi"
---

CNAV je služba 3GPP, která integruje schopnosti civilní navigace ze systémů jako GPS do mobilních sítí za účelem poskytování lokalizačních služeb pro zařízení.

## Popis

CNAV (Civil Navigation) je standardizovaná služba v rámci 3GPP, která usnadňuje doručování a zpracování dat civilní navigace, například z globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)) jako [GPS](/mobilnisite/slovnik/gps/), Galileo, [GLONASS](/mobilnisite/slovnik/glonass/) a BeiDou, prostřednictvím mobilních sítí. Funguje jako součást polohovacího rámce, kde síť pomáhá uživatelskému zařízení (UE) s akvizicí a interpretací satelitních signálů pro určení geografické polohy. Architektura zahrnuje komponenty jako Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5G nebo Enhanced Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE, které generují asistenční data – včetně efemerid, almanachu a časových informací – a přenášejí je k UE pomocí protokolů řídicí nebo uživatelské roviny. Tato asistence snižuje čas do prvního určení polohy ([TTFF](/mobilnisite/slovnik/ttff/)) a zlepšuje přesnost, zejména v náročných prostředích, jako jsou městské kaňony nebo vnitřní prostory, kde jsou satelitní signály slabé.

Co se týče fungování, CNAV využívá specifikace jako 3GPP TS 36.355 pro LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) a TS 37.355 pro NR Positioning Protocol (NRPP), které definují zprávy vyměňované mezi UE a sítí pro určování polohy. UE si vyžádá nebo přijme nevyžádaná asistenční data, zpracuje je pro korelaci s přijímanými satelitními signály a vypočítá svou polohu pomocí metod jako Assisted GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). Mezi klíčové komponenty patří GNSS přijímač v UE, polohovací server v síti (např. LMF) a rozhraní jako LTE Positioning Protocol Annex (LPPa) pro komunikaci mezi síťovými uzly. Úlohou CNAV je umožnit efektivní, sítí asistované určování polohy, které zvyšuje výkonnost oproti samostatnému GNSS, a bezproblémově jej integrovat s celulární konektivitou pro služby polohování v reálném čase.

Služba podporuje různé polohovací techniky, včetně A-GNSS, Observed Time Difference of Arrival (OTDOA) a Enhanced Cell ID (E-CID), přičemž CNAV se zaměřuje na aspekty GNSS. Zahrnuje funkce jako monitorování integrity v reálném čase, kde síť může poskytovat data o stavu nebo chybách satelitů, a podporu více konstelací pro zvýšení robustnosti. V systémech 5G se CNAV vyvíjí spolu s New Radio (NR) a zahrnuje vyšší požadavky na přesnost pro aplikace jako autonomní vozidla nebo průmyslový IoT. Integrace s network slicing umožňuje přizpůsobené polohovací služby pro různé případy užití a zajišťuje nízkou latenci a vysokou spolehlivost. Celkově je CNAV základním prvkem polohovacího ekosystému 3GPP, který propojuje satelitní navigaci a mobilní komunikaci za účelem poskytnutí všudypřítomného povědomí o poloze.

## K čemu slouží

CNAV byl vytvořen, aby řešil potřebu spolehlivých, přesných a rychlých polohovacích služeb v mobilních zařízeních s využitím rozšířeného nasazení GNSS. Před jeho standardizací trpěly samostatné GNSS přijímače v telefonech často dlouhou dobou akvizice, špatným výkonem v oblastech se slabým signálem a vysokou spotřebou energie. Integrací dat civilní navigace do sítí 3GPP CNAV tyto problémy řeší poskytováním síťové asistence, která snižuje TTFF, zvyšuje přesnost v městském nebo vnitřním prostředí a šetří životnost baterie zařízení díky optimalizovanému zpracování signálu. To bylo motivováno rostoucí poptávkou po lokalizačních aplikacích, regulatorními požadavky na lokalizaci tísňových volání (např. E911 v USA) a expanzí služeb IoT vyžadujících přesné sledování.

Historicky rané mobilní určování polohy spoléhalo na síťové metody jako Cell ID, které nabízely omezenou přesnost. Zavedení CNAV v 3GPP Release 8 znamenalo posun k hybridním přístupům kombinujícím GNSS s celulární asistencí, aby byly splněny přísnější požadavky na přesnost. Řešilo omezení předchozích přístupů standardizací protokolů pro doručování asistenčních dat, což umožnilo interoperabilitu napříč zařízeními a sítěmi, a podporou více GNSS konstelací pro globální pokrytí. V průběhu releasů se CNAV vyvíjel, aby podporoval nové potřeby, jako je vysoce přesné polohování pro automobilový a průmyslový sektor, poháněné pokrokem v satelitní technologii a nízkolatenčními schopnostmi 5G. Jeho účel přesahuje základní navigaci a umožňuje kritické služby jako záchranné operace, optimalizaci logistiky a výpočty zohledňující polohu v moderním propojeném světě.

## Klíčové vlastnosti

- Síťově asistované doručování GNSS dat prostřednictvím protokolů LPP/NRPP
- Podpora více satelitních konstelací (GPS, Galileo atd.)
- Snížení času do prvního určení polohy (TTFF) a zvýšení přesnosti
- Integrace s polohovací architekturou 3GPP (např. LMF, E-SMLC)
- Monitorování integrity a stavu navigačních signálů v reálném čase
- Kompatibilita s metodami určování polohy v řídicí a uživatelské rovině

## Související pojmy

- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 44.031** (Rel-19) — Radio Resource LCS Protocol (RRLP)

---

📖 **Anglický originál a plná specifikace:** [CNAV na 3GPP Explorer](https://3gpp-explorer.com/glossary/cnav/)
