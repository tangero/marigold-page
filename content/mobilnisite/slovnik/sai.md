---
slug: "sai"
url: "/mobilnisite/slovnik/sai/"
type: "slovnik"
title: "SAI – Service Area Identifier"
date: 2026-01-01
abbr: "SAI"
fullName: "Service Area Identifier"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sai/"
summary: "Jedinečný identifikátor pro servisní oblast, což je skupina buněk v rámci lokální oblasti. Používá se v sítích UMTS a LTE pro služby založené na poloze, optimalizaci pagingu a správu mobility. SAI umo"
---

SAI (identifikátor servisní oblasti) je jedinečný identifikátor pro skupinu buněk v rámci lokální oblasti, používaný v sítích UMTS a LTE pro služby založené na poloze, optimalizaci pagingu a správu mobility.

## Popis

Service Area Identifier (SAI) je základní koncept v sítích 3GPP, definovaný v architekturách UMTS Terrestrial Radio Access Network ([UTRAN](/mobilnisite/slovnik/utran/)) a Evolved UTRAN ([E-UTRAN](/mobilnisite/slovnik/e-utran/)). Jedná se o strukturovaný identifikátor, který jednoznačně reprezentuje servisní oblast, což je logické seskupení jedné nebo více buněk. SAI je tvořen z Mobile Country Code ([MCC](/mobilnisite/slovnik/mcc/)), Mobile Network Code ([MNC](/mobilnisite/slovnik/mnc/)), Location Area Code ([LAC](/mobilnisite/slovnik/lac/)) a Service Area Code ([SAC](/mobilnisite/slovnik/sac/)). Tato hierarchická struktura mu zajišťuje globální jedinečnost a vnoření do širší Lokální oblasti ([LA](/mobilnisite/slovnik/la/)) a Public Land Mobile Network ([PLMN](/mobilnisite/slovnik/plmn/)). SAI primárně používá Core Network (CN), konkrétně Mobility Management Entity (MME) v LTE nebo Serving GPRS Support Node (SGSN) v UMTS/GPRS, pro správu polohy a spouštění služeb.

Provozně hraje SAI klíčovou roli v procedurách správy mobility. Když se User Equipment (UE) pohybuje a provádí aktualizaci polohy, může síti nahlásit svou aktuální servisní oblast. To síti umožňuje sledovat polohu UE s jemnější granularitou než pouze na úrovni Lokální oblasti, což vede k efektivnějšímu pagingu. Namísto pagingu celé LA může síť cílit na konkrétní servisní oblast, kde bylo UE naposledy evidováno, což výrazně snižuje signalizační zátěž a latenci pagingu. SAI je komunikován mezi Radio Access Network (RAN) a Core Network prostřednictvím protokolů jako Radio Access Network Application Part (RANAP) v UMTS a S1 Application Protocol (S1AP) v LTE.

Kromě mobility je SAI klíčovým prvkem pro služby založené na poloze (LBS) a regulační funkce. Poskytovatelé služeb mohou použít SAI k určení přibližné polohy účastníka pro služby jako lokalizovaná reklama, nouzová upozornění nebo zákonný odposlech. V kontextu CAMEL (Customised Applications for Mobile networks Enhanced Logic) nebo jiných služeb inteligentní sítě může SAI sloužit jako spouštěcí bod pro vykonání servisní logiky. Jeho definice v četných specifikacích 3GPP, od protokolů core networku po požadavky na služby, podtrhuje jeho nedílnou roli v síťové architektuře, poskytujíc stabilní a standardizovaný referenční bod pro oblastní funkčnosti napříč více generacemi systémů 3GPP.

## K čemu slouží

Service Area Identifier byl zaveden, aby řešil potřebu jemnějšího sledování polohy, než jaké poskytoval Location Area Identifier (LAI). V raných sítích GSM byl LAI primární jednotkou pro registraci polohy a paging. Paging celé Lokální oblasti, která mohla obsahovat stovky buněk, generoval značný signalizační provoz a mohl vést k neefektivní spotřebě baterie v UE kvůli častému naslouchání. SAI byl vytvořen, aby rozdělil Lokální oblast na menší, řiditelné servisní oblasti.

Toto rozdělení řeší problém přetížení pagingu tím, že síti umožňuje paging pouze buněk v konkrétní servisní oblasti, kde se UE pravděpodobně nachází. Tato optimalizace snižuje signalizaci mezi core networkem a RAN, omezuje zahlcení pagingového kanálu a urychluje dobu navázání hovoru. Dále umožňuje síti nabízet pokročilé služby závislé na oblasti. Například diferencované účtování, doručování obsahu na základě polohy a plnění geografických regulačních požadavků jsou závislé na schopnosti určit polohu uživatele na konkrétní servisní oblast.

Návrh SAI jako hierarchického identifikátoru v rámci struktury PLMN a LA zajišťuje zpětnou kompatibilitu a bezproblémovou integraci s existujícími paradigmaty správy mobility. Poskytl mechanismus připravený na budoucnost, který byl zachován od UMTS (3G) přes LTE (4G) až do systémů 5G pro určité scénáře vzájemného propojení, což demonstruje jeho účinnost jako základního konceptu pro efektivní správu síťových zdrojů a vylepšené servisní schopnosti.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor složený z MCC, MNC, LAC a SAC
- Umožňuje jemné sledování polohy v rámci Lokální oblasti
- Optimalizuje procedury pagingu ke snížení signalizační zátěže
- Slouží jako spouštěč pro služby založené na poloze (LBS)
- Používá se v správě mobility mezi RAN a Core Network
- Podporován napříč architekturami UMTS (UTRAN) a LTE (E-UTRAN)

## Definující specifikace

- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.216** (Rel-19) — SRVCC Architecture Enhancements
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.479** (Rel-19) — MBMS API for Mission Critical Services
- **TS 23.792** (Rel-16) — MBMS API for Mission Critical Services
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.281** (Rel-19) — MCVideo Signalling Control Specification
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.334** (Rel-19) — ProSe Protocols and Procedures
- **TS 24.379** (Rel-19) — Mission Critical Push To Talk (MCPTT) call control
- … a dalších 13 specifikací

---

📖 **Anglický originál a plná specifikace:** [SAI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sai/)
