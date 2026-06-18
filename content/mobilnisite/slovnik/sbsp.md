---
slug: "sbsp"
url: "/mobilnisite/slovnik/sbsp/"
type: "slovnik"
title: "SBSP – Special Burst Scheduling Period"
date: 2025-01-01
abbr: "SBSP"
fullName: "Special Burst Scheduling Period"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sbsp/"
summary: "Special Burst Scheduling Period (SBSP) je parametr v UMTS (WCDMA), který definuje periodický časový interval, během nějž síť může naplánovat vysílání speciálních přenosů (Special Bursts) ve vzestupném"
---

SBSP je parametr UMTS definující periodický interval, ve kterém síť může naplánovat speciální vzestupné (uplink) přenosy pro procedury jako měření v komprimovaném režimu.

## Popis

Special Burst Scheduling Period (SBSP) je koncept definovaný ve specifikacích 3GPP UMTS, konkrétně související s provozem fyzické vrstvy rozhraní [WCDMA](/mobilnisite/slovnik/wcdma/). Jedná se o konfigurovatelný síťový parametr, který stanovuje periodický časový rámec, během nějž síť může naplánovat 'Special Bursts' na vzestupném vyhrazeném fyzickém řídicím kanálu ([DPCCH](/mobilnisite/slovnik/dpcch/)). DPCCH je řídicí kanál doprovázející vyhrazený fyzický datový kanál ([DPDCH](/mobilnisite/slovnik/dpdch/)) ve spojení WCDMA, který nese pilotní bity pro odhad kanálu, indikátor kombinace transportního formátu ([TFCI](/mobilnisite/slovnik/tfci/)), zpětnou informaci ([FBI](/mobilnisite/slovnik/fbi/)) a příkazy řízení vysílacího výkonu ([TPC](/mobilnisite/slovnik/tpc/)).

Během normálního provozu vysílá vzestupný DPCCH nepřetržitě. Mechanismus SBSP však umožňuje řídicímu řadiči rádiové sítě ([RNC](/mobilnisite/slovnik/rnc/)) nařídit uživatelskému zařízení (UE), aby během konkrétních, naplánovaných mezer dočasně vysílalo předdefinovaný vzor 'Special Burst' na DPCCH. Primárním technickým účelem těchto Special Bursts je umožnit provoz v komprimovaném režimu. Komprimovaný režim je technika používaná v UMTS k vytváření přenosových mezer v normálních rámečcích pro vzestupný/sestupný směr, což umožňuje přijímači UE naladit se na jiné frekvence (např. pro mezifrekvenční nebo mezisystémová měření, jako je měření nosných GSM) bez nutnosti duálního přijímače.

SBSP definuje periodicitu těchto příležitostí pro vysílání Special Burst. Když síť nakonfiguruje komprimovaný režim, použije SBSP k zarovnání přenosových mezer. Během naplánované mezery UE zastaví své normální vysílání DPDCH/DPCCH a může vyslat Special Burst, což je krátký, známý signál. Tento Special Burst pomáhá udržovat smyčku řízení výkonu ve vzestupném směru a umožňuje Node B odhadnout stav kanálu i během mezery, čímž zajišťuje rychlejší a stabilnější obnovení spojení po skončení mezery. Konfigurace SBSP, včetně jeho periody a délky, je signalizována UE prostřednictvím zpráv řízení rádiových zdrojů ([RRC](/mobilnisite/slovnik/rrc/)) z RNC jako součást parametrů komprimovaného režimu. Tento parametr je klíčový pro vyvážení potřeby měřicích mezer s potřebou udržovat kvalitu spojení a synchronizaci.

## K čemu slouží

SBSP byl zaveden pro podporu kritické funkce mobility, kterou je předávání spojení mezi různými frekvencemi nebo různými technologiemi rádiového přístupu (inter-RAT), konkrétně v UMTS (Release 99 a novější). Ve WCDMA systému UE typicky nepřetržitě vysílá a přijímá na přiřazené frekvenci. Pro přípravu na předání spojení do jiného pásma UMTS nebo do sítě GSM musí UE změřit sílu signálu a kvalitu těchto potenciálních cílových buněk. Bez specifického mechanismu by to vyžadovalo drahé a energeticky neefektivní duální přijímače v UE.

Komprimovaný režim byl vyvinut jako řešení, které dočasně komprimuje data do kratších přenosových rámců, aby vytvořilo nečinná období pro měření. SBSP je nedílnou součástí tohoto řešení, poskytuje strukturovaný a předvídatelný plánovací rámec pro tyto mezery komprimovaného režimu. Řeší problém, jak periodicky vytvářet tyto příležitosti pro měření ve vzestupném směru, aniž by došlo k selhání řídicí smyčky vzestupného směru (zejména řízení výkonu). Special Burst vysílaný během mezery SBSP udržuje minimální spojení, což umožňuje Node B sledovat signál UE.

Jeho vytvoření bylo motivováno požadavkem na bezproblémovou mobilitu ve scénářích nasazení s více frekvencemi a více technologiemi RAT, které jsou nezbytné pro vyrovnávání zátěže sítě, optimalizaci pokrytí a plynulý vývoj ze sítí 2G na 3G. Parametr SBSP poskytl síťovým operátorům kontrolu nad načasováním a četností těchto měřicích mezer, což jim umožnilo volit mezi měřicím výkonem (více/častější mezery) a efektivitou přenosu dat (méně mezer).

## Klíčové vlastnosti

- Definuje periodické plánování pro vysílání Special Burst ve vzestupném směru
- Umožňuje a strukturovaně řídí provoz komprimovaného režimu v UMTS
- Umožňuje provádění mezifrekvenčních a mezisystémových (inter-RAT) měření UE
- Pomáhá udržovat řízení výkonu a synchronizaci ve vzestupném směru během přenosových mezer
- Konfigurovatelný parametr signalizovaný sítí prostřednictvím RRC
- Nedílná součást procedur mobility a předávání spojení ve WCDMA

## Související pojmy

- [DPCCH – Dedicated Physical Control Channel](/mobilnisite/slovnik/dpcch/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [SBSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbsp/)
