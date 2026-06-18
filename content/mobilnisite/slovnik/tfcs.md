---
slug: "tfcs"
url: "/mobilnisite/slovnik/tfcs/"
type: "slovnik"
title: "TFCS – Transport Format Combination Set"
date: 2025-01-01
abbr: "TFCS"
fullName: "Transport Format Combination Set"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tfcs/"
summary: "Množina všech platných kombinací transportních formátů (TFCs), které může uživatelské zařízení (UE) použít na daném kódovaném složeném transportním kanálu (CCTrCH). Je konfigurována vrstvou RRC a defi"
---

TFCS je množina všech platných kombinací transportních formátů (Transport Format Combinations), které může uživatelské zařízení (UE) použít na daném kódovaném složeném transportním kanálu (CCTrCH), jak je nakonfigurováno vrstvou RRC pro definování přípustných konfigurací multiplexování a kódování.

## Popis

Množina kombinací transportních formátů (TFCS) je klíčovým konfiguračním prvkem v protokolové architektuře rádiového rozhraní UMTS, konkrétně ve vrstvách řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)) a fyzické vrstvě. Jedná se o konečný, uspořádaný seznam kombinací transportních formátů (TFCs), které jsou povoleny pro použití uživatelským zařízením (UE) na konkrétním kódovaném složeném transportním kanálu (CCTrCH). CCTrCH je entita fyzické vrstvy, která vzniká multiplexováním jednoho nebo více transportních kanálů (TrCHs). Každý transportní kanál má svou vlastní množinu možných transportních formátů (TFs), které definují parametry jako velikost transportního bloku, počet bloků na rámec a kódovací schéma. [TFC](/mobilnisite/slovnik/tfc/) je konkrétní platný výběr jednoho [TF](/mobilnisite/slovnik/tf/) z každého z transportních kanálů uvnitř CCTrCH.

TFCS je konfigurována a poskytnuta uživatelskému zařízení (UE) vrstvou řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) během zřizování nebo rekonfigurace rádiového přenosového kanálu prostřednictvím signalizačních zpráv RRC. Konfigurace zahrnuje kompletní seznam povolených TFCs. Vrstva MAC je zodpovědná za výběr nejvhodnějšího TFC z této množiny pro každý přenosový časový interval ([TTI](/mobilnisite/slovnik/tti/), typicky 10, 20, 40 nebo 80 ms) na základě dostupných dat v bufferech různých logických kanálů a jejich priorit. Tento výběrový proces je řízen algoritmy pro výběr TFC, jejichž cílem je maximalizovat přenos dat při respektování výkonových možností UE a zdrojů přidělených sítí.

Jakmile MAC vybere TFC, dá pokyn fyzické vrstvě, aby jej použila. Fyzická vrstva poté použije odpovídající indikátor kombinace transportních formátů ([TFCI](/mobilnisite/slovnik/tfci/)) k signalizaci, *který* TFC z předem definované TFCS je používán v aktuálním rádiovém rámci. Příjemce, který byl nakonfigurován se stejnou TFCS, použije přijatý TFCI k indexování do své lokální kopie TFCS a získání přesného TFC. To mu umožní data správně dekódovat. TFCS tedy funguje jako sdílený kódový slovník mezi vysílačem a přijímačem, což umožňuje efektivní dynamickou adaptaci přenosové rychlosti bez nutnosti signalizovat všechny podrobnosti formátu v každém rámci. Velikost a složení TFCS přímo určují flexibilitu a granularitu adaptace přenosové rychlosti dostupné pro rádiový přenosový kanál.

## K čemu slouží

TFCS byla vytvořena, aby poskytla strukturovaný a efektivní rámec pro správu komplexní, vícerozměrné adaptace přenosové rychlosti vyžadované v UMTS. [WCDMA](/mobilnisite/slovnik/wcdma/) podporuje simultánní přenos více služeb (např. hlas, videotelefonie, paketová data) přes jediné rádiové spojení, z nichž každá má různé a proměnlivé požadavky na šířku pásma. Tyto služby jsou mapovány na samostatné transportní kanály. Síť potřebuje řídit možné kombinace datových rychlostí na těchto kanálech, aby zajistila efektivní využití rádiového spektra, udržela QoS a kontrolovala rušení.

Bez předem definované množiny, jako je TFCS, by si uživatelské zařízení (UE) a Node B musely vyjednávat nebo signalizovat kompletní podrobnosti formátu pro každou možnou kombinaci v reálném čase, což by vedlo k nadměrné signalizační režii a latenci. TFCS tento problém řeší předkonfigurováním všech platných provozních bodů během zřizování spojení. To umožňuje velmi rychlou (na [TTI](/mobilnisite/slovnik/tti/)) adaptaci s minimální signalizací (pouze index TFCI). Poskytuje síti přesnou kontrolu nad přenosovými schopnostmi UE a zabraňuje jí v používání neautorizovaných nebo neefektivních kombinací formátů, které by mohly degradovat výkon sítě nebo porušit přidělené zdroje. TFCS je klíčovým prvkem umožňujícím sofistikované řízení QoS a efektivní multiplexování, které odlišuje UMTS od předchozích systémů 2G.

## Klíčové vlastnosti

- Definuje všechny přípustné kombinace transportních formátů (TFCs) pro CCTrCH
- Konfigurována vrstvou RRC prostřednictvím síťové signalizace
- Poskytuje sdílený kódový slovník, na který odkazuje TFCI pro dekódování rámců
- Umožňuje síťovou kontrolu nad přenosovými schopnostmi UE a QoS
- Řídí algoritmus pro výběr TFC ve vrstvě MAC
- Určuje dynamický rozsah a granularitu adaptace přenosové rychlosti

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol
- **TR 25.931** (Rel-19) — UTRAN Signalling Procedures Examples
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TR 45.902** (Rel-19) — Flexible Layer One (FLO) for GERAN

---

📖 **Anglický originál a plná specifikace:** [TFCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tfcs/)
