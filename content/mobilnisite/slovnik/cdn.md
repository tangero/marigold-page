---
slug: "cdn"
url: "/mobilnisite/slovnik/cdn/"
type: "slovnik"
title: "CDN – Content Delivery Network / Content Distribution Network"
date: 2025-01-01
abbr: "CDN"
fullName: "Content Delivery Network / Content Distribution Network"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cdn/"
summary: "Distribuovaná síť serverů, která doručuje webový obsah a média uživatelům na základě geografické blízkosti. Snižuje latenci, odlehčuje zatížení původních serverů a zlepšuje kvalitu uživatelského zážit"
---

CDN je distribuovaná síť serverů, která doručuje webový obsah a média uživatelům na základě geografické blízkosti, aby se snížila latence a zlepšila kvalita uživatelského zážitku.

## Popis

Obsahová doručovací síť (Content Delivery Network, CDN) je geograficky distribuovaná síť proxy serverů a datových center navržená k zajištění vysoké dostupnosti a výkonu doručováním obsahu koncovým uživatelům z co nejoptimálnější lokality. V architekturách 3GPP jsou CDN integrovány za účelem efektivního poskytování multimediálního obsahu, softwarových aktualizací a webových aplikací přes mobilní sítě. Základní princip spočívá v ukládání obsahu do mezipaměti na hraničních serverech umístěných blíže uživateli, čímž se minimalizuje vzdálenost, kterou data musí urazit, snižuje se doba odezvy a zmírňuje se zahlcení páteřní sítě a původních serverů.

Z architektonického hlediska se CDN skládá z původních serverů hostujících původní obsah, hraničních serverů (nebo bodů přítomnosti, PoP) nasazených na strategických místech, systému směrování požadavků a systému správy obsahu. Mechanismus směrování požadavků, často využívající směrování založené na [DNS](/mobilnisite/slovnik/dns/) nebo anycast, inteligentně nasměruje požadavky uživatelů na nejbližší nebo nejméně vytížený hraniční server. Tento proces je pro uživatele transparentní a je založen na faktorech v reálném čase, jako je zatížení serveru, stav sítě a geografická poloha. Pro dynamický obsah nebo obsah, který není v mezipaměti, si jej hraniční server může vyžádat z původního serveru, často s využitím optimalizačních technik, jako je TCP akcelerace a komprese.

V rámci standardů 3GPP je integrace CDN specifikována pro podporu služeb, jako je Služba multimediálního vysílání skupině (Multimedia Broadcast Multicast Service, [MBMS](/mobilnisite/slovnik/mbms/)), pokročilá služba multimediálního vysílání skupině (evolved Multimedia Broadcast Multicast Service, eMBMS), a pozdějších vylepšení pro streamování médií v 5G. Specifikace definují rozhraní a procedury pro výběr CDN, směrování provozu a vynucování politik, což zajišťuje bezproblémový provoz s funkcemi mobilní páteřní sítě, jako je Funkce pravidel pro politiku a účtování (Policy and Charging Rules Function, [PCRF](/mobilnisite/slovnik/pcrf/)) a Funkce uživatelské roviny (User Plane Function, [UPF](/mobilnisite/slovnik/upf/)). Mezi klíčové komponenty patří CDN proxy, která komunikuje s uživatelským zařízením (UE), a CDN řadič, který spravuje politiky distribuce obsahu a strategie ukládání do mezipaměti.

Úloha CDN v mobilní síti je klíčová pro zvládnutí explozivního růstu datového provozu, zejména videa, který tvoří většinu mobilních dat. Ukládáním oblíbeného obsahu do mezipaměti na okraji sítě CDN snižují zatížení přístupové rádiové sítě (RAN) a přenosových spojů páteře, což umožňuje efektivnější využití síťových zdrojů. Také zlepšují kvalitu uživatelského zážitku (Quality of Experience, [QoE](/mobilnisite/slovnik/qoe/)) tím, že poskytují nižší latenci, vyšší propustnost a sníženou ztrátu paketů, což je zásadní pro aplikace v reálném čase, jako je živé streamování, video na vyžádání (Video on Demand, VoD) a online hraní. Mezi pokročilé funkce patří podpora adaptivního streamování s proměnnou datovou rychlostí (např. [DASH](/mobilnisite/slovnik/dash/), [HLS](/mobilnisite/slovnik/hls/)), přednačítání obsahu na základě předpovědi chování uživatelů a integrace s síťovým řezáním (network slicing) pro dedikované poskytování služeb.

## K čemu slouží

Hlavním účelem CDN v sítích 3GPP je řešení výzev způsobených rychlým nárůstem spotřeby mobilních dat, zejména multimediálního obsahu náročného na šířku pásma. Před integrací CDN byly všechny uživatelské požadavky na obsah obsluhovány přímo z centralizovaných původních serverů, což vedlo k vysoké latenci, zahlcení sítě a špatnému uživatelskému zážitku, zejména pro uživatele vzdálené od umístění serveru. Tento přístup byl neudržitelný, když se streamování videa a stahování velkých souborů staly dominantními typy provozu, což zatěžovalo síťovou infrastrukturu a zvyšovalo provozní náklady mobilních operátorů.

CDN byly zavedeny, aby tyto problémy vyřešily decentralizací doručování obsahu a jeho přiblížením koncovému uživateli. Tím se zkracuje vzdálenost, kterou data putují po síti, a minimalizuje se latence a kolísání zpoždění (jitter), což je klíčové pro služby v reálném čase. Navíc CDN odlehčují provoz z páteřní sítě a původních serverů, což jim umožňuje efektivně obsloužit více uživatelů a požadavků. To je obzvláště důležité v mobilních sítích, kde jsou rádiové zdroje omezené a drahé; ukládáním obsahu do mezipaměti na okraji sítě CDN snižují množství dat, která je nutné přenášet přes RAN, čímž zlepšují celkovou kapacitu a výkon sítě.

Historicky se CDN objevily v ekosystému pevného internetu, ale jejich integrace do standardů 3GPP začala ve vydání 6 za účelem podpory mobilních požadavků, jako je správa mobility, optimalizace s ohledem na síť a integrace s funkcemi mobilní páteře. Tento vývoj byl motivován potřebou poskytovat konzistentní vysoce kvalitní zážitky pro mobilní uživatele, podporovat nové služby jako mobilní [TV](/mobilnisite/slovnik/tv/) a streamování videa a umožnit operátorům efektivní distribuci obsahu. CDN také usnadňují snížení nákladů díky nižším nákladům na přenos a partnerské spojení (peering), zlepšení škálovatelnosti a umožnění nových zdrojů příjmů prostřednictvím vylepšené nabídky služeb.

## Klíčové vlastnosti

- Geograficky distribuované hraniční servery pro doručování obsahu s nízkou latencí
- Inteligentní směrování požadavků využívající DNS nebo anycast k nasměrování uživatelů na optimální servery
- Ukládání obsahu do mezipaměti a replikace ke snížení zatížení původních serverů a využití šířky pásma
- Podpora protokolů pro adaptivní streamování s proměnnou datovou rychlostí, jako jsou DASH a HLS
- Integrace s funkcemi páteřní sítě 3GPP pro vynucování politik a směrování provozu
- Škálovatelnost a vyrovnávání zatížení pro zvládání vysokých objemů provozu a prevenci zahlcení

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.906** (Rel-19) — IMS P2P Content Distribution Services
- **TS 23.247** (Rel-19) — 5G Multicast/Broadcast Service Architecture
- **TR 23.737** (Rel-17) — Satellite Access in 5G Architecture Study
- **TS 23.844** (Rel-12) — IMS P2P Content Distribution Services Study
- **TS 25.113** (Rel-19) — EMC Requirements for UTRA Base Stations & Repeaters
- **TS 26.501** (Rel-19) — 5G Media Streaming (5GMS) Architecture
- **TS 26.512** (Rel-19) — 5G Media Streaming Protocols & APIs
- **TS 26.802** (Rel-19) — Multicast Enhancements for 5G Media Streaming
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.849** (Rel-12) — MBMS Operation on Demand (MooD)
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 26.904** (Rel-19) — Future video capability requirements for streaming and MBMS
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- … a dalších 9 specifikací

---

📖 **Anglický originál a plná specifikace:** [CDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/cdn/)
