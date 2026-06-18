---
slug: "sfd"
url: "/mobilnisite/slovnik/sfd/"
type: "slovnik"
title: "SFD – Start Frame Delimiter"
date: 2025-01-01
abbr: "SFD"
fullName: "Start Frame Delimiter"
category: "Physical Layer"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sfd/"
summary: "Specifický bitový vzor používaný v 5G neterestriálních sítích (NTN) k označení začátku rámce pro synchronizaci. Je klíčový pro navázání časového zarovnání mezi satelitem/branou a uživatelským zařízení"
---

SFD je specifický bitový vzor používaný v 5G neterestriálních sítích (NTN) k označení začátku rámce pro synchronizaci, který umožňuje časové zarovnání přes dlouhá a proměnná zpoždění.

## Popis

Start Frame Delimiter (SFD) je základní synchronizační signál ve fyzické vrstvě 5G neterestriálních sítí ([NTN](/mobilnisite/slovnik/ntn/)), standardizovaný v 3GPP Release 15 a zachovaný v následujících vydáních. Funguje jako odlišná, předem definovaná bitová sekvence vysílaná na začátku rámce. Primární technickou rolí SFD je poskytnout jednoznačný časový referenční bod, který umožňuje přijímači – ať už uživatelskému zařízení (UE) na zemi nebo síťovému uzlu – provést synchronizaci rámce. Tento proces je v prostředí NTN kritický kvůli výjimečně dlouhým a proměnným zpožděním šíření zavedeným satelitními spoji, která se mohou pohybovat od několika milisekund pro satelity na nízké oběžné dráze ([LEO](/mobilnisite/slovnik/leo/)) až po stovky milisekund pro geostacionární ([GEO](/mobilnisite/slovnik/geo/)) satelity. Přijímač kontinuálně vyhledává tento známý vzor v příchozím bitovém toku; po jeho detekci může přesně zarovnat svůj interní časování na začátek hranice rámce, čímž správně vymezí strukturu rámce pro následné dekódování řídicích a datových kanálů.

Z architektonického hlediska je SFD integrován do preambule rámce. Jeho návrh musí vyvážit detekovatelnost a spektrální účinnost. Vzor je zvolen pro své silné autokorelační vlastnosti, což znamená, že při korelaci se sebou samým má ostrý vrchol a nízkou korelaci s náhodnými daty nebo jinými částmi signálu. Tato vlastnost minimalizuje pravděpodobnost falešné detekce (falešných poplachů) nebo nezachycené detekce, což je prvořadé v hlučném a útlumovými jevy náchylném satelitním kanálu. Generování a vložení SFD zajišťuje řetězec zpracování fyzické vrstvy v vysílači, typicky po kanálovém kódování a modulaci. V přijímači se pro skenování vzoru SFD používá přizpůsobený filtr nebo korelační obvod a časový posun odpovídající vrcholu korelačního výstupu se použije k úpravě okamžiku vzorkování.

Jeho role přesahuje pouhou synchronizaci. Úspěšná detekce SFD je často předpokladem pro další procedury fyzické vrstvy, jako je dekódování hlavního informačního bloku ([MIB](/mobilnisite/slovnik/mib/)) nebo bloků systémové informace ([SIB](/mobilnisite/slovnik/sib/)), které v rámci následují. Jedná se o nízkourovňový, zásadní handshake, který zajišťuje, že přijímač a vysílač pracují na společné časové bázi, než může pokračovat jakákoli komunikace vyšší vrstvy. V kontextu NTN, kde pohyb satelitu (u negeostacionárních satelitů) způsobuje kontinuální Dopplerův posuv a časovou derivační odchylku, poskytuje SFD periodický referenční bod. Zatímco pokročilé techniky jako příkazy časového předstihu (timing advance) spravují průběžnou synchronizaci, počáteční a periodické zarovnání rámce zajišťované SFD je základní. Bez robustní detekce SFD by bylo celé navázání a udržování spoje v 5G NTN nespolehlivé, což by vedlo k neúspěšným připojením a špatné kvalitě služeb.

## K čemu slouží

SFD byl zaveden speciálně k řešení jedinečných synchronizačních výzev vlastních integraci satelitního přístupu do systému 5G, což je klíčová pracovní položka od Release 15 dále. Pozemní sítě pracují s relativně krátkými a stabilními zpožděními šíření, což umožňuje, aby synchronizační mechanismy navržené pro tyto podmínky fungovaly dostatečně. Přímá aplikace těchto mechanismů na satelitní spoje je však problematická kvůli o několik řádů větším zpožděním a jejich proměnlivosti způsobené pohybem satelitu na oběžné dráze. Primární problém, který SFD řeší, je spolehlivá identifikace přesného začátku přenosového rámce v tomto prostředí s vysokou latencí a dynamikou. Předchozí synchronizační signály pro pozemní sítě nebyly navrženy tak, aby byly odolné vůči specifickému profilu zkreslení satelitních kanálů, který zahrnuje významný útlum na dráze, Dopplerovy jevy a potenciální stínění.

Vytvoření SFD bylo motivováno vizí 3GPP pro jednotné rádiové rozhraní, které bezproblémově zahrnuje neterestriální sítě. Základním požadavkem pro tuto integraci je, aby se uživatelská zařízení (UE) mohla synchronizovat se satelitní buňkou způsobem stejně spolehlivým jako s pozemní buňkou, navzdory zcela odlišným podmínkám fyzické vrstvy. SFD poskytuje pro toto počáteční časové zachycení vyhrazený, optimalizovaný signál. Slouží jako jasná značka 'začni zde', která se snadno odliší od šumu a dat, což umožňuje UE rychle se zachytit satelitního signálu. Tato schopnost je zásadní pro zkrácení času počátečního přístupu, šetření životnosti baterie UE během hledání buněk a zajištění stabilního základu spojení, na kterém mohou být aplikována další přizpůsobení specifická pro [NTN](/mobilnisite/slovnik/ntn/) (jako je předkompenzace zpoždění na bráně). Řeší tak omezení předchozích přístupů, kterým chyběl vyhrazený, robustní oddělovač schopný spolehlivě fungovat přes několik set milisekund rozprostření zpoždění a za podmínek nízkého poměru signálu k šumu typických pro satelitní komunikaci.

## Klíčové vlastnosti

- Poskytuje jednoznačnou časovou referenci pro synchronizaci začátku rámce
- Navržen se silnými autokorelačními vlastnostmi pro spolehlivou detekci v hlučných NTN kanálech
- Integrální součást preambule rámce ve struktuře fyzické vrstvy 5G NTN
- Umožňuje počáteční časové zachycení v satelitním prostředí s vysokým zpožděním šíření
- Podporuje systémy s geostacionárními (GEO) i negeostacionárními (NGSO) satelitními drahami
- Základ pro následné dekódování systémových informací a datových kanálů

## Související pojmy

- [NTN – Non-Terrestrial Networks](/mobilnisite/slovnik/ntn/)

## Definující specifikace

- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [SFD na 3GPP Explorer](https://3gpp-explorer.com/glossary/sfd/)
