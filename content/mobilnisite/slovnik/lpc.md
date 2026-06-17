---
slug: "lpc"
url: "/mobilnisite/slovnik/lpc/"
type: "slovnik"
title: "LPC – Linear Predictive Coding"
date: 2025-01-01
abbr: "LPC"
fullName: "Linear Predictive Coding"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lpc/"
summary: "Řečová kódovací technika používaná v 3GPP hlasových kodecích, jako jsou AMR a EVS. Modeluje lidský hlasový trakt jako lineární filtr buzený signálem, což umožňuje účinnou kompresi řečových signálů pro"
---

LPC je řečová kódovací technika používaná v 3GPP hlasových kodecích, která modeluje hlasový trakt jako lineární filtr pro účinnou kompresi, což umožňuje vysoko kvalitní přenos hlasu s minimální šířkou pásma.

## Popis

Lineární prediktivní kódování (LPC) je základní technika kódování a komprese řeči používaná ve standardech 3GPP hlasových kodeků, především v kodecích Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a Enhanced Voice Services ([EVS](/mobilnisite/slovnik/evs/)). Funguje na principu, že řečový vzorek lze aproximovat jako lineární kombinaci jeho předchozích vzorků, čímž efektivně modeluje spektrální obálku lidského hlasového traktu. Základní proces zahrnuje analýzu krátkého segmentu vstupního řečového signálu za účelem výpočtu sady LPC koeficientů, které definují časově proměnný digitální filtr. Tento filtr, známý jako syntézní filtr, je navržen tak, aby jeho frekvenční charakteristika odpovídala formantům (rezonančním frekvencím) původní řeči. Následně je určen buzení signál – reprezentující hlasivkový puls pro znělé zvuky nebo šum pro neznělé zvuky. Enkodér přenáší tyto LPC koeficienty a kvantovanou verzi buzení signálu, čímž dosahuje výrazného snížení datového toku ve srovnání s původním průběhem.

Z architektonického hlediska je LPC integrováno do řečového enkodéru a dekodéru hlasového kodeku. Mezi klíčové komponenty patří modul LPC analýzy, který provádí autokorelační nebo kovarianční metody pro odvození koeficientů, a percepční váhovací filtr, který tvaruje kvantizační šum tak, aby byl méně slyšitelný. Syntézní filtr v dekodéru rekonstruuje řečový průběh pomocí přijatých koeficientů a buzení. V kodecích jako AMR jsou LPC parametry často transformovány do robustnějších reprezentací pro přenos, jako jsou Line Spectral Pairs ([LSP](/mobilnisite/slovnik/lsp/)) nebo Immittance Spectral Frequencies ([ISF](/mobilnisite/slovnik/isf/)), které jsou méně citlivé na kvantizační chyby a zajišťují lepší interpolaci mezi rámci.

Role LPC v síti je klíčová pro zpracování hlasového provozu na fyzické vrstvě. Přímo ovlivňuje efektivitu rozhraní vzduchem tím, že určuje přenosovou rychlost přidělenou hlasovým kanálům. V GSM a UMTS umožňují kodeky AMR využívající LPC dynamickou adaptaci přenosové rychlosti řeči na základě stavu kanálu, což v případě potřeby umožňuje kompromis mezi kvalitou řeči a zvýšenou ochranou proti chybám. V LTE a 5G NR používá kodek EVS pokročilé techniky založené na LPC, jako je rozšíření šířky pásma (Bandwidth Extension, [BWE](/mobilnisite/slovnik/bwe/)) a kompenzace časového aliasingu (Time-Domain Aliasing Cancellation, TDAC), pro podporu superširokopásmového a plnopásmového audia, což poskytuje vynikající kvalitu hlasu při zachování zpětné kompatibility. Účinnost LPC je tedy základním kamenem kvality hlasových služeb a kapacity sítě napříč všemi generacemi systémů 3GPP.

## K čemu slouží

LPC bylo vyvinuto k řešení zásadní výzvy přenosu srozumitelné, přirozeně znějící lidské řeči přes šířkově omezené a na chyby náchylné digitální rádiové kanály v mobilních sítích. Před jeho přijetím v digitálních celulárních standardech, jako je GSM, vyžadovaly řečové kódovací techniky používané v pevných sítích, například pulzně kódová modulace (PCM), vysoké přenosové rychlosti (64 kbps), které byly pro vzácný bezdrátový spektrální prostor nepraktické. Kodeky založené na LPC, jako byl plnorychlostní kodek v raném GSM, si kladly za cíl komprimovat řeč na přibližně 13 kbps nebo méně při zachování přijatelné kvality, což umožnilo efektivní využití rádiových zdrojů a učinilo digitální celulární hlasové služby komerčně životaschopnými.

Motivace pro LPC vychází z jeho schopnosti poskytnout vysoký kompresní poměr využitím předvídatelné povahy tvorby řeči, namísto pouhého digitalizování průběhu. Řeší problém udržení kapacity a pokrytí hlasových služeb bez nutnosti nadměrné šířky pásma. Oddělením pomalu se měnícího filtru hlasového traktu (LPC koeficienty) od rychle se měnícího buzení signálu může kodek efektivně stanovit priority bitů a přidělit více bitů percepčně kritické spektrální obálce. Tento přístup také usnadňuje robustní maskování chyb; pokud jsou některé parametry během přenosu poškozeny, dekodér může použít předchozí nepoškozené rámce k zamaskování chyb, čímž zabrání úplnému výpadku hlasu.

Historicky se LPC vyvinulo z vládního a akademického výzkumu nízkorychlostního kódování řeči pro zabezpečenou komunikaci a satelitní spoje. Jeho integrace do standardů 3GPP, počínaje GSM, vytvořila škálovatelný rámec pro kompresi hlasu, který byl v průběhu desetiletí vylepšován. Každá nová generace kodeků ([AMR](/mobilnisite/slovnik/amr/), [AMR-WB](/mobilnisite/slovnik/amr-wb/), [EVS](/mobilnisite/slovnik/evs/)) zdokonalila LPC techniky, aby poskytovala vyšší kvalitu při stejné nebo nižší přenosové rychlosti, čímž podpořila vývoj od úzkopásmové telefonie po vysokokvalitní hlas a multimediální služby v 5G.

## Klíčové vlastnosti

- Modeluje lidský hlasový trakt jako časově proměnný lineární filtr definovaný LPC koeficienty.
- Odděluje řečový signál na parametry filtru a buzení signál pro účinnou kompresi.
- Umožňuje provoz s proměnnou přenosovou rychlostí v kodecích jako AMR pro adaptaci na podmínky kanálu.
- Používá robustní reprezentace parametrů, jako jsou Line Spectral Pairs (LSP), pro kvantizaci a přenos.
- Tvoří jádro spektrálního modelovacího komponentu v 3GPP kodecích včetně AMR, AMR-WB a EVS.
- Podporuje techniky rozšíření šířky pásma pro vylepšení audio šířky pásma nad kódované základní pásmo.

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [EVS – Enhanced Voice Services (specifically, the AMR-WB IO mode: AMR-WB Interoperable)](/mobilnisite/slovnik/evs/)

## Definující specifikace

- **TS 26.090** (Rel-19) — AMR Speech Codec Detailed Mapping Specification
- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification
- **TS 46.021** (Rel-19) — GSM Half Rate DTX Frame Substitution & Muting
- **TS 46.060** (Rel-19) — GSM Enhanced Full Rate Speech Codec

---

📖 **Anglický originál a plná specifikace:** [LPC na 3GPP Explorer](https://3gpp-explorer.com/glossary/lpc/)
