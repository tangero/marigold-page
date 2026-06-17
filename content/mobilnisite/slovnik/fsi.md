---
slug: "fsi"
url: "/mobilnisite/slovnik/fsi/"
type: "slovnik"
title: "FSI – Frame Start Identifier"
date: 2025-01-01
abbr: "FSI"
fullName: "Frame Start Identifier"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fsi/"
summary: "FSI (Frame Start Identifier) je identifikátor začátku rámce, synchronizační signál sloužící k identifikaci začátku přenosového rámce. Zavedený v 3GPP Release 8, je základním prvkem fyzické vrstvy pro"
---

FSI (Frame Start Identifier) je identifikátor začátku rámce, synchronizační signál zavedený ve specifikaci 3GPP Release 8, který označuje začátek přenosového rámce pro zarovnání a časování v systémech GSM/GERAN.

## Popis

Identifikátor začátku rámce (Frame Start Identifier, FSI) je základní synchronizační signál definovaný v technických specifikacích 3GPP, primárně v doméně GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network ([GERAN](/mobilnisite/slovnik/geran/)). Zavedený v Release 8 a detailně popsaný ve specifikaci TS 48.020, se FSI používá k jednoznačnému označení začátku přenosového rámce na fyzické vrstvě. Je to kritická komponenta pro zarovnání rámců, která umožňuje jak síťové infrastruktuře (základnové stanici - [BTS](/mobilnisite/slovnik/bts/)), tak uživatelskému zařízení (UE) navázat a udržovat přesnou časovou synchronizaci pro digitální rádiové rozhraní.

Z architektonického hlediska je FSI generován a vkládán do vysílaného signálového proudu podle struktury rámce definované pro konkrétní typ kanálu, například provozní kanály (TCH) nebo řídicí kanály. V kontextu GSM je fyzická vrstva organizována do mnohorámců, superrámců a hyperrámců, přičemž každý rámec je základní časovou jednotkou. FSI poskytuje referenční bod, který identifikuje začátek rámce v této hierarchii. Funguje tak, že představuje odlišný, detekovatelný vzor nebo sekvenci v přenášeném bitovém proudu. Přijímač využívá korelační techniky k vyhledání tohoto známého FSI vzoru. Po jeho detekci může přijímač zarovnat svůj vnitřní čítač rámců, což umožňuje správnou demodulaci a dekódování následujících bitů, které jsou strukturovány do burstů, časových slotů a rámců.

Mezi klíčové komponenty související s FSI patří obvod pro tvorbu rámce v vysílači, který identifikátor vkládá, a synchronizační jednotka v přijímači, která provádí porovnávání vzorů. Návrh FSI zajišťuje, že má dobré autokorelační vlastnosti, aby byl odlišitelný od náhodných dat a odolný vůči zhoršení kvality kanálu, jako je šum a útlum. Jeho úloha v síti je fundamentální: bez přesné identifikace začátku rámce by vyšší vrstvové funkce, jako je dekódování kanálu, přiřazování časových slotů a procedury předávání hovoru, selhaly. Je to první krok v řetězci zpracování na fyzické vrstvě, který umožňuje všechny následné operace obnovy dat a řízení. Zatímco jeho specifikace je soustředěna v TS 48.020, jeho princip je základem časové synchronizace napříč všemi buňkovými systémy, přestože se mechanismy vyvíjely v UMTS a LTE s různými primárními a sekundárními synchronizačními signály.

## K čemu slouží

Identifikátor začátku rámce byl standardizován, aby vyřešil základní problém časové synchronizace v digitálních buňkových systémech založených na TDMA, jako je GSM. Před a během raných specifikací GSM bylo pro provoz systému kritické definovat robustní metodu, která přijímači umožní přesně určit, kde ve spojitém proudu rádiových vln rámec začíná. Motivací pro jeho vytvoření bylo zajistit spolehlivou komunikaci poskytnutím jasného, standardizovaného referenčního bodu, který všechna kompatibilní zařízení mohou použít pro zarovnání svého zpracování.

Historicky měly analogové systémy jiné synchronizační potřeby. Přechod k digitálnímu TDMA v GSM vyžadoval přesné časování k oddělení časových slotů náležejících různým uživatelům. FSI řeší omezení spočívající v neexistenci inherentní časové reference v samotných přenášených datech. Vložením známého identifikátoru na specifickou pozici vůči struktuře rámce umožňuje mobilní stanici rychle získat časování po zapnutí (počáteční synchronizace) a udržovat jej během hovorů (průběžná synchronizace), a to i při pohybu. Tím řeší problémy mezi symbolového rušení a ko-kanálového rušení tím, že zajišťuje respektování přesných hranic časových slotů. Jeho zařazení od Release 8 v příslušném souboru dokumentů poskytlo stabilní, dlouhodobou definici pro tuto základní funkci fyzické vrstvy, zajišťující zpětnou kompatibilitu a spolehlivý provoz sítí [GERAN](/mobilnisite/slovnik/geran/).

## Klíčové vlastnosti

- Poskytuje jednoznačný ukazatel začátku přenosového rámce.
- Umožňuje časovou synchronizaci přijímače a zarovnání rámců.
- Používá odlišný vzor navržený pro spolehlivou detekci v zašuměných kanálech.
- Základní pro správnou demodulaci v systémech s TDMA, jako je GSM.
- Podporuje jak počáteční zachycení časování, tak jeho průběžné sledování.
- Specifikováno ve specifikacích fyzické vrstvy GERAN pro interoperabilitu.

## Související pojmy

- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TS 48.020** (Rel-19) — PLMN Rate Adaptation Functions

---

📖 **Anglický originál a plná specifikace:** [FSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/fsi/)
