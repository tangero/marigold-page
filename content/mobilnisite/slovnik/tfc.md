---
slug: "tfc"
url: "/mobilnisite/slovnik/tfc/"
type: "slovnik"
title: "TFC – Transport Format Combination"
date: 2025-01-01
abbr: "TFC"
fullName: "Transport Format Combination"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tfc/"
summary: "Konkrétní povolená sada transportních formátů (TF), které lze současně použít na různých transportních kanálech jednoho uživatelského zařízení (UE) v UMTS. Definuje kódování, modulaci a přidělení zdro"
---

TFC je konkrétní povolená sada transportních formátů, které lze současně použít na různých transportních kanálech jednoho uživatelského zařízení (UE) v UMTS, a definuje parametry fyzické vrstvy pro přenos.

## Popis

Transport Format Combination (TFC) je klíčový koncept v rádiovém rozhraní UMTS ([WCDMA](/mobilnisite/slovnik/wcdma/)), který definuje okamžitou konfiguraci fyzické vrstvy pro přenos a příjem dat. V UMTS může mít uživatelské zařízení (UE) více paralelních transportních kanálů (TrCH), například vyhrazený kanál ([DCH](/mobilnisite/slovnik/dch/)) pro uživatelská data a vyhrazený řídicí kanál ([DCCH](/mobilnisite/slovnik/dcch/)) pro signalizaci. Každý transportní kanál má sadu možných transportních formátů ([TF](/mobilnisite/slovnik/tf/)), které specifikují atributy jako velikost transportního bloku, velikost sady transportních bloků a přenosový časový interval ([TTI](/mobilnisite/slovnik/tti/)). TFC je platná kombinace jednoho konkrétního transportního formátu z každého aktivního transportního kanálu, vybraná pro použití v daném TTI.

Z architektonického hlediska je výběr TFC dynamický proces prováděný vrstvou řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)), konkrétně entitou MAC-d v UE pro uplink a MAC vrstvou v Node B pro downlink. Sada všech povolených TFC pro dané UE je konfigurována vrstvou řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) prostřednictvím RRC signalizace a je známá jako Transport Format Combination Set ([TFCS](/mobilnisite/slovnik/tfcs/)). Úlohou MAC vrstvy je vybrat pro každý TTI z této sady nejvhodnější TFC na základě faktorů, jako je množství dat k odeslání (z logických kanálů), dostupný vysílací výkon a možnosti UE. Tento výběr přímo určuje okamžitou přenosovou rychlost a multiplexování různých datových toků na kódovaný složený transportní kanál (CCTrCH).

Proces funguje následovně: RRC nakonfiguruje TFCS, čímž definuje přípustné kombinace. Během provozu MAC vrstva vyhodnocuje své vyrovnávací paměti. Pro uplink MAC v UE vybere TFC, které dokáže přenést čekající data z jeho logických kanálů, aniž by překročilo maximální povolený uplinkový vysílací výkon, který je řízen sítí. Zvolený TFC určuje velikosti bloků a kódování pro každý TrCH. Tyto bloky jsou následně multiplexovány, prokládány a rozprostřeny podle parametrů TFC před vysíláním. V downlinku plánovač Node B provádí podobný výběr a rozhoduje o TFC na základě dostupného výkonu, stavu kanálu a požadavků QoS rádiových přenosů UE.

TFC je vnitřně propojeno s QoS. Každý rádiový přenos je mapován na transportní kanál s konkrétními TF. Výběrem různých TFC může síť upřednostňovat provoz, garantovat přenosové rychlosti a efektivně spravovat rádiové zdroje. Tento koncept zajišťuje, že složitý vícekanálový přenos v UMTS je řízen koordinovaným a standardizovaným způsobem, což umožňuje flexibilní a efektivní využití rozhraní WCDMA. Je základním prvkem mechanismů přizpůsobení rychlosti a přidělování zdrojů fyzické vrstvy v UMTS.

## K čemu slouží

Mechanismus TFC byl vytvořen k řešení základního problému flexibilní a současné podpory více služeb na širokopásmovém CDMA rozhraní UMTS. Na rozdíl od GSM, které používalo relativně pevné časové sloty, UMTS potřebovalo dynamicky podporovat více datových toků (např. hlas, video, prohlížení webu) s velmi odlišnými požadavky QoS (přenosová rychlost, zpoždění, chybovost) v rámci jednoho připojení uživatele. TFC poskytuje potřebnou detailní kontrolu pro efektivní správu tohoto multiplexování.

Bez takového strukturovaného přístupu by řízení služeb s proměnnou rychlostí v CDMA systému bylo nahodilé a neefektivní. Koncept TFC umožňuje síti předem definovat sadu platných konfigurací fyzické vrstvy (TFCS) přizpůsobených službám, k nimž je uživatel přihlášen. To umožňuje rychlou adaptaci přenosové rychlosti a kódování po snímcích bez nutnosti nepřetržité signalizace na vysokých vrstvách. Přímo řeší potřebu efektivního statistického multiplexování různých typů provozu na sdílenou kódovou doménu WCDMA.

Historicky bylo jeho zavedení s UMTS Release 99 klíčovou inovací, která umožnila skutečná vysokorychlostní paketová data vedle přepojování okruhů hlasu na stejném nosiči. Poskytlo nezbytný rámec pro adaptaci spoje k maximalizaci spektrální účinnosti a propustnosti uživatele. Algoritmus výběru TFC, který zohledňuje výkon a dostupnost dat, je ústřední pro řízení výkonu a správu zahlcení v UMTS. Vyřešil výzvu, jak dát UE autonomii při výběru své uplinkové rychlosti v rámci omezení definovaných sítí, což je efektivnější než to, aby Node B mikromanagementem řídil každý přenosový parametr pro každého uživatele v každém časovém intervalu.

## Klíčové vlastnosti

- Definuje platnou kombinaci transportních formátů pro více paralelních transportních kanálů
- Dynamicky vybíráno MAC vrstvou pro každý TTI zvlášť
- Řídí okamžitou přenosovou rychlost, kódování a využití fyzických zdrojů
- Konfigurováno RRC v rámci sady kombinací transportních formátů (TFCS)
- Nedílná součást procedur řízení výkonu uplinku a přizpůsobení rychlosti
- Přímo vynucuje QoS mapováním požadavků rádiových přenosů na parametry fyzické vrstvy

## Související pojmy

- [TFCS – Transport Format Combination Set](/mobilnisite/slovnik/tfcs/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)
- [TTI – Transmission Timing Interval](/mobilnisite/slovnik/tti/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TS 25.823** (Rel-8) — Synchronised E-DCH Study for UTRA FDD
- **TR 25.903** (Rel-19) — Continuous Connectivity for Packet Data Users
- **TR 25.927** (Rel-14) — Energy Saving Solutions for UMTS Node B
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 43.129** (Rel-19) — PS Handover in GERAN A/Gb and GAN Modes
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [TFC na 3GPP Explorer](https://3gpp-explorer.com/glossary/tfc/)
