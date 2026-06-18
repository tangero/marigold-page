---
slug: "rn"
url: "/mobilnisite/slovnik/rn/"
type: "slovnik"
title: "RN – Rank Notification"
date: 2025-01-01
abbr: "RN"
fullName: "Rank Notification"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/rn/"
summary: "Zpětnovazební mechanismus v LTE a NR, ve kterém UE hlásí eNB/gNB doporučený počet datových proudů (hodnost) pro MIMO přenos. Je klíčový pro optimalizaci zisku z prostorového multiplexování a adaptace"
---

RN je zpětnovazební mechanismus v LTE a NR, ve kterém UE hlásí doporučený počet datových proudů pro MIMO přenos, aby optimalizovalo prostorové multiplexování na základě stavu kanálu.

## Popis

Rank Notification (RN, oznámení hodnosti) je klíčovou součástí rámce pro hlášení informace o stavu kanálu ([CSI](/mobilnisite/slovnik/csi/)) v systémech 3GPP LTE a NR. Funguje v rámci řídicí signalizace fyzické vrstvy, konkrétně jako součást zpětné vazby z uživatelského zařízení (UE) k základnové stanici sítě ([eNB](/mobilnisite/slovnik/enb/) v LTE, gNB v NR). Primární funkcí RN je informovat plánovač na straně vysílače o doporučeném počtu prostorově nezávislých vrstev – označovaném jako hodnost – které lze podporovat na aktuálním [MIMO](/mobilnisite/slovnik/mimo/) kanálu. Toto doporučení vychází z odhadu matice downlink kanálu provedeného UE, typicky vypočteného pomocí referenčních signálů jako je [CSI-RS](/mobilnisite/slovnik/csi-rs/). Hodnota hodnosti přímo určuje počet současně přenášených datových proudů využitím prostorového multiplexování, čímž vyvažuje kompromis mezi ziskem z multiplexování a diverzity.

Generování Rank Notification je vnitřně propojeno s dalšími parametry CSI, zejména s indikátorem předkódovací matice ([PMI](/mobilnisite/slovnik/pmi/)) a indikátorem kvality kanálu ([CQI](/mobilnisite/slovnik/cqi/)). UE provádí odhad kanálu a na základě kritérií, jako je maximalizace propustnosti nebo zajištění spolehlivosti, vybere preferovanou hodnost a odpovídající předkódovací matici z kodebuku definovaného ve specifikacích. Tento společný výběr hodnosti a PMI je následně nahlášen síti. Hlášení může být periodické, nakonfigurované pomocí signalizace vyšší vrstvy [RRC](/mobilnisite/slovnik/rrc/), nebo aperiodické, spuštěné downlink grantem. Frekvence a granularita hlášení RN jsou konfigurovatelné, což síti umožňuje vyvážit režii zpětné vazby vůči agilitě MIMO adaptace.

Po přijetí RN (a přidruženého PMI/CQI) učiní plánovač eNB/gNB konečné rozhodnutí o hodnosti přenosu (TR) a předkódování pro downlink přenos dat. Síť může doporučení UE přepsat na základě jiných faktorů, jako je vytížení přenosu, stav vyrovnávací paměti nebo ohledy plánování víceuživatelského MIMO. Přesné hlášení hodnosti je zásadní pro využití kapacitních výhod MIMO. Podhodnocená hodnost vede k nevyužitým prostorovým zdrojům, zatímco nadhodnocená hodnost může způsobit silný mezi-vrstvový interference a chyby paketů. RN je tedy klíčovým prvkem pro adaptivní MIMO, který systému umožňuje dynamicky přepínat mezi diverzitou vysílání, prostorovým multiplexováním a beamformingem podle aktuálního rádiového prostředí.

## K čemu slouží

Rank Notification byl zaveden, aby umožnil efektivní a adaptivní využití technologie antén Multiple-Input Multiple-Output ([MIMO](/mobilnisite/slovnik/mimo/)) v celulárních sítích. Před standardizovanými zpětnovazebními mechanismy, jako je RN, byl provoz MIMO do značné míry statický nebo založený na pomalém odhadu kanálu na straně sítě, který nedokázal sledovat rychlé úniky nebo rychle se měnící prostorové charakteristiky. To omezovalo praktické výhody prostorového multiplexování, zejména pro mobilní uživatele. Mechanismus RN tento problém řeší tím, že poskytuje včasnou zpětnou vazbu od zařízení o prostorové dimenzionalitě kanálu, což síti umožňuje přizpůsobit strategii MIMO přenosu aktuálním podmínkám šíření, které zažívá každé UE.

Vznik RN byl motivován potřebou maximalizovat spektrální účinnost a datové rychlosti, což jsou primární cíle LTE a NR. Tím, že informuje vysílač o udržitelném počtu datových proudů, RN přímo přispívá k vyšší špičkové a průměrné propustnosti v buňce. Řeší základní problém nejistoty kanálu na straně vysílače v systému FDD, kde uplink a downlink používají různé frekvence. Bez takové zpětné vazby by síť musela spoléhat na slepou detekci nebo konzervativní přenosy s nízkou hodností, což by výrazně omezilo výkon MIMO. RN jako součást komplexního rámce pro hlášení CSI poskytuje nezbytnou informaci pro uzavřenou smyčku prostorového multiplexování, čímž se z pokročilého MIMO stává praktická a robustní funkce pro komerční nasazení.

## Klíčové vlastnosti

- Poskytuje hodnost přenosu pro MIMO prostorové multiplexování doporučenou UE
- Integrální součást hlášení informace o stavu kanálu (CSI)
- Založeno na měření downlink referenčních signálů (např. CSI-RS) provedeném UE
- Hlášeno společně s indikátorem předkódovací matice (PMI) a indikátorem kvality kanálu (CQI)
- Podporuje jak periodický (PUCCH), tak aperiodický (PUSCH) režim hlášení
- Používá předkódování založené na kodebuku pro výběr hodnosti a matice

## Související pojmy

- [CSI – Combined CS and IMS Services](/mobilnisite/slovnik/csi/)
- [PMI – Precoding Matrix Indicator](/mobilnisite/slovnik/pmi/)
- [CQI – Channel Quality Indicator](/mobilnisite/slovnik/cqi/)
- [MIMO – Multiple Input Multiple Output](/mobilnisite/slovnik/mimo/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.786** (Rel-16) — Study on V2X architecture enhancements for EPS and 5GS
- **TS 28.658** (Rel-19) — E-UTRAN NRM IRP Information Service
- **TS 29.204** (Rel-19) — SS7 Security Gateway Functional Description
- **TS 32.425** (Rel-19) — E-UTRAN Performance Measurements
- **TS 32.762** (Rel-11) — E-UTRAN NRM IRP Information Service
- **TS 32.851** (Rel-12) — Network Sharing OAM Requirements
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.816** (Rel-11) — Security Analysis for LTE Relay Nodes
- **TS 36.201** (Rel-19) — LTE Physical Layer General Description
- **TS 36.216** (Rel-19) — LTE Relay Node Physical Layer
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.314** (Rel-19) — E-UTRA Radio Measurements Specification
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [RN na 3GPP Explorer](https://3gpp-explorer.com/glossary/rn/)
