---
slug: "pbcp"
url: "/mobilnisite/slovnik/pbcp/"
type: "slovnik"
title: "PBCP – Personal Broadcast Contents Provider"
date: 2025-01-01
abbr: "PBCP"
fullName: "Personal Broadcast Contents Provider"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pbcp/"
summary: "Servisní poskytovatel (entita) definovaný v 3GPP pro doručování personalizovaného vysílaného obsahu mobilním uživatelům. Představuje zdroj nebo agregátor obsahu v architektuře Personal Broadcast Servi"
---

PBCP je servisní poskytovatel (entita) v 3GPP, který v rámci architektury Personal Broadcast Service funguje jako zdroj nebo agregátor obsahu pro doručování personalizovaného vysílaného obsahu mobilním uživatelům.

## Popis

Personal Broadcast Contents Provider (PBCP) je funkční entita v architektuře služby Personal Broadcast Service ([PBS](/mobilnisite/slovnik/pbs/)) dle 3GPP, standardizovaná primárně v TS 22.947. Funguje jako zdroj nebo agregátor multimediálního obsahu určeného pro vysílání definované skupině účastníků. PBCP je zodpovědný za přípravu obsahu, včetně kódování, formátování a zabalení podle specifikací 3GPP pro vysílací mechanismy, jako je Multimedia Broadcast Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)) nebo evolved MBMS (eMBMS). Rozhraní s jádrovými komponentami vysílací sítě, jako je Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), slouží k zahájení a správě vysílacích relací.

Z architektonického hlediska se PBCP nachází ve služební vrstvě a je často provozován třetími stranami (mediálními společnostmi) nebo samotnými mobilními operátory. Poskytuje BM-SC potřebná metadata a obsahové toky, které BM-SC následně distribuuje přes rádiovou přístupovou síť. PBCP může také implementovat servisní logiku pro personalizaci, například definici cílových skupin uživatelů na základě předplatného, polohy nebo preferencí. To zahrnuje interakci s uživatelskými databázemi a systémy správy předplatného, aby byl obsah doručen pouze autorizovaným příjemcům.

Během provozu začíná role PBCP příjmem obsahu a končí vydáním příkazů k zahájení relace směrem k BM-SC. Zajišťuje, aby obsah splňoval vysílací standardy, spravuje digitální práva a může podporovat funkce jako oznámení služeb pro informování uživatelů o dostupných vysíláních. PBCP je klíčovou komponentou pro efektivní doručování obsahu typu jeden-všem, které ve srovnání s unicastovým streamováním populárních událostí nebo médií snižuje zatížení sítě. Jeho integrace do sítí 3GPP podporuje komerční vysílací služby, nouzová varování a další scénáře skupinové komunikace, čímž vytváří most mezi tvůrci obsahu a mobilní vysílací infrastrukturou.

## K čemu slouží

PBCP byl zaveden, aby formalizoval roli poskytovatelů obsahu ve vysílacích architekturách 3GPP a řešil potřebu standardizovaných rozhraní a procedur pro doručování personalizovaného vysílaného obsahu. Před jeho definicí chybělo ve vysílacích službách jasné architektonické oddělení mezi zdrojem obsahu a síťovou distribucí, což vedlo k proprietárním implementacím a problémům s interoperabilitou. Specifikace PBCP ve vydání 9 měla za cíl umožnit škálovatelné komerční vysílací služby přes mobilní sítě definováním samostatné entity zodpovědné za přípravu obsahu a správu služeb.

Motivován růstem spotřeby mobilních médií a neefektivitou unicastového doručování pro populární obsah vyvinul 3GPP službu Personal Broadcast Service pro optimalizaci síťových zdrojů. PBCP řeší problém integrace různorodých zdrojů obsahu do vysílacího ekosystému a zajišťuje, že je obsah správně naformátován a autorizován pro distribuci. Podporuje obchodní modely, kde poskytovatelé třetích stran mohou nabízet vysílaný obsah na bázi předplatného nebo podpory reklamou, čímž rozšiřují nabídku služeb operátorů. Standardizací PBCP 3GPP usnadnilo nasazení služeb jako mobilní [TV](/mobilnisite/slovnik/tv/), streamování živých událostí a veřejná varování, čímž vytvořilo základ pro efektivní hromadnou komunikaci v sítích LTE a 5G.

## Klíčové vlastnosti

- Příprava a kódování obsahu pro vysílací standardy
- Rozhraní s Broadcast Multicast Service Center (BM-SC) pro správu relací
- Podpora personalizovaného cílení vysílání a definice uživatelských skupin
- Poskytování metadat pro oznámení a objevování služeb
- Integrace se systémy správy předplatného a digitálních práv
- Soulad s vysílacími mechanismy 3GPP, jako jsou MBMS a eMBMS

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [BM-SC – Broadcast-Multicast Service Centre](/mobilnisite/slovnik/bm-sc/)

## Definující specifikace

- **TR 22.947** (Rel-19) — Personal Broadcast Service (PBS) Use Cases

---

📖 **Anglický originál a plná specifikace:** [PBCP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pbcp/)
