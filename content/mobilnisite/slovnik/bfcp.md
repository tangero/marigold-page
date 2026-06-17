---
slug: "bfcp"
url: "/mobilnisite/slovnik/bfcp/"
type: "slovnik"
title: "BFCP – Binary Floor Control Protocol"
date: 2025-01-01
abbr: "BFCP"
fullName: "Binary Floor Control Protocol"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bfcp/"
summary: "BFCP je binární protokol pro správu sdílených zdrojů, jako je 'právo slova' (oprávnění mluvit nebo vysílat), v konferenčních a komunikačních službách v reálném čase. Je klíčový pro koordinaci přenosu"
---

BFCP (Binary Floor Control Protocol) je binární protokol pro správu sdílených zdrojů, jako je oprávnění vysílat při konferencích, klíčový pro koordinaci médií v multimediálních relacích založených na IMS.

## Popis

Binary Floor Control Protocol (BFCP) je protokol typu klient-server standardizovaný [IETF](/mobilnisite/slovnik/ietf/) a přijatý 3GPP pro použití v IP Multimedia Subsystem (IMS). Funguje nad spolehlivými transportními protokoly, typicky TCP nebo TLS nad TCP, a slouží ke správě soutěžení o sdílené zdroje, především o 'právo slova' na konferenci. Právo slova představuje dočasné, exkluzivní oprávnění využívat zdroj, například vysílat audio nebo video v multimediální relaci. BFCP umožňuje centralizovanému Floor Control Serveru ([FCS](/mobilnisite/slovnik/fcs/)) přijímat žádosti o právo slova od klientů (např. uživatelských zařízení nebo účastníků konference), rozhodovat o nich na základě politiky a právo slova udělit nebo odmítnout, čímž předchází kolizím a zajišťuje řádný přenos médií.

Z architektonického hlediska zahrnuje BFCP několik klíčových entit: účastníka práva slova (klient), předsedu práva slova (entita, která může schvalovat žádosti, často používaná v moderovaných konferencích) a Floor Control Server. Protokol definuje sadu binárních zpráv pro operace řízení práva slova, včetně FloorRequest, FloorRelease, FloorGrant a FloorDeny. Tyto zprávy se vyměňují v rámci BFCP spojení, které je navázáno pomocí identifikátoru specifického pro konferenci a uživatelských identifikátorů. FCS udržuje stav každého práva slova a souvisejících žádostí a rozhoduje na základě politiky první příchozí je první obsloužen, rozhodnutí předsedy nebo jiných nastavených politik.

V kontextu 3GPP IMS je BFCP integrován s protokolem Session Initiation Protocol (SIP) a Session Description Protocol (SDP). Konferenční fokus, typicky SIP Application Server ([AS](/mobilnisite/slovnik/as/)), jako je Multimedia Resource Function Controller ([MRFC](/mobilnisite/slovnik/mrfc/)), často funguje jako nebo řídí FCS. Během navazování relace se SDP používá k vyjednání a indikaci podpory BFCP, včetně portu a transportu pro BFCP spojení. Jakmile je multimediální relace aktivní, BFCP zprávy se vyměňují mimo pásmo od mediálních proudů, aby řídily, který mediální obsah účastníka bude přeposílán nebo má prioritu. To je nezbytné pro služby jako audio/videokonference, push-to-talk a interaktivní hry.

Role BFCP je klíčová pro správu kvality uživatelského prožitku (QoE) v kolaborativních relacích. Poskytnutím deterministického, bezkonfliktního přístupu ke sdíleným zdrojům zabraňuje situacím, kdy více účastníků vysílá současně a způsobuje tak zkreslený audio nebo video signál. Protokol podporuje funkce jako fronta žádostí o právo slova, dohled předsedy a oznámení o stavu, což umožňuje komplexní konferenční scénáře. Jeho binární povaha zajišťuje efektivní přenos ve srovnání s textovými protokoly, což je důležité pro řízení v reálném čase, kde je požadována nízká latence.

## K čemu slouží

BFCP byl vytvořen, aby řešil potřebu standardizovaného, efektivního mechanismu pro správu sdílených zdrojů v multimediálních konferencích v reálném čase, zejména v rámci IP architektur 3GPP IMS a konferenčních rámců [IETF](/mobilnisite/slovnik/ietf/). Před BFCP konferenční systémy často používaly proprietární signalizaci nebo základní moderátorské ovládání, kterému chyběla interoperabilita a které nemohlo zaručit spravedlivý nebo bezkonfliktní přístup ve velkých, více-dodavatelských prostředích. Protokol řeší základní problém 'řízení práva slova' – určení, kdo má právo vysílat mediální obsah v daném čase – což je nezbytné pro řádnou komunikaci ve scénářích, jako jsou telekonference, webináře a push-to-talk over cellular (PoC).

Motivace vychází z omezení použití mechanismů na úrovni médií (jako je detekce mluvčího) nebo pouhé jednoduché SIP signalizace, které jsou nedostatečné pro komplexní rozhodování a vynucování politik. BFCP poskytuje explicitní, mimopásmový řídicí kanál věnovaný správě zdrojů, který odděluje řídicí logiku od transportu médií. To umožňuje sofistikované politiky, jako je fronta žádostí, moderování předsedou a zpracování priorit, které jsou nezbytné pro profesionální a klíčové komunikační služby. Jeho přijetí ve standardech 3GPP umožnilo poskytování standardizovaných, operátorsky kvalitních konferenčních a skupinových komunikačních služeb přes mobilní sítě.

Historicky byl vývoj BFCP hnán pracovní skupinou IETF Centralized Conferencing (XCON) a byl začleněn do specifikací 3GPP, aby splnil požadavky pro služby Multimedia Telephony (MMTel) a konferencí. Poskytl klíčový prvek pro skupinovou komunikaci založenou na IMS, což umožnilo síťovým operátorům nabízet funkčně bohaté, řiditelné konference jako součást jejich portfolia služeb. Tím, že standardizovaným způsobem vyřešil problém rozhodování o právu slova, BFCP usnadnil interoperabilitu mezi klientskými a serverovými zařízeními různých dodavatelů, což byl významný krok vpřed pro ekosystém aplikací pro spolupráci v reálném čase.

## Klíčové vlastnosti

- Binární formát zpráv pro efektivní parsování a přenos
- Architektura klient-server s centrálním Floor Control Serverem (FCS) pro rozhodování
- Integrace s SIP a SDP pro navázání relace a vyjednání schopností
- Podpora primitiv pro žádost o právo slova, udělení, uvolnění, zamítnutí a oznámení stavu
- Mechanismy pro řízení předsedou práva slova pro moderované konference
- Spolehlivý transport přes TCP nebo TLS pro zaručené doručení řídicích zpráv

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRFC – Multimedia Resource Function Controller](/mobilnisite/slovnik/mrfc/)

## Definující specifikace

- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 24.103** (Rel-19) — Telepresence Protocol for IMS
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.803** (Rel-12) — Telepresence using IMS - Study
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TR 26.923** (Rel-19) — Study on IMS-based Telepresence Media Handling
- **TR 26.980** (Rel-19) — Multi-stream Multiparty Conferencing Media Handling
- **TR 26.982** (Rel-19) — Multiparty Real-Time Text Protocol Details
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.333** (Rel-19) — MRFC-MRFP Mp Interface Protocol
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [BFCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/bfcp/)
