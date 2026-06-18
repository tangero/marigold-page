---
slug: "bmff"
url: "/mobilnisite/slovnik/bmff/"
type: "slovnik"
title: "BMFF – Based Media File Format"
date: 2025-01-01
abbr: "BMFF"
fullName: "Based Media File Format"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/bmff/"
summary: "BMFF je standard formátu souboru pro ukládání a doručování multimediálního obsahu v systémech 3GPP. Poskytuje strukturovaný kontejner pro audio, video a časovaný text, což umožňuje efektivní streamová"
---

BMFF je standard formátu souboru 3GPP pro ukládání a doručování multimediálního obsahu, který poskytuje strukturovaný kontejner pro audio, video a časovaný text, aby umožnil efektivní streamování přes mobilní sítě.

## Popis

Based Media File Format (BMFF) je kontejnerový formát standardizovaný organizací 3GPP pro zapouzdření multimediálního obsahu, včetně audio, video a stop s časovaným textem. Vychází ze standardu [ISO](/mobilnisite/slovnik/iso/) Base Media File Format ([ISOBMFF](/mobilnisite/slovnik/isobmff/)) a je navržen pro podporu efektivního doručování přes paketové sítě, zejména v mobilním prostředí. Formát organizuje mediální data do hierarchické struktury boxů (také nazývaných atomy), z nichž každý plní specifický účel, jako je ukládání metadat, mediálních vzorků nebo časových informací. Tato architektura založená na boxech umožňuje rozšiřitelnost a efektivní parsování, protože přehrávače mohou rychle najít potřebné informace bez zpracování celého souboru.

V jádru BMFF používá box 'moov' pro uložení všech metadat potřebných k interpretaci mediálních vzorků, které jsou uloženy v jednom nebo více boxech 'mdat'. Box 'moov' zahrnuje definice stop, tabulky vzorků (stbl) a časové informace, což umožňuje náhodný přístup a synchronizaci mezi různými mediálními stopami. Pro streamovací aplikace BMFF podporuje fragmentaci, kdy je soubor rozdělen na menší segmenty, z nichž každý obsahuje box 'moof' (movie fragment) a box 'mdat'. Tato fragmentace umožňuje adaptivní streamování s proměnnou přenosovou rychlostí, protože klient může na základě síťových podmínek žádat segmenty různé kvality.

BMFF také zahrnuje podporu pokročilých funkcí, jako jsou hint tracky, které poskytují návod pro paketizaci mediálních dat pro streamovací protokoly jako [RTP](/mobilnisite/slovnik/rtp/). Ochrané schémata, včetně šifrování a správy digitálních práv ([DRM](/mobilnisite/slovnik/drm/)), jsou podporovány prostřednictvím vyhrazených boxů, které popisují metodu šifrování a správu klíčů. Návrh formátu zajišťuje kompatibilitu s různými kodeky, včetně těch specifikovaných 3GPP (např. [AMR](/mobilnisite/slovnik/amr/), [EVS](/mobilnisite/slovnik/evs/), H.264, H.265) a dalších, což jej činí univerzálním pro různé multimediální aplikace.

V kontextu služeb 3GPP se BMFF používá ve službě Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), ve streamovacích službách a při doručování souborů přes [HTTP](/mobilnisite/slovnik/http/). Umožňuje efektivní využití síťových prostředků podporou funkcí jako progresivní stahování, kdy může přehrávání začít před stažením celého souboru. Struktura formátu také usnadňuje odolnost vůči chybám a obnovu, protože poškozené boxy lze často přeskočit bez ovlivnění celého přehrávání. Celkově BMFF slouží jako základní technologie pro doručování bohatých mediálních zážitků v sítích 3GPP, vyvažující flexibilitu, efektivitu a robustnost.

## K čemu slouží

BMFF byl vytvořen, aby řešil potřebu standardizovaného, efektivního kontejnerového formátu pro multimediální obsah v systémech 3GPP. Před jeho přijetím byly používány různé proprietární formáty, což vedlo k problémům s interoperabilitou a zvýšené složitosti pro poskytovatele obsahu a výrobce zařízení. Tím, že 3GPP založilo BMFF na široce přijímaném ISOBMFF, zajistilo kompatibilitu s existujícími nástroji a ekosystémy, zároveň jej však přizpůsobilo pro doručování v mobilních sítích.

Formát řeší několik klíčových problémů v mobilním doručování médií: umožňuje efektivní streamování podporou fragmentace a adaptivního přepínání přenosové rychlosti, snižuje latenci prostřednictvím progresivního stahování a zajišťuje synchronizaci mezi audio, video a textovými stopami. Dále podpora šifrování a DRM v BMFF řeší požadavky na ochranu obsahu, které jsou klíčové pro komerční mediální služby. Jeho návrh je také optimalizován pro síťové podmínky typické pro mobilní prostředí, jako je proměnná šířka pásma a přerušované připojení.

Historicky vývoj mobilních mediálních služeb vyžadoval formát, který by dokázal držet krok s rostoucí kvalitou videa a interaktivními funkcemi. Zavedení BMFF ve vydání Release 15 bylo v souladu s nasazením služeb 5G, které slibovaly vylepšené mobilní širokopásmové připojení a nové mediální aplikace. Poskytnutím robustního a flexibilního kontejneru BMFF umožňuje poskytovatelům služeb doručovat kvalitní video, imerzivní audio a interaktivní obsah při zachování efektivního využití síťových prostředků a zajištění konzistentního uživatelského zážitku napříč zařízeními.

## Klíčové vlastnosti

- Hierarchická struktura založená na boxech pro rozšiřitelnost a efektivní parsování
- Podpora fragmentace a movie fragment boxů (moof) umožňující adaptivní streamování s proměnnou přenosovou rychlostí
- Kompatibilita s kodeky specifikovanými 3GPP a stopami s časovaným textem
- Integrovaná podpora šifrování a správy digitálních práv (DRM)
- Hint tracky pro usměrnění paketizace ve streamovacích protokolech jako RTP
- Schopnost progresivního stahování umožňující přehrávání před úplným stažením souboru

## Související pojmy

- [ISOBMFF – International Organization for Standards, Base Media File Format](/mobilnisite/slovnik/isobmff/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.998** (Rel-19) — 5G AR/MR Glasses Integration Study

---

📖 **Anglický originál a plná specifikace:** [BMFF na 3GPP Explorer](https://3gpp-explorer.com/glossary/bmff/)
