---
slug: "sml"
url: "/mobilnisite/slovnik/sml/"
type: "slovnik"
title: "SML – Soft Metric Location"
date: 2025-01-01
abbr: "SML"
fullName: "Soft Metric Location"
category: "Radio Access Network"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/sml/"
summary: "Parametr používaný v UMTS a LTE správě rádiových zdrojů, představující soft bit kanálu, který indikuje kvalitu nebo spolehlivost přijímaného signálu. Je využíván v algoritmech pro rozhodování o přecho"
---

SML je parametr soft bitů kanálu používaný v UMTS a LTE správě rádiových zdrojů k indikaci kvality signálu nebo spolehlivosti pro algoritmy přechodů mezi buňkami, řízení výkonu a adaptace spojení.

## Popis

Soft Metric Location (SML) je koncept používaný ve fyzické vrstvě a správě rádiových zdrojů 3GPP mobilních sítí, zejména v systémech UMTS ([WCDMA](/mobilnisite/slovnik/wcdma/)) a LTE. Odkazuje na soft bit kanálu nebo metrik odvozenou z přijímaného signálu, která poskytuje informaci o kvalitě nebo spolehlivosti přenosu. V digitálních komunikacích představují 'soft' bity výstup demodulátoru s úrovněmi spolehlivosti (často jako logaritmické poměry věrohodnosti, LLR) na rozdíl od pevně rozhodnutých hodnot '0' nebo '1'. SML využívá tyto soft hodnoty k odhadu podmínek kanálu, jako je poměr signálu k šumu a interferenci ([SINR](/mobilnisite/slovnik/sinr/)) nebo chybovost bitů ([BER](/mobilnisite/slovnik/ber/)), které jsou klíčové pro adaptivní algoritmy. Tato metrika se typicky počítá v základnové stanici (NodeB nebo eNodeB) nebo v uživatelském terminálu (UE) zpracováním přijatých symbolů s ohledem na faktory jako útlum, interference a šum.

V praxi se SML používá v různých funkcích správy rádiových zdrojů ([RRM](/mobilnisite/slovnik/rrm/)) ke zlepšení výkonu sítě. Pro rozhodování o přechodech mezi buňkami v UMTS může být SML součástí měření hlášených UE radiové síti ([RNC](/mobilnisite/slovnik/rnc/)), což pomáhá určit, kdy spustit přechod mezi buňkami na základě kvality signálu spíše než pouze přijímané síly signálu. Tím se zlepšuje přesnost přechodů a snižuje počet přerušených hovorů. V algoritmech řízení výkonu poskytuje SML zpětnou vazbu o kvalitě spoje, což umožňuje dynamické přizpůsobení vysílacího výkonu pro udržení cílové kvality při minimalizaci interference. Dále, pro adaptaci spojení – jako je adaptivní modulace a kódování ([AMC](/mobilnisite/slovnik/amc/)) – SML informuje o výběru modulačních schémat a kódovacích rychlostí, které odpovídají aktuálním podmínkám kanálu, a maximalizuje tak propustnost a spolehlivost. Specifikace jako 25.101 pro rádiový vysílací a přijímací terminál v UMTS podrobně popisují postupy měření zahrnující soft metriky, zatímco 32.819 odkazuje na SML v kontextu řízení výkonu pro RRM.

Technická implementace SML zahrnuje komponenty zpracování signálu v řetězci vysílače/přijímače. Po demodulaci se přijaté symboly převedou na soft bity, které se dále zpracují pro výpočet metrik jako SML. Tyto metriky mohou být časově zprůměrovány nebo filtrovány za účelem redukce šumu a následně použity jako vstupy do RRM algoritmů. V síťové architektuře proudí SML data mezi UE a sítí prostřednictvím hlášení o měření a přispívají k centralizovaným nebo distribuovaným rozhodovacím procesům řízení. Jeho role je zvláště důležitá v systémech založených na [CDMA](/mobilnisite/slovnik/cdma/), jako je UMTS, kde jsou měkké přechody a řízení výkonu kritické kvůli provozu omezenému interferencí. Poskytnutím jemnějšího pohledu na kvalitu kanálu než samotné pevné metriky umožňuje SML efektivnější využití rádiových zdrojů, lepší správu mobility a zlepšenou celkovou kapacitu systému a uživatelský zážitek.

## K čemu slouží

SML bylo zavedeno proto, aby uspokojilo potřebu přesnějších a spolehlivějších indikátorů kvality kanálu v mobilních sítích, zejména když se systémy vyvíjely pro podporu vyšších přenosových rychlostí a složitějších rádiových prostředí. Rané mobilní systémy se často spoléhaly na jednoduché metriky, jako je indikátor síly přijímaného signálu ([RSSI](/mobilnisite/slovnik/rssi/)), pro rozhodnutí jako přechod mezi buňkami, ale ty mohly být zavádějící v podmínkách silné interference nebo útlumu. Soft metriky, odvozené z procesu demodulace, poskytují pravděpodobnostní měřítko spolehlivosti bitů, které lépe odráží skutečné podmínky kanálu. To umožňuje chytřejší rozhodování RRM, snižuje chybovost a zlepšuje výkon v technologiích jako WCDMA, kde je zásadní řízení interference.

V 3GPP se SML objevilo s UMTS pro zlepšení klíčových funkcí, jako je měkký přechod a rychlé řízení výkonu. Měkký přechod ve WCDMA vyžaduje přesná měření kvality, aby se určilo, kdy má UE komunikovat s více buňkami současně, a SML nabízí jemnější metriku než prosté úrovně výkonu. Pomáhá vyvažovat kompromisy mezi kvalitou signálu a interferencí, což vede k menšímu počtu přerušených hovorů a lepšímu pokrytí. Pro řízení výkonu umožňuje SML rychlejší a přesnější úpravy, šetří životnost baterie v UE a snižuje celkovou interferenci v síti. S pokrokem sítí k LTE a 5G principy stojící za SML ovlivnily pokročilé techniky, jako je hlášení informace o stavu kanálu (CSI) a adaptace masivního MIMO, i když samotný termín je více spojen s dřívějšími vydáními. Jeho vznik byl motivován posunem k datově orientovaným službám, kde optimalizace kvality spojení přímo ovlivňuje propustnost a latenci, a tak uspokojuje uživatelské požadavky na spolehlivou mobilní konektivitu.

## Klíčové vlastnosti

- Odvozeno z soft bitů kanálu reprezentujících spolehlivost signálu
- Používáno ve správě rádiových zdrojů pro přechody mezi buňkami, řízení výkonu a adaptaci spojení
- Poskytuje jemnější odhad kvality kanálu než pevné metriky
- Podporuje hlášení měření mezi UE a sítí
- Zvyšuje výkon v prostředích omezených interferencí, jako je WCDMA
- Integruje se s algoritmy pro adaptivní modulaci a kódování

## Související pojmy

- [RRM – Radio Resource Management](/mobilnisite/slovnik/rrm/)
- [SINR – Signal to Interference plus Noise Ratio](/mobilnisite/slovnik/sinr/)

## Definující specifikace

- **TS 25.101** (Rel-19) — UTRA FDD UE RF Requirements
- **TS 32.819** (Rel-8) — Element Management Layer OS Functions

---

📖 **Anglický originál a plná specifikace:** [SML na 3GPP Explorer](https://3gpp-explorer.com/glossary/sml/)
