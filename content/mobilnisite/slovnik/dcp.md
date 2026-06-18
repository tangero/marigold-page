---
slug: "dcp"
url: "/mobilnisite/slovnik/dcp/"
type: "slovnik"
title: "DCP – Downlink Control Information with CRC scrambled by PS-RNTI"
date: 2025-01-01
abbr: "DCP"
fullName: "Downlink Control Information with CRC scrambled by PS-RNTI"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dcp/"
summary: "Specifický typ informace řídicího kanálu pro downlink (DCI) používaný v NR k plánování stránkovacích zpráv. Její CRC je zamaskováno pomocí stránkovacího RNTI (PS-RNTI), což umožňuje UE ve stavech RRC_"
---

DCP je typ informace řídicího kanálu pro downlink (Downlink Control Information) v NR, která plánuje stránkovací zprávy. Je identifikována tím, že její CRC je zamaskováno (scrambled) pomocí PS-RNTI, což umožňuje UE v režimu idle nebo inactive efektivně monitorovat stránkování.

## Popis

DCP je klíčový signalizační mechanismus na fyzické vrstvě v 3GPP New Radio (NR). Odkazuje na formát informace řídicího kanálu pro downlink ([DCI](/mobilnisite/slovnik/dci/)), jehož bity cyklického redundantního kódu ([CRC](/mobilnisite/slovnik/crc/)) jsou zamaskovány (scrambled) pomocí stránkovacího [RNTI](/mobilnisite/slovnik/rnti/) ([PS-RNTI](/mobilnisite/slovnik/ps-rnti/)). PS-RNTI je pevný, předdefinovaný identifikátor (hodnota: 0xFFFE) známý všem uživatelským zařízením (UE). Tato operace maskování je zásadní pro stránkovací proceduru. Když je UE v úsporném stavu, jako je [RRC](/mobilnisite/slovnik/rrc/)_IDLE nebo RRC_INACTIVE, neudržuje nepřetržité spojení se sítí. Místo toho se periodicky probouzí, aby monitorovala specifické časově-frekvenční zdroje známé jako stránkovací příležitosti (Paging Occasions, [PO](/mobilnisite/slovnik/po/)) v rámci stránkovacího rámce (Paging Frame, [PF](/mobilnisite/slovnik/pf/)). Během těchto PO UE slepe dekóduje fyzický řídicí kanál pro downlink ([PDCCH](/mobilnisite/slovnik/pdcch/)) a hledá DCI. Pokouší se demaskovat CRC jakéhokoli detekovaného DCI pomocí PS-RNTI. Pokud je demaskování úspěšné, potvrdí, že se jedná o DCP určené pro stránkování. Samotný DCP nenese obsah stránkovací zprávy. Místo toho obsahuje informace o přidělení zdrojů (scheduling assignment), jako je modulační a kódovací schéma, přidělení bloků zdrojů a transportní formát. Tyto plánovací informace nasměrují UE ke konkrétním zdrojům na fyzickém sdíleném kanálu pro downlink (PDSCH), kde je přenášena skutečná stránkovací zpráva, zapouzdřená v řídicím prvku MAC pro stránkování (Paging MAC CE) nebo RRC stránkovací zprávě. UE poté dekóduje PDSCH na indikované pozici, aby přijala úplné stránkovací informace, které mohou obsahovat její identitu, pokud je stránkována kvůli příchozímu hovoru, SMS nebo jiné službě iniciované sítí. Tento dvoukrokový proces (DCP na PDCCH, poté zpráva na PDSCH) je vysoce efektivní. Umožňuje síti stránkovat více UE současně ve stejné stránkovací zprávě, zatímco UE provádí minimální zpracování – dekóduje úplnou zátěž PDSCH pouze pokud DCP indikuje přítomnost stránkovacího přenosu. Specifikace řídící DCP, jako je TS 38.212 pro zpracování fyzického kanálu a TS 38.331 pro RRC procedury, detailně popisují přesný použitý formát DCI (např. DCI formát 1_0) a související procesy maskování a dekódování.

## K čemu slouží

Primárním účelem DCP je umožnit efektivní, sítí iniciované probuzení UE v úsporných stavech pro služby iniciované sítí. V celulárních sítích nelze kontaktovat UE, pokud síť nezná její přibližnou polohu a nemůže jí vyslat signál. Když je UE v režimu idle, šetří baterii tím, že většinu času vypíná svůj přijímač. Síť seskupuje UE do stránkovacích skupin na základě jejich identifikátorů a konfiguruje je s cyklem nespojitého příjmu (DRX). Mechanismus DCP řeší problém, jak upozornit konkrétní UE ve skupině, aniž by všechny UE musely neustále naslouchat kanálu. Použitím společného PS-RNTI může jakékoli UE monitorující danou PO efektivně identifikovat řídicí informace určené pro její stránkovací skupinu. Plánovací informace uvnitř DCP pak nasměrují pouze ta UE, která potřebují dekódovat následnou stránkovací zprávu, čímž se minimalizuje zbytečné zpracování PDSCH pro UE, která nejsou stránkována. Tento design je přímým vývojem procedury stránkování z LTE, ale je přizpůsoben pružnější struktuře rámce NR. Řeší základní kompromis mezi životností baterie UE a dostupností v síti. Bez takové cílené signalizační metody by UE musela buď zůstávat ve stavu připojení (což vybíjí baterii), nebo by síť musela častěji vysílat úplné stránkovací zprávy (což plýtvá rádiovými zdroji). DCP poskytuje přesný spouštěč s nízkou režií, který tyto požadavky vyvažuje.

## Klíčové vlastnosti

- CRC je zamaskováno pomocí pevného PS-RNTI (0xFFFE) pro identifikaci
- Nese přidělení zdrojů pro downlink (downlink scheduling assignment) pro stránkovací zprávu na PDSCH
- Používáno UE ve stavech RRC_IDLE a RRC_INACTIVE během stránkovacích příležitostí (Paging Occasions)
- Založeno na DCI formátu 1_0 s kompaktní zátěží pro efektivitu
- Umožňuje skupinové stránkování a efektivní provoz s DRX
- Základní prvek stránkovací procedury NR definované na vrstvě 1 (fyzické) a vrstvě 2 (MAC/RRC)

## Související pojmy

- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [PS-RNTI – Power Saving Radio Network Temporary Identifier](/mobilnisite/slovnik/ps-rnti/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)

## Definující specifikace

- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TR 38.869** (Rel-18) — Study on low-power wake up signal and receiver for NR

---

📖 **Anglický originál a plná specifikace:** [DCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/dcp/)
