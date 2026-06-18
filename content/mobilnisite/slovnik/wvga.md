---
slug: "wvga"
url: "/mobilnisite/slovnik/wvga/"
type: "slovnik"
title: "WVGA – Wide Video Graphics Array"
date: 2025-01-01
abbr: "WVGA"
fullName: "Wide Video Graphics Array"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/wvga/"
summary: "Standardizovaný formát rozlišení videa (typicky 854x480 pixelů) definovaný 3GPP pro multimediální služby. Zajišťuje konzistentní kvalitu videa a interoperabilitu pro streamování videa a komunikační ap"
---

WVGA je standardizovaný formát rozlišení mobilního videa 854x480 pixelů definovaný 3GPP za účelem zajištění konzistentní kvality a interoperability pro streamovací a komunikační služby jako MBMS a IMS.

## Popis

Wide Video Graphics Array (WVGA) je standard rozlišení video displeje definovaný ve specifikacích 3GPP, primárně v TS 26.938, který se zabývá multimediálními vysílacími a skupinovými službami ([MBMS](/mobilnisite/slovnik/mbms/)). Rozlišení je typicky 854 pixelů na šířku a 480 pixelů na výšku, což poskytuje širokoúhlý poměr stran přibližně 16:9. Tento formát je širší variantou tradičního rozlišení [VGA](/mobilnisite/slovnik/vga/) (640x480), přizpůsobenou moderním širokoúhlým displejům běžně používaným v mobilních zařízeních, tabletech a další spotřební elektronice. V rámci ekosystému 3GPP slouží WVGA jako referenční nebo cílové rozlišení pro doručování video obsahu, čímž zajišťuje, že multimediální služby mohou být konzistentně kódovány, přenášeny a dekódovány napříč různými síťovými implementacemi a uživatelskými zařízeními (UE).

Z architektonického hlediska je WVGA integrováno do multimediálního rámce 3GPP, zejména v kontextu služby Multimedia Broadcast Multicast Service (MBMS) a IP Multimedia Subsystem (IMS). Specifikace definuje technické parametry pro video kódování, včetně profilů kodeků, přenosových rychlostí a snímkových frekvencí spojených s rozlišením WVGA. Tato standardizace je klíčová pro komplexní výkon video služeb, protože umožňuje poskytovatelům obsahu a síťovým operátorům optimalizovat video proudy pro známé rozlišení, čímž vyvažují kvalitu a efektivitu využití šířky pásma. Multimediální schopnosti UE, včetně podpory WVGA, jsou často součástí testů shody zařízení, aby byla zajištěna základní kvalita uživatelského zážitku ([QoE](/mobilnisite/slovnik/qoe/)).

Při provozu, když je zahájena video služba – například mobilní televizní vysílání přes MBMS nebo video hovor přes IMS – síť a UE vyjednávají schopnosti, které mohou zahrnovat podporu rozlišení WVGA. Video obsah je zakódován ve zdroji (např. vysílacím serveru nebo jiném UE) pomocí kodeků jako H.264/[AVC](/mobilnisite/slovnik/avc/) nebo H.265/[HEVC](/mobilnisite/slovnik/hevc/) s parametry sladěnými se specifikacemi WVGA. Během přenosu přes rádiovou přístupovou síť (RAN) a páteřní síť je video proud paketizován a doručován pomocí protokolů jako [RTP](/mobilnisite/slovnik/rtp/)/[UDP](/mobilnisite/slovnik/udp/)/IP. Na přijímací straně UE proud dekóduje a vykreslí na displeji, přičemž využívá WVGA k poskytnutí širokoúhlého zobrazení bez zkreslení nebo nadměrného škálování.

Klíčové komponenty spojené s WVGA v systémech 3GPP zahrnují MBMS Gateway ([MBMS-GW](/mobilnisite/slovnik/mbms-gw/)), Broadcast Multicast Service Center (BM-SC) a multimediální procesní jednotku UE. BM-SC zajišťuje provisioning obsahu a plánování, přičemž dbá na to, aby video proudy vyhovovaly parametrům WVGA pro vysílací relace. MBMS-GW spravuje distribuci dat k základnovým stanicím, zatímco software a hardware UE dekódují proud v souladu s omezeními rozlišení. Úlohou WVGA je standardizovat jeden aspekt kvality videa, což usnadňuje interoperabilitu a snižuje problémy s kompatibilitou v heterogenních síťových prostředích, od 4G LTE po 5G NR, kde jsou multimediální služby klíčovým zdrojem příjmů.

## K čemu slouží

WVGA bylo zavedeno ve 3GPP Release 12, aby řešilo rostoucí poptávku po standardizovaných video rozlišeních v mobilních multimediálních službách. Před jeho definicí často trpělo doručování video obsahu přes mobilní sítě nekonzistencí v podpoře rozlišení napříč různými zařízeními a sítěmi, což vedlo k suboptimálnímu uživatelskému zážitku, jako jsou zkreslené poměry stran, špatná kvalita videa nebo selhání kompatibility. Rozšíření širokoúhlých displejů na chytrých telefonech a tabletech si vyžádalo formát rozlišení, který by odpovídal těmto obrazovkám a zároveň byl efektivní pro síťový přenos. WVGA poskytuje společný referenční bod, který umožňuje poskytovatelům obsahu kódovat videa jednou pro široké publikum, snižuje složitost a zajišťuje předvídatelnou kvalitu služby (QoS).

Historicky se mobilní video služby vyvíjely od nízkých rozlišení jako QCIF (176x144) k vyšším definicím jako VGA (640x480), ale ty byly často navrženy pro poměr stran 4:3, který neodpovídal moderním širokoúhlým zařízením. Tento nesoulad způsoboval černé pruhy nebo ořezávání, což degradovalo zážitek z prohlížení. WVGA se svým poměrem stran 16:9 tento problém přímo řeší tím, že nabízí rozlišení, které odpovídá současným displejům bez úprav. Jeho standardizace ve specifikacích 3GPP, zejména pro aplikace MBMS a IMS, byla motivována potřebou podporovat služby jako mobilní televize, streamování videa a komunikace v reálném čase s konzistentní kvalitou napříč různými modely UE a síťovými podmínkami.

Definováním WVGA 3GPP také usnadňuje optimalizaci sítě, protože operátoři mohou plánovat přidělování šířky pásma a nastavení kodeků na základě známého profilu rozlišení. To pomáhá při řízení zahlcení sítě a zlepšování spektrální efektivity, zejména pro vysílací služby, kde stejný obsah konzumuje více uživatelů. WVGA v podstatě existuje za účelem harmonizace doručování videa v mobilním ekosystému, řeší problémy interoperability a zlepšuje celkový multimediální zážitek jako součást širšího úsilí 3GPP standardizovat pokročilé služby od Release 12 dále.

## Klíčové vlastnosti

- Standardizované rozlišení 854x480 pixelů pro širokoúhlý poměr stran 16:9
- Integrace s multimediálními službami 3GPP jako MBMS a IMS pro konzistentní doručování videa
- Podpora moderních kodeků jako H.264/AVC a H.265/HEVC v rámci specifikovaných parametrů
- Umožňuje interoperabilitu napříč různými uživatelskými zařízeními a síťovými implementacemi
- Usnadňuje optimalizaci kvality uživatelského zážitku (QoE) poskytnutím základního video formátu
- Používá se v testech shody k zajištění, že multimediální schopnosti UE splňují síťové požadavky

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [QoE – Quality of Experience](/mobilnisite/slovnik/qoe/)

## Definující specifikace

- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [WVGA na 3GPP Explorer](https://3gpp-explorer.com/glossary/wvga/)
