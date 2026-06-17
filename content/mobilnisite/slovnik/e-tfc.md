---
slug: "e-tfc"
url: "/mobilnisite/slovnik/e-tfc/"
type: "slovnik"
title: "E-TFC – E-DCH Transport Format Combination"
date: 2025-01-01
abbr: "E-TFC"
fullName: "E-DCH Transport Format Combination"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/e-tfc/"
summary: "V UMTS/HSPA definuje konkrétní kombinaci transportních formátů (např. velikost bloku, kódovací poměr), které mohou být použity současně na Enhanced Dedicated Channel (E-DCH) pro uplinkový přenos. UE v"
---

E-TFC je konkrétní kombinace transportních formátů, kterou UE vybírá pro uplinkový přenos na Enhanced Dedicated Channel (E-DCH) na základě grantů od NodeB a své dostupné výkonové rezervy.

## Popis

[E-DCH](/mobilnisite/slovnik/e-dch/) Transport Format Combination (E-TFC) je ústředním konceptem v uplinku High-Speed Packet Access ([HSPA](/mobilnisite/slovnik/hspa/)), konkrétně pro Enhanced Dedicated Channel (E-DCH). Definuje přesnou sadu parametrů pro přenos dat z uživatelského zařízení (UE) do NodeB na [E-DPDCH](/mobilnisite/slovnik/e-dpdch/) (E-DCH Dedicated Physical Data Channel). E-TFC specifikuje kombinaci transportních formátů pro různé logické kanály (MAC-d toky) multiplexované dohromady pro daný Transmission Time Interval (TTI). Každý transportní formát v rámci kombinace definuje atributy pro svůj přidružený MAC-d tok, jako je Transport Block Size (TBS), typ kanálového kódování (Turbo nebo konvoluční) a kódovací poměr. UE udržuje E-TFC Set, což je kolekce všech povolených E-TFC nakonfigurovaných sítí prostřednictvím signalizace Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)). Proces funguje následovně: Entita MAC-e/es v UE přijímá data z vyšších vrstev v bufferu logických kanálů. Musí se rozhodnout, kolik dat odeslat v příštím TTI. Toto rozhodnutí je proces výběru E-TFC. UE bere v úvahu dvě hlavní omezení: Serving Grant (SG) od NodeB, který udává maximální povolený výkonový offset pro E-DPDCH vůči [DPCCH](/mobilnisite/slovnik/dpcch/), a vlastní dostupný vysílací výkon (Power Headroom). Na jejich základě UE vybere E-TFC ze svého povoleného souboru, který maximalizuje přenos dat bez překročení přiděleného výkonového zdroje. Poté multiplexuje odpovídající množství dat z každého logického kanálu podle transportních formátů vybraného E-TFC, sestaví transportní blok(y) a odešle je. NodeB, který zná E-TFC set UE, může přenos dekódovat na základě signalizovaného ukazatele E-TFC ([E-TFCI](/mobilnisite/slovnik/e-tfci/)) na [E-DPCCH](/mobilnisite/slovnik/e-dpcch/). Tento mechanismus umožňuje rychlou adaptaci přenosové rychlosti v uplinku po jednotlivých TTI (2 ms nebo 10 ms), což umožňuje efektivní packet scheduling a řízení interference v buňce.

## K čemu slouží

E-TFC bylo vytvořeno, aby umožnilo rychlý a efektivní packet scheduling v uplinku UMTS, což byla zásadní vylepšení oproti původnímu Release 99 [DCH](/mobilnisite/slovnik/dch/). Pre-HSPA uplink používal pomalé řízení výkonu řízené Radio Network Controllerem (RNC), což bylo neefektivní pro trhavý packetový datový provoz, což vedlo k vysoké latenci a špatnému využití uplinkové kapacity. Účelem E-TFC rámce v architektuře E-DCH (HSUPA) bylo přesunout rozhodování o schedulingu blíže k rádiovému rozhraní – k NodeB – a umožnit UE autonomně vybírat svou datovou rychlost na bázi jednotlivých TTI v rámci síťově definovaných limitů. Tím se vyřešil problém pomalé reakce na měnící se podmínky kanálu a stav bufferu. Mechanismus E-TFC spolu s granty od NodeB (Absolute a Relative Grants) umožňuje velmi rychlou adaptaci spojení, snižuje latenci a zvyšuje špičkové datové rychlosti a celkovou propustnost buňky. Byl motivován potřebou učinit UMTS konkurenceschopné pro symetrické datové aplikace jako je nahrávání videa, online hry a přenos velkých souborů, čímž řešil klíčovou slabost ve srovnání s jinými vyvíjejícími se technologiemi.

## Klíčové vlastnosti

- Definuje velikost transportního bloku a kódovací parametry pro přenos na E-DCH
- UE autonomně vybírá E-TFC na základě grantů od NodeB a dostupného výkonu
- Umožňuje rychlou adaptaci spojení (pro TTI 2 ms) pro packetová data v uplinku
- Podporuje multiplexování více logických kanálů (MAC-d toků) v rámci jednoho TTI
- Řídí se E-TFC Setem nakonfigurovaným prostřednictvím RRC signalizace
- Pro signalizaci vybrané kombinace používá E-TFCI na E-DPCCH

## Související pojmy

- [E-DCH – Enhanced Dedicated Channel](/mobilnisite/slovnik/e-dch/)
- [HSUPA – High Speed Uplink Packet Access](/mobilnisite/slovnik/hsupa/)
- [E-TFCI – E-DCH Transport Format Combination Indicator](/mobilnisite/slovnik/e-tfci/)

## Definující specifikace

- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.309** (Rel-6) — FDD Enhanced Uplink Support
- **TS 25.319** (Rel-19) — Enhanced Uplink for UTRA FDD/TDD
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.700** (Rel-12) — Further Enhanced Uplink (EUL) Study
- **TS 25.874** (Rel-11) — HSPA Feedback & Signalling Efficiency for LCR TDD

---

📖 **Anglický originál a plná specifikace:** [E-TFC na 3GPP Explorer](https://3gpp-explorer.com/glossary/e-tfc/)
