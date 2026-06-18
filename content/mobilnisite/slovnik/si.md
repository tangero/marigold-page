---
slug: "si"
url: "/mobilnisite/slovnik/si/"
type: "slovnik"
title: "SI – Service Interface"
date: 2025-01-01
abbr: "SI"
fullName: "Service Interface"
category: "Interface"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/si/"
summary: "Standardizovaná předpona používaná k označení metod třídy rozhraní ve specifikacích 3GPP. Poskytuje jednotnou konvenci pojmenování pro rozhraní služeb (service-based interfaces), usnadňuje interoperab"
---

SI je standardizovaná předpona používaná ve specifikacích 3GPP k označení metod třídy rozhraní služeb (service-based interface), která poskytuje jednotnou konvenci pojmenování pro jasné architektonické definice a interoperabilitu mezi síťovými funkcemi.

## Popis

Rozhraní služeb (Service Interface, SI) není jediné fyzické nebo logické rozhraní, ale kritická konvence pojmenování a konceptuální předpona hojně používaná napříč technickými specifikacemi 3GPP. Označuje třídu metod nebo operací, které vystavuje síťová funkce ([NF](/mobilnisite/slovnik/nf/)), aby umožnila interakce založené na službách v rámci systémové architektury 3GPP. Tato předpona se aplikuje na definice rozhraní, zejména v kontextu architektury založené na službách (Service-Based Architecture, [SBA](/mobilnisite/slovnik/sba/)) používané od 5G Core (5GC) dále, ale její konceptuální použití sahá až k dřívějším vydáním. Když specifikace odkazuje na rozhraní jako Nnrf_NFManagement, část 'Nnrf' označuje síťovou funkci ([NRF](/mobilnisite/slovnik/nrf/)) a metody v rámci tohoto rozhraní by byly popsány pomocí konvence SI pro definici servisních operací, jako je NFRegister, NFUpdate atd.

Architektonicky koncept SI podporuje přechod od tradičních bod-bod referenčních rozhraní k flexibilnějšímu, webovému modelu založenému na službách. V tomto modelu síťové funkce jako [AMF](/mobilnisite/slovnik/amf/), [SMF](/mobilnisite/slovnik/smf/) nebo [UDM](/mobilnisite/slovnik/udm/) poskytují sadu služeb a další autorizované NF mohou tyto služeby objevovat a vyvolávat. Předpona SI pomáhá kategorizovat a standardizovat pojmenování těchto servisních operací. Například všechny servisní operace související s konkrétní službou NF (např. služba Nudm_UEContextManagement poskytovaná UDM) budou sdílet společnou předponu, což zajišťuje jasnost a konzistenci napříč tisíci stránkami specifikací.

Její role je zásadní pro návrh protokolů, zejména pro rozhraní jako N1, [N2](/mobilnisite/slovnik/n2/) a různá rozhraní Nx v 5GC. Specifikace (např. řada TS 29.5xx) definují tato rozhraní služeb pomocí OpenAPI definic, kde je konvence pojmenování SI důsledně aplikována na každý koncový bod [API](/mobilnisite/slovnik/api/) a operaci. Tato standardizace je klíčová pro výrobce zařízení a vývojáře softwaru, aby vytvářeli interoperabilní produkty. Zajišťuje, že 'NF Service Consumer' přesně rozumí, jak požádat o službu od 'NF Service Producer', bez ohledu na implementaci od konkrétního dodavatele, tím, že dodržuje názvy metod a datové struktury definované pomocí konvence SI.

Z provozní perspektivy použití SI usnadňuje virtualizaci síťových funkcí (NFV) a principy cloud-nativního přístupu. Definováním jasných, spotřebitelných rozhraní služeb mohou být síťové funkce vyvíjeny, nasazovány a škálovány nezávisle. Systémy pro správu a orchestraci, včetně Network Repository Function (NRF), spoléhají na přesnou definici těchto služeb s předponou SI k provádění objevování služeb. Síťová funkce zaregistruje své schopnosti (seznam podporovaných instancí služeb, každá se specifickými metodami SI) u NRF, což umožňuje dalším funkcím je dynamicky nalézat a k nim se vázat, a tím umožňuje agilnější a automatizovanější síť.

## K čemu slouží

Koncept Rozhraní služeb (SI) byl vytvořen, aby řešil rostoucí složitost a rigiditu architektur telekomunikačních sítí. V systémech před 5G (jako 4G EPC) byla rozhraní definována jako statické referenční body (např. S1, S6a, S11) s protokoly typu bod-bod. Tento model se stal úzkým hrdlem pro inovace, protože zavedení nové funkce nebo síťové funkce často vyžadovalo definici nových, specifických rozhraní, což vedlo k rozrůstání protokolů a problémům s integrací. Paradigma SI, vyvíjející se napříč vydáními 3GPP, mělo za cíl zavést modulárnější a softwarově orientovaný přístup.

Primární problém, který řeší, je nedostatek flexibility a škálovatelnosti v návrhu sítě. Přijetím modelu založeného na službách se standardizovaným pojmenováním rozhraní (předpona SI) umožnilo 3GPP oddělenou architekturu, kde síťové funkce vystavují své schopnosti jako znovupoužitelné služby. Tento posun byl motivován celoprůmyslovým přechodem k cloud-nativním technologiím, mikroslužbám a praktikám DevOps. Historický kontext zahrnuje vývoj architektury založené na službách (SBA) 3GPP jako klíčového pilíře 5G systému (5GS), kde se koncept SI formálně zakořenil. Odstraňuje omezení předchozího bod-bod přístupu tím, že umožňuje snadnější zavádění nových služeb, zjednodušenou interakci síťových funkcí a podporu automatizované správy životního cyklu.

Dále konvence SI poskytuje zásadní sémantickou jasnost. V rozsáhlém ekosystému specifikací vyvíjených různými pracovními skupinami zajišťuje jednotné pravidlo pro pojmenování servisních operací prevenci nejednoznačnosti a to, že inženýři a vývojáři mohou okamžitě identifikovat rozsah a poskytovatele dané metody rozhraní. Nejde jen o triviální cvičení v pojmenování; je to základní prvek pro dosažení skutečné interoperability v multi-vendor, softwarově definovaných 5G sítích. Zajišťuje budoucí odolnost architektury tím, že umožňuje bezproblémovou integraci nových služeb dodržováním zavedených vzorů pojmenování a návrhu.

## Klíčové vlastnosti

- Standardizovaná předpona pro pojmenování metod rozhraní služeb napříč specifikacemi 3GPP.
- Umožňuje jasnou definici servisních operací poskytovaných síťovými funkcemi (NF).
- Základní pro architekturu založenou na službách (SBA) v sítích 5G Core.
- Usnadňuje automatizované objevování služeb a vazbu prostřednictvím Network Repository Function (NRF).
- Podporuje definici nezávislou na protokolu, běžně realizovanou pomocí HTTP/2 a JSON.
- Podporuje interoperabilitu tím, že poskytuje konzistentní model pro spotřebitele a producenty služeb NF.

## Související pojmy

- [NRF – Network Resource Fulfilment](/mobilnisite/slovnik/nrf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TS 25.800** (Rel-12) — UMTS Heterogeneous Networks Study
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 32.843** (Rel-13) — PS Domain Online Charging in Roaming
- **TS 32.863** (Rel-13) — PM Measurement Metadata Definition
- **TS 33.831** (Rel-12) — Study on Spoofed Call Detection & Prevention
- **TS 36.133** (Rel-19) — E-UTRA RRM Requirements
- … a dalších 12 specifikací

---

📖 **Anglický originál a plná specifikace:** [SI na 3GPP Explorer](https://3gpp-explorer.com/glossary/si/)
