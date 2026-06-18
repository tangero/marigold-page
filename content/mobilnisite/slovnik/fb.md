---
slug: "fb"
url: "/mobilnisite/slovnik/fb/"
type: "slovnik"
title: "FB – Frequency correction Burst"
date: 2025-01-01
abbr: "FB"
fullName: "Frequency correction Burst"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fb/"
summary: "Specifický typ blesku v GSM používaný pro počáteční frekvenční synchronizaci mobilní stanice. Přenáší čistou sinusovku, aby umožnil mobilní stanici přesně upravit frekvenci svého lokálního oscilátoru"
---

FB je typ blesku v GSM, který vysílá čistou sinusovkou pro počáteční frekvenční synchronizaci, což umožňuje mobilní stanici upravit svůj oscilátor na nosnou frekvenci základnové stanice pro následnou demodulaci.

## Popis

Frekvenční korekční blesk (Frequency correction Burst, FB) je základní signál fyzické vrstvy v systému GSM, definovaný v rámci struktury [TDMA](/mobilnisite/slovnik/tdma/) rámce. Je jedním z pěti standardních typů blesků a je vysílán výhradně na frekvenčním korekčním kanálu ([FCCH](/mobilnisite/slovnik/fcch/)). FB se skládá ze 148 bitů, které jsou všechny nastaveny na binární nulu. Při modulaci pomocí [GMSK](/mobilnisite/slovnik/gmsk/) (Gaussian Minimum Shift Keying) tento specifický bitový vzor vytváří čistou nemodulovanou sinusovku s pevnou frekvenční odchylkou od nominální vysokofrekvenční nosné. Tato odchylka je přesně 67,7 kHz nad nosnou frekvencí. Primární funkcí tohoto blesku je poskytnout absolutní frekvenční referenci.

Když se mobilní stanice ([MS](/mobilnisite/slovnik/ms/)) zapne nebo vstoupí do nové buňky, musí provést vyhledávání buňky a synchronizaci. MS prohledává vysokofrekvenční kanály a hledá tento charakteristický signál s konstantní frekvencí. Po jeho detekci může MS změřit rozdíl mezi přijímanou frekvencí a frekvencí svého vlastního interního oscilátoru. Následně použije toto měření k aplikaci korekce, čímž sladí svou lokální frekvenční referenci s referencí základnové přenosové stanice ([BTS](/mobilnisite/slovnik/bts/)). Tento proces je zásadní, protože demodulace GMSK je vysoce citlivá na frekvenční chyby; přesná frekvenční synchronizace je nezbytným předpokladem pro úspěšný příjem synchronizačního kanálu ([SCH](/mobilnisite/slovnik/sch/)) a následné dekódování vysílacího řídicího kanálu ([BCCH](/mobilnisite/slovnik/bcch/)).

FB je vysílán ve specifických časových slotech v rámci více-rámcové struktury GSM podle předvídatelného vzoru. V 51-rámcovém více-rámci řídicích kanálů je FCCH (nesoucí FB) vysílán v časovém slotu 0 určitých rámců, prokládaně se SCH a BCCH. Opakovaný přenos umožňuje MS nejen získat, ale také sledovat frekvenční drift v čase. Konstrukce FB – jednoduchý, vysoko-výkonný, konstantní tón – jej činí robustním a snadno detekovatelným i v nepříznivých podmínkách signálu, což zajišťuje spolehlivý počáteční přístup k síti. Jeho funkce je úhelným kamenem rádiového rozhraní GSM a umožňuje efektivní a spolehlivou mobilitu, která je pro tento systém charakteristická.

## K čemu slouží

Frekvenční korekční blesk byl vytvořen k řešení základního problému rychlé a přesné frekvenční synchronizace v digitálním celulárním [TDMA](/mobilnisite/slovnik/tdma/) systému, jakým je GSM. V raných celulárních systémech bylo frekvenční sladění méně kritické nebo používalo jiné metody. Použití GMSK modulace v GSM v kombinaci s potřebou rychlého připojování mobilních zařízení k buňkám při pohybu vyžadovalo jednoduchý, jednoznačný signál, který by bylo možné detekovat s minimálním zpracováním. FB toto poskytuje tím, že je spektrálně čistým referenčním tónem.

Bez takového vyhrazeného signálu by mobil musel provádět složitější a časově náročnější odhad frekvence naslepo založený na modulovaném provozu, což by zvýšilo spotřebu energie a zpozdilo sestavení hovoru nebo převzetí buňky. FB umožňuje mobilu velmi rychle zamknout svůj frekvenční syntezátor na referenci sítě, což je proces nezbytný před započetím jakékoli komunikace. Řeší praktická omezení levných krystalových oscilátorů v mobilních zařízeních, které mohou mít významný frekvenční drift způsobený teplotou a stárnutím, tím, že poskytuje korekční signál odvozený od sítě. Tato konstrukce byla motivována potřebou robustního, nízkokomplexního vstupního bodu do rámcové struktury GSM, který by umožnil efektivní sériovou výrobu koncových zařízení a spolehlivý provoz sítě.

## Klíčové vlastnosti

- Generuje čistou sinusovku s pevnou odchylkou 67,7 kHz od vysokofrekvenční nosné
- Používá předdefinovaný 148bitový vzor složený ze samých nul pro modulaci GMSK
- Vysílán výhradně na frekvenčním korekčním kanálu (FCCH)
- Umožňuje korekci a synchronizaci frekvence oscilátoru mobilní stanice
- Umístěn ve specifických rámcích v rámci 51-rámcové struktury více-rámce řídicích kanálů
- Poskytuje robustní referenční signál s vysokým výkonem pro počáteční vyhledávání buňky

## Související pojmy

- [FCCH – Frequency Correction Channel](/mobilnisite/slovnik/fcch/)
- [SCH – Synchronization Channel](/mobilnisite/slovnik/sch/)
- [GMSK – Gaussian Minimum Shift Keying](/mobilnisite/slovnik/gmsk/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 26.103** (Rel-19) — 3GPP Codec Lists for OoBTC and TrFO
- **TR 26.996** (Rel-19) — ISAR Split Rendering Audio Characterization

---

📖 **Anglický originál a plná specifikace:** [FB na 3GPP Explorer](https://3gpp-explorer.com/glossary/fb/)
