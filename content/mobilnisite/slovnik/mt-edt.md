---
slug: "mt-edt"
url: "/mobilnisite/slovnik/mt-edt/"
type: "slovnik"
title: "MT-EDT – Mobile Terminated Early Data Transmission"
date: 2026-01-01
abbr: "MT-EDT"
fullName: "Mobile Terminated Early Data Transmission"
category: "IoT"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mt-edt/"
summary: "Mobile Terminated Early Data Transmission (MT-EDT) je funkce pro Narrowband IoT (NB-IoT) a LTE-M, která umožňuje efektivní, sítí iniciovaný přenos dat ve směru downlink během procedury náhodného příst"
---

MT-EDT je funkce pro NB-IoT a LTE-M, která umožňuje efektivní, sítí iniciovaný přenos dat ve směru downlink během procedury náhodného přístupu, aby se snížila signalizace a spotřeba energie pro malé pakety.

## Popis

Mobile Terminated Early Data Transmission (MT-EDT) je vylepšení pro technologie Cellular IoT (CIoT), konkrétně Narrowband IoT (NB-IoT) a LTE for Machine-Type Communications (LTE-M). Optimalizuje proceduru pro doručení malého downlinkového datového paketu ze sítě k uživatelskému zařízení (UE), které je v úsporném stavu (např. Idle nebo Inactive). Tradičně vyžaduje doručení mobilně-terminovaných dat plnou proceduru Service Request, zahrnující paging, náhodný přístup, navázání [RRC](/mobilnisite/slovnik/rrc/) spojení a nastavení datového beareru, což je signalizačně náročné a spotřebovává značnou energii UE. MT-EDT umožňuje, aby byla downlinková data přenášena spolu se zprávou používanou k odpovědi na preambuli náhodného přístupu od UE během procedury contention-based náhodného přístupu. Proces je spuštěn, když síť obdrží downlinková data pro UE ve stavu RRC Idle nebo RRC Inactive. Síť zašle paging zprávu s indikací, že MT-EDT je podporována. UE po přijetí pagingu iniciuje proceduru náhodného přístupu pomocí specifické preambule alokované pro [EDT](/mobilnisite/slovnik/edt/). V odpovědi na náhodný přístup (Random Access Response, [RAR](/mobilnisite/slovnik/rar/)) zprávě síť zahrne nejen obvyklé časové posunutí (timing advance) a povolení pro uplink (uplink grant), ale také samotnou downlinkovou datovou část (nebo její indikaci). UE pak může přijmout data přímo v této rané výměně zpráv, často dokončující transakci bez přechodu do stavu RRC Connected. To významně snižuje počet signálních zpráv vyměňovaných mezi UE a sítí (eNodeB/gNB). Funkce je úzce spojena s Control Plane CIoT EPS Optimization a User Plane CIoT EPS Optimization. Je řízena specifickými prahovými hodnotami pro velikost dat, aby byla zajištěna efektivita. Klíčové specifikace definují RRC procedury, adaptace signalizace [NAS](/mobilnisite/slovnik/nas/) a dopady na core network, zejména v [MME](/mobilnisite/slovnik/mme/) a Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)).

## K čemu slouží

MT-EDT byl vytvořen k řešení kritické výzvy spotřeby energie a signalizační režie sítě pro IoT zařízení, která primárně přijímají malé, občasné downlinkové pakety (např. konfigurační aktualizace, vzdálené příkazy nebo záplaty firmwaru). Před [EDT](/mobilnisite/slovnik/edt/) vyžadovala každá mobilně-terminovaná datová transakce, bez ohledu na velikost, plné navázání [RRC](/mobilnisite/slovnik/rrc/) spojení zahrnující více kol signálních zpráv. To bylo neefektivní pro IoT zařízení s omezenou kapacitou baterie, která tráví většinu času v hlubokém spánku. Motivace vycházela z potřeby prodloužit výdrž baterie IoT zařízení na roky při zachování spolehlivé dostupnosti downlinku. MT-EDT to řeší minimalizací aktivního rádiového času a počtu přenášených/přijímaných zpráv potřebných pro downlinkovou transakci. Navazuje na základy Uplink EDT (zavedeného dříve) a rozšiřuje koncept časného přenosu dat na směr downlink. Tato optimalizace je klíčovým prvkem pro masivní nasazení IoT, kde jsou kapacita sítě a dlouhá životnost zařízení prvořadé. Řeší omezení předchozích procedur pagingu a service request, které byly navrženy pro provoz orientovaný na člověka s odlišnými profily latence a spotřeby energie.

## Klíčové vlastnosti

- Přenáší downlinková data spolu se zprávou odpovědi na náhodný přístup (Random Access Response, RAR)
- Významně snižuje počet signálních zpráv ve srovnání s plnou procedurou Service Request
- Umožňuje příjem dat, zatímco UE zůstává ve stavu RRC Idle nebo Inactive
- Používá specifické preambule k indikaci schopnosti EDT pro síť
- Definováno pro technologie NB-IoT i LTE-M
- Integruje se s CIoT EPS Optimizations (CP a UP)

## Související pojmy

- [EDT – Energy Detection Threshold](/mobilnisite/slovnik/edt/)

## Definující specifikace

- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters

---

📖 **Anglický originál a plná specifikace:** [MT-EDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mt-edt/)
