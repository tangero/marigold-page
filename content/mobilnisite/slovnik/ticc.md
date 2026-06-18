---
slug: "ticc"
url: "/mobilnisite/slovnik/ticc/"
type: "slovnik"
title: "TICC – Transport Independent Call Control"
date: 2025-01-01
abbr: "TICC"
fullName: "Transport Independent Call Control"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ticc/"
summary: "Transport Independent Call Control (TICC) je architektura a protokolový rámec 3GPP, který odděluje logiku řízení hovoru od podkladové transportní technologie. Umožňuje vytváření a správu multimediální"
---

TICC je architektura a protokolový rámec 3GPP, který odděluje řízení hovoru od transportní technologie, aby umožnil správu multimediálních relací napříč různými IP a okruhově přepínanými sítěmi.

## Popis

Transport Independent Call Control (TICC) je klíčový architektonický princip a protokolový rámec definovaný v 3GPP TS 23.153. Jeho základní návrh odděluje řízení hovoru a servisní logiku od konkrétních detailů podkladové transportní sítě, ať už je založená na IP (jako IMS) nebo tradiční okruhově přepínané. Toho je dosaženo vrstveným přístupem, kde vrstva řízení hovoru spravuje stav a signalizaci pro multimediální relace, zatímco transportní vrstva zajišťuje vlastní vytváření přenosových kanálů a tok médií. Mezi klíčové komponenty patří Call State Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) v IMS pro řízení IP transportu a Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) pro propojení s okruhově přepínanými doménami. TICC využívá a rozšiřuje Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) jako svůj primární signalizační protokol pro navazování, modifikaci a ukončování relací. Definuje, jak se SIP zprávy mapují na jiné signalizační systémy, jako je [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo Bearer Independent Call Control (BICC), a z nich, aby zajistil bezproblémové poskytování služeb napříč heterogenními sítěmi. Tento rámec je zásadní pro umožnění konvergence pevných a mobilních sítí, což dovoluje službám jako Voice over LTE (VoLTE) interoperabilitu s legacy sítěmi [PSTN](/mobilnisite/slovnik/pstn/)/[PLMN](/mobilnisite/slovnik/plmn/).

## K čemu slouží

TICC byl vyvinut, aby řešil výzvu síťové evoluce a konvergence. Tradiční telekomunikace byly postaveny na okruhově přepínaných sítích s těsně integrovaným řízením hovoru a transportem. Nástup paketově přepínaných IP sítí vytvořil potřebu podporovat stávající telefonní služby na nové infrastruktuře bez úplné a okamžité přestavby. TICC to řeší tím, že poskytuje jednotný model řízení hovoru, který je agnostický vůči transportní vrstvě. To umožňuje síťovým operátorům zavádět IP jádrové sítě (jako IMS) postupně, při zachování interoperability s rozsáhlou instalovanou základnou okruhově přepínaných zařízení a účastníků. Motivací bylo snížení provozních nákladů, umožnění nových multimediálních služeb a vytvoření architektury odolné vůči budoucím změnám. Oddělením řízení od transportu TICC usnadňuje zavádění nových přístupových technologií (např. LTE, 5G NR) a transportních mechanismů bez nutnosti zásadních změn servisní logiky, čímž chrání investice a urychluje inovace.

## Klíčové vlastnosti

- Odděluje logiku řízení hovoru/relace od podkladové transportní technologie
- Využívá SIP jako primární signalizační protokol pro řízení relace
- Definuje funkce pro vzájemné propojení (např. MGCF) pro připojení k okruhově přepínaným sítím
- Podporuje protokol Bearer Independent Call Control (BICC) pro propojování tras (trunking)
- Umožňuje bezproblémovou konvergenci pevných a mobilních sítí (FMC)
- Poskytuje základ pro služby založené na IMS, jako jsou VoLTE a ViLTE

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [MGCF – Media Gateway Control Function](/mobilnisite/slovnik/mgcf/)
- [CSFB – Circuit Switched Fallback](/mobilnisite/slovnik/csfb/)

## Definující specifikace

- **TS 23.153** (Rel-19) — Out-of-Band Transcoder Control Stage 2

---

📖 **Anglický originál a plná specifikace:** [TICC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ticc/)
