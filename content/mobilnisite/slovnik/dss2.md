---
slug: "dss2"
url: "/mobilnisite/slovnik/dss2/"
type: "slovnik"
title: "DSS2 – Digital Subscriber Signalling System No. 2"
date: 2025-01-01
abbr: "DSS2"
fullName: "Digital Subscriber Signalling System No. 2"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dss2/"
summary: "DSS2 je signalizační protokol používaný v jádrové síti, konkrétně pro navazování, správu a uvolňování paketových spojení v architektuře NGN/IMS. Jde o 3GPP adaptaci standardu ITU-T Q.2931 pro B-ISDN,"
---

DSS2 je 3GPP adaptace protokolu ITU-T Q.2931 používaná v jádrové síti pro navazování, správu a uvolňování paketových spojení v architekturách NGN/IMS.

## Popis

Digital Subscriber Signalling System No. 2 (DSS2) je signalizační protokol síťové vrstvy definovaný 3GPP pro použití v architekturách IP Multimedia Subsystem (IMS) a Next Generation Network ([NGN](/mobilnisite/slovnik/ngn/)). Působí přes rozhraní Nc, což je referenční bod mezi funkcemi řízení relací ([CSCF](/mobilnisite/slovnik/cscf/)) uvnitř jádra IMS. DSS2 je založen na standardu [ITU-T](/mobilnisite/slovnik/itu-t/) Q.2931, původně vyvinutém pro Broadband Integrated Services Digital Network ([B-ISDN](/mobilnisite/slovnik/b-isdn/)), a byl adaptován 3GPP, aby poskytoval řízení hovoru a přenosového kanálu pro paketové multimediální relace. Protokol využívá strukturu orientovanou na zprávy k výměně informačních prvků mezi síťovými entitami, čímž usnadňuje navazování, modifikaci a ukončování spojení s definovanými parametry kvality služeb (QoS).

Z architektonického hlediska funguje DSS2 v řídicí rovině jádrové sítě, odděleně od uživatelské roviny, která přenáší skutečný mediální provoz. Je klíčovou součástí interakcí mezi funkcí řízení mediálních bran ([MGCF](/mobilnisite/slovnik/mgcf/)) a CSCF, zejména pro propojení se staršími sítěmi s přepojováním okruhů nebo v určitých scénářích řízení hovoru v IMS. Protokol používá spolehlivý transportní mechanismus, typicky přes IP s využitím Stream Control Transmission Protocol ([SCTP](/mobilnisite/slovnik/sctp/)) nebo [MTP3](/mobilnisite/slovnik/mtp3/), aby zajistil doručování signalizačních zpráv. Jeho činnost zahrnuje výměnu specifických zpráv, jako jsou SETUP, CALL PROCEEDING, ALERTING, CONNECT a RELEASE, z nichž každá obsahuje povinné a volitelné informační prvky popisující charakteristiky hovoru, možnosti přenosového kanálu a adresování.

Role DSS2 v síti 3GPP je primárně jako protokol pro propojení se staršími systémy a pro interní řízení v rámci architektury IMS. Umožňuje CSCF řídit mediální brány a navazovat cesty přenosových kanálů pro multimediální relace. Zatímco novější protokoly, jako je Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)), se staly dominantními pro řízení hovorů v IMS, DSS2 zůstává specifikován pro konkrétní rozhraní a scénáře, čímž zajišťuje zpětnou kompatibilitu a podporu standardizovaných propojovacích funkcí. Jeho podrobné procedury pokrývají zpracování chyb, správu stavů a vyjednávání parametrů spojení, což z něj činí robustní, byť specializovanou součást signalizační sady 3GPP.

## K čemu slouží

DSS2 byl zaveden do specifikací 3GPP, aby poskytl standardizovaný, robustní signalizační mechanismus pro řízení hovoru a přenosového kanálu v rámci se vyvíjející jádrové sítě s přepojováním paketů, zejména v době definování architektury IMS. Řešil potřebu osvědčeného, spojově orientovaného signalizačního protokolu, který by dokázal spravovat navazování přenosových kanálů se zaručenou QoS pro multimediální služby, což byl požadavek, který rané paketové protokoly postrádaly. Motivace vycházela z průmyslových zkušeností s B-ISDN a z touhy využít stávající, dobře specifikovanou signalizační technologii (ITU-T Q.2931) pro nové sítě založené na IP, což mělo zajistit spolehlivost a funkční paritu se staršími systémy.

Vznik DSS2 v rámci 3GPP byl hnut nutností propojení mezi novou doménou IMS a existujícími sítěmi s přepojováním okruhů, stejně jako pro interní řízení v určitých uzlech IMS. Předchozí přístupy v čistě IP sítích se často spoléhaly na jednodušší, best-effort signalizaci nebo nebyly navrženy pro složitou dohodu parametrů přenosového kanálu s konkrétními parametry provozu. DSS2 poskytl formalizovanou metodu pro vyžádání spojení s explicitními charakteristikami šířky pásma, zpoždění a chvění, což bylo nezbytné pro hlasové a video služby vyžadující garantovaný výkon. Jeho přijetí nabídlo migrační cestu a stabilní technologii řídicí roviny během přechodu od jádrových sítí s přepojováním okruhů k plně IP jádrovým sítím.

Historicky DSS2 představuje most mezi telekomunikačním světem B-ISDN a novým světem paketových jader 3GPP. Ačkoli bylo jeho použití v mnoha oblastech nahrazeno více nativními IP protokoly, jako je SIP, jeho specifikace zajistila, že raná nasazení IMS mohla začlenit důsledné řízení spojení a propojení se zařízeními používajícími mezinárodní telekomunikační standardy. Vyřešil problém, jak aplikovat spolehlivost a stavovost signalizace tradiční telekomunikační úrovně na navazování paketových přenosových kanálů.

## Klíčové vlastnosti

- Založen na standardu ITU-T Q.2931 pro signalizaci B-ISDN
- Poskytuje funkce řízení hovoru a řízení přenosového kanálu pro paketová spojení
- Působí přes referenční bod Nc mezi CSCF v IMS
- Používá signalizaci orientovanou na zprávy s definovanými informačními prvky
- Podporuje vyjednávání parametrů QoS pro přenosový kanál
- Zahrnuje procedury pro navázání, modifikaci a uvolnění spojení

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)

## Definující specifikace

- **TS 29.414** (Rel-19) — Nb Interface Bearer Transport & Control Protocols

---

📖 **Anglický originál a plná specifikace:** [DSS2 na 3GPP Explorer](https://3gpp-explorer.com/glossary/dss2/)
