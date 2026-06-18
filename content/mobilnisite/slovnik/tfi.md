---
slug: "tfi"
url: "/mobilnisite/slovnik/tfi/"
type: "slovnik"
title: "TFI – Transport Format Identification"
date: 2025-01-01
abbr: "TFI"
fullName: "Transport Format Identification"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tfi/"
summary: "Parametr v UMTS, který jednoznačně identifikuje kombinaci transportních formátů použitou pro přenos dat po transportním kanálu. Příjemci umožňuje správně dekódovat přijatá data tím, že označuje konkré"
---

TFI je parametr v UMTS, který jednoznačně identifikuje kombinaci transportních formátů použitou pro přenos dat po transportním kanálu, což příjemci umožňuje správně dekódovat přijatá data.

## Popis

Transport Format Identification (TFI) je základní koncept v UMTS Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)), konkrétně v rámci protokolových vrstev Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) a Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)). Působí na úrovni Transportních kanálů, které představují přístupové body služeb nabízené fyzickou vrstvou pro vrstvu 2. Každý Transportní kanál může podporovat více Transportních formátů (TFs), které definují parametry zpracování na fyzické vrstvě pro interval přenosového času ([TTI](/mobilnisite/slovnik/tti/)). Tyto parametry zahrnují velikost transportního bloku, počet transportních bloků, typ kanálového kódování (např. konvoluční, turbo), kódovací poměr a atribut přizpůsobení rychlosti. TFI je označení přiřazené každému platnému Transportnímu formátu pro daný Transportní kanál.

V praxi jsou data přenášena jako Kombinace transportních formátů ([TFC](/mobilnisite/slovnik/tfc/)), což je konkrétní sada Transportních formátů, jeden z každého Transportního kanálu, které jsou společně multiplexovány na jeden Coded Composite Transport Channel (CCTrCH). Odpovídající Ukazatel kombinace transportních formátů ([TFCI](/mobilnisite/slovnik/tfci/)) je parametr skutečně přenášený vzduchem na řídicím kanálu fyzické vrstvy (např. [DPCCH](/mobilnisite/slovnik/dpcch/)). TFCI je odvozen z TFI aktivních transportních kanálů. Příjemce použije dekódovaný TFCI k určení TFI pro každý kanál, což zase říká přijímači na fyzické vrstvě přesně, jak demultiplexovat a dekódovat data na vyhrazeném datovém kanálu fyzické vrstvy ([DPDCH](/mobilnisite/slovnik/dpdch/)).

Role TFI je primárně interní pro Node B a uživatelské zařízení (UE) pro konfiguraci a signalizaci řízení mezi vyššími vrstvami (MAC/RLC) a fyzickou vrstvou. Když vrstva Radio Resource Control (RRC) zřizuje nebo rekonfiguruje rádiový bearer, definuje sadu povolených Transportních formátů a jejich přidružených TFI pro každý zapojený Transportní kanál. Vrstva MAC poté vybere vhodnou TFC (a tím i TFI) na základě dostupných dat a přidělených prostředků a tuto volbu signalizuje fyzické vrstvě prostřednictvím TFCI. Tento mechanismus poskytuje flexibilitu potřebnou pro služby s proměnlivou přenosovou rychlostí, umožňuje dynamické přizpůsobení přenosových parametrů tak, aby odpovídaly okamžité zdrojové rychlosti a rádiovým podmínkám, bez rekonfigurace na vyšší vrstvě.

## K čemu slouží

TFI bylo vytvořeno pro řešení potřeby flexibilního a efektivního přenosu dat přes rádiové rozhraní založené na WCDMA v UMTS, které bylo navrženo pro podporu širokého spektra služeb s velmi rozdílnými požadavky na kvalitu služeb (QoS), od hlasu po vysokorychlostní paketová data. Předchozí systémy jako GSM používaly pevnější struktury kanálů a schémata kódování. Účelem TFI je oddělit zpracování dat na vyšší vrstvě od zpracování na fyzické vrstvě. Poskytuje standardizovanou „smlouvu“ nebo rozhraní mezi vrstvou MAC a fyzickou vrstvou, což vrstvě MAC umožňuje instruovat fyzickou vrstvu, jak přesně zpracovat daný blok dat pro přenos, aniž by musela pro každý přenos přímo specifikovat všechny nízkourovňové parametry.

Tím se řeší problém podpory více simultánních služeb (multimediální hovory) a rychle se měnících datových rychlostí. Bez mechanismu jako TFI/TFCI by síť musela signalizovat kompletní konfigurace fyzické vrstvy pro každý TTI, což by vytvořilo nadměrný řídicí provoz. Místo toho je během sestavování hovoru nakonfigurována předdefinovaná sada Transportních formátů (indexovaných pomocí TFI). Vrstva MAC pak jednoduše vybírá z tohoto předem dohodnutého menu a stručný TFCI informuje příjemce o výběru. To umožňuje rychlé přizpůsobení se dynamice provozu s nízkou režií, což je klíčové pro efektivní využití spektra a podporu pokročilých služeb 3G.

## Klíčové vlastnosti

- Jednoznačně identifikuje Transportní formát v rámci sady Transportního kanálu
- Definuje parametry zpracování na fyzické vrstvě, jako je velikost bloku a schéma kódování
- Používá se interně pro generování přenášeného Ukazatele kombinace transportních formátů (TFCI)
- Umožňuje dynamický výběr přenosových parametrů pro každý Interval přenosového času (TTI)
- Nezbytné pro multiplexování více transportních kanálů na jeden fyzický kanál
- Konfigurováno vrstvou RRC během zřizování a rekonfigurace rádiového beareru

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- **TS 25.425** (Rel-19) — UTRAN Iur Interface User Plane Protocols
- **TS 25.427** (Rel-19) — UTRAN Iub/Iur User Plane Protocols
- **TS 25.435** (Rel-19) — UTRAN Iub Interface User Plane Protocols
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 45.003** (Rel-19) — Channel Coding and Multiplexing for GSM/EDGE
- **TR 45.902** (Rel-19) — Flexible Layer One (FLO) for GERAN

---

📖 **Anglický originál a plná specifikace:** [TFI na 3GPP Explorer](https://3gpp-explorer.com/glossary/tfi/)
