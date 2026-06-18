---
slug: "wgs-84"
url: "/mobilnisite/slovnik/wgs-84/"
type: "slovnik"
title: "WGS-84 – World Geodetic System 1984"
date: 2025-01-01
abbr: "WGS-84"
fullName: "World Geodetic System 1984"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/wgs-84/"
summary: "Globální geodetický souřadnicový systém používaný jako standardní reference pro služby založené na poloze v sítích 3GPP. Poskytuje konzistentní, pevný zemský souřadnicový rámec pro určování polohy uži"
---

WGS-84 je standardizovaný globální geodetický souřadnicový systém, který poskytuje pevný zemský referenční rámec pro všechny služby založené na poloze a pro určování polohy v sítích 3GPP.

## Popis

World Geodetic System 1984 (WGS-84) je standardizovaný globální referenční systém pro geografické informace, který definuje konzistentní souřadnicový rámec, referenční elipsoid a geoid pro Zemi. Ve standardech 3GPP slouží WGS-84 jako základní geodetický datum pro všechny služby založené na poloze ([LBS](/mobilnisite/slovnik/lbs/)) a funkce určování polohy. Poskytuje trojrozměrný kartézský souřadnicový systém (X, Y, Z) a přidruženou elipsoidní reprezentaci (zeměpisná šířka, délka, nadmořská výška), která je pevně spojena se Zemí, což znamená, že se otáčí s planetou a nabízí tak stabilní referenci pro absolutní určování polohy. Tento systém je klíčový pro převod surových měření polohy, například z globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)) jako [GPS](/mobilnisite/slovnik/gps/), Galileo nebo BeiDou, na univerzálně srozumitelnou polohu, kterou lze použít napříč síťovými prvky a aplikacemi.

Z architektonického hlediska je WGS-84 integrován do různých komponent sítě 3GPP zapojených do určování polohy. Souřadnice WGS-84 využívají uživatelské zařízení (UE), rádiová přístupová síť (RAN) a entity jádra sítě, jako je Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5G nebo Enhanced Serving Mobile Location Centre ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE. Když je iniciován požadavek na určení polohy, UE nebo síť vypočítá polohu zařízení pomocí metod jako Assisted GNSS ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) nebo Enhanced Cell ID ([E-CID](/mobilnisite/slovnik/e-cid/)). Tyto metody produkují měření, která jsou nakonec převedena na souřadnice WGS-84. Například v A-GNSS přijímá UE pomocná data ze sítě pro rychlé zachycení satelitních signálů, vypočítá svou polohu a nahlásí ji ve formátu WGS-84 do jádra sítě pro další zpracování nebo doručení externímu klientovi.

Mezi klíčové komponenty v architektuře 3GPP, které využívají WGS-84, patří pozicovací protokoly a rozhraní definované v technických specifikacích. Specifikace jako TS 25.331 (UTRAN RRC), TS 36.305 (LTE positioning) a TS 38.305 (NR positioning) podrobně popisují, jak jsou souřadnice WGS-84 kódovány, přenášeny a používány v signalizačních zprávách. Role systému sahá za pouhé hlášení souřadnic; umožňuje pokročilé služby jako geofencing, směrování na základě polohy a zákonný odposlech. Poskytnutím jediné, jednoznačné reference WGS-84 eliminuje nesrovnalosti, které by mohly vzniknout používáním různých lokálních dat, a zajišťuje, že poloha nahlášená v jedné části světa je správně interpretována v jiné, což je zásadní pro globální roaming a nouzové služby jako E911 ve Spojených státech nebo eCall v Evropě.

## K čemu slouží

WGS-84 byl přijat 3GPP, aby vyřešil kritický problém nekonzistentních a nekompatibilních geografických referenčních systémů v různých regionech a technologiích. Před jeho standardizací se používala různá národní nebo regionální geodetická data (např. NAD83 v Severní Americe, ED50 v Evropě), což vedlo k potenciálním chybám v hlášení polohy, když se zařízení pohybovala přes hranice nebo když sítě vzájemně spolupracovaly. Tato nekonzistence představovala významná rizika pro nouzové služby, kde přesná poloha může být otázkou života a smrti, a pro komerční služby založené na poloze, které vyžadují spolehlivé určování polohy pro funkčnost a uživatelský zážitek.

Vytvoření WGS-84 jako globálního standardu bylo motivováno potřebou jednotného, přesného a stabilního referenčního rámce, který by mohl podpořit rostoucí poptávku po mobilních lokalizačních službách. Jak se mobilní sítě vyvíjely, aby nabízely více než jen hlasové hovory – začleňovaly datové služby, navigaci a IoT aplikace – společný geodetický systém se stal nezbytným. WGS-84, původně vyvinutý Ministerstvem obrany USA pro GPS, nabídl dobře definovaný, globálně přijímaný model s vysokou přesností, což z něj učinilo ideální volbu pro 3GPP. Jeho přijetí zajišťuje, že pozicovací technologie v systémech 3GPP, od 3G UMTS po 5G NR, mohou bezproblémově integrovat se satelitními systémy a poskytovat konzistentní polohová data bez ohledu na podkladovou technologii rádiového přístupu.

WGS-84 navíc řeší omezení dřívějších přístupů tím, že poskytuje trojrozměrný, geocentrický rámec, který zohledňuje tvar geoidu planety, čímž zlepšuje přesnost oproti plochým nebo lokálním modelům. To je obzvláště důležité pro pokročilé případy užití, jako je sledování dronů, autonomní vozidla a precizní zemědělství v 5G, kde je nadmořská výška a přesná horizontální poloha klíčová. Zavedením WGS-84 do svých specifikací umožňuje 3GPP interoperabilitu nejen v rámci vlastního ekosystému, ale také s externími systémy, jako jsou mapové služby, sítě pro reakci na mimořádné události a globální logistické platformy, čímž podporuje soudržnou digitální infrastrukturu s povědomím o poloze.

## Klíčové vlastnosti

- Pevný zemský, trojrozměrný kartézský souřadnicový systém (X, Y, Z)
- Elipsoidní geografické souřadnice (zeměpisná šířka, délka, nadmořská výška) založené na definovaném referenčním elipsoidu
- Globální standardizace zajišťuje interoperabilitu napříč všemi releasy a technologiemi 3GPP
- Vysoká přesnost a stabilita, podpora přesného určování polohy pro nouzové a komerční služby
- Integrace s více metodami určování polohy (např. A-GNSS, OTDOA, E-CID) v RAN a jádru sítě
- Zakódováno v signalizačních protokolech 3GPP pro spolehlivý přenos mezi UE a sítí

## Související pojmy

- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [E-CID – Enhanced Cell-ID](/mobilnisite/slovnik/e-cid/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 44.031** (Rel-19) — Radio Resource LCS Protocol (RRLP)

---

📖 **Anglický originál a plná specifikace:** [WGS-84 na 3GPP Explorer](https://3gpp-explorer.com/glossary/wgs-84/)
