---
slug: "hpbw"
url: "/mobilnisite/slovnik/hpbw/"
type: "slovnik"
title: "HPBW – Half-Power Bandwidth"
date: 2025-01-01
abbr: "HPBW"
fullName: "Half-Power Bandwidth"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hpbw/"
summary: "Half-Power Bandwidth (HPBW) je základní metrika antén a beamformingu definovaná jako úhlová šířka, ve které výkon vyzařovacího diagramu poklesne na polovinu (-3 dB) své maximální hodnoty. V 3GPP je kl"
---

HPBW je úhlová šířka, ve které výkon vyzařovacího diagramu antény poklesne na polovinu (-3 dB) své maximální hodnoty; používá se v 3GPP pro charakterizaci tvarů paprsků v souvislosti s pokrytím a interferencí.

## Popis

Half-Power Bandwidth (HPBW), známá také jako šířka paprsku 3 dB, je klíčový parametr v teorii antén a vysokofrekvenční technice, který kvantifikuje úhlovou šířku hlavního vyzařovacího laloku antény. Konkrétně se jedná o úhlovou vzdálenost mezi dvěma body na vyzařovacím diagramu, kde je vysílaný nebo přijímaný výkon přesně poloviční (nebo -3 decibely) oproti špičkovému výkonu ve směru hlavního maxima paprsku. V kontextu 3GPP, zejména od Release 15 pro New Radio (NR), se HPBW hojně používá k definování a standardizaci charakteristik anténních polí a beamformovaných signálů, především pro frekvence nad 6 GHz (mmWave pásma).

Technicky se HPBW odvozuje z vyzařovacího diagramu antény, což je grafické znázornění relativní intenzity pole nebo výkonové hustoty v závislosti na směru. Pro danou anténu nebo beamformovaný přenos inženýři změří diagram a identifikují body -3 dB na obou stranách vrcholu hlavního laloku. Úhlová vzdálenost mezi těmito dvěma body, obvykle měřená ve stupních, je HPBW. Lze ji specifikovat pro různé roviny – nejčastěji pro horizontální rovinu (azimutový HPBW) a vertikální rovinu (elevační HPBW). V systémech massive [MIMO](/mobilnisite/slovnik/mimo/) a beamformingu využívají základnové stanice (gNB) digitální precoding k vytváření úzkých paprsků s vysokým ziskem směrovaných k uživatelskému zařízení; HPBW těchto paprsků přímo ovlivňuje plochu pokrytí a prostorovou selektivitu.

V rámci specifikací 3GPP, jako je TS 38.762 (NR; Base Station radio transmission and reception), se HPBW používá k definování požadavků na antény základnových stanic a charakteristik paprsků. Ovlivňuje několik aspektů systému: užší paprsky (menší HPBW) poskytují vyšší anténní zisk a lepší poměr signálu k šumu, ale vyžadují přesnější zarovnání a sledování paprsku. Širší paprsky (větší HPBW) nabízejí širší pokrytí a jsou odolnější vůči pohybu uživatele, ale mají nižší zisk. Standard NR definuje různé beamformingové scénáře se specifickými předpoklady HPBW pro testování shody a hodnocení výkonu. Dále je v integrovaném přístupu a backhaulu (IAB) a dalších pokročilých nasazeních HPBW kritickým parametrem pro výpočet útlumu na trase a koordinaci interferencí mezi sousedními buňkami nebo paprsky.

## K čemu slouží

Formalizace a důraz na Half-Power Bandwidth ve specifikacích 3GPP se staly obzvláště důležité se zavedením 5G New Radio (NR) a jeho využitím vyšších kmitočtových pásem počínaje Release 15. Na milimetrových vlnách (např. 24,25–52,6 GHz) dochází k vyššímu útlumu na trase a rádiové vlny jsou náchylnější k překážkám. Aby se tomu předešlo, NR využívá massive [MIMO](/mobilnisite/slovnik/mimo/) s beamformingem k vytváření směrových paprsků s vysokým ziskem, které koncentrují energii směrem k uživatelům. Přesná charakterizace těchto paprsků je zásadní pro návrh systému, predikci výkonu a interoperabilitu.

Před NR fungovaly mobilní systémy převážně na nižších frekvencích (pod 6 GHz) s anténami širších paprsků nebo jednodušší sektorizací. Charakteristiky paprsků byly pro standardizaci méně kritické. Přechod na mmWave si vyžádal přesné metriky pro definici tvaru, šířky a zisku paprsku. HPBW slouží jako základní, jednoznačná metrika pro tento účel. Umožňuje výrobcům zařízení, operátorům sítí a standardizačním orgánům používat společný jazyk pro specifikaci požadavků na šířku paprsku, což umožňuje konzistentní výkon různých hardwarových implementací. Také přímo ovlivňuje klíčové síťové funkce, jako je počáteční prohledávání paprsků, sledování paprsku, předávání hovoru a plánování více paprsků. Standardizací parametrů, jako je HPBW, zajišťuje 3GPP, že beamformingové systémy od různých výrobců mohou koexistovat a předvídatelně fungovat v reálných nasazeních, což je klíčové pro dosažení vysokých přenosových rychlostí a kapacity slibovaných 5G.

## Klíčové vlastnosti

- Definována jako úhlová šířka mezi body -3 dB vyzařovacího diagramu
- Klíčová pro charakterizaci výkonu antén a beamformingu v NR
- Specifikována samostatně pro azimutovou (horizontální) a elevační (vertikální) rovinu
- Používána v 3GPP testování shody pro požadavky na rádiovou část základnových stanic
- Ovlivňuje zisk beamformingu, plochu pokrytí a správu interferencí
- Základní parametr pro návrh mmWave a massive MIMO systémů

## Definující specifikace

- **TS 36.777** (Rel-15) — Enhanced Support for Aerial Vehicles
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.762** (Rel-19) — Dynamic MIMO OTA Test Methodology for NR FR1

---

📖 **Anglický originál a plná specifikace:** [HPBW na 3GPP Explorer](https://3gpp-explorer.com/glossary/hpbw/)
