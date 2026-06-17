---
slug: "g-pdu"
url: "/mobilnisite/slovnik/g-pdu/"
type: "slovnik"
title: "G-PDU – GTP encapsulated user Plane Data Unit"
date: 2025-01-01
abbr: "G-PDU"
fullName: "GTP encapsulated user Plane Data Unit"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/g-pdu/"
summary: "Jednotka dat, která zapouzdřuje provoz uživatelské roviny v rámci protokolu GTP pro přenos přes páteřní síť. Je zásadní pro přenos uživatelských dat (např. IP paketů) mezi síťovými uzly, jako je SGW a"
---

G-PDU je GTP zapouzdřená jednotka dat uživatelské roviny, která přenáší provoz, jako jsou IP pakety, mezi uzly páteřní sítě pro efektivní tunelování a správu mobility.

## Popis

G-PDU je specifický formát paketu definovaný v rámci sady protokolů [GPRS](/mobilnisite/slovnik/gprs/) Tunnelling Protocol ([GTP](/mobilnisite/slovnik/gtp/)), standardizovaný v 3GPP TS 29.281 pro protokol [GTP-U](/mobilnisite/slovnik/gtp-u/) a odkazovaný v TS 29.274 pro řídicí rovinu. Představuje zapouzdřený obsah dat uživatelské roviny, který je tunelován mezi koncovými body GTP-U, jako je například mezi eNodeB/gNB a Serving Gateway (SGW), nebo mezi bránami (SGW a PGW) v Evolved Packet Core (EPC). Proces zapouzdření zahrnuje vzít původní datový paket uživatele (např. IP paket od UE) a přidat hlavičku GTP-U a typicky také hlavičku transportní vrstvy UDP/IP. Hlavička GTP-U obsahuje klíčová pole, jako je Tunnel Endpoint Identifier (TEID), který jednoznačně identifikuje GTP tunel pro konkrétní přenos uživatele, čísla sekvence pro detekci ztrát a indikátory typu zprávy. Tato struktura umožňuje multiplexovat více datových toků uživatelů přes stejné spojení transportní sítě, které jsou logicky odděleny svými TEID.

V síťové architektuře jsou G-PDU hlavním nástrojem uživatelské roviny, přenášejícím skutečná data účastníka. Když UE naváže PDN spojení nebo PDU relaci, je zřízen jeden nebo více EPS bearerů nebo QoS toků, z nichž každý je asociován s konkrétním GTP tunelem identifikovaným párem TEID. Jak datové pakety přicházejí od UE do základnové stanice, jsou zapouzdřeny do G-PDU a přeposlány na příslušnou bránu na základě TEID. Přijímající koncový bod GTP-U dekapuluje G-PDU odstraněním hlavičky GTP-U a přepošle původní obsah na jeho další cíl, ať už uvnitř páteřní sítě, nebo do externí paketové datové sítě. Tento tunelovací mechanismus je transparentní pro uživatelská data a poskytuje konzistentní metodu přenosu dat, která je nezávislá na podkladové technologii rádiového přístupu (např. LTE, NR nebo i ne-3GPP přístup).

Role G-PDU přesahuje jednoduché tunelování. Podporuje procedury správy cesty, jako jsou Echo Requests/Responses pro ověření dostupnosti protistrany. Zařazení čísel sekvence do hlavičky (volitelné pro některá rozhraní) umožňuje mechanismy doručování ve správném pořadí a detekce ztrát, což je zvláště důležité pro rozhraní mezi uzly, kde může docházet k přeřazení paketů. V systémech 5G, zatímco protokol páteřní sítě mezi (R)[AN](/mobilnisite/slovnik/an/) a [UPF](/mobilnisite/slovnik/upf/) je stále GTP-U (rozhraní N3) nebo potenciálně jiné protokoly, základní koncept tunelované jednotky dat uživatelské roviny přetrvává. Formát G-PDU zajišťuje zpětnou kompatibilitu a interoperabilitu mezi síťovými prvky 4G a 5G a tvoří stabilní páteř pro mobilní broadband a další služby.

## K čemu slouží

G-PDU bylo vytvořeno, aby poskytlo standardizovanou, efektivní a škálovatelnou metodu pro přenos dat uživatelské roviny přes paketovou páteřní síť v systémech 3GPP. Před jeho formální definicí v rámci [GTP](/mobilnisite/slovnik/gtp/) vyžadovaly rané systémy [GPRS](/mobilnisite/slovnik/gprs/) mechanismus pro oddělení a směrování jednotlivých datových toků uživatelů přes síťové uzly, které obsluhují miliony účastníků. G-PDU jako součást GTP řeší problém multiplexování uživatelských dat a správy mobility zavedením paradigmatu tunelování. Umožňuje páteřní síti vytvářet logické kanály (tunely) pro uživatelská data, které jsou oddělené od řídicí signalizace, což umožňuje nezávislé škálování a správu datové roviny.

Jeho vytvoření bylo motivováno přechodem k plně IP sítím v 3GPP, počínaje GPRS a vývojem přes UMTS k EPS a 5GS. G-PDU poskytuje nezbytnou abstraktní vrstvu mezi IP pakety uživatele a transportní sítí (IP sítí) spojující uzly páteřní sítě. Tato abstrakce je klíčová pro podporu mobility účastníka; když se uživatel pohybuje, GTP tunely mohou být pře-směrovány (např. během procedur předání spojení nebo přepnutí cesty) bez ovlivnění IP relace uživatele. TEID v hlavičce G-PDU funguje jako lokální směrovací štítek, umožňující uzlům přeposílat pakety bez nutnosti prohlížení vnitřního IP obsahu, což zvyšuje efektivitu zpracování a podporuje různé typy provozu včetně IPv4, IPv6 a Ethernetových rámců.

Dále G-PDU standardizuje rozhraní mezi zařízeními různých výrobců, čímž zajišťuje interoperabilitu v sítích s více dodavateli. Definováním společného formátu paketu umožňuje, aby SGW od výrobce A mohlo bezproblémově vyměňovat uživatelská data s PGW od výrobce B. To byl klíčový faktor pro konkurenční ekosystém v mobilních páteřních sítích. Pokračující vývoj a používání formátu G-PDU napříč releasy, včetně 5G, zdůrazňuje jeho efektivitu v řešení základního problému agilního, tunelovaného přenosu uživatelské roviny v mobilních sítích.

## Klíčové vlastnosti

- Zapouzdřuje uživatelské IP pakety nebo Ethernetové rámce v hlavičce GTP-U
- Používá Tunnel Endpoint Identifier (TEID) pro logické multiplexování a směrování tunelů
- Podporuje volitelná čísla sekvence pro doručování ve správném pořadí a detekci ztrát
- Nezávislé na transportu, typicky přenášené přes sítě UDP/IP
- Umožňuje mobilitu tím, že umožňuje aktualizaci koncových bodů tunelu během předání spojení
- Poskytuje standardizovaný formát pro interoperabilitu více dodavatelů napříč rozhraními páteřní sítě

## Související pojmy

- [GTP-U – GPRS Tunnelling Protocol for User Plane](/mobilnisite/slovnik/gtp-u/)

## Definující specifikace

- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.281** (Rel-19) — GTPv1-U Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [G-PDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/g-pdu/)
