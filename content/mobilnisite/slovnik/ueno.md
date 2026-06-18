---
slug: "ueno"
url: "/mobilnisite/slovnik/ueno/"
type: "slovnik"
title: "UENO – Network Operator"
date: 2025-01-01
abbr: "UENO"
fullName: "Network Operator"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ueno/"
summary: "UENO je standardizovaný termín 3GPP pro síťového operátora (Network Operator), tedy subjekt poskytující služby veřejné pozemní mobilní sítě. Definuje administrativní a provozní roli zodpovědnou za nas"
---

UENO je standardizovaný termín 3GPP pro síťového operátora (Network Operator), tedy subjekt, který poskytuje služby veřejné pozemní mobilní sítě a je zodpovědný za její nasazení, správu a údržbu.

## Popis

Ve specifikacích 3GPP je UENO formální označení pro síťového operátora (Network Operator). Tento subjekt je právní a administrativní entita, která vlastní licenci k provozování veřejné pozemní mobilní sítě ([PLMN](/mobilnisite/slovnik/plmn/)). Tento koncept je základním kamenem celé architektury 3GPP, neboť vymezuje vlastnictví a provozní hranice sítě. Specifikace podrobně popisují odpovědnosti, rozhraní a smlouvy o úrovni služeb, které se týkají UENO, zejména ve scénářích zahrnujících roaming, propojení mezi operátory a regulatorní požadavky.

Role UENO zahrnuje nasazení infrastruktury jádra sítě (CN) a rádiové přístupové sítě (RAN), včetně síťových uzlů jako [MME](/mobilnisite/slovnik/mme/), [SGW](/mobilnisite/slovnik/sgw/), [PGW](/mobilnisite/slovnik/pgw/) a eNodeB/gNB. UENO je zodpovědný za správu účastníků, poskytování [SIM](/mobilnisite/slovnik/sim/)/[USIM](/mobilnisite/slovnik/usim/) karet, definici tarifních plánů a zajištění výkonu a zabezpečení sítě. V prostředí více operátorů UENO uzavírá dohody s dalšími UENO o roamingu, propojení a sdílení zdrojů, které se řídí standardy definovanými např. ve specifikaci TS 22.057.

Z technického hlediska je UENO v síti identifikován svým PLMN ID, jedinečným kódem složeným z mobilního kódu země ([MCC](/mobilnisite/slovnik/mcc/)) a mobilního kódu sítě ([MNC](/mobilnisite/slovnik/mnc/)). Tento identifikátor je vysílán RAN a používá jej uživatelské zařízení (UE) pro procedury výběru a připojení k síti. Provozní domény UENO zahrnují síťové operační centrum (NOC), fakturační systémy a platformy pro správu vztahů se zákazníky, které jsou neoddělitelnou součástí komerčního poskytování služeb. Standardizace této role zajišťuje interoperabilitu a jasné vymezení odpovědností v globálním ekosystému.

## K čemu slouží

Formální definice UENO ve standardech 3GPP slouží k vytvoření jasné a jednoznačné reference pro subjekt provozující mobilní síť. To je klíčové pro vývoj specifikací, které zahrnují právní, komerční a technické interakce mezi různými stranami. Před takovou standardizací mohly být termíny jako 'dopravce' nebo 'poskytovatel služeb' vágní a vést k nekonzistencím v mezinárodních roamingových dohodách, regulatorním reporting a definicích technických rozhraní.

Stanovením UENO jako standardizovaného termínu poskytuje 3GPP konzistentní rámec pro všechny následující specifikace odkazující na síťového operátora. To je nezbytné pro definici rolí domácí a navštívené sítě v roamingových architekturách, specifikaci odpovědností za bezpečnostní funkce jako je autentizace a vymezení povinností v oblasti zákonného odposlechu a tísňových služeb. Reaguje tak na potřebu univerzální smluvní a technické entity v globálně propojeném telekomunikačním systému.

Vznik tohoto termínu byl motivován přechodem od národních, monolitických telekomunikačních operátorů ke konkurenčnímu, více-dodavatelskému a mezinárodnímu prostředí. Pomáhá vymezit hranice pro správu sítě, odpovědnost za poruchy a dělení výnosů. Specifikace řídící rozhraní mezi operátory, jako jsou ta pro roamingové partnery nebo mezi síťovým operátorem a poskytovatelem služeb třetí strany, spoléhají na přesný koncept UENO, aby fungovaly správně a komerčně.

## Klíčové vlastnosti

- Držitel licence k provozování veřejné pozemní mobilní sítě (PLMN)
- Jednoznačně identifikován PLMN ID (MCC+MNC)
- Zodpovědný za nasazení a údržbu infrastruktury jádra sítě (CN) a RAN
- Spravuje data účastníků, jejich zřízení a fakturaci
- Uzavírá roamingové a propojovací dohody s dalšími UENO
- Podléhá regulatorním povinnostem včetně zákonného odposlechu a tísňových služeb

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [MCC – Mobile Country Code](/mobilnisite/slovnik/mcc/)
- [MNC – Mobile Network Code](/mobilnisite/slovnik/mnc/)

## Definující specifikace

- **TS 22.057** (Rel-19) — Mobile Execution Environment (MExE) Stage 1

---

📖 **Anglický originál a plná specifikace:** [UENO na 3GPP Explorer](https://3gpp-explorer.com/glossary/ueno/)
