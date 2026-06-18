---
slug: "rfn"
url: "/mobilnisite/slovnik/rfn/"
type: "slovnik"
title: "RFN – RNC Frame Number"
date: 2025-01-01
abbr: "RFN"
fullName: "RNC Frame Number"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/rfn/"
summary: "12bitový čítač vedený řadičem rádiové sítě (RNC) v sítích UMTS. Poskytuje společný časový referenční signál pro plánování, předávání spojení (handover) a synchronizační procedury mezi RNC a více Node"
---

RFN je 12bitový čítač vedený řadičem rádiové sítě (RNC) v UMTS, který poskytuje společný časový referenční signál pro plánování a synchronizaci mezi RNC a Node B na rozhraní UTRAN.

## Popis

[RNC](/mobilnisite/slovnik/rnc/) Frame Number (RFN) je klíčový časový parametr v rádiové přístupové síti ([UTRAN](/mobilnisite/slovnik/utran/)) systému Universal Mobile Telecommunications System (UMTS). Jedná se o 12bitový čítač, který cykluje od 0 do 4095 a je nezávisle veden každým řadičem rádiové sítě (RNC). RFN slouží jako hlavní časová základna RNC pro rámcové časování na rozhraní Iub, které spojuje RNC s jím řízenými základnovými stanicemi Node B. Každý rámec přenášený přes rozhraní Iub je asociován s konkrétní hodnotou RFN, což poskytuje časový referenční bod pro všechna datová a řídicí signalizaci vyměňovanou mezi RNC a Node B.

Fungování RFN je svázáno s rámcovou strukturou UTRAN, kde jeden rádiový rámec má délku 10 ms. 12bitový čítač poskytuje cyklus 4096 rámců, což odpovídá hyperrámci o délce 40,96 sekundy. RNC inkrementuje svůj RFN na každé hranici 10ms rámce. Tato hodnota RFN se používá k časovému označování zpráv a plánování přenosu datových rámců (přes přenosové kanály dat Iub) a řídicích rámců (jako jsou zprávy [NBAP](/mobilnisite/slovnik/nbap/) - Node B Application Part). Například když RNC odešle Node B požadavek na nastavení rádiového spoje (Radio Link Setup Request), zahrnuje časovací informace založené na RFN, aby Node B instruovalo, kdy má začít vysílat na novém rádiovém spoji.

Klíčovou funkcí RFN je umožnit synchronizaci mezi RNC a více Node B pro procedury, jako je měkké předání spojení (soft handover). Při měkkém předání spojení komunikuje uživatelské zařízení (UE) současně s více Node B. RNC musí zajistit, aby datové rámce odeslané těmto různým Node B pro stejné UE byly časově zarovnány, aby mohly být správně zkombinovány v přijímači UE. RNC používá svůj interní RFN k výpočtu parametrů Frame Offset a Chip Offset, které odesílá každému Node B, a tím jim instruuje přesné časování jejich vysílání vzhledem k časové základně RFN RNC. Tato centralizovaná časová kontrola ze strany RNC je charakteristickým rysem architektury UMTS, který kontrastuje s distribuovanějším časováním v pozdějších systémech LTE a 5G NR.

RFN je také zásadní pro fungování synchronizačního protokolu na rozhraní Iub. Node B synchronizuje své vlastní časování s RFN RNC prostřednictvím procesu, při kterém měří časování přijímaných rámců a podle toho upravuje své vysílání. To zajišťuje, že celý cluster Node B pod jedním RNC pracuje na společné časové základně, což je nezbytné pro koordinované vícebodové operace a efektivní správu rádiových zdrojů. Specifikace řídící RFN, především TS 25.402 (synchronizace UTRAN) a TS 21.905 (slovní zásoba), podrobně popisují jeho vztah k dalším časovým identifikátorům UTRAN, jako je [BFN](/mobilnisite/slovnik/bfn/) (Node B Frame Number) a [SFN](/mobilnisite/slovnik/sfn/) (System Frame Number).

## K čemu slouží

RFN byl vytvořen k řešení základního problému časové koordinace a synchronizace v hierarchické, centralizované architektuře UMTS [UTRAN](/mobilnisite/slovnik/utran/). V této architektuře jeden [RNC](/mobilnisite/slovnik/rnc/) řídí více Node B a spravuje složité procedury, jako je měkké předání spojení. Bez společné, přesné časové reference vycházející z RNC by bylo nemožné koordinovat vysílání a příjem signálů přes různá Node B pro stejné uživatelské spojení, což by vedlo k neúspěšným předáním spojení a degradaci kvality hovoru.

Historicky sítě GSM používaly jinou časovou strukturu založenou na řadiči základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)), ale zavedení systému WCDMA založeného na CDMA v UMTS přineslo nové výzvy. Systémy CDMA jsou vysoce citlivé na časové chyby; signály musí dorazit k UE ve velmi krátkém časovém okně, aby mohly být správně despreádovány. RFN jako součást synchronizační architektury UTRAN definované od verze Release 4 poskytl potřebný mechanismus, aby RNC mohlo fungovat jako časový nadřízený (master). Vyřešil tak omezení plynoucí z toho, že každé Node B pracovalo s nezávislými hodinami, což by způsobovalo časový drift a nezarovnání, a znemožňovalo by spolehlivé pokročilé funkce, jako je makro-diverzitní kombinování při měkkém předání spojení.

Jeho vytvoření bylo motivováno potřebou škálovatelného a řiditelného časovacího řešení. RFN umožňuje RNC předvídatelně plánovat všechny aktivity ve své doméně. Řeší problém, jak sdělit 'kdy' se má něco stát přes rozhraní Iub. Tím, že RNC časově označí příkazy hodnotami RFN, může předem naplánovat akce (jako zahájení rádiového spoje) s dostatečným předstihem a zohlednit přitom zpoždění přenosové sítě. Tento návrh byl klíčový pro podporu služeb reálného času s přísnými požadavky na zpoždění přes často asynchronní přenosovou síť (jako ATM nebo IP). RFN se tak stal základním kamenem fungování UTRAN a umožnil pokročilé rádiové funkce, které odlišovaly rané sítě 3G od jejich předchůdců 2G.

## Klíčové vlastnosti

- 12bitový čítač vedený řadičem rádiové sítě (RNC)
- Poskytuje společný časový referenční signál pro všechna Node B pod kontrolou jednoho RNC
- Zásadní pro plánování přenosů a signalizaci na rozhraní Iub
- Kritický pro synchronizaci více Node B během procedur měkkého předání spojení (soft handover)
- Tvoří základ pro výpočet parametrů Frame Offset a Chip Offset
- Definován v synchronizačních specifikacích UTRAN (TS 25.402)

## Související pojmy

- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms

---

📖 **Anglický originál a plná specifikace:** [RFN na 3GPP Explorer](https://3gpp-explorer.com/glossary/rfn/)
