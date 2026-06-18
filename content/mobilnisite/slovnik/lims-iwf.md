---
slug: "lims-iwf"
url: "/mobilnisite/slovnik/lims-iwf/"
type: "slovnik"
title: "LIMS-IWF – Location IMS – Interworking Function"
date: 2025-01-01
abbr: "LIMS-IWF"
fullName: "Location IMS – Interworking Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lims-iwf/"
summary: "Síťová funkce, která umožňuje služby určení polohy pro tísňová volání v IMS. Funguje jako zprostředkovatel mezi jádrem IP Multimedia Subsystem (IMS) a systémem určení polohy (GMLC) podkladové mobilní"
---

LIMS-IWF je síťová funkce, která umožňuje služby určení polohy pro tísňová volání v IMS tím, že zprostředkovává komunikaci mezi jádrem IMS a systémem určení polohy mobilní sítě, aby poskytla polohu volajícího záchranným složkám.

## Popis

Location IMS – Interworking Function (LIMS-IWF) je klíčová funkční entita definovaná ve specifikacích 3GPP pro umožnění služeb určení polohy ([LCS](/mobilnisite/slovnik/lcs/)) v rámci IP Multimedia Subsystem (IMS), zejména pro scénáře tísňových volání. Nachází se v architektuře sítě IMS a slouží jako protokolová brána a služební prvek. Když je iniciováno tísňové volání v IMS (např. prostřednictvím [SIP](/mobilnisite/slovnik/sip/) INVITE směrovaného na službu identifikace tísňového volání), síť IMS toto volání identifikuje jako tísňovou relaci. LIMS-IWF je poté aktivován, aby získal polohu volajícího. Jeho primární role spočívá ve vzájemném propojení mezi signalizační rovinou IMS, která používá Session Initiation Protocol (SIP) a jeho rozšíření, a infrastrukturou pro určení polohy legacy okruhově nebo paketově spínané mobilní sítě, která typicky používá Mobile Location Protocol ([MLP](/mobilnisite/slovnik/mlp/)) ke komunikaci s Gateway Mobile Location Center ([GMLC](/mobilnisite/slovnik/gmlc/)). LIMS-IWF přijímá požadavek na určení polohy spuštěný signalizací IMS, který často obsahuje veřejnou uživatelskou identitu IMS ([IMPU](/mobilnisite/slovnik/impu/)). Poté tuto identitu namapuje na odpovídající identifikátor mobilní sítě (jako je [MSISDN](/mobilnisite/slovnik/msisdn/) nebo [IMSI](/mobilnisite/slovnik/imsi/)), vytvoří standardizovaný MLP požadavek (např. Emergency Location Immediate Request – ELIR) a odešle jej příslušnému GMLC. Po obdržení odhadu polohy (geodetické nebo občanské) od GMLC LIMS-IWF přeloží tento údaj do formátu vhodného pro IMS, jako je [PIDF-LO](/mobilnisite/slovnik/pidf-lo/) (Presence Information Data Format Location Object), a doručí jej do jádra IMS pro směrování tísňového volání ke správnému přijímacímu středisku tísňového volání (PSAP). Toto bezproblémové překládání je klíčové pro splnění regulatorních požadavků na určení polohy volajícího při tísňovém volání v sítích nové generace.

## K čemu slouží

LIMS-IWF byl vyvinut k vyřešení zásadní nekompatibility mezi vznikající architekturou sítě IMS založenou čistě na IP a stávající infrastrukturou služeb určení polohy navrženou pro okruhově a paketově spínané sítě GSM/UMTS. Když operátoři začali nasazovat IMS pro hlasové a multimediální služby, objevil se kritický problém: jak poskytnout přesnou polohu volajícího pro tísňová volání založená na IMS (jako VoIP 911), když tradiční mechanismy určení polohy spoléhaly na protokoly a rozhraní, která nejsou nativně podporována v jádru IMS založeném na SIP. Bez LIMS-IWF by sítě IMS nebyly schopny využít zavedené síťové možnosti určení polohy (např. Cell-ID, OTDOA, A-GPS), které již byly nasazeny v rádiovém přístupu a jádru sítě. Jeho vytvoření bylo motivováno přísnými regulatorními požadavky (např. pravidly FCC pro E911), které nařizují poskytnutí informace o poloze s tísňovými voláními bez ohledu na podkladovou technologii (okruhově spínanou, paketově spínanou nebo IMS). LIMS-IWF překlenuje tuto technologickou propast, umožňuje operátorům znovu využít jejich stávající infrastrukturu GMLC a určení polohy při migraci na IMS, zajišťuje tak regulatorní shodu, chrání bezpečnost účastníků a vyhýbá se potřebě nákladného paralelního systému určení polohy pro IMS.

## Klíčové vlastnosti

- Protokolové vzájemné propojení mezi signalizací IMS/SIP a legacy Mobile Location Protocol (MLP)
- Mapování identity z veřejné uživatelské identity IMS (IMPU) na mobilní identifikátory (MSISDN, IMSI)
- Podpora požadavku Emergency Location Immediate Request (ELIR) pro tísňová volání v IMS
- Převod dat o poloze z GMLC do formátů kompatibilních s IMS, jako je PIDF-LO
- Integrace s mechanizmy spouštění služeb v IMS pro detekci tísňových relací
- Umožňuje opětovné využití stávající síťové infrastruktury pro určení polohy (GMLC, LMU) pro služby IMS

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [MLP – Mobile Location Protocol](/mobilnisite/slovnik/mlp/)
- [PIDF-LO – Presence Information Data Format Location Object](/mobilnisite/slovnik/pidf-lo/)
- [PSAP – Public Safety Answering Point](/mobilnisite/slovnik/psap/)
- [E-CSCF – Emergency – Call Session Control Function](/mobilnisite/slovnik/e-cscf/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [LIMS-IWF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lims-iwf/)
