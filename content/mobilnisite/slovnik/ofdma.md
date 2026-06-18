---
slug: "ofdma"
url: "/mobilnisite/slovnik/ofdma/"
type: "slovnik"
title: "OFDMA – Orthogonal Frequency Division Multiple Access"
date: 2025-01-01
abbr: "OFDMA"
fullName: "Orthogonal Frequency Division Multiple Access"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ofdma/"
summary: "Orthogonal Frequency Division Multiple Access (OFDMA) je víceuživatelská verze OFDM, která umožňuje současnou obsluhu více uživatelů přidělováním podmnožin subnosných (zdrojových bloků) různým uživate"
---

OFDMA je primární schéma mnohonásobného přístupu pro downlink 4G LTE a pro uplink/downlink 5G NR, které umožňuje efektivní plánování pro více uživatelů tím, že umožňuje současné obsluhování více uživatelů přidělováním podmnožin subnosných.

## Popis

Orthogonal Frequency Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (OFDMA) rozšiřuje modulační schéma Orthogonal Frequency Division [Multiplexing](/mobilnisite/slovnik/multiplexing/) ([OFDM](/mobilnisite/slovnik/ofdm/)) na flexibilní protokol mnohonásobného přístupu. Zatímco OFDM definuje, jak jsou data modulována na více subnosných pro jednoho uživatele, OFDMA definuje, jak jsou časově-frekvenční zdroje systému OFDM rozděleny a sdíleny mezi více současnými uživateli. Základní jednotkou zdroje je zdrojový blok ([RB](/mobilnisite/slovnik/rb/)), který se skládá ze skupiny sousedících subnosných po dobu jednoho plánovacího intervalu (např. jeden slot). Plánovač v základnové stanici (eNodeB v LTE, gNB v NR) dynamicky přiděluje tyto RB různým uživatelům na základě faktorů, jako je kvalita kanálu, požadavky QoS a vytížení přenosu.

Při provozu vysílač (základnová stanice pro downlink) multiplexuje data pro více uživatelů v rámci stejného OFDM symbolu. Data každého uživatele jsou namapována na konkrétní jemu přidělené subnosné. Kompozitní signál pro všechny uživatele je poté vytvořen pomocí [IFFT](/mobilnisite/slovnik/ifft/), vyslán a přijímán všemi uživateli v buňce. Příjímač každého uživatele provede [FFT](/mobilnisite/slovnik/fft/) na celém přijatém signálu, ale dekóduje pouze subnosné v rámci jemu přidělených RB, ostatní ignoruje. To je možné díky ortogonalitě subnosných. Pro uplink v 5G NR je také používáno OFDMA, což vyžaduje přesnou časovou a frekvenční synchronizaci mezi všemi vysílajícími uživatelskými zařízeními (UE), aby byla zachována ortogonalita na straně přijímače základnové stanice.

OFDMA poskytuje několik klíčových výhod pro mobilní sítě. Umožňuje jemnozrnné dvourozměrné (časové a frekvenční) přidělování zdrojů, což plánovači umožňuje využít diverzitu více uživatelů tím, že přiděluje zdroje uživatelům na jejich nejlepších frekvencích. Podporuje škálovatelné přidělování šířky pásma, od jediného RB až po celou systémovou šířku pásma, a přizpůsobuje se okamžitým datovým potřebám každého uživatele. Dále bezproblémově integruje pokročilé technologie, jako jsou prostorové vrstvy [MIMO](/mobilnisite/slovnik/mimo/), kde mohou být různé vrstvy přiděleny různým uživatelům (Multi-User MIMO). Flexibilita OFDMA, zejména s proměnnou numerologií zavedenou v 5G NR, je klíčová pro podporu různorodých služeb od hromadného IoT přes rozšířené mobilní širokopásmové připojení až po ultra-spolehlivou komunikaci s nízkou latencí.

## K čemu slouží

OFDMA bylo vyvinuto, aby řešilo neefektivitu statického nebo kódováním založeného sdílení zdrojů v předchozích generacích mobilních sítí. V 3G UMTS přiděloval [WCDMA](/mobilnisite/slovnik/wcdma/) celou šířku pásma uživateli prostřednictvím rozprostíracích kódů, což bylo neefektivní pro trhavý datový provoz a omezovalo úroveň podrobnosti plánování pro více uživatelů. Cílem bylo vytvořit schéma mnohonásobného přístupu, které by mohlo efektivně podporovat velký počet uživatelů s různými a dynamickými požadavky na datový tok, což je charakteristické pro paketově přepínaný internetový provoz.

Jeho zavedení s LTE (Release 8) bylo hnací silou potřeby vyšší spektrální účinnosti, nižší latence a lepší podpory paketových datových služeb. OFDMA tyto problémy řeší tím, že umožňuje dynamické přidělování frekvenčních zdrojů na bázi TTI (Transmission Time Interval). To umožňuje paketové plánování ve frekvenční oblasti, kdy jsou uživatelé obsluhováni na subpásmech, kde jsou jejich podmínky kanálu nejsilnější, čímž se maximalizuje propustnost systému. Také umožňuje velmi malé minimální přidělení zdrojů, což je efektivní pro zařízení s nízkým datovým tokem a snižuje plánovací latenci. Pro 5G NR rozšíření OFDMA na uplink (nahrazení SC-FDMA používaného v uplinku LTE) poskytlo větší flexibilitu plánování a bylo umožněno zlepšenou účinností výkonového zesilovače UE, což dále optimalizovalo systém pro extrémní nároky nových případů užití.

## Klíčové vlastnosti

- Umožňuje mnohonásobný přístup dynamickým přidělováním podmnožin OFDM subnosných (zdrojových bloků) různým uživatelům
- Podporuje dvourozměrné (časové a frekvenční) plánování pro využití diverzity více uživatelů
- Umožňuje škálovatelné přidělení šířky pásma na uživatele, od jediného zdrojového bloku po plnou systémovou šířku pásma
- Zachovává ortogonalitu mezi uživateli, minimalizuje vnitrobuněčné rušení při synchronizaci
- Usnadňuje efektivní podporu smíšených typů provozu (např. vysoká propustnost a nízká latence) prostřednictvím flexibilního plánování
- Bezproblémově integruje techniky MIMO pro prostorové multiplexování více uživatelů (MU-MIMO)

## Související pojmy

- [OFDM – Orthogonal Frequency Division Multiplexing](/mobilnisite/slovnik/ofdm/)
- [SC-FDMA – Single Carrier – Frequency Division Multiple Access](/mobilnisite/slovnik/sc-fdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.123** (Rel-19) — Radio Resource Management for TDD
- **TS 25.133** (Rel-19) — UTRAN RRM Requirements for FDD
- **TR 25.912** (Rel-19) — Evolved UTRA and UTRAN Technical Report
- **TS 36.101** (Rel-19) — LTE UE Radio Transmission & Reception Requirements
- **TS 36.102** (Rel-19) — E-UTRA UE Satellite Access RF Requirements
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.302** (Rel-19) — E-UTRA Physical Layer Services
- **TS 36.521** (Rel-19) — E-UTRA UE Conformance ICS Proforma
- **TS 38.133** (Rel-19) — 5G UE Radio Requirements for RRC_IDLE Mobility
- **TS 38.819** (Rel-16) — Band n65 for New Radio Technical Report
- **TS 45.820** (Rel-13) — CIoT for Internet of Things

---

📖 **Anglický originál a plná specifikace:** [OFDMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ofdma/)
