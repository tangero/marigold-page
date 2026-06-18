---
slug: "tch-h"
url: "/mobilnisite/slovnik/tch-h/"
type: "slovnik"
title: "TCH/H – Traffic Channel Half Rate"
date: 2025-01-01
abbr: "TCH/H"
fullName: "Traffic Channel Half Rate"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tch-h/"
summary: "Poloviční provozní kanál v GSM, který umožňuje efektivnější využití rádiových zdrojů přidělením poloviční šířky pásma oproti plnorychlostnímu kanálu. Zdvojnásobuje síťovou kapacitu pro hlasové služby,"
---

TCH/H je poloviční GSM provozní kanál, který přiděluje poloviční šířku pásma oproti plnorychlostnímu kanálu, čímž zdvojnásobuje hlasovou kapacitu sítě a zlepšuje spektrální účinnost, zejména v oblastech s vysokou hustotou.

## Popis

Traffic Channel Half Rate ([TCH](/mobilnisite/slovnik/tch/)/H) je základním typem kanálu v GSM (Global System for Mobile Communications) rádiové přístupové síti, konkrétně ve struktuře kanálů fyzické vrstvy. Funguje tak, že využívá poloviční kapacitu časového slotu oproti plnorychlostnímu provoznímu kanálu ([TCH/F](/mobilnisite/slovnik/tch-f/)). Ve struktuře [TDMA](/mobilnisite/slovnik/tdma/) (Time Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)) rámce GSM je fyzický kanál rozdělen na osm časových slotů na rámec. TCH/F typicky zabírá jeden časový slot na rámec pro jedno uživatelské spojení. Naproti tomu TCH/H je navržen pro přenos komprimovaného hlasového hovoru využitím pouze poloviny této kapacity, což efektivně umožňuje multiplexovat dva odlišné hlasové hovory do jednoho fyzického časového slotu prostřednictvím střídavých rámců nebo mechanismů sdílení dílčích slotů. Toho je dosaženo použitím pokročilých hlasových kodeků, které komprimují zvukový signál, aby se vešel do snížené přenosové rychlosti, jako jsou kodeky Enhanced Full Rate ([EFR](/mobilnisite/slovnik/efr/)) nebo Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) pracující v polovičních režimech.

Architektonicky je TCH/H spravován základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)) a řadičem základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)). Když mobilní stanice (MS) iniciuje nebo přijímá hovor, síť jí může přiřadit TCH/H na základě dostupnosti zdrojů, vytížení provozu a profilu účastníka. Přiřazení je signalizováno přes řídicí kanály, jako je Slow Associated Control Channel (SACCH), který je také přidělen v poloviční konfiguraci spolu s TCH/H pro přenos nezbytných signalizačních informací, jako jsou měřicí reporty a příkazy pro řízení výkonu. Schémata kanálového kódování a prokládání pro TCH/H jsou specificky přizpůsobena k ochraně komprimovaných hlasových bitů přes rádiové rozhraní, vyvažují korekci chyb s omezeným bitovým rozpočtem.

Jeho role v síti je primárně zvýšení kapacity. Tím, že umožňuje dvěma hlasovým hovorům sdílet jeden fyzický zdroj (jeden časový slot), může síť obsloužit dvojnásobný počet současných konverzací na stejné sadě rádiových nosných. To je zvláště důležité v přetížených městských buňkách nebo během špičky. Kompromisem byla historicky potenciální redukce kvality hovoru ve srovnání s plnorychlostním kanálem, protože hlasový kodek pracuje s nižší přenosovou rychlostí. Avšak s pokroky, jako je kodek AMR, který dynamicky přepíná mezi plnorychlostními a polovičními režimy na základě rádiových podmínek, byl tento dopad na kvalitu minimalizován. TCH/H je základním kamenem efektivního využití spektra v GSM a tvoří základ pro pozdější koncepty vícečetných rychlostí a adaptivních kanálů ve 2G a dalších generacích.

## K čemu slouží

TCH/H byl vytvořen, aby řešil kritický problém omezeného rádiového spektra a rostoucí poptávky účastníků v raných sítích GSM. V 90. letech 20. století, s nárůstem adopce mobilních telefonů, čelili síťoví operátoři kapacitním omezením; dostupná frekvenční pásma mohla podporovat pouze konečný počet plnorychlostních hlasových kanálů na buňku. Primární motivací bylo zdvojnásobit hlasovou kapacitu bez nutnosti získání dalších spektrálních licencí nebo nasazení více stanovišť základnových stanic, což je nákladné a logisticky náročné. Toto byla přímá reakce na ekonomickou a technickou potřebu vyšší síťové účinnosti.

Před zavedením polovičních kanálů GSM spoléhalo výhradně na plnorychlostní provozní kanály (TCH/F), které přidělovaly jeden časový slot na uživatele. Tento přístup byl jednoduchý, ale spektrálně neefektivní, zejména pro hlasové hovory, které snesly určitou kompresi. Omezením bylo, že původní hlasový kodek GSM Full-Rate (FR) používal přibližně 13 kbps, což zanechávalo malý prostor pro rozšíření kapacity. TCH/H zavedl nový provozní režim, ve kterém síť mohla dynamicky přepínat kompatibilní mobilní stanice na poloviční kanál, používající kodeky pracující přibližně na 5,6 kbps (jako Half-Rate (HR) kodek), čímž uvolňovala časové sloty pro jiné uživatele. Tím se efektivně proměnila síť s omezenou kapacitou na škálovatelnější.

Vytvoření TCH/H bylo klíčovým evolučním krokem v návrhu celulárních sítí, který stanovil princip adaptivního přidělování zdrojů na základě vytížení provozu. Vyřešil bezprostřední problém zahlcení a snížil náklady na hlasový kanál pro operátory. Dále připravil cestu pro sofistikovanější adaptivní vícečetné kodeky (AMR) v pozdějších vydáních, které mohly plynule přepínat mezi plnorychlostním, polovičním a dokonce i dalšími režimy na základě vyhodnocení kvality kanálu a síťového vytížení v reálném čase, optimalizujících jak kapacitu, tak kvalitu.

## Klíčové vlastnosti

- Využívá poloviční kapacitu časového slotu oproti plnorychlostnímu TCH, což umožňuje dva hlasové hovory na jeden fyzický časový slot.
- Používá komprimované hlasové kodeky (např. GSM Half-Rate, poloviční režimy AMR) k udržení hlasové služby při nižších přenosových rychlostech.
- Dynamicky přiřaditelný sítí na základě vytížení provozu a algoritmů správy zdrojů.
- Zahrnuje přidružený poloviční Slow Associated Control Channel (SACCH) pro signalizaci a měření během hovoru.
- Zvyšuje síťovou kapacitu a spektrální účinnost, což je klíčové pro scénáře s vysokým provozem.
- Podporován širokou škálou GSM mobilních stanic a síťové infrastruktury.

## Související pojmy

- [TCH/F – Traffic Channel / Full Rate](/mobilnisite/slovnik/tch-f/)
- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [TCH/H na 3GPP Explorer](https://3gpp-explorer.com/glossary/tch-h/)
