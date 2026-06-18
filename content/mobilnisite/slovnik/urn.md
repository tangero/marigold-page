---
slug: "urn"
url: "/mobilnisite/slovnik/urn/"
type: "slovnik"
title: "URN – Uniform Resource Name"
date: 2025-01-01
abbr: "URN"
fullName: "Uniform Resource Name"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/urn/"
summary: "Uniform Resource Name (URN) je trvalý identifikátor nezávislý na umístění, používaný v systémech 3GPP k jednoznačnému pojmenování prostředků, jako jsou služby, uživatelé nebo síťové prvky. Dodržuje sy"
---

URN je trvalý identifikátor nezávislý na umístění, používaný v systémech 3GPP k jednoznačnému pojmenování prostředků, jako jsou služby nebo síťové prvky, podle syntaxe urn:namespace:identifier.

## Popis

V architektuře 3GPP je Uniform Resource Name (URN) specifickým typem Uniform Resource Identifier ([URI](/mobilnisite/slovnik/uri/)) definovaným v [IETF](/mobilnisite/slovnik/ietf/) [RFC](/mobilnisite/slovnik/rfc/) 2141, používaným jako trvalý a na umístění nezávislý identifikátor prostředků. Na rozdíl od [URL](/mobilnisite/slovnik/url/) (Uniform Resource Locator), které určuje jak identitu, tak síťové umístění/mechanismus přístupu, má URN poskytovat globálně jedinečné a trvalé jméno, které zůstává platné, i když se identifikovaný prostředek přesune nebo stane nedostupným. Syntaxe má strukturu 'urn:<identifikátor jmenného prostoru>:<řetězec specifický pro jmenný prostor>'. 3GPP definuje a registruje vlastní specifické jmenné prostory URN, jako například 'urn:3gpp' a 'urn:oma', aby se předešlo kolizím s identifikátory od jiných organizací.

V praktickém provozu se URN hojně používají v IP Multimedia Subsystem (IMS) a dalších platformách pro poskytování služeb. Například Public Service Identity ([PSI](/mobilnisite/slovnik/psi/)) používaná k identifikaci aplikačního serveru IMS (jako je konferenční služba) může být vyjádřena jako URN (např. urn:service:sos.fire pro tísňovou službu). Když User Equipment (UE) zahájí [SIP](/mobilnisite/slovnik/sip/) relaci, může Request-URI v SIP INVITE zprávě obsahovat URN reprezentující požadovanou službu. Jádro IMS, konkrétně Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)), používá toto URN k provedení spouštění služby. Dotazuje se Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo vyhrazeného Application Server (AS), aby přeložil URN na směrovatelné kontaktní informace (jako je SIP URI nebo tel URI) nebo aby vyvolal příslušnou servisní logiku.

Správa a překlad URN jsou kritické komponenty. Specifikace 3GPP definují postupy pro porovnávání URN (zajištění zpracování bez rozlišení velikosti písmen tam, kde je to vhodné) a mechanismy jejich překladu. Překlad často zahrnuje služby ENUM (Telephone Number Mapping) nebo vyhrazené funkce pro překlad jmen v síti. Například URN reprezentující telefonní číslo v jmenném prostoru 'tel' (urn:tel:+1-555-123-4567) může být prostřednictvím DNS/ENUM přeloženo na SIP URI pro směrování přes IP. Použití URN odděluje servisní logiku od síťové topologie, což umožňuje funkce jako přenositelnost služeb, federace mezi různými síťovými operátory a vytváření abstraktních identit služeb, které nejsou vázány na konkrétní IP adresu serveru nebo doménové jméno.

## K čemu slouží

Zavedení URN v rámci 3GPP, zejména od Release 6 s plným nasazením IMS, bylo motivováno potřebou standardizovaného, flexibilního a do budoucna odolného schématu pojmenování prostředků v plně IP síti. Předchozí sítě s přepojováním okruhů spoléhaly primárně na telefonní čísla E.164 (MSISDN) a IMSI pro identifikaci, které jsou omezené číselným prostorem a nejsou ze své podstaty vhodné pro pojmenování abstraktních služeb, multimediálního obsahu nebo zařízení. Jak se sítě vyvíjely, aby podporovaly multimediální služby, zjišťování služeb a komunikaci mezi stroji, byl vyžadován univerzálnější identifikátor.

URN řeší několik klíčových problémů: poskytují trvalost (jméno služby se nemění, i když se změní hostující server), globální jedinečnost (řízenou prostřednictvím registrovaných jmenných prostorů) a abstrakci od umístění. To umožňuje mobilitu služeb – uživatel může přistupovat ke své službě 'video schránky' pomocí stejného URN bez ohledu na svou geografickou polohu nebo síťového operátora, do jehož sítě přerušuje. Dále usnadňuje interoperabilitu mezi různými implementacemi od výrobců a mezi sítěmi 3GPP a dalšími platformami IP služeb (jako jsou ty definované Open Mobile Alliance - OMA). Použitím standardizovaného mechanismu IETF využilo 3GPP existující, dobře známou technologii a vyhnulo se vytvoření proprietárního a potenciálně nekompatibilního identifikačního systému.

## Klíčové vlastnosti

- Trvalý identifikátor nezávislý na umístění podle syntaxe IETF RFC 2141
- Globálně jedinečné pojmenování prostřednictvím registrovaných jmenných prostorů (např. urn:3gpp, urn:oma)
- Rozsáhlé použití v IMS pro Public Service Identities (PSI) a spouštění služeb
- Umožňuje zjišťování a překlad služeb nezávisle na síťové topologii
- Podporuje abstrakci telefonních čísel prostřednictvím jmenného prostoru URN 'tel'
- Usnadňuje interoperabilitu a federaci mezi různými doménami služeb

## Související pojmy

- [URI – Universal Resource Identifier](/mobilnisite/slovnik/uri/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [ENUM – E.164 telephone NUmber Mapping](/mobilnisite/slovnik/enum/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 22.820** (Rel-15) — Restricted Local Operator Services for Unauthenticated UEs
- **TS 23.167** (Rel-19) — IMS Emergency Sessions
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.334** (Rel-19) — IMS-ALG to IMS-AGW Interface (Iq) Stage 2
- **TS 24.109** (Rel-19) — HTTP Digest AKA & GAA Stage 3
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.282** (Rel-19) — MCData Signalling Control Protocols
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.483** (Rel-19) — Mission Critical Services Management Object
- **TS 24.484** (Rel-19) — MCS Configuration Management
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 26.117** (Rel-19) — 5G Media Streaming Speech/Audio Capabilities
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [URN na 3GPP Explorer](https://3gpp-explorer.com/glossary/urn/)
