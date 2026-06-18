---
slug: "npn"
url: "/mobilnisite/slovnik/npn/"
type: "slovnik"
title: "NPN – Non-Public Network"
date: 2026-01-01
abbr: "NPN"
fullName: "Non-Public Network"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/npn/"
summary: "5G síť nasazená pro soukromé použití, například podnikem, továrnou nebo kampusem. Poskytuje vyhrazenou, lokalizovanou konektivitu s rozšířenou kontrolou nad zabezpečením, výkonem a službami, a odlišuj"
---

NPN je soukromá 5G síť, například pro podnik nebo továrnu, která poskytuje vyhrazenou, lokalizovanou konektivitu s rozšířenou kontrolou nad zabezpečením a výkonem, a která se odlišuje od veřejných sítí.

## Popis

Non-Public Network (NPN, neveřejná síť) je systém 5G sítě určený pro soukromé použití subjektu, jako je podnik, energetická společnost, vládní organizace nebo průmyslový areál. 3GPP ji definuje jako síť, která není nabízena široké veřejnosti. NPN lze nasadit jako plně samostatné systémy nebo je možné je pro určité služby integrovat s veřejnou pozemní mobilní sítí ([PLMN](/mobilnisite/slovnik/plmn/)). Architektura je postavena na standardním 3GPP 5G systému (5GS), ale je přizpůsobena pro soukromý provoz a nabízí vyhrazený a předvídatelný výkon, ultra-spolehlivou komunikaci s nízkou latencí ([URLLC](/mobilnisite/slovnik/urllc/)) a rozšířenou ochranu soukromí a zabezpečení dat v definované geografické oblasti, jako je výrobní hala, přístav, důl nebo kampus.

NPN pracují s využitím základních síťových funkcí ([NF](/mobilnisite/slovnik/nf/)) 5G, jako je funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)), funkce správy relací ([SMF](/mobilnisite/slovnik/smf/)) a funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)), které lze nasadit na vlastních prostorách nebo ve vyhrazeném cloudu. Pro bezdrátový přístup využívají 5G New Radio (NR), potenciálně v licencovaném, sdíleném nebo nelicencovaném spektru (např. 5G [NR-U](/mobilnisite/slovnik/nr-u/)). Klíčovým architektonickým konceptem je identifikátor sítě ([NID](/mobilnisite/slovnik/nid/)), který v kombinaci s identifikátorem PLMN (PLMN ID) jednoznačně identifikuje NPN. Samostatné NPN (SNPN) fungují zcela nezávisle s vlastními přihlašovacími údaji a identitou, zatímco NPN integrované s veřejnou sítí (PNI-NPN) využívají síťové řezy nebo vyhrazené prostředky od operátora veřejné PLMN k poskytování služeb NPN.

Princip fungování: Zařízení (UE) nakonfigurovaná pro NPN objevují a vybírají síť na základě vysílaných identifikátorů. Pro SNPN se ověřování a autorizace provádějí pomocí přihlašovacích údajů spravovaných soukromým subjektem, nikoli veřejným mobilním operátorem (MNO). Síťové politiky, jako je řízení přístupu, upřednostňování QoS pro kritická zařízení a lokální odklonění datového provozu, jsou vynucovány lokálně nasazenými funkcemi 5G jádra. To umožňuje, aby citlivá data zůstala na místě, zajišťuje nízkou latenci pro průmyslové řídicí smyčky a poskytuje podniku plnou administrativní kontrolu nad síťovými prostředky, uživatelskými zařízeními a službami.

## K čemu slouží

NPN byly vytvořeny za účelem splnění náročných požadavků vertikálních odvětví (např. výroba, logistika, energetika) na konektivitu, které nemohou být plně uspokojeny veřejnými mobilními sítěmi s nejlepším úsilím (best-effort). Veřejné sítě jsou navrženy pro široké pokrytí a vysokou kapacitu, ale nabízejí omezené záruky na latenci, spolehlivost, lokalitu dat a administrativní kontrolu. Odvětví procházející digitální transformací (Průmysl 4.0) vyžadují deterministický výkon pro aplikace jako automaticky řízená vozidla, řízení procesů v reálném čase, rozšířená realita pro údržbu a rozsáhlé senzorové sítě.

Motivace pro standardizaci NPN v 3GPP (počínaje Release 16) bylo poskytnout jednotný, interoperabilní rámec pro soukromé 5G sítě, což znamená odklon od proprietárních řešení. Řeší omezení předchozích přístupů, jako je Wi-Fi (kterému chybí bezproblémová mobilita, ultra-spolehlivost a nativní podpora síťových řezů) a raných nestandardizovaných soukromých systémů LTE. NPN využívají plnou kapacitu 5G – včetně síťových řezů, edge computingu a přesné QoS – ve vyhrazeném prostředí. Řeší problémy suverenity dat, spolehlivosti komunikace pro mise-kritické aplikace a integrace s průmyslovými systémy operační technologie (OT), což podnikům umožňuje vybudovat zabezpečenou, vysoce výkonnou bezdrátovou infrastrukturu šitou na míru jejich specifickým provozním potřebám.

## Klíčové vlastnosti

- Vyhrazený síťový provoz pro jedinou organizaci (podnik, továrna)
- Podpora jak modelu samostatné NPN (SNPN), tak modelu NPN integrované s veřejnou sítí (PNI-NPN)
- Použití identifikátoru sítě (NID) pro jednoznačnou identifikaci
- Nasazení síťových funkcí 5G jádra na vlastních prostorách nebo lokalizovaně
- Rozšířená kontrola nad zabezpečením, ověřováním a ochranou soukromí dat
- Podpora klíčových schopností 5G jako URLLC, mMTC a síťových řezů v rámci soukromé domény

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [URLLC – Ultra Reliable Low Latency Communication](/mobilnisite/slovnik/urllc/)
- [5GS – 5G System](/mobilnisite/slovnik/5gs/)
- [PNF – Physical Network Function](/mobilnisite/slovnik/pnf/)

## Definující specifikace

- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TR 22.832** (Rel-17) — Study on cyber-physical control in vertical domains
- **TS 23.289** (Rel-20) — Mission Critical services over 5G System
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TR 26.805** (Rel-17) — Study on Media Production over 5G NPN Systems
- **TR 26.942** (Rel-19) — Study on Media Energy Consumption Exposure & Evaluation
- **TS 28.557** (Rel-19) — Management of Non-Public Networks (NPN)
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- **TR 28.807** (Rel-17) — Study on NPN Management
- **TR 28.843** (Rel-18) — Technical Report on Charging Aspects for Vertical Scenarios
- **TR 28.907** (Rel-19) — Enhanced Management of Non-Public Networks
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 32.255** (Rel-20) — Telecom Management; Charging for 5G Data Connectivity
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [NPN na 3GPP Explorer](https://3gpp-explorer.com/glossary/npn/)
