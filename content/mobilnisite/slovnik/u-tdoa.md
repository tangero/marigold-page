---
slug: "u-tdoa"
url: "/mobilnisite/slovnik/u-tdoa/"
type: "slovnik"
title: "U-TDOA – Uplink Time Difference Of Arrival"
date: 2025-01-01
abbr: "U-TDOA"
fullName: "Uplink Time Difference Of Arrival"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/u-tdoa/"
summary: "Síťová metoda určování polohy, při které se poloha uživatelského zařízení (UE) vypočítává měřením časového rozdílu příchodu jeho rádiových signálů v uplinku na více geograficky rozptýlených přijímacíc"
---

U-TDOA je síťová metoda určování polohy, která lokalizuje zařízení výpočtem časových rozdílů příchodu jeho rádiových signálů v uplinku na více geograficky rozptýlených přijímacích stanicích, aniž by vyžadovala speciální schopnosti v samotném zařízení.

## Popis

Uplink Time Difference of Arrival (U-TDOA) je síťová technologie určování polohy definovaná konsorciem 3GPP pro stanovení geografické polohy uživatelského zařízení (UE). Na rozdíl od metod založených na UE nebo asistovaných UE funguje U-TDOA výhradně na straně sítě. Základní princip spočívá v přesném změření času, kdy známý signál od cílového UE dorazí na více jednotek pro měření polohy ([LMU](/mobilnisite/slovnik/lmu/)), které jsou synchronizovány na společný časový referenční zdroj, často pomocí [GPS](/mobilnisite/slovnik/gps/). LMU jsou typicky umístěny společně s nebo integrovány do lokalit Node B (základnových stanic).

Technický proces začíná, když je vydán požadavek na určení polohy, například klientem lokalizační služby ([LCS](/mobilnisite/slovnik/lcs/)). Síť poté nařídí cílovému UE, aby vyslalo specifický lokalizační signál, například předdefinovanou dávku na vyhrazeném fyzickém kanálu v uplinku. Tento signál detekuje více LMU, minimálně tři nebo čtyři pro 2D určení. Každá LMU zaznamená přesný čas příchodu ([TOA](/mobilnisite/slovnik/toa/)) signálu. Vzhledem k tomu, že LMU jsou časově synchronizovány, lze vypočítat rozdíly těchto časů příchodu (TDOA) vzhledem k referenční LMU.

Naměřené hodnoty TDOA odpovídají hyperbolickým liniím polohy. Průsečík více hyperbol, vypočítaný centrálním uzlem zvaným Serving Mobile Location Centre ([SMLC](/mobilnisite/slovnik/smlc/)) nebo vyhrazeným U-TDOA serverem, poskytne odhadovanou polohu UE. Přesnost U-TDOA závisí na faktorech, jako je geometrie LMU vůči UE (zředění přesnosti), šířka pásma signálu (která ovlivňuje časové rozlišení) a přesnost synchronizace mezi LMU. Klíčovou výhodou je, že funguje s jakýmkoli standardním UE, protože UE pouze vysílá svůj normální nebo síťově nařízený signál v uplinku; zařízení nevyžaduje GPS ani speciální lokalizační hardware.

## K čemu slouží

U-TDOA byla vyvinuta za účelem poskytnutí spolehlivého síťového řešení pro určování polohy, které je nezávislé na schopnostech UE, a to pro splnění regulatorních požadavků, jako je lokalizace volajícího v nouzových případech (E911), a pro umožnění lokalizačních služeb pro všechny účastníky včetně starších koncových zařízení. Předchozí metody často vyžadovaly specifickou podporu na straně UE (např. pro [GPS](/mobilnisite/slovnik/gps/) nebo [OTDOA](/mobilnisite/slovnik/otdoa/) měření), což vytvářelo bariéru pro nasazení. U-TDOA tento problém řeší přesunutím složitosti a nákladů do síťové infrastruktury.

Její vznik byl motivován potřebou metody, která by mohla nabídnout dobrou přesnost, zejména v městském a vnitřním prostředí, kde jsou signály satelitní GPS slabé nebo nedostupné. Využitím vysílání UE v uplinku, které je navrženo tak, aby dosáhlo sítě, může U-TDOA často zachytit signály v podmínkách, kde by metoda OTDOA založená na downlinku mohla selhat. Řešila tak omezení jednodušších metod založených na Cell-ID, které poskytovaly pouze velmi hrubou přesnost polohy. U-TDOA představovala vyvážené řešení, nabízející přesnost v řádu desítek až stovek metrů bez jakékoli úpravy UE, což z ní učinilo klíčový nástroj pro síťové operátory k plnění požadavků nouzových služeb a nasazení komerčních [LBS](/mobilnisite/slovnik/lbs/).

## Klíčové vlastnosti

- Síťové určování polohy nevyžadující úpravy ani speciální schopnosti UE
- Využívá synchronizované jednotky pro měření polohy (LMU) v lokalitách Node B
- Měří časový rozdíl příchodu (TDOA) signálů UE v uplinku
- Vypočítává polohu pomocí hyperbolického průsečíku na centrálním serveru (např. SMLC)
- Poskytuje polohu pro nouzové služby (E911, E112) a komerční LBS
- Výkon je nezávislý na typu nebo modelu UE

## Související pojmy

- [LMU – Location Measurement Unit](/mobilnisite/slovnik/lmu/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)
- [SMLC – Standalone Mobile Location Center](/mobilnisite/slovnik/smlc/)

## Definující specifikace

- **TS 22.071** (Rel-19) — 3GPP TS 22.071: Location Services (LCS) Stage 1
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.111** (Rel-19) — LMU RF Characteristics for UTRA FDD
- **TS 25.305** (Rel-19) — UTRAN UE Positioning Stage 2
- **TS 25.453** (Rel-19) — PCAP Protocol Specification
- **TS 29.171** (Rel-19) — LCS Application Protocol (LCS-AP) Specification
- **TS 43.059** (Rel-19) — GERAN LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [U-TDOA na 3GPP Explorer](https://3gpp-explorer.com/glossary/u-tdoa/)
