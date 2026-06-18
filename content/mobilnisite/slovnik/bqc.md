---
slug: "bqc"
url: "/mobilnisite/slovnik/bqc/"
type: "slovnik"
title: "BQC – Bad Quality Call"
date: 2025-01-01
abbr: "BQC"
fullName: "Bad Quality Call"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bqc/"
summary: "BQC je klíčový ukazatel výkonnosti (KPI), který měří procento hovorů ukončených z důvodu špatné kvality. Pomáhá operátorům identifikovat problémy sítě ovlivňující uživatelský zážitek sledováním hovorů"
---

BQC je klíčový ukazatel výkonnosti, který měří procento hovorů ukončených z důvodu špatné kvality, což pomáhá operátorům identifikovat problémy sítě ovlivňující uživatelský zážitek.

## Popis

Bad Quality Call (BQC, hovor se špatnou kvalitou) je standardizované měření výkonnosti definované ve specifikacích 3GPP, které kvantifikuje podíl hlasových hovorů, které dosahují nepřijatelné úrovně kvality vedoucí k předčasnému ukončení. Metrika funguje sledováním specifických parametrů kvality hovoru po celou dobu jeho trvání a jejich porovnáváním s předdefinovanými prahovými hodnotami. Když jsou tyto prahové hodnoty překročeny, systém klasifikuje hovor jako událost BQC, která přispívá k celkovému výpočtu míry BQC.

Technická implementace BQC zahrnuje nepřetržité sledování více ukazatelů kvality během aktivních hovorů. Mezi tyto ukazatele patří, ale nejsou omezeny na: metriky kvality řeči (jako ekvivalenty Mean Opinion Score), míry chyb rámců, míry ztráty paketů, variace zpoždění a měření síly signálu. Síťové prvky zodpovědné za zpracování hovorů, zejména v rádiové přístupové síti (RAN) a v jádru sítě (Core Network), tato měření sbírají v reálném čase. Systém používá sofistikované algoritmy ke korelaci více faktorů degradace a určení, zda celková kvalita hovoru klesla pod přijatelné úrovně.

Výpočet BQC se řídí specifickými vzorci definovanými ve specifikacích 3GPP, typicky vyjádřenými jako procento z celkového počtu hovorů. Měřící období, metodika vzorkování a prahové hodnoty jsou standardizovány, aby byla zajištěna konzistence napříč různými síťovými implementacemi a operátory. Metrika se počítá jak na úrovni jednotlivých buněk, tak pro celou síť, což umožňuje operátorům identifikovat jak lokalizované problémy, tak systémové potíže. Infrastruktura sběru dat zahrnuje sondy, systémy správy výkonnosti a specializované měřicí funkce integrované do síťových prvků.

Role BQC v řízení sítě přesahuje pouhé měření k aktivnímu zajišťování kvality. Síťoví operátoři používají data BQC ke spouštění automatizovaných optimalizačních procesů, identifikaci problematických oblastí sítě a stanovení priorit údržbových činností. Metrika se integruje s funkcemi samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)), aby umožnila automatické úpravy parametrů, které zlepšují kvalitu hovorů. Měření BQC také vstupují do systémů řízení zákaznického zážitku (CEM), poskytujíce vhled do skutečně vnímané kvality uživatelem spíše než jen do technického výkonu sítě.

## K čemu slouží

BQC byl vytvořen, aby řešil základní výzvu objektivního měření a zlepšování kvality hlasových hovorů v mobilních sítích. Před standardizovanými metrikami kvality se operátoři spoléhali na subjektivní stížnosti zákazníků a základní technická měření, která přesně neodrážela uživatelský zážitek. To ztěžovalo proaktivní identifikaci a řešení problémů s kvalitou dříve, než významně ovlivnily spokojenost zákazníků. Zavedení BQC poskytlo standardizovanou, objektivní metodu pro kvantifikaci degradace kvality hovorů.

Historický kontext vývoje BQC vznikl během přechodu na sítě 3G, kde se kvalita hlasu stala variabilnější kvůli přenosu s přepojováním paketů a zvýšené složitosti sítě. Tradiční metriky, jako jsou míry spadlých hovorů, nezachycovaly degradaci kvality, která nevedla k úplnému selhání hovoru. BQC tuto mezeru zaplnil měřením hovorů, které zůstaly spojené, ale poskytovaly špatný uživatelský zážitek. To bylo obzvláště důležité, protože hlasové služby zůstaly primárním zdrojem příjmů operátorů, což činilo udržování kvality klíčovým pro obchodní úspěch.

BQC řeší problém neviditelné degradace kvality tím, že poskytuje indikátory včasného varování předtím, než hovory zcela selžou. Umožňuje operátorům implementovat proaktivní strategie řízení kvality spíše než reaktivní řešení problémů. Metrika také usnadňuje srovnávání napříč různými síťovými technologiemi a operátory, což pohání celoprůmyslová zlepšení kvality. Zaměřením se na kvalitu vnímanou uživatelem spíše než jen na technické parametry sladí BQC úsilí o optimalizaci sítě se skutečným zákaznickým zážitkem.

## Klíčové vlastnosti

- Standardizované definice prahových hodnot kvality pro konzistentní měření napříč sítěmi
- Sledování více parametrů kvality v reálném čase během aktivních hovorů
- Integrace se systémy řízení sítě pro automatizovanou optimalizaci kvality
- Podpora jak hlasových služeb s přepojováním okruhů, tak s přepojováním paketů
- Schopnost korelace propojující degradaci kvality se specifickými síťovými prvky
- Historické trendy a reportování pro dlouhodobé řízení kvality

## Související pojmy

- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)
- [MOS – Mean Opinion Score](/mobilnisite/slovnik/mos/)

## Definující specifikace

- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B

---

📖 **Anglický originál a plná specifikace:** [BQC na 3GPP Explorer](https://3gpp-explorer.com/glossary/bqc/)
