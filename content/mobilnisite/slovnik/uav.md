---
slug: "uav"
url: "/mobilnisite/slovnik/uav/"
type: "slovnik"
title: "UAV – Uncrewed Aerial Vehicle"
date: 2026-01-01
abbr: "UAV"
fullName: "Uncrewed Aerial Vehicle"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/uav/"
summary: "Letadlo provozované bez lidského pilota na palubě, běžně známé jako dron. V rámci 3GPP se tento termín vztahuje k využití mobilních sítí (4G/5G) pro přenos povelů a řízení UAV, jejich sledování a komu"
---

UAV je bezpilotní letadlo (uncrewed aerial vehicle), které využívá mobilní sítě pro přenos povelů, řízení, sledování a komunikaci s užitečným zatížením, aby umožnilo bezpečné, škálovatelné operace mimo vizuální dohled (BVLOS).

## Popis

Ve standardech 3GPP se termín Bezpilotní Letadlo (Uncrewed Aerial Vehicle – UAV) nevztahuje pouze k fyzickému letadlu, ale také k jeho integraci jako Uživatelského Zařízení (User Equipment – UE) v rámci mobilní sítě. Tato integrace umožňuje UAV využívat sítě 3GPP pro komunikaci Povelů a Řízení (Command and Control – [C2](/mobilnisite/slovnik/c2/)), sledování a datové spoje s užitečným zatížením. Systém 3GPP poskytuje konektivní infrastrukturu, která vyžaduje vylepšení pro podporu specifických požadavků UAV, jako jsou služby založené na nadmořské výšce, mobilita, identifikace a zabezpečení.

Z architektonického hlediska se UAV připojuje k síti jako jakékoli jiné UE, ale je asociováno s dodatečnými síťovými funkcemi a externími systémy. Mezi klíčové síťové entity patří Funkce Řízení Přístupu a Mobility (Access and Mobility Management Function – [AMF](/mobilnisite/slovnik/amf/)) pro registraci a mobilitu, Funkce Řízení Relací (Session Management Function – [SMF](/mobilnisite/slovnik/smf/)) pro správu [PDU](/mobilnisite/slovnik/pdu/) relací a Funkce Vystavení Síťových Schopností (Network Exposure Function – [NEF](/mobilnisite/slovnik/nef/)) pro zpřístupnění síťových schopností externím Poskytovatelům Služeb [UAS](/mobilnisite/slovnik/uas/) (UAS Service Suppliers – [USS](/mobilnisite/slovnik/uss/)) nebo Řízení Letového Provozu UAS (UAS Traffic Management – [UTM](/mobilnisite/slovnik/utm/)). Předplatné a autorizace UAV spravuje Jednotná Správa Dat (Unified Data Management – UDM). Samotné UAV může mít specifické schopnosti, jako je reportování své 3D polohy (zeměpisná šířka, délka, nadmořská výška) a identity UAV, které jsou komunikovány síti přes Řídicí Rovinu (Control Plane) nebo Uživatelskou Rovinu (User Plane).

Princip fungování: UAV, vybavené modemem 3GPP, se připojí k síti. Během registrace může indikovat své schopnosti UAV. Síť pak může uplatnit specifické politiky, jako je omezení služby na určité geografické zóny (geo-fencing) nebo zvýšení priority jeho C2 provozu. Pro sledování může síť poskytovat služby určování polohy (např. prostřednictvím LTE Positioning Protocol nebo 5G NR positioning) autorizovaným externím entitám (jako je UASS) na základě předplatného. Komunikace C2 UAV typicky využívá vyhrazenou PDU relaci se zaručenou QoS (nízké zpoždění, vysoká spolehlivost). Síť komunikuje se systémy UTM za účelem výměny informací o letové autorizaci, telemetrii a řízení letového provozu, čímž vytváří soudržný ekosystém pro bezpečné operace UAV.

## K čemu slouží

Standardizace podpory UAV v 3GPP řeší kritickou potřebu spolehlivé, rozlehlé a zabezpečené komunikační sítě pro drony, zejména pro operace mimo vizuální dohled (Beyond Visual Line of Sight – BVLOS). Tradiční komunikace dronů byla závislá na přímých rádiových spojích (např. Wi-Fi, proprietární C2) s omezeným dosahem a bez plynulé mobility, což bránilo škálovatelným komerčním aplikacím. Mobilní sítě nabízejí všudypřítomné pokrytí, vysokou spolehlivost, zabezpečení a pokročilé funkce, jako je síťové dělení (network slicing).

Práce zahájená ve vydání 14 jako studijní položka byla motivována rychlým růstem průmyslu dronů a regulatorními tlaky na Řízení Letového Provozu UAS (UAS Traffic Management – UTM). Sítě 3GPP řeší omezení předchozích přístupů poskytováním řízené infrastruktury s podporou QoS. To umožňuje rozmanité aplikace, jako je letecká doprava, sledování a inspekce. Vývoj v následujících vydáních kontinuálně vylepšoval podporu, přidával funkce jako identifikace UAV, reportování nadmořské výšky, zmírnění interference s pozemními uživateli a přímá komunikace UAV-síť a UAV-UAV, čímž pozice mobilní technologie jako základního prvku umožňujícího budoucnost autonomních leteckých systémů.

## Klíčové vlastnosti

- Funguje jako Uživatelské Zařízení (User Equipment – UE) 3GPP s rozšířenými schopnostmi pro leteckou konektivitu
- Podporuje komunikaci Povelů a Řízení (Command and Control – C2) se zaručenou QoS s nízkým zpožděním a vysokou spolehlivostí
- Poskytuje síti a autorizovaným externím systémům reportování 3D polohy (včetně nadmořské výšky)
- Umožňuje identifikaci a autentizaci UAV pro regulatorní shodu a zabezpečení
- Usnadňuje integraci s Řízením Letového Provozu UAS (UAS Traffic Management – UTM) prostřednictvím síťových funkcí pro vystavení schopností
- Podporuje funkce jako letecké geografické ohraničení (aerial geo-fencing), autorizaci letové trasy a zmírnění interference

## Související pojmy

- [UAS – NF Uncrewed Aerial System Network Function](/mobilnisite/slovnik/uas/)
- [UASS – UAS Application Specific Server](/mobilnisite/slovnik/uass/)
- [UTM – Uncrewed Aerial System Traffic Management](/mobilnisite/slovnik/utm/)
- [UE – User Equipment](/mobilnisite/slovnik/ue/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.125** (Rel-19) — UAS Requirements via 3GPP System
- **TS 22.261** (Rel-20) — 5G System Service Requirements
- **TS 22.825** (Rel-16) — UAS Remote Identification and Tracking over 3GPP
- **TR 22.862** (Rel-14) — Critical Communications Feasibility Study
- **TS 23.255** (Rel-19) — UAS Application Layer Support
- **TS 23.256** (Rel-19) — UAS Support Architecture Enhancements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.755** (Rel-17) — Study on app layer support for UAS
- **TS 24.257** (Rel-19) — UAS Application Enabler (UAE) Layer
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 28.853** (Rel-19) — Charging for Uncrewed Aerial Systems
- **TS 29.255** (Rel-19) — USS Services for UAS in 5G
- … a dalších 17 specifikací

---

📖 **Anglický originál a plná specifikace:** [UAV na 3GPP Explorer](https://3gpp-explorer.com/glossary/uav/)
