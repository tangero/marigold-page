---
slug: "hevc"
url: "/mobilnisite/slovnik/hevc/"
type: "slovnik"
title: "HEVC – High Efficiency Video Coding"
date: 2025-01-01
abbr: "HEVC"
fullName: "High Efficiency Video Coding"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hevc/"
summary: "HEVC (H.265) je standard pro kompresi videa, který zdvojnásobuje kompresní poměr dat ve srovnání se svým předchůdcem AVC (H.264). Umožňuje přenos kvalitního videa včetně obsahu 4K a 8K přes mobilní sí"
---

HEVC je standard pro kompresi videa, který zdvojnásobuje kompresní poměr dat oproti svému předchůdci AVC a umožňuje efektivní přenos kvalitního videa, jako je 4K, přes mobilní sítě s omezenou přenosovou kapacitou v systémech 3GPP.

## Popis

High Efficiency Video Coding (HEVC), známý také jako H.265 a MPEG-H Part 2, je standard pro kompresi videa vyvinutý společnou pracovní skupinou Joint Collaborative Team on Video Coding ([JCT-VC](/mobilnisite/slovnik/jct-vc/)). V rámci ekosystému 3GPP je standardizován jako kodek pro multimediální telefonii, streamování a vysílací služby. Architektura kodeku je založena na blokově hybridním přístupu ke kódování videa, podobně jako jeho předchůdce [AVC](/mobilnisite/slovnik/avc/), ale s významnými vylepšeními. Používá pokročilé techniky, jako jsou větší a flexibilnější blokové struktury (Coding Tree Units až 64x64 pixelů), vylepšená intra-predikce s 35 směrovými režimy, pokročilá predikce pohybových vektorů a techniky slučování (merge) a sofistikovanější in-loop filtry jako Sample Adaptive Offset (SAO). Tato vylepšení umožňují dosáhnout přibližně 50% snížení datového toku při zachování stejné vnímané kvality videa ve srovnání s AVC.

V síti 3GPP funguje HEVC v rámci rámce pro zpracování a doručování médií definovaného pro služby jako Multimedia Telephony Service for IMS ([MTSI](/mobilnisite/slovnik/mtsi/)), Packet-Switched Streaming Service (PSS) a Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)). Kodek je integrován do koncových zařízení (UE) a síťových prvků, jako je Media Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)) pro překódování nebo Broadcast-Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) pro vysílání. Proces kódování zahrnuje rozdělení každého snímku na Coding Tree Units ([CTU](/mobilnisite/slovnik/ctu/)), které jsou následně rekurzivně rozděleny na Coding Units ([CU](/mobilnisite/slovnik/cu/)) pomocí kvadrantové struktury. Na tyto CU se následně aplikuje predikce (intra nebo inter), transformace, kvantizace a entropické kódování. Výsledný datový proud je zabalen podle formátů definovaných 3GPP, jako je ISO Base Media File Format (ISOBMFF) pro streamování nebo Real-time Transport Protocol (RTP) pro konverzační služby.

Úlohou HEVC v síti je umožnit aplikace videa s vysokou účinností, které jsou hlavním hybatelem mobilního datového provozu. Pro poskytovatele služeb snižuje náklady na přenosovou kapacitu a úložiště spojené s doručováním videa s vysokým rozlišením. Pro uživatele umožňuje vyšší kvalitu zážitků, jako je video 4K Ultra HD na mobilních zařízeních, bez úměrného zvýšení spotřeby dat. Specifikace 3GPP definují profily, úrovně a formáty přenosu pro HEVC za účelem zajištění interoperability mezi zařízeními a sítěmi. To zahrnuje podporu různých barevných prostorů, vysokého dynamického rozsahu (HDR) a videa 360 stupňů, což z něj činí univerzální kodek pro multimediální služby nové generace.

## K čemu slouží

HEVC byl vytvořen, aby řešil exponenciální růst video provozu v mobilních sítích a omezení předchozího standardu AVC (H.264). Jak se spotřebitelská poptávka přesunula k videu s vyšším rozlišením (HD, 4K a nakonec 8K) a objevily se nové aplikace jako virtuální realita, kompresní účinnost AVC se stala úzkým hrdlem. Doručování takového obsahu by vyžadovalo neudržitelné množství síťové přenosové kapacity a úložiště, což by zvýšilo náklady operátorů a potenciálně zhoršilo uživatelský zážitek kvůli přetížení. Primární motivací bylo vyvinout kodek, který by mohl snížit potřebný datový tok na polovinu při ekvivalentní kvalitě, a tím zajistit budoucí připravenost sítí pro éru dat orientovaných na video.

Historicky každá nová generace video kodeku (např. MPEG-2, AVC) přinesla významný skok v kompresní účinnosti. HEVC pokračuje v tomto trendu, byl zahájen skupinou ITU-T Video Coding Experts Group (VCEG) a ISO/IEC Moving Picture Experts Group (MPEG) prostřednictvím jejich společné spolupráce. Jeho přijetí do 3GPP, počínaje Release 12, bylo motivováno potřebou standardizovat jeho použití v rámci služeb založených na IMS a streamování. Tím byl zajištěn jednotný, interoperabilní přístup k doručování videa v celosvětových mobilních sítích, který zabránil fragmentaci. Standardizací HEVC umožnil 3GPP operátorům efektivně nasazovat pokročilé video služby, podporující obchodní modely jako mobilní TV, video na vyžádání a kvalitní videohovory, které jsou ústřední pro portfolia služeb 4G a 5G.

## Klíčové vlastnosti

- Struktura Coding Tree Unit (CTU) podporující bloky až 64x64 pixelů pro efektivnější reprezentaci homogenních oblastí
- Pokročilá predikce pohybových vektorů včetně režimu Merge a Advanced Motion Vector Prediction (AMVP) ke snížení režie inter-predikce
- In-loop filtr Sample Adaptive Offset (SAO), který redukuje pruhování (banding) a zlepšuje subjektivní kvalitu
- Podpora nástrojů pro paralelní zpracování jako Tiles a Wavefront Parallel Processing (WPP) pro využití vícejádrových architektur
- Široká škála profilů a úrovní podporujících mainstreamové kódování, video s vysokým dynamickým rozsahem (HDR) a škálovatelné kódování videa
- Integrace s rámci pro doručování médií 3GPP včetně ISOBMFF pro streamování a RTP pro komunikaci v reálném čase

## Související pojmy

- [AVC – Assured Voice Communication](/mobilnisite/slovnik/avc/)
- [MTSI – Multimedia Telephony Services for IMS](/mobilnisite/slovnik/mtsi/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [5GMS – 5G Media Streaming](/mobilnisite/slovnik/5gms/)

## Definující specifikace

- **TS 22.864** (Rel-15) — 5G Network Operation Use Cases & Requirements
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 26.114** (Rel-19) — IMS Multimedia Telephony Media Handling
- **TS 26.116** (Rel-19) — TV Video Formats for 3GPP Services
- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.119** (Rel-19) — XR Media Capabilities for AR Devices
- **TS 26.140** (Rel-19) — MMS Media Formats and Codecs Specification
- **TS 26.223** (Rel-19) — IMS Telepresence Client Specification
- **TS 26.234** (Rel-19) — 3GPP PSS Protocols and Codecs Specification
- **TS 26.244** (Rel-19) — 3GPP File Format (3GP) Specification
- **TS 26.265** (Rel-19) — Video Operation Points & Capabilities
- **TS 26.281** (Rel-19) — MCVideo Codecs and Media Handling
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.511** (Rel-19) — 5G Media Streaming Profiles, Codecs & Formats
- **TS 26.522** (Rel-19) — RTP for XR in 5G Systems
- … a dalších 20 specifikací

---

📖 **Anglický originál a plná specifikace:** [HEVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/hevc/)
