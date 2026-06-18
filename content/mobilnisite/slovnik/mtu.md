---
slug: "mtu"
url: "/mobilnisite/slovnik/mtu/"
type: "slovnik"
title: "MTU – Maximum Transmission Unit"
date: 2025-01-01
abbr: "MTU"
fullName: "Maximum Transmission Unit"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mtu/"
summary: "MTU je maximální velikost datového paketu, který lze přenést přes síťové rozhraní bez nutnosti fragmentace. Jde o základní parametr v IP síťování, který ovlivňuje výkon, efektivitu a chování protokolů"
---

MTU je maximální velikost datového paketu, který lze přenést přes síťové rozhraní bez nutnosti fragmentace.

## Popis

Maximum Transmission Unit (MTU) je klíčový parametr v datové komunikaci, který definuje maximální velikost v bajtech jednotky protokolových dat ([PDU](/mobilnisite/slovnik/pdu/)), kterou lze přenést v jednom rámci přes síťový spoj bez fragmentace. V kontextu systémů 3GPP se MTU vztahuje k různým vrstvám, včetně IP vrstvy (např. pro pakety uživatelských dat) a spojových vrstev (např. pro Ethernet nebo rádiové nosiče v buňkových sítích). Obvykle se měří na IP vrstvě a zahrnuje IP hlavičku a datovou část, ale nezahrnuje hlavičky nižších vrstev, jako je Ethernet nebo [PPP](/mobilnisite/slovnik/ppp/). Hodnota MTU je dána použité síťovou technologií; například Ethernet běžně používá 1500 bajtů, zatímco rádiové nosiče v 3GPP mohou mít různé MTU v závislosti na konfiguraci a rádiových podmínkách. Pokud paket překročí MTU spoje, musí být fragmentován na menší části, z nichž každá má vlastní IP hlavičku, a ty jsou na cíli znovu sestaveny. Fragmentace však může vést k neefektivitám kvůli režii hlaviček, zvýšenému zpracování a potenciální ztrátě paketů, pokud jsou fragmenty zahazovány. Aby se fragmentaci předešlo, používají se protokoly jako Path MTU Discovery (PMTUD), které zjišťují nejmenší MTU na cestě a podle toho upravují velikosti paketů. V architekturách 3GPP jsou úvahy o MTU kritické pro rozhraní jako [S1-U](/mobilnisite/slovnik/s1-u/) (mezi [eNB](/mobilnisite/slovnik/enb/) a [SGW](/mobilnisite/slovnik/sgw/)), N3 (mezi gNB a [UPF](/mobilnisite/slovnik/upf/) v 5G) a Gi/SGi (mezi [PGW](/mobilnisite/slovnik/pgw/)/UPF a externími sítěmi). Síť může vynucovat limity MTU pomocí parametrů QoS nebo konfigurací nosičů a zařízení se těmto omezením musí přizpůsobit. MTU také ovlivňuje protokoly vyšších vrstev; například TCP používá Maximum Segment Size ([MSS](/mobilnisite/slovnik/mss/)), odvozené od MTU, k optimalizaci velikostí segmentů a vyhýbání se fragmentaci. V 5G, s podporou rozšířeného mobilního širokopásmového připojení (eMBB) a massive IoT, se mohou nastavení MTU lišit podle síťového řezu nebo QoS toku, aby se vyvážila efektivita a latence pro různé služby. Správná správa MTU zajišťuje efektivní využití šířky pásma, snižuje latenci a udržuje kvalitu služeb napříč heterogenními sítěmi.

## K čemu slouží

MTU existuje jako základní síťový koncept pro optimalizaci efektivity a spolehlivosti přenosu dat napříč různými síťovými technologiemi s různými omezeními velikosti rámců. Historicky, jak se sítě vyvíjely z jednoduchých point-to-point spojů ke komplexním internetovým sítím, vznikla potřeba definovat maximální velikost paketu, kterou každý spoj dokáže zpracovat bez degradace výkonu. Bez MTU by mohly být pakety pro některé spoje příliš velké, což by způsobilo fragmentaci zvyšující režii, zatížení procesoru a riziko ztráty paketů, pokud by některý fragment chyběl. V systémech 3GPP je MTU obzvláště důležité kvůli omezeným zdrojům bezdrátových spojů, kde jsou rádiové zdroje vzácné a musí být využívány efektivně. Rané buňkové datové služby (např. GPRS) měly omezené MTU, ale s příchodem 3G, 4G LTE a 5G se velikosti MTU zvýšily, aby podpořily aplikace s vyšší propustností a nižší latencí, jako je streamování videa a hraní her v reálném čase. Koncept řeší omezení univerzální velikosti paketů tím, že umožňuje sítím inzerovat své možnosti MTU, což koncovým bodům umožňuje dynamickou adaptaci. To je klíčové pro bezproblémovou spolupráci mezi buňkovými sítěmi a pevnými sítěmi (např. Ethernet, DSL), což zajišťuje výkon end-to-end. MTU také hraje roli při podpoře nových služeb v 5G, jako je síťové krájení (network slicing), kde různé řezy mohou mít odlišné požadavky na MTU v závislosti na jejich případech užití (např. velké MTU pro eMBB, menší pro IoT). Celkově MTU řeší problémy související s fragmentací, interoperabilitou a optimalizací zdrojů, což z něj činí základní kámen IP komunikace v 3GPP a dalších systémech.

## Klíčové vlastnosti

- Definuje maximální velikost paketu pro přenos bez fragmentace
- Ovlivňuje síťový výkon, latenci a efektivitu
- Podporuje Path MTU Discovery (PMTUD) pro dynamickou adaptaci
- Konfigurovatelné pro každé síťové rozhraní, nosič nebo QoS tok v 3GPP
- Ovlivňuje protokoly vyšších vrstev, jako je TCP, prostřednictvím odvození MSS
- Kritické pro spolupráci mezi heterogenními sítěmi (např. buňkovou a Ethernet)

## Související pojmy

- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)
- [MSS – Mobile Satellite Services](/mobilnisite/slovnik/mss/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.827** (Rel-17) — Study on Audio-Visual Service Production Stage 1
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.539** (Rel-19) — NW-TT Protocol Aspects
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.142** (Rel-19) — 3GPP TS 26.142: Dynamic and Interactive Multimedia Scenes (DIMS)
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.937** (Rel-19) — 3GPP PSS Characterization
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TS 27.007** (Rel-19) — AT Command Set for UE
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.061** (Rel-19) — Packet Domain Interworking for PLMN
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [MTU na 3GPP Explorer](https://3gpp-explorer.com/glossary/mtu/)
