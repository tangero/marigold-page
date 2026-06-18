---
slug: "5gc"
url: "/mobilnisite/slovnik/5gc/"
type: "slovnik"
title: "5GC – 5G Core Network"
date: 2026-01-01
abbr: "5GC"
fullName: "5G Core Network"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5gc/"
summary: "Síť 5G Core je centrální částí systému 5G, postavenou na cloud-native, službami řízené architektuře (service-based architecture). Poskytuje vylepšené mobilní širokopásmové připojení, ultraspolehlivou"
---

5GC je cloud-native, službami řízená centrální část systému 5G, která umožňuje vylepšené mobilní širokopásmové připojení, ultraspolehlivou komunikaci s nízkou latencí, komunikaci s obrovským množstvím strojových zařízení, dělení sítě (network slicing) a výpočty na okraji sítě (edge computing).

## Popis

Síť 5G Core (5GC) je základní řídicí a spojovací rámec definovaný standardy 3GPP pro systémy 5G, který nahrazuje Evolved Packet Core (EPC). Je navržena jako architektura řízená službami (Service-Based Architecture, [SBA](/mobilnisite/slovnik/sba/)), kde síťové funkce (NFs) jsou modulární softwarové entity, které vystavují své schopnosti jako služby prostřednictvím dobře definovaných rozhraní, primárně využívající [HTTP](/mobilnisite/slovnik/http/)/2 a [JSON](/mobilnisite/slovnik/json/). Tento cloud-native návrh, využívající koncepty jako bezestavovost, mikroslužby a kontejnerizace, umožňuje flexibilní nasazení, škálování a správu životního cyklu nezávisle na hardwaru. 5GC fyzicky odděluje uživatelskou rovinu ([UP](/mobilnisite/slovnik/up/)) a řídicí rovinu ([CP](/mobilnisite/slovnik/cp/)), což umožňuje nasazení distribuovaných funkcí uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) na okraji sítě pro služby s nízkou latencí, zatímco řídicí funkce jsou centralizované.

Klíčové funkční komponenty zahrnují funkci pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)), která zpracovává připojení a správu mobility; funkci pro správu relací ([SMF](/mobilnisite/slovnik/smf/)), odpovědnou za zřizování, modifikaci a ukončení relací; a funkci uživatelské roviny (UPF), která představuje ukotvovací bod pro směrování dat, prověřování paketů a vynucování kvality služeb (QoS). Mezi další kritické funkce patří autentizační serverová funkce (AUSF) a Unified Data Management (UDM) pro zabezpečení a předplatitelská data, funkce pro řízení politik (PCF) pro správu politik a funkce úložiště síťových služeb (NRF) pro zjišťování služeb v rámci SBA. Funkce pro vystavení síťových schopností (NEF) bezpečně vystavuje síťové schopnosti externím aplikacím.

5GC pracuje tak, že zřizuje jednotku protokolových dat (PDU) Session, což je logické spojení mezi uživatelským zařízením (UE) a konkrétní datovou sítí (DN), jako je internet nebo podniková síť. Během počáteční registrace UE interaguje s AMF a AUSF/UDM za účelem autentizace. Pro zřízení relace SMF, po konzultaci s PCF, vybere UPF a nastaví potřebná pravidla pro rozhraní N4 pro zpracování provozu. Pakety uživatelských dat pak proudí mezi UE (přes rádiovou přístupovou síť) a DN prostřednictvím UPF, přičemž SMF spravuje stav relace a AMF zpracovává události mobility, jako jsou předání spojení (handover). Tato architektura podporuje souběžný přístup k více datovým sítím a více PDU relacím různých typů (např. IPv4, IPv6, Ethernet, nestrukturované).

Stěžejní schopností 5GC je nativní podpora dělení sítě (Network Slicing). Umožňuje vytvoření více logických, koncových sítí na společné fyzické infrastruktuře, z nichž každá je přizpůsobena konkrétním charakteristikám (např. šířka pásma, latence) pro různé typy služeb, jako je vylepšené mobilní širokopásmové připojení (eMBB), ultraspolehlivá komunikace s nízkou latencí (URLLC) nebo IoT s obrovským množstvím zařízení. 5GC identifikuje řez sítě pomocí Single Network Slice Selection Assistance Information (S-NSSAI) a zajišťuje, že PDU relace UE je asociována se správnou instancí řezu, s vyhrazenými prostředky AMF, SMF a UPF podle potřeby. Architektura 5GC navíc integruje podporu pro výpočty na okraji sítě (Edge Computing), což umožňuje aplikačním funkcím ovlivňovat směrování provozu (např. prostřednictvím výběru lokální datové sítě nebo UPF) pro splnění přísných požadavků na latenci.

## K čemu slouží

5GC byla vytvořena, aby řešila omezení předchozího Evolved Packet Core (EPC) pro 4G a aby splnila rozmanité a náročné požadavky služeb 5G podle vize IMT-2020. EPC, navržené primárně pro mobilní širokopásmové připojení, byla monolitickou, na hardware orientovanou architekturou s těsným propojením mezi síťovými funkcemi, což ji činilo nepružnou a nákladnou na škálování nebo inovace. Exploze připojených zařízení (IoT), potřeba průmyslové automatizace s ultranízkou latencí a poptávka po imerzivních zážitcích, jako je AR/VR, vyžadovaly agilnější, efektivnější a programovatelnou základní síť (core network).

Historicky každá generace mobilních sítí přinesla novou základní síť (např. circuit-switched core pro GSM, packet-switched core pro UMTS, EPC pro 4G). Přechod na 5G představoval příležitost pro radikální přepracování architektury. Hlavními motivacemi bylo dosažení větší flexibility prostřednictvím softwarových, cloud-native principů; umožnění efektivní podpory široké škály služeb prostřednictvím dělení sítě (network slicing); a snížení provozních nákladů prostřednictvím automatizace a škálovatelnosti. 5GC řeší tyto problémy oddělením softwaru od hardwaru, oddělením uživatelské a řídicí roviny pro nezávislou optimalizaci a zavedením modelu rozhraní řízeného službami, který zjednodušuje integraci a umožňuje rychlejší nasazení nových funkcí. Je to základní prvek, který umožňuje, aby 5G bylo víc než jen rychlejší mobilní širokopásmové připojení, a proměňuje ho v platformu pro vertikální průmyslové sektory a nové obchodní modely.

## Klíčové vlastnosti

- Architektura řízená službami (SBA) s rozhraními HTTP/2
- Oddělení řídicí a uživatelské roviny (CUPS) pro flexibilní nasazení
- Nativní podpora dělení sítě (Network Slicing) prostřednictvím S-NSSAI
- Integrovaná podpora výpočtů na okraji sítě (Edge Computing) a lokálního přerušení toku (Local Breakout)
- Principy cloud-native návrhu (bezestavové NFs, mikroslužby)
- Souběžné více typů PDU relací (IP, Ethernet, nestrukturované)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.830** (Rel-16) — Business Role Models for Network Slicing
- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 23.380** (Rel-19) — IMS Restoration Procedures
- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.732** (Rel-16) — User Data Interworking, Coexistence, Migration Study
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TR 23.758** (Rel-17) — Study on Edge Application Architecture
- **TR 23.783** (Rel-18) — Technical Report on Mission Critical Services over 5GS
- **TR 23.794** (Rel-17) — Study on enhanced IMS to 5GC integration
- **TR 23.973** (Rel-19) — Separate HSS/UDM Deployment Scenarios & Solutions
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- … a dalších 66 specifikací

---

📖 **Anglický originál a plná specifikace:** [5GC na 3GPP Explorer](https://3gpp-explorer.com/glossary/5gc/)
