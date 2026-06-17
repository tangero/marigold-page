---
slug: "mp4"
url: "/mobilnisite/slovnik/mp4/"
type: "slovnik"
title: "MP4 – MPEG-4 Part 14 File Format"
date: 2025-01-01
abbr: "MP4"
fullName: "MPEG-4 Part 14 File Format"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mp4/"
summary: "MP4 je standardizovaný kontejnerový formát pro multimédia definovaný organizací 3GPP pro ukládání audia, videa a souvisejících dat. Je klíčový pro mobilní mediální služby, jako je streamování a stahov"
---

MP4 je standardizovaný kontejnerový formát pro multimédia definovaný organizací 3GPP pro ukládání audia, videa a souvisejících dat, který je klíčový pro mobilní mediální služby, jako je streamování a stahování, a zajišťuje interoperabilitu.

## Popis

Formát souboru MP4, technicky MPEG-4 Part 14, je univerzální a strukturovaný kontejnerový formát pro digitální multimédia. V ekosystému 3GPP je specifikován tak, aby zajišťoval, že multimediální obsah – jako je video, audio, titulky a metadata – může být konzistentně zabalen, přenášen a spotřebováván na různých mobilních zařízeních a síťových infrastrukturách. Formát je založen na [ISO](/mobilnisite/slovnik/iso/) Base Media File Format ([ISOBMFF](/mobilnisite/slovnik/isobmff/)), který používá hierarchickou strukturu 'boxů' neboli 'atomů'. Každý box je samostatný datový objekt s definovaným typem a délkou, obsahující buď mediální data, nebo metadata popisující tato data. Mezi klíčové strukturní boxy patří box 'moov' (metadata filmu, obsahující informace o stopách a časování), box 'mdat' (vlastní vzorky mediálních dat) a box 'ftyp' (typ souboru a kompatibilita). Tato architektura založená na boxech umožňuje efektivní parsování, náhodný přístup pro vyhledávání a podporu pokročilých funkcí, jako je streamování, speciální režimy přehrávání a ochrana obsahu.

Při činnosti soubor MP4 zapouzdřuje jednu nebo více mediálních stop. Každá stopa je kódována nezávisle (např. pomocí H.264/[AVC](/mobilnisite/slovnik/avc/) pro video nebo [AAC](/mobilnisite/slovnik/aac/) pro audio) a obsahuje sekvenci vzorků (snímků). Box 'moov' obsahuje komplexní index, tzv. Sample Table, který mapuje každý vzorek na jeho bajtový offset, velikost a časovou značku prezentace uvnitř boxu 'mdat' nebo dokonce v externích souborech. Toto oddělení metadat a dat je zásadní pro progresivní stahování a streamovací protokoly, jako je Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)), kde lze box 'moov' načíst jako první pro inicializaci přehrávání, zatímco mediální data jsou stahována po segmentech. Formát také podporuje fragmentaci, kdy je prezentace rozdělena do série filmových fragmentů, každý se svými vlastními metadaty, což umožňuje živé streamování a efektivní nahrávání.

Role MP4 v sítích 3GPP je ústřední pro multimediální služby definované v Packet-Switched Streaming Service (PSS) a Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). Specifikace 3GPP, jako je TS 26.244, definují aplikaci formátu MP4 pro tyto služby, specifikují omezení a rozšíření pro mobilní použití. Například ukládají konkrétní profilové úrovně kodeků, definují způsob signalizace obsahu pomocí Session Description Protocol (SDP) a zajišťují kompatibilitu s procedurami streamování a stahování definovanými 3GPP. Podpora formátu pro časovaný text (titulky), kapitolové značky a více audio stop jej činí vhodným pro bohaté mediální aplikace. Jeho standardizovaná povaha je základním kamenem interoperability, umožňující obsah zakódovaný jednou přehrát na jakémkoli kompatibilním zařízení, od smartphonů po tablety, napříč sítěmi 2G, 3G, 4G a 5G.

## K čemu slouží

Formát MP4 byl přijat a specifikován organizací 3GPP, aby vyřešil kritický problém interoperability multimédií v mobilním prostředí. Před jeho standardizací existovala řada proprietárních a nekompatibilních mediálních formátů, což vedlo k fragmentaci. To bránilo rozvoji bezproblémového rozsáhlého ekosystému mobilních médií, kde by poskytovatelé obsahu mohli spolehlivě doručovat služby na jakékoli účastnické zařízení. Standard MPEG-4 a konkrétně kontejner MP4 nabídl robustní, mezinárodně uznávané řešení, které mohlo zapouzdřit špičkové video a audio kodeky, jako jsou H.264 a [AAC](/mobilnisite/slovnik/aac/), které byly také standardizovány organizací 3GPP pro svou efektivitu.

Primárním motivem bylo umožnit pokročilé mobilní služby, jako je videotelefonie, streamování a stahování obsahu, které byly klíčovými službami s přidanou hodnotou pro sítě 3G (UMTS) a následující generace. Formát musel být efektivní pro ukládání a přenos přes rádiové spoje s omezenou šířkou pásma, podporovat funkce jako rychlý start a vyhledávání pro dobrou uživatelskou zkušenost a být dostatečně flexibilní, aby podporoval budoucí kodeky a typy médií. Standardizací na MP4 zajistila organizace 3GPP, že síťové prvky (jako streamovací servery), koncová zařízení a nástroje pro přípravu obsahu mají společný, dobře definovaný cíl, což snižuje složitost a náklady pro celý průmysl.

Navíc návrh formátu MP4 dokonale korespondoval s vývojem směrem k IP paketovým službám. Jeho struktura je ze své podstaty vhodná pro přenos přes RTP/UDP/IP pro streamování nebo HTTP/TCP/IP pro progresivní stahování. To z něj učinilo volbu připravenou na budoucnost, jak se sítě 3GPP vyvíjely od okruhově přepínaných přenosů k plně IP jádrovým sítím. Rozšiřitelnost formátu prostřednictvím mechanismu boxů umožnila organizaci 3GPP definovat specifické boxy pro své vlastní potřeby, například pro přenos metadat 3GPP, což zajišťuje, že se formát může vyvíjet spolu se samotnými standardy.

## Klíčové vlastnosti

- Strukturovaný kontejner založený na ISO Base Media File Format (ISOBMFF) využívající 'boxy' pro data a metadata
- Podpora více mediálních stop (video, audio, text) s nezávislým kódováním a časováním
- Umožňuje efektivní streamování a progresivní stahování díky oddělení metadat ('moov') a mediálních dat ('mdat')
- Umožňuje náhodný přístup a vyhledávání prostřednictvím komplexních tabulek vzorků a volitelné fragmentace filmu
- Rozšiřitelný návrh umožňující zahrnutí budoucích kodeků, systémů DRM a typů metadat
- Standardizován organizací 3GPP pro PSS a MBMS, což zajišťuje interoperabilitu napříč všemi kompatibilními mobilními zařízeními

## Definující specifikace

- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.141** (Rel-19) — IMS Messaging & Presence Media Formats
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 26.245** (Rel-19) — 3GPP Timed Text Format Specification

---

📖 **Anglický originál a plná specifikace:** [MP4 na 3GPP Explorer](https://3gpp-explorer.com/glossary/mp4/)
