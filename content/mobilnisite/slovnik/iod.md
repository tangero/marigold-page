---
slug: "iod"
url: "/mobilnisite/slovnik/iod/"
type: "slovnik"
title: "IOD – Inter-aural Output Difference"
date: 2025-01-01
abbr: "IOD"
fullName: "Inter-aural Output Difference"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/iod/"
summary: "IOD je parametr používaný v audiokodecích a službách 3GPP k vyjádření vnímaného rozdílu hladiny zvukového signálu mezi dvěma ušima posluchače. Je klíčový pro vytváření realistického prostorového zvuku"
---

IOD je parametr používaný v audiokodecích 3GPP k vyjádření vnímaného rozdílu hladiny zvuku mezi dvěma ušima posluchače, což je klíčové pro vytváření realistického prostorového zvuku.

## Popis

Inter-aural Output Difference (IOD) je psychoakustický parametr definovaný ve specifikacích 3GPP týkajících se kódování audia a přenosu médií. Kvantifikuje vnímaný rozdíl ve zvukové hladině (intenzitě) dopadající na levé a pravé ucho posluchače. Tento parametr je klíčovou součástí percepčního modelování prostorového zvuku a umožňuje zvukovým systémům simulovat přirozené podněty, které lidé používají pro lokalizaci zvuku. V technických implementacích se IOD často odvozuje nebo používá spolu s dalšími prostorovými parametry, jako je Inter-aural Time Difference ([ITD](/mobilnisite/slovnik/itd/)) a Head-Related Transfer Functions ([HRTF](/mobilnisite/slovnik/hrtf/)), pro vykreslování binauračního zvuku.

V rámci architektury 3GPP se parametry IOD typicky generují, kódují a přenášejí jako součást imerzivních mediálních datových přenosů. Specifikace jako TS 26.928 (Extended Reality (XR) in 5G) definují, jak jsou tyto prostorové audio parametry zabaleny pro efektivní streamování přes mobilní sítě. Parametr není samostatným protokolem, ale datovým prvkem v audiokodecích a formátech pro popis médií. Funguje tak, že je vypočítán ve fázi tvorby obsahu nebo kódování na základě prostorových vlastností zdrojového zvuku a zamýšlené pozice posluchače.

Role IOD v síti je součástí end-to-end řetězce přenosu médií. Během relace, jako je hovor XR nebo služba imerzivního streamování, aplikační server nebo mediální enkodér generuje metadata prostorového zvuku včetně IOD. Tato data jsou následně paketizována podle příslušných formátů přenosu Real-Time Transport Protocol (RTP) a přenášena přes systém 5G. Zařízení uživatele, například headset, dekóduje zvukový proud a používá přijatý parametr IOD spolu s dalšími daty k řízení svého binauračního vykreslovače. Tento proces vytváří iluzi zvuku přicházejícího z konkrétních směrů a zvyšuje realističnost.

Klíčové komponenty zahrnující IOD zahrnují mediální aplikační funkci, architekturu streamování médií 5G a klientský audio vykreslovač. Jeho hodnota je dynamická a může se měnit snímek po snímku ve zvukovém proudu, aby odrážela pohyb zdrojů zvuku. Přesnost parametrizace IOD přímo ovlivňuje kvalitu zážitku z prostorového zvuku, což z něj činí klíčový faktor pro komunikaci nové generace, jejímž cílem je poskytnout pocit přítomnosti. Jeho zařazení do standardů 3GPP zajišťuje interoperabilitu mezi zařízeními a službami různých výrobců pro imerzivní audio.

## K čemu slouží

IOD byl zaveden, aby řešil potřebu standardizovaných prostorových audio parametrů v mobilní telekomunikaci a umožnil pokročilé zvukové zážitky přesahující tradiční stereo. Před jeho standardizací bylo vytváření interoperabilních imerzivních audio služeb obtížné kvůli proprietárním metodám reprezentace prostorového zvuku. Omezení prostého stereo audia, které poskytuje pouze levopravou panorámu, se stalo zjevným s nástupem aplikací virtuální a rozšířené reality vyžadujících plnou 3D lokalizaci zvuku.

Vytvoření IOD v rámci 3GPP bylo motivováno posunem průmyslu směrem k rozšířené realitě (XR) a imerzivním médiím jako klíčovým případům užití 5G. Tyto aplikace vyžadují, aby síť dodávala audio, které přesvědčivě umisťuje zvuky kolem posluchače a vytváří pocit přítomnosti. Standardizací IOD spolu s dalšími parametry umožňuje 3GPP tvůrcům obsahu, síťovým operátorům a výrobcům zařízení implementovat prostorový zvuk konzistentním způsobem. Tím se řeší problém fragmentace a zajišťuje se, že uživatelé mají vysoce kvalitní, realistické zvukové zážitky bez ohledu na poskytovatele služeb nebo značku zařízení.

Historicky bylo zpracování prostorového zvuku omezeno na vyspělé profesionální nebo herní systémy. Jeho integrace do standardů 3GPP přináší tuto schopnost na masový trh mobilních zařízení a sítí. IOD jako percepční parametr umožňuje efektivní využití šířky pásma ve srovnání s přenosem plných vícekanálových zvukových proudů, protože může být použit k syntéze binauračního zvuku z mono nebo stereo základní vrstvy s metadaty. Tato efektivita je klíčová pro mobilní sítě, kde jsou šířka pásma a latence omezenými zdroji.

## Klíčové vlastnosti

- Vyjadřuje vnímaný rozdíl hladiny zvuku mezi levým a pravým uchem posluchače
- Používá se jako metadata v imerzivních audiokodecích a streamovacích formátech
- Umožňuje efektivní binaurační vykreslování pro 3D audio zážitky
- Standardizovaný parametr zajišťující interoperabilitu napříč zařízeními a sítěmi
- Dynamický parametr, který lze aktualizovat pro každý audio snímek, aby odrážel pohyb zdroje zvuku
- Integrální součást architektur rozšířené reality (XR) a streamování médií 3GPP

## Související pojmy

- [ITD – Inter-Channel Time Difference](/mobilnisite/slovnik/itd/)

## Definující specifikace

- **TR 26.928** (Rel-19) — Study on eXtended Reality (XR) in 5G
- **TS 36.305** (Rel-19) — UE Positioning in E-UTRAN Stage 2
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 44.031** (Rel-19) — Radio Resource LCS Protocol (RRLP)

---

📖 **Anglický originál a plná specifikace:** [IOD na 3GPP Explorer](https://3gpp-explorer.com/glossary/iod/)
