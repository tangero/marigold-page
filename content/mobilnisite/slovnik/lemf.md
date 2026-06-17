---
slug: "lemf"
url: "/mobilnisite/slovnik/lemf/"
type: "slovnik"
title: "LEMF – Law Enforcement Monitoring Facility"
date: 2025-01-01
abbr: "LEMF"
fullName: "Law Enforcement Monitoring Facility"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lemf/"
summary: "Standardizované, zabezpečené zařízení provozované orgány činnými v trestním řízení pro zákonný odposlech komunikací a souvisejících dat ze sítí 3GPP. Jedná se o autorizovaný koncový bod pro příjem odp"
---

LEMF je zabezpečené, standardizované zařízení provozované orgány činnými v trestním řízení za účelem zákonného příjmu odposlechnutých komunikací a dat ze sítí 3GPP jako autorizovaný koncový bod pro vyšetřování.

## Popis

Zařízení pro monitorování orgánů činných v trestním řízení (Law Enforcement Monitoring Facility, LEMF) je klíčovou součástí architektury zákonného odposlechu (Lawful Interception, [LI](/mobilnisite/slovnik/li/)) v rámci 3GPP, definovanou jako fyzické umístění nebo systém provozovaný orgánem činným v trestním řízení (Law Enforcement Agency, [LEA](/mobilnisite/slovnik/lea/)). Slouží jako zabezpečený, autorizovaný koncový bod pro veškerý odposlechnutý komunikační obsah (Communication Content, [CC](/mobilnisite/slovnik/cc/)) a odposlechnuté související informace (Intercepted Related Information, [IRI](/mobilnisite/slovnik/iri/)) doručované mediačními a doručovacími funkcemi operátora sítě. LEMF není součástí veřejné telekomunikační sítě, ale je k ní připojeno prostřednictvím standardizovaných, zabezpečených rozhraní (konkrétně rozhraní [HI2](/mobilnisite/slovnik/hi2/) a [HI3](/mobilnisite/slovnik/hi3/)) za účelem příjmu odposlechnutých dat. Jeho primární rolí je shromažďovat, ukládat, analyzovat a spravovat odposlechnutá data v souladu s národními zákonnými požadavky, čímž zajišťuje řetězec úschovy a důkazní integritu.

Z architektonického hlediska LEMF komunikuje s Administrativní funkcí (Administration Function, [ADMF](/mobilnisite/slovnik/admf/)) operátora sítě a s Mediačními a doručovacími funkcemi (Mediation and Delivery Functions, [DF2](/mobilnisite/slovnik/df2/) pro IRI a DF3 pro CC). ADMF, která je před LEMF skrytá, spravuje příkazy k odposlechu a aktivuje odposlechy na konkrétních cílech v síti. DF následně formátují a doručují datové proudy odposlechnutých dat na LEMF prostřednictvím předávacích rozhraní (Handover Interfaces, HI). Rozhraní HI2 doručuje IRI, která zahrnuje signalizační data o komunikaci (např. sestavení hovoru, poloha, účastníci), zatímco rozhraní HI3 doručuje samotný CC, jako jsou hlasové pakety nebo data uživatelské roviny. LEMF musí být schopno zabezpečeně přijímat, dešifrovat (pokud byl obsah pro zabezpečení přenosu přes předávací rozhraní zašifrován) a zpracovávat tyto standardizované datové formáty.

Vnitřní architektura LEMF je do značné míry specifická pro implementaci a řízená národními předpisy, ale její externí rozhraní k síti operátora jsou přísně standardizována 3GPP, aby byla zajištěna interoperabilita a konzistentní metoda zákonného přístupu napříč různými sítěmi a dodavateli. Typicky zahrnuje zabezpečené úložné systémy, analytické nástroje a řízení přístupu, aby bylo zajištěno, že odposlechnutá data mohou zobrazit pouze autorizovaní pracovníci. Provoz LEMF je z pohledu sítě zcela pasivní; neiniciuje odposlechy, ale pouze přijímá data, která mu systémy operátora sítě zasílají na základě zákonného pověření.

## K čemu slouží

LEMF bylo standardizováno, aby vyřešilo kritickou potřebu zabezpečeného, spolehlivého a zákonně konformního koncového bodu pro operace zákonného odposlechu v mobilních sítích. Jelikož se telekomunikace staly klíčovými pro legální i nelegální činnosti, vlády po celém světě přijaly zákony vyžadující, aby operátoři sítí poskytovali technické možnosti pro zákonný odposlech. Před standardizací byla rozhraní mezi sítěmi operátorů a systémy orgánů činných v trestním řízení často proprietární, což vedlo k vysokým nákladům, složitosti pro operátory obsluhující více LEA a potenciálním právním problémům týkajícím se integrity dat a řízení přístupu.

Vytvoření konceptu LEMF ve specifikacích 3GPP (počínaje Release 8) poskytlo jasný demarkační bod mezi odpovědnostmi operátora sítě a orgánu činného v trestním řízení. Toto oddělení je zásadní: operátor je odpovědný za implementaci odposlechu v síti a doručování standardizovaných datových proudů, zatímco LEA je odpovědná za zabezpečený příjem a zpracování těchto dat ve vlastním zařízení (LEMF). Tento model řeší problém zapojení operátora do samotné analýzy odposlechnutých dat, chrání soukromí uživatelů a neutralitu operátora a zároveň zajišťuje, že LEA obdrží informace, na které má zákonný nárok, ve konzistentním, auditovatelném formátu.

Standardizace LEMF a jeho předávacích rozhraní navíc umožňuje výrobcům zařízení vyrábět kompatibilní síťové prvky a umožňuje LEA pořizovat systémy správy odposlechů, které mohou spolupracovat s více operátory, a to jak vnitrostátními, tak mezinárodními. To je klíčové pro moderní vyšetřování, která mohou zahrnovat několik poskytovatelů služeb. Vývoj specifikací LEMF napříč releasy zajišťuje, že může zvládnout nové služby, jako jsou VoLTE, IMS a 5G, a udržovat tak schopnosti zákonného odposlechu s postupem síťových technologií.

## Klíčové vlastnosti

- Zabezpečený koncový bod pro datové proudy z předávacího rozhraní (HI2 a HI3)
- Přijímá a zpracovává standardizované odposlechnuté související informace (IRI)
- Přijímá a zpracovává standardizovaný komunikační obsah (CC)
- Zajišťuje řetězec úschovy a důkazní integritu pro odposlechnutá data
- Provozně oddělené od veřejné telekomunikační sítě
- Implementace řízená národními zákonnými a regulačními požadavky

## Související pojmy

- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)
- [ADMF – Administration Function](/mobilnisite/slovnik/admf/)

## Definující specifikace

- **TS 23.889** (Rel-10) — Local Call Local Switch Core Network Impact Study
- **TS 33.106** (Rel-19) — Lawful Interception Requirements (Pre-Rel-15)
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [LEMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lemf/)
