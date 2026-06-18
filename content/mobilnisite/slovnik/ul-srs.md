---
slug: "ul-srs"
url: "/mobilnisite/slovnik/ul-srs/"
type: "slovnik"
title: "UL-SRS – Uplink Sounding Reference Signal"
date: 2025-01-01
abbr: "UL-SRS"
fullName: "Uplink Sounding Reference Signal"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ul-srs/"
summary: "Referenční signál vysílaný uživatelským terminálem (UE) ve směru uplink, který umožňuje stanici gNB odhadnout kvalitu uplinkového kanálu v širokém pásmu. Tyto informace jsou klíčové pro plánování v up"
---

UL-SRS je referenční signál vysílaný terminálem UE v uplinku, který umožňuje stanici gNB odhadnout kvalitu uplinkového kanálu pro účely plánování, adaptace přenosového spoje a v režimu TDD také pro beamforming v downlinku.

## Popis

Uplink Sounding Reference Signal (UL-SRS) je předem známá sekvence vysílaná terminálem UE, která umožňuje stanici gNodeB (gNB) provést odhad uplinkového kanálu. Na rozdíl od demodulačních referenčních signálů ([DM-RS](/mobilnisite/slovnik/dm-rs/)), které jsou vázány na konkrétní přenos [PUSCH](/mobilnisite/slovnik/pusch/)/[PUCCH](/mobilnisite/slovnik/pucch/), je [SRS](/mobilnisite/slovnik/srs/) vysílán nezávisle, často na základě konfigurace – periodicky, semi-perzistentně nebo aperiodicky. Stanice gNB konfiguruje parametry přenosu SRS prostřednictvím signalizace [RRC](/mobilnisite/slovnik/rrc/) a může spustit aperiodický SRS pomocí [DCI](/mobilnisite/slovnik/dci/). Mezi klíčové parametry patří šířka pásma, časová/frekvenční pozice, přenosový hřeben (comb), cyklický posun a ID sekvence, což umožňuje flexibilní a na UE specifické sondování kanálu.

Primární funkcí je sondování kanálu. Analýzou přijatého SRS může gNB odhadnout informace o stavu uplinkového kanálu ([CSI](/mobilnisite/slovnik/csi/)), včetně frekvenční odezvy kanálu v celém sondovaném pásmu. Tento odhad je klíčový pro několik síťových funkcí. Za prvé umožňuje frekvenčně selektivní plánování pro uplinkový kanál [UL-SCH](/mobilnisite/slovnik/ul-sch/). Plánovač může přidělit prostředky PUSCH ve frekvenčních oblastech, kde má UE silný kanál, čímž maximalizuje propustnost a spektrální účinnost. Za druhé usnadňuje adaptaci uplinkového přenosového spoje tím, že poskytuje informace potřebné pro výběr vhodného schématu modulace a kódování (MCS) pro PUSCH přenos daného UE, čímž vyvažuje přenosovou rychlost a pravděpodobnost chyby.

V systémech s časovým duplexem (TDD), kde uplink a downlink sdílejí stejné frekvenční pásmo, lze uplatnit princip reciprocity kanálu. Odhad uplinkového kanálu získaný ze SRS lze použít k odvození podmínek downlinkového kanálu. To je základním kamenem pro massive MIMO a beamforming. Stanice gNB může použít znalost kanálu založenou na SRS k výpočtu předkódovacích vah pro downlinkové přenosy, čímž efektivně směruje energii k UE a vytváří úzké, fokusované paprsky. Tím se zlepšuje síla downlinkového signálu, sníží se rušení ostatním uživatelům a zvýší celková kapacita sítě. Dále lze SRS nakonfigurovat s přepínáním antén, což umožňuje terminálu UE s více vysílacími anténami postupně sondovat kanál z různých antén, a umožnit tak stanici gNB získat znalost kanálu pro všechny vysílací antény UE, což je zásadní pro uplinkové MIMO a downlinkový beamforming založený na reciprocitě.

## K čemu slouží

UL-SRS byl zaveden, aby poskytl síti vyhrazený a flexibilní mechanismus pro získávání informací o stavu uplinkového kanálu (CSI). Tato schopnost se stala stále kritičtější s vývojem LTE a příchodem 5G NR. Rané verze LTE se zaměřovaly na zpětnou vazbu CSI pro downlink (CQI, PMI, RI) hlášenou terminálem UE. Pro optimální výkon uplinku a plné využití potenciálu pokročilých anténních systémů však síť potřebovala přímou, širokopásmovou znalost rádiového kanálu ve směru uplink.

Motivace vychází z několika omezení spoléhání se pouze na downlinková měření nebo demodulační reference. Demodulační referenční signály (DM-RS) jsou přítomny pouze během přenosu PUSCH a pokrývají pouze přidělené pásmo, neposkytují tedy žádné informace o kvalitě kanálu na jiných frekvencích. SRS tento problém řeší tím, že umožňuje síti proaktivně sondovat kanál v konfigurovatelném, potenciálně celosystémovém pásmu, i když UE nemá žádná data k odeslání. To umožňuje proaktivní rozhodování plánovače.

S důrazem na massive MIMO a beamforming, zejména v TDD nasazeních, se reciprocity kanálu stala vysoce efektivní alternativou k explicitní zpětné vazbě CSI. UL-SRS je signál, který tento přístup umožňuje. Sondováním uplinku může stanice gNB, vybavená velkou anténní soustavou, odhadnout prostorové charakteristiky kanálu a odvodit přesné beamformingové vektory pro downlinkový přenos. To je mnohem škálovatelnější a poskytuje aktuálnější informace než to, aby každé UE měřilo a hlásilo downlinkové CSI pro desítky anténních portů. UL-SRS je tedy klíčovým prvkem pro dosažení vysoké spektrální účinnosti a kapacitních cílů sítí 5G.

## Klíčové vlastnosti

- Širokopásmové nebo částečné sondování kanálu pro získání uplinkového CSI
- Více konfigurací přenosu: periodický, semi-perzistentní a aperiodický (spouštěný DCI)
- Podpora přepínání antén, umožňující sondování kanálu z více vysílacích antén UE
- Konfigurovatelné parametry pro šířku pásma, strukturu hřebene (comb), cyklický posun a časovou pozici pro multiplexování více uživatelů
- Umožňuje frekvenčně selektivní plánování a adaptaci přenosového spoje v uplinku
- Kritický pro downlinkový beamforming založený na reciprocitě kanálu v TDD systémech

## Související pojmy

- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)
- [PUSCH – Physical Uplink Shared Channel](/mobilnisite/slovnik/pusch/)
- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [DM-RS – Demodulation Reference Signal](/mobilnisite/slovnik/dm-rs/)

## Definující specifikace

- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.455** (Rel-19) — NR Positioning Protocol A (NRPPa)
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [UL-SRS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ul-srs/)
