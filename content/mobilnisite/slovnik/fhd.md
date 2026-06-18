---
slug: "fhd"
url: "/mobilnisite/slovnik/fhd/"
type: "slovnik"
title: "FHD – Full High Definition"
date: 2025-01-01
abbr: "FHD"
fullName: "Full High Definition"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fhd/"
summary: "Standard rozlišení videa 1920x1080 pixelů, standardizovaný organizací 3GPP pro multimediální služby. Definuje požadavky na kvalitu pro streamování videa, vysílání a konverzační služby přes mobilní sít"
---

FHD je standardizované rozlišení videa 1920x1080 pixelů podle 3GPP, které definuje požadavky na kvalitu pro streamování, vysílání a konverzační služby přes mobilní sítě.

## Popis

Full High Definition (FHD) v kontextu 3GPP odkazuje na technické specifikace a požadavky na kvalitu služeb (QoS) pro videoobsah s rozlišením 1920 pixelů horizontálně a 1080 pixelů vertikálně, typicky při snímkové frekvenci 30 nebo 60 snímků za sekundu (fps). Je to klíčový ukazatel výkonu pro multimediální služby přes buněčné sítě, zahrnující streamování (např. MPEG-DASH, [HLS](/mobilnisite/slovnik/hls/)), služby multimediálního vysílání/multicastu ([MBMS](/mobilnisite/slovnik/mbms/)) a služby reálného času jako videohovory. Standardizace zahrnuje profily kodeků (např. H.264/[AVC](/mobilnisite/slovnik/avc/) High Profile, H.265/[HEVC](/mobilnisite/slovnik/hevc/) Main 10 Profile), rozsahy datového toku, limity latence a mechanismy odolnosti proti chybám, aby bylo zajištěno spolehlivé doručení videa v proměnných rádiových podmínkách.

Architektonicky je podpora FHD integrována napříč aplikační vrstvou, páteřní sítí a rádiovou přístupovou sítí. V aplikační vrstvě aplikační servery (např. streamovací servery, IMS aplikační servery) kódují a paketizují FHD video podle profilů specifikovaných 3GPP. V páteřní síti, zejména Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) a Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)), se uplatňují QoS politiky označené příslušnými QoS Class Identifiers ([QCI](/mobilnisite/slovnik/qci/)) pro zvýšení priority provozu FHD videa, čímž se zajišťuje dostatečná šířka pásma a nízká ztrátovost paketů. Na rádiové straně [eNB](/mobilnisite/slovnik/enb/)/gNB dynamicky plánuje rádiové zdroje pomocí algoritmů, které berou v úvahu indikátory kvality kanálu (CQI) a stav vyrovnávací paměti, aby udržely vysoké datové toky (typicky 5-10 Mbps) potřebné pro FHD streamování bez zasekávání.

Mezi klíčové technické komponenty patří logika adaptivního datového toku (ABR), kde klientské zařízení monitoruje síťové podmínky a vyžaduje od serveru různé kvalitní reprezentace (včetně FHD), jak je definováno v 3GPP TS 26.247 pro DASH. Pro vysílání architektura evolved Multimedia Broadcast Multicast Service (eMBMS) v TS 26.346 specifikuje, jak je FHD obsah multiplexován a přenášen přes LTE/5G vysílací přenašeče. Úloha FHD v síti spočívá v poskytnutí srovnávacího standardu pro prémiové multimediální služby, což pohání vylepšení v rádiové efektivitě (např. vyšší modulace jako 256-QAM, agregace nosných), kapacitě páteřní sítě a správě QoS od konce ke konci. Ovlivňuje také schopnosti zařízení, vyžadující pokročilé procesory pro zobrazení, dostatečnou vyrovnávací paměť a efektivní hardwarové dekodéry kodeků.

## K čemu slouží

Standardizace FHD v 3GPP byla motivována explozivním růstem video provozu a uživatelskou poptávkou po vysoce kvalitních vizuálních zážitcích na mobilních zařízeních. Před jejím formálním definováním byly video služby přes mobilní sítě omezeny na standardní rozlišení (SD) nebo nižší kvůli omezením šířky pásma a nedostatku konzistentních QoS mechanismů. Rozšíření chytrých telefonů s vysokým rozlišením displeje a úspěch streamovacích služeb OTT vytvořily potřebu, aby síťoví operátoři nabízeli diferencované, vysoce kvalitní video jako konkurenční službu.

Primární problém, který FHD řeší, je zajištění toho, aby video s vysokým rozlišením mohlo být spolehlivě a efektivně doručováno přes paketově přepínané mobilní sítě, které jsou inherentně proměnlivé z hlediska propustnosti a latence. Bez standardizovaných profilů a QoS zpracování by FHD video trpělo neustálým bufferingem, artefakty a špatným uživatelským zážitkem. Práce 3GPP, počínaje Release 14, poskytla společný rámec pro parametry kodeků, transportní protokoly a síťové politiky, což umožnilo interoperabilitu mezi poskytovateli obsahu, síťovým vybavením a zařízeními.

Historicky FHD navázalo na dřívější video standardy jako QCIF a VGA definované v 3GPP pro 3G služby. Řešilo omezení těchto formátů, která byla nedostatečná pro moderní tablety a telefony s velkými displeji. Definováním požadavků na FHD 3GPP usnadnilo vývoj mobilních sítí z primárně hlasově orientované infrastruktury na infrastrukturu schopnou multimédií, podporující služby jako živé TV vysílání, videohovory v ultra vysokém rozlišení a imerzivní média. To také pohánělo pokrok ve video kompresi (HEVC, VVC) a síťovém dělení pro služby se zaručeným datovým tokem.

## Klíčové vlastnosti

- Standardizované rozlišení 1920x1080 pixelů s definovanými snímkovými frekvencemi (např. 30, 60 fps)
- Specifikuje profily a úrovně kodeků (např. H.264/AVC, H.265/HEVC) pro efektivní kompresi
- Integruje se s adaptivním datovým tokem (DASH, HLS) pro dynamickou úpravu kvality
- Vyžaduje vynucení QoS prostřednictvím QCI a řízení politik pro zaručený datový tok a nízkou latenci
- Podporuje jak unicastové (streamování), tak multicastové/broadcastové (eMBMS) mechanismy doručování
- Definuje ukazatele výkonu od konce ke konci, jako je počáteční zpoždění, poměr zasekávání a poměr šum-vrcholový signál (PSNR)

## Související pojmy

- [QCI – Quality of Service Class Identifier](/mobilnisite/slovnik/qci/)
- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)

## Definující specifikace

- **TR 22.816** (Rel-14) — 3GPP TV Service Enhancement Technical Report
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TR 26.929** (Rel-19) — QoE Metrics for VR Services Study
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study

---

📖 **Anglický originál a plná specifikace:** [FHD na 3GPP Explorer](https://3gpp-explorer.com/glossary/fhd/)
