---
slug: "nidd"
url: "/mobilnisite/slovnik/nidd/"
type: "slovnik"
title: "NIDD – Non-IP Data Delivery"
date: 2026-01-01
abbr: "NIDD"
fullName: "Non-IP Data Delivery"
category: "IoT"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nidd/"
summary: "Funkce 3GPP umožňující přenos malých ne-IP datových paketů (např. ze senzorů IoT) přímo přes řídicí rovinu mobilní sítě. Optimalizuje využití síťových prostředků tím, že se vyhne režii spojené se zřiz"
---

NIDD je funkce 3GPP, která přenáší malé ne-IP datové pakety přímo přes řídicí rovinu mobilní sítě, čímž optimalizuje využití prostředků tím, že se vyhne režii plné IP relace.

## Popis

Non-IP Data Delivery (NIDD, doručování ne-IP dat) je schopnost jádrové sítě standardizovaná organizací 3GPP pro efektivní podporu komunikace typu stroj-stroj ([MTC](/mobilnisite/slovnik/mtc/)) a zařízení internetu věcí (IoT). Umožňuje přenos malých datových jednotek aplikační vrstvy, které nejsou zapouzdřeny v IP paketu. Toho je dosaženo přenosem datové části přímo přes signalizační protokoly řídicí roviny, konkrétně protokol Non-Access Stratum ([NAS](/mobilnisite/slovnik/nas/)) mezi uživatelským zařízením (UE) a funkcí Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G, nebo funkcí Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) v 5G. Data tímto obcházejí tradiční přenosové kanály uživatelské roviny ([PDN](/mobilnisite/slovnik/pdn/) připojení nebo [PDU](/mobilnisite/slovnik/pdu/) relace), které jsou navrženy pro souvislý objemný IP provoz.

Architektonická implementace zahrnuje klíčové síťové funkce. V architektuře EPS (4G) se Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) pro provoz NIDD nepoužívají. Místo toho MME přímo komunikuje s funkcí Service Capability Exposure Function (SCEF) přes rozhraní T6a. SCEF funguje jako brána API, která bezpečně zpřístupňuje službu NIDD externím aplikačním serverům (AS). Poskytuje možnosti doručování ne-IP dat, spouštění zařízení a monitorování. V architektuře 5G System (5GS) je analogickou funkcí Network Exposure Function (NEF), která pro přenos dat řídicí rovinou komunikuje s AMF.

Procedura NIDD zahrnuje, že UE při připojení nebo registraci indikuje svou podporu optimalizací CIoT EPS/5GS pro řídicí rovinu. Když má zařízení nebo síť data k odeslání, jsou tato zapouzdřena do přenosové zprávy NAS. Pro data iniciovaná mobilním zařízením (MO) UE zahrne aplikační data do zprávy NAS odeslané MME/AMF. MME/AMF pak tato data přepošle SCEF/NEF, která je doručí určenému AS. Pro data směřující k mobilnímu zařízení (MT) je proces opačný: AS odešle data SCEF/NEF, která spustí downlink zprávu NAS k zařízení přes MME/AMF.

NIDD hraje klíčovou roli při umožnění masivního nasazení IoT tím, že výrazně snižuje signalizaci a spotřebu energie. Protože využívá signalizační spojení, které je pro účely správy mobility trvale udržováno aktivní, odpadá potřeba, aby zařízení pro každý přenos malých dat aktivovalo datový rádiový kanál a provedlo proceduru Service Request. To je ideální pro zařízení odesílající občasné aktualizace stavu, odečty měřidel nebo data ze senzorů, což vede k prodloužené životnosti baterie (často až na 10 let) a snížení zatížení jádrové sítě.

## K čemu slouží

NIDD bylo vytvořeno, aby vyřešilo zásadní neefektivitu používání tradičních IP mobilních datových připojení pro jedinečné charakteristiky provozu IoT zařízení. Raná nasazení IoT/MTC používala standardní mobilní data, což vyžadovalo zřízení plného kontextu Packet Data Protocol (PDP) nebo PDN připojení – proces zahrnující významnou signalizační výměnu a alokaci rádiových prostředků – i pro odeslání několika bajtů dat. To bylo z hlediska síťových prostředků a energie baterie zařízení velmi plýtvavé, což činilo rozsáhlá nasazení ekonomicky a technicky náročnými.

Hlavní motivací byla optimalizace sítě pro 'občasný přenos malých objemů dat', což je charakteristický znak mnoha aplikací MTC, jako jsou chytré měřiče, sledovače majetku a environmentální senzory. 3GPP uznalo, že režie IP hlaviček (často 40 bajtů pro IPv4 nebo 60+ bajtů pro IPv6) může být větší než samotná užitečná datová část. Tím, že umožňuje odesílání dat bez IP zapouzdření přes existující signalizační cestu řídicí roviny, NIDD drasticky snižuje protokolovou režii a signalizační latenci.

Historicky byl NIDD klíčovou součástí optimalizací Cellular Internet of Things (CIoT) zavedených ve verzi 3GPP Release 13. Vyřešil omezení předchozích přístupů opětovným využitím zabezpečeného, autentizovaného signalizačního spojení NAS, čímž poskytl odlehčenou, vždy dostupnou datovou cestu. To umožnilo nové obchodní modely a služby vyžadující ultra-nízkou spotřebu energie a vysokou hustotu připojení, které nebyly s konvenčními architekturami mobilního širokopásmového připojení proveditelné.

## Klíčové vlastnosti

- Přenos aplikačních dat přes signalizaci NAS (řídicí rovinu)
- Odstraňuje potřebu aktivace kontextu PDP/PDU relace v uživatelské rovině pro malá data
- Významně snižuje signalizační režii a spotřebu energie zařízení
- Podporováno přes SCEF v EPS (4G) a NEF v 5GS pro zpřístupnění aplikacím
- Poskytuje zabezpečené doručování s využitím stávajícího zabezpečení na vrstvě NAS a síťové vrstvě
- Umožňuje efektivní zpracování občasných, na zpoždění necitlivých malých datových paketů

## Související pojmy

- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)
- [SCEF – Service Capability Exposure Function](/mobilnisite/slovnik/scef/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TS 22.262** (Rel-19) — MSGin5G Service Requirements
- **TS 23.554** (Rel-19) — MSGin5G Service Application Architecture
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.538** (Rel-19) — MSGin5G Service Protocol Specification
- **TR 28.816** (Rel-17) — Charging for 5G Cellular IoT
- **TS 29.122** (Rel-19) — T8 Reference Point for Northbound APIs
- **TS 29.336** (Rel-19) — HSS Diameter Interfaces for PDN Interworking
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.541** (Rel-19) — NEF Service-Based Interfaces for NIDD & SMS
- **TS 29.542** (Rel-19) — SMF NIDD Service Based Interface Stage 3
- **TS 32.253** (Rel-19) — Charging for Control Plane Data Transfer
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [NIDD na 3GPP Explorer](https://3gpp-explorer.com/glossary/nidd/)
