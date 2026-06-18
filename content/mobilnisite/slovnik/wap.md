---
slug: "wap"
url: "/mobilnisite/slovnik/wap/"
type: "slovnik"
title: "WAP – Wireless Application Protocol"
date: 2025-01-01
abbr: "WAP"
fullName: "Wireless Application Protocol"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wap/"
summary: "Otevřený mezinárodní standard pro přístup k internetovým službám a informacím z mobilních zařízení přes bezdrátové sítě. Definuje sadu protokolů umožňujících doručování a prezentaci webového obsahu na"
---

WAP (Wireless Application Protocol) je otevřený mezinárodní standard, který definuje sadu protokolů pro doručování a prezentaci webového obsahu na mobilních zařízeních prostřednictvím bezdrátových sítí, což umožnilo rané služby mobilního internetu.

## Popis

Wireless Application Protocol (WAP) je komplexní, otevřené standardní aplikační prostředí a sada komunikačních protokolů navržených k přenosu internetového obsahu a pokročilých telefonních služeb na digitální mobilní telefony a další bezdrátové terminály. Jeho architektura je strukturována ve vrstvách, odrážejících model [OSI](/mobilnisite/slovnik/osi/), aby zajistila interoperabilitu mezi různými typy sítí a výrobci zařízení. Základní zásobník protokolů zahrnuje Wireless Application Environment ([WAE](/mobilnisite/slovnik/wae/)) pro vývoj aplikací (pomocí [WML](/mobilnisite/slovnik/wml/) - Wireless Markup Language), Wireless Session Protocol ([WSP](/mobilnisite/slovnik/wsp/)) pro spojované a nespojované služby, Wireless Transaction Protocol ([WTP](/mobilnisite/slovnik/wtp/)) poskytující spolehlivé transakce typu požadavek/odpověď, Wireless Transport Layer Security ([WTLS](/mobilnisite/slovnik/wtls/)) pro zabezpečení a Wireless Datagram Protocol ([WDP](/mobilnisite/slovnik/wdp/)), který nabízí konzistentní datový formát vyšším vrstvám nad různými přenosovými službami, jako jsou [SMS](/mobilnisite/slovnik/sms/), CSD nebo GPRS.

Klíčovou architektonickou součástí je WAP Gateway, který funguje jako prostředník mezi bezdrátovou doménou a internetem. Gateway plní kritické funkce, jako je překlad protokolů (konverze požadavků ze zásobníku WAP protokolů, jako je WTP/WSP, na standardní HTTP pro webové servery) a kódování/dekódování obsahu (překlad webového obsahu (HTML) do kompaktního, binárně kódovaného WML pro efektivní přenos přes bezdrátové spoje s omezenou šířkou pásma). Tento model brány umožňuje poskytovatelům obsahu hostovat standardní webové servery a zároveň umožňuje mobilním zařízením přístup k optimalizovanému obsahu.

Úlohou WAP bylo vytvořit uživatelský zážitek založený na mikroprohlížeči na mobilních zařízeních, což uživatelům umožnilo procházet stránky informací (balíčky karet ve WML) a interagovat se službami. Umožnil rané mobilní služby, jako jsou upozornění na zprávy, bankovnictví, e-mail a jednoduché prohlížení webu. Ačkoli byl z velké části nahrazen plnohodnotným mobilním broadbandem založeným na IP a nativními aplikacemi pro chytré telefony, WAP stanovil základní koncepty pro poskytování služeb mobilních dat, adaptaci obsahu a oddělení aplikační logiky od podkladové rádiové sítě – principy, které ovlivnily pozdější architektury mobilního webu a služeb.

## K čemu slouží

WAP byl vytvořen, aby řešil základní výzvu přenosu internetových informací a interaktivních služeb do prostředí s omezenými zdroji u raných mobilních telefonů. Před WAP byl přístup k mobilním datům proprietární, roztříštěný a omezený, bez univerzálního standardu pro poskytování služeb napříč různými výrobci zařízení a síťovými operátory. Motivací bylo vytvořit otevřený globální protokol, který by umožnil poskytovatelům služeb a vývojářům vytvářet aplikace přístupné z jakéhokoli mobilního zařízení, a tím podpořit nový ekosystém služeb mobilních dat.

Konkrétně řešil problémy spojené s omezeními tehdejších bezdrátových sítí, které měly ve srovnání s pevnými sítěmi vysokou latenci, nízkou šířku pásma a méně spolehlivá spojení. Standardní webové protokoly jako HTTP a TCP byly v tomto prostředí neefektivní. WAP zavedl optimalizované, odlehčené protokoly (WSP, WTP), které snížily počet transakcí vyžadujících několik kol a zvládaly přerušovanou konektivitu. Mobilní zařízení navíc měla omezený výpočetní výkon, paměť, velikost displeje a metody vstupu. WAP to řešil prostřednictvím WAE, které definovalo WML jako odlehčený značkovací jazyk vhodný pro malé obrazovky a jazyk WMLScript pro přidání klientské logiky, přičemž oba byly efektivnější než jejich desktopové protějšky.

Historicky se WAP objevil koncem 90. let 20. století, když sítě GSM zaváděly paketově přepínaný GPRS, což vytvořilo potřebu standardizovaného aplikačního rámce pro využití této nové datové schopnosti. Jeho cílem bylo překlenout propast mezi výkonným, obsahem bohatým světem internetu a rodícím se mobilním světem, a připravit tak půdu pro éru mobilního internetu%e, i když jeho uživatelský zážitek byl často kritizován. Jeho vývoj byl výsledkem spolupráce WAP Fóra, které se později sloučilo do Open Mobile Alliance (OMA).

## Klíčové vlastnosti

- Otevřený, bezlicenční standard pro interoperabilitu napříč zařízeními a sítěmi
- Zásobník protokolů optimalizovaný pro bezdrátové sítě s vysokou latencí a nízkou šířkou pásma
- Wireless Application Environment (WAE) s WML a WMLScript pro obsah optimalizovaný pro mobilní zařízení
- Architektura brány (gateway) pro překlad protokolů a adaptaci obsahu
- Wireless Transport Layer Security (WTLS) pro zabezpečené transakce
- Podpora více přenosových služeb (SMS, CSD, GPRS)

## Související pojmy

- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)
- [OMA – Open Mobile Alliance](/mobilnisite/slovnik/oma/)

## Definující specifikace

- **TR 21.902** (Rel-10) — 3GPP Evolution Roadmap
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.945** (Rel-4) — Fax Services Guidance for GSM/UMTS
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TR 23.976** (Rel-19) — Push Service Requirements Analysis
- **TS 26.233** (Rel-15) — 3GPP Packet-Switched Streaming Service (PSS)
- **TS 29.198** (Rel-9) — OSA API Overview Specification
- **TS 31.113** (Rel-8) — USAT Interpreter Byte Code Specification
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TS 33.320** (Rel-19) — H(e)NB Subsystem Security Architecture

---

📖 **Anglický originál a plná specifikace:** [WAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/wap/)
