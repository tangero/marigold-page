---
slug: "rntable"
url: "/mobilnisite/slovnik/rntable/"
type: "slovnik"
title: "RNTABLE – Hopping Sequence Table"
date: 2025-01-01
abbr: "RNTABLE"
fullName: "Hopping Sequence Table"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rntable/"
summary: "Předdefinovaná tabulka 128 celých čísel používaná k vytváření posloupností přeskakování kmitočtů v rádiových systémech GSM a UMTS. Poskytuje deterministické pseudonáhodné vzory pro rozprostření interf"
---

RNTABLE je předdefinovaná tabulka 128 celých čísel používaná k vytváření deterministických posloupností přeskakování kmitočtů (frequency hopping sequences) v rádiových systémech GSM a UMTS za účelem rozprostření interference a zvýšení odolnosti spoje.

## Popis

RNTABLE je základní součástí mechanismů přeskakování kmitočtů v sítích 2G GSM a 3G UMTS, konkrétně definovaná ve specifikaci 3GPP 21.905. Jedná se o statickou, standardizovanou tabulku obsahující 128 celočíselných položek, z nichž každá představuje specifický kmitočtový posun nebo index. Tuto tabulku používá základnová stanice ([BTS](/mobilnisite/slovnik/bts/) v GSM, Node B v UMTS) i mobilní stanice k synchronizovanému výpočtu shodných posloupností přeskakování. Primární funkcí je mapování logických kanálových časových slotů na různé fyzické rádiové kmitočty v po sobě jdoucích rámečcích podle předem dohodnutého algoritmu, který využívá parametry jako Mobile Allocation Index Offset ([MAIO](/mobilnisite/slovnik/maio/)) a Hopping Sequence Number ([HSN](/mobilnisite/slovnik/hsn/)) k výběru položek z RNTABLE.

Fungování je založeno na deterministickém pseudonáhodném procesu. Pro každý časový slot, kde se uplatňuje přeskakování kmitočtů, síť a UE vypočítají index na základě aktuálního čísla rámečku a nakonfigurovaného HSN. Tento index odkazuje na konkrétní celočíselnou hodnotu v 128položkové RNTABLE. Získané celé číslo se pak spolu s dalšími parametry, jako je seznam přidělených kmitočtů (Mobile Allocation, [MA](/mobilnisite/slovnik/ma/)), použije k určení přesného absolutního čísla rádiového kmitočtového kanálu ([ARFCN](/mobilnisite/slovnik/arfcn/) v GSM, [UARFCN](/mobilnisite/slovnik/uarfcn/) v UMTS), který má být použit pro daný vysílací nebo přijímací vzruch. Tím je zajištěno, že oba konce spoje přeskakují kmitočty v dokonalé synchronizaci bez nutnosti explicitně komunikovat kmitočet pro každý vzruch.

Z architektonického hlediska je RNTABLE vestavěna do vrstvy správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) protokolového zásobníku. Její hodnoty jsou pevně stanoveny standardem, což zaručuje interoperabilitu mezi zařízeními od různých výrobců. Použití společné tabulky odstraňuje potřebu přenášet celou posloupnost přeskakování vzduchem, čímž se šetří signalizační šířka pásma. Délka 128 položek poskytuje dostatečnou periodu, aby se posloupnost jevila jako náhodná, což snižuje pravděpodobnost trvalé kolize s interferencí na specifických kmitočtech. Rozprostřením přenosů na více kmitočtů umožňuje RNTABLE kmitočtovou diverzitu, která zmírňuje účinky vícecestného útlumu a vzájemné kanálové interference, což vede ke zlepšené kvalitě řeči, snížení chybovosti a zvýšení celkové kapacity systému.

## K čemu slouží

RNTABLE byla vytvořena za účelem standardizace procesu přeskakování kmitočtů v GSM, aby se vyřešily klíčové výzvy v raných celulárních sítích. Bez přeskakování kmitočtů je rádiový spoj pracující na pevném kmitočtu vysoce náchylný k hlubokým útlumům způsobeným vícecestným šířením a přetrvávající interferenci od jiných uživatelů nebo vnějších zdrojů. To vede ke špatné kvalitě hovoru a přerušeným spojům. RNTABLE poskytuje standardizovanou, efektivní metodu pro pseudonáhodný výběr kmitočtů v čase, čímž přeměňuje problém úzkopásmové interference na širší, průměrovanou hladinu šumu.

Její zavedení vyřešilo problém implementace synchronizovaného přeskakování bez nadměrné signalizační režie. Před standardizovaným přeskakováním by ad-hoc řešení vyžadovala složitou koordinaci a významnou šířku pásma řídicího kanálu k signalizaci následujícího kmitočtu pro každý skok. RNTABLE v kombinaci s malou sadou parametrů ([HSN](/mobilnisite/slovnik/hsn/), MAIO) umožňuje síti i mobilní stanici vypočítat celou posloupnost nezávisle. Toto elegantní řešení je výpočetně jednoduché pro koncová zařízení i síť, což byl klíčový aspekt pro baterií napájená mobilní zařízení éry 2G. Pevná tabulka zajišťuje, že všechna kompatibilní zařízení generují ze stejných vstupů shodné posloupnosti, což je zásadní pro provoz sítě a přechody mezi buňkami.

Motivace pokračovala i v UMTS, kde podporovala specifické režimy, jako je volitelné přeskakování kmitočtů pro uplink DPCH (Dedicated Physical Channel). Řešila podobné cíle průměrování interference a kmitočtové diverzity, což bylo zvláště přínosné v CDMA prostředí UMTS pro snížení variance interference uvnitř buňky a mezi buňkami. Poskytnutím deterministického, avšak pseudonáhodného vzoru zůstává RNTABLE základním, stabilním prvkem, který podporuje robustnost fyzické vrstvy starších GSM/EDGE a UMTS rádiových přístupových sítí.

## Klíčové vlastnosti

- Standardizovaná tabulka 128 celočíselných položek pro interoperabilitu
- Umožňuje deterministický, synchronizovaný výpočet přeskakování kmitočtů
- Používá se spolu s Hopping Sequence Number (HSN) a Mobile Allocation Index Offset (MAIO)
- Snižuje signalizační režii tím, že umožňuje nezávislé generování posloupnosti
- Poskytuje kmitočtovou diverzitu pro potírání vícecestného útlumu a interference
- Základní prvek pro přidělování zdrojů na fyzické vrstvě v GSM a UMTS

## Související pojmy

- [HSN – Hopping Sequence Number](/mobilnisite/slovnik/hsn/)
- [MAIO – Mobile Allocation Index Offset](/mobilnisite/slovnik/maio/)
- [ARFCN – Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/arfcn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [RNTABLE na 3GPP Explorer](https://3gpp-explorer.com/glossary/rntable/)
