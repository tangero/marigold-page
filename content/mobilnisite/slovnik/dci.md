---
slug: "dci"
url: "/mobilnisite/slovnik/dci/"
type: "slovnik"
title: "DCI – Downlink Control Information"
date: 2025-01-01
abbr: "DCI"
fullName: "Downlink Control Information"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dci/"
summary: "DCI je signalizace fyzické vrstvy vysílaná gNB/eNB k UE na kanálu PDCCH. Nese nezbytná plánovací přiřazení, příkazy pro řízení výkonu a konfigurační informace, které umožňují dynamické přidělování zdr"
---

DCI je řídicí informace fyzické vrstvy vysílaná základnovou stanicí k uživatelským zařízením, která nese nezbytná plánovací přiřazení a příkazy pro dynamické přidělování zdrojů v systémech 5G NR a LTE.

## Popis

Downlink Control Information (DCI) je klíčový signalizační mechanismus fyzické vrstvy v 3GPP rádiových přístupových sítích, vysílaný ze základnové stanice (gNB v 5G NR, [eNB](/mobilnisite/slovnik/enb/) v LTE) k uživatelskému zařízení (UE) prostřednictvím fyzického kanálu pro řídicí informace v downlinku ([PDCCH](/mobilnisite/slovnik/pdcch/)). DCI nese nezbytné plánovací a řídicí informace, které umožňují dynamické přidělování zdrojů, adaptaci spoje a efektivní provoz rádiového rozhraní. Obsah a formát zpráv DCI se liší v závislosti na konkrétní přenášené řídicí informaci, přičemž jsou definovány různé formáty DCI pro různé účely, jako jsou plánovací přiřazení pro downlink, plánovací povolení pro uplink, příkazy pro řízení výkonu a indikace formátu časového slotu.

DCI funguje prostřednictvím sofistikovaného procesu vysílání a příjmu. Základnová stanice generuje zprávy DCI na základě plánovacích rozhodnutí, poté je zakóduje a moduluje před mapováním na konkrétní prvky zdrojů v PDCCH. Každá zpráva DCI obsahuje kontrolní součet cyklickou redundancí ([CRC](/mobilnisite/slovnik/crc/)), který je zamíchán pomocí dočasného identifikátoru rádiové sítě ([RNTI](/mobilnisite/slovnik/rnti/)) specifického pro UE nebo skupinu UE. Toto adresování založené na RNTI umožňuje cílené oslovení a zajišťuje, že pouze zamýšlené UE může úspěšně dekódovat DCI. UE provádí tzv. slepé dekódování na více možných kandidátech PDCCH v rámci prohledávacího prostoru, přičemž se pokouší dekódovat zprávy DCI s různými formáty a velikostmi, dokud nenajde takovou, jejíž CRC je platné a odpovídá jejímu přiřazenému RNTI.

Klíčové součásti DCI zahrnují hlavičku pro přidělení zdrojů, indikátor modulačního a kódovacího schématu ([MCS](/mobilnisite/slovnik/mcs/)), verzi redundance, indikátor nových dat, číslo procesu hybridního automatického opakování ([HARQ](/mobilnisite/slovnik/harq/)), příkazy pro řízení vysílacího výkonu ([TPC](/mobilnisite/slovnik/tpc/)) a různé příznaky a indikátory specifické pro formát DCI. V 5G NR bylo DCI rozšířeno o funkce jako indikace části šířky pásma ([BWP](/mobilnisite/slovnik/bwp/)), pole indikátoru nosné (pro agregaci nosných) a podpora plánování přes více nosných. Velikost a obsah formátů DCI jsou pečlivě navrženy tak, aby vyvážily efektivitu režie s potřebou komplexních řídicích informací, přičemž některé formáty mají konfigurovatelnou velikost prostřednictvím signalizace vyšších vrstev.

DCI hraje zásadní roli na rádiovém rozhraní tím, že umožňuje dynamické a efektivní využívání zdrojů. Umožňuje síti rychle se přizpůsobovat měnícím se podmínkám kanálu, požadavkům na přenos dat a schopnostem UE. Prostřednictvím DCI může základnová stanice plánovat přenosy dat v downlinku (přes PDSCH) i v uplinku (přes PUSCH), řídit vysílací výkon UE, indikovat formáty slotů pro systémy s duplexním dělením času (TDD) a spouštět různé procedury fyzické vrstvy. Flexibilita a efektivita DCI přímo ovlivňují výkonnostní metriky systému, jako je propustnost, latence a spektrální účinnost.

## K čemu slouží

DCI bylo vytvořeno, aby řešilo základní potřebu dynamického a efektivního řízení rádiových zdrojů v celulárních sítích. Před LTE používaly starší 3GPP systémy méně flexibilní plánovací mechanismy s vyšší latencí a režií. DCI umožňuje rychlou adaptaci na měnící se rádiové podmínky a charakteristiky provozu prostřednictvím signalizace fyzické vrstvy, která probíhá v každém přenosovém časovém intervalu (TTI), což umožňuje jemně odstupňované přidělování zdrojů maximalizující spektrální účinnost a podporující různé požadavky na kvalitu služeb.

Hlavní problémy, které DCI řeší, zahrnují minimalizaci režie řídicí signalizace při současném poskytování komplexních plánovacích informací, umožnění komunikace s nízkou latencí díky rychlým plánovacím rozhodnutím a podporu pokročilých funkcí, jako je agregace nosných, massive MIMO a komunikace s ultra-spolehlivou nízkou latencí (URLLC). Přesunutím kritických řídicích informací na fyzickou vrstvu a jejich častým vysíláním (v každém slotu nebo podrámci) umožňuje DCI síti rychle reagovat na změny kanálu a kolísání provozu, což je zásadní pro podporu širokopásmových datových služeb s přísnými požadavky na výkon.

Historicky představuje DCI významný vývoj oproti statičtějším metodám přidělování zdrojů používaným v systémech 3G. Jeho zavedení v LTE Release 8 položilo základy pro vysoce dynamické plánování, které je charakteristické pro sítě 4G a 5G. Průběžné vylepšování DCI napříč 3GPP releasy řešilo nově vznikající požadavky, jako je podpora širších šířek pásma, složitějších anténních konfigurací, různých numerologií a nových typů služeb včetně rozšířeného mobilního širokopásmového připojení (eMBB), komunikace pro hromadné strojové připojení (mMTC) a kritických komunikací.

## Klíčové vlastnosti

- Dynamické plánování zdrojů pro downlink i uplink
- Více formátů DCI optimalizovaných pro různé případy užití a přenosové režimy
- Adresování založené na RNTI pro UE-specifickou, skupinovou nebo společnou řídicí informaci
- Podpora agregace nosných prostřednictvím pole indikátoru nosné
- Indikace části šířky pásma pro flexibilní využití spektra
- Schopnosti plánování přes sloty a přes nosné

## Související pojmy

- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.213** (Rel-19) — LTE Physical Layer Procedures
- **TS 36.216** (Rel-19) — LTE Relay Node Physical Layer
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.878** (Rel-13) — LTE Performance Enhancements for High Speed Scenarios
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.174** (Rel-19) — NR Integrated Access and Backhaul Radio Spec
- **TS 38.176** (Rel-19) — IAB Conformance Testing Specification
- **TS 38.211** (Rel-19) — NR Physical Channels and Modulation
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [DCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/dci/)
