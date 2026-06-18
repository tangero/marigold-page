---
slug: "sfi-rnti"
url: "/mobilnisite/slovnik/sfi-rnti/"
type: "slovnik"
title: "SFI-RNTI – Slot Format Indication Radio Network Temporary Identifier"
date: 2025-01-01
abbr: "SFI-RNTI"
fullName: "Slot Format Indication Radio Network Temporary Identifier"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sfi-rnti/"
summary: "UE-specifický identifikátor používaný v 5G NR pro dynamické označování formátu časového slotu (uplink, downlink, flexibilní) prostřednictvím DCI formátu 2_0. Umožňuje efektivní provoz TDD přizpůsobení"
---

SFI-RNTI je uživatelským zařízením (UE) specifický identifikátor používaný v 5G NR pro dynamické označování formátu časového slotu prostřednictvím DCI formátu 2_0, který umožňuje efektivní provoz TDD přizpůsobením potřebám přenosu.

## Popis

SFI-RNTI je klíčovou součástí dynamického rámce časového duplexu ([TDD](/mobilnisite/slovnik/tdd/)) v 5G New Radio (NR). Jedná se o 16bitovou hodnotu Radio Network Temporary Identifier ([RNTI](/mobilnisite/slovnik/rnti/)), kterou gNB konfiguruje prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) pro uživatelské zařízení (UE) nebo skupinu UE. Její primární funkcí je skramblovat kontrolní součet [CRC](/mobilnisite/slovnik/crc/) (Cyclic Redundancy Check) downlinkového řídicího informačního pole ([DCI](/mobilnisite/slovnik/dci/)) formátu 2_0, což je speciální skupinově společný DCI určený pro indikaci formátu slotu. Když UE úspěšně dekóduje kandidáta [PDCCH](/mobilnisite/slovnik/pdcch/) skramblovaného svým nakonfigurovaným SFI-RNTI, interpretuje jeho obsah jako DCI formát 2_0. Tento DCI obsahuje pole indikátoru formátu slotu, které se mapuje na předkonfigurovanou tabulku formátů slotů, jež definuje směr (downlink 'D', uplink 'U' nebo flexibilní 'F') každého symbolu uvnitř slotu nebo sady slotů. UE pak musí tento indikovaný formát aplikovat, čímž přebije jakoukoli semistatickou konfiguraci TDD UL-DL poskytnutou signalizací vyšší vrstvy pro odpovídající symboly. Tento mechanismus funguje v mnohem rychlejším časovém měřítku (řádově sloty nebo milisekundy) než rekonfigurace RRC, což síti umožňuje rychle reagovat na trhavý provoz. SFI-RNTI tedy funguje jako klíč, který odemyká síťově řízenou adaptaci struktury rádiového rámce v reálném čase, což je zásadní pro podporu různorodých služeb s odlišnými požadavky na latenci a propustnost v 5G. Z architektonického hlediska je definován ve specifikaci [MAC](/mobilnisite/slovnik/mac/) vrstvy (38.321 pro definice RNTI) a je využíván procedurami fyzické vrstvy definovanými v 38.213 pro monitorování PDCCH a interpretaci formátu slotu.

## K čemu slouží

SFI-RNTI byl zaveden v 5G NR Release 15, aby vyřešil nepružnost statických nebo semistatických [TDD](/mobilnisite/slovnik/tdd/) konfigurací používaných v předchozích generacích, jako je LTE. Statické TDD přiděluje pevné vzory uplinkových a downlinkových slotů, což je neefektivní pro asymetrické a rychle se měnící přenosové vzory, což vede buď k plýtvání zdroji, nebo ke zvýšení latence. Dynamické TDD, umožněné mechanismy jako SFI-RNTI a DCI 2_0, dovoluje gNB rekonfigurovat formát slotu na bázi jednotlivých slotů. Tím se řeší klíčové požadavky 5G na ultra-spolehlivou komunikaci s nízkou latencí (URLLC) a rozšířené mobilní širokopásmové připojení (eMBB) minimalizací zpoždění plánování. Například, když vznikne naléhavý downlinkový grant nebo uplinkový přenos, může síť okamžitě převést flexibilní symboly na požadovaný směr bez čekání na pomalou rekonfiguraci RRC. To maximalizuje spektrální efektivitu a kapacitu sítě, což je obzvláště důležité pro vysokofrekvenční pásma (např. mmWave), kde jsou zdroje vzácné. Vytvoření vyhrazeného RNTI pro tento účel zajišťuje, že příkazy pro formát slotu jsou spolehlivě a bezpečně cíleny na konkrétní UE nebo skupiny UE, a udržuje tak jasné signalizační oddělení od ostatních DCI používaných pro plánovací granty.

## Klíčové vlastnosti

- Skrambluje CRC skupinově společného DCI formátu 2_0 pro indikaci formátu slotu
- Umožňuje dynamickou, síťově řízenou adaptaci směru TDD symbolů na každý slot
- Přebíjí semistatickou TDD UL-DL konfiguraci pro indikované symboly
- Konfigurován pro každé UE nebo skupinu UE prostřednictvím RRC signalizace
- Podporuje rychlé časy rekonfigurace (řádově milisekundy)
- Nezbytný pro efektivní využití spektra v nasazeních 5G NR TDD

## Související pojmy

- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [RNTI – Radio Network Temporary Identifier](/mobilnisite/slovnik/rnti/)

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SFI-RNTI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sfi-rnti/)
