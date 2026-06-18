---
slug: "tch-hs-2"
url: "/mobilnisite/slovnik/tch-hs-2/"
type: "slovnik"
title: "TCH/HS – Traffic Channel Half Rate Speech"
date: 2025-01-01
abbr: "TCH/HS"
fullName: "Traffic Channel Half Rate Speech"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tch-hs-2/"
summary: "GSM kanál pro přenos hovorů, který je specificky nakonfigurován pro použití řečového kodeku s poloviční rychlostí. Optimalizuje kapacitu sítě přenosem komprimované řeči, což umožňuje sdílet jeden rádi"
---

TCH/HS je GSM kanál pro přenos hovorů, který využívá poloviční rychlostní řečový kodek k optimalizaci kapacity sítě tím, že umožňuje sdílení jednoho rádiového časového slotu dvěma hlasovými hovory.

## Popis

Traffic Channel Half Rate Speech ([TCH](/mobilnisite/slovnik/tch/)/HS) je konkrétní instance kanálu s poloviční rychlostí v GSM, explicitně určená pro přenos hlasového provozu s využitím řečového kodeku s poloviční rychlostí. Funguje v rámci struktury [TDMA](/mobilnisite/slovnik/tdma/) rámců GSM, kde je jeden rádiový kmitočtový nosič rozdělen na osm časových slotů. TCH/HS zabírá ekvivalent poloviny kapacity časového slotu na rámec, typicky přiřazením kanálu uživateli v střídavých rámcích nebo využitím subkanálu uvnitř časového slotu. To síti umožňuje multiplexovat dva nezávislé hlasové rozhovory na jeden fyzický časový slot, čímž se efektivně zdvojnásobí potenciální počet současných hovorů v buňce ve srovnání s použitím pouze kanálů s plnou rychlostí ([TCH/FS](/mobilnisite/slovnik/tch-fs-2/)).

Technicky, když je TCH/HS přidělen, mobilní stanice a základnová přijímací a vysílací stanice ([BTS](/mobilnisite/slovnik/bts/)) pracují v určitém režimu provozu. Hlasový signál od uživatele je kódován řečovým kodekem s poloviční rychlostí, jako je například kodek GSM Half-Rate ([HR](/mobilnisite/slovnik/hr/)) definovaný v dřívějších vydáních nebo adaptivní více rychlostní kodek ([AMR](/mobilnisite/slovnik/amr/)) pracující v režimu poloviční rychlosti (např. AMR 5,90 kbps). Zakódované řečové rámce jsou následně kanálově kódovány, prokládány a mapovány na určený fyzický zdroj s poloviční rychlostí. Související řídicí signalizace, nezbytná pro udržení hovoru (jako řízení výkonu, časový předstih a hlášení měření), je přenášena na pomalém přidruženém řídicím kanálu s poloviční rychlostí ([SACCH](/mobilnisite/slovnik/sacch/)/HS), který je spárován s TCH/HS. Tento SACCH/HS využívá sníženou signalizační rychlost, což odpovídá efektivitě využití zdrojů samotného kanálu pro přenos hovorů.

V architektuře sítě rozhoduje o přidělení TCH/HS řadič základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) na základě algoritmů, které berou v úvahu faktory jako celkové zatížení buňky, dostupné kanály a schopnosti mobilní stanice (ne všechny starší telefony podporovaly poloviční rychlost). BSC dá pokyn BTS a mobilní stanici, aby linku odpovídajícím způsobem nakonfigurovaly. Role TCH/HS je nedílnou součástí správy provozu a optimalizace kapacity v sítích GSM. Umožňuje operátorům obsloužit více účastníků, zejména v hustě obydlených městských oblastech, kde je spektrum omezené. Zatímco původní kodek s poloviční rychlostí nabízel nižší kvalitu hlasu, zavedení vylepšených kodeků, jako je AMR, které mohou dynamicky přepínat mezi plnou a poloviční rychlostí na základě rádiových podmínek, umožnilo agresivnější využití TCH/HS bez výrazného zhoršení kvality, čímž se dosáhlo optimální rovnováhy mezi kapacitou a kvalitou služby.

## K čemu slouží

TCH/HS byl vyvinut, aby poskytl konkrétní, na řeč optimalizovanou implementaci konceptu kanálu s poloviční rychlostí v rámci GSM. Základní problém, který řešil, byl totožný s problémem TCH/H: nedostatek spektra a potřeba vyšší hlasové kapacity. TCH/HS se však specificky zaměřuje na použití pro hlasové služby, na rozdíl od datových služeb (které by pro jiné účely, jako je datový přenos s přepojováním okruhů s poloviční rychlostí, využívaly TCH/H). Jeho vytvoření bylo motivováno potřebou standardizovat přesně to, jak bude kanál s poloviční rychlostí pro hlas využíván, včetně specifických mapování kodeků a souvisejících řídicích procedur.

Omezením předchozích přístupů bylo, že sítě buď výhradně používaly kanály s plnou rychlostí, což omezovalo kapacitu, nebo používaly nestandardizované metody pro zvýšení kapacity. TCH/HS poskytl standardizovaný, interoperabilní způsob nasazení hlasu s poloviční rychlostí napříč zařízeními různých výrobců a mobilními terminály. To bylo klíčové pro rozsáhlá nasazení sítí a pro zajištění, aby účastníci mohli služby s poloviční rychlostí bezproblémově využívat při pohybu mezi buňkami a sítěmi. Řešil problém neefektivního využití spektra pro hlas, který tvořil naprostou většinu raného mobilního provozu.

Dále TCH/HS položil základy pro inteligentnější adaptivní řízení rychlosti. Existence definovaného typu kanálu pro řeč s poloviční rychlostí umožnila síti implementovat algoritmy, které mohly během přetížení převést hovor z TCH/FS na TCH/HS, nebo jej upgradovat, když se kapacita uvolnila, a to vše transparentně pro uživatele. Toto dynamické přidělování kanálů, umožněné specifikacemi jako 45.914 (více rychlostní řečový kodek), byl významný krok k sofistikovanosti správy kvality služeb a zdrojů, jakou známe v pozdějších systémech 3G a 4G.

## Klíčové vlastnosti

- Určen pro přenos hlasového provozu s využitím standardizovaných řečových kodeků s poloviční rychlostí (např. GSM-HR, režimy AMR s poloviční rychlostí).
- Zdvojnásobuje hlasovou kapacitu multiplexováním dvou hovorů na jeden GSM TDMA časový slot.
- Funguje ve spojení s pomalým přidruženým řídicím kanálem s poloviční rychlostí (SACCH/HS) pro nezbytnou signalizaci během hovoru.
- Dynamicky přidělitelný síťovými algoritmy na základě zatížení, čímž zlepšuje využití zdrojů.
- Umožňuje kompromis mezi kapacitou sítě a kvalitou řeči, řízený adaptací kodeku.
- Široce podporován napříč vydáními GSM a základní funkce pro správu kapacity GERAN.

## Související pojmy

- [TCH-FS – Traffic Channel Full rate Speech](/mobilnisite/slovnik/tch-fs/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity

---

📖 **Anglický originál a plná specifikace:** [TCH/HS na 3GPP Explorer](https://3gpp-explorer.com/glossary/tch-hs-2/)
