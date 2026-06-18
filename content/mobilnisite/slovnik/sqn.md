---
slug: "sqn"
url: "/mobilnisite/slovnik/sqn/"
type: "slovnik"
title: "SQN – Sequence Number"
date: 2025-01-01
abbr: "SQN"
fullName: "Sequence Number"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/sqn/"
summary: "SQN (Sequence Number) je bezpečnostní parametr v 3GPP protokolech pro autentizaci a dohodu klíčů (AKA), používaný k zajištění aktuálnosti a prevenci replay útoku. Je generován síťovým prvkem a ověřová"
---

SQN je bezpečnostní parametr v 3GPP autentizačních protokolech, který je generován síťovým prvkem, aby zajistil aktuálnost (freshness) a prevenci replay útoku, a který je ověřován UE pro vzájemnou autentizaci a derivaci klíčů.

## Popis

Sequence Number (SQN) je základní bezpečnostní element v 3GPP systémech, definovaný v řadě specifikací jako 33.102 a 33.401, jako část protokolu Authentication and Key Agreement ([AKA](/mobilnisite/slovnik/aka/)). SQN je hodnota typu counter nebo nonce generovaná autentizačním centrem (AuC) nebo serverem [HSS](/mobilnisite/slovnik/hss/) síťového prvku, která zajišťuje aktuálnost autentizačních vektorů a prevenci replay útoku. Během autentizačního procesu je SQN zahrnuto v autentizačním tokenu ([AUTN](/mobilnisite/slovnik/autn/)) zaslaném uživatelskému zařízení (UE), které jej pak ověřuje vůči lokálně uloženým hodnotám, aby potvrdilo, že autentizační požadavek je aktuální a není duplicitní. Tento mechanismus je nezbytný pro vzájemnou autentizaci, kde síťový prvek i UE ověřují legitimnost druhé strany, a pro derivaci session klíčů (např. [CK](/mobilnisite/slovnik/ck/), [IK](/mobilnisite/slovnik/ik/)), které zabezpečují následnou komunikaci.

Architektonicky SQN funguje v bezpečnostní vrstvě core networku a UE, a komunikuje s komponentami jako AuC, HSS a [USIM](/mobilnisite/slovnik/usim/) v UE. SQN je typicky 48-bitová hodnota, strukturovaná tak, aby obsahovala sekvenční informaci a volitelně index pro management. Funguje tak, že je inkrementována nebo aktualizována síťovým prvkem pro každou autentizační instanci, což zajistí její unikátnost. Když UE přijme AUTN, extrahuje SQN, ověří jeho aktuálnost na základě okna přijatelných hodnot, a pokud je validní, pokračuje s derivací klíčů. Pokud je SQN mimo synchronizaci (např. kvůli problémům v síti nebo útoku), UE může iniciovat resynchronizační procedury, jak definují specifikace jako 33.102, aby obnovila bezpečnostní alignment bez narušení služby.

Operačně SQN je integrální část procesu AKA: síťový prvek generuje autentizační vektor obsahující [RAND](/mobilnisite/slovnik/rand/) (random challenge), AUTN (který obsahuje SQN maskovaný anonymizačním klíčem [AK](/mobilnisite/slovnik/ak/)), XRES (expected response) a session klíče. UE dešifruje AUTN, aby získalo SQN, ověří jej pomocí parametrů uložených v USIM, a vypočítá odpověď (RES) pro ověření síťovým prvkem. Toto zajistí, že každá autentizační session je unikátní a resistentní vůči replay útoku, což poskytuje ochranu proti eavesdropping a man-in-the-middle útoku. Role SQN se rozšiřuje od 2G (kde byla jednodušší) až do 5G, a vyvíjí se, aby podporovala enhanced privacy a bezpečnostní funkce, jako v 5G AKA, kde je zpracování SQN refinované, aby řešilo privacy concerns jako subscriber traceability.

## K čemu slouží

SQN bylo zaváděno, aby řešilo bezpečnostní vulnerability v raných mobilních sítích, konkrétně absence replay protection v autentizačních protokolech. Před SQN systémy jako GSM používaly simple challenge-response mechanismy bez sekvenčního sledování, což je činilo susceptible vůči replay útoku, kdy interceptované autentizační message mohly být reused k impersonation userů. SQN řeší tento problém přidáním aktuálnosti prostřednictvím sekvenčně rostoucího čísla, což zajistí, že každý autentizační pokus je unikátní a time-sensitive. Tato enhancement byla motivována potřebou stronger mutual authentication, jak se sítě vyvíjely od 2G do 3G a dalších generací, aby podporovaly služby jako mobile banking a IoT, které demand vyšší security.

Historicky SQN bylo standardizováno v 3GPP Rel-2 jako část UMTS AKA protokolu, building na lessons z GSM weaknesses. Jeho creation bylo driven requirement pro robustní key agreement a privacy v 3G sítích, jak je outlined v specifikacích jako 33.102. V průběhu releases bylo SQN adapted, aby address nové threats, jako v 4G EPS AKA (33.401), kde podporuje LTE security, a v 5G AKA (33.501), kde je jeho structure optimized, aby prevent privacy leaks. Zajišťováním autentizační aktuálnosti SQN enable secure mobility, roaming a service access across generací mobilní technologie.

## Klíčové vlastnosti

- Zajišťuje aktuálnost (freshness) autentizačních vektorů k prevenci replay útoku
- 48-bitová hodnota generovaná AuC/HSS a ověřovaná UE USIM
- Integrální část AUTN v AKA protokolech pro vzájemnou autentizaci
- Podporuje resynchronizační procedury pro handling out-of-sync scénářů
- Vyvíjeno od 2G do 5G s enhanced privacy a bezpečnostními refinements
- Kritické pro derivaci session klíčů (CK, IK) a zabezpečení komunikace

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [AUTN – Authentication Token](/mobilnisite/slovnik/autn/)
- [AUC – Authentication Centre](/mobilnisite/slovnik/auc/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.103** (Rel-19) — ISIM Application Specification
- **TR 31.900** (Rel-19) — 3GPP TS 31.900: Security Interworking Guidance
- **TS 33.102** (Rel-19) — 3G Security Architecture Specification
- **TS 33.105** (Rel-19) — 3G Security: Cryptographic Algorithm Requirements
- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.863** (Rel-14) — Security for Battery-Efficient IoT Device to Enterprise
- **TS 35.205** (Rel-19) — MILENAGE Algorithm Set: General Overview
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [SQN na 3GPP Explorer](https://3gpp-explorer.com/glossary/sqn/)
