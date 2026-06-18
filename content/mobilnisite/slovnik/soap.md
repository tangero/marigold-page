---
slug: "soap"
url: "/mobilnisite/slovnik/soap/"
type: "slovnik"
title: "SOAP – Simple Object Access Protocol"
date: 2025-01-01
abbr: "SOAP"
fullName: "Simple Object Access Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/soap/"
summary: "Protokol pro zasílání zpráv založený na XML, používaný ve specifikacích 3GPP pro komunikaci webových služeb, zejména v kontextu architektury otevřených služeb (OSA) a rozhraní brány Parlay/OSA. Definu"
---

SOAP je protokol pro zasílání zpráv založený na XML, používaný ve specifikacích 3GPP k definování standardizované obálkové struktury pro výměnu strukturovaných informací v komunikaci webových služeb, zejména pro API pro zpřístupnění síťových schopností.

## Popis

Ve standardech 3GPP je protokol SOAP přijat jako základní protokol pro zasílání zpráv pro implementaci rozhraní webových služeb, nejvýznamněji pro architekturu otevřených služeb ([OSA](/mobilnisite/slovnik/osa/)) a bránu Parlay/OSA. SOAP je protokol založený na [XML](/mobilnisite/slovnik/xml/), který definuje rámec pro strukturování zpráv a konvenci pro reprezentaci vzdálených volání procedur ([RPC](/mobilnisite/slovnik/rpc/)) a odpovědí. V kontextu 3GPP se používá k usnadnění komunikace mezi stroji (M2M) aplikačními servery ([AS](/mobilnisite/slovnik/as/)) umístěnými v externí doméně a servery s možnostmi služeb ([SCS](/mobilnisite/slovnik/scs/)) sítě, které zpřístupňují funkce jádra sítě.

Architektura zahrnuje SOAP klienta (typicky externí aplikaci) a SOAP server, kterým je brána Parlay/OSA sítě nebo konkrétní server s možnostmi služeb. Komunikace probíhá přes transportní protokoly jako [HTTP](/mobilnisite/slovnik/http/) nebo [HTTPS](/mobilnisite/slovnik/https/). Zpráva SOAP je XML dokument obsahující povinný prvek Envelope (obálka), volitelný prvek Header (hlavička) pro rozšiřitelnost (např. pro zabezpečení nebo transakční informace) a povinný prvek Body (tělo), který nese vlastní data požadavku nebo odpovědi RPC. Pro OSA obsahuje tělo volání metod a parametry definované aplikačními programovacími rozhraními ([API](/mobilnisite/slovnik/api/)) Parlay/OSA, jako jsou metody pro řízení hovorů, zasílání zpráv nebo dotazování na stav uživatele.

Úlohou SOAP v 3GPP je poskytnout pro volání API formát přenosu dat nezávislý na platformě a programovacím jazyku. Tato abstrakce je klíčová pro princip OSA, jehož cílem je oddělit vývoj služeb od podkladové síťové technologie. Použitím SOAP/XML mohou vývojáři aplikací využívat různé programovací jazyky a nástroje k vytváření služeb, které komunikují s telekomunikační sítí přes standardizované, webu přátelské rozhraní. Specifikace 3GPP podrobně definují přesné XML schémata (XSD) a soubory WSDL, které popisují OSA API, a zajišťují tak interoperabilitu mezi bránami a aplikacemi různých výrobců.

## K čemu slouží

SOAP byl začleněn do specifikací 3GPP pro řešení potřeby standardizovaného, otevřeného a na technologii nezávislého protokolu pro zpřístupnění síťových schopností. Hnacím motorem byla architektura otevřených služeb (OSA) a iniciativa skupiny Parlay vytvořit bezpečná, škálovatelná API, která by umožnila poskytovatelům aplikací třetích stran inovovat bez hluboké znalosti telekomunikačních síťových protokolů. Předtím vyžadoval přístup k síťovým schopnostem proprietární rozhraní specifická pro daného výrobce, což potlačovalo rozvoj živé ekosystému přidaných služeb.

Přijetí SOAP spolu s příbuznými standardy webových služeb jako WSDL a XML poskytlo široce uznávaný a průmyslem podporovaný základ. Vyřešil problém interoperability mezi heterogenními systémy tím, že nabídl textový, samoopisný formát zprávy. To umožnilo 3GPP specifikovat *co* (sémantiku API) odděleně od *jak* (podkladového transportu a kódování). Historický kontext zahrnuje konvergenci světa IT a telekomunikací na počátku 21. století, kde se webové služby staly dominantním paradigmatem pro integraci systémů. SOAP poskytl potřebnou přísnost a rozšiřitelnost (např. prostřednictvím standardů WS-* pro zabezpečení) vyžadovanou pro kritické telekomunikační operace, což z něj učinilo vhodnou volbu pro framework Parlay/OSA v rámci 3GPP.

## Klíčové vlastnosti

- Protokol pro zasílání zpráv založený na XML pro výměnu strukturovaných informací.
- Základní protokol pro implementaci rozhraní webových služeb 3GPP Parlay/OSA.
- Definuje standardní strukturu zprávy: Envelope (obálka), Header (hlavička) a Body (tělo).
- Nezávislý na transportním protokolu, běžně používaný přes HTTP/HTTPS.
- Umožňuje interakce typu vzdálené volání procedur (RPC) a dokumentového stylu.
- Usnadňuje interoperabilitu prostřednictvím standardizovaných definic WSDL a XSD.

## Související pojmy

- [XML – Extensible Markup Language](/mobilnisite/slovnik/xml/)

## Definující specifikace

- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework
- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification
- **TS 23.127** (Rel-6) — Virtual Home Environment Stage 2 Specification
- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 23.198** (Rel-9) — Open Service Access (OSA); Stage 2
- **TS 23.722** (Rel-15) — Common API Framework (CAPIF) for 3GPP Northbound APIs
- **TS 23.845** (Rel-10) — UDC Evolution Study
- **TS 28.518** (Rel-19) — Fault Management for Virtualized Networks Stage 3
- **TS 29.198** (Rel-9) — OSA API Overview Specification
- **TS 29.199** (Rel-9) — Multimedia Messaging Web Services
- **TS 29.240** (Rel-19) — 3GPP Generic User Profile (GUP) Stage 3 Protocol
- **TS 29.817** (Rel-12) — Study on XML-based Rx interface for PCC
- **TS 32.153** (Rel-19) — IRP Technology-Specific Templates Specification
- **TS 32.818** (Rel-8) — SA5 MTOSI XML Harmonization Study
- **TS 32.824** (Rel-9) — SOA and IRP Gap Analysis
- … a dalších 2 specifikací

---

📖 **Anglický originál a plná specifikace:** [SOAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/soap/)
