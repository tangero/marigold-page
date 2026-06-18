---
slug: "db"
url: "/mobilnisite/slovnik/db/"
type: "slovnik"
title: "DB – Dummy Burst"
date: 2025-01-01
abbr: "DB"
fullName: "Dummy Burst"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/db/"
summary: "Dummy Burst (DB) je specifický typ rádiového burstu vysílaný v sítích GSM a UMTS, když není k dispozici žádná uživatelská data nebo řídicí informace k odeslání v časovém slotu. Udržuje kontinuální pře"
---

DB je rádiový burst vysílaný v sítích GSM a UMTS, který vyplňuje nevyužité časové sloty známým vzorkem, čímž udržuje kontinuální přenos pro synchronizaci sítě a prevenci rušení.

## Popis

Dummy Burst (DB) je základním prvkem fyzické vrstvy v režimech GSM (Global System for Mobile Communications) a UMTS Terrestrial Radio Access ([UTRA](/mobilnisite/slovnik/utra/)) [TDD](/mobilnisite/slovnik/tdd/) (Time Division Duplex), jak je definováno ve specifikacích 3GPP. Jedná se o specifickou strukturu rádiového burstu vysílanou na časovém slotu nosné, když není k přenosu k dispozici žádná data provozního kanálu ([TCH](/mobilnisite/slovnik/tch/)) nebo řídicího kanálu (např. Broadcast Control Channel - [BCCH](/mobilnisite/slovnik/bcch/), Common Control Channel - [CCCH](/mobilnisite/slovnik/ccch/)). Primární funkcí DB je udržovat kontinuální průběh rádiové frekvence ([RF](/mobilnisite/slovnik/rf/)) nosné. V systémech [TDMA](/mobilnisite/slovnik/tdma/), jako je GSM, je každá nosná rozdělena na opakující se rámce časových slotů. Pokud není slot přidělen pro aktivní komunikaci, ponechání zcela prázdného (nepřenášejícího nic) by vytvořilo mezery v RF přenosu. Tyto mezery mohou vést k několika problémům: mohou narušit synchronizaci mobilních stanic sledujících nosnou, způsobit zvýšené rušení v důsledku výkyvů výkonu a zkomplikovat provoz přijímače. DB vyplňuje tyto 'nečinné' časové sloty strukturovaným, známým signálem.

Technicky má Dummy Burst definovaný formát podobný jiným typům burstů v GSM (jako je Normal Burst). Obsahuje specifický bitový vzorek pro svou datovou část. Tento vzorec je navržen tak, aby měl žádoucí RF vlastnosti, jako je konstantní amplituda a dobře definovaný spektrální tvar, což minimalizuje emise mimo pásmo a rušení. Burst obsahuje tréninkovou sekvenci ve své středové části (midamble), což je známý bitový vzorek používaný pro odhad kanálu, který však v případě DB není použit pro demodulaci uživatelských dat, ale pomáhá zachovat integritu struktury burstu. Vysílání DB zajišťuje, že výkonový zesilovač základnové stanice pracuje v kontinuálním lineárním režimu, čímž se vyhne spektrálnímu rozstřiku a přechodovým jevům spojeným s rychlým zapínáním a vypínáním vysílače pro každý prázdný slot.

Z pohledu architektury sítě je generování a plánování Dummy Burstů řízeno základnovou přenosovou stanicí ([BTS](/mobilnisite/slovnik/bts/)) v GSM nebo Node B v UMTS. Jednotka zpracování fyzické vrstvy sestaví burst podle specifikace a vloží jej do TDMA rámce pro jakýkoli časový slot, který není jinak přidělen. Jeho role je čistě infrastrukturní a pro uživatelské zařízení (UE) transparentní. UE neinterpretuje datovou část DB jako smysluplnou informaci; jednoduše zachází s kontinuální nosnou jako se synchronizačním a měřicím referenčním bodem. Důsledná přítomnost RF energie, byť 'dummy', umožňuje mobilům provádět přesná měření síly signálu (RxLev) a udržovat časovou synchronizaci, což je klíčové pro výběr buňky, procedury předávání hovoru (handover) a celkové řízení rádiových prostředků (RRM).

## K čemu slouží

Dummy Burst byl vytvořen, aby řešil základní výzvy vlastní systémům TDMA (Time Division Multiple Access), jako je GSM. V čistém schématu TDMA je vysílač aktivní pouze během svého přiděleného časového slotu. Pokud by více vysílačů (např. pro různé nosné nebo sektory) na jednom místě následovalo tento vzorec nezávisle, výsledné RF prostředí by bylo vysoce nespojité. To by mohlo způsobit několik problémů: mobilní přijímače spoléhající na kontinuální signál pro synchronizaci by mohly ztratit lock, což by vedlo k přerušeným hovorům nebo neúspěšným pokusům o přístup. Navíc rychlé zapínání/vypínání výkonových zesilovačů vytváří širokopásmové emise (přechodové jevy), které mohou rušit sousední kanály a porušovat přísné spektrální masky požadované regulátory.

Před standardizovaným použitím dummy přenosů by jednou z alternativ bylo prostě nevysílat během nečinných slotů. Tento režim 'discontinuous transmission' (DTX), ačkoli se používá pro hlasovou aktivitu na provozních kanálech za účelem úspory energie, je pečlivě řízen a liší se od úplné absence signálu na řídicích časových slotech nosné. DB poskytuje inženýrské řešení, které zajišťuje konstantní a předvídatelnou RF stopu nosné. Tato předvídatelnost zjednodušuje návrh základnových stanic a mobilních přijímačů, zlepšuje stabilitu sítě a zvyšuje koexistenci zařízení více operátorů minimalizací nepředvídatelných interferenčních vzorců. Jeho zavedení bylo klíčovým faktorem pro robustní mobilní sítě s vysokou kapacitou, pro které se GSM stalo známým.

## Klíčové vlastnosti

- Udržuje kontinuální přenos RF nosné během nečinných TDMA časových slotů.
- Používá předdefinovaný, spektrálně efektivní bitový vzorek pro minimalizaci rušení.
- Obsahuje tréninkovou sekvenci (midamble) odpovídající standardní struktuře burstu.
- Umožňuje stabilní synchronizaci mobilní stanice a měření síly signálu.
- Zabraňuje přechodovým jevům výkonového zesilovače a zajišťuje soulad s RF spektrálními maskami.
- Je transparentní pro uživatelské zařízení (UE) a nevyžaduje specifickou dekódaci ze strany mobilů.

## Související pojmy

- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.707** (Rel-14) — Multi-Carrier Enhancements for UMTS Study

---

📖 **Anglický originál a plná specifikace:** [DB na 3GPP Explorer](https://3gpp-explorer.com/glossary/db/)
