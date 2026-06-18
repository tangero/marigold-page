---
slug: "ul-rscp"
url: "/mobilnisite/slovnik/ul-rscp/"
type: "slovnik"
title: "UL-RSCP – Uplink Reference Signal Carrier Phase"
date: 2025-01-01
abbr: "UL-RSCP"
fullName: "Uplink Reference Signal Carrier Phase"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ul-rscp/"
summary: "Měření fáze nosné vlny uplink referenčních signálů přijímaných na základnové stanici. Používá se pro techniky vysoce přesného určování polohy, umožňující přesný odhad lokalizace UE analýzou fázových r"
---

UL-RSCP je měření fáze nosné vlny uplink referenčních signálů na základnové stanici, používané pro vysoce přesné určování polohy UE analýzou fázových rozdílů přijímaného signálu.

## Popis

Uplink Reference Signal Carrier Phase (UL-RSCP) je měření prováděné sítí, konkrétně jednou nebo více základnovými stanicemi (gNB) nebo jednotkami pro měření polohy ([LMU](/mobilnisite/slovnik/lmu/)), na uplink referenčních signálech vysílaných uživatelským zařízením (UE). Kvantifikuje fázi přijímaného nosného signálu, což je klíčový parametr pro metody určování polohy založené na fázi nosné vlny. Měření funguje tak, že UE vysílá známý uplink referenční signál, například Sounding Reference Signal ([SRS](/mobilnisite/slovnik/srs/)) nakonfigurovaný pro určování polohy. Tento signál následně zachytí více geograficky rozmístěných síťových přijímacích bodů. Každý přijímač změří absolutní fázi nosné vlny příchozího signálu na své anténě. Protože vysílaný signál má známou frekvenci, naměřená fáze v každém bodě přímo souvisí s délkou přenosové dráhy (dosahu) mezi UE a tímto přijímačem, modulo vlnová délka nosné vlny. Klíčem k určování polohy je analýza fázových rozdílů mezi signály přijímanými na různých místech nebo změny fáze v čase na jednom místě. Pro převod těchto fázových měření na přesné odhady vzdálenosti se používají sofistikované algoritmy, často zahrnující rozlišení nejednoznačnosti (určení celočíselného počtu vlnových délek na dráze). Tyto odhady vzdálenosti jsou následně kombinovány pomocí technik multilaterace pro výpočet polohy UE. Architektura zahrnuje koordinaci mezi UE, obsluhující gNB a potenciálně více sousedními gNB nebo LMU, řízenou polohovými servery jako je Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)). Měření UL-RSCP je typicky hlášeno s vysokým rozlišením a používá se ve spojení s dalšími měřeními (např. [UL-RTOA](/mobilnisite/slovnik/ul-rtoa/)) k dosažení přesnosti na úrovni centimetrů v podporovaných scénářích.

## K čemu slouží

UL-RSCP bylo zavedeno, aby splnilo náročné požadavky na přesnost pro nové vertikální aplikace a regulační povinnosti, jako je enhanced 911 (E911) Phase 2 a komerční služby jako sledování majetku, navigace dronů a rozšířená realita. Tradiční metody určování polohy jako Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) nebo Assisted [GNSS](/mobilnisite/slovnik/gnss/) ([A-GNSS](/mobilnisite/slovnik/a-gnss/)) mohou mít potíže v náročných rádiových prostředích, jako jsou hluboké vnitřní prostory nebo městské kaňony. Určování polohy pomocí fáze nosné vlny, technika dlouho používaná ve vysoce přesných GNSS systémech, nabízí významný skok v přesnosti využitím fáze signálu, která poskytuje mnohem jemnější granularitu měření ve srovnání s metodami založenými na čase. UL-RSCP umožňuje tuto techniku pro mobilní sítě a řeší tak omezení předchozího uplink určování polohy, které primárně spoléhalo na měření času příchodu s nižší přesností. Jeho vytvoření v Rel-18 bylo motivováno potřebou síťových řešení pro určování polohy, která nejsou závislá na dostupnosti GNSS a mohou poskytovat kontinuální, spolehlivé a vysoce přesné polohové informace.

## Klíčové vlastnosti

- Měření fáze nosné vlny přijímaných uplink referenčních signálů
- Umožňuje určování polohy založené na fázi nosné vlny pro vysokou přesnost
- Prováděno více gNB nebo LMU na signálech jako SRS-for-positioning
- Poskytuje měření s velmi vysokým rozlišením pro přesný odhad vzdálenosti
- Vyžaduje algoritmy pro rozlišení nejednoznačnosti k určení celočíselných cyklů vlnové délky
- Používá se ve spojení s dalšími měřeními (např. UL-RTOA) pro robustní určování polohy

## Související pojmy

- [UL-RTOA – Uplink Relative Time of Arrival](/mobilnisite/slovnik/ul-rtoa/)
- [SRS – Space Radiocommunication Stations](/mobilnisite/slovnik/srs/)

## Definující specifikace

- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.455** (Rel-19) — NR Positioning Protocol A (NRPPa)
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [UL-RSCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ul-rscp/)
