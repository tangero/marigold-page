---
slug: "ussi"
url: "/mobilnisite/slovnik/ussi/"
type: "slovnik"
title: "USSI – Unstructured Supplementary Service Data over IM CN subsystem"
date: 2025-01-01
abbr: "USSI"
fullName: "Unstructured Supplementary Service Data over IM CN subsystem"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ussi/"
summary: "Evoluce USSD, která umožňuje přenos relací nestrukturovaných doplňkových služeb (Unstructured Supplementary Services Data) přes IP jádrovou síť IMS (IP Multimedia Subsystem). Umožňuje interaktivní slu"
---

USSI je evolucí USSD, která přenáší relace nestrukturovaných doplňkových služeb (Unstructured Supplementary Service Data) přes IP jádrovou síť IMS, což umožňuje uživatelům v sítích LTE nebo 5G využívat interaktivní služby ve stylu USSD.

## Popis

Unstructured Supplementary Service Data over [IM](/mobilnisite/slovnik/im/) CN subsystem (USSI) je standard 3GPP, který přizpůsobuje starší službu [USSD](/mobilnisite/slovnik/ussd/) pro provoz v rámci jádrové sítě IP Multimedia Subsystem (IMS). Definuje mechanismy pro navázání a správu USSD relací pomocí protokolů IMS (především [SIP](/mobilnisite/slovnik/sip/) a [MSRP](/mobilnisite/slovnik/msrp/)) namísto spoléhání se na tradiční signalizaci v přepojování okruhů ([MAP](/mobilnisite/slovnik/map/) přes [SS7](/mobilnisite/slovnik/ss7/)). V této architektuře funguje uživatelské zařízení (UE) jako USSI klient. Když uživatel zadá USSD řetězec (např. *123#), UE jej neodesílá prostřednictvím tradiční signalizace [NAS](/mobilnisite/slovnik/nas/) k [MSC](/mobilnisite/slovnik/msc/). Místo toho zapouzdří USSD informaci do požadavku SIP MESSAGE nebo naváže SIP relaci s MSRP (Message Session Relay Protocol) pro dialog orientovaný na relaci a odešle ji do jádra IMS.

Klíčovou síťovou funkcí pro USSI je aplikační server USSI (USSI AS) umístěný v doméně IMS. Jádro IMS (zahrnující P-CSCF, I-CSCF, S-CSCF) směruje SIP požadavek obsahující USSD datovou část k USSI AS na základě počátečních filtračních kritérií (iFC) v profilu služeb uživatele. USSI AS interpretuje USSD řetězec. Může obsahovat vlastní aplikační logiku nebo, častěji, funguje jako brána/funkce pro vzájemné propojení. V druhém případě překládá zprávy SIP/MSRP do staršího formátu MAP/USSD a komunikuje s tradičním USSD servisním centrem v doméně přepojování okruhů přes Interworking MRF (IM-MRF) nebo přímo přes rozhraní pro vzájemné propojení. Odpověď z aplikační logiky se vrací zpět k UE stejnou cestou a zobrazí se jako USSD odpověď.

USSI podporuje dva režimy provozu: relací orientovaný (session-based) a transakčně orientovaný (transaction-based). Režim orientovaný na relaci používá SIP INVITE k navázání relace a MSRP pro výměnu více USSD zpráv v rámci této relace, čímž napodobuje klasický interaktivní zážitek s USSD menu. Transakčně orientovaný režim používá jednu výměnu požadavek-odpověď typu SIP MESSAGE pro jednoduché jednorázové dotazy. To poskytuje flexibilitu v závislosti na složitosti služby. Detaily protokolu pro přenos USSD datové části jsou specifikovány v hlavičkách SIP a formátech těla zprávy. Role USSI je klíčová pro kontinuitu služeb, protože umožňuje operátorům vyřadit starší jádra pro přepojování okruhů, a přitom zachovat výnosné a nezbytné služby založené na USSD pro účastníky na čistě IP přístupu, jako je VoLTE, VoWiFi nebo v budoucnu 5G Voice (VoNR).

## K čemu slouží

USSI bylo vytvořeno k řešení problému kontinuity služby USSD v měnícím se prostředí mobilních sítí směřujících k plně IP architekturám, konkrétně s nasazením IMS pro multimediální služby. Když operátoři spouštěli LTE (které zpočátku postrádalo jádro pro přepojování okruhů pro hlas) a přijali IMS pro Voice over LTE (VoLTE), tradiční USSD služby závislé na signalizaci MAP přes MSC/VLR se staly pro uživatele připojené k LTE nedostupné. Vznikla tak služební mezera, kdy účastníci nemohli přistupovat ke kritickým službám, jako je kontrola zůstatku nebo doplňování kreditu u předplacených služeb, při použití svého primárního datového připojení LTE. USSI to řeší tím, že poskytuje nativní IP přenos pro USSD v rámci architektury IMS.

Přímo řeší omezení starší architektury USSD, která byla pevně svázána s doménou sítě pro přepojování okruhů. Definováním čistého protokolu založeného na SIP pro USSI umožňuje poskytovat stejné interaktivní služby přes jakoukoli IP přístupovou síť (LTE, 5G NR, WLAN), která má připojení k IMS. Tato evoluce byla nezbytná pro podporu vize GSM Association (GSMA) pro Voice over LTE (VoLTE) a Rich Communication Services (RCS), které vyžadují, aby všechny služby byly založeny na IMS. Bez USSI by byli operátoři nuceni implementovat složité mechanismy navrácení (např. Circuit-Switched Fallback) pouze pro USSD, což by zhoršilo uživatelský zážitek.

Historická motivace vychází z 3GPP Release 11, kde průmysl uznal potřebu plné konvergence služeb na IMS. USSI umožňuje operátorům modernizovat své síťové jádro migrací USSD aplikačních serverů do cloudu IMS, čímž snižuje závislost na starších sítích SS7 a zjednodušuje provoz. Zajišťuje budoucí životaschopnost hodnotného ekosystému služeb USSD, takže i při přechodu sítí na architektury 5G Standalone (SA) bez jakýchkoli prvků pro přepojování okruhů zůstanou základní interaktivní služby dostupné všem uživatelům, včetně těch se základními zařízeními s podporou IMS.

## Klíčové vlastnosti

- Přenáší USSD zprávy přes IMS pomocí protokolů SIP a MSRP
- Podporuje jak relací orientovaný (SIP INVITE + MSRP), tak transakčně orientovaný (SIP MESSAGE) režim
- Využívá aplikační server USSI (AS) v rámci servisní vrstvy IMS
- Umožňuje služby USSD pro uživatele na přístupu LTE (VoLTE) a 5G (VoNR)
- Poskytuje vzájemné propojení se staršími USSD servisními centry pro zpětnou kompatibilitu
- Definováno v 3GPP TS 24.390 a 24.391 pro detaily protokolu fáze 3

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [USSD – Unstructured Supplementary Services Data](/mobilnisite/slovnik/ussd/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [MSRP – Multiple Stream Registration Protocol](/mobilnisite/slovnik/msrp/)

## Definující specifikace

- **TS 24.390** (Rel-19) — USSD over IMS Procedures
- **TS 24.391** (Rel-19) — USSD over IMS Management Object Specification

---

📖 **Anglický originál a plná specifikace:** [USSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/ussi/)
