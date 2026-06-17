---
slug: "lapd"
url: "/mobilnisite/slovnik/lapd/"
type: "slovnik"
title: "LAPD – Link Access Procedure on the D-channel"
date: 2025-01-01
abbr: "LAPD"
fullName: "Link Access Procedure on the D-channel"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lapd/"
summary: "LAPD je protokol linkové vrstvy používaný v ISDN a adaptovaný v 3GPP pro signalizační přepravu, zejména přes D-kanál. Poskytuje spolehlivou, multiplexovanou komunikaci mezi více koncovými body přes je"
---

LAPD je protokol linkové vrstvy používaný v ISDN a adaptovaný v 3GPP pro zajištění spolehlivé, multiplexované signalizační přepravy na rozhraních, jako je A-bis v mobilních sítích.

## Popis

Link Access Procedure on the D-channel (LAPD) je linkový protokol standardizovaný [ITU-T](/mobilnisite/slovnik/itu-t/) (Q.921) a přijatý v rámci 3GPP pro signalizační aplikace. Jak název napovídá, byl původně navržen pro D-kanál (signalizační kanál) v [ISDN](/mobilnisite/slovnik/isdn/), ale v kontextech 3GPP se používá primárně pro přepravu signalizace mezi síťovými prvky, například mezi Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) a Base Transceiver Station ([BTS](/mobilnisite/slovnik/bts/)) na rozhraní A-bis v GSM. LAPD pracuje na vrstvě 2 (linkové vrstvě) a poskytuje spolehlivou, spojově orientovanou službu, která může multiplexovat více spojení datové linky (pomocí Data Link Connection Identifiers - [DLCI](/mobilnisite/slovnik/dlci/)) přes jeden fyzický kanál, což umožňuje efektivní sdílení signalizačních linek.

LAPD je založen na rámci [HDLC](/mobilnisite/slovnik/hdlc/), ale je specificky přizpůsoben požadavkům D-kanálu. Jeho rámcová struktura zahrnuje příznak (flag), adresní pole (obsahující Service Access Point Identifier - SAPI, Terminal Endpoint Identifier - TEI a bit příkaz/odpověď), řídicí pole (pro číslování sekvencí a typ rámce), informační pole (pro zprávy vyšších vrstev) a [FCS](/mobilnisite/slovnik/fcs/). Protokol podporuje dva provozní režimy: Unacknowledged Information Transfer (UI rámce) pro nespojovou signalizaci a Acknowledged Information Transfer (pomocí I-rámců) pro spojově orientované, spolehlivé služby. Pro potvrzovaný režim implementuje detekci chyb prostřednictvím FCS a retransmise prostřednictvím [ARQ](/mobilnisite/slovnik/arq/) spolu s řízením toku pomocí sekvenčních čísel.

V rámci sítí 3GPP GSM/UMTS je primární rolí LAPD spolehlivě přenášet signalizační zprávy vrstvy 3 (např. BSS Management, Radio Resource Management) přes rozhraní A-bis. Umožňuje více BTS sdílet jednu fyzickou linku k BSC použitím různých TEI, čímž optimalizuje využití infrastruktury. Protokol navazuje a udržuje spojení datové linky, zajišťuje integritu zpráv a spravuje logický kanál pro signalizační provoz. I když pozdější verze 3GPP přešly na IP-based transport, LAPD zůstal klíčovým prvkem pro signalizaci v legacy circuit-switched sítích, poskytujíc robustní a multiplexovanou službu vrstvy 2, která zajišťovala spolehlivé doručování kritických informací řídicí roviny.

## K čemu slouží

LAPD byl začleněn do standardů 3GPP, aby poskytl standardizovaný, multiplexovaný a spolehlivý linkový protokol pro signalizační kanály v mobilních sítích, řešíc potřebu efektivní přepravy řídicích zpráv mezi síťovými prvky. Jeho původ v ISDN poskytl osvědčené řešení pro zpracování signalizace odděleně od uživatelského provozu (B-kanál). V architektuře GSM bylo toto oddělení stejně hodnotné pro rozhraní jako je A-bis, kde robustní signalizace mezi BSC a BTS byla klíčová pro sestavování hovorů, handover a správu radiových zdrojů.

Protokol řešil několik klíčových problémů: Za prvé umožnil multiplexování signalizace pro více koncových bodů (např. několik BTS) přes jeden fyzický okruh, čímž snížil náklady na kabeláž a rozhraní. Za druhé poskytl detekci a korekci chyb, což zajišťovalo, že signalizační zprávy – které jsou malé, ale kritické – nebyly poškozeny během přenosu přes potenciálně šumné digitální linky. Bez takové spolehlivosti by mohlo častěji docházet k přerušeným hovorům nebo neúspěšným handoverům.

Historicky, před přijetím LAPD, mohly proprietární signalizační linky vést k závislosti na dodavateli a problémům s interoperabilitou. Standardizací na LAPD (založeném na ITU-T Q.921) zajistilo 3GPP kompatibilitu více dodavatelů pro rozhraní A-bis. Jeho návrh specificky pro signalizaci (D-kanál) znamenal, že byl optimalizován pro nárazové, nízkolatenční požadavky řídicího provozu, na rozdíl od univerzálních linkových protokolů. Toto zaměření z něj učinilo ideální volbu pro distribuovanou architekturu celulárních sítí, kde je spolehlivá a efektivní přeprava signalizace základním kamenem provozu sítě.

## Klíčové vlastnosti

- Podpora multiplexování prostřednictvím Data Link Connection Identifier (DLCI) kombinujícího SAPI a TEI
- Dva přenosové režimy: Nepotvrzovaný (UI rámce) a Potvrzovaný (I-rámce s ARQ)
- Detekce chyb pomocí Frame Check Sequence (FCS) s CRC-16
- Řízení toku a sekvencování pomocí sekvenčních čísel modulo 128
- Procedury navázání a uvolnění spojení (SABME, DISC)
- Podpora více service access points (SAPI) pro různé signalizační vrstvy

## Související pojmy

- [ISDN – Integrated Services Digital Network](/mobilnisite/slovnik/isdn/)
- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [BTS – Base Transceiver Station](/mobilnisite/slovnik/bts/)

## Definující specifikace

- **TS 44.064** (Rel-19) — GPRS Logical Link Control (LLC) Protocol

---

📖 **Anglický originál a plná specifikace:** [LAPD na 3GPP Explorer](https://3gpp-explorer.com/glossary/lapd/)
