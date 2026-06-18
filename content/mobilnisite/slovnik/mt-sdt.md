---
slug: "mt-sdt"
url: "/mobilnisite/slovnik/mt-sdt/"
type: "slovnik"
title: "MT-SDT – Mobile Terminated Small Data Transmission"
date: 2025-01-01
abbr: "MT-SDT"
fullName: "Mobile Terminated Small Data Transmission"
category: "IoT"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mt-sdt/"
summary: "Funkce 5G NR umožňující efektivní doručování malých datových paketů iniciované sítí pro IoT zařízení ve stavu RRC Inactive. Snižuje signalizační režii a spotřebu energie zařízení tím, že se vyhne plné"
---

MT-SDT je funkce 5G NR, která umožňuje efektivní doručování malých datových paketů iniciované sítí pro IoT zařízení ve stavu RRC Inactive, čímž snižuje signalizační zátěž a spotřebu energie.

## Popis

Mobile Terminated Small Data Transmission (MT-SDT) je funkce 3GPP standardizovaná ve vydání 18 pro 5G New Radio (NR). Je protějškem k Mobile Originated Small Data Transmission ([MO-SDT](/mobilnisite/slovnik/mo-sdt/)) a je navržena pro scénáře IoT a mMTC (massive Machine-Type Communications). Základní princip spočívá v umožnění síti doručit malé množství downlink dat uživatelskému zařízení (UE), které je ve stavu [RRC](/mobilnisite/slovnik/rrc/)_INACTIVE, aniž by zařízení přešlo do stavu RRC_CONNECTED. To je klíčové pro IoT zařízení s omezenou kapacitou baterie, která pouze sporadicky přijímají malé příkazy, aktualizace nebo potvrzení ze síťových serverů.

Z architektonického hlediska MT-SDT využívá stávající architekturu 5G core sítě (5GC) a NG-RAN. Když downlink data dorazí na [UPF](/mobilnisite/slovnik/upf/) (User Plane Function) pro UE ve stavu RRC_INACTIVE, 5GC, konkrétně [AMF](/mobilnisite/slovnik/amf/) (Access and Mobility Management Function), spustí proceduru Network Triggered Service Request. RAN, který udržuje kontext UE ve stavu RRC_INACTIVE (uložený v poslední obsluhující gNB a potenciálně v RAN-based Notification Area), stránkuje (page) UE. Po přijetí stránkovací zprávy UE zahájí proceduru Random Access. Namísto provedení konvenčního Service Request vedoucího k RRC_CONNECTED však může UE během procesu Random Access indikovat svou schopnost a záměr použít MT-SDT, typicky prostřednictvím specifického preambule nebo zprávy.

Klíčovým technickým prvkem je přenos downlink uživatelských dat uvnitř počátečních signalizačních zpráv procedury RRC, která obnovuje pozastavené RRC spojení. Konkrétně může gNB zahrnout datovou část (payload) downlink dat do zprávy RRCResume nebo následující downlink RRC zprávy dříve, než je RRC spojení plně obnoveno do stavu CONNECTED. Tato data jsou přenášena pomocí uloženého [AS](/mobilnisite/slovnik/as/) bezpečnostního kontextu a stejných protokolových vrstev ([PDCP](/mobilnisite/slovnik/pdcp/), [RLC](/mobilnisite/slovnik/rlc/), [MAC](/mobilnisite/slovnik/mac/)) jako normální datový přenos, ale signalizační procedura je zkrácena. Po úspěšném doručení dat se může UE vrátit do stavu RRC_INACTIVE bez dokončení plné procedury obnovení (resume), nebo se síť může rozhodnout převést UE do stavu RRC_CONNECTED, pokud čekají další data. Tento mechanismus významně snižuje signalizaci řídicí roviny mezi UE a sítí a minimalizuje dobu, po kterou je rádiový transceiver UE aktivní, což přímo prodlužuje životnost baterie.

MT-SDT je definována napříč několika skupinami specifikací 3GPP. TS 38.300 poskytuje celkový popis systému NR, zatímco TS 38.331 (RRC) a TS 38.321 (MAC) detailně popisují signalizační procedury a vylepšení MAC. TS 38.423 (XnAP) a TS 38.473 (NGAP) pokrývají relevantní signalizaci rozhraní RAN pro načítání kontextu a koordinaci stránkování. TS 29.244 specifikuje protokol uživatelské roviny 5GC. TS 37.480 a 37.483 pokrývají požadavky na výkon a testovací specifikace pro UE a síť, zajišťující interoperabilitu a spolehlivý provoz. Její role je nedílnou součástí podpory 5G pro rozsáhlá nasazení IoT s nízkou spotřebou, což činí komunikaci iniciovanou sítí stejně efektivní jako komunikace iniciovaná zařízením.

## K čemu slouží

MT-SDT byla vytvořena k řešení kritické neefektivity v celulárním IoT: vysoké náklady na vytvoření plného RRC spojení pro doručení malých downlink paketů. Před zavedením MT-SDT, pokud IoT zařízení v úsporném stavu (jako RRC_IDLE nebo RRC_INACTIVE) potřebovalo přijmout data, síť jej musela stránkovat (page), zařízení by provedlo úplnou proceduru RRC Connection Resume nebo Setup, přešlo by do stavu RRC_CONNECTED, přijalo data a poté by prošlo další procedurou k uvolnění spojení a návratu do stavu idle/inactive. Celý tento cyklus spotřebovává významné signalizační zdroje na rádiovém rozhraní a v core síti a, což je důležitější, vybíjí baterii zařízení pro datovou část, která může mít jen několik bajtů.

Historický kontext spočívá ve vývoji celulárního IoT od 2G/3G přes LTE-M a NB-IoT až po 5G NR. Zatímco MO-SDT (pro uplink) byla zavedena dříve, downlinková cesta zůstávala neefektivní. Motivací pro MT-SDT ve vydání Rel-18 bylo dosáhnout symetrie a dokončit paradigma optimalizace pro "malá data" v 5G. Řeší omezení předchozích přístupů, kdy jakákoli downlink data, bez ohledu na velikost, spustila plné navázání spojení. To byla hlavní překážka pro aplikace jako dálkové ovládání senzorů, aktualizace firmwaru nebo příkazové a řídicí systémy pro miliony zařízení, kde jsou hlavními omezeními zatížení síťové signalizace a spotřeba energie zařízení.

Zavedením MT-SDT umožňuje 3GPP síťovým operátorům podporovat obrovské množství IoT zařízení s občasným downlink provozem škálovatelným a udržitelným způsobem. Snižuje latenci pro downlink příkazy a optimalizuje využití rádiových zdrojů. Tato funkce je základním kamenem pro umožnění skutečně masivních Machine-Type Communications (mMTC) v 5G Advanced, podporujících případy užití v chytrých městech, průmyslovém IoT a sledování majetku, kde jsou zařízení převážně pasivní, ale občas potřebují být instruována nebo aktualizována sítí.

## Klíčové vlastnosti

- Umožňuje doručování downlink dat pro UE ve stavu RRC_INACTIVE bez plného obnovení RRC spojení
- Snižuje signalizační režii a spotřebu energie UE pro občasný provoz iniciovaný sítí
- Využívá stávající proceduru RRCResume s přibaleními (piggybacked) uživatelskými daty
- Podporuje modely přenosu malých dat založené na CP (Control Plane) i UP (User Plane)
- Integruje se s procedurou 5GC Network Triggered Service Request a stránkováním v RAN-based notification area
- Udržuje AS bezpečnost pomocí uloženého bezpečnostního kontextu z předchozího stavu RRC_CONNECTED

## Související pojmy

- [MO-SDT – Mobile Originated Small Data Transmission](/mobilnisite/slovnik/mo-sdt/)

## Definující specifikace

- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 37.480** (Rel-19) — E1 Interface General Aspects and Principles
- **TS 37.483** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [MT-SDT na 3GPP Explorer](https://3gpp-explorer.com/glossary/mt-sdt/)
