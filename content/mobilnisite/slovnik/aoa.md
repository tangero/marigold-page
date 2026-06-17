---
slug: "aoa"
url: "/mobilnisite/slovnik/aoa/"
type: "slovnik"
title: "AOA – Azimuth Angle of Arrival"
date: 2025-01-01
abbr: "AOA"
fullName: "Azimuth Angle of Arrival"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/aoa/"
summary: "AOA je polohovací technika, která odhaduje směr, ze kterého rádiový signál dorazí k anténnímu poli základnové stanice. Používá se pro určení polohy uživatelského zařízení (UE), čímž zlepšuje služby za"
---

AOA je polohovací technika, která odhaduje směr, ze kterého rádiový signál dorazí k anténnímu poli základnové stanice, pro určení polohy uživatelského zařízení (UE).

## Popis

Azimuth Angle of Arrival (AOA) je síťová metoda polohování definovaná ve standardech 3GPP pro určení geografické polohy uživatelského zařízení (UE). Funguje tak, že odhaduje horizontální úhel (azimut), pod kterým rádiový signál vysílaný UE dorazí k přijímací základnové stanici (např. [eNB](/mobilnisite/slovnik/enb/) v LTE nebo gNB v NR). Technika využívá anténní pole na místě základnové stanice, která mohou měřit fázové rozdíly příchozího signálu na více anténních prvcích. Zpracováním těchto fázových rozdílů pomocí algoritmů, jako je Multiple Signal Classification (MUSIC) nebo Estimation of Signal Parameters via Rotational Invariance Techniques (ESPRIT), může síť vypočítat směr k UE vůči hlavnímu směru antény základnové stanice.

Mezi základní architektonické komponenty pro AOA polohování patří UE, obsluhující a sousední základnové stanice vybavené anténními poli a polohový server, jako je Enhanced Serving Mobile Location Center ([E-SMLC](/mobilnisite/slovnik/e-smlc/)) v LTE nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)) v 5G. Polohovací procedura je typicky iniciována sítí. Polohový server vyžádá měřicí data z více základnových stanic. Každá způsobilá základnová stanice změří AOA signálů od cílového UE, často využívajíc vzestupné referenční signály jako Sounding Reference Signal (SRS) v LTE/NR nebo Physical Random Access Channel (PRACH). Tyto úhlové měření jsou pak nahlášeny zpět polohovému serveru.

Pro dvourozměrné určení polohy jsou zapotřebí měření AOA z alespoň dvou geograficky oddělených základnových stanic. Polohový server použije triangulaci nebo jiné geometrické algoritmy k protnutí nahlášených směrových přímek a odhadne polohu UE. Přesnost AOA je ovlivněna faktory, jako je počet anténních prvků, geometrie pole, poměr signálu k šumu (SNR) a vícecestné šíření. V prostředích s bohatým rozptylem mohou vícecestné složky zkreslit měření úhlu přímé cesty a snížit tak přesnost. Pro zmírnění těchto efektů se používají pokročilé zpracování a kalibrace.

V rámci celé sítě slouží AOA jako jedna z několika doplňkových polohovacích metod, mezi které patří také Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)), Uplink Time Difference of Arrival (UTDOA) a Assisted Global Navigation Satellite System ([A-GNSS](/mobilnisite/slovnik/a-gnss/)). Její role je zvláště důležitá ve scénářích, kde nejsou dostupné satelitní signály (např. uvnitř budov nebo v městských kaňonech). AOA poskytuje síťově centrické řešení, které nevyžaduje specifický hardware v UE, což jej činí univerzálně použitelným. Podporuje regulatorní požadavky na lokalizaci nouzových volajících a umožňuje komerční služby založené na poloze.

## K čemu slouží

AOA byla zavedena, aby řešila rostoucí potřebu přesného a spolehlivého polohování mobilních zařízení v rámci buněčných sítí. Před standardizovanými síťovými metodami se polohování často spoléhalo pouze na identitu buňky (Cell-ID), která poskytovala velmi hrubou přesnost polohy omezenou na oblast pokrytí buňky, nebo vyžadovalo UE-bázované [GNSS](/mobilnisite/slovnik/gnss/), které je energeticky náročné a selhává v indoorových prostředích. Primární motivací bylo splnit přísné regulatorní požadavky, jako jsou požadavky Enhanced 911 (E911) ve Spojených státech, které vyžadují, aby operátoři poskytovali záchranným službám polohu volajícího. AOA spolu s dalšími technikami, jako je [OTDOA](/mobilnisite/slovnik/otdoa/), byla vyvinuta, aby splnila tyto zákonné povinnosti bez závislosti pouze na dostupnosti satelitů.

Navíc komercializace služeb založených na poloze ([LBS](/mobilnisite/slovnik/lbs/)) vytvořila silný obchodní důvod pro přesnější polohování. Aplikace jako sledování vozového parku, reklama založená na poloze nebo geografické ohraničení vyžadovaly lepší přesnost, než jakou mohl nabídnout Cell-ID. AOA poskytuje síťově bázované řešení, což znamená, že výpočet polohy provádí síťová infrastruktura. To je výhodné, protože funguje pro jakékoli standardní UE, nevybíjí baterii UE nepřetržitým používáním GNSS a může fungovat v prostředích bez GNSS. Řeší tak problém poskytnutí všudypřítomného určení polohy podporovaného infrastrukturou.

Vytvoření AOA bylo také motivováno pokrokem v technologii antén základnových stanic. Nasazení anténních polí pro Multiple-Input Multiple-Output (MIMO) a beamforming v LTE a 5G poskytlo potřebný fyzický hardware – více koherentních přijímacích prvků – aby bylo možné provádět přesná úhlová měření. Využitím této stávající infrastruktury nabídla AOA cenově efektivní vylepšení polohování. Odstranila omezení předchozích metod určování směru s jednou anténou použitím zpracování signálu z anténního pole ke zlepšení rozlišení a odolnosti proti rušení, čímž se stala životaschopnou součástí hybridního polohovacího řešení v rámci standardů 3GPP.

## Klíčové vlastnosti

- Odhaduje horizontální úhel příchodu signálů z UE pomocí anténních polí základnové stanice
- Umožňuje síťové polohování bez povinných úprav hardwaru UE
- Využívá vzestupné referenční signály (např. SRS, PRACH) pro měření
- Vyžaduje měření z více základnových stanic pro 2D triangulaci polohy
- Integruje se se síťovými polohovacími servery (E-SMLC, LMF) pro výpočet polohy
- Výkon závisí na konfiguraci anténního pole a prostředí s vícecestným šířením

## Související pojmy

- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [E-SMLC – Enhanced Serving Mobile Location Centre](/mobilnisite/slovnik/e-smlc/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)

## Definující specifikace

- **TS 25.865** (Rel-10) — Distributed Antenna Enhancements for TDD
- **TS 32.405** (Rel-19) — UTRAN Performance Measurements Specification
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 38.151** (Rel-19) — NR UE MIMO OTA Performance Requirements
- **TS 38.551** (Rel-18) — User Equipment (UE) Multiple Input Multiple Output (MIMO) Over-the-Air (OTA) performance
- **TS 38.753** (Rel-19) — Spatial Channel Model Study for NR Demodulation
- **TS 38.761** (Rel-19) — MIMO OTA Performance Measurements for UE
- **TS 38.811** (Rel-15) — Study on NR Support for Non-Terrestrial Networks
- **TS 38.827** (Rel-16) — NR MIMO OTA Radiated Metrics & Test Methodology
- **TR 38.858** (Rel-18) — Technical Report on Evolution of NR Duplex Operation
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- **TR 38.901** (Rel-19) — Channel Model for 0.5-100 GHz
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study

---

📖 **Anglický originál a plná specifikace:** [AOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/aoa/)
