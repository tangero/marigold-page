---
slug: "srns"
url: "/mobilnisite/slovnik/srns/"
type: "slovnik"
title: "SRNS – Serving Radio Network Subsystem"
date: 2025-01-01
abbr: "SRNS"
fullName: "Serving Radio Network Subsystem"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/srns/"
summary: "SRNS je soubor síťových prvků UTRAN, především obslužného RNC (SRNC) a jím řízených Node Bs, který poskytuje službu přenosového rádiového kanálu (radio access bearer service) konkrétnímu uživatelskému"
---

SRNS je soubor prvků UTRAN, především obslužného RNC (Serving RNC) a jeho Node Bs, který poskytuje službu přenosového rádiového kanálu (radio access bearer) a funguje jako aktivní rádiový přístupový bod připojení pro konkrétní uživatelské zařízení (UE).

## Popis

Serving Radio Network Subsystem (SRNS) je logické seskupení v rámci pozemní rádiové přístupové sítě UMTS ([UTRAN](/mobilnisite/slovnik/utran/)), které zahrnuje všechny rádiové síťové entity zodpovědné za spojení konkrétního uživatelského zařízení (UE) v daném čase. Jeho klíčovou součástí je Serving Radio Network Controller ([SRNC](/mobilnisite/slovnik/srnc/)), který drží spojení řídicí roviny ([RRC](/mobilnisite/slovnik/rrc/)) a spravuje rádiové zdroje pro UE. SRNS také zahrnuje jednu nebo více stanic Node B (základnových stanic), které jsou aktuálně zapojeny do rádiové komunikace s UE, například ty v aktivní sadě při měkkém předání spojení.

Funkčně je SRNS stranou UTRAN pro přenosový rádiový kanál (Radio Access Bearer, [RAB](/mobilnisite/slovnik/rab/)), což je služba poskytovaná jádrem sítě (CN) uživatelskému zařízení pro přenos uživatelských dat. SRNS je zodpovědné za zřizování, udržování a uvolňování těchto RABů na žádost jádra sítě. Mapuje parametry kvality služeb (QoS) RABu na příslušné přenosové a rádiové zdroje napříč rozhraními Iub a Uu. SRNS spravuje mobilitu UE v rámci své pokryté oblasti, provádí předání spojení a aktualizuje aktivní sadu buněk.

Klíčovým architektonickým aspektem je procedura přesunu SRNS (SRNS relocation). Když se UE přesune tak, že jiný [RNC](/mobilnisite/slovnik/rnc/) se stane vhodnějším pro roli SRNC (např. z důvodu efektivity nebo protože rozhraní Iur není dostupné), je role SRNS převedena ze starého SRNC na nový RNC. Tento postup zahrnuje přenos celého kontextu UE, včetně bezpečnostních klíčů a konfigurací rádiových kanálů, na nový RNC, který se poté stává novým SRNC a naváže přímé spojení Iu s jádrem sítě. Koncept SRNS tedy definuje jasný 'kotvicí bod' v UTRAN pro každé UE, což zjednodušuje směrování v jádru sítě a správu mobility.

## K čemu slouží

Koncept SRNS byl zaveden, aby poskytl jasnou a řiditelnou abstrakci pro roli rádiové přístupové sítě při obsluze mobilního uživatele. Ve složité, decentralizované architektuře [UTRAN](/mobilnisite/slovnik/utran/) s potenciálně více [RNC](/mobilnisite/slovnik/rnc/) a rozšířeným měkkým předáním spojení bylo nutné definovat pro každé UE z pohledu jádra sítě jediný, odpovědný subsystém. Tím byl vyřešen problém, že jádro sítě potřebovalo komunikovat s potenciálně proměnlivou skupinou RNC při pohybu uživatele; místo toho komunikuje pouze s aktuálním SRNS (prostřednictvím [SRNC](/mobilnisite/slovnik/srnc/)).

Řešil omezení dřívějších buněčných systémů, kde byla řídicí entita (jako BSC v GSM) staticky vázána na skupinu základnových stanic. SRNS je dynamické přiřazení, které může následovat uživatele, umožněné rozhraním Iur a procedurami přesunu SRNS. To bylo zásadní pro podporu plynulé mobility a kontinuity služeb pro paketově i okruhově přepínané služby v 3G, zejména pro aplikace v reálném čase.

Model SRNS navíc čistě odděluje agendu řízení rádiových zdrojů (řešenou v rámci SRNS) od směrování v jádru sítě a řízení služeb. Poskytuje stabilní koncový bod pro rozhraní Iu, což umožňuje jádru sítě zacházet s rádiovým přístupem jako se službu poskytujícím subsystémem, což později usnadnilo vývoj k plošším architekturám v LTE, kde bylo mnoho funkcí SRNC distribuováno do základnových stanic (eNB).

## Klíčové vlastnosti

- Logicky seskupuje SRNC a jím asociované aktivní Node Bs obsluhující konkrétní UE
- Funguje jako koncový bod služby UTRAN pro jeden nebo více přenosových rádiových kanálů (RAB)
- Odpovídá za provádění procedur přesunu SRNS (SRNS relocation) k přenosu obslužné role mezi RNC
- Spravuje mapování parametrů kvality služeb (QoS) RABu na rádiové a přenosové síťové zdroje
- Udržuje kontext UE, včetně bezpečnostních informací a konfigurací rádiových kanálů
- Poskytuje rozhraní (Iu) mezi UTRAN a jádrem sítě (Core Network) pro spojení UE

## Související pojmy

- [SRNC – Serving Radio Network Controller](/mobilnisite/slovnik/srnc/)
- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.236** (Rel-19) — Intra Domain Connection of RAN Nodes to Multiple CN Nodes
- **TR 23.923** (Rel-4) — Mobile IP+ Feasibility Study for UMTS/GPRS
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.321** (Rel-19) — MAC Protocol Specification for UTRAN
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.410** (Rel-19) — Iu Interface Introduction for UTRAN
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)
- **TS 25.415** (Rel-19) — Iu Interface User Plane Protocol
- … a dalších 5 specifikací

---

📖 **Anglický originál a plná specifikace:** [SRNS na 3GPP Explorer](https://3gpp-explorer.com/glossary/srns/)
