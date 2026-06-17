---
slug: "ild"
url: "/mobilnisite/slovnik/ild/"
type: "slovnik"
title: "ILD – Inter-Channel Level Difference"
date: 2025-01-01
abbr: "ILD"
fullName: "Inter-Channel Level Difference"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ild/"
summary: "Inter-Channel Level Difference (ILD) je audio parametr ve specifikacích 3GPP pro imerzivní média, který definuje relativní rozdíl hladiny mezi zvukovými kanály. Je klíčový pro vytváření realistického"
---

ILD (Inter-Channel Level Difference) je relativní rozdíl hladiny mezi zvukovými kanály, což je audio parametr ve specifikacích 3GPP pro imerzivní média klíčový pro vytváření realistického prostorového zvuku.

## Popis

Inter-Channel Level Difference (ILD) je klíčový percepční atribut a technický parametr ve standardech 3GPP pro imerzivní audio, zejména těch souvisejících se 5G Media Streaming ([5GMS](/mobilnisite/slovnik/5gms/)) a Extended Reality (XR). Definován ve specifikacích jako TS 26.253 (Immersive Voice and Audio Services) kvantifikuje ILD rozdíl ve hladině akustického tlaku (nebo výkonu signálu) mezi dvěma či více zvukovými kanály v konkrétním časovém okamžiku pro daný audio objekt nebo scénu. V nastavení vícekanálového zvuku (např. stereo, 5.1 surround nebo Ambisonics) jsou tyto rozdíly hladin mezi kanály primární vodítko, které lidský sluchový systém používá k vnímání směru a šířky zdroje zvuku.

V kontextu kodeků a formátů imerzivních médií 3GPP, jako je MPEG-H 3D Audio nebo AC-4, jsou parametry ILD často součástí širší sady deskriptorů prostorového zvuku, která může zahrnovat Inter-Channel Time Difference (ICTD) a koherenci. Tyto parametry lze extrahovat během audio produkce, efektivně zakódovat jako metadata spolu se základními audio signály a následně použít kompatibilním audio rendererem v přehrávacím zařízení k rekonstrukci prostorového zvukového pole. Tento parametrický přístup umožňuje doručování vysoce kvalitního imerzivního zvuku při nižších datových tocích ve srovnání s nezávislým přenosem všech diskrétních kanálů, což je klíčové pro streamování přes mobilní sítě.

Technická implementace zahrnuje analýzu audio scény za účelem určení vztahů hladin mezi kanály pro různé kmitočtová pásma a časové segmenty. U objektového zvuku, kde jsou zvuky považovány za jednotlivé entity s polohovými metadaty, se ILD vypočítává na základě zamýšlené pozice audio objektu vůči posluchači a rozmístění reproduktorů. Renderer používá tato data ILD spolu s modelem přehrávacího prostředí (např. sluchátka nebo konkrétní sestava reproduktorů) k syntéze odpovídajících audio signálů pro každý výstupní kanál, čímž vytváří iluzi zvuků přicházejících z konkrétních směrů. Tento proces je zásadní pro poskytování přesvědčivých 360stupňových audio zážitků pro virtuální realitu (VR), rozšířenou realitu ([AR](/mobilnisite/slovnik/ar/)) a imerzivní telekonference.

## K čemu slouží

ILD byl standardizován v 3GPP, aby vyřešil rostoucí poptávku po vysoce kvalitních, přenosově efektivních službách imerzivního zvuku přes 5G sítě. Tradiční vícekanálový zvuk (jako 5.1 surround) přenáší každý kanál nezávisle, což vyžaduje vysoké datové toky, které jsou pro mobilní streamování neefektivní. S nástupem služeb jako 360stupňové video, VR a XR vznikla potřeba zvuku, který by mohl odpovídat vizuálnímu prožitku bez nadměrné spotřeby síťových prostředků.

Účelem zahrnutí ILD a souvisejících parametrů prostorového zvuku do specifikací 3GPP (významně od Rel-18) je umožnit doručování působivých trojrozměrných zvukových scén, které posilují pocit přítomnosti a realismu. ILD řeší problém efektivního reprezentování jednoho z nejdůležitějších psychoakustických vodítek pro lokalizaci zvuku. Parametrizací rozdílů hladin namísto odesílání plných diskrétních kanálů lze výrazně snížit datové toky audia při zachování percepční kvality, což činí imerzivní služby realizovatelnými na mobilních zařízeních.

Tento vývoj byl motivován konvergencí vysoké přenosové kapacity/nízké latence 5G s nástupem metaverse a XR aplikací. Standardizace těchto audio parametrů zajišťuje interoperabilitu mezi nástroji pro tvorbu obsahu, systémy pro doručování přes síť (prostřednictvím [5GMS](/mobilnisite/slovnik/5gms/)) a koncovými uživatelskými zařízeními (telefony, VR headset). Umožňuje tvůrcům obsahu vytvořit imerzivní audio jednou a mít jej správně vykresleno na široké škále přehrávacích systémů, od stereo sluchátek po složité sestavy reproduktorů, čímž řeší klíčový problém fragmentace v rodícím se ekosystému imerzivních médií.

## Klíčové vlastnosti

- Definuje rozdíly hladiny mezi zvukovými kanály jako prostorové vodítko
- Používá se pro efektivní parametrickou reprezentaci imerzivních audio scén
- Integrální součást specifikací audia pro 5G Media Streaming a XR v 3GPP
- Spolupracuje s Inter-Channel Time Difference (ICTD) pro lokalizaci zvuku
- Umožňuje přenosově efektivní doručování 3D zvuku přes mobilní sítě
- Podporuje objektové a scénové modely vykreslování zvuku

## Definující specifikace

- **TS 26.253** (Rel-19) — IVAS Codec Algorithmic Description
- **TS 26.260** (Rel-19) — Immersive Audio Objective Test Methods
- **TS 26.261** (Rel-19) — Electro-acoustic specs for immersive terminals

---

📖 **Anglický originál a plná specifikace:** [ILD na 3GPP Explorer](https://3gpp-explorer.com/glossary/ild/)
