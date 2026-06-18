---
slug: "ua"
url: "/mobilnisite/slovnik/ua/"
type: "slovnik"
title: "UA – Unnumbered Acknowledgement"
date: 2025-01-01
abbr: "UA"
fullName: "Unnumbered Acknowledgement"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ua/"
summary: "Typ rámce používaný v protokolech vrstvy datového spoje pro spolehlivý přenos dat bez sekvenčních čísel. Potvrzuje příjem rámců, umožňuje řízení toku a obnovu po chybě při signalizaci a přenosu dat. J"
---

UA je základní typ rámce vrstvy datového spoje používaný na rozhraních 3GPP pro spolehlivý přenos bez použití sekvenčních čísel, který poskytuje potvrzení příjmu, řízení toku dat a obnovu po chybě, čímž zajišťuje integritu dat.

## Popis

Unnumbered Acknowledgement (UA) je typ řídicího rámce definovaný v protokolech vrstvy datového spoje, jako jsou ty založené na principech [HDLC](/mobilnisite/slovnik/hdlc/) (High-Level Data Link Control), které se používají na mnoha rozhraních 3GPP. Funguje v režimu spojovaného přenosu a poskytuje kladné potvrzení pro přijaté rámce. Na rozdíl od informačních (I) rámců rámce UA nenesou sekvenční čísla (N(S) a N(R)); místo toho se používají k potvrzení navázání spoje, k potvrzení příkazu bez čísla a ke správě stavu spoje. Rámec UA je klíčovou součástí procedur přístupu ke spoji (Link Access Procedures – [LAP](/mobilnisite/slovnik/lap/)) pro různé signalizační přenašeče, zajišťující spolehlivé doručení signalizačních zpráv řídicí roviny mezi síťovými uzly.

Rámec UA funguje v systému příkaz/odezva. Když uzel přijme platný příkazový rámec [SABM](/mobilnisite/slovnik/sabm/) (Set Asynchronous Balanced Mode) nebo SABME (Set Asynchronous Balanced Mode Extended) pro inicializaci spoje, musí odpovědět rámcem UA, aby příkaz potvrdil a převedl spoj do stavu přenosu informací. Toto handshake potvrzuje, že oba konce spoje jsou synchronizovány a připraveny na výměnu dat. Podobně se rámce UA používají k potvrzení dalších příkazů bez čísla, jako je [DISC](/mobilnisite/slovnik/disc/) (Disconnect). Přenos rámce UA je přímou odpovědí na konkrétní příkaz a jeho příjem odesílateli potvrzuje úspěšné provedení tohoto příkazu.

V rámci architektury 3GPP jsou rámce UA specifikovány v podkladových transportních protokolech pro kritická rozhraní. Používají se například v protokolech vrstvy 2 pro [RANAP](/mobilnisite/slovnik/ranap/) (Radio Access Network Application Part) na rozhraní Iu, pro [BSSAP](/mobilnisite/slovnik/bssap/) (Base Station System Application Part) na rozhraní A a v řídicí rovině [GTP](/mobilnisite/slovnik/gtp/) ([GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol). Spolehlivost zajištěná mechanismem potvrzení UA je zásadní pro navázání, údržbu a ukončení signalizačních asociací a datových přenašečů. Jeho specifikace v širokém spektru technických specifikací (TS), od základní řady 23 přes zpoplatňovací řadu 32 až po bezpečnostní řadu 33, podtrhuje jeho základní roli ve spolehlivém provozu celého systému 3GPP od 2G GSM po 5G NR.

## K čemu slouží

Typ rámce Unnumbered Acknowledgement existuje, aby poskytoval jednoduchý a spolehlivý mechanismus pro správu spoje a potvrzování příkazů v protokolech datového spoje bez režie spojené se sekvenčními čísly. Řeší základní problém zajištění, že řídicí příkazy pro navázání a ukončení spojení jsou přijaty a správně provedeny. Než může začít spolehlivý přenos dat s číslovanými rámci, musí být samotný spoj spolehlivě navázán; rámec UA poskytuje potřebné kladné potvrzení pro toto úvodní handshake.

Historicky, odvozeno z norem ISO HDLC, byl tento mechanismus přijat do telekomunikací k vytvoření robustních signalizačních spojů. Řeší omezení spočívající v absenci potvrzení pro kritické řídicí příkazy spoje. Bez takového potvrzení by odesílající uzel nebyl jistý, zda je spoj navázán, což by mohlo vést k selhání přenosu nebo uváznutí protokolu. Rámec UA tuto jistotu poskytuje s minimální režií protokolu, protože se používá pouze pro specifické řídicí funkce a nikoli pro průběžné potvrzování každého datového rámce, které je zajišťováno číslovanými potvrzeními v I-rámcích.

Jeho trvalá přítomnost ve všech vydáních 3GPP od R99 po Rel-19 dokládá jeho trvalý účel jako základního prvku protokolu. Umožňuje spolehlivý transport signalizačních zpráv vyšších vrstev (jako je správa mobility a řízení hovoru) napříč všemi síťovými doménami. Stabilita konceptu UA umožňuje novějším síťovým funkcím a rozhraním spoléhat se na ověřený mechanismus spolehlivosti nízké úrovně pro své transportní vrstvy.

## Klíčové vlastnosti

- Kladné potvrzení pro příkazové rámce bez čísla, jako jsou SABM a DISC.
- Neobsahuje sekvenční čísla pro odeslání/příjem (N(S), N(R)).
- Používá se pro spolehlivé navázání a ukončení datového spoje.
- Základní pro procedury přístupu ke spoji založené na HDLC (LAPD, LAPF, LAPB).
- Zajišťuje synchronizaci stavu spoje mezi dvěma připojenými protistranami.
- Specifikován pro širokou škálu rozhraní 3GPP za účelem spolehlivosti transportu.

## Související pojmy

- [HDLC – High Level Data Link Control](/mobilnisite/slovnik/hdlc/)
- [LAPD – Link Access Procedure on the D-channel](/mobilnisite/slovnik/lapd/)
- [SABM – Set Asynchronous Balanced Mode frame](/mobilnisite/slovnik/sabm/)

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.454** (Rel-8) — Closed User Group (CUG) Protocol Specification
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.604** (Rel-19) — Communications Diversion (CDIV) Protocol Spec
- **TS 24.606** (Rel-19) — MWI Service Protocol Description
- **TS 24.654** (Rel-19) — Closed User Group (CUG) supplementary service
- **TS 29.079** (Rel-19) — Optimal Media Routeing (OMR) Procedures
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- … a dalších 12 specifikací

---

📖 **Anglický originál a plná specifikace:** [UA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ua/)
