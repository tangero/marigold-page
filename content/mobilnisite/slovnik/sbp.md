---
slug: "sbp"
url: "/mobilnisite/slovnik/sbp/"
type: "slovnik"
title: "SBP – Special Burst Period"
date: 2025-01-01
abbr: "SBP"
fullName: "Special Burst Period"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sbp/"
summary: "Definované časové období v režimu UMTS TDD, během kterého jsou vysílány speciální bursty pro účely synchronizace a měření. Je klíčové pro počáteční vyhledání buňky, převýběr buňky a procedury předání"
---

SBP je definované časové období v režimu UMTS TDD, během kterého jsou vysílány speciální bursty pro synchronizaci sítí a měření, což je klíčové pro procedury vyhledání buňky, jejího převýběru a předání hovoru.

## Popis

Období speciálních burstů (SBP) je základním konceptem v režimu s časovým duplexem ([TDD](/mobilnisite/slovnik/tdd/)) rozhraní Universal Mobile Telecommunications System (UMTS), jak je standardizováno v 3GPP TS 25.224. Odkazuje na specifický, opakující se časový interval ve struktuře rádiového rámce vyhrazený pro vysílání 'speciálních burstů'. Tyto bursty se nepoužívají pro přenos uživatelských dat nebo běžné řídicí signalizace, ale plní kritické funkce fyzické vrstvy nezbytné pro synchronizaci sítě a správu rádiových zdrojů. SBP je architektonicky integrováno do struktury rámce a časových slotů TDD a poskytuje předvídatelná okna, během kterých uživatelské zařízení (UE) může očekávat tyto speciální signály.

Provozně během SBP síť vysílá předdefinované speciální bursty. Nejběžnějším typem je DwPTS (Downlink Pilot Time Slot) ve variantě [TD-SCDMA](/mobilnisite/slovnik/td-scdma/) UMTS TDD, ale koncept platí obecně. Tyto bursty obsahují specifické tréninkové sekvence nebo midambly, které UE používají pro klíčové procedury. Primární technickou funkcí je umožnit přesnou časovou synchronizaci. UE provádějící počáteční vyhledání buňky skenuje tyto speciální bursty, aby identifikovalo buňky, určilo jejich časování a odhadlo impulzní odezvu kanálu. Předvídatelná periodicita SBP umožňuje UE efektivně provádět tyto úkoly bez nepřetržitého, energeticky náročného skenování celého rámce.

Role SBP přesahuje rámec počátečního přístupu. Je nedílnou součástí průběžného řízení mobility. Pro převýběr buňky a předání hovoru UE měří kvalitu signálu a časování sousedních buněk. SBP poskytuje garantovanou příležitost pro taková měření s kontrolovaným rušením. Protože všechny buňky vysílají své speciální bursty během tohoto vyhrazeného období, může UE rychle naladit na různé frekvence nebo identifikátory buněk a zachytit potřebné měřicí vzorky. Tento strukturovaný přístup zvyšuje přesnost a rychlost měření ve srovnání s náhodným vzorkováním. Dále návrh SBP pomáhá řídit rušení v TDD sítích tím, že soustřeďuje určité přenosy mimo provoz do omezeného časového okna, což zjednodušuje plánování a optimalizaci sítě.

## K čemu slouží

Období speciálních burstů (SBP) bylo vytvořeno k řešení jedinečných výzev synchronizace a měření buněk, které jsou vlastní buňkovým systémům s časovým duplexem ([TDD](/mobilnisite/slovnik/tdd/)). V TDD sdílejí vysílání v uplinku a downlinku stejné frekvenční pásmo, ale jsou odděleny v čase. Na rozdíl od systémů s kmitočtovým duplexem ([FDD](/mobilnisite/slovnik/fdd/)), které mají nepřetržité pilotní kanály, potřebují TDD systémy metodu, aby UE mohla rychle získat a synchronizovat se s nespojitým přenosovým vzorem sítě. SBP toto poskytuje tím, že nabízí vyhrazený, předvídatelný časový slot pro synchronizační signály.

Historicky, bez strukturovaného období jako je SBP, by UE musela provádět slepé prohledávání celé struktury rámce, aby našla buňkově specifické signály, což by vedlo k prodloužené době počátečního přístupu, zvýšené spotřebě energie UE a potenciálně méně přesným měřením. SBP tyto problémy řeší standardizací časování. Zajišťuje, že každá buňka vysílá svůj klíčový synchronizační burst na známé relativní pozici v rámci rámce. Tento návrh dramaticky snižuje dobu potřebnou k synchronizaci, což je klíčové pro uživatelský zážitek při zapnutí a pro efektivní mobilitu. Vytvoření SBP bylo klíčovým prvkem umožňujícím praktické nasazení a výkon UMTS TDD a jeho evoluce, včetně [TD-SCDMA](/mobilnisite/slovnik/td-scdma/), a poskytlo robustní základ pro procedury vyhledání buňky a měření, které jsou stejně spolehlivé jako ty ve FDD systémech.

## Klíčové vlastnosti

- Poskytuje vyhrazené časové intervaly pro vysílání synchronizačních burstů v TDD rámcích
- Umožňuje rychlé a efektivní počáteční vyhledání buňky a získání časování pro UE
- Usnadňuje přesná měření kvality signálu pro převýběr buňky a předání hovoru
- Standardizuje příležitosti pro měření napříč všemi buňkami v síti
- Pomáhá řídit a omezovat rušení od signálů mimo provoz
- Integruje se se specifickou strukturou časových slotů režimů UMTS TDD

## Související pojmy

- [TDD – Time Division Duplex(ing)](/mobilnisite/slovnik/tdd/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)

## Definující specifikace

- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [SBP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbp/)
