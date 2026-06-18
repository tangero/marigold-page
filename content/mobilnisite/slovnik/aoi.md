---
slug: "aoi"
url: "/mobilnisite/slovnik/aoi/"
type: "slovnik"
title: "AOI – Area of Interest"
date: 2026-01-01
abbr: "AOI"
fullName: "Area of Interest"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/aoi/"
summary: "AOI je koncept správy v sítích 5G, který definuje geografickou nebo logickou oblast, pro kterou se shromažďují a analyzují výkonnostní data. Umožňuje cílené monitorování a optimalizaci síťových zdrojů"
---

AOI je koncept správy v rámci 3GPP, který definuje geografickou nebo logickou oblast, pro kterou se shromažďují a analyzují výkonnostní data za účelem cíleného monitorování a optimalizace sítě.

## Popis

Area of Interest (AOI, oblast zájmu) je základní konstrukt v rámci frameworku správy sítí 5G, konkrétně definovaný v kontextech Management Data Analytics ([MDA](/mobilnisite/slovnik/mda/)) a Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)). Představuje definovanou geografickou oblast (např. buňku, oblast sledování, sadu [GPS](/mobilnisite/slovnik/gps/) souřadnic) nebo logickou doménu (např. konkrétní instanci síťového slicu, skupinu uživatelských zařízení), která je cílem pro sběr dat, analytiku a následné akce správy. AOI funguje jako parametr vymezení rozsahu, který umožňuje funkcím správy sítě zaměřit své procesy sběru informací a rozhodování na relevantní podmnožinu celé síťové infrastruktury.

Z architektonického hlediska je AOI primárně využíváno funkcí NWDAF a systémem správy definovaným v 3GPP TS 28.552. Spotřebitel analytiky, jako je funkce správy síťových slicingů ([NSMF](/mobilnisite/slovnik/nsmf/)) nebo systém provozu, správy a údržby ([OAM](/mobilnisite/slovnik/oam/)), může požadovat analytiku od NWDAF pro konkrétní AOI. Žádost zahrnuje definici AOI, která analytické funkci určuje, odkud má čerpat vstupní data. NWDAF následně shromažďuje relevantní data, jako jsou měření výkonu, informace o zátěži nebo metriky toků kvality služeb (QoS), konkrétně od síťových funkcí a entit uvnitř nebo asociovaných s danou AOI.

Operace zahrnuje několik klíčových komponent. První je samotná definice AOI, kterou lze specifikovat pomocí různých identifikátorů, jako je ID buňky, kód oblasti sledování nebo geografické souřadnice. Druhou je spotřebitel analytiky, který formuluje žádost s parametrem AOI. Třetí je NWDAF, který interpretuje AOI, komunikuje s příslušnými úložišti dat (jako je Network Repository Function ([NRF](/mobilnisite/slovnik/nrf/)) pro zjišťování a další síťové funkce (NFs) pro data) a provádí analýzu. Výstupem je pak přizpůsobená analytická zpráva (např. předpověď zátěže, detekce abnormálního chování, zážitek ze služby) použitelná pouze pro definovanou oblast, což umožňuje přesnou, lokalizovanou optimalizaci a automatizaci sítě.

V širším síťovém ekosystému hraje AOI klíčovou roli při umožnění granulární a efektivní síťové automatizace. Odklonem od celoplošné, plošné analytiky mohou operátoři implementovat cílené politiky, optimalizovat přidělování zdrojů pro zóny s vysokou poptávkou, preventivně řídit zahlcení v konkrétních oblastech a garantovat smlouvy o úrovni služeb ([SLA](/mobilnisite/slovnik/sla/)) pro prémiové služby nebo slicingy na určených místech. Tato granularita je nezbytná pro podporu pokročilých případů užití 5G, jako je tovární automatizace, chytré stadiony a vozidlové sítě, kde jsou požadavky na výkon vysoce lokalizované.

## K čemu slouží

AOI bylo zavedeno, aby řešilo omezení monolitických, celoplošných přístupů k řízení a analytice, které byly pro rozmanité požadavky služeb 5G neefektivní a nepřesné. Předchozí generace se často spoléhaly na široké výkonnostní ukazatele, které mohly maskovat lokalizované problémy nebo příležitosti k optimalizaci. S příchodem 5G a konceptů, jako je síťový slicing, ultra-spolehlivá komunikace s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a masivní IoT, se stala prvořadou potřeba monitorovat a řídit výkon na granulární, kontextově-aware úrovni. AOI poskytuje potřebný mechanismus vymezení rozsahu, jak toho dosáhnout.

Primární problém, který AOI řeší, je neefektivní spotřeba zpracovatelských a signalizačních zdrojů v analytických enginech. Sběr a analýza dat pro celou veřejnou pozemní mobilní síť (PLMN) je výpočetně náročný a často zbytečný, když operátor potřebuje přehledy pouze pro konkrétní průmyslový kampus, hustou městskou buňku nebo instanci konkrétního síťového slicu. AOI umožňuje přesné cílení analytických žádostí, čímž snižuje zatížení NWDAF a objem dat přenášených přes rozhraní správy, což vede k škálovatelnější a responsivnější síťové inteligenci.

Historicky byly akce správy často reaktivní a aplikované plošně. Vytvoření AOI spolu s NWDAF v servisně orientované architektuře 5G bylo motivováno posunem k proaktivní, uzavřené smyčce automatizace a správě založené na záměru. Definováním oblasti zájmu mohou operátoři vyjádřit svůj 'záměr' správy pro konkrétní doménu. To umožňuje automatizovaným systémům tuto oblast kontinuálně monitorovat, aplikovat modely strojového učení k předpovídání trendů nebo anomálií konkrétně v ní a spouštět automatizované nápravné akce (jako škálování zdrojů) pouze tam, kde je to potřeba, čímž se naplňuje vize skutečně samooptimalizující se sítě (SON) pro komplexní nasazení 5G.

## Klíčové vlastnosti

- Umožňuje geograficky nebo logicky vymezený sběr dat pro síťovou analytiku
- Snižuje signalizační a zpracovatelskou režii zaměřením analytiky na relevantní podmnožiny sítě
- Podporuje definici pomocí více identifikátorů (ID buňky, oblast sledování, GPS souřadnice, ID slicu)
- Integruje se s NWDAF pro prediktivní a deskriptivní analytiku v rámci definované oblasti
- Usnadňuje cílené optimalizační a automatizační akce pro konkrétní zóny nebo služby
- Nezbytné pro řízení výkonu a SLA lokalizovaných síťových slicingů a služeb

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)

## Definující specifikace

- **TS 28.552** (Rel-20) — 5G Performance Management Measurements
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3

---

📖 **Anglický originál a plná specifikace:** [AOI na 3GPP Explorer](https://3gpp-explorer.com/glossary/aoi/)
