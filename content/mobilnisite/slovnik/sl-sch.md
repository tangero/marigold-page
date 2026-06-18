---
slug: "sl-sch"
url: "/mobilnisite/slovnik/sl-sch/"
type: "slovnik"
title: "SL-SCH – Sidelink Shared Channel"
date: 2025-01-01
abbr: "SL-SCH"
fullName: "Sidelink Shared Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sl-sch/"
summary: "Primární transportní kanál pro uživatelská data v komunikaci postranním spojem (sidelink, zařízení-zařízení). Přenáší data z vrstvy MAC mezi UEs přes rozhraní PC5. SL-SCH je zásadní pro V2X, veřejnou"
---

SL-SCH je primární transportní kanál pro uživatelská data v postranním spoji (sidelink), přenášející data mezi zařízeními přes rozhraní PC5 pro služby jako V2X a veřejná bezpečnost.

## Popis

Sidelink Shared Channel (SL-SCH) je transportní kanál v protokolových zásobnících 3GPP LTE a NR určený pro přenos uživatelských dat a některých řídicích informací pro přímou komunikaci zařízení-zařízení, známou jako sidelink. Funguje přes rozhraní PC5. Funkčně analogický k Downlink Shared Channel ([DL-SCH](/mobilnisite/slovnik/dl-sch/)) a Uplink Shared Channel ([UL-SCH](/mobilnisite/slovnik/ul-sch/)) používaným pro spoje síť-zařízení, SL-SCH je hlavním nosičem pro přenos dat sidelink. V protokolovém zásobníku vysílače jsou data z vyšších vrstev (např. IP pakety pro [V2X](/mobilnisite/slovnik/v2x/) zprávy) zpracovány vrstvami Packet Data Convergence Protocol ([PDCP](/mobilnisite/slovnik/pdcp/)), Radio Link Control ([RLC](/mobilnisite/slovnik/rlc/)) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)). Vrstva MAC doručuje transportní bloky fyzické vrstvě, která je mapuje na SL-SCH. Fyzická vrstva následně aplikuje kanálové kódování (např. Turbo kódy v LTE, [LDPC](/mobilnisite/slovnik/ldpc/) v NR), modulaci a mapuje zakódované bity na zdrojové prvky v rámci fondu zdrojů sidelink v časově-frekvenční mřížce. Klíčovou součástí spojenou se SL-SCH je Sidelink Control Information ([SCI](/mobilnisite/slovnik/sci/)), vysílaná na PSCCH (Physical Sidelink Control Channel). SCI nese potřebné informace pro demodulaci a dekódování odpovídajícího přenosu SL-SCH, jako je přidělení zdrojů, modulační a kódovací schéma (MCS) a skupinové cílové ID. Na straně přijímače je proces obrácený: UE nejprve dekóduje SCI a poté použije tyto informace k nalezení, demodulaci a dekódování transportního bloku SL-SCH. SL-SCH podporuje jak vysílací (broadcast), tak skupinové (groupcast) režimy přenosu a je navržen pro dynamické a efektivní sdílení zdrojů mezi více UEs v blízkosti.

## K čemu slouží

SL-SCH byl vytvořen, aby poskytl standardizovaný, efektivní a škálovatelný transportní mechanismus pro uživatelská data v přímé komunikaci zařízení-zařízení, což byla zásadní nová schopnost zavedená 3GPP počínaje LTE Release 12 pro Proximity Services (ProSe). Před jeho zavedením byla komunikace zařízení-zařízení v celulárních sítích nestandardizovaná nebo závisela na krátkodosahových technologiích jako Bluetooth či Wi-Fi Direct, kterým chyběla synchronizace v široké oblasti, kvalita služeb a bezproblémová integrace s celulárními sítěmi, kterou 3GPP chtěla poskytnout. SL-SCH řeší problém, jak efektivně multiplexovat data od mnoha potenciálně vysílajících UEs na sdílený fond rádiových zdrojů řízeným způsobem. Umožnil klíčové případy užití, jako je komunikace pro veřejnou bezpečnost, když jsou celulární sítě nedostupné (např. při katastrofách), a komunikaci vozidlo-se-vším (V2X) pro bezpečnost v automobilovém průmyslu. Jeho vývoj v následujících releasech byl hnán potřebou vyšší spolehlivosti, nižší latence, vyšších přenosových rychlostí a sofistikovanějších režimů přidělování zdrojů (režim 1 plánovaný sítí a režim 2 autonomní), aby podpořil stále náročnější aplikace jako autonomní řízení a pokročilý průmyslový IoT.

## Klíčové vlastnosti

- Primární transportní kanál pro přenos uživatelských dat přes postranní spoj (sidelink) rozhraní PC5
- Dynamicky sdílený mezi více UEs pomocí fondů zdrojů přidělených v čase a frekvenci
- Spojený s řídicí informací postranního spoje (SCI) na PSCCH pro parametry dekódování
- Podporuje vysílací (broadcast), skupinové (groupcast) a individuální (unicast) režimy přenosu (závislé na režimu)
- Využívá adaptivní modulaci a kódování (MCS) pro adaptaci spoje
- Základní pro architektury postranního spoje založené na LTE (D2D, V2X) i na NR

## Související pojmy

- [PSCCH – Physical Sidelink Control Channel](/mobilnisite/slovnik/pscch/)
- [SCI – Subscriber Controlled Input / Send Charging Information](/mobilnisite/slovnik/sci/)
- [V2X – Vehicle-to-Everything Application Server](/mobilnisite/slovnik/v2x/)
- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 38.212** (Rel-19) — NR Multiplexing and Channel Coding
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [SL-SCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/sl-sch/)
