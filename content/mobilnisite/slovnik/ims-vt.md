---
slug: "ims-vt"
url: "/mobilnisite/slovnik/ims-vt/"
type: "slovnik"
title: "IMS-VT – IP Multimedia Subsystem Video Telephony"
date: 2025-01-01
abbr: "IMS-VT"
fullName: "IP Multimedia Subsystem Video Telephony"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ims-vt/"
summary: "IMS-VT je standardizovaná služba umožňující reálný čas, vysoce kvalitní videohovory přes sítě LTE a 5G prostřednictvím IP Multimedia Subsystem. Zajišťuje interoperabilitu mezi zařízeními a sítěmi a na"
---

IMS-VT je standardizovaná služba umožňující reálný čas, vysoce kvalitní videohovory přes sítě LTE a 5G prostřednictvím IP Multimedia Subsystem, která zajišťuje interoperabilitu a nahrazuje starší přepojování okruhů v telekomunikacích.

## Popis

IMS-VT (IP Multimedia Subsystem Video Telephony) je služba definovaná standardy 3GPP, která využívá jádro IMS k navázání a správě obousměrných komunikačních relací v reálném čase mezi uživateli. Funguje jako služba aplikační vrstvy nad architekturou IMS, která poskytuje nezbytné funkce řízení relací, autentizace a zpracování médií. Služba využívá pro signalizaci protokol SIP (Session Initiation Protocol) k navázání, změně a ukončení videosession a protokol RTP (Real-time Transport Protocol) pro vlastní přenos médií. Mezi klíčové komponenty IMS zapojené do procesu patří [P-CSCF](/mobilnisite/slovnik/p-cscf/) (Proxy-Call Session Control Function), S-CSCF (Serving-CSCF) a [MRF](/mobilnisite/slovnik/mrf/) (Media Resource Function), které mohou v případě potřeby zajišťovat mixování médií nebo transkódování.

Z technického pohledu začíná IMS-VT hovor výměnou SIP zpráv INVITE mezi uživatelskými zařízeními, které procházejí jádrem IMS. Tyto zprávy vyjednávají parametry relace pomocí SDP (Session Description Protocol), včetně výběru kodeků (např. H.264 pro video, [AMR-WB](/mobilnisite/slovnik/amr-wb/) nebo [EVS](/mobilnisite/slovnik/evs/) pro audio), přenosových rychlostí a síťových adres. Jádro IMS zajišťuje prostřednictvím [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server), že jsou uživatelé pro službu autentizováni a autorizováni. Jakmile je relace navázána, média proudí přímo mezi koncovými body (UE) přes zřízenou [IP-CAN](/mobilnisite/slovnik/ip-can/) (IP Connectivity Access Network), jako je LTE nebo 5G NR, s využitím QoS mechanismů pro upřednostnění provozu v reálném čase.

Úlohou IMS-VT v síti je poskytnout standardizovaný, interoperabilní rámec pro videotelefonii, který zajišťuje, že zařízení od různých výrobců a služby různých operátorů mohou bezproblémově spolupracovat. Plně se integruje s dalšími službami založenými na IMS, jako je VoLTE (Voice over LTE), což umožňuje bohaté komunikační sady. Služba podporuje základní funkce jako čekání na hovor, přidržení hovoru a doplňkové služby, přičemž zachovává uživatelský zážitek konzistentní s tradiční telekomunikací, avšak obohacený o video. Její architektura je navržena tak, aby byla nezávislá na přístupové síti a fungovala přes jakoukoli IP přístupovou síť, což ji připravuje na budoucí vývoj síťových technologií.

## K čemu slouží

IMS-VT byla vytvořena, aby řešila fragmentaci a omezení dřívějších řešení pro mobilní videohovory, jako byla okruhově přepínaná videotelefonie 3G-324M, která nabízela nízkou kvalitu, omezenou interoperabilitu a neefektivní využití síťových zdrojů. Přechod na plně IP sítě, jako je LTE, si vyžádal nový, standardizovaný přístup ke komunikaci v reálném čase s videem, který by mohl využít možností IMS. Primární motivací bylo poskytnout konzistentní, vysoce kvalitní a interoperabilní službu videotelefonie, kterou by operátoři mohli globálně nasadit, čímž by zlepšili uživatelský zážitek a umožnili nové komunikační paradigma.

Historicky vedly proprietární aplikace pro videohovory a nestandardní implementace ke špatnému uživatelskému zážitku, kdy uživatelé mohli volat pouze lidem ve stejné síti nebo se stejným typem zařízení. IMS-VT, standardizovaná jako součást širší multimediální telekomunikační služby IMS, tento problém řeší definováním jednotné sady protokolů a procedur v rámci standardů 3GPP. Umožňuje operátorům nabízet službu videotelefonie operátorské kvality (carrier-grade) se zaručenou QoS, integrovaným účtováním a podporou regulačních funkcí, jako je zákonné odposlouchávání. Tím, že je součástí IMS, také umožňuje konvergenci s dalšími službami založenými na IP, čímž vytváří jednotnou komunikační platformu.

## Klíčové vlastnosti

- Standardizovaná signalizace založená na SIP pro řízení relací
- Podpora vysoce účinných videokodeků jako H.264 a H.265
- Interoperabilita napříč zařízeními a síťovými operátory
- Integrované QoS mechanismy pro zaručený výkon médií
- Bezproblémová spolupráce se službami VoLTE a dalšími IMS službami
- Podpora doplňkových služeb (přidržení hovoru, přesměrování, čekání)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TR 26.922** (Rel-19) — Video Telephony Robustness Improvements Study

---

📖 **Anglický originál a plná specifikace:** [IMS-VT na 3GPP Explorer](https://3gpp-explorer.com/glossary/ims-vt/)
