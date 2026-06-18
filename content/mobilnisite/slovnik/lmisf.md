---
slug: "lmisf"
url: "/mobilnisite/slovnik/lmisf/"
type: "slovnik"
title: "LMISF – LI Mirror IMS State Function"
date: 2025-01-01
abbr: "LMISF"
fullName: "LI Mirror IMS State Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lmisf/"
summary: "Funkce zákonného odposlechu (LI) zavedená ve 3GPP Release 14 pro IMS sítě. Zrcadlí informace o stavu registrace a sezení cílového uživatele z funkcí IMS jádra (jako jsou CSCF) do systému zákonného odp"
---

LMISF je funkce zákonného odposlechu, která zrcadlí stav registrace a sezení cílového uživatele v IMS z funkcí jádra sítě do odposlechového systému pro autorizované monitorování.

## Popis

[LI](/mobilnisite/slovnik/li/) Mirror IMS State Function (LMISF) je specializovaná funkční entita v architektuře zákonného odposlechu (LI) dle 3GPP pro sítě IP Multimedia Subsystem (IMS). Jejím hlavním úkolem je replikovat, neboli 'zrcadlit', informace o stavu registrace a sezení cílového uživatele (účastníka) z prvků IMS jádra do funkce správy zákonného odposlechu (LIMF) a následně do zařízení monitorování orgánů činných v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)). LMISF funguje jako zprostředkovatel, který shromažďuje informace související s odposlechem ([IRI](/mobilnisite/slovnik/iri/)) nesouvisející s obsahem, týkající se služeb IMS, jako jsou VoIP hovory, videosezení a zasílání zpráv přes IMS.

Architektonicky je LMISF typicky umístěna společně nebo úzce integrována s klíčovými funkcemi řízení IMS sezení ([CSCF](/mobilnisite/slovnik/cscf/)), konkrétně s Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) a potenciálně s Proxy-CSCF ([P-CSCF](/mobilnisite/slovnik/p-cscf/)). Rozhraní má interně s těmito CSCF, aby získala přístup k signalizačním tokům a stavovým automatům, které spravují registrace uživatelů, zahájení sezení (pomocí [SIP](/mobilnisite/slovnik/sip/) INVITE), změny sezení a ukončení sezení. LMISF sama neodposlouchává mediální obsah (hlasové, video pakety); tento úkol zajišťují jiné LI funkce, jako je Media Gateway nebo Packet Data Gateway. Místo toho se zaměřuje na signalizační metadata.

Provozně, když se cílový uživatel zaregistruje v IMS síti nebo naváže sezení, příslušná CSCF aktivuje LMISF. LMISF následně naformátuje tyto stavové informace do standardizovaných hlášení IRI, jak je definováno v 3GPP TS 33.107. Tato hlášení obsahují podrobnosti, jako je identita cíle (např. SIP [URI](/mobilnisite/slovnik/uri/)), identity komunikačních partnerů, časy začátku/konce sezení a typ vyvolané služby. Hlášení jsou doručována bezpečně přes Handover Interface (HI) k Administration Function (ADMF) a poté k LEMF. LMISF zajišťuje, že zrcadlený stav je přesný a včasný, a poskytuje tak orgánům činným v trestním řízení pohled na aktivitu cíle v IMS v reálném čase nebo téměř v reálném čase.

Návrh LMISF musí splňovat přísné požadavky na zabezpečení a integritu, aby zabránil neoprávněnému přístupu nebo manipulaci. Funguje pod kontrolou ADMF, která aktivuje odposlech na základě zákonného pověření. Její implementace je klíčová pro operátory, aby vyhověli národním předpisům pro zákonný odposlech u služeb nové generace, které jsou stále více založeny na plně IP platformách IMS, které nahrazují tradiční přepojování okruhů v telefonii.

## K čemu slouží

LMISF byla zavedena ve 3GPP Release 14 jako reakce na vývoj komunikačních služeb směrem k plně IP sítím založeným na IMS. Když operátoři nasazovali Voice over LTE (VoLTE), Voice over Wi-Fi (VoWiFi) a Rich Communication Services (RCS) využívající IMS, stávající řešení zákonného odposlechu navržená pro hlasové služby s přepojováním okruhů a služby paketových dat byla nedostatečná. Tato řešení nemohla snadno zachytit signalizační stav a informace o řízení sezení, které jsou vlastní protokolům IMS založeným na SIP.

Její vytvoření bylo motivováno regulačními požadavky po celém světě, které ukládají telekomunikačním operátorům povinnost poskytovat schopnosti zákonného odposlechu pro autorizované sledování. LMISF řeší problém, jak efektivně a spolehlivě extrahovat potřebné IRI ze složitého, stavového IMS jádra, aniž by to ovlivnilo výkon nebo škálovatelnost CSCF. Poskytuje standardizovanou, na dodavateli nezávislou metodu pro zrcadlení stavu IMS, což zajišťuje interoperabilitu mezi IMS a LI systémy různých dodavatelů.

Centralizací funkce zrcadlení stavu LMISF zjednodušuje LI architekturu pro IMS. Odstraňuje potřebu, aby si orgány činné v trestním řízení osvojily složité detaily IMS signalizace, protože LMISF je překládá do konzistentních hlášení IRI. Tento přístup zajišťuje budoucí použitelnost zákonného odposlechu, jak se sítě vyvíjejí směrem k 5G jádru, kde IMS pro hlas a zasílání zpráv zůstává klíčovou servisní vrstvou, a zaručuje tak kontinuální soulad s předpisy s postupem technologií.

## Klíčové vlastnosti

- Zrcadlí informace o stavu registrace a sezení v IMS (např. ze S-CSCF) pro cílového účastníka do systému LI.
- Generuje standardizovaná hlášení informací souvisejících s odposlechem (IRI) pro služby založené na IMS, jako jsou VoLTE a ViLTE.
- Má interní rozhraní s IMS CSCF pro monitorování signalizačních událostí SIP (REGISTER, INVITE, BYE).
- Doručuje hlášení IRI přes zabezpečené rozhraní Handover Interface (HI) k funkci správy zákonného odposlechu (LIMF).
- Funguje pod přísnou administrativní kontrolou prostřednictvím ADMF, což zajišťuje aktivaci pouze na základě zákonného oprávnění.
- Zaměřuje se na odposlech nesouvisející s obsahem (signalizace), čímž doplňuje funkce odposlechu obsahu v mediální cestě.

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [ADMF – Administration Function](/mobilnisite/slovnik/admf/)
- [IRI – Intercept Related Information](/mobilnisite/slovnik/iri/)

## Definující specifikace

- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.827** (Rel-14) — LI for S8 Home Routed VoLTE Roaming

---

📖 **Anglický originál a plná specifikace:** [LMISF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lmisf/)
