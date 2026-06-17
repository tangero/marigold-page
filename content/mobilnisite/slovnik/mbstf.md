---
slug: "mbstf"
url: "/mobilnisite/slovnik/mbstf/"
type: "slovnik"
title: "MBSTF – Multicast/Broadcast Service Transport Function"
date: 2026-01-01
abbr: "MBSTF"
fullName: "Multicast/Broadcast Service Transport Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mbstf/"
summary: "Síťová funkce 5G, která efektivně doručuje multicastový a broadcastový provoz více uživatelským zařízením (UE). Optimalizuje využití síťových prostředků umožněním distribuce dat typu point-to-multipoi"
---

MBSTF je síťová funkce 5G, která efektivně doručuje multicastový a broadcastový provoz více uživatelským zařízením (UE) tím, že umožňuje distribuci dat typu point-to-multipoint.

## Popis

Multicast/Broadcast Service Transport Function (MBSTF) je síťová funkce jádra sítě zavedená v architektuře systému 5G (5GS) pro podporu doručování služby Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). Působí v rámci jádra 5G sítě (5GC) a je zodpovědná za správu přenosu multicastových a broadcastových dat v uživatelské rovině. MBSTF komunikuje s ostatními síťovými funkcemi, jako je Session Management Function ([SMF](/mobilnisite/slovnik/smf/)) a User Plane Function ([UPF](/mobilnisite/slovnik/upf/)), za účelem zřízení a udržování multicastových/broadcastových relací. Zpracovává klíčové procedury včetně oznámení, modifikace a ukončení relace, čímž zajišťuje efektivní distribuci dat do rádiové přístupové sítě (RAN) pro přenos k uživatelskému zařízení (UE).

Z architektonického hlediska může být MBSTF nasazena jako samostatná funkce nebo integrována s jinými funkcemi uživatelské roviny. Přijímá multicastový/broadcastový provoz od poskytovatelů obsahu nebo od UPF a přeposílá jej pomocí IP multicast protokolů směrem k uzlům RAN (gNB). Tato funkce podporuje jak broadcastový režim, kdy jsou data odesílána všem UE v servisní oblasti, tak multicastový režim, kdy jsou data odesílána pouze těm UE, která se připojila ke konkrétní multicastové skupině. Spolupracuje s Broadcast/Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) při poskytování služeb a s Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) při registraci UE pro multicastové služby.

MBSTF hraje klíčovou roli v optimalizaci síťových prostředků tím, že snižuje duplicitní přenosy stejných dat přes jádro sítě. Namísto odesílání jednotlivých datových proudů každému UE agreguje provoz a využívá doručování typu point-to-multipoint, což je zvláště výhodné pro obsah s vysokou poptávkou, jako jsou živá sportovní utkání nebo nouzová hlášení. Podporuje dynamickou správu relací, což síťovým operátorům umožňuje škálovat služby na základě poptávky a spravovat parametry Quality of Service (QoS) pro multicastové toky. Funkce také zahrnuje bezpečnostní mechanismy a integruje se s funkcemi pro autentizaci a správu klíčů, aby zajistila, že multicastový obsah je doručován bezpečně pouze autorizovaným uživatelům.

## K čemu slouží

MBSTF byla vytvořena pro řešení rostoucí poptávky po efektivních službách skupinové komunikace v sítích 5G. Předchozí generace, jako 4G LTE, podporovaly [MBMS](/mobilnisite/slovnik/mbms/) prostřednictvím [BM-SC](/mobilnisite/slovnik/bm-sc/) a [MCE](/mobilnisite/slovnik/mce/) (Multi-cell/multicast Coordination Entity), ale architektura nebyla plně integrována do jádra sítě jako standardizovaná funkce. To vedlo k omezením ve škálovatelnosti, flexibilitě a podpoře nových případů užití 5G, jako je massive IoT a ultra-spolehlivá nízkolatenční komunikace (URLLC). MBSTF poskytuje nativní, cloud-nativní přístup k multicastu/broadcastu v rámci 5GC, což umožňuje bezproblémové poskytování služeb v různých scénářích nasazení.

Primární problém, který řeší, je neefektivní využití síťové šířky pásma při doručování stejného obsahu více uživatelům. Tradiční unicastové doručování by vyžadovalo samostatné datové proudy pro každého uživatele, což by zatěžovalo síť a zvyšovalo latenci. MBSTF umožňuje síťovým operátorům odlehčovat oblíbený obsah prostřednictvím multicastu, čímž snižuje zatížení jádra sítě a zlepšuje uživatelský zážitek. To je zvláště důležité pro aplikace náročné na šířku pásma, jako je streamování videa v rozlišení 4K/8K, kde se unicastové doručování během špičkové poptávky stává neudržitelným.

Dále MBSTF podporuje vznikající služby 5G, jako je komunikace Vehicle-to-Everything (V2X), sítě pro veřejnou bezpečnost a softwarové aktualizace pro zařízení IoT. Poskytnutím standardizovaného, škálovatelného mechanismu pro skupinové doručování dat usnadňuje komercializaci multicastových/broadcastových služeb a umožňuje operátorům nové zdroje příjmů. Integrace této funkce s network slicing také umožňuje vyhrazené multicastové řezy pro konkrétní služby, což zajišťuje izolaci výkonu a přizpůsobené QoS.

## Klíčové vlastnosti

- Doručování dat v uživatelské rovině typu point-to-multipoint pro multicastový a broadcastový provoz
- Integrace se síťovými funkcemi jádra 5G (SMF, UPF, AMF) pro správu relací
- Podpora dynamického zřizování, modifikace a ukončování multicastových relací
- Vynucování QoS pro multicastové toky, včetně priority a alokace šířky pásma
- Bezpečnostní integrace pro autentizaci a šifrování multicastového obsahu
- Podpora network slicing pro umožnění vyhrazených instancí multicastových služeb

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 26.502** (Rel-19) — 5G Multicast-Broadcast User Services Architecture
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.517** (Rel-19) — 5G MBS User Service Protocols and Formats
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation
- **TS 29.532** (Rel-19) — MB-SMF Service Based Interface Protocol
- **TS 29.580** (Rel-19) — 5G MBSF Service Interface Stage 3 Specification
- **TS 29.581** (Rel-19) — MBSTF Service Based Interface Protocol Specification
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TR 33.850** (Rel-17) — 5G MBS Security Study

---

📖 **Anglický originál a plná specifikace:** [MBSTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mbstf/)
