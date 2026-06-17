---
slug: "jct-vc"
url: "/mobilnisite/slovnik/jct-vc/"
type: "slovnik"
title: "JCT-VC – Joint Collaborative Team on Video Coding"
date: 2025-01-01
abbr: "JCT-VC"
fullName: "Joint Collaborative Team on Video Coding"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/jct-vc/"
summary: "Společný tým pro spolupráci v oblasti videokódování (JCT-VC) byl partnerstvím mezi skupinou ITU-T VCEG a skupinou ISO/IEC MPEG, které vyvinulo standard High Efficiency Video Coding (HEVC/H.265). Organ"
---

JCT-VC (Společný tým pro spolupráci v oblasti videokódování) je partnerství mezi skupinou ITU-T VCEG a skupinou ISO/IEC MPEG, které vyvinulo standard HEVC/H.265, později přijatý organizací 3GPP pro mobilní video.

## Popis

Společný tým pro spolupráci v oblasti videokódování (JCT-VC) nebyl interním orgánem 3GPP, ale společným týmem založeným dvěma mezinárodními normalizačními organizacemi: skupinou [ITU-T](/mobilnisite/slovnik/itu-t/) Video Coding Experts Group (VCEG) a skupinou [ISO](/mobilnisite/slovnik/iso/)/[IEC](/mobilnisite/slovnik/iec/) Moving Picture Experts Group ([MPEG](/mobilnisite/slovnik/mpeg/)). 3GPP ve své roli specifikátora celých mobilních systémů odkazuje na standardy videokodeků vyvinuté takovými externími orgány a přijímá je. Hlavním výstupem JCT-VC byl standard High Efficiency Video Coding ([HEVC](/mobilnisite/slovnik/hevc/)), známý také jako H.265. Specifikace 3GPP, zejména TS 26.906 (shoda kodeku) a TS 26.955 (výkonnost kodeku), definují, jak je HEVC aplikován v rámci ekosystému 3GPP pro služby jako Multimedia Telephony Service for IMS ([MTSI](/mobilnisite/slovnik/mtsi/)), Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) a Packet-Switched Streaming Service (PSS). Technické fungování HEVC zahrnuje pokročilé kompresní techniky, které přibližně zdvojnásobují kompresní poměr dat ve srovnání s jeho předchůdcem H.264/[AVC](/mobilnisite/slovnik/avc/) při stejné úrovni kvality videa. Mezi klíčové architektonické komponenty patří větší a flexibilnější blokové struktury (Coding Tree Units – CTU až 64x64), sofistikovanější směry vnitrosnímkové predikce, vylepšené techniky predikce a slučování pohybových vektorů a vylepšená filtráce ve smyčce (Sample Adaptive Offset – SAO). V kontextu 3GPP klient videoslužby (např. na UE) a server vyjednají použití HEVC pomocí parametrů Session Description Protocol (SDP), specifikujících konkrétní profil a úroveň definované 3GPP, které omezují funkce kodeku, aby byla zajištěna interoperabilita a zvládnutelná výpočetní složitost na zařízeních. Zakódovaný videoproud je pak paketizován a přenášen přes IP sítě pomocí RTP/UDP nebo jiných přenašečů. Jeho role spočívá v umožnění efektivního doručování videa s vysokým rozlišením (např. 4K, 8K) a vysokým dynamickým rozsahem (HDR) přes rádiové spoje mobilních sítí s omezenou šířkou pásma, což je klíčové pro kvalitu uživatelského zážitku u mobilního streamování videa, videokonferencí a vysílacích služeb.

## K čemu slouží

JCT-VC byl založen za účelem vytvoření standardu videokódování nové generace, který by dokázal řešit explodující poptávku po videu s vyšším rozlišením (např. HD, 4K, 8K) a s tím spojená omezení šířky pásma, zejména v bezdrátových sítích. Omezení předchozího standardu H.264/AVC se stala zřejmými s rostoucím rozlišením videa; vyžadoval přibližně dvojnásobný datový tok pro srovnatelnou kvalitu při vyšších rozlišeních, což zatěžovalo kapacitu sítě a zvyšovalo náklady operátorů. Spolupráce mezi ITU-T a ISO/IEC spojila odborné znalosti k vývoji HEVC/H.265 s cílem dosáhnout 50% snížení datového toku při srovnatelné vnímané kvalitě. Pro 3GPP bylo přijetí HEVC motivováno potřebou specifikovat moderní kodek pro své multimediální služby, aby bylo zajištěno, že sítě 3G, 4G LTE a 5G mohou efektivně doručovat vysoce kvalitní video. Tím se vyřešil problém, jak nabízet atraktivní videoslužby (jako mobilní TV, videohovory a streamování), aniž by byly zahlceny rádiové prostředky nebo způsobovaly nadměrné buffering pro koncové uživatele. Historický kontext zahrnuje přechod od SD k HD videu v mobilních sítích a očekávání videa 4K/8K a 360 stupňů, což vše vyžadovalo pokročilejší kompresi, aby bylo komerčně životaschopné přes mobilní spojení.

## Klíčové vlastnosti

- Vysoká kompresní účinnost (přibližně 50% úspora datového toku oproti H.264/AVC)
- Podpora ultra vysokého rozlišení (až 8K) a vysokého dynamického rozsahu (HDR)
- Flexibilní dělení bloků pomocí Coding Tree Units (CTU) a kvadrantových struktur
- Pokročilé predikční režimy (35 směrů vnitrosnímkové predikce, sofistikovaná predikce pohybových vektorů)
- Vylepšené filtry ve smyčce (Deblocking Filter a Sample Adaptive Offset)
- Návrh pro paralelní zpracování (dlaždice, wavefront paralelní zpracování) pro hardware s více jádry

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TR 26.906** (Rel-19) — HEVC Evaluation for 3GPP Services
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services

---

📖 **Anglický originál a plná specifikace:** [JCT-VC na 3GPP Explorer](https://3gpp-explorer.com/glossary/jct-vc/)
