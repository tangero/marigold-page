---
slug: "sn"
url: "/mobilnisite/slovnik/sn/"
type: "slovnik"
title: "SN – Serving Network Identifier"
date: 2026-01-01
abbr: "SN"
fullName: "Serving Network Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sn/"
summary: "Identifikátor obslužné sítě (SN) je klíčový síťový identifikátor používaný v systémech 3GPP k jednoznačné identifikaci obslužné sítě, ke které je připojeno uživatelské zařízení (UE). Je nezbytný pro b"
---

SN (Serving Network Identifier) je identifikátor obslužné sítě, který jednoznačně identifikuje obslužnou síť, ke které je uživatelské zařízení (UE) připojeno v systémech 3GPP, a to pro účely zabezpečení, správy mobility a kontinuity služeb.

## Popis

Identifikátor obslužné sítě (SN) je základní parametr v architekturách 3GPP, který slouží jako jedinečný štítek pro síť, jež uživatelskému zařízení (UE) aktuálně poskytuje služby. Je vytvořen z mobilního kódu země ([MCC](/mobilnisite/slovnik/mcc/)) a mobilního kódu sítě ([MNC](/mobilnisite/slovnik/mnc/)) obslužné veřejné pozemní mobilní sítě ([PLMN](/mobilnisite/slovnik/plmn/)). Tento identifikátor není jen statický štítek; je dynamicky využíván sítí i UE během klíčových procedur. Například v procedurách autentizace a dohody o klíči ([AKA](/mobilnisite/slovnik/aka/)) je SN vstupem pro generování bezpečnostních klíčů, což zajišťuje, že bezpečnostní kontexty jsou vázány na konkrétní síť, což brání opětovnému použití klíčů v různých sítích a zvyšuje bezpečnost.

Z architektonického hlediska je SN využíván napříč více síťovými doménami. V jádru sítě jej používá entita správy mobility ([MME](/mobilnisite/slovnik/mme/)) v 4G nebo funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5G k identifikaci síťového kontextu pro UE. Je také signalizován mezi síťovými uzly, například mezi MME/AMF a domácím registrem účastníků ([HSS](/mobilnisite/slovnik/hss/)) nebo jednotnou správou dat ([UDM](/mobilnisite/slovnik/udm/)), během procedur jako je aktualizace polohy nebo autentizace. V rádiové přístupové síti, přestože není přímo používán v protokolech rozhraní vzduch, informace z něj odvozené ovlivňují výběr síťových řezů a sledovacích oblastí.

Role SN zasahuje do správy mobility, zejména při předávání spojení mezi různými PLMN. Pomáhá identifikovat cílovou síť a zajistit aplikaci správných síťových politik a bezpečnostních parametrů. Dále v scénářích sdílení sítě, kde více operátorů sdílí infrastrukturu rádiové přístupové sítě, SN pomáhá rozlišit jádrové sítě jednotlivých operátorů, což zajišťuje, že účastníci jsou správně asociováni se službami a fakturačními systémy svého domovského operátora. Jeho konzistentní používání od 3G až po 5G a dále podtrhuje jeho význam jako stabilního, základního prvku správy identit v systémech 3GPP.

## K čemu slouží

Identifikátor obslužné sítě (SN) byl vytvořen, aby řešil základní potřebu jednoznačné identifikace sítě v mobilní telekomunikaci. Jak se sítě vyvíjely od nasazení jediného operátora ke komplexním, víceoperátorským prostředím s roamováním a sdílením sítě, stalo se kriticky důležitým přesně identifikovat, která síť v daném okamžiku obsluhuje účastníka. Tato identifikace je nezbytná pro směrování signalizačních zpráv, aplikaci správných profilů účastníků a zajištění přesnosti zákonného odposlechu a fakturace.

Historicky, bez standardizovaného, jedinečného identifikátoru obslužné sítě, systémy čelily výzvám při zpracování mobility mezi PLMN a zabezpečením. SN tyto problémy řeší tím, že poskytuje konzistentní, standardizovaný způsob, jak odkazovat na obslužnou síť napříč všemi rozhraními a protokoly 3GPP. Umožňuje bezpečnostní architektuře, zejména protokolu autentizace a dohody o klíči (AKA), generovat síťově specifické klíče, čímž zmírňuje rizika jako jsou replay útoky napříč sítěmi. Jeho zavedení formalizovalo klíčový prvek dat, který byl implicitně potřebný, ale v raných mobilních systémech nebyl vždy explicitně standardizován, čímž se zlepšila interoperabilita a bezpečnost v nasazeních s více dodavateli a více operátory.

## Klíčové vlastnosti

- Jednoznačně identifikuje obslužnou PLMN pomocí MCC a MNC
- Kritický vstupní parametr pro bezpečnostní procedury 3GPP AKA
- Používá se při správě mobility pro předávání spojení mezi PLMN
- Podporuje scénáře sdílení sítě tím, že rozlišuje jádrové sítě
- Umožňuje správné směrování signalizace a uživatelských dat
- Konzistentně definován a používán od systémů 3G až po 5G

## Související pojmy

- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)
- [MCC – Mobile Country Code](/mobilnisite/slovnik/mcc/)
- [MNC – Mobile Network Code](/mobilnisite/slovnik/mnc/)
- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 21.133** (Rel-5) — 3G Security Requirements
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.105** (Rel-19) — Telecommunication Services Framework
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TR 22.975** (Rel-4) — UMTS Numbering and Addressing Requirements
- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks
- **TS 28.622** (Rel-20) — Telecommunication Management; Generic NRM Information Service
- … a dalších 26 specifikací

---

📖 **Anglický originál a plná specifikace:** [SN na 3GPP Explorer](https://3gpp-explorer.com/glossary/sn/)
