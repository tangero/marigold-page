---
slug: "slc"
url: "/mobilnisite/slovnik/slc/"
type: "slovnik"
title: "SLC – Signalling Link Code"
date: 2025-01-01
abbr: "SLC"
fullName: "Signalling Link Code"
category: "Core Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/slc/"
summary: "Signalling Link Code (SLC) je číselný identifikátor používaný v signalizačních sítích založených na SS7 a SIGTRAN k jednoznačnému rozlišení mezi více paralelními signalizačními spoji spojujícími tytéž"
---

SLC je číselný identifikátor používaný v signalizačních sítích SS7 a SIGTRAN k jednoznačnému rozlišení mezi více paralelními signalizačními spoji spojujícími tytéž dva signalizační body.

## Popis

Signalling Link Code (SLC) je základní parametr v systému [SS7](/mobilnisite/slovnik/ss7/) (Signalling System No. 7) a jeho IP nástupci SIGTRAN. Funguje na vrstvě signalizačního spoje ([MTP2](/mobilnisite/slovnik/mtp2/)) protokolového zásobníku. Linkset je skupina signalizačních spojů mezi dvěma sousedními signalizačními body ([SP](/mobilnisite/slovnik/sp/)), například dvěma [MSC](/mobilnisite/slovnik/msc/) nebo MSC a [HLR](/mobilnisite/slovnik/hlr/). SLC poskytuje lokální identifikátor, typicky 4bitový (hodnoty 0-15), pro každý fyzický spoj v rámci tohoto linksetu. Zatímco zdrojový a cílový kód bodu (OPC/[DPC](/mobilnisite/slovnik/dpc/)) identifikují signalizační body, SLC identifikuje konkrétní cestu mezi nimi.

Při aktivaci spoje je hodnota SLC dohodnuta oběma konci spoje výměnou testovacích zpráv signalizačního spoje. Tato hodnota je následně zahrnuta v hlavičce signalizační jednotky vrstvy 2 (např. [MSU](/mobilnisite/slovnik/msu/), LSSU). Vrstva MTP2 používá SLC pro několik klíčových funkcí. Umožňuje části Message Transfer Part Level 3 ([MTP3](/mobilnisite/slovnik/mtp3/)) spravovat více spojů v rámci linksetu a provádět sdílení zátěže distribucí zpráv přes dostupné spoje na základě SLC. Důležitější je, že umožňuje identifikaci selhání a obnovu; pokud spoj selže, může MTP3 směrovat provoz na jiné spoje v linksetu pomocí jejich odlišných SLC.

V architekturách SIGTRAN (jako M3UA) je koncept přizpůsoben pro IP přenos. SLC je přenášen v parametrech adaptační vrstvy (např. pole Signalling Link Selection - SLS je často odvozeno nebo namapováno na SLC), aby byla zachována stejná logická identifikace spoje a chování sdílení zátěže přes SCTP asociace a streamy. SLC tedy zůstává klíčovým prvkem pro zajištění spolehlivého, redundantního a efektivního signalizačního přenosu jak v TDM, tak v IP jádrových sítích.

## K čemu slouží

Signalling Link Code existuje pro správu redundance a distribuce zátěže v telefonních signalizačních sítích. Rané signalizační systémy používaly mezi ústřednami jednotlivé spoje, což vytvářelo jediný bod selhání. S růstem sítí byly pro kapacitu a odolnost instalovány více paralelní spoje. SLC poskytuje mechanismus k identifikaci a správě těchto jednotlivých spojů v rámci skupiny (linksetu).

Řeší problém nejednoznačnosti. Dva signalizační body potřebují způsob, jak odkazovat na konkrétní spoj při odesílání řídicích příkazů (např. 'vyřaď spoj č. 3 z provozu') a jak identifikovat, kterým spojem přijatá zpráva prošla pro diagnostiku a hlášení chyb. Bez SLC by síť nemohla rozlišit mezi více fyzickými nebo logickými spojeními mezi stejnými dvěma uzly.

Historicky je jeho definice nedílnou součástí standardů SS7 přijatých 3GPP pro jádrové sítě s přepojováním okruhů. Řešila omezení konfigurací s jedním spojem tím, že umožnila robustní architekturu linksetu. Tato architektura je klíčová pro dostupnost na úrovni operátora, protože umožňuje automatické přesměrování provozu přes alternativní spoje v rámci stejného linksetu při selhání s minimálním narušením služeb. SLC je klíčovým prvkem tohoto vysoce dostupného návrhu.

## Klíčové vlastnosti

- Jednoznačně identifikuje signalizační spoj v rámci linksetu mezi dvěma signalizačními body
- Typicky 4bitové pole, umožňující až 16 spojů na linkset
- Používá se v MTP3 pro sdílení zátěže a alternativní směrování v rámci linksetu
- Nezbytný pro postupy aktivace, deaktivace a správy selhání spojů
- Jeho hodnota je koordinována během procedury počátečního zarovnání
- Zachován v IP adaptacích SIGTRAN (např. M3UA) pro zpětnou kompatibilitu

## Související pojmy

- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)
- [MTP – Message Transfer Part](/mobilnisite/slovnik/mtp/)

## Definující specifikace

- **TS 28.735** (Rel-19) — STN Interface NRM IRP Information Service
- **TS 32.742** (Rel-11) — STN NRM for Configuration Management

---

📖 **Anglický originál a plná specifikace:** [SLC na 3GPP Explorer](https://3gpp-explorer.com/glossary/slc/)
