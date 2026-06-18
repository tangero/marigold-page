---
slug: "cibr"
url: "/mobilnisite/slovnik/cibr/"
type: "slovnik"
title: "CIBR – Common Informative Binaural Renderer"
date: 2025-01-01
abbr: "CIBR"
fullName: "Common Informative Binaural Renderer"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cibr/"
summary: "CIBR je standardizovaný binaurální renderer pro imerzivní audiovizuální služby, jako je rozšířená realita (XR) a 3GPP Audio. Zpracovává prostorové audioobjekty a popisy scén za účelem generování binau"
---

CIBR je standardizovaný binaurální renderer, který zpracovává prostorový zvuk za účelem generování signálů pro sluchátka pro konzistentní 3D zvuk ve službách jako rozšířená realita a 3GPP Audio.

## Popis

Common Informative Binaural Renderer (CIBR) je normativní komponenta definovaná v rámci řady 3GPP Media Streaming (26.xxx), konkrétně pro imerzivní audiovizuální služby. Funguje jako referenční zvukový procesor navržený k dekódování a vykreslování zvukových scén složených z audioobjektů a přidružených prostorových metadat do binaurálního stereo signálu vhodného pro přehrávání na sluchátkách. CIBR nemusí být fyzicky implementován v každém zařízení, ale slouží jako společná algoritmická specifikace, vůči které lze testovat shodu komerčních rendererů, čímž zajišťuje interoperabilitu a základní úroveň kvality uživatelského zážitku.

Architektonicky CIBR pracuje s kódovaným zvukovým datovým tokem, který obsahuje jak zvukovou podstatu (samotné zvukové signály), tak doprovodné informace popisu scény (Spatial Audio Object Coding - SAOC). Tento popis scény definuje vlastnosti každého audioobjektu, jako je jeho pozice v 3D prostoru (azimut, elevace, vzdálenost), hladina a případně další akustické vlastnosti. Jádrem zpracování rendereru je aplikace přenosových funkcí hlavy (Head-Related Transfer Functions - [HRTF](/mobilnisite/slovnik/hrtf/)) nebo podobných prostorových filtrů na každý audioobjekt na základě jeho metadat. Tyto filtry simulují akustické signály (meziušní časové a hladinové rozdíly, spektrální tvarování), které lidský sluchový systém používá k lokalizaci zvuků v prostoru. CIBR následně smíchá všechny zpracované signály objektů dohromady, čímž vytvoří konečný dvoukanálový binaurální výstup.

Klíčové vnitřní komponenty specifikace CIBR zahrnují dekodér pro SAOC datový tok, binaurální vykreslovací engine s jeho databází HRTF nebo metodou zpracování a funkce pro mixování/omezování, které zajišťují integritu výstupního signálu. Jeho role v ekosystému 3GPP je klíčová pro služby jako [VR](/mobilnisite/slovnik/vr/)/[AR](/mobilnisite/slovnik/ar/)/[XR](/mobilnisite/slovnik/xr/) a pokročilé telekonference, kde je realistické a stabilní umístění zvuku zásadní pro imerzi a komunikaci. Standardizací informativního chování rendereru 3GPP zajišťuje, že jednou vytvořená zvuková scéna bude reprodukována s předvídatelným prostorovým dojmem na jakémkoli kompatibilním přehrávacím zařízení, bez ohledu na podrobnosti hardwarové nebo softwarové implementace skutečného rendereru produktu.

## K čemu slouží

CIBR byl vytvořen k řešení kritického problému interoperability zvuku a konzistentní kvality v nově vznikajících imerzivních mediálních službách. Před jeho standardizací bylo binaurální vykreslování prostorového zvuku implementováno proprietárním, roztříštěným způsobem různými výrobci zařízení, tvůrci obsahu a poskytovateli platforem. To vedlo ke scénáři „babylónské věže“, kdy obsah vytvořený pro renderer jednoho dodavatele mohl znít zcela odlišně – s objektům na nesprávných místech nebo narušenou prostorovou imerzí – při přehrání na jiném zařízení, což vážně brzdilo růst ekosystému.

Historickým kontextem je vzestup rozšířené reality ([XR](/mobilnisite/slovnik/xr/)) a potřeba vysokokvalitního 3D zvuku doručovaného přes síť jako součást portfolia služeb 5G a dalších generací. 3GPP uznalo, že pro úspěch imerzivních služeb vyžaduje zvuková složka stejnou úroveň standardizace a spolehlivosti jako video kodeky. CIBR řeší omezení předchozích ad-hoc přístupů tím, že poskytuje společný, dobře definovaný cíl pro vykreslování. Umožňuje srovnávací testování výkonu, umožňuje testy kvality a dává tvůrcům obsahu jistotu, že jejich záměr v oblasti prostorového zvuku bude zachován. Tato standardizace snižuje vstupní bariéry, podporuje konkurenční trh implementací rendererů a v konečném důsledku garantuje základní uživatelský zážitek, což je nezbytné pro široké přijetí XR a dalších imerzivních zvukových aplikací přes mobilní sítě.

## Klíčové vlastnosti

- Standardizované dekódování a zpracování datových toků Spatial Audio Object Coding (SAOC)
- Normativní binaurální vykreslování využívající prostorovou lokalizaci založenou na přenosových funkcích hlavy (HRTF)
- Podpora dynamických audioobjektů s časově proměnnou pozicí a dalšími metadaty
- Bod shody pro implementátory za účelem zajištění interoperability imerzivních audiovizuálních služeb
- Výstup standardizovaného formátu dvoukanálového binaurálního signálu pro přehrávání na sluchátkách
- Integrace v rámci architektury 3GPP Media Streaming pro poskytování služeb end-to-end

## Definující specifikace

- **TS 26.118** (Rel-19) — Virtual Reality Media Formats
- **TS 26.818** (Rel-15) — Audio Media Profiles Test Results for VR Streaming

---

📖 **Anglický originál a plná specifikace:** [CIBR na 3GPP Explorer](https://3gpp-explorer.com/glossary/cibr/)
