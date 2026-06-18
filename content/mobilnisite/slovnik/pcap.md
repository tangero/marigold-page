---
slug: "pcap"
url: "/mobilnisite/slovnik/pcap/"
type: "slovnik"
title: "PCAP – Positioning Calculation Application Part"
date: 2025-01-01
abbr: "PCAP"
fullName: "Positioning Calculation Application Part"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pcap/"
summary: "PCAP je protokol v rámci UTRAN pro podporu polohovacích služeb, jako jsou E-OTD a OTDOA. Zprostředkovává komunikaci mezi Serving Mobile Location Center (SMLC) a Radio Network Controller (RNC) za účele"
---

PCAP je protokol v UTRAN, který umožňuje polohovací služby tím, že zprostředkovává komunikaci mezi Serving Mobile Location Center a Radio Network Controller.

## Popis

Positioning Calculation Application Part (PCAP) je klíčový protokol definovaný v architektuře 3GPP [UTRAN](/mobilnisite/slovnik/utran/), který je speciálně navržen pro podporu polohovacích služeb. Funguje jako aplikační část a zprostředkovává komunikaci mezi Serving Mobile Location Center ([SMLC](/mobilnisite/slovnik/smlc/)) a Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)). Hlavní funkcí PCAP je přenos polohovacích informací, měřicích dat a výpočetních požadavků za účelem umožnění přesného určení polohy uživatelského zařízení (UE). Tento protokol je nezbytný pro implementaci standardizovaných polohovacích metod, jako je Enhanced Observed Time Difference ([E-OTD](/mobilnisite/slovnik/e-otd/)) a Observed Time Difference Of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)), které jsou založeny na časových měřeních z více základnových stanic.

Z architektonického hlediska jsou zprávy PCAP přenášeny přes rozhraní Iupc, které spojuje SMLC a RNC. SMLC funguje jako polohovací server zodpovědný za výpočet polohy UE na základě měření poskytnutých UE a/nebo sítí. RNC na druhé straně spravuje rádiové zdroje a může koordinovat polohovací měření z Node B. PCAP definuje procedury pro zahájení určování polohy, přenos měřicích dat (jako je časový předstih, síla signálu nebo pozorované časové rozdíly) a doručení vypočítaného výsledku polohy. Podporuje jak metody určování polohy s asistencí UE (UE-assisted), tak metody založené na UE (UE-based), což nabízí flexibilitu v závislosti na schopnostech UE a nasazení sítě.

Klíčové komponenty protokolu PCAP zahrnují různé typy zpráv pro řízení určování polohy a přenos dat. Patří mezi ně zprávy pro zahájení určování polohy, požadavek na měření a jeho hlášení, procedury přerušení a ošetření chyb. Protokol zajišťuje spolehlivé doručení polohovacích dat, což je zásadní pro služby vyžadující vysokou přesnost, jako jsou nouzová volání (E911), služby založené na poloze a zákonný odposlech. Role PCAP je nedílnou součástí architektury Location Services ([LCS](/mobilnisite/slovnik/lcs/)) v 3GPP a poskytuje standardizovaný mechanismus pro síťové určování polohy, který je nezávislý na podkladové technologii rádiového přístupu, ačkoli byl původně definován pro UMTS.

Při provozu, když je vyvolán požadavek na polohu (např. nouzovým voláním nebo komerční [LBS](/mobilnisite/slovnik/lbs/) aplikací), použije SMLC PCAP k požádání RNC o zahájení polohovacích procedur. RNC pak může nařídit UE a/nebo Node Bs, aby provedly specifická měření. Naměřená data jsou odeslána zpět do SMLC prostřednictvím zpráv PCAP. SMLC tato data zpracuje pomocí polohovacích algoritmů a vypočítá zeměpisné souřadnice UE. PCAP také podporuje výměnu informací o schopnostech, což umožňuje SMLC a RNC vyjednat podporované polohovací metody a úrovně přesnosti. To zajišťuje interoperabilitu mezi zařízeními různých výrobců a umožňuje škálovatelné nasazení polohovacích služeb v síti.

## K čemu slouží

PCAP byl vytvořen za účelem standardizace signalizačního rozhraní pro polohovací služby v sítích 3GPP, konkrétně v rámci UMTS [UTRAN](/mobilnisite/slovnik/utran/). Před jeho zavedením mohla být pro určování polohy používána proprietární řešení nebo nestandardizovaná rozhraní, což vedlo k problémům s interoperabilitou mezi síťovými prvky různých výrobců. Potřeba standardizovaného protokolu se stala kritickou s regulatorními požadavky na lokalizaci volajícího v nouzových případech (např. E112 v Evropě) a rostoucím trhem komerčních služeb založených na poloze (LBS). PCAP poskytl jednotný způsob komunikace mezi SMLC a RNC, což umožnilo konzistentní a spolehlivé polohovací schopnosti v sítích s více výrobci.

Protokol řeší problém efektivního a přesného určení polohy mobilního účastníka pomocí síťových metod. Řeší výzvu koordinace časových měření mezi UE, více Node Bs a entitou provádějící výpočet polohy. Definováním jasných procedur a formátů zpráv PCAP snižuje složitost implementace polohovacích funkcí a zajišťuje, že polohová data mohou být doručena s požadovanou latencí a přesností pro různé aplikace. Jeho vytvoření bylo motivováno cílem 3GPP umožnit robustní architekturu LCS jako součást služeb jádra sítě od Release 5 dále, s podporou jak okruhově, tak paketově přepínané domény.

PCAP navíc usnadnil vývoj polohovacích technologií v rámci 3GPP. Zatímco počáteční verze se zaměřovaly na metody jako E-OTD a OTDOA, standardizované rozhraní umožnilo začlenění pokročilejších technik v pozdějších verzích, jako je Assisted-GNSS (A-GNSS), aniž by to vyžadovalo zásadní změny signalizačního protokolu. Tato rozšiřitelnost zajistila, že PCAP zůstal relevantní, když se zvyšovaly požadavky na přesnost určování polohy a objevovaly se nové případy užití, včetně navigace, správy vozového parku a doručování obsahu zohledňujícího polohu. Položil základy pro integrovanou podporu určování polohy v následných systémech 4G a 5G, ačkoli konkrétní protokoly se vyvíjely (např. na LPPa v LTE).

## Klíčové vlastnosti

- Standardizovaná signalizace mezi SMLC a RNC přes rozhraní Iupc
- Podpora více polohovacích metod včetně E-OTD a OTDOA
- Procedury pro režimy určování polohy s asistencí UE (UE-assisted) i založené na UE (UE-based)
- Spolehlivý přenos polohovacích měřicích dat a výsledků výpočtu
- Vyjednávání schopností pro zajištění interoperability mezi síťovými prvky
- Ošetření chyb a procedury přerušení pro robustní provoz

## Související pojmy

- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [E-OTD – Enhanced Observed Time Difference](/mobilnisite/slovnik/e-otd/)
- [LCS – Location Services](/mobilnisite/slovnik/lcs/)

## Definující specifikace

- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.450** (Rel-19) — Iupc Interface Introduction for UTRAN Positioning
- **TS 25.452** (Rel-19) — Iupc Interface Signalling Transport for PCAP
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 37.857** (Rel-13) — Study on Indoor Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [PCAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcap/)
