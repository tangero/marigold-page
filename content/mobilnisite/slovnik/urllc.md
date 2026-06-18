---
slug: "urllc"
url: "/mobilnisite/slovnik/urllc/"
type: "slovnik"
title: "URLLC – Ultra Reliable Low Latency Communication"
date: 2026-01-01
abbr: "URLLC"
fullName: "Ultra Reliable Low Latency Communication"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/urllc/"
summary: "URLLC je služební kategorie 3GPP navržená pro aplikace s kritickými požadavky (mission-critical), které vyžadují extrémně vysokou spolehlivost (např. 99,9999 %) a velmi nízkou latenci (např. 1 ms). Um"
---

URLLC je služební kategorie 3GPP pro aplikace s kritickými požadavky (mission-critical), které vyžadují extrémně vysokou spolehlivost a velmi nízkou latenci, což umožňuje využití například v průmyslové automatizaci a autonomních vozidlech.

## Popis

Ultra Reliable Low Latency Communication (URLLC) je základní služební kategorie v architektuře systému 5G, definovaná pro podporu aplikací s přísnými požadavky na koncovou latenci, spolehlivost a dostupnost. Na rozdíl od rozšířeného mobilního širokopásmového připojení (eMBB), které se zaměřuje na vysoké přenosové rychlosti, URLLC upřednostňuje deterministický výkon, často s cílovou latencí na rádiovém rozhraní až 1 milisekundu a úrovněmi spolehlivosti až 1-10^-5 nebo 1-10^-6 (pravděpodobnost úspěchu 99,999 % až 99,9999 %). Architektura podporující URLLC prostupuje jak rádiovou přístupovou síť (RAN), tak síť jádra (5GC), a vyžaduje koordinovaná vylepšení v plánování, přenosových schématech a správě síťových zdrojů.

Na fyzické vrstvě a vrstvě [MAC](/mobilnisite/slovnik/mac/) používá URLLC několik klíčových technik pro dosažení nízké latence. Patří mezi ně uplinkové přenosy bez udělení grantu (grant-free) nebo s konfigurovaným grantem (configured grant), které umožňují uživatelskému zařízení (UE) vysílat data okamžitě bez čekání na udělení plánovacího grantu, čímž se výrazně snižuje signalizační zpoždění. Krátké přenosové časové intervaly ([TTI](/mobilnisite/slovnik/tti/)), například mini-sloty, umožňují rychlejší kódování a dekódování paketů. Pro spolehlivost se využívají robustní modulační a kódovací schémata ([MCS](/mobilnisite/slovnik/mcs/)) spolu s technikami jako opakované kódování, kmitočtová diverzita a multi-konektivita (kdy je UE současně připojeno k více gNB nebo buňkám). Kritickou funkcí je duplikace paketů na vrstvě [PDCP](/mobilnisite/slovnik/pdcp/) přes více rádiových spojů, při které jsou identické datové pakety odesílány různými rádiovými linkami nebo nosnými kmitočty, aby se zvýšila pravděpodobnost úspěšného doručení.

V síti jádra podpora URLLC zahrnuje síťové funkce, jako je funkce pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a funkce pro správu relací ([SMF](/mobilnisite/slovnik/smf/)), které jsou si vědomy profilů kvality služeb (QoS) pro URLLC. Identifikátor QoS pro 5G ([5QI](/mobilnisite/slovnik/5qi/)) obsahuje standardizované hodnoty určené speciálně pro toky URLLC, které se mapují na přesný rozpočet zpoždění paketu, míru chybovosti paketů a výchozí úrovně priority. Síť jádra zajišťuje vhodné nasazení funkcí uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)), případně s využitím edge computingu (prostřednictvím Multi-access Edge Computing - MEC) k lokalizaci zpracování provozu a dalšímu snížení latence. Slicování sítí je s URLLC vnitřně propojeno a umožňuje vytváření vyhrazených, logicky izolovaných síťových řezů s rezervovanými zdroji a přizpůsobenými konfiguracemi, které garantují požadovaný výkon nezávisle na jiných typech služeb.

## K čemu slouží

URLLC bylo vytvořeno jako odpověď na rostoucí poptávku po bezdrátové konektivitě v průmyslových a jiných aplikacích s kritickými požadavky (mission-critical), které nesnesou proměnnou latenci a spolehlivost tradičních mobilních širokopásmových služeb. Před 5G byly mobilní sítě (2G, 3G, 4G) optimalizovány pro komunikaci zaměřenou na člověka – hlas a mobilní internet – kde byla přijatelná zpoždění v řádu desítek nebo stovek milisekund. Nástup Průmyslu 4.0, autonomních systémů a vzdáleného řízení v reálném čase odhalil omezení těchto sítí pro aplikace, jako je tovární automatizace, chytré sítě a telechirurgie, kde by zmeškání termínu nebo ztracený paket mohly vést ke katastrofickému selhání, bezpečnostním rizikům nebo významné ekonomické ztrátě.

Motivací pro standardizaci URLLC v rámci 3GPP, počínaje vydáním 14 jako studijní položkou a dále se vyvíjející v následujících vydáních, byla proměna mobilní technologie v univerzální konektivní platformu schopnou podporovat komunikaci jak lidského typu, tak typu stroj-stroj se zaručeným výkonem. Řeší problém poskytování 'deterministické' bezdrátové komunikace přes sdílené médium se statistickým multiplexováním. Definováním jasných cílů a standardizací umožňujících mechanismů napříč celou zásobníkem protokolů umožňuje URLLC různým vertikálním odvětvím spoléhat na 5G jako na náhradu nebo doplněk kabelových sběrnicových systémů pole (jako PROFINET, EtherCAT) a proprietárních bezdrátových řešení, což umožňuje větší flexibilitu, mobilitu a škálovatelnost v automatizovaných prostředích.

## Klíčové vlastnosti

- Uplinkový přenos bez udělení grantu (grant-free) nebo s konfigurovaným grantem (configured grant) pro snížení plánovací latence
- Duplikace paketů na vrstvě PDCP přes více rádiových spojů pro zvýšenou spolehlivost
- Zkrácené přenosové časové intervaly (TTI), například mini-sloty
- Specifické hodnoty 5QI pro URLLC pro zpracování toků QoS
- Podpora časově kritické komunikace (TSC) a integrace s IEEE TSN
- Rozšířená podpora uplinkového přerušení (pre-emption) a stanovování priorit

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.830** (Rel-16) — Business Role Models for Network Slicing
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TR 23.745** (Rel-17) — Study on App Layer Support for Factories of the Future in 5G
- **TS 24.543** (Rel-19) — SEAL Data Delivery Management Protocol
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.892** (Rel-16) — Study on User Plane Protocol in 5GC
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.825** (Rel-16) — Security for 5G URLLC Services
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [URLLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/urllc/)
