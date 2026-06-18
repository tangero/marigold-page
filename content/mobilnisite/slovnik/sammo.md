---
slug: "sammo"
url: "/mobilnisite/slovnik/sammo/"
type: "slovnik"
title: "SAMMO – SAND Message for MBMS Operations"
date: 2025-01-01
abbr: "SAMMO"
fullName: "SAND Message for MBMS Operations"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sammo/"
summary: "Specifický formát zprávy používaný v rámci frameworku Server and Network Assisted DASH (SAND) k podpoře operací Multimedia Broadcast Multicast Service (MBMS). Umožňuje síti poskytovat dynamické inform"
---

SAMMO je specifický formát zprávy SAND používaný k podpoře operací MBMS tím, že umožňuje síti poskytovat dynamické informace o doručování, jako je dostupnost služby a plány vysílání, klientům DASH.

## Popis

SAMMO je standardizovaný typ zprávy definovaný v rámci architektury 3GPP [SAND](/mobilnisite/slovnik/sand/) (Server and Network Assisted [DASH](/mobilnisite/slovnik/dash/)), specifikovaný v TS 26.946. Funguje jako vyhrazený kontejner zpráv pro přenos informací relevantních pro doručování [MBMS](/mobilnisite/slovnik/mbms/) (Multimedia Broadcast Multicast Service) klientům DASH (Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/)). Samotný framework SAND vytváří datový kanál mezi klientem DASH a síťovými entitami (jako je SAND server), umožňující výměnu zpráv, které klientovi pomáhají činit informovanější rozhodnutí o adaptaci. Zprávy SAMMO jsou klíčovou součástí této výměny, je-li zapojeno MBMS.

Technicky je zpráva SAMMO strukturovaný [XML](/mobilnisite/slovnik/xml/) dokument odpovídající schématu definovanému 3GPP. Obsahuje metadata a operační parametry související se službami přenosu MBMS. To může zahrnovat podrobné informace o dostupných relacích MBMS, jejich přidružených oblastech pokrytí služby, plánovaných časech vysílání a mapování mezi reprezentacemi DASH (různé úrovně kvality stejného obsahu) a konkrétními přenosy MBMS. Zprávu generuje síťová entita, typicky SAND server nebo [BM-SC](/mobilnisite/slovnik/bm-sc/) (Broadcast Multicast Service Centre), a doručuje ji klientovi DASH prostřednictvím kanálu pro zprávy SAND, který může používat protokoly jako HTTP.

Po přijetí zprávy SAMMO klient DASH analyzuje informace, aby porozuměl možnostem doručování přes MBMS. Například se může dozvědět, kdy bude přes MBMS vysílána verze obsahu s vysokým datovým tokem, což mu umožní naplánovat její příjem a potenciálně přepnout z unicastového na multicastový proud, čímž šetří rádiové zdroje a zvyšuje efektivitu. Klient tyto informace používá k naplnění svého procesoru Media Presentation Description ([MPD](/mobilnisite/slovnik/mpd/)) a k vedení své adaptační logiky. Architektura integruje aplikační vrstvu frameworku SAND s transportními mechanismy MBMS nižších vrstev, čímž vytváří souvislou optimalizaci napříč vrstvami pro vysílací a multicastové streamovací služby.

## K čemu slouží

SAMMO byl zaveden, aby překlenul mezeru mezi efektivním vysílacím/multicastovým doručováním na síťové vrstvě ([MBMS](/mobilnisite/slovnik/mbms/)) a adaptivním streamovacím protokolem na aplikační vrstvě (DASH). Zatímco MBMS poskytuje efektivní metodu pro doručování oblíbeného obsahu mnoha uživatelům současně, klienti DASH byli původně navrženi pro unicastové doručování přes HTTP a postrádali standardizované mechanismy pro inteligentní vyhledání a využití přenosů MBMS. Bez SAMMO by klient nemusel vědět, že vysílání MBMS pro požadovaný obsah existuje nebo kdy je naplánováno, což by vedlo k neoptimálnímu využití síťových zdrojů a uživatelského zážitku.

Vytvoření SAMMO jako součásti širšího frameworku SAND ve verzi 12 (Release 12) bylo motivováno potřebou síťově asistovaných optimalizací streamování, zejména pro vysílací scénáře jako živé sportovní přenosy nebo zprávy. Řeší problém povědomí klienta. Dodáváním strukturovaných operačních dat MBMS přímo do klientské aplikace umožňuje SAMMO proaktivní a informované chování klienta. To klientům umožňuje oportunisticky využívat vysílací proudy pro segmenty vysoké kvality, zatímco potenciálně používají unicast jako záložní řešení, čímž optimalizují využití kapacity sítě a zajišťují robustní streamovací zážitek vysoké kvality. Představuje klíčový prvek pro konvergované unicastově-vysílací doručování služeb.

## Klíčové vlastnosti

- Standardizovaný formát XML zprávy pro informace o doručování MBMS
- Přenáší parametry relací MBMS, plány a podrobnosti o oblasti služby
- Mapuje reprezentace DASH na konkrétní přenosy MBMS
- Doručován přes kanál pro zprávy SAND (např. přes HTTP)
- Umožňuje klientovi DASH naplánovat příjem vysílaného obsahu
- Usnadňuje plynulé přepínání mezi unicastovou a multicastovou cestou doručování

## Související pojmy

- [SAND – Server and Network Assisted DASH](/mobilnisite/slovnik/sand/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)
- [MPD – Media Presentation Description](/mobilnisite/slovnik/mpd/)

## Definující specifikace

- **TR 26.946** (Rel-19) — MBMS User Services Overview

---

📖 **Anglický originál a plná specifikace:** [SAMMO na 3GPP Explorer](https://3gpp-explorer.com/glossary/sammo/)
