---
slug: "imc"
url: "/mobilnisite/slovnik/imc/"
type: "slovnik"
title: "IMC – IMS Media Coding"
date: 2026-01-01
abbr: "IMC"
fullName: "IMS Media Coding"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/imc/"
summary: "IMS Media Coding (IMC, kódování médií v IMS) označuje kodeky a standardy pro zpracování médií používané v IP Multimedia Subsystem (IMS) pro hlasové, video a jiné multimediální relace. Zajišťuje intero"
---

IMC je soubor kodeků a standardů pro zpracování médií používaných v IP Multimedia Subsystem (IMS), který zajišťuje interoperabilitu a kvalitu hlasových, video a multimediálních relací napříč různými zařízeními a sítěmi.

## Popis

IMS Media Coding (IMC) zahrnuje soubor standardů pro kódování médií, kodeků a funkcí pro zpracování definovaných v rámci architektury IP Multimedia Subsystem (IMS) od 3GPP. IMS je základní síťová architektura pro poskytování IP multimediálních služeb přes mobilní i pevné sítě a IMC zajišťuje, že mediální komponenty (audio, video, text) těchto služeb jsou konzistentně kódovány, přenášeny a dekódovány na různých koncových bodech a sítích. Specifikace jako TS 23.228 (IMS fáze 2) a TS 24.229 (řízení hovorů v IMS) odkazují na požadavky pro kódování médií, zatímco série TS 26 (specifikace kodeků) podrobně popisuje konkrétní kodeky jako [AMR](/mobilnisite/slovnik/amr/), [EVS](/mobilnisite/slovnik/evs/) nebo H.264/[AVC](/mobilnisite/slovnik/avc/). IMC zahrnuje nejen samotné kodeky, ale také procedury pro vyjednávání kodeků, adaptaci médií a v případě potřeby překódování.

Při navazování relace v IMS, například VoIP hovoru nebo videokonference, se pro signalizaci používá protokol Session Initiation Protocol (SIP). Během výměny SIP zpráv koncové body pomocí nabídek a odpovědí protokolu Session Description Protocol (SDP) vyjednávají mediální parametry. Toto vyjednávání zahrnuje výběr kompatibilních kodeků ze sady IMC, stanovení přenosových rychlostí, snímkových frekvencí a dalších atributů média. Jádro IMS, včetně prvků jako Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)), může napomáhat zpracování médií. MRF může poskytovat služby překódování, pokud koncové body podporují různé kodeky, a tím zajistit interoperabilitu. Například zařízení používající kodek Enhanced Voice Services (EVS) může komunikovat se starším zařízením používajícím Adaptive Multi-Rate (AMR) právě díky překódování v MRF.

IMC pokrývá řadu kodeků optimalizovaných pro různé podmínky. Pro řeč existují úzkopásmové ([AMR-NB](/mobilnisite/slovnik/amr-nb/)), širokopásmové ([AMR-WB](/mobilnisite/slovnik/amr-wb/)) a superširokopásmové/plnopásmové (EVS) kodeky, z nichž každý nabízí různou kvalitu a efektivitu využití šířky pásma. Pro video jsou podporovány kodeky jako H.264, H.265 a VP8. Volba kodeku ovlivňuje využití síťové šířky pásma, spotřebu baterie na zařízeních a uživatelský zážitek. Standardy IMC také definují výkonnostní metriky, povinnou a volitelnou podporu kodeků pro zařízení a sítě a procedury pro dynamické přepínání mezi kodeky během relace (např. pro přizpůsobení se měnícím se síťovým podmínkám). Bezpečnostní aspekty, jako jsou šifrované mediální toky, jsou také v kontextu IMC zohledněny. Celkově IMC poskytuje technický základ pro kvalitní a interoperabilní multimediální komunikaci v IMS, což umožňuje služby jako VoLTE, ViLTE a rich communication services (RCS).

## K čemu slouží

IMS Media Coding bylo vyvinuto, aby řešilo problém nekonzistentního zpracování médií v raných IP multimediálních službách. Bez standardizovaných kodeků a procedur vyjednávání mohly koncové body používat nekompatibilní mediální formáty, což vedlo k neúspěšným relacím nebo špatné kvalitě. Rozšíření různorodých kodeků napříč zařízeními a sítěmi si vyžádalo vytvoření rámce v rámci IMS pro zajištění bezproblémové multimediální komunikace. IMC tento rámec poskytuje definováním preferované sady kodeků a procedur pro vyjednávání a adaptaci médií.

Hlavními problémy, které IMC řeší, jsou interoperabilita a zajištění kvality. Specifikací společné sady kodeků (jako [AMR](/mobilnisite/slovnik/amr/) pro hlas a H.264 pro video), které by měly sítě IMS a zařízení podporovat, snižuje pravděpodobnost nekompatibility. Dále zavádí mechanismy, jako je překódování přes [MRF](/mobilnisite/slovnik/mrf/), které překlenují rozdílné možnosti kodeků a zajišťují, že relace mohou proběhnout i v případě, že koncové body podporují různé kodeky. To je obzvláště důležité v mobilních sítích, kde se zařízení pohybují od pokročilých smartphonů po základní feature telefony. IMC také řeší efektivitu využití šířky pásma tím, že zahrnuje kodeky přizpůsobující přenosovou rychlost síťovým podmínkám, čímž optimalizuje využití zdrojů při zachování přijatelné kvality. Zavedeno v Release 5 spolu se samotným IMS, IMC se vyvíjelo, aby zahrnovalo novější a efektivnější kodeky (např. EVS, H.265), a tak drželo krok s pokrokem technologie a uživatelskými očekáváními vyšší kvality médií.

## Klíčové vlastnosti

- Standardizovaná sada řečových a video kodeků pro IMS (např. AMR, EVS, H.264)
- Procedury vyjednávání kodeků využívající SDP v SIP signalizaci
- Možnosti překódování přes Media Resource Function (MRF) pro zajištění interoperability
- Podpora adaptivní přenosové rychlosti a přepínání kodeků během relací
- Metriky kvality a výkonu pro média v relacích IMS
- Bezpečnostní hlediska pro šifrování médií

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRFC – Multimedia Resource Function Controller](/mobilnisite/slovnik/mrfc/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.944** (Rel-19) — UE Functionality Split Scenarios and Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP
- **TS 33.203** (Rel-19) — IMS Security Specification

---

📖 **Anglický originál a plná specifikace:** [IMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/imc/)
