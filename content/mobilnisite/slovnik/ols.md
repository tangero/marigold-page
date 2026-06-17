---
slug: "ols"
url: "/mobilnisite/slovnik/ols/"
type: "slovnik"
title: "OLS – Output Layer Set"
date: 2025-01-01
abbr: "OLS"
fullName: "Output Layer Set"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ols/"
summary: "Output Layer Set (OLS) je koncept ve specifikaci 3GPP Release 13 a novějších, definovaný v dokumentu TS 26.948. Odkazuje na sadu výstupních vrstev ve videosignálu a umožňuje škálovatelné kódování vide"
---

OLS je sada výstupních vrstev ve videosignálu, definovaná ve specifikaci 3GPP Release 13, která umožňuje škálovatelné kódování videa pro adaptivní streamování přes mobilní sítě.

## Popis

Output Layer Set (OLS) je základní koncept v kontextu škálovatelného kódování videa, konkrétně pro standard High Efficiency Video Coding ([HEVC](/mobilnisite/slovnik/hevc/)) a jeho rozšíření, jak je přijat specifikací 3GPP pro služby doručování médií. OLS je definován jako sada vrstev ze škálovatelného videosignálu, které jsou určeny pro výstup k dekódování nebo prezentaci. Škálovatelný videosignál je strukturován do základní vrstvy a jedné či více zlepšujících vrstev. Základní vrstva poskytuje základní kvalitativní reprezentaci, zatímco zlepšující vrstvy postupně zvyšují kvalitu, rozlišení nebo snímkovou frekvenci, když jsou přidány. OLS specifikuje, která kombinace těchto vrstev má být extrahována a dekódována, aby vznikla konkrétní výstupní stopa s požadovanými charakteristikami.

Z architektonického hlediska je koncept OLS řízen v rámci frameworku pro doručování médií, jako je Dynamic Adaptive Streaming over [HTTP](/mobilnisite/slovnik/http/) ([DASH](/mobilnisite/slovnik/dash/)). Server nebo balicí entita generuje manifestní soubor (např. Media Presentation Description nebo [MPD](/mobilnisite/slovnik/mpd/) v DASH), který popisuje dostupné OLS. Každý OLS odpovídá konkrétnímu adaptačnímu setu nebo reprezentaci, charakterizované svou přenosovou rychlostí, rozlišením a úrovní kvality. Logika adaptivní přenosové rychlosti ([ABR](/mobilnisite/slovnik/abr/)) na straně klienta používá tuto informaci k výběru nejvhodnějšího OLS na základě aktuálních síťových podmínek a možností zařízení, a vyžádá si odpovídající segmenty ze serveru.

Klíčové komponenty spojené s OLS zahrnují videoenkodér, který produkuje vrstvený videosignál; mediální server nebo origin, který ukládá a poskytuje segmenty signálu; a klientský přehrávač, který provádí výběr OLS a dekódování. Role OLS v síti spočívá v umožnění efektivního streamování videa s ohledem na přenosovou kapacitu. Umožňuje, aby jediný zakódovaný videosignál obsloužil více typů zařízení a síťových podmínek bez nutnosti více nezávislých kódování, čímž šetří úložný prostor a zjednodušuje správu obsahu. Dekodér na straně klienta je instruován, aby dekódoval pouze vrstvy specifikované vybraným OLS, a podle toho rekonstruuje video.

## K čemu slouží

Technologie Output Layer Set byla vytvořena, aby řešila výzvy doručování videa vysoké kvality přes mobilní sítě charakterizované kolísající přenosovou kapacitou a různorodými uživatelskými zařízeními. Před škálovatelným kódováním videa a OLS adaptivní streamování typicky vyžadovalo uložení více nezávislých kódování (např. 480p, 720p, 1080p) stejného obsahu. Tento přístup spotřebovával významný úložný prostor a zvyšoval složitost a náklady kódování. Navíc přepínání mezi těmito nezávislými reprezentacemi mohlo být neefektivní a vést k oscilacím kvality.

Motivací pro OLS, zavedené v 3GPP Release 13, bylo využít efektivitu rozšíření pro škálovatelné kódování videa (SVC) standardu [HEVC](/mobilnisite/slovnik/hevc/). SVC umožňuje, aby jediný videosignál obsahoval více vrstev kvality. Koncept OLS poskytuje standardizovaný způsob, jak definovat a signalizovat, která podmnožina těchto vrstev tvoří použitelný stream pro klienta. Tím řeší problém, jak namapovat flexibilní, ale komplexní strukturu vrstveného videosignálu do jednoduššího modelu reprezentace používaného streamovacími protokoly jako je [DASH](/mobilnisite/slovnik/dash/). Umožňuje skutečnou adaptaci přenosové rychlosti na úrovni jednotlivých vrstev namísto přepnutí celého streamu, což vede k plynulejším přechodům kvality a efektivnějšímu využití síťových zdrojů. Jeho vytvoření bylo hnací silou potřeb průmyslu po efektivnějším doručování médií, jelikož video provoz nadále dominuje mobilním sítím.

## Klíčové vlastnosti

- Umožňuje adaptivní streamování z jediného škálovatelného videosignálu
- Definuje konkrétní kombinaci základní a zlepšujících vrstev pro výstup
- Snižuje režii úložiště ve srovnání s ukládáním více nezávislých kódování
- Usnadňuje plynulejší přechody kvality během síťových výkyvů
- Standardizovaná signalizace v mediálních manifestech (např. DASH MPD)
- Podporuje přizpůsobení možnostem zařízení výběrem odpovídajících sad vrstev

## Související pojmy

- [HEVC – High Efficiency Video Coding](/mobilnisite/slovnik/hevc/)
- [DASH – Dynamic Adaptive Streaming over HTTP](/mobilnisite/slovnik/dash/)

## Definující specifikace

- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [OLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ols/)
