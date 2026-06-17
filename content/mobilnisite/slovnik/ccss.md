---
slug: "ccss"
url: "/mobilnisite/slovnik/ccss/"
type: "slovnik"
title: "CCSS – Call Completion Service Set-up"
date: 2025-01-01
abbr: "CCSS"
fullName: "Call Completion Service Set-up"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ccss/"
summary: "CCSS je služební funkce 3GPP umožňující rozšířené mechanismy dokončování hovorů pro okruhově přepínané (circuit-switched) hovory, především Čekání na hovor (CW) a Dokončení komunikace se zaneprázdněný"
---

CCSS je služební funkce 3GPP, která umožňuje rozšířené mechanismy dokončování hovorů, jako je Čekání na hovor (Call Waiting) a CCBS, aby volajícího upozornila, když se obsazený účastník uvolní, nebo aby ho varovala před příchozím druhým hovorem.

## Popis

Call Completion Service Set-up (CCSS) je standardizovaný služební rámec definovaný 3GPP pro správu rozšířených scénářů dokončování hovorů v okruhově přepínané ([CS](/mobilnisite/slovnik/cs/)) doméně mobilních sítí. Funguje jako doplňková služba v jádru sítě, která interaguje s Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) a Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)). Nastavení služby zahrnuje specifické procedury a signalizační toky mezi síťovými entitami pro aktivaci, vyvolání a správu funkcí jako Čekání na hovor a [CCBS](/mobilnisite/slovnik/ccbs/).

Architektonicky je CCSS implementována v rámci MSC a může zahrnovat servisní logiku v HLR pro správu profilů účastníků. Když pokus o hovor narazí na stav obsazeno (pro CCBS) nebo je účastník již v hovoru (pro [CW](/mobilnisite/slovnik/cw/)), MSC vyvolá procedury CCSS. Pro CCBS MSC uloží informace o hovorovém požadavku, monitoruje stav zaneprázdněného účastníka prostřednictvím správy mobility a iniciuje zpětné zavolání původnímu účastníkovi, jakmile se volaná strana uvolní. To zahrnuje správu časovačů, rezervaci prostředků pro pokus o zpětné volání a generování odpovídajících účtovacích záznamů.

Pro Čekání na hovor (Call Waiting) rámec CCSS umožňuje MSC upozornit obsazeného účastníka na příchozí čekající hovor pomocí specifického tónu nebo indikace, aniž by přerušil probíhající hovor. Účastník si pak může vybrat, zda čekající hovor přijme, odmítne nebo ignoruje. Nastavení služby zahrnuje vyjednávání a správu stavu čekajícího hovoru, zpracování odpovědí účastníka a interakci se základním řízením hovoru. Procedury CCSS jsou podrobně popsány v 3GPP TS 29.163, která specifikuje vzájemné propojení mezi MSC a dalšími síťovými elementy, často se zaměřením na IP Multimedia Subsystem (IMS) a scénáře propojení CS a IMS v pozdějších vydáních.

CCSS hraje klíčovou roli ve zvyšování spolehlivosti a uživatelské spokojenosti u tradičních hlasových služeb. Poskytnutím mechanismů pro dokončení hovorů, které by jinak selhaly, zvyšuje úspěšnost dokončení síťového provozu a snižuje potřebu opakovaných pokusů o přivolání, které mohou zahlcovat signalizační kanály. Její integrace vyžaduje podporu specifických rozšíření signalizace [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) nebo Diameter pro správu dat účastníků a vyvolání služby, což zajišťuje bezproblémový provoz mezi zařízeními různých výrobců a napříč generacemi sítí, kde je podporován CS fallback nebo legacy služby.

## K čemu slouží

CCSS byla vytvořena, aby řešila běžnou uživatelskou frustraci a neefektivitu sítě způsobenou obsazenými účastníky a zmeškanými příležitostmi pro hovory v okruhově přepínaných mobilních sítích. Před její standardizací základní obsluha hovoru při obsazení účastníka jednoduše vedla k obsazovacímu tónu nebo neúspěchu hovoru, což vedlo k opakovaným pokusům o spojení a zvýšenému zatížení signalizace bez záruky dokončení. Účelem bylo zavést inteligentní, síťově asistované funkce, které by mohly hovor automaticky dokončit, jakmile to podmínky dovolí, a tím zlepšit úspěšnost hovorů napoprvé a celkovou kvalitu služeb.

Historický kontext spočívá ve vývoji od základní telefonie k rozšířeným doplňkovým službám v sítích GSM a UMTS. Funkce jako Čekání na hovor a Přidržení hovoru existovaly, ale vyžadovaly standardizované, robustní nastavení a procedury vzájemného propojení, zejména když se sítě vyvíjely směrem k plně IP architekturám jako IMS. CCSS poskytla jednotný rámec pro tyto služby, což zajišťuje konzistentní chování mezi různými operátory a výrobci síťového vybavení. Řešila problém proprietárních implementací, které mohly bránit interoperabilitě a roamingu.

CCSS dále řešila omezení pasivního selhání hovoru tím, že učinila síť aktivní při správě dokončování hovorů. Pro [CCBS](/mobilnisite/slovnik/ccbs/) vyřešila problém, kdy volající strana musela ručně opakovaně zkoušet volat na obsazené číslo, což bylo nepohodlné a mohlo zatěžovat síťové zdroje neúspěšnými pokusy. Automatizací zpětného volání optimalizovala využití zdrojů a zlepšila zákaznický zážitek. Rámec také položil základy pro konvergenci s IP službami, jak je specifikováno v TS 29.163 pro IMS Centralized Services (ICS) a propojení CS-IMS, což zajišťuje podporu funkcí pro dokončování hovorů z legacy systémů v rozvíjejících se síťových architekturách.

## Klíčové vlastnosti

- Standardizované procedury aktivace a vyvolání pro Čekání na hovor (CW)
- Síťově řízený mechanismus zpětného volání pro Dokončení komunikace se zaneprázdněným účastníkem (CCBS)
- Integrace s MSC a HLR pro správu služebního profilu účastníka
- Podpora časovačů pro správu zdrojů a frontování hovorů
- Generování specifických účtovacích záznamů pro události dokončení hovoru
- Propojení s IMS a dalšími doménami podle TS 29.163

## Související pojmy

- [CCBS – Completion of Communications to Busy Subscriber](/mobilnisite/slovnik/ccbs/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks

---

📖 **Anglický originál a plná specifikace:** [CCSS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ccss/)
