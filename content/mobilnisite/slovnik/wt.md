---
slug: "wt"
url: "/mobilnisite/slovnik/wt/"
type: "slovnik"
title: "WT – WLAN Termination"
date: 2025-01-01
abbr: "WT"
fullName: "WLAN Termination"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/wt/"
summary: "Síťový uzel definovaný v architekturách LTE-WLAN Aggregation (LWA) a LTE-WLAN Radio Level Integration (LWIP). Ukončuje protokoly uživatelské a řídicí roviny pro WLAN a komunikuje přes rozhraní s LTE e"
---

WT je síťový uzel v architekturách LWA a LWIP, který ukončuje protokoly WLAN a komunikuje přes rozhraní s LTE eNB, aby umožnil integrované řízení rádiových prostředků napříč LTE a WLAN.

## Popis

[WLAN](/mobilnisite/slovnik/wlan/) Termination (WT) je funkční entita zavedená ve 3GPP Release 13 jako součást funkcí LTE-WLAN Radio Level Integration ([LWIP](/mobilnisite/slovnik/lwip/)) a LTE-WLAN Aggregation ([LWA](/mobilnisite/slovnik/lwa/)). Působí jako brána nebo koncový bod na straně WLAN v těchto architekturách těsné integrace. Jak je definováno v TS 36.300, WT ukončuje protokoly uživatelské a řídicí roviny směrem k přístupovému bodu WLAN ([AP](/mobilnisite/slovnik/ap/)) a komunikuje s LTE eNodeB ([eNB](/mobilnisite/slovnik/enb/)) přes standardizované rozhraní (konkrétně rozhraní Xw pro řídicí a uživatelskou rovinu v LWA).

Architektonicky je WT umístěn mezi eNB a jedním či více WLAN AP. V LWA WT ukončuje protokol [PDCP](/mobilnisite/slovnik/pdcp/) pro datové rádiové přenosy, které jsou přesměrovány na WLAN. Přijímá PDCP Protocol Data Units ([PDU](/mobilnisite/slovnik/pdu/)) od eNB přes uživatelskou rovinu Xw a předává je WLAN AP pro přenos k UE, a naopak. V LWIP WT funguje spíše jako brána [IPsec](/mobilnisite/slovnik/ipsec/), navazující se zařízením UE zabezpečené tunely pro přesměrování IP provozu. WT je řízen eNB, který činí centralizovaná rozhodnutí o směrování, rozdělování a přepínání provozu mezi LTE a WLAN na základě rádiových podmínek.

Klíčové součásti funkčnosti WT zahrnují ukončení aplikačního protokolu Xw (Xw-AP) pro řídicí signalizaci s eNB, správu přenosu dat přes uživatelskou rovinu Xw (pomocí GTP-U nebo IPSec) a jeho rozhraní s WLAN AP (které je specifické pro implementaci, ale logicky je řízeno WT). Jeho role je klíčová pro to, aby eNB mohl s WLAN zacházet jako se sekundární skupinou buněk nebo jako s řízenou cestou pro přesměrování toků, což umožňuje skutečnou integraci na rádiové úrovni s koordinovaným plánováním, mobilitou a správou QoS napříč oběma rádiovými technologiemi. To poskytuje výrazně lepší uživatelský zážitek ve srovnání s volným propojením na síťové úrovni.

## K čemu slouží

WT byl vytvořen, aby řešil omezení dřívějších řešení propojení 3GPP a WLAN (jako I-WLAN a směrování založené na ANDSF), která fungovala na úrovni jádra sítě nebo politiky a nebyla schopna provádět rychlý, na rádiové podmínky reagující management provozu. Tyto dřívější přístupy trpěly suboptimálním uživatelským zážitkem kvůli nedostatku koordinace mezi LTE a WLAN rádiovými rozhraními, což vedlo k problémům, jako jsou "přilepení" klienti a neefektivní vyrovnávání zátěže. Motivací pro WT byla potřeba těsnější integrace na rádiové vrstvě, aby bylo možné plně využít kombinovanou kapacitu a pokrytí LTE a Wi-Fi.

Tato technologie řeší problém nekoordinovaného duálního připojení. Zavedením WT jako podřízeného uzlu eNB umožnilo 3GPP síti LTE přímo řídit a spravovat prostředky WLAN na úrovni rádiových přenosů. To umožňuje plynulou agregaci datových toků (LWA) nebo zabezpečenou, sítí řízenou mobilitu IP toků (LWIP), čímž se zlepšuje propustnost, spolehlivost a výkon mobility. Představovala posun paradigmatu od propojování na síťové úrovni ke skutečné konvergenci přístupových sítí, poháněný požadavky operátorů na efektivnější využití všech dostupných rádiových prostředků.

## Klíčové vlastnosti

- Ukončuje rozhraní Xw (řídicí a uživatelskou rovinu) směrem k eNB
- Působí jako koncový bod PDCP pro přenosy WLAN v LTE-WLAN Aggregation (LWA)
- Funguje jako brána IPsec pro LTE-WLAN Radio Level Integration (LWIP)
- Řízen a kontrolován LTE eNodeB pro centralizované řízení rádiových prostředků
- Umožňuje rozdělování/agregaci dat na úrovni rádiových přenosů
- Podporuje hlášení měření rádiových podmínek WLAN asistované zařízením UE

## Související pojmy

- [LWA – LTE-WLAN Radio Level Aggregation](/mobilnisite/slovnik/lwa/)
- [LWIP – LTE WLAN Radio Level Integration with IPsec Tunnel](/mobilnisite/slovnik/lwip/)
- [eNB – Evolved Node B](/mobilnisite/slovnik/enb/)
- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)

## Definující specifikace

- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 36.423** (Rel-19) — X2 Application Protocol (X2AP) Specification
- **TS 36.462** (Rel-19) — Xw Interface Signalling Transport
- **TS 36.463** (Rel-19) — XwAP Protocol Specification
- **TS 36.464** (Rel-19) — Xw Interface User Plane Protocol
- **TS 36.465** (Rel-19) — Xw User Plane Protocol Specification
- **TS 37.870** (Rel-13) — Study on Multi-RAT Joint Coordination
- **TR 38.804** (Rel-14) — Study on New Radio Access Technology; Radio Interface Protocol Aspects

---

📖 **Anglický originál a plná specifikace:** [WT na 3GPP Explorer](https://3gpp-explorer.com/glossary/wt/)
