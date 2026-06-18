---
slug: "rsd"
url: "/mobilnisite/slovnik/rsd/"
type: "slovnik"
title: "RSD – Reference Sensitivity Degradation"
date: 2026-01-01
abbr: "RSD"
fullName: "Reference Sensitivity Degradation"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rsd/"
summary: "RSD je metrika výkonu, která kvantifikuje zhoršení referenční citlivosti přijímače v důsledku interference jiných signálů v pásmu nebo mimo pásmo. Je klíčová pro definování požadavků na přijímače, zaj"
---

RSD je metrika výkonu, která kvantifikuje zhoršení (degradaci) referenční citlivosti přijímače způsobené interferencí jiných signálů v pásmu nebo mimo pásmo.

## Popis

Reference Sensitivity Degradation (RSD) je klíčový ukazatel výkonu a parametr testu shody definovaný ve specifikacích 3GPP, zejména od vydání Release 17. Měří, jak moc je referenční citlivost přijímače – minimální výkon vstupního signálu, při kterém je dosaženo specifikované kvality (např. určité chybovosti bloků) – zhoršena (degradována) přítomností rušivého signálu. Degradace je vyjádřena v decibelech (dB). Například RSD 3 dB znamená, že přijímač potřebuje signál o 3 dB silnější, aby dosáhl stejného výkonu jako bez rušiče. Test zahrnuje aplikaci požadovaného signálu na úrovni výkonu referenční citlivosti, zavedení řízeného rušiče na specifikované odstupňované frekvenci a výkonu a měření výsledné chybovosti.

Z architektonického hlediska RSD není síťovou funkcí, ale standardizovanou testovací metodologií a požadavkem aplikovaným na přijímače uživatelského zařízení (UE) a základnové stanice (gNB). Spadá pod charakteristiky rádiového výkonu definované ve specifikacích [RF](/mobilnisite/slovnik/rf/) požadavků. Klíčovými komponentami při hodnocení RSD jsou testovací zařízení generující přesné požadované a rušivé signály a testované zařízení ([DUT](/mobilnisite/slovnik/dut/)), jehož přijímač je charakterizován. Specifikace 3GPP podrobně definují testovací podmínky: typ požadovaného signálu (např. specifický referenční kanál), typ rušiče (např. nosná LTE, nosná 5G NR nebo generický [OFDM](/mobilnisite/slovnik/ofdm/) signál), frekvenční odstup mezi nimi a úroveň výkonu rušiče. Výsledná přípustná degradace definuje robustnost přijímače.

V kontextu nasazení a provozu sítě je RSD základním konceptem pro správu spektra a koexistenci. Jeho hodnoty, definované ve specifikacích shody, zajišťují, že zařízení od různých výrobců mají předvídatelnou a přijatelnou úroveň výkonu při nasazení v reálných prostředích s nevyhnutelnou interferencí. To je zvláště kritické pro režimy sdílení spektra, jako je Dynamické sdílení spektra (DSS) mezi 4G a 5G, nebo provoz ve sdíleném a nelicencovaném spektru (např. 5G [NR-U](/mobilnisite/slovnik/nr-u/)). Specifikací maximální povolené RSD zajišťuje 3GPP, že zavedení nové služby (např. nosné 5G) nezpůsobí katastrofické zhoršení citlivosti stávající sousední služby (např. nosné LTE). Plánovači sítí používají modely RSD k výpočtu ochranných pásem a plánování kmitočtů nosných, aby zajistili, že všechny služby splní své cíle kvality služby.

## K čemu slouží

RSD bylo zavedeno, aby formálně řešilo komplexní interferenční scénáře, které se staly běžnými s hustým, heterogenním a sdíleným nasazením spektra v 5G a dalších generacích. Starší vydání 3GPP měla požadavky na blokování a selektivitu, ale RSD poskytuje jemnější a přímější měřítko degradace výkonu v přítomnosti specifických, často v-kanálových nebo sousedně-kanálových, rušičů. Řeší problém kvantifikace reálného dopadu interference ze souběžně umístěných nebo sousedních rádiových systémů.

Historickým hybatelem byla proliferace nových technologií rádiového přístupu ([RAT](/mobilnisite/slovnik/rat/)) pracujících ve stejných kmitočtových pásmech. Například, když LTE a NR potřebují koexistovat ve stejném pásmu prostřednictvím DSS, bylo zásadní definovat, jak moc může přenos NR zhoršit citlivost přijímače LTE a naopak. Bez standardizovaných limitů RSD by jedna technologie mohla učinit druhou nepoužitelnou. Podobně pro provoz v nelicencovaném pásmu 6 GHz pro [NR-U](/mobilnisite/slovnik/nr-u/) musí zařízení koexistovat nejen s jinými zařízeními NR-U, ale také s Wi-Fi. Požadavky RSD zajišťují spravedlivou a předvídatelnou koexistenci.

Dále, jak se sítě vyvíjejí směrem k Open RAN a vícevýrobcovým nasazením, jsou standardizované metriky výkonu přijímače, jako je RSD, důležitější než kdy dříve. Poskytují jasné, testovatelné měřítko, které zajišťuje interoperabilitu. Operátor sítě kombinující rádiové jednotky od výrobce A s UE od výrobce B může být přesvědčen, že systém bude fungovat podle plánu, pokud všechny komponenty splní požadavky 3GPP na RSD. Zmírňuje to riziko, že implementace přijímačů specifické pro výrobce budou nadměrně citlivé na určité typy interference, což by v prostředí s více výrobci mohlo vést k neočekávaným mezerám v pokrytí nebo ztrátě kapacity.

## Klíčové vlastnosti

- Kvantifikuje degradaci citlivosti přijímače v dB způsobenou rušičem
- Definováno pro různé typy rušičů (např. LTE, NR, OFDM) a frekvenční odstupnění
- Klíčový parametr pro testování shody přijímačů UE a gNB
- Zásadní pro zajištění koexistence ve sdíleném spektru (DSS, NR-U)
- Podkládá plánování sítě pro rozestupy nosných a ochranná pásma
- Podporuje spolehlivý provoz v hustých, heterogenních nasazeních sítí

## Definující specifikace

- **TS 23.304** (Rel-20) — 5G Proximity Services (ProSe) Stage 2
- **TR 36.770** (Rel-18) — Technical Report for High Power UE in LTE Band 14

---

📖 **Anglický originál a plná specifikace:** [RSD na 3GPP Explorer](https://3gpp-explorer.com/glossary/rsd/)
