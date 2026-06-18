---
slug: "rcs"
url: "/mobilnisite/slovnik/rcs/"
type: "slovnik"
title: "RCS – Return Channel via Satellite"
date: 2025-01-01
abbr: "RCS"
fullName: "Return Channel via Satellite"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rcs/"
summary: "Služba umožňující satelitní zpětný komunikační kanál pro uživatelské zařízení, která doplňuje pozemní sítě. Poskytuje konektivitu v odlehlých nebo nedostatečně pokrytých oblastech, kde je pozemní infr"
---

RCS je satelitní služba zpětného komunikačního kanálu pro uživatelské zařízení, která poskytuje konektivitu v odlehlých oblastech, kde nejsou dostupné pozemní sítě, a podporuje aplikace jako IoT a širokopásmový přístup.

## Popis

Return Channel via Satellite (RCS) je standardizovaná služba 3GPP, která vytváří satelitní zpětnou komunikační cestu pro uživatelské zařízení (UE). Tato technologie je navržena tak, aby poskytovala konektivitu ve scénářích, kde pozemní sítě chybí, jsou nespolehlivé nebo ekonomicky neproveditelné, například v námořním, leteckém nebo vzdáleném venkovském prostředí. Architektura integruje satelitní přístupové sítě se sítí 5G jádra (5GC), což umožňuje uživatelským zařízením komunikovat prostřednictvím satelitních spojení jak pro řídicí, tak pro uživatelskou rovinu přenosů. Mezi klíčové součásti patří satelitní radiová přístupová síť (RAN), která se skládá ze satelitních uzlů (např. satelitů na nízké oběžné dráze nebo geostacionárních satelitů) a pozemních bran, propojených se sítí 5GC prostřednictvím standardizovaných rozhraní jako [N2](/mobilnisite/slovnik/n2/) a N3. Služba podporuje různé satelitní konstelace a kmitočtová pásma, což zajišťuje flexibilní možnosti nasazení.

RCS funguje tak, že umožňuje uživatelským zařízením vytvořit zpětný kanál prostřednictvím satelitních spojení pro uplink komunikaci, zatímco downlink může být doručován satelitně nebo pozemními prostředky v závislosti na nasazení. Uživatelské zařízení komunikuje se satelitním přístupovým uzlem, který přenáší signály na pozemní bránu připojenou k síti 5GC. Tato brána slouží jako zprostředkovatel, překládající satelitně specifické protokoly na standardy 3GPP a zajišťující bezproblémovou integraci s funkcemi jádrové sítě, jako je Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) a Session Management Function ([SMF](/mobilnisite/slovnik/smf/)). Systém podporuje správu mobility, což umožňuje uživatelským zařízením udržovat relace při pohybu napříč oblastmi pokrytí satelitem, i když s ohledem na latenci a procedury předání optimalizované pro charakteristiky satelitu.

V síti hraje RCS klíčovou roli při rozšiřování služeb 5G na mimopozemní sítě ([NTN](/mobilnisite/slovnik/ntn/)), čímž zvyšuje globální pokrytí a spolehlivost. Umožňuje aplikace jako monitorování IoT, nouzovou komunikaci a širokopásmový internetový přístup v izolovaných oblastech. Služba je definována napříč více vydáními 3GPP s vylepšeními, která řeší aspekty jako kvalita služeb (QoS), zabezpečení a interoperabilita s pozemními systémy. Standardizací satelitních zpětných kanálů 3GPP zajišťuje, že RCS může být operátory nasazena konzistentně, což podporuje široké přijetí a integraci do sítí nové generace.

## K čemu slouží

RCS bylo vytvořeno, aby řešilo omezení pozemních sítí při poskytování všudypřítomného pokrytí, zejména v geograficky náročných nebo řídce osídlených oblastech. Tradiční mobilní sítě se spoléhají na hustou infrastrukturu základnových stanic, což je v regionech jako oceány, pouště nebo polární oblasti nákladově neúnosné nebo fyzicky nemožné. Satelitní komunikace nabízí životaschopnou alternativu, ale historicky proprietární systémy postrádaly integraci s hlavními mobilními sítěmi, což vedlo k fragmentaci a omezené kontinuitě služeb.

Motivace pro standardizaci RCS v rámci 3GPP vychází z rostoucí poptávky po globální konektivitě poháněné aplikacemi IoT, autonomními vozidly a dálkovým průzkumem. Definováním zpětného kanálu prostřednictvím satelitu umožňuje 3GPP bezproblémový roaming mezi pozemními a mimopozemními sítěmi a zajišťuje, že uživatelé mohou přistupovat ke službám bez ohledu na polohu. Tím jsou řešeny kritické mezery v oblasti nouzového řízení, dopravy a venkovského širokopásmového připojení, což podporuje společenské a ekonomické cíle. Vývoj od dřívějších metod satelitní komunikace k integrovaným standardům 3GPP snižuje složitost pro výrobce zařízení a operátory, podporuje inovace a konkurenci v satelitním průmyslu.

## Klíčové vlastnosti

- Satelitní uplink komunikační kanál pro uživatelské zařízení
- Integrace se sítí 5G jádra prostřednictvím standardizovaných rozhraní
- Podpora více satelitních konstelací (LEO, GEO, MEO)
- Správa mobility napříč oblastmi satelitního pokrytí
- Mechanismy kvality služeb (QoS) přizpůsobené satelitní latenci
- Zabezpečovací protokoly pro bezpečné navázání satelitního spoje

## Související pojmy

- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)

## Definující specifikace

- **TS 22.278** (Rel-19) — Evolved Packet System Service Requirements
- **TS 22.803** (Rel-12) — Proximity Services (ProSe) Study
- **TR 22.916** (Rel-19) — Study on Network of Service Robots with Ambient Intelligence
- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.143** (Rel-19) — 5G Messaging Media Types and Codecs
- **TS 26.841** (Rel-19) — Study on Media Messaging Enhancements
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN
- **TS 29.828** (Rel-12) — IMS Media Plane Security H.248 Profiles Study
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols
- **TR 38.900** (Rel-15) — Channel Model Study for >6 GHz
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [RCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/rcs/)
