---
slug: "npusch"
url: "/mobilnisite/slovnik/npusch/"
type: "slovnik"
title: "NPUSCH – Narrowband Physical Uplink Shared Channel"
date: 2025-01-01
abbr: "NPUSCH"
fullName: "Narrowband Physical Uplink Shared Channel"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/npusch/"
summary: "NPUSCH je transportní kanál pro uplink v NB-IoT používaný pro přenos uživatelských dat a řídicích informací z koncového zařízení do sítě. Podporuje dva formáty: jeden pro uplinková data (NPUSCH formát"
---

NPUSCH je úzkopásmový fyzický kanál pro sdílenou uplinkovou přenosovou cestu (Narrowband Physical Uplink Shared Channel) v NB-IoT, sloužící k přenosu uživatelských dat a řídicích informací z koncového zařízení do sítě, a podporující formáty pro data i pro potvrzení.

## Popis

Úzkopásmový fyzický kanál pro sdílenou uplinkovou přenosovou cestu (Narrowband Physical Uplink Shared Channel – NPUSCH) je klíčovým fyzickým kanálem v NB-IoT odpovědným za přenosy v uplinku od uživatelského zařízení (UE) k základnové stanici ([eNB](/mobilnisite/slovnik/enb/)/gNB). Je protějškem downlinkového kanálu [NPDSCH](/mobilnisite/slovnik/npdsch/) (Narrowband Physical Downlink Shared Channel). NPUSCH je navržen tak, aby pracoval v rámci omezení NB-IoT, primárně v šířce pásma 180 kHz (nebo jako jednosubnosníkový přenos s šířkou pásma 3,75 kHz či 15 kHz), a splňoval požadavky na extrémní rozšíření pokrytí a ultra-nízkou spotřebu energie. Slouží jako fyzická vrstva přenosové cesty pro úzkopásmovou sdílenou uplinkovou přenosovou cestu (NUL-SCH), která nese data vyšších vrstev, a pro potvrzení hybridního automatického opakování ([HARQ](/mobilnisite/slovnik/harq/)) pro downlinkové přenosy.

NPUSCH je definován ve dvou odlišných formátech, z nichž každý má specifický účel. NPUSCH formát 1 se používá pro přenos uplinkových dat. Lze jej nakonfigurovat pro jednosubnosníkový přenos (s roztečí subnosníků 3,75 kHz nebo 15 kHz) nebo vícesubnosníkový přenos (s použitím 3, 6 nebo 12 subnosníků s roztečí 15 kHz). Jednosubnosníkový přenos, zejména s roztečí 3,75 kHz, poskytuje velmi úzkou přenosovou šířku pásma, což vede k vysoké spektrální výkonové hustotě. To je klíčové pro dosažení maximálního rozšíření pokrytí, protože umožňuje zařízení soustředit svůj omezený vysílací výkon do extrémně úzkého frekvenčního pásma pro průnik náročným prostředím. Vícesubnosníkový přenos nabízí vyšší datové rychlosti pro zařízení v dobrém pokrytí. Kanálové kódování pro formát 1 používá Turbo kódování pro robustní opravu chyb.

NPUSCH formát 2 je vyhrazen výhradně pro přenos řídicích informací v uplinku (UCI), konkrétně potvrzení HARQ ([ACK](/mobilnisite/slovnik/ack/)/[NACK](/mobilnisite/slovnik/nack/)) jako odpovědi na downlinkový přenos NPDSCH. Formát 2 používá jednosubnosníkový přenos s pevnou roztečí subnosníků 3,75 kHz. Přenáší velmi malou datovou část (1 nebo 2 bity pro ACK/NACK) a používá opakovací kódování pro spolehlivost. Přenos NPUSCH je plánován sítí prostřednictvím řídicích informací v downlinku ([DCI](/mobilnisite/slovnik/dci/)) přenášených na [NPDCCH](/mobilnisite/slovnik/npdcch/). Plánovací povolení určují parametry jako přiřazení zdrojů (indexy subnosníků), schéma modulace a kódování (QPSK pro formát 1, [BPSK](/mobilnisite/slovnik/bpsk/) pro formát 2), počet opakování a velikost transportního bloku. Tento přístup založený na povolení zajišťuje efektivní využití sdíleného přenosového média. Konstrukce NPUSCH s jeho flexibilitou v počtu subnosníků a rozsáhlou podporou opakování je klíčová pro splnění cílů NB-IoT v podobě hlubokého pokrytí, dlouhé životnosti baterie (umožněno efektivním využitím výkonového zesilovače v jednosubnosníkovém režimu) a podpory obrovského počtu zařízení s nízkou propustností.

## K čemu slouží

NPUSCH byl vytvořen, aby řešil specifické požadavky NB-IoT na uplink, které stávající fyzický kanál pro sdílenou uplinkovou přenosovou cestu LTE (PUSCH) neuspokojoval dostatečně. Standardní LTE PUSCH je navržen pro širší pásma (nejméně 1,4 MHz) a vyšší datové rychlosti, což jej činí neefektivním a energeticky náročným pro IoT zařízení, která potřebují posílat pouze malé, nepravidelné pakety na velmi dlouhé vzdálenosti. Vysoký poměr špičkového výkonu k průměrnému výkonu (PAPR) více nosičových uplinkových signálů LTE také snižuje účinnost výkonového zesilovače v nízkonákladových zařízeních a zkracuje životnost baterie. Byla zde zjevná potřeba nového uplinkového kanálu optimalizovaného pro IoT paradigma.

Účelem NPUSCH je poskytnout schéma přenosu v uplinku, které maximalizuje pokrytí, minimalizuje spotřebu energie zařízení a podporuje masivní připojení. Řeší problém pokrytí podporou jednosubnosníkového přenosu s nízkou roztečí subnosníků (3,75 kHz), což dramaticky prodlužuje dobu trvání symbolu a zlepšuje odolnost vůči zpoždění šíření a šumu. Rozsáhlý mechanismus opakování (až 128 či více opakování) poskytuje zpracovatelský zisk potřebný pro hluboké vnitřní nebo venkovské pokrytí. Řeší problém energetické účinnosti tím, že umožňuje jednosubnosníkové signály s konstantní obálkou (s modulací pi/2-BPSK nebo pi/4-QPSK), které mají nízký PAPR, což dovoluje výkonovému zesilovači zařízení pracovat blízko svého saturačního bodu s vysokou účinností. Dále, dvouformátová struktura odděluje data a malou řídicí zpětnou vazbu, optimalizuje využití zdrojů pro každý typ informace. NPUSCH byl tedy zásadní inovací, která umožnila realizaci celulární, na baterie provozované IoT v masovém měřítku.

## Klíčové vlastnosti

- Podporuje dva formáty: Formát 1 pro uplinková data a Formát 2 pro HARQ ACK/NACK
- Umožňuje jednosubnosníkový přenos (3,75 kHz nebo 15 kHz) pro maximální pokrytí a energetickou účinnost
- Podporuje vícesubnosníkový přenos (3, 6 nebo 12 subnosníků při 15 kHz) pro vyšší datové rychlosti
- Využívá rozsáhlé opakování (až 2048krát) pro rozšíření pokrytí až na 164 dB MCL
- Používá modulaci s nízkým PAPR (pi/2-BPSK, pi/4-QPSK) pro efektivní provoz výkonového zesilovače
- Přenos založený na plánovacím povolení (grant-based) plánovaný přes NPDCCH pro řízený přístup v uplinku

## Související pojmy

- [NPDSCH – Narrow Band Physical Downlink Shared Channel](/mobilnisite/slovnik/npdsch/)
- [NPDCCH – Narrow Band Physical Downlink Control Channel](/mobilnisite/slovnik/npdcch/)
- [HARQ – Hybrid Automatic Repeat Request](/mobilnisite/slovnik/harq/)

## Definující specifikace

- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.211** (Rel-19) — LTE Physical Layer Specification
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.321** (Rel-19) — E-UTRA MAC Protocol Specification
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [NPUSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/npusch/)
