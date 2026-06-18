---
slug: "gbr"
url: "/mobilnisite/slovnik/gbr/"
type: "slovnik"
title: "GBR – Generic Binaural Renderer"
date: 2026-01-01
abbr: "GBR"
fullName: "Generic Binaural Renderer"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gbr/"
summary: "Standardizovaná funkce pro zpracování zvuku, která vykresluje prostorový zvuk pro binaurální přehrávání, typicky přes sluchátka. Umožňuje ponořivé 3D zvukové zážitky v multimediálních službách, jako j"
---

GBR je standardizovaná funkce pro zpracování zvuku, která vykresluje prostorový zvuk pro binaurální přehrávání přes sluchátka, a umožňuje tak ponořivý 3D zvuk v multimediálních službách 3GPP.

## Popis

Generic Binaural Renderer (GBR) je normativní součást architektury pro doručování médií v 3GPP, speciálně navržená pro zpracování a vykreslování prostorových zvukových objektů nebo scénických zvukových formátů do binaurálního signálu vhodného pro přehrávání přes sluchátka. Funguje jako funkční blok, který může být implementován v síťovém zpracování médií (např. v rámci Media Processing Host) nebo v uživatelském zařízení (UE). Vykreslovač přijímá zvukový vstup, který může být ve formátech jako Scene-Based Audio (např. MPEG-H 3D Audio s objekty nebo vyššími řády ambisonics) nebo Channel-Based Audio, spolu s přidruženými metadaty popisujícími pozice zdrojů a akustické vlastnosti. S využitím databáze Head-Related Transfer Function ([HRTF](/mobilnisite/slovnik/hrtf/)), která modeluje, jak se zvuk z konkrétního bodu v prostoru dostane ke každému uchu, GBR konvoluje zvukové signály, aby vytvořil interaurální časové a úrovňové rozdíly, které vyvolávají vjem zvuku pocházejícího z konkrétních míst v trojrozměrném prostoru kolem posluchače.

Z architektonického hlediska je GBR definován v kontextu mediálního streamování a konverzačních služeb. V Media Streaming může být odkazován ve specifikacích jako 5G Media Streaming ([5GMS](/mobilnisite/slovnik/5gms/)) nebo Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)) pro ponořivé zvukové zážitky. Pro komunikaci v reálném čase může být součástí řetězce zpracování zvuku pro aplikace rozšířené reality ([XR](/mobilnisite/slovnik/xr/)). Chování a rozhraní vykreslovače jsou specifikovány tak, aby zajistily interoperabilitu mezi nástroji pro tvorbu obsahu, síťovými zpracovatelskými funkcemi a koncovými uživatelskými zařízeními. Mezi klíčové parametry, které zpracovává, patří souřadnice zvukového objektu (azimut, elevace, vzdálenost), difuznost a režimy vykreslování, což umožňuje dynamickou adaptaci na základě orientace hlavy posluchače, pokud jsou k dispozici data o sledování polohy hlavy.

Jeho úlohou v síti je oddělit tvorbu obsahu od možností přehrávacího zařízení. Standardizací procesu binaurálního vykreslování mohou tvůrci obsahu vytvořit zvukovou scénu jednou a síť nebo schopné UE ji mohou následně vykreslit vhodně pro konkrétní kontext posluchače (např. typ sluchátek). To je klíčové pro škálovatelné ponořivé služby. Specifikace GBR podrobně popisují vykreslovací algoritmy, požadované charakteristiky HRTF, vstupní/výstupní datové formáty a řídicí protokoly, což zajišťuje, že „obecná“ implementace dokáže zpracovat širokou škálu prostorového zvukového obsahu definovaného jinými standardizačními orgány, jako je [MPEG](/mobilnisite/slovnik/mpeg/), a tím budoucí zvukové služby 3GPP zabezpečit proti zastarávání.

## K čemu slouží

GBR byl vytvořen jako odpověď na rostoucí poptávku po ponořivých zvukových zážitcích v mobilních a bezdrátových službách, zejména s nástupem virtuální reality ([VR](/mobilnisite/slovnik/vr/)), rozšířené reality ([AR](/mobilnisite/slovnik/ar/)) a vysokokvalitních telekonferencí. Před jeho standardizací bylo vykreslování prostorového zvuku často proprietární, specifické pro konkrétní zařízení nebo vyžadovalo významné výpočetní zdroje, které nebyly na všech UE zaručeny. Tato fragmentace bránila rozvoji interoperabilních, sítí poskytovaných ponořivých služeb. 3GPP uznalo, že pro úspěch služeb jako je [XR](/mobilnisite/slovnik/xr/) založené na 5G je nezbytná standardizovaná metoda pro doručování 3D zvuku, aby byla zajištěna konzistentní kvalita uživatelského zážitku na různých zařízeních a sítích.

Historicky se zvukové služby v mobilních sítích zaměřovaly na monofonní nebo stereofonní přehrávání. Omezení těchto přístupů se stala zřejmá s ponořivým videoobsahem, kde odpovídající 3D zvuk je nezbytný pro pocit přítomnosti a realističnost. Proprietární řešení svazovala obsah s konkrétní hardwarovou nebo softwarovou platformou, což omezovalo distribuci obsahu. GBR standardizuje proces vykreslování, což umožňuje výpočetně náročnou úlohu volitelně přesunout do sítě (umožňující vysokokvalitní zážitky na méně výkonných UE) nebo ji provádět lokálně na pokročilých UE. Tato flexibilita řeší problém heterogenity zařízení. Jeho vytvoření bylo motivováno potřebou integrovat sítě 3GPP s mezinárodními multimediálními standardy (jako je MPEG-H) a definovat jasnou architekturu pro zpracování zvuku v rámci specifikací 5G systému pro média a podpůrné služby.

## Klíčové vlastnosti

- Standardizované zpracování formátů prostorového zvuku (objektově a scénicky orientovaných)
- Využívá databáze Head-Related Transfer Function (HRTF) pro binaurální syntézu
- Podporuje dynamické aktualizace zvukové scény pomocí metadat o poloze objektů
- Lze nasadit v síťovém zpracování médií nebo přímo v uživatelském zařízení (UE)
- Umožňuje vykreslování s ohledem na polohu hlavy, pokud jsou k dispozici data o orientaci posluchače
- Zajišťuje interoperabilitu mezi nástroji pro tvorbu obsahu a systémy pro přehrávání

## Související pojmy

- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.202** (Rel-19) — CS Bearer Services Architecture in UMTS
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.401** (Rel-19) — Evolved Packet System (EPS) Stage 2 Description
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TR 23.910** (Rel-5) — UMTS Circuit Switched Bearer Services Overview
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 24.301** (Rel-19) — NAS protocol for Evolved Packet System
- **TS 24.801** (Rel-8) — CT1 SAE NAS Aspects for EPC
- **TS 26.348** (Rel-19) — xMB Interface Specification
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- … a dalších 16 specifikací

---

📖 **Anglický originál a plná specifikace:** [GBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/gbr/)
