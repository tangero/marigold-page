---
slug: "ch"
url: "/mobilnisite/slovnik/ch/"
type: "slovnik"
title: "CH – Correspondent Host"
date: 2026-01-01
abbr: "CH"
fullName: "Correspondent Host"
category: "Other"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ch/"
summary: "Correspondent Host (CH) je síťový uzel nebo koncový bod, který komunikuje s mobilním uživatelem (Mobile Node) v IP mobilních scénářích. Je to partnerská entita v komunikační relaci, která se často nac"
---

CH je partnerský síťový uzel nebo koncový bod, často mimo doménu mobilní sítě, který komunikuje s mobilním uživatelem v rámci IP relace.

## Popis

V kontextu standardů 3GPP a [IETF](/mobilnisite/slovnik/ietf/) pro IP mobilitu je Correspondent Host (CH) definován jako komunikační partner Mobile Node ([MN](/mobilnisite/slovnik/mn/)). Je to jakýkoli hostitel (např. server, jiné uživatelské zařízení), se kterým si MN vyměňuje IP pakety. CH se typicky předpokládá jako standardní IP hostitel bez specifických podpůrných schopností pro mobilitu, což znamená, že funguje pomocí konvenčních mechanismů IP směrování. Primární architektonická role CH je jako cíl nebo zdroj datového provozu v relacích zahrnujících mobilního uživatele. Protokoly správy mobility sítě, jako je Mobile IP ([MIP](/mobilnisite/slovnik/mip/)) a jeho varianty, jsou navrženy tak, aby zajistily správné směrování paketů mezi MN (který může měnit svůj bod připojení k síti) a CH, navzdory tomu, že CH není inherentně vědoma mobility MN.

Provoz CH je z pohledu signalizace mobility pasivní. V základním Mobile IPv4 (MIPv4) a Mobile IPv6 (MIPv6) odesílá CH pakety na domácí adresu (HoA) MN. Tyto pakety zachytí Home Agent ([HA](/mobilnisite/slovnik/ha/)) v domovské síti MN a tuneluje je na aktuální Care-of Address (CoA) MN. Návratový provoz od MN může být odesílán přímo na CH (pomocí optimalizace trasy) nebo zpětně tunelován přes HA. CH samotné se neúčastní aktualizací vazeb (binding updates) ani signalizace mobility; jednoduše odesílá a přijímá IP pakety na/z IP adresy MN podle standardní IP sémantiky. Toto řešení udržuje CH jednoduché a odděluje podporu mobility od korespondenčních uzlů.

Klíčové komponenty v interakci s CH zahrnují Home Agent Mobile Node a v optimalizovaných scénářích funkci Correspondent Node (CN). Zatímco pojmy 'Correspondent Host' a 'Correspondent Node' se často používají synonymně, některé kontexty je rozlišují: Correspondent Node může implikovat uzel, který je si vědom mobility a může se účastnit signalizace optimalizace trasy (jako v MIPv6 Route Optimization), zatímco CH může být považován za obecnějšího, možná mobility nevědomého partnera. IP adresa CH slouží jako stabilní kotva relace z pohledu aplikační vrstvy MN.

V architekturách 3GPP, zejména pro IP Multimedia Subsystem (IMS) a paketové datové sítě, je koncept CH klíčový pro pochopení poskytování služeb end-to-end. Zatímco sítě 3GPP spravují mobilitu na linkové vrstvě (např. handovery) a často používají síťové protokoly správy mobility jako Proxy Mobile IP (PMIP) nebo [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)), IP koncový bod viditelný pro User Equipment (UE) je CH někde na internetu nebo v servisní síti. Role jádra sítě 3GPP spočívá v poskytování nepřerušeného IP spojení mezi UE a jeho různými CH, což zajišťuje, že probíhající relace (jako VoIP hovory nebo video přenosy) jsou při pohybu uživatele plynule udržovány.

## K čemu slouží

Koncept Correspondent Host existuje pro formální modelování partnerské entity v mobilní komunikaci v rámci IP síťových rámců. Před standardizovanými protokoly IP mobility byla IP adresa hostitele vázána na jeho fyzickou síťovou polohu. Pokud se hostitel přesunul, stávající TCP/IP relace s korespondenčními hostiteli (CH) se přerušily, protože pakety již nemohly být správně směrovány. Vývoj Mobile IP zavedl oddělení identifikace (domácí adresa) a lokace (care-of adresa), čímž vznikla potřeba definovat druhou stranu v komunikaci – CH – která nadále používá stabilní domácí adresu.

Jeho vytvoření bylo motivováno potřebou analyzovat, specifikovat a implementovat mobilní řešení bez nutnosti upgradů nebo změn každého možného komunikačního partnera na internetu. Definováním CH jako potenciálně mobility nevědomé entity mohli návrháři protokolů omezit složitost mobility na mobilní uzel a jeho domovskou síť (agenty). Tento přístup zajistil praktickou nasaditelnost mobilních řešení, protože obrovská základna již instalovaných internetových hostitelů nepotřebovala úpravy. CH reprezentuje 'zbytek internetu' v mobilních scénářích.

Koncept řeší základní omezení tradičního IP směrování, které je topologicky založené. Poskytuje jasný referenční bod pro specifikaci toho, jak mají být pakety přesměrovány (pomocí tunelování) a jak lze implementovat optimalizace směrování (např. informování CH o aktuální poloze mobilního uzlu). V kontextech 3GPP pomáhá vymezit odpovědnosti mezi doménou mobilního operátora (spravující mobilitu pro UE) a externím IP světem (obsahujícím CH), což je zásadní pro definice tarifování, řízení politik a bezpečnostních hranic.

## Klíčové vlastnosti

- Partnerský koncový bod v IP komunikační relaci s Mobile Node
- Typicky funguje pomocí standardních IP protokolů bez rozšíření pro mobilitu
- Odesílá pakety na stabilní Home Address Mobile Node
- Přijímá pakety přímo od Mobile Node nebo prostřednictvím jeho Home Agent
- Klíčová referenční entita v architekturách IETF Mobile IP (RFC 3344, RFC 6275) a 3GPP TS 23.402
- Základní pro analýzu end-to-end směrování v mobilních sítích

## Definující specifikace

- **TS 23.042** (Rel-19) — Data Compression and Decompression for 3GPP
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 29.509** (Rel-19) — AUSF Service Based Interface Protocol
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures

---

📖 **Anglický originál a plná specifikace:** [CH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ch/)
