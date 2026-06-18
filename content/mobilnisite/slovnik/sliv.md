---
slug: "sliv"
url: "/mobilnisite/slovnik/sliv/"
type: "slovnik"
title: "SLIV – Start and Length Indicator Value"
date: 2025-01-01
abbr: "SLIV"
fullName: "Start and Length Indicator Value"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sliv/"
summary: "Kompaktní signalizační parametr v 5G NR, který sdruženě kóduje počáteční symbol a počet po sobě jdoucích symbolů alokovaných pro přiřazení fyzického sdíleného kanálu pro downlink nebo uplink (PDSCH/PU"
---

SLIV je kompaktní signalizační parametr v 5G NR, který sdruženě kóduje počáteční symbol a délku alokace PDSCH nebo PUSCH v rámci slotu za účelem snížení režie řídicího kanálu.

## Popis

Hodnota indikátoru počátku a délky (SLIV) je klíčovým polem informace řídicího kanálu pro downlink ([DCI](/mobilnisite/slovnik/dci/)) v 5G New Radio (NR) používaným pro dynamické přidělování časových zdrojů. Jejím hlavním účelem je efektivně signalizovat uživatelskému zařízení (UE) přesnou polohu a dobu trvání přenosu ve fyzickém sdíleném kanálu pro downlink ([PDSCH](/mobilnisite/slovnik/pdsch/)) nebo fyzickém sdíleném kanálu pro uplink ([PUSCH](/mobilnisite/slovnik/pusch/)) v rámci daného slotu. Namísto vysílání dvou samostatných hodnot pro počáteční symbol (S) a délku ve znacích (L) je gNodeB kóduje do jediné kompaktní celočíselné hodnoty – SLIV. UE tuto hodnotu dekóduje pomocí předdefinovaného vzorce nebo tabulky specifikované v 3GPP TS 38.214, aby získala S a L.

Kódovací pravidlo zajišťuje platnost: kombinace S a L musí definovat zdroj, který se celý vejde do 14 symbolů slotu (pro normální cyklickou předponu). Vzorec je: pokud (L-1) ≤ 7, pak SLIV = 14*(L-1) + S, jinak SLIV = 14*(14-L+1) + (14-1-S). UE vypočítá S a L z přijaté hodnoty SLIV vyzkoušením obou možných interpretací. Toto sdružené kódování šetří cenné bity v datové části DCI, což je klíčové pro udržení nízké režie řídicího kanálu, zejména pro menší části šířky pásma a při plánování mnoha uživatelů.

SLIV je součástí tabulky přidělování časových zdrojů (TDRA). Síť může prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) nakonfigurovat UE s jednou nebo více položkami TDRA, kde každá položka obsahuje parametry jako typ mapování, posun slotu (K0/K2) a SLIV. Během dynamického plánování odkazuje DCI na jednu z těchto předem nakonfigurovaných položek pomocí pole indexu TDRA. Tento dvoukrokový proces (konfigurace RRC + indikace DCI) poskytuje flexibilitu: běžné vzory lze konfigurovat polostaticky, zatímco DCI dynamicky vybere ten vhodný. SLIV přímo určuje časové zdroje, které v kombinaci s přidělením frekvenčních zdrojů (prostřednictvím pole přiřazení frekvenčních zdrojů) dávají UE jeho kompletní naplánovanou sadu bloků zdrojů.

## K čemu slouží

SLIV byl vytvořen pro 5G NR, aby řešil potřebu vysoce flexibilního a efektivního přidělování časových zdrojů. Na rozdíl od 4G LTE, které primárně plánovalo zdroje v jednotkách podrámců (1 ms), zavedlo 5G NR flexibilnější strukturu slotů a minislotů s proměnnou numerologií (rozestup podnosných). To umožňuje, aby přenosy začínaly na libovolném symbolu a měly délku až jeden symbol. Signalizace takové flexibility pomocí samostatných polí pro počátek a délku by vyžadovala příliš mnoho bitů v [DCI](/mobilnisite/slovnik/dci/), což by zvýšilo režii řídicího kanálu a snížilo kapacitu plánování.

Motivací bylo minimalizovat režii řídicí signalizace při maximalizaci flexibility plánování – což je klíčový požadavek pro různorodé případy užití 5G. Pro rozšířené mobilní širokopásmové připojení (eMBB) umožňuje efektivní zabalení uživatelských dat. Pro ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) umožňuje okamžité plánování minislotů pro přerušení probíhajícího provozu eMBB, což je usnadněno schopností signalizovat přenos začínající na libovolném symbolu. Sdružené kódování SLIV je elegantním řešením z teorie informace, které využívá omezení, že S+L musí být ≤ 14, aby se snížil počet možných platných kombinací (S, L), a tím i počet bitů potřebných k jejich signalizaci. Tento návrh přímo řeší omezení rigidnější alokace LTE a je zásadní pro dynamické [TDD](/mobilnisite/slovnik/tdd/) a schopnosti nízké latence v NR.

## Klíčové vlastnosti

- Sdruženě kóduje počáteční symbol (S) a délku alokace (L) do jediné celočíselné hodnoty za účelem úspory bitů v DCI.
- Podporuje flexibilní plánování začínající na libovolném OFDM symbolu v rámci slotu pro downlink i uplink.
- Umožňuje přenosy v minislotech (délka menší než 14 symbolů), klíčové pro URLLC a snížení latence.
- Používá deterministický vzorec pro kódování/dekódování, standardizovaný v 3GPP TS 38.214.
- Integrováno do rámce přidělování časových zdrojů (TDRA) s tabulkami konfigurovanými přes RRC.
- Nezbytné pro dynamické sdílení zdrojů a přerušování v 5G NR.

## Související pojmy

- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)
- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)

## Definující specifikace

- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.214** (Rel-19) — NR Physical Layer Procedures for Data

---

📖 **Anglický originál a plná specifikace:** [SLIV na 3GPP Explorer](https://3gpp-explorer.com/glossary/sliv/)
