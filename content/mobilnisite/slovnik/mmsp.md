---
slug: "mmsp"
url: "/mobilnisite/slovnik/mmsp/"
type: "slovnik"
title: "MMSP – Multimodal Synchronization Protocol"
date: 2025-01-01
abbr: "MMSP"
fullName: "Multimodal Synchronization Protocol"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mmsp/"
summary: "MMSP je protokol definovaný 3GPP pro synchronizaci více mediálních komponent (jako je audio, video a text) v multimediální prezentaci nebo službě. Zajišťuje, že různé mediální toky jsou uživateli prez"
---

MMSP je 3GPP protokol pro synchronizaci více mediálních komponent, jako je audio a video, aby bylo zajištěno, že jsou prezentovány koordinovaným, časově sladěným způsobem pro soudržný uživatelský zážitek.

## Popis

Protokol pro multimodální synchronizaci (MMSP) je klíčový protokol v rámci architektury 3GPP služby Multimedia Broadcast/Multicast Service ([MBMS](/mobilnisite/slovnik/mbms/)), konkrétně navržený pro zvládnutí časového sladění více nezávislých mediálních toků, které tvoří jednu multimediální relaci. Na rozdíl od jediného kontejnerového formátu zachází MMSP s každou mediální komponentou (např. audio stopou, video stopou, časovaným textovým proudem nebo sekvencí obrázků) jako se samostatnou entitou, která je doručována, často prostřednictvím vysílání (broadcast) nebo skupinového vysílání (multicast), a musí být na přijímači přesně synchronizována. Protokol pracuje na aplikační vrstvě a spolupracuje s transportními protokoly nižších vrstev k dosažení synchronizace obrazu a zvuku (lip-sync), synchronizace snímků a dalších časově kritických prezentací.

MMSP funguje pomocí využití synchronizačních značek a časových informací vložených do každého mediálního toku. Ústředním konceptem je použití společné časové osy, často odvozené od referenčního hodinového signálu. Protokol definuje struktury, jako jsou synchronizační kanály a synchronizační položky, které přenášejí tyto časové údaje. MBMS klient na přijímacím zařízení používá MMSP ke shromáždění těchto toků, jejich vhodnému vyrovnávání a následné prezentaci synchronizovaným způsobem na základě přijatých časových instrukcí. Řeší problémy jako síťový jitter a rozdílné zpoždění mezi toky, aby zajistil, že například audio komentář přesně odpovídá změně zobrazeného snímku, bez ohledu na to, jak dorazily jednotlivé datové pakety.

Architektura protokolu je úzce spojena s protokolem pro doručování souborů [FLUTE](/mobilnisite/slovnik/flute/)/[ALC](/mobilnisite/slovnik/alc/) používaným v MBMS pro přenos mediálních souborů nebo fragmentů proudů. MMSP poskytuje potřebná metadata a řídicí informace, které sdělují klientovi, jak tyto doručené soubory asociovat a sladit. Podporuje jak režim streamování, tak režim stahování v rámci MBMS. Mezi klíčové komponenty patří popis synchronizačního zdroje, který identifikuje mediální komponenty a jejich vzájemné vztahy, a časová metadata, která poskytují přesný harmonogram prezentace. Oddělením doručování mediálních objektů od logiky jejich synchronizované prezentace umožňuje MMSP efektivní vysílání bohatého, časově citlivého multimediálního obsahu velkému publiku, což je základním kamenem služeb jako je mobilní TV a systémy veřejného varování s multimediálními výstrahami.

## K čemu slouží

MMSP byl vytvořen k řešení základní výzvy ve službách vysílaného (broadcast)/skupinového (multicast) multimediálního obsahu: doručení souvislého zážitku z více, samostatně kódovaných a přenášených mediálních elementů. Rané streamovací služby často kombinovaly média do jediného toku (jako je [MPEG](/mobilnisite/slovnik/mpeg/) transportní tok), což bylo efektivní, ale nepružné. Pro [MBMS](/mobilnisite/slovnik/mbms/) potřebovalo 3GPP metodu, která by umožnila různé mediální komponenty (např. video tok vysoké kvality, samostatnou audio stopu v několika jazycích a doprovodné obrázkové snímky) efektivně vysílat a na přijímači je flexibilně kombinovat na základě uživatelského výběru nebo možností zařízení.

Protokol řeší problém synchronizace v prostředí, kde toky mohou využívat různé síťové cesty nebo zažívat různá zpoždění. Bez MMSP by audio stopa a sekvence obrázků mohly dorazit správně, ale přehrát se nesynchronně, čímž by byla prezentace zničena. Jeho vývoj byl motivován snahou umožnit sofistikované MBMS aplikace, jako jsou komentované zpravodajské klipy, sportovní highlights se synchronizovanými statistikami a interaktivní vzdělávací obsah. MMSP poskytuje potřebné 'lepidlo' na aplikační vrstvě, což síťovým operátorům a poskytovatelům obsahu umožňuje vytvářet bohaté, televizi podobné zážitky přes celulární vysílací sítě a optimalizovat využití přenosové kapacity tím, že například uživatelé mohou odebírat pouze audio stopu v jazyce, který potřebují, zatímco všichni uživatelé přijímají společný video tok.

## Klíčové vlastnosti

- Poskytuje časovou synchronizaci pro více nezávislých mediálních toků v MBMS
- Využívá společnou časovou osu a synchronizační značky napříč toky
- Spolupracuje s protokolem FLUTE/ALC pro efektivní doručování souborů přes vysílání (broadcast)
- Podporuje jak režim streamování, tak režim stahování v rámci MBMS
- Umožňuje synchronizaci obrazu a zvuku (lip-sync), synchronizaci snímků s audiem a další časované prezentace
- Umožňuje flexibilní kombinaci mediálních komponent (např. výběr jazyka audio stopy) na přijímači

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)
- [FLUTE – File Delivery over Unidirectional Transport](/mobilnisite/slovnik/flute/)

## Definující specifikace

- **TR 22.977** (Rel-19) — Speech Enabled Services and Multimodal Framework

---

📖 **Anglický originál a plná specifikace:** [MMSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmsp/)
