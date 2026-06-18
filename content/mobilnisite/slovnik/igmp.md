---
slug: "igmp"
url: "/mobilnisite/slovnik/igmp/"
type: "slovnik"
title: "IGMP – Internet Group Management Protocol"
date: 2025-01-01
abbr: "IGMP"
fullName: "Internet Group Management Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/igmp/"
summary: "Protokol síťové vrstvy používaný IP hostiteli a přilehlými multicast směrovači k vytváření a správě členství ve multicast skupinách. Umožňuje efektivní distribuci dat typu jeden-vůči-mnoha, což je klí"
---

IGMP je protokol síťové vrstvy používaný IP hostiteli a přilehlými multicast směrovači k vytváření a správě členství ve multicast skupinách pro efektivní distribuci dat typu jeden-vůči-mnoha v sítích 3GPP.

## Popis

Internet Group Management Protocol (IGMP) je základní součástí pro IP multicast komunikaci v paketových sítích 3GPP. Funguje mezi hostitelem (například uživatelským zařízením – UE) a jeho přímo připojeným multicast směrovačem, který se typicky nachází v Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) nebo Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) ve starších, respektive novějších architekturách. Hostitelé používají IGMP k hlášení svého členství ve multicast skupině sousedním směrovačům a směrovače jej používají k dotazování na členství ve multicast skupinách hostitelů na svých přímo připojených podsítích. Tento protokol je zásadní pro efektivní doručování multicast provozu, jako je živý videostream nebo distribuce obsahu, přes mobilní sítě.

IGMP funguje prostřednictvím série výměn zpráv. Hlavními typy zpráv jsou Membership Query, odesílaná směrovačem pro zjištění, které multicast skupiny mají členy na jeho připojených linkách; a Membership Report, odesílaná hostitelem, aby vyjádřil zájem o připojení ke konkrétní multicast skupině, nebo jako odpověď na dotaz. Třetí typ, zpráva Leave Group, umožňuje hostiteli signalizovat odchod ze skupiny, což směrovačům umožňuje implementovat mechanismy rychlejšího opuštění. V kontextu 3GPP vystupuje UE jako IGMP hostitel. Protokolové zprávy jsou typicky tunelovány v rámci Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)) kontextu nebo [PDN](/mobilnisite/slovnik/pdn/) spojení mezi UE a bránou. Brána, fungující jako multicast směrovač, tyto zprávy zpracovává a komunikuje s infrastrukturou multicast směrování IP (např. pomocí Protocol Independent Multicast – [PIM](/mobilnisite/slovnik/pim/)), aby spravovala tok multicast provozu od zdroje do mobilní páteřní sítě.

Úlohou protokolu je správa členství ve skupinách na základě jednotlivých spojů. Když si UE přeje přijímat provoz pro konkrétní multicast skupinovou adresu, odešle pro tuto skupinu nevyžádanou IGMP zprávu Membership Report. Směrovač tuto zprávu přijme a pokud již pro danou skupinu provoz nepřijímá, zahájí proces připojení k příslušnému stromu distribuce multicast. Směrovač také periodicky posílá obecné dotazovací zprávy (General Query) na multicast adresu 'all-hosts'. Všichni hostitelé naslouchající multicast musí odpovědět hlášeními pro skupiny, o které mají stále zájem, což směrovači umožňuje odstranit skupiny, které již nemají žádné lokální členy. Tento stav je udržován v IGMP cache směrovače. Pro 3GPP je tento mechanismus přizpůsoben pro práci přes logický point-to-point spoj reprezentovaný [GTP](/mobilnisite/slovnik/gtp/) tunelem mezi UE a sítí, což zajišťuje efektivní využití rádiových a páteřních síťových prostředků pro multicast služby.

## K čemu slouží

IGMP byl do standardů 3GPP integrován, aby umožnil efektivní IP multicast služby přes mobilní sítě. Před jeho přijetím by doručení stejného obsahu více uživatelům (např. živého sportovního přenosu) vyžadovalo samostatné unicast proudy ke každému účastníkovi, což vedlo k masivní duplikaci dat a neefektivnímu využití kapacity sítě, zejména na rozhraní radiového přístupu. Hlavní problém, který IGMP řeší, je umožnění škálovatelných modelů komunikace jeden-vůči-mnoha a mnoho-vůči-mnoha v rámci IP frameworku paketového jádra 3GPP.

Jeho vznik motivovala rostoucí poptávka po službách skupinové komunikace náročných na šířku pásma, jako je mobilní [TV](/mobilnisite/slovnik/tv/) ([MBMS](/mobilnisite/slovnik/mbms/)), distribuce obsahu a služby push-to-talk. Tím, že umožňuje UE dynamicky se připojovat k multicast skupinám a opouštět je, poskytuje IGMP síti inteligenci k doručování multicast paketů pouze tam, kde jsou požadovány, a tím optimalizuje využití prostředků. Toto bylo klíčovým předpokladem pro službu Multimedia Broadcast Multicast Service (MBMS) v 3GPP, kde IGMP (a jeho protějšek pro IPv6, MLD) slouží jako signalizační protokol, kterým UE signalizuje svůj zájem o konkrétní obsahové proudy MBMS doručované přes IP vrstvu.

## Klíčové vlastnosti

- Hlášení členství od hostitele pro připojení k multicast skupinám
- Dotazování směrovače pro zjišťování členství ve skupinách
- Explicitní zprávy o opuštění skupiny pro efektivní odchod
- Podpora více verzí IGMP (v1, v2, v3) pro zpětnou kompatibilitu a filtrování zdrojů
- Provoz přes logické point-to-point spoje v tunelech GTP 3GPP
- Základ pro signalizaci na IP vrstvě při poskytování služby MBMS

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [PIM – Protocol-Independent Multicast](/mobilnisite/slovnik/pim/)
- [MLD – Multicast Listener Discovery](/mobilnisite/slovnik/mld/)

## Definující specifikace

- **TS 23.316** (Rel-19) — Wireline and Wireless Convergence Access Support
- **TS 23.846** (Rel-6) — MBMS Architecture and Functionality
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- **TS 29.281** (Rel-19) — GTPv1-U Protocol Specification
- **TS 33.820** (Rel-8) — Home NodeB/eNodeB Security Architecture

---

📖 **Anglický originál a plná specifikace:** [IGMP na 3GPP Explorer](https://3gpp-explorer.com/glossary/igmp/)
