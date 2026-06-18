---
slug: "sei"
url: "/mobilnisite/slovnik/sei/"
type: "slovnik"
title: "SEI – Supplemental Enhancement Information"
date: 2025-01-01
abbr: "SEI"
fullName: "Supplemental Enhancement Information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/sei/"
summary: "Formát metadatových zpráv používaný ve standardech pro kódování videa, jako jsou H.264/AVC a H.265/HEVC, k přenosu doplňkových informací, které vylepšují dekódování, zobrazení nebo interpretaci videos"
---

SEI je formát metadatových zpráv používaný ve standardech pro kódování videa k přenosu doplňkových, nepodstatných informací, které vylepšují dekódování, zobrazení nebo interpretaci videosignálu.

## Popis

Supplemental Enhancement Information (SEI) je standardizovaný mechanismus pro vkládání doplňkových metadat do videosignálu, jak je definováno standardy pro kódování videa přijatými 3GPP pro multimediální služby. Je součástí syntaxe kodeků jako H.264/[AVC](/mobilnisite/slovnik/avc/) (Advanced Video Coding) a H.265/[HEVC](/mobilnisite/slovnik/hevc/) (High Efficiency Video Coding). Zprávy SEI jsou obsaženy v jednotkách Network Abstraction Layer ([NAL](/mobilnisite/slovnik/nal/)) videosignálu. Nesou informace, které nejsou vyžadovány pro normativní dekódovací proces k vytvoření správných hodnot vzorků, ale jsou prospěšné pro zlepšení uživatelského zážitku, řízení procesů zobrazení, umožnění pokročilých funkcí nebo poskytnutí ladících informací.

Zprávy SEI fungují tak, že jsou vloženy v kodéru a přenášeny spolu s kódovanými videořezky. Dekodér tyto zprávy analyzuje a může použít informace, které obsahují. Syntaxe a sémantika zpráv SEI jsou přesně definovány. Každá zpráva SEI má specifický typ datového bloku a jeho strukturu. Mezi běžné příklady patří "pic_timing", který poskytuje časové razítko pro synchronizaci dekódování a zobrazení, "user_data_registered_itu_t_t35" pro přenos dat specifických pro výrobce nebo aplikaci a "recovery_point", který signalizuje, jak se zotavit z chyb nebo bodů vyhledávání. Zprávy jsou jednosměrné (od kodéru k dekodéru) a nevyžadují potvrzení.

Z pohledu sítě 3GPP jsou zprávy SEI považovány za součást uživatelské roviny videa. Během navazování multimediální relace prostřednictvím protokolů jako [SIP](/mobilnisite/slovnik/sip/) a [SDP](/mobilnisite/slovnik/sdp/) lze vyjednávat podporu určitých zpráv SEI. Jádrová síť a rádiová přístupová síť transparentně přenášejí videosignál obsahující SEI. Nicméně prvky sítě s povědomím o médiích, jako je Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) nebo aplikační servery, mohou zprávy SEI analyzovat a dokonce generovat nebo upravovat, aby přizpůsobily obsah pro různá zařízení nebo síťové podmínky. Například MRF může vkládat zprávy SEI pro uspořádání snímků pro stereoskopické 3D video služby.

Role SEI je klíčová pro umožnění vylepšených video služeb přes mobilní sítě. Podporuje funkce jako dynamická adaptace, speciální režimy přehrávání (rychlé přetáčení vpřed, vzad), transformace barevného objemu ([HDR](/mobilnisite/slovnik/hdr/)) a popis obsahu. Standardizací tohoto přenosu metadat SEI zajišťuje interoperabilitu mezi kodéry, dekodéry a middlewarem různých výrobců, což umožňuje bohatý ekosystém video aplikací v rámci multimediálního rámce 3GPP.

## K čemu slouží

SEI existuje, aby vyřešil problém přenosu nepodstatných, ale velmi cenných řídicích a popisných informací spolu s komprimovanou podstatou videa, aniž by se měnil základní dekódovací standard. Před jeho přijetím musela být taková doplňková data odesílána mimopásmově (např. v samostatném rozšíření hlavičky [RTP](/mobilnisite/slovnik/rtp/) nebo zcela jiným kanálem), což komplikovalo synchronizaci a zvyšovalo složitost systému. SEI poskytuje standardizovaný mechanismus přenosu v pásmu.

Primární motivací bylo umožnit pokročilé video funkce a zlepšit robustnost a použitelnost. Například přesné informace o načasování zobrazení (SEI pic_timing) jsou klíčové pro plynulé přehrávání a synchronizaci obrazu se zvukem při multimediálním streamování. Pan-scan obdélníky umožňují upravit zobrazovanou oblast na displejích s různými poměry stran. Zprávy SEI pro období vyrovnávací paměti a body obnovy jsou zásadní pro adaptivní streamovací protokoly jako DASH a HLS, které jsou široce používány ve službách MBMS a streamování 3GPP. Pomáhají dekodérům efektivně spravovat vyrovnávací paměti a zotavovat se ze ztráty paketů nebo operací vyhledávání.

Historicky bylo SEI začleněno ze standardů pro video ITU-T a ISO/IEC MPEG do multimediálních specifikací 3GPP, aby bylo zajištěno, že mobilní zařízení mohou spolupracovat se širokým ekosystémem video technologií. Jeho vytvoření řeší omezení videosignálu, který obsahuje pouze obrazová data, přidáním vrstvy 'inteligence', která řídí, jak by s videem mělo být nakládáno po dekódování. To umožňuje poskytovatelům služeb nabízet konzistentní, vysoce kvalitní video zážitek napříč různými sítěmi a zařízeními, což je základním cílem služby Packet-Switched Streaming Service (PSS) a Multimedia Broadcast/Multicast Service (MBMS) 3GPP.

## Klíčové vlastnosti

- Přenos v pásmu v rámci jednotek NAL videosignálu
- Definované typy datových bloků pro načasování, řízení zobrazení a uživatelská data
- Není vyžadováno pro normativní dekódování, ale vylepšuje použitelnost
- Podporuje data specifická pro výrobce prostřednictvím registrovaných zpráv uživatelských dat
- Umožňuje funkce jako metadata HDR, uspořádání snímků pro 3D a řízení vyrovnávací paměti
- Používáno adaptivními streamovacími protokoly pro náhodný přístup a speciální režimy přehrávání

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.855** (Rel-19) — Study on Film Grain Synthesis
- **TR 26.862** (Rel-17) — Immersive Teleconferencing & Telepresence for Remote Terminals
- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.919** (Rel-19) — Study on 5G Conversational Media Handling
- **TR 26.946** (Rel-19) — MBMS User Services Overview
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.949** (Rel-19) — TV Service Profiles for 3GPP Networks
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.962** (Rel-19) — ITT4RT Operation and Usage Guidelines

---

📖 **Anglický originál a plná specifikace:** [SEI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sei/)
