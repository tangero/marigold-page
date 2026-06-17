---
slug: "mv-hevc"
url: "/mobilnisite/slovnik/mv-hevc/"
type: "slovnik"
title: "MV-HEVC – MultiView High Efficiency Video Coding"
date: 2025-01-01
abbr: "MV-HEVC"
fullName: "MultiView High Efficiency Video Coding"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mv-hevc/"
summary: "MV-HEVC je rozšíření standardu pro kompresi videa HEVC (H.265), které efektivně kóduje více pohledů na stejnou scénu. Je klíčové pro doručování 3D videa, televize s volným výběrem pohledu (FTV) a imer"
---

MV-HEVC je rozšíření standardu pro kompresi videa HEVC, které efektivně kóduje více pohledů na scénu pro 3D a imerzivní mediální služby v mobilních sítích, čímž snižuje potřebu šířky pásma ve srovnání s nezávislým kódováním jednotlivých pohledů.

## Popis

MV-HEVC, neboli Multi-view High Efficiency Video Coding, je standardizovaný profil kódování videa v rámci rodiny [HEVC](/mobilnisite/slovnik/hevc/) (H.265), speciálně navržený pro kompresi video sekvencí zachycených více kamerami sledujícími stejnou scénu z mírně odlišných perspektiv. Základní architektonický princip spočívá ve využití vysokého stupně meziplehlové redundance – podobností mezi různými kamerovými pohledy – kromě časové redundance v rámci sekvence jednoho pohledu. Toho je dosaženo pomocí pokročilých predikčních technik.

Kodek funguje tak, že jeden pohled je určen jako základní (base view) a je zakódován pomocí standardního jedno-vrstvého HEVC kodeku, což zajišťuje zpětnou kompatibilitu se staršími HEVC dekodéry. Další závislé pohledy jsou poté kódovány s intenzivním odkazováním na základní pohled a na další již zakódované závislé pohledy. Mezi klíčové nástroje kódování patří meziplehlová pohybová predikce, kde lze pohybové vektory predikovat z jiných pohledů; meziplehlová reziduální predikce; a predikce kompenzovaná disparitou, která je analogická pohybové kompenzaci, ale pro prostorové rozdíly mezi pohledy. Struktura bitového toku podporuje zapouzdření více pohledů spolu s potřebnými parametrickými sadami, které popisují vztahy mezi nimi (např. parametry kamery, pořadí pohledů).

V kontextu služeb 3GPP, jako je [MBMS](/mobilnisite/slovnik/mbms/) (Multimedia Broadcast Multicast Service) nebo streamování, umožňuje MV-HEVC efektivní doručování 3D nebo vícepohledového obsahu. Síť vysílá jeden integrovaný bitový tok. Kompatibilní klientské zařízení může dekódovat základní pohled pro 2D přehrávání nebo dekódovat více pohledů pro vykreslení stereoskopického 3D videa na kompatibilních displejích nebo pro umožnění interaktivního přepínání pohledu. Klíčovými komponentami jsou dekodér MV-HEVC, který implementuje meziplehlové predikční nástroje, a signalizace v rámci popisu mediální prezentace (např. [DASH](/mobilnisite/slovnik/dash/) [MPD](/mobilnisite/slovnik/mpd/)), která označuje dostupnost vícepohledových reprezentací. To umožňuje adaptivním streamovacím klientům vybrat vhodný počet pohledů na základě schopností zařízení, stavu sítě a uživatelských preferencí.

## K čemu slouží

MV-HEVC byl vyvinut, aby uspokojil požadavky nově vznikajících imerzivních video aplikací, jako je 3DTV, video s volným výběrem pohledu a virtuální realita, v rámci omezení šířky pásma mobilních sítí. Před jeho standardizací bylo vysílání více nezávislých video toků pro každý kamerový pohled neúměrně náročné na šířku pásma, což omezovalo proveditelnost takových služeb přes bezdrátové spoje.

Motivace vycházela z úspěchu dřívějšího vícepohledového kódování v H.264/[AVC](/mobilnisite/slovnik/avc/) ([MVC](/mobilnisite/slovnik/mvc/)) a z potřeby vyšší efektivity nabízené novějším [HEVC](/mobilnisite/slovnik/hevc/) kodekem. HEVC již poskytovalo přibližně 50% úsporu datového toku oproti H.264 pro video s jedním pohledem. MV-HEVC tyto úspory rozšiřuje do vícepohledové domény aplikací pokročilých kódovacích nástrojů HEVC napříč pohledy. Tím přímo řeší omezení předchozího standardu MVC tím, že poskytuje efektivnější, moderní základ kodeku, což umožňuje služby vícepohledového videa vysoké kvality v šířkově omezených sítích 4G a 5G. Byl klíčovým prvkem pro práci 3GPP na pokročilých mediálních službách v releasech zaměřených na vylepšené mobilní širokopásmové připojení a doručování médií.

## Klíčové vlastnosti

- Efektivní komprese více video pohledů prostřednictvím využití meziplehlové redundance
- Zpětná kompatibilita prostřednictvím základního pohledu, který lze dekódovat standardními HEVC dekodéry
- Pokročilé predikční nástroje včetně meziplehlové pohybové predikce a predikce kompenzované disparitou
- Podpora stereoskopického 3D videa a interaktivního přehrávání s volným výběrem pohledu
- Integrace s rámci pro doručování médií 3GPP, jako jsou DASH a MBMS
- Škálovatelný výběr pohledů umožňující klientům dekódovat podmnožinu pohledů na základě jejich schopností

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [MVC – Multi-view Video Coding](/mobilnisite/slovnik/mvc/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study

---

📖 **Anglický originál a plná specifikace:** [MV-HEVC na 3GPP Explorer](https://3gpp-explorer.com/glossary/mv-hevc/)
