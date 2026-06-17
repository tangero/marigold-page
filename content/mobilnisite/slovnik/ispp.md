---
slug: "ispp"
url: "/mobilnisite/slovnik/ispp/"
type: "slovnik"
title: "ISPP – Interleaved Single-Pulse Permutation"
date: 2025-01-01
abbr: "ISPP"
fullName: "Interleaved Single-Pulse Permutation"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ispp/"
summary: "ISPP je technika kanálového kódování používaná v GSM a EDGE pro hlasové a datové kanály. Aplikuje specifický permutační vzor pro prokládání zakódovaných bitů, čímž zvyšuje odolnost proti shlukovým chy"
---

ISPP je technika kanálového kódování používaná v GSM a EDGE, která aplikuje permutační vzor pro prokládání bitů, čímž zvyšuje odolnost proti shlukovým chybám a zlepšuje spolehlivost přenosu.

## Popis

Interleaved Single-Pulse Permutation (ISPP, prokládaná permutace jednotlivých impulsů) je sofistikované schéma prokládání definované ve specifikacích 3GPP pro GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)), primárně pro hlasové a datové provozní kanály. Působí na zakódovaný bitový proud na výstupu z kanálových kodérů, jako jsou konvoluční nebo turbo kódy, před modulací. Hlavní funkcí ISPP je přeuspořádat pořadí těchto bitů podle deterministického permutačního vzoru. Tento proces, známý jako prokládání, je klíčový pro potlačení účinků shlukových chyb, které jsou běžné v mobilních rádiových prostředích kvůli útlumu, rušení nebo krátkodobému zastínění signálu. Rozptýlením po sobě jdoucích bitů z původní sekvence v přenášeném signálu na delší časový úsek dojde k tomu, že jediný shluk rušení poškodí v původním proudu bity, které nejsou sousední. Tím se lokalizovaná shluková chyba na přijímací straně přemění na více izolovaných jednobitových chyb, které je pro kanálový dekodér mnohem snazší opravit, což výrazně zlepšuje výkonnost z hlediska bitové chybovosti ([BER](/mobilnisite/slovnik/ber/)) a celkovou spolehlivost spoje.

Architektura ISPP je integrována do řetězce zpracování fyzické vrstvy GSM/EDGE transceiveru. Mezi klíčové komponenty patří matice prokladače definovaná permutačním algoritmem, která určuje mapování mezi pozicemi vstupních a výstupních bitů. Proces je úzce spjat s konkrétním typem kanálu (např. Traffic Channel - TCH, nebo Packet Data Traffic Channel - PDTCH) a s ním spojenou velikostí bloku a přenosovým časovým intervalem. Hloubka prokládání, neboli rozsah, přes který jsou bity rozprostřeny, je klíčový parametr určený ISPP vzorem. Větší hloubka poskytuje silnější ochranu proti delším shlukům chyb, ale zavádí větší zpoždění. Schéma funguje ve spojení s dalšími postupy fyzické vrstvy, jako je šifrování, modulace (např. [GMSK](/mobilnisite/slovnik/gmsk/), [8-PSK](/mobilnisite/slovnik/8-psk/) pro EDGE) a přiřazení bitů k rádiovým výbuchům v rámcové struktuře TDMA.

V síti hraje ISPP zásadní roli při zajišťování Quality of Service (QoS) pro hlasové a datové služby přes GERAN. Jeho efektivní implementace umožňuje sítím GSM a EDGE udržovat přijatelnou kvalitu hovoru a datový propust i v náročných rádiových podmínkách, aniž by vyžadovala nadměrný vyzařovaný výkon nebo šířku pásma. Standardizované permutační vzory zajišťují interoperabilitu mezi síťovými zařízeními od různých výrobců a uživatelskými terminály. Zatímco pokročilejší systémy jako UMTS a LTE používají jiné techniky prokládání a hybridního [ARQ](/mobilnisite/slovnik/arq/), ISPP zůstává klíčovou součástí starší i modernizované infrastruktury GERAN, podporuje služby pro obrovskou uživatelskou základnu a slouží jako záložní vrstva pro pokrytí v mnoha mobilních sítích.

## K čemu slouží

ISPP bylo vytvořeno, aby řešilo základní výzvu spolehlivé digitální komunikace přes náchylné bezdrátové kanály, konkrétně v rámci systému GSM a jeho evoluce na [EDGE](/mobilnisite/slovnik/edge/). Hlavní problém, který řeší, je zmírnění shlukových chyb, kdy krátkodobá porucha (jako hluboký útlum nebo impulsní šum) poškodí souvislou sekvenci bitů. Bez prokládání by takový shluk přemohl schopnost opravy chyb konvolučních kódů, které jsou navrženy pro opravu náhodných, izolovaných chyb. Permutací pořadí bitů ISPP tyto shluky chyb rozbíjí, čímž se kanál jeví pro dekodér jako kanál s náhodnými chybami, a tím dramaticky zvyšuje účinnost kódování s dopřednou opravou chyb ([FEC](/mobilnisite/slovnik/fec/)).

Historický kontext je zakořeněn v návrhu standardu GSM na konci 80. a v 90. letech 20. století, který potřeboval doručovat hovorovou kvalitu na úrovni veřejné telefonní sítě přes buněčné spoje. Předchozí jednoduchá schémata prokládání nebo absence prokládání byly pro cílové míry chybovosti nedostatečné. ISPP poskytlo strukturovanou, optimalizovanou metodu přizpůsobenou struktuře výbuchů TDMA v GSM a typům kanálů. Řešilo omezení jednodušších blokových prokladačů tím, že nabízelo permutaci maximalizující oddělení sousedních bitů v rámci omezení přenosového formátu, optimalizující kompromis mezi ochranou proti chybám, zpožděním a implementační složitostí. Jeho zavedení a zdokonalování prostřednictvím vydání zajistilo, že se GSM mohlo vyvíjet pro podporu zvýšených přenosových rychlostí (EDGE) při zachování zpětné kompatibility a robustního výkonu.

## Klíčové vlastnosti

- Deterministický permutační algoritmus pro rozptýlení shlukových chyb
- Integrováno se zpracováním provozního kanálu (TCH) a paketového kanálu (PDTCH) GSM/EDGE
- Zvyšuje účinnost konvolučních a turbo kanálových kódů
- Definováno pro specifické velikosti bloků a hloubky prokládání
- Standardizováno ve specifikacích 3GPP pro zajištění interoperability
- Snižuje požadovaný poměr signálu k šumu pro cílovou bitovou chybovost

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)

## Definující specifikace

- **TS 26.090** (Rel-19) — AMR Speech Codec Detailed Mapping Specification
- **TS 26.190** (Rel-19) — AMR-WB Speech Codec Detailed Mapping
- **TS 26.290** (Rel-19) — AMR-WB+ Audio Codec Specification
- **TS 46.060** (Rel-19) — GSM Enhanced Full Rate Speech Codec

---

📖 **Anglický originál a plná specifikace:** [ISPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/ispp/)
