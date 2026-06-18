---
slug: "pei"
url: "/mobilnisite/slovnik/pei/"
type: "slovnik"
title: "PEI – Permanent Equipment Identifier"
date: 2026-01-01
abbr: "PEI"
fullName: "Permanent Equipment Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pei/"
summary: "Globálně unikátní, trvalý identifikátor uživatelského zařízení (UE) v rámci 3GPP. Používá se pro identifikaci zařízení, registraci a bezpečnostní procedury a je odlišný od identity účastníka. Je klíčo"
---

PEI je globálně unikátní, trvalý identifikátor uživatelského zařízení (UE) v rámci 3GPP, používaný pro identifikaci zařízení, registraci, zabezpečení a autentizaci.

## Popis

Permanent Equipment Identifier (PEI) je základní identifikátor v systému 3GPP navržený k jednoznačné a trvalé identifikaci fyzického hardwaru uživatelského zařízení (UE). Je definován jako samostatná entita oddělená od identit založených na účastníkovi, jako je [SUPI](/mobilnisite/slovnik/supi/), což zajišťuje jasné rozlišení mezi zařízením a uživatelem. PEI je zapsán do nevolatilní paměti UE během výroby a má po dobu životnosti zařízení zůstat nezměněn, s výjimkou výměny hardwaru. Jeho primární architektonická role je v jádru sítě, konkrétně při interakcích s funkcí pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a jednotnou správou dat ([UDM](/mobilnisite/slovnik/udm/)) v rámci registračních a autentizačních procedur.

Během provozu se PEI používá při počáteční registraci do sítě a autentizaci. V systémech 5G může být PEI zahrnuto do zprávy Registration Request odesílané z UE do AMF. AMF pak tento identifikátor může použít, zejména pro UE, která nemají modul [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module), k autentizaci samotného zařízení. PEI je také klíčovým parametrem pro síťové funkce, jako je registr identit zařízení ([EIR](/mobilnisite/slovnik/eir/)), který jej používá ke kontrole stavu zařízení (např. na černé, šedé nebo bílé listině), aby se zabránilo používání ukradených nebo neautorizovaných zařízení v síti. Tato kontrola pomáhá zmírňovat podvody a chránit síťové zdroje.

Samotný identifikátor může mít různé formy v závislosti na typu zařízení. U tradičních mobilních zařízení jde typicky o [IMEI](/mobilnisite/slovnik/imei/) (International Mobile Equipment Identity) nebo [IMEISV](/mobilnisite/slovnik/imeisv/). U IoT a dalších zařízení může být definován odlišně dle specifikací 3GPP. PEI je kritickým prvkem pro zabezpečení, správu a regulatorní shodu. Podporuje funkce jako autentizace zařízení pro přístup k síti (zejména pro autentizaci bez USIM v IoT scénářích), požadavky na zákonné odposlouchávání a odrazování od krádeží zařízení. Jeho zacházení se řídí přísnými specifikacemi ochrany soukromí a zabezpečení, aby se zabránilo neautorizovanému sledování, přičemž protokoly zajišťují, že není zbytečně přenášen vzduchem.

## K čemu slouží

PEI byl vytvořen, aby poskytl standardizovanou, trvalou a globálně unikátní metodu pro identifikaci telekomunikačního zařízení nezávisle na účastníkovi. Toto řeší několik kritických problémů: umožňuje síťovým operátorům autentizovat zařízení, nikoli pouze účastníky, což je zásadní pro nasazení IoT a scénáře bez [USIM](/mobilnisite/slovnik/usim/). Řeší problém krádeže zařízení a podvodů tím, že umožňuje sítím zařadit ukradená zařízení na černou listinu prostřednictvím registru identit zařízení (EIR) a zabránit tak jejich používání. Historicky, před standardizovanými trvalými identifikátory zařízení, bylo sledování ukradených zařízení nebo správa přístupových politik specifických pro zařízení v různých sítích a regionech nekonzistentní a méně efektivní.

Jeho zavedení a formalizace ve specifikacích 3GPP, zejména od Release 15 s 5G, bylo motivováno rozšiřujícím se ekosystémem internetu věcí (IoT) a potřebou robustnější správy zařízení. Zařízení IoT často používají zjednodušené autentizační schémata nebo nemusí používat tradiční SIM kartu, což činí spolehlivý identifikátor zařízení nezbytným pro síťovou bezpečnost a řízení přístupu. PEI také plní regulatorní požadavky na zákonné odposlouchávání a registraci zařízení v mnoha jurisdikcích. Poskytuje stabilní kotvu pro funkce správy sítě, účtovací systémy a bezpečnostní protokoly, které potřebují korelovat činnosti s konkrétním fyzickým zařízením v čase.

## Klíčové vlastnosti

- Globálně unikátní identifikátor hardwaru UE
- Trvale uložen v nevolatilní paměti zařízení
- Používán pro autentizaci zařízení, odděleně od identity účastníka
- Umožňuje funkci registru identit zařízení (EIR) pro zařazování na černou listinu
- Podporuje přístup k síti pro IoT a zařízení bez USIM
- Nezbytný pro regulatorní shodu a zákonné odposlouchávání

## Související pojmy

- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)
- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 29.256** (Rel-19) — UAS-NF Stage 3 Protocol Specification
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.507** (Rel-19) — 5G Access & Mobility Policy Control Service
- **TS 29.511** (Rel-19) — 5G Equipment Identity Register Service Interface
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 29.571** (Rel-19) — Common Data Types for 5G Service Based Interfaces
- **TS 29.890** (Rel-16) — CT3 5G System Technical Report
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- **TS 32.256** (Rel-19) — 5G Connection & Mobility Charging Spec
- **TS 32.291** (Rel-19) — Charging Management: Service-Based Interface Protocol
- … a dalších 11 specifikací

---

📖 **Anglický originál a plná specifikace:** [PEI na 3GPP Explorer](https://3gpp-explorer.com/glossary/pei/)
