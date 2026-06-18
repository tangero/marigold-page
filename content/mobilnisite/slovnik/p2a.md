---
slug: "p2a"
url: "/mobilnisite/slovnik/p2a/"
type: "slovnik"
title: "P2A – Person to Application"
date: 2026-01-01
abbr: "P2A"
fullName: "Person to Application"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/p2a/"
summary: "P2A je komunikační servisní model, ve kterém osoba (uživatel) interaguje s aplikačním serverem, například u chatbotů, hlasových asistentů nebo automatizovaných služeb zákaznické podpory. Je definován"
---

P2A je komunikační servisní model 3GPP, ve kterém osoba interaguje s aplikačním serverem, například u chatbotů nebo hlasových asistentů, a umožňuje standardizované síťové interakce mezi člověkem a strojem.

## Popis

Person to Application (P2A) je servisní paradigma standardizované v 3GPP Release 18 a novějších, které se zaměřuje na přímou komunikaci mezi lidským uživatelem a aplikačním serverem. Tento model je podmnožinou širších komunikačních frameworků Person-to-Person (P2P) a Application-to-Person ([A2P](/mobilnisite/slovnik/a2p/)), ale konkrétně řeší scénáře, kdy je interakce iniciována osobou a cílí na aplikaci, jako je konverzační [AI](/mobilnisite/slovnik/ai/), virtuální asistent nebo automatizovaná servisní platforma. Architektura využívá stávající schopnosti jádra IMS (IP Multimedia Subsystem) nebo 5G core sítě, včetně řízení relací, zpracování médií a servisních enablerů, k zavedení a správě těchto relací. Mezi klíčové síťové funkce zapojené do procesu patří [P-CSCF](/mobilnisite/slovnik/p-cscf/) (Proxy-Call Session Control Function), [S-CSCF](/mobilnisite/slovnik/s-cscf/) (Serving-CSCF) a aplikační servery ([AS](/mobilnisite/slovnik/as/)), které hostují konverzační logiku. Služba může využívat protokoly jako [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) pro signalizaci a [RTP](/mobilnisite/slovnik/rtp/) (Real-time Transport Protocol) pro přenos médií, podporující interakce založené na hlase, videu nebo textu.

Z technické perspektivy jsou P2A relace navazovány podobně jako tradiční hlasové nebo video hovory, ale jsou směrovány na aplikační server namísto jiného koncového bodu uživatele. Síť identifikuje žádost o službu P2A prostřednictvím počátečních filtračních kritérií ([IFC](/mobilnisite/slovnik/ifc/)) nebo mechanismů identifikace služby a směruje relaci na příslušný AS. Aplikační server následně zpracuje vstup uživatele – který může být řeč, text nebo DTMF tóny – pomocí zpracování přirozeného jazyka nebo předdefinované logiky a vygeneruje odpověď. Síťové prostředky pro média, jako je převod řeči na text nebo syntéza textu na řeč, mohou být poskytovány síťovou funkcí Media Resource Function (MRF) nebo integrovány v rámci AS. Mechanismy Quality of Service (QoS) zajišťují nízkou latenci a vysokou spolehlivost pro interakce v reálném čase, což je klíčové pro uživatelský zážitek u služeb jako hlasoví asistenti.

Role P2A v síti přesahuje základní zavedení hovoru; umožňuje operátorům nové zdroje příjmů tím, že usnadňuje pokročilé konverzační služby. Integruje se se síťovými API (např. CAPIF - Common API Framework), aby zpřístupnila aplikačním serverům síťové schopnosti jako uživatelskou autentizaci, polohu nebo status, což umožňuje kontextově-aware interakce. Zabezpečení je prvořadé, s opatřeními jako TLS pro šifrování signalizace a SRTP pro ochranu médií, jak je definováno v příslušných bezpečnostních specifikacích 3GPP. P2A také podporuje regulatorní požadavky, jako je zákonné odposlouchávání a zpracování nouzových služeb, a zajišťuje tak komplianci v nasazených sítích. Celkově P2A představuje konvergenci telekomunikací a IT, umožňující plynulou komunikaci mezi člověkem a strojem přes standardizované mobilní sítě.

## K čemu slouží

P2A bylo zavedeno, aby řešilo rostoucí poptávku po interaktivních, aplikací řízených komunikačních službách, kde uživatelé přímo komunikují s automatizovanými systémy. Před jeho standardizací byly takové interakce často implementovány pomocí proprietárních řešení nebo over-the-top (OTT) aplikací, což vedlo k fragmentaci, nekonzistentní kvalitě a omezené integraci se síťovými schopnostmi. To ztěžovalo mobilním operátorům nabízet standardizované, carrier-grade konverzační služby, jako jsou hlasem aktivovaní asistenti nebo zákaznické servisní boty, se zaručeným výkonem a zabezpečením. Motivace pro P2A v 3GPP Release 18 vychází z evoluce směrem k 5G Advanced, která klade důraz na vylepšené servisní enablery a síťová API pro podporu nových use case přesahujících tradiční telefonii.

Historicky byly komunikační služby primárně P2P (např. hlasové hovory) nebo A2P (např. SMS upozornění), ale vzestup AI a konverzačních rozhraní vytvořil potřebu hybridního modelu, kde osoba iniciuje relaci s aplikací. Stávající mechanismy, jako je unstructured supplementary service data (USSD) nebo systémy interaktivní hlasové odpovědi (IVR), měly omezenou funkcionalitu, podporu médií a škálovatelnost. P2A standardizuje tuto interakci v rámci ekosystému 3GPP, využívající sítě IMS a 5G core k poskytnutí jednotného frameworku. To umožňuje operátorům nasazovat služby s konzistentní QoS, zabezpečením a interoperabilitou mezi různými dodavateli a regiony, což snižuje vývojové náklady a time-to-market.

Dále P2A řeší výzvy související s objevováním služeb, směrováním a zpracováním médií ve scénářích interakce člověk-aplikace. Definováním jasných architektonických rolí a procedur ve specifikacích jako TS 23.228 a TS 24.186 zajišťuje, že aplikace mohou spolehlivě interagovat s uživateli přes mobilní sítě, podporující funkce jako kontinuita relace, integrace účtování a regulatorní kompliance. To umožňuje inovativní služby v oblastech jako zdravotnictví (virtuální zdravotní asistenti), automobilový průmysl (hlasové ovládání v autech) a chytrá města, čímž pohání digitální transformaci komunikačních sítí.

## Klíčové vlastnosti

- Standardizovaná interakce mezi lidskými uživateli a aplikačními servery
- Podpora více typů médií včetně hlasu, videa a textu
- Integrace s IMS a 5G core sítí pro řízení relací
- Garance Quality of Service (QoS) pro konverzační služby v reálném čase
- Bezpečnostní mechanismy včetně šifrování a autentizace
- Zpřístupnění síťových schopností prostřednictvím API pro kontextově-aware aplikace

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [A2P – Application to Person](/mobilnisite/slovnik/a2p/)
- [CAPIF – Common API Framework](/mobilnisite/slovnik/capif/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)

## Definující specifikace

- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 26.567** (Rel-19) — IMS-based Split Rendering
- **TS 28.851** (Rel-19) — Charging for Next Gen Real Time Communication Phase 2
- **TS 33.790** (Rel-19) — Security for Next-Gen Real-Time Communication Phase 2
- **TR 33.890** (Rel-18) — Technical Report on Security Aspects

---

📖 **Anglický originál a plná specifikace:** [P2A na 3GPP Explorer](https://3gpp-explorer.com/glossary/p2a/)
