---
slug: "bm-sc"
url: "/mobilnisite/slovnik/bm-sc/"
type: "slovnik"
title: "BM-SC – Broadcast-Multicast Service Centre"
date: 2026-01-01
abbr: "BM-SC"
fullName: "Broadcast-Multicast Service Centre"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bm-sc/"
summary: "BM-SC je entita jádra sítě zodpovědná za správu a doručování obsahu služby Multimedia Broadcast Multicast Service (MBMS). Zajišťuje oznamování služeb, plánování relací, zabezpečení a synchronizaci obs"
---

BM-SC je entita jádra sítě, která spravuje a doručuje obsah služby Multimedia Broadcast Multicast Service (MBMS), zajišťuje oznamování služeb, plánování, zabezpečení a synchronizaci pro efektivní distribuci dat jeden-všem.

## Popis

Broadcast-Multicast Service Centre (BM-SC) je centrální funkční entita v architektuře 3GPP pro službu Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). Slouží jako vstupní bod pro poskytovatele obsahu k vložení vysílacího (broadcast) nebo skupinového (multicast) provozu do mobilní sítě a spravuje celý životní cyklus doručování služby MBMS. BM-SC komunikuje s externími zdroji obsahu a s Gateway [GPRS](/mobilnisite/slovnik/gprs/) Support Node (GGSN) nebo Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) jádra sítě v pozdějších vydáních specifikací a funguje jako autoritativní zdroj pro řízení relací MBMS a distribuci dat.

Z architektonického hlediska se BM-SC skládá z několika klíčových logických funkcí definovaných ve specifikacích 3GPP. Členská funkce (Membership Function) zajišťuje správu předplatného a autorizaci a určuje, kteří uživatelé mají nárok na příjem konkrétních služeb MBMS. Funkce správy relací a přenosu (Session and Transmission Function) spravuje plánování relací MBMS, včetně časů zahájení/ukončení a parametrů kvality služby. Proxy a přenosová funkce (Proxy and Transport Function) slouží jako přenosový bod pro data MBMS mezi poskytovateli obsahu a jádrem sítě, zatímco funkce oznamování služeb (Service Announcement Function) distribuuje informace o dostupných službách MBMS k uživatelským zařízením. Bezpečnostní funkce (Security Function) je zodpovědná za správu klíčů a šifrování, což zajišťuje, že k chráněnému obsahu mají přístup pouze autorizovaní uživatelé.

Během provozu BM-SC zahajuje relace MBMS odesláním požadavku na zahájení relace do jádra sítě, které následně zřídí potřebné přenosové kanály napříč rádiovou přístupovou sítí. BM-SC synchronizuje doručování obsahu pomocí protokolu [SYNC](/mobilnisite/slovnik/sync/), čímž zajišťuje, že všechny základnové stanice vysílají identická data v přesně koordinovaných časech, což je zásadní pro provoz Single Frequency Network ([MBSFN](/mobilnisite/slovnik/mbsfn/)), kde více buněk vysílá stejný obsah současně. BM-SC také spravuje sběr údajů pro účtování a komunikuje s fakturačními systémy, čímž poskytuje potřebné informace pro komerční nabídky služeb MBMS.

Po celou dobu trvání relace MBMS BM-SC monitoruje doručování služby a může upravovat přenosové parametry na základě stavu sítě a požadavků služby. Relace řádně ukončuje po dokončení doručení obsahu nebo podle plánu, čímž uvolňuje síťové prostředky. Centralizované řízení BM-SC umožňuje efektivní využití spektra koordinací vysílání napříč více buňkami, snižuje rušení a zlepšuje kvalitu příjmu na okrajích buněk díky zisku makro-diverzity v oblastech MBSFN.

## K čemu slouží

BM-SC byl vytvořen, aby vyřešil zásadní neefektivitu doručování populárního obsahu pomocí tradičních jednosměrných (unicast) metod v mobilních sítích. Před zavedením [MBMS](/mobilnisite/slovnik/mbms/), když více uživatelů ve stejné oblasti požadovalo stejný obsah (jako přímé přenosy sportovních událostí, zpravodajské relace nebo populární videa), musela síť navázat individuální spojení ke každému uživateli, což spotřebovávalo nadměrné množství rádiových prostředků a kapacity jádra sítě. Tento přístup se špatně škáloval a stal se ekonomicky neudržitelným pro hromadnou distribuci obsahu.

BM-SC umožňuje skutečné vysílací (broadcast) a skupinové (multicast) schopnosti v sítích 3GPP, což dovoluje, aby jeden přenos obsloužil více uživatelů současně v definované servisní oblasti. To dramaticky zlepšuje spektrální účinnost a snižuje zatížení sítě během období špičkové poptávky. Tato technologie byla motivována zejména rostoucí poptávkou po službách mobilní televize a videa v polovině roku 2000, stejně jako potřebou efektivní distribuce aktualizací softwaru, nouzových upozornění a další komunikace jeden-všem.

Kromě zvýšení efektivity poskytuje BM-SC standardizovaný rámec pro správu služeb, zabezpečení a účtování, který dříve u vysílacích služeb v mobilních sítích chyběl. Umožňuje komerční vysílací služby s řádnou správou předplatného, ochranou obsahu a integrací do fakturace. Architektura také podporuje jak vysílací režim (pro všechny uživatele v oblasti), tak skupinový režim (pro specifické skupiny předplatitelů), což poskytuje flexibilitu pro různé modely služeb a obchodní případy.

## Klíčové vlastnosti

- Správa a plánování relací MBMS
- Oznamování a vyhledávání služeb
- Synchronizace obsahu pro provoz MBSFN
- Správa předplatného a autorizace
- Zabezpečení a distribuce klíčů pro chráněný obsah
- Sběr údajů pro účtování a rozhraní k fakturačnímu systému

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [MBSFN – Multimedia Broadcast multicast service Single Frequency Network](/mobilnisite/slovnik/mbsfn/)
- [MCE – Multi-cell/multicast Coordination Entity](/mobilnisite/slovnik/mce/)
- [MBMS-GW – MBMS Gateway](/mobilnisite/slovnik/mbms-gw/)

## Definující specifikace

- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.222** (Rel-19) — Common API Framework for 3GPP Northbound APIs
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.468** (Rel-19) — Group Communication System Enablers for LTE
- **TS 23.479** (Rel-19) — MBMS API for Mission Critical Services
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 23.768** (Rel-12) — Group Communication System Enablers for LTE
- **TR 23.780** (Rel-14) — MBMS for Mission Critical Communication Services
- **TS 23.792** (Rel-16) — MBMS API for Mission Critical Services
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 23.846** (Rel-6) — MBMS Architecture and Functionality
- **TS 24.548** (Rel-19) — SEAL Network Resource Management Protocol
- **TS 26.237** (Rel-19) — IMS for PSS and MBMS Control
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- … a dalších 27 specifikací

---

📖 **Anglický originál a plná specifikace:** [BM-SC na 3GPP Explorer](https://3gpp-explorer.com/glossary/bm-sc/)
