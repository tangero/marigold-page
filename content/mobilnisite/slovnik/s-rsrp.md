---
slug: "s-rsrp"
url: "/mobilnisite/slovnik/s-rsrp/"
type: "slovnik"
title: "S-RSRP – Sidelink Reference Signal Received Power"
date: 2025-01-01
abbr: "S-RSRP"
fullName: "Sidelink Reference Signal Received Power"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/s-rsrp/"
summary: "Měření úrovně přijímaného výkonu referenčních signálů sidelinku v LTE a NR ProSe/V2X. UE jej používá k vyhodnocení kvality a síly přímého rádiového spoje od jiného UE pro komunikaci mezi zařízeními. T"
---

S-RSRP je měření úrovně přijímaného výkonu referenčních signálů sidelinku, které UE používá k vyhodnocení kvality a síly přímého rádiového spoje od jiného UE pro komunikaci mezi zařízeními.

## Popis

Sidelink Reference Signal Received Power (S-RSRP) je měření fyzické vrstvy definované pro komunikaci přes sidelink ([SL](/mobilnisite/slovnik/sl/)) v 3GPP LTE (od Release 12) a NR (od Release 16). Sidelink označuje přímé rozhraní pro komunikaci mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)), známé jako PC5, používané v Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) a Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/)). S-RSRP je protějškem downlinkového měření [RSRP](/mobilnisite/slovnik/rsrp/) pro sidelink. Je definováno jako lineární průměr výkonových příspěvků (ve wattech) zdrojových prvků nesoucích demodulační referenční signály sidelinku ([DM-RS](/mobilnisite/slovnik/dm-rs/)) v rámci určené měřicí šířky pásma a časového trvání.

Měření provádí přijímající UE na DM-RS vysílaných potenciální vysílající UE. Tyto DM-RS jsou vloženy do Physical Sidelink Shared Channel ([PSSCH](/mobilnisite/slovnik/pssch/)) pro data nebo do Physical Sidelink Control Channel ([PSCCH](/mobilnisite/slovnik/pscch/)) pro řídicí informace, v závislosti na konkrétním sidelinkovém přenosu. UE měří výkon těchto referenčních signálů k odhadu útlumu na dráze a kvality kanálu sidelinku. Přesnost S-RSRP je zásadní, protože slouží jako vstup pro algoritmy vyšších vrstev pro správu prostředků. UE typicky hlásí naměřené hodnoty S-RSRP svému protokolovému zásobníku, který je používá pro kritéria jako je spuštění hlášení měření pro síť (v režimech plánovaných sítí) nebo pro autonomní rozhodnutí (v režimech autonomního výběru prostředků UE).

Z architektonického hlediska je měření S-RSRP funkcí fyzické vrstvy UE. Postup zahrnuje synchronizaci UE na sidelinkové synchronizační signály (S-SS), identifikaci pozic DM-RS v přijatých sidelinkových podrámcích a provedení průměrování výkonu. Konkrétní prostředky k měření jsou konfigurovány vyššími vrstvami prostřednictvím signalizace RRC (v režimu 1 nebo 3) nebo jsou určeny předkonfigurovanými parametry (v režimu 2 nebo 4). S-RSRP je klíčovým vstupem pro proceduru Sidelink Radio Link Monitoring (S-RLM), kde UE monitoruje kvalitu navázaného sidelinku pro detekci selhání rádiového spoje. Hraje také ústřední roli v algoritmu sense-based semi-persistent scheduling (SPS) používaném v LTE V2X režimu 4, kde UE snímají kanál a měří S-RSRP rezervací od jiných UE, aby vybraly prostředky, které jsou pravděpodobně volné a mají přijatelnou úroveň interference.

V NR Sidelink (zavedeném v Release 16) je koncept S-RSRP rozšířen a upřesněn. NR podporuje flexibilnější struktury referenčních signálů a širší šířky pásma. Měření S-RSRP v NR lze provádět na různých typech referenčních signálů, jako jsou Phase-Tracking Reference Signals (PT-RS) kromě DM-RS, a napříč aktivovaným šířkovým pásmem (BWP) pro sidelink. Měření je klíčové pro pokročilé funkce NR-V2X, jako je víceanténní přenos, správa beamů pro sidelink a vylepšená schémata přidělování prostředků. UE používá S-RSRP k výběru nejlepšího beam pair linku v beamformingových sidelinkových operacích a k napomáhání mechanismům řízení výkonu, čímž zajišťuje spolehlivou přímou komunikaci při minimalizaci interference vůči jiným sidelinkovým uživatelům.

## K čemu slouží

S-RSRP bylo zavedeno v 3GPP Release 12 pro podporu nové funkce LTE Direct (D2D), známé jako Proximity Services (ProSe). Základní problém, který řeší, je potřeba standardizované, spolehlivé metody, aby UE mohlo měřit sílu signálu a kvalitu přímého rádiového spoje od jiného UE. Před sidelinkem byla buněčná měření jako RSRP definována pouze pro rozhraní Uu (UE-síť). Pro přímou komunikaci potřebují UE podobnou metriku k posouzení životaschopnosti spoje, provedení přechodu mezi přímou a infrastrukturní cestou a ke správě interference. S-RSRP poskytuje toto zásadní měření fyzické vrstvy, které umožňuje UE a síti činit informovaná rozhodnutí o sidelinkové komunikaci.

Primární motivací bylo umožnit služby objevování a komunikace pro veřejnou bezpečnost a komerční ProSe. Uživatelé veřejné bezpečnosti často operují v oblastech bez pokrytí sítě, což vyžaduje přímou komunikaci UE-UE. S-RSRP umožňuje UE vyhodnotit blízkost a podmínky kanálu jiných objevených UE, což je klíčové pro rozhodnutí, zda navázat přímý spoj. Podporuje také síťově řízený provoz, kdy eNB používá S-RSRP měření hlášená UE ke správě fondů prostředků sidelinku, provedení výběru režimu (zda komunikovat přes síť nebo přímo) a ke správě interference mezi buněčnými a sidelinkovými přenosy.

S rozšířením na V2X v Release 14 a 15 se role S-RSRP stala ještě kritičtější. Pro autonomní výběr prostředků (LTE Režim 4) musí UE snímat kanál, aby vybrala přenosové prostředky. Dekódují řídicí informace (SA) od jiných vozidel a měří S-RSRP přidružených DM-RS. Pokud je naměřené S-RSRP nad určitým prahem, je prostředek považován za rezervovaný a pravděpodobně zažívající vysokou interferenci, takže snímací UE jej vyloučí z vlastní sady kandidátních prostředků. Tento mechanismus vyhýbání se interferenci je základním kamenem distribuovaného plánování ve V2X a plně závisí na přesných měřeních S-RSRP. S-RSRP se tedy vyvinulo z jednoduchého indikátoru kvality spoje v klíčový prvek umožňující distribuovanou, spolehlivou a nízkolatencovou přímou komunikaci pro bezpečnostně kritické automobilové aplikace.

## Klíčové vlastnosti

- Měří přijímaný výkon Sidelink Demodulation Reference Signals (DM-RS) na rozhraní PC5.
- Slouží jako primární metrika fyzické vrstvy pro kvalitu kanálu sidelinku a odhad útlumu na dráze.
- Používá se jako vstup pro algoritmy výběru prostředků sidelinku, zejména v autonomních (sense-based) režimech.
- Podporuje Sidelink Radio Link Monitoring (S-RLM) pro detekci selhání sidelinkového rádiového spoje.
- Konfigurovatelné signalizací RRC v síťově plánovaných režimech nebo na základě předkonfigurace v autonomních režimech.
- Rozšířené v NR Sidelink pro podporu správy beamů a měření na širších šířkových pásmech (BWP).

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [DM-RS – Demodulation Reference Signal](/mobilnisite/slovnik/dm-rs/)

## Definující specifikace

- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [S-RSRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-rsrp/)
