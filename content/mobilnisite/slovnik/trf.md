---
slug: "trf"
url: "/mobilnisite/slovnik/trf/"
type: "slovnik"
title: "TRF – Transit and Roaming Function"
date: 2025-01-01
abbr: "TRF"
fullName: "Transit and Roaming Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/trf/"
summary: "Funkce jádra sítě definovaná pro sítě IP Multimedia Subsystem (IMS), primárně odpovědná za směrování signalizačních zpráv SIP mezi různými sítěmi operátorů. Zpracovává přenos SIP provozu pro roamující"
---

TRF je funkce jádra sítě IMS, která směruje signalizaci SIP mezi sítěmi operátorů pro roamování a propojení, provádí skrývání topologie, zabezpečení a vynucování politik na hranici sítě.

## Popis

Transit and Roaming Function (TRF) je funkce aplikačního serveru Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) v rámci architektury IMS, standardizovaná 3GPP. Funguje jako SIP proxy nebo back-to-back user agent ([B2BUA](/mobilnisite/slovnik/b2bua/)), která se nachází na hranici mezi IMS sítí operátora a externími sítěmi, jako jsou jiné IMS sítě, sítě s přepojováním okruhů přes [MGCF](/mobilnisite/slovnik/mgcf/) nebo internet. Jejím hlavním úkolem je zpracovávat a směrovat signalizační zprávy SIP pro relace zahrnující roamující uživatele nebo relace, které vznikají v jedné síti a končí v jiné.

Architektonicky je TRF součástí servisní vrstvy IMS a komunikuje s dalšími funkcemi jádra IMS, jako je Interrogating-Call Session Control Function ([I-CSCF](/mobilnisite/slovnik/i-cscf/)), Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) a Breakout Gateway Control Function ([BGCF](/mobilnisite/slovnik/bgcf/)). Její fungování zahrnuje několik klíčových procedur. Pro příchozí roamující relace, když SIP požadavek (jako INVITE) vstoupí do domovské sítě pro roamujícího uživatele, může být směrován přes TRF. TRF provádí bezpečnostní funkce, jako je ověření zdroje, kontrola proti černým listinám a případně skrývání interní topologie sítě odstraněním nebo úpravou citlivých hlaviček SIP. Také vynucuje směrovací politiky operátora a zajišťuje, že relace jsou směrovány ke správnému S-CSCF nebo aplikačnímu serveru.

Pro odchozí relace (např. když domácí uživatel volá uživatele v jiné síti) TRF funguje jako výstupní bod. Aplikuje směrování založené na politikách, vybírá vhodné propojení mezi operátory (např. přes [IPX](/mobilnisite/slovnik/ipx/)) a může provádět nezbytné adaptace protokolu. TRF je také klíčová ve scénářích IMS roamingu, kde může komunikovat s infrastrukturou 3GPP [AAA](/mobilnisite/slovnik/aaa/) založenou na Diameteru pro získání profilů a autorizace roamujících uživatelů. Mezi klíčové komponenty její logiky patří mechanismy pro manipulaci se zprávami SIP, funkce pro rozhodování o politikách a bezpečnostní brány. Její role je zásadní pro udržení bezpečnosti, spolehlivosti a obchodních dohod spojených s komunikací mezi operátory.

## K čemu slouží

TRF byla zavedena, aby řešila specifické výzvy vyplývající z plně IP a SIP-based povahy IMS, zejména pro komunikaci mezi sítěmi a roaming. Před IMS bylo roamování a propojení v sítích s přepojováním okruhů řešeno vyhrazenými signalizačními systémy (SS7) a systémy hlasových trunků s jasně definovanými hraničními body (jako GMSC). IMS se svou otevřenou IP signalizací postrádala standardizovanou, bezpečnou a na politiky citlivou hraniční funkci pro SIP provoz, což vedlo k rizikům bezpečnostních zranitelností, nekontrolovaného směrování a neschopnosti vynucovat obchodní dohody.

Její vytvoření ve verzi Release 11 bylo motivováno potřebou konsolidované funkce pro zvládnutí složitých signalizačních požadavků na hranicích IMS sítě. Řeší problémy jako skrývání topologie (zabraňuje externím entitám poznat interní strukturu sítě), filtrování škodlivého SIP provozu, vynucování politik propojení (např. preferovaní partneři) a poskytuje jednotný bod pro zákonné odposlechy pro provoz mezi operátory. Dále, jak se IMS stala základem pro VoLTE a pokročilé komunikační služby, byl standardizovaný přístup k roamingu a tranzitu klíčový pro globální interoperabilitu.

TRF řeší omezení dřívějších, více ad-hoc přístupů používajících generická SIP proxy nebo SBC (Session Border Controllers) bez standardizovaného chování. Poskytuje 3GPP definovanou šablonu, která zajišťuje konzistentní chování napříč dodavateli a operátory, což je klíčové pro škálování služeb založených na IMS, jako je hlasový a video roaming, v globálním měřítku.

## Klíčové vlastnosti

- SIP signalizační proxy/B2BUA pro směrování relací mezi operátory a pro roaming
- Funkce Topology Hiding Gateway (THIG) pro skrytí interní topologie sítě
- Bezpečnostní kontrola a filtrování příchozích/odchozích SIP zpráv
- Vynucování politik pro směrování mezi operátory a autorizaci služeb
- Interakce s AAA pro autentizaci roamujících uživatelů a získání profilů
- Podpora propojení IMS přes sítě IP Exchange (IPX)

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [IPX – Internetwork Packet Exchange](/mobilnisite/slovnik/ipx/)

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TS 29.079** (Rel-19) — Optimal Media Routeing (OMR) Procedures
- **TS 29.162** (Rel-19) — IMS-IP Network Interworking
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions

---

📖 **Anglický originál a plná specifikace:** [TRF na 3GPP Explorer](https://3gpp-explorer.com/glossary/trf/)
