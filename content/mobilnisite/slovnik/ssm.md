---
slug: "ssm"
url: "/mobilnisite/slovnik/ssm/"
type: "slovnik"
title: "SSM – Source Specific IP Multicast"
date: 2025-01-01
abbr: "SSM"
fullName: "Source Specific IP Multicast"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ssm/"
summary: "Model doručování IP multicastu, ve kterém je provoz směrován pouze z konkrétní zdrojové adresy na adresu multicastové skupiny. Zlepšuje bezpečnost a efektivitu oproti tradičnímu multicastu z libovolné"
---

SSM je model doručování IP multicastu, ve kterém je provoz směrován pouze z konkrétní zdrojové adresy na adresu multicastové skupiny.

## Popis

Source Specific IP Multicast (SSM) je model služby Internet Protocol (IP) multicast definovaný [IETF](/mobilnisite/slovnik/ietf/) a přijatý v architekturách 3GPP pro efektivní distribuci multimediálního obsahu. Na rozdíl od multicastu z libovolného zdroje (ASM), kde se příjemci připojí ke skupině G a přijímají data od libovolného odesílatele do této skupiny, vyžaduje SSM, aby příjemci specifikovali jak adresu multicastové skupiny G, tak konkrétní zdrojovou adresu S, čímž vytvoří kanál (S,G). Tento model zásadně mění mechanizmy přihlašování k multicastu a směrování. Příjemce vyjádří zájem odesláním hlášení protokolu [IGMP](/mobilnisite/slovnik/igmp/) nebo [MLD](/mobilnisite/slovnik/mld/) pro kanál (S,G). Multicastové směrovací protokoly v síti (jako Protocol Independent Multicast - Sparse Mode v SSM, PIM-SSM) poté vytvoří zdrojově specifické distribuční stromy od určeného zdroje S ke všem příjemcům kanálu (S,G).

V systémech 3GPP je SSM obzvláště relevantní pro architektury IP Multimedia Subsystem (IMS) a Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). Pro MBMS lze SSM použít jako metodu IP multicastového směrování pro doručování obsahu přes síť jádra k více základnovým stanicím. [BM-SC](/mobilnisite/slovnik/bm-sc/) (Broadcast Multicast Service Center) funguje jako zdroj (S) a UEs se připojují ke konkrétnímu kanálu (S,G), aby přijímaly vysílací nebo multicastový proud. Tato architektura zjednodušuje provoz sítě tím, že odstraňuje potřebu sdílených setkávacích bodů (RPs) používaných v ASM, a poskytuje inherentně základní úroveň řízení přístupu, protože příjemci získávají data pouze od předem oznámeného zdroje.

Provoz zahrnuje několik klíčových komponent: zdroj obsahu (např. BM-SC), IP multicastové směrovače v síti jádra a UE, které podporuje IGMP/MLD. BM-SC oznamuje informace o kanálu (S,G) prostřednictvím procedur oznámení služby. Když si UE přeje službu přijímat, aktivuje připojení (join) k tomuto konkrétnímu kanálu. Zpráva o připojení se šíří směrem ke zdroji po jednotlivých skocích a vytváří distribuční strom. Data ze zdroje pak proudí tímto stromem ke všem připojeným příjemcům. Tento model je vysoce efektivní pro distribuci lineárních médií (jako živé [TV](/mobilnisite/slovnik/tv/)) od jednoho k mnoha, protože vytváří optimální směrovací cesty a zabraňuje tomu, aby provoz z neautorizovaných nebo nezamýšlených zdrojů dosáhl skupiny.

## K čemu slouží

SSM byl vyvinut, aby překonal provozní a bezpečnostní složitosti spojené s původním modelem multicastu z libovolného zdroje (ASM). ASM čelil výzvám s objevováním zdrojů (vyžadující mechanismy jako MSDP), zranitelnosti vůči útokům typu odepření služby od falešných zdrojů vysílajících do skupiny a složitému mezidoménovému směrování. SSM tyto problémy řeší tím, že činí zdroj explicitní součástí přihlášení, což zjednodušuje návrh protokolu, zvyšuje bezpečnost omezením platných zdrojů a zlepšuje škálovatelnost pro rozsáhlou distribuci obsahu.

V kontextu 3GPP bylo přijetí SSM motivováno požadavky na efektivní vysílací a multicastové služby, počínaje [MBMS](/mobilnisite/slovnik/mbms/) ve vydání 6. Doručování stejného obsahu (např. živé sportovní události) tisícům UEs vyžaduje efektivní mechanismus IP multicastu v síti jádra. SSM poskytl čistší a lépe spravovatelný model než ASM pro toto řízené prostředí, kde je zdroj ([BM-SC](/mobilnisite/slovnik/bm-sc/) poskytovatele služeb) vždy známý a autorizovaný. Vyřešil problém, jak efektivně škálovat vysílací služby založené na IP přes mobilní sítě bez režie a bezpečnostních rizik obecnějšího modelu ASM. Jeho zařazení podpořilo komerční nasazení služeb mobilní televize a skupinové komunikace.

## Klíčové vlastnosti

- Definuje multicastové kanály jako dvojici (Zdroj, Skupina) (S,G)
- Odstraňuje potřebu protokolů pro objevování zdrojů, jako je MSDP
- Vytváří zdrojově specifické stromy nejkratších cest pro efektivní směrování
- Poskytuje inherentní základní řízení přístupu specifikací legitimního zdroje
- Zjednodušuje alokaci adres, protože rozsah 232.0.0.0/8 je vyhrazen pro SSM
- Podporován IGMPv3/MLDv2 v hostitelích a PIM-SSM ve směrovačích

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)

## Definující specifikace

- **TS 23.246** (Rel-19) — MBMS Bearer Service Stage 2 Description
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.522** (Rel-19) — 5G NEF Northbound APIs Stage 3

---

📖 **Anglický originál a plná specifikace:** [SSM na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssm/)
