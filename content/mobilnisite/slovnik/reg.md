---
slug: "reg"
url: "/mobilnisite/slovnik/reg/"
type: "slovnik"
title: "REG – Resource Element Group"
date: 2025-01-01
abbr: "REG"
fullName: "Resource Element Group"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/reg/"
summary: "Resource Element Group (REG) je základní jednotkou přidělování zdrojů ve fyzické vrstvě LTE a NR, která se skládá z malé, pevné skupiny resource elementů. Primárně slouží k mapování informací řídicího"
---

REG je základní jednotka přidělování zdrojů v LTE a NR, která se skládá z malé, pevné skupiny resource elementů primárně používané pro mapování informací řídicího kanálu (např. PDCCH) na časově-frekvenční mřížku.

## Popis

Resource Element Group (REG) je základní stavební jednotka v rámci zdrojové mřížky fyzické vrstvy LTE a NR. V časově-frekvenční doméně je zdrojová mřížka rozdělena na resource bloky, z nichž každý se skládá z více resource elementů ([RE](/mobilnisite/slovnik/re/)) – nejmenších jednotek představujících jeden podnosný kmitočet pro jeden [OFDM](/mobilnisite/slovnik/ofdm/) symbol. REG seskupuje specifický počet těchto RE dohromady a vytváří tak logickou jednotku pro mapování řídicích kanálů. V LTE se REG typicky skládá ze 4 po sobě jdoucích RE ve frekvenční doméně v rámci jednoho OFDM symbolu, s výjimkou RE používaných pro referenční signály. Toto seskupení je zásadní pro strukturované přidělování řídicích informací.

V LTE se REG primárně používají pro Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)) a další řídicí kanály, jako je Physical Control Format Indicator Channel ([PCFICH](/mobilnisite/slovnik/pcfich/)) a Physical Hybrid [ARQ](/mobilnisite/slovnik/arq/) Indicator Channel ([PHICH](/mobilnisite/slovnik/phich/)). PDCCH je mapován na Control Channel Elements ([CCE](/mobilnisite/slovnik/cce/)), přičemž každý CCE se skládá ze sady REG (např. v LTE 9 REG na jeden CCE). Tato hierarchická struktura – RE seskupená do REG, která se následně agregují do CCE – umožňuje flexibilní a škálovatelný návrh řídicích kanálů. Mapování REG na fyzické zdroje následuje specifické vzory, aby se zajistila frekvenční diverzita a randomizace interference, což zvyšuje spolehlivost v proměnných rádiových podmínkách.

V NR je koncept REG rozšířen a zpřesněn, aby podporoval flexibilnější numerologie a části šířky pásma. NR REG je definován jako jeden resource blok ve frekvenční doméně a jeden OFDM symbol v časové doméně, obsahuje tedy 12 RE, avšak některé RE jsou vyhrazeny pro demodulační referenční signály ([DM-RS](/mobilnisite/slovnik/dm-rs/)). NR zavádí REG svazky (REG bundles), které sdružují více REG pro konfiguraci sady řídicích zdrojů (CORESET). To umožňuje efektivní beamforming a podporu massive MIMO. Použití REG jak v LTE, tak v NR zajišťuje robustní přenos řídicí signalizace i v náročných prostředích prostřednictvím diverzitních technik a strukturovaného přidělování zdrojů.

## K čemu slouží

Resource Element Group (REG) byl zaveden, aby naplnil potřebu standardizované, jemně strukturované jednotky pro mapování řídicích kanálů ve fyzické vrstvě LTE, počínaje 3GPP Release 8. Před LTE používaly systémy 3G (jako UMTS) pro řídicí signalizaci jiné mechanismy, např. vyhrazené kanály a přidělování založené na kódech, které byly v systémech založených na OFDMA méně efektivní. REG poskytují strukturovaný způsob přidělování řídicích informací v rámci časově-frekvenční mřížky, což umožňuje efektivní využití zdrojů a podporu pokročilých funkcí, jako je frekvenční diverzita a koordinace interference.

REGs řeší problém, jak spolehlivě přenášet řídicí kanály, které nesou kritické informace pro plánování, řízení výkonu a hybridní ARQ, v dynamickém a zdrojově omezeném prostředí. Seskupením RE do REG může systém aplikovat schémata kódování kanálu a modulace přizpůsobená pro řídicí data, což zajišťuje odolnost vůči útlumu a interferenci. To je obzvláště důležité v LTE a NR, kde řídicí kanály musí být dekódovány všemi uživatelskými zařízeními (UE) v buňce, často za proměnných podmínek kanálu.

Vývoj směrem k NR dále využil REG k podpoře flexibilních numerologií a beamformingu, čímž reagoval na požadavky 5G na vyšší přenosové rychlosti a nižší latenci. REG umožňují efektivní mapování řídicích informací jak v LTE, tak v NR, tvoří tak základ spolehlivého provozu sítě a usnadňují funkce jako agregace nosných, massive MIMO a síťové segmenty (network slicing).

## Klíčové vlastnosti

- Pevné seskupení resource elementů (např. 4 RE v LTE, 12 RE v NR) pro mapování řídicích kanálů
- Používají se v PDCCH, PCFICH a PHICH v LTE a v CORESET v NR
- Podporuje frekvenční diverzitu prostřednictvím distribuovaného mapování napříč šířkou pásma
- Umožňuje hierarchickou agregaci do Control Channel Elements (CCE) v LTE
- Napomáhá randomizaci interference a robustnímu přenosu v proměnných rádiových podmínkách
- V NR se rozšiřuje na REG svazky (bundles) pro podporu beamformingu a flexibilních numerologií

## Související pojmy

- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [CORESET – Control Resource Set](/mobilnisite/slovnik/coreset/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.216** (Rel-19) — LTE Relay Node Physical Layer
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [REG na 3GPP Explorer](https://3gpp-explorer.com/glossary/reg/)
