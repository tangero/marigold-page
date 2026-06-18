---
slug: "mm"
url: "/mobilnisite/slovnik/mm/"
type: "slovnik"
title: "MM – Mobility Management"
date: 2025-01-01
abbr: "MM"
fullName: "Mobility Management"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mm/"
summary: "Mobility Management (MM) je základní protokol vrstvy 3 v sítích 3GPP zodpovědný za sledování a udržování polohy mobilního zařízení (UE). Umožňuje síti znát stav dosažitelnosti UE (např. nečinné, připo"
---

MM je protokol vrstvy 3 v sítích 3GPP zodpovědný za sledování polohy a stavu dosažitelnosti mobilního zařízení, aby umožnil funkce jako volání, registrace a předávání spojení.

## Popis

Mobility Management (MM) je základní síťová funkce fungující na vrstvě Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)), která spravuje mobilitu uživatelského zařízení (UE) nezávisle na podkladové technologii rádiového přístupu. Primárním cílem MM je udržovat přesnou polohu UE, aby síť mohla úspěšně doručovat příchozí hovory, zprávy a datové relace. Toho dosahuje správou různých stavů UE, především stavů IDLE a CONNECTED, a zpracováním procedur, které převádějí UE mezi těmito stavy. Ve stavu IDLE UE aktivně nepřenáší uživatelská data, ale je registrováno v síti a naslouchá zprávám volání. Stav CONNECTED (nebo v některých kontextech ACTIVE) značí, že mezi UE a jádrem sítě existuje signalizační spojení, což umožňuje aktivní komunikaci.

Funkce MM se opírá o soubor informací známý jako MM kontext. Tento kontext je uložen jak v UE, tak v příslušných uzlech jádra sítě, jako je Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) ve 2G/3G nebo Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G. MM kontext zahrnuje kritické parametry jako dočasná identita UE ([TMSI](/mobilnisite/slovnik/tmsi/), [GUTI](/mobilnisite/slovnik/guti/)), bezpečnostní klíče, aktuální registrační oblast UE a jeho aktuální stav správy mobility. Tento sdílený kontext umožňuje síti a UE mít synchronizovaný pohled na stav mobility UE, což umožňuje efektivní procedury jako periodické aktualizace registrace, předávání spojení mezi buňkami nebo oblastmi sledování a žádosti o službu pro opětovné navázání spojení uživatelské roviny.

Klíčové procedury MM zahrnují Připojení/Registraci, Odpojení/Zrušení registrace, Aktualizaci oblasti sledování ([TAU](/mobilnisite/slovnik/tau/)) nebo Aktualizaci směrovací oblasti ([RAU](/mobilnisite/slovnik/rau/)), Periodickou aktualizaci registrace a Žádost o službu. Procedura Připojení založí přítomnost UE v síti a vytvoří počáteční MM kontext. Periodické aktualizace a TAU/RAU informují síť o poloze UE při jejím pohybu, což zajišťuje, že síť může volat UE v konkrétní oblasti namísto v celé síti. Procedura Žádost o službu je spuštěna UE nebo sítí k přechodu UE ze stavu IDLE do stavu CONNECTED pro přenos uživatelských dat. Tyto procedury jsou základní pro fungování jakékoliv mobilní sítě, zajišťují, že mobilní zařízení zůstávají dosažitelná, a zároveň optimalizují využití rádiových a síťových zdrojů minimalizací signalizační zátěže, když je zařízení nehybné nebo neaktivní.

Ve vývoji od 2G/3G k 4G a 5G zůstávají základní principy MM zachovány, ale konkrétní síťové entity a detaily protokolu se vyvinuly. Například v 5G je funkce MM logicky oddělena od správy relací (SM) a je umístěna v rámci AMF. MM v 5G zavádí koncepty jako Registrační oblasti, které mohou být seznamem oblastí sledování, a vylepšené stavy pro úsporu energie (např. RRC_INACTIVE). Navzdory těmto architektonickým změnám zůstává základní role MM – sledování polohy UE, správa dosažitelnosti a podpora kontinuity relace – pilířem architektury mobilních sítí 3GPP.

## K čemu slouží

Mobility Management existuje, aby řešila základní výzvu poskytování bezproblémové komunikace zařízení, které se může volně pohybovat po rozsáhlé geografické oblasti. Ve pevné síti je bod připojení a adresa zařízení statické. V mobilní síti se bod připojení (buňka) neustále mění. Bez MM by síť neměla způsob, jak lokalizovat UE pro doručení příchozích služeb, což by znemožnilo mobilní komunikaci. Primární problémy, které MM řeší, jsou dosažitelnost UE, efektivní využití zdrojů a kontinuita relace během pohybu.

Historicky zavedly rané celulární systémy jako GSM základní koncepty MM, jako jsou oblasti polohy a periodické aktualizace. Omezení dřívějších, jednodušších přístupů zahrnovala nadměrnou zátěž volání (pokud byla poloha příliš hrubá) nebo nadměrný signalizační provoz z častých aktualizací (pokud byla oblast polohy příliš malá). Protokoly MM od 3GPP se vyvinuly, aby vytvořily vyvážený, škálovatelný systém. Zavedly hierarchické koncepty jako Směrovací oblasti (pro paketově orientovanou doménu) a Oblasti sledování a stavy jako IDLE a CONNECTED pro optimalizaci signalizace. MM kontext umožňuje síti uložit právě dostatek informací pro rychlé znovunavázání spojení bez nutnosti plné opětovné autentizace pokaždé, když se UE pohne nebo probudí ze stavu úspory energie.

Vytvoření a neustálé vylepšování protokolů MM bylo motivováno potřebou podporovat stále rostoucí počet mobilních účastníků, rozmanité služby (od hlasu po vysokorychlostní data) a nové typy zařízení (IoT senzory s velmi odlišnými vzorci mobility). Poskytuje základní vrstvu, na které jsou všechny ostatní služby – hlasové hovory, prohlížení internetu, IoT zprávy – spolehlivě doručovány pohyblivému cíli. Je to klíčový prvek umožňující splnění slibu celulárních sítí o konektivitě 'kdekoli a kdykoli'.

## Klíčové vlastnosti

- Spravuje stavy UE (IDLE, CONNECTED, INACTIVE) pro rovnováhu mezi dosažitelností a energetickou účinností
- Udržuje sdílený MM kontext mezi UE a síťovými uzly pro synchronizovaný stav mobility
- Provádí procedury aktualizace polohy (TAU, RAU, Periodická registrace) pro sledování pohybu UE
- Zpracovává procedury Připojení/Registrace a Odpojení/Zrušení registrace pro vstup do sítě a výstup z ní
- Spouští proceduru Žádost o službu pro přechod UE do připojeného stavu pro přenos dat
- Spolupracuje s voláním pro lokalizaci UE ve stavu IDLE v konkrétní oblasti pro příchozí komunikaci

## Související pojmy

- [GUTI – Globally Unique Temporary UE Identity](/mobilnisite/slovnik/guti/)
- [TAU – Tracking Area Update](/mobilnisite/slovnik/tau/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)

## Definující specifikace

- **TS 21.810** (Rel-4) — Multi-mode UE Issues - Categories, principles and procedures
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 21.910** (Rel-4) — Multi-mode UE Operation Principles
- **TS 22.140** (Rel-19) — MMS Stage 1 Requirements
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.110** (Rel-19) — Access Stratum Services Specification
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.851** (Rel-6) — Network Sharing Architecture for 3G Systems
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- … a dalších 27 specifikací

---

📖 **Anglický originál a plná specifikace:** [MM na 3GPP Explorer](https://3gpp-explorer.com/glossary/mm/)
