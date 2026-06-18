---
slug: "ul-rtoa"
url: "/mobilnisite/slovnik/ul-rtoa/"
type: "slovnik"
title: "UL-RTOA – Uplink Relative Time of Arrival"
date: 2025-01-01
abbr: "UL-RTOA"
fullName: "Uplink Relative Time of Arrival"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ul-rtoa/"
summary: "Síťové měření relativního času příchodu uplink signálu od uživatelského zařízení (UE) na více přijímacích místech. Je to základní metrika pro pozicování metodou rozdílu času příchodu v uplinku (UL-TDO"
---

UL-RTOA je síťové měření relativního času příchodu uplink signálu od uživatelského zařízení (UE) na více přijímacích místech, používané pro pozicování metodou UL-TDOA k výpočtu polohy UE.

## Popis

Uplink Relative Time of Arrival (UL-RTOA) je měření definované pro účely pozicování v sítích 3GPP. Představuje naměřený čas příchodu specifického uplink signálu od cílového uživatelského zařízení (UE) na síťovém přijímacím místě (např. gNB nebo [LMU](/mobilnisite/slovnik/lmu/)), vztažený k internímu časovému referenčnímu signálu tohoto přijímacího místa. Základní princip spočívá v tom, že více geograficky rozptýlených přijímacích míst současně naslouchá známému uplink signálu vysílanému UE, jako je například Sounding Reference Signal ([SRS](/mobilnisite/slovnik/srs/)) nakonfigurovaný pro pozicování. Každé místo zaznamená přesný čas ([RTOA](/mobilnisite/slovnik/rtoa/)), kdy signál dorazí. Protože se signál šíří rychlostí světla, rozdíly v těchto časech příchodu (Time Differences of Arrival - TDOA) odpovídají rozdílům ve vzdálenosti od UE ke každému přijímacímu místu. Síť shromažďuje tato měření UL-RTOA z více míst a předává je pozicovacímu serveru, typicky Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)). LMF následně vypočítá hodnoty TDOA mezi dvojicemi přijímacích míst. Pomocí multilateračních algoritmů LMF určí hyperbolické linie polohy; průsečík těchto hyperbol odhaduje polohu UE. Přesnost UL-RTOA závisí na faktorech, jako je šířka pásma signálu (která ovlivňuje časové rozlišení), přesnost synchronizace mezi síťovými přijímacími místy a geometrie těchto míst vůči UE. Měřicí procedura zahrnuje koordinaci, při které LMF požádá UE o vyslání specifického uplink referenčního signálu pro pozicování a nakonfiguruje příslušné gNB k provedení a hlášení měření UL-RTOA. Tato metoda tvoří základ pro pozicovou techniku Uplink Time Difference of Arrival ([UL-TDOA](/mobilnisite/slovnik/ul-tdoa/)).

## K čemu slouží

UL-RTOA bylo zavedeno, aby poskytlo síťovou, na uplink orientovanou pozicovou metodu, která nezávisí na signálech globálních navigačních satelitních systémů ([GNSS](/mobilnisite/slovnik/gnss/)). To je klíčové pro lokalizaci zařízení v interiérech, městských kaňonech nebo jiných prostředích, kde je pokrytí GNSS slabé nebo nedostupné. Reaguje na potřebu regulatorní compliance (např. lokalizace volajícího v nouzových případech) a podporuje komerční služby založené na poloze. Před jeho standardizací se síťové pozicování často opíralo o downlinkové metody (jako [OTDOA](/mobilnisite/slovnik/otdoa/)) vyžadující měřicí schopnosti UE, nebo o méně přesné techniky typu cell-ID. UL-RTOA umožňuje metodu, kde se výpočetní náročnost a složitost měření primárně nachází v síťové infrastruktuře, což může být výhodné pro IoT zařízení s nízkou složitostí nebo když je baterie nebo výpočetní výkon UE omezený. Jeho vývoj od Rel-13 dále byl hnán rostoucí poptávkou po spolehlivém a přesném pozicování ve všech scénářích nasazení.

## Klíčové vlastnosti

- Měření času příchodu uplink signálu na síťovém přijímacím místě
- Základní prvek pro pozicování metodou rozdílu času příchodu v uplinku (UL-TDOA)
- Měření prováděno na specifických uplink signálech, jako je SRS-for-positioning
- Vyžaduje přesnou synchronizaci mezi síťovými přijímacími místy
- Hlášeno pozicovacímu serveru (LMF) pro výpočet polohy
- Poskytuje síťové řešení, které snižuje složitost na straně UE

## Související pojmy

- [UL-TDOA – Uplink Time Difference of Arrival](/mobilnisite/slovnik/ul-tdoa/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [SRS – Space Radiocommunication Stations](/mobilnisite/slovnik/srs/)

## Definující specifikace

- **TS 37.857** (Rel-13) — Study on Indoor Positioning Enhancements
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.455** (Rel-19) — NR Positioning Protocol A (NRPPa)
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)
- **TR 38.857** (Rel-17) — Study on NR Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [UL-RTOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ul-rtoa/)
