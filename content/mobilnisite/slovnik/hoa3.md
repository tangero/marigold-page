---
slug: "hoa3"
url: "/mobilnisite/slovnik/hoa3/"
type: "slovnik"
title: "HOA3 – Higher-Order Ambisonics (3rd order)"
date: 2025-01-01
abbr: "HOA3"
fullName: "Higher-Order Ambisonics (3rd order)"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hoa3/"
summary: "3D audio formát pro služby imerzivních médií, standardizovaný pro přenos v systémech 5G. Umožňuje prostorové zvukové zážitky díky reprezentaci zvukového pole s vyšším rozlišením než Ambisonics prvního"
---

HOA3 je 3D audio formát standardizovaný konsorciem 3GPP pro imerzivní média v sítích 5G, využívající Ambisonics třetího řádu pro prostorový zvuk s vyšším rozlišením v aplikacích jako je virtuální a rozšířená realita.

## Popis

Higher-Order Ambisonics ([HOA](/mobilnisite/slovnik/hoa/)) je technika prostorového zvuku pokrývající celou sféru, která reprezentuje trojrozměrné zvukové pole pomocí sférických harmonických funkcí. HOA3 konkrétně označuje reprezentaci třetího řádu, která ve srovnání s Ambisonics prvního řádu ([FOA](/mobilnisite/slovnik/foa/)) poskytuje vyšší prostorové rozlišení a přesnější lokalizaci zdrojů zvuku. V kontextu 3GPP je HOA3 standardizován jako audiokodek a formát pro Media Streaming Services, což umožňuje přenos imerzivních zvukových zážitků přes sítě 5G, zejména pro aplikace rozšířené reality ([XR](/mobilnisite/slovnik/xr/)), jako je virtuální realita ([VR](/mobilnisite/slovnik/vr/)) a rozšířená realita ([AR](/mobilnisite/slovnik/ar/)). Technické specifikace definují formát bitového toku, zapouzdření a mechanismy synchronizace pro streamování HOA3 audia, čímž zajišťují interoperabilitu mezi nástroji pro tvorbu obsahu, streamovacími servery a klientskými zařízeními.

Z architektonického hlediska je HOA3 audio zpracováno a zakódováno mediálním serverem, často jako součást Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) nebo unicast streamovací služby. Zakódovaný bitový tok je paketizován podle formátů definovaných 3GPP (např. v kontejnerech MPEG-4 nebo podobných) a transportován přes 5G Core a rádiovou přístupovou síť. Na přijímací straně klientská aplikace nebo mediální přehrávač dekóduje HOA3 bitový tok. Proces dekódování zahrnuje rekonstrukci koeficientů sférických harmonických funkcí, které popisují pole akustického tlaku kolem bodu v prostoru. Tyto koeficienty jsou následně vykresleny pro přehrávání prostřednictvím sluchátek nebo reproduktorového pole, přičemž se pro sluchátka používají binaurální vykreslovací techniky a pro vícekanálová uspořádání dekódovací matice pro reproduktory, čímž vzniká iluze zvuku přicházejícího ze specifických směrů v 3D prostoru.

Úloha HOA3 v síti spočívá v tom, že je služebním prvkem pro pokročilá média. Je klíčovou součástí architektury 5G Media Streaming ([5GMS](/mobilnisite/slovnik/5gms/)) a rámce služeb 5G Immersive Media. Síť musí poskytnout dostatečnou šířku pásma a nízkou latenci pro streamování dat HOA3, která mají vyšší datový tok než konvenční stereo nebo prostorový audio formát prvního řádu. Ke zvýšení priority těchto streamů mohou být použity mechanismy Quality of Service (QoS). Specifikační práce zajišťují, že audio formát je nezávislý na podkladovém transportu, což mu umožňuje fungovat jak s vysílacím/multicastovým, tak s on-demand streamovacím modelem definovaným 3GPP.

## K čemu slouží

Primárním účelem standardizace HOA3 v rámci 3GPP je podpora přenosu vysoce kvalitních, imerzivních zvukových zážitků přes mobilní sítě, což je základním požadavkem pro přesvědčivé aplikace rozšířené reality ([XR](/mobilnisite/slovnik/xr/)). Před jeho zařazením služby XR často spoléhaly na jednodušší audio formáty, jako je stereo nebo Ambisonics prvního řádu, které nemohly poskytnout přesné prostorové zvukové podněty nezbytné pro skutečné ponoření a pocit přítomnosti uživatele ve virtuálních prostředích. Mezi omezení těchto dřívějších přístupů patřila slabá externalizace zvuku (zvuky se zdály být uvnitř hlavy) a nepřesná lokalizace zdrojů zvuku nad, pod a za posluchačem. HOA3 tato omezení řeší tím, že poskytuje reprezentaci zvukového pole s vyšší věrností.

Motivace pro jeho vytvoření v Rel-18 vychází z tlaku průmyslu směrem k metaverse a službám imerzivních médií jako klíčovým případům použití 5G. Standardizace zajišťuje interoperabilitu mezi různými tvůrci obsahu, poskytovateli sítí a výrobci zařízení a zabraňuje tak fragmentaci trhu. Definováním HOA3 ve specifikacích jako je TS 26.260 (Codec for immersive speech and audio services) poskytuje 3GPP jasný, technický základ bez licenčních poplatků (kde je to možné). To umožňuje mobilnímu ekosystému efektivně streamovat komplexní 3D audio bez nutnosti spoléhat se na proprietární, neinteroperabilní formáty, a tím urychlit adopci služeb XR přes sítě 5G.

## Klíčové vlastnosti

- Reprezentace pomocí sférických harmonických funkcí třetího řádu pro vysoké prostorové rozlišení
- Standardizovaný formát bitového toku pro interoperabilní streamování přes 5G
- Podpora plného 3D audia (perifonický zvuk), včetně elevace
- Efektivní komprese pro přenos po síti
- Mechanismy synchronizace s videem pro aplikace XR
- Kompatibilita s architekturami 5G Media Streaming (5GMS) a MBMS

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TR 26.933** (Rel-19) — Study on Diverse Audio Capturing System
- **TR 26.996** (Rel-19) — ISAR Split Rendering Audio Characterization
- **TR 26.997** (Rel-19) — IVAS Codec Specification

---

📖 **Anglický originál a plná specifikace:** [HOA3 na 3GPP Explorer](https://3gpp-explorer.com/glossary/hoa3/)
