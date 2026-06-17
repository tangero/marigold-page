---
slug: "aau"
url: "/mobilnisite/slovnik/aau/"
type: "slovnik"
title: "AAU – Active Antenna Unit"
date: 2025-01-01
abbr: "AAU"
fullName: "Active Antenna Unit"
category: "Radio Access Network"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/aau/"
summary: "Aktivní anténní jednotka (AAU) je rádiový vysílač-přijímač, který integruje aktivní rádiové komponenty, jako jsou výkonové zesilovače a šumově nízké zesilovače, přímo s anténními prvky. Umožňuje pokro"
---

AAU je rádiový vysílač-přijímač, který integruje aktivní rádiové komponenty a anténní prvky, aby umožnil pokročilé formování svazku a massive MIMO pro zlepšený výkon v sítích 4G a 5G.

## Popis

Aktivní anténní jednotka (AAU) představuje zásadní architektonický posun v návrhu rádiové přístupové sítě tím, že integruje aktivní vysokofrekvenční (RF) komponenty přímo s pasivními anténními prvky do jedné fyzické jednotky. Na rozdíl od tradičních architektur základnových stanic, kde jsou vzdálené rádiové hlavice (RRH) a pasivní antény samostatné komponenty propojené koaxiálními kabely, AAU kombinuje výkonové zesilovače, šumově nízké zesilovače, vysílače-přijímače a anténní prvky v integrovaném balení. Tato integrace odstraňuje potřebu napájecích kabelů mezi rádiovou jednotkou a anténou, což výrazně snižuje ztráty signálu, které jsou typické pro tradiční nasazení.

V jádru AAU obsahuje více přijímacích/vysílacích řetězců, z nichž každý se skládá z digitálně-analogových převodníků (DAC), analogově-digitálních převodníků (ADC), výkonových zesilovačů (PA), šumově nízkých zesilovačů (LNA), filtrů a anténních prvků. Tyto komponenty jsou uspořádány v těsně integrované architektuře, která umožňuje přesné řízení fáze a amplitudy každého anténního prvku. AAU se připojuje k základnové jednotce (BBU) nebo distribuované jednotce (DU) prostřednictvím vysokorychlostních optických rozhraní za použití protokolů jako Common Public Radio Interface (CPRI) nebo enhanced CPRI (eCPRI), které přenášejí digitalizované základnové pásmové signály mezi zpracovatelskou jednotkou a rádiovou jednotkou.

Architektura AAU umožňuje pokročilé anténní technologie včetně formování svazku a massive Multiple-Input Multiple-Output (MIMO). Řízením fáze a amplitudy signálů na každém anténním prvku může AAU elektronicky směrovat rádiové svazky bez fyzického pohybu antény. Tato schopnost je zvláště důležitá pro milimetrové vlny (mmWave) v 5G, kde je formování svazku nezbytné pro překonání vysoké útlumové ztráty. AAU také podporuje vícepásmový provoz, což umožňuje, aby jedna jednotka současně vysílala a přijímala napříč více kmitočtovými pásmy, což zjednodušuje nasazení na lokalitě a snižuje množství zařízení.

Při provozu AAU přijímá digitalizované základnové pásmové signály z BBU/DU, převádí je na analogové RF signály, zesiluje je a vysílá prostřednictvím integrovaného anténního pole. Na straně příjmu zachycuje signály prostřednictvím anténních prvků, zesiluje je pomocí LNA, převádí je do digitálního formátu a odesílá zpět do BBU/DU pro další zpracování. Integrace aktivních komponent s anténami umožňuje přesnější kalibraci a řízení, což vede ke zlepšené kvalitě signálu, sníženému rušení a lepšímu celkovému výkonu sítě ve srovnání s tradičními oddělenými architekturami.

## K čemu slouží

AAU byla vyvinuta k řešení několika omezení tradičních architektur základnových stanic, kde byly rádiové jednotky a antény samostatné komponenty. V konvenčních nasazeních se rádiová jednotka (často implementovaná jako vzdálená rádiová hlavice) připojuje k pasivním anténám prostřednictvím koaxiálních napájecích kabelů, které způsobují významné ztráty signálu, zejména na vyšších kmitočtech. Tyto ztráty snižují efektivitu sítě, zvyšují spotřebu energie a omezují praktické nasazení pokročilých anténních technologií. AAU tyto napájecí ztráty eliminuje integrací aktivních komponent přímo s anténními prvky, což vede ke zlepšené energetické účinnosti a lepší kvalitě signálu.

Dalším klíčovým motivem pro vývoj AAU byla potřeba podpory pokročilých anténních technologií vyžadovaných pro sítě 4G LTE-Advanced a 5G. Technologie jako formování svazku a massive MIMO vyžadují přesné řízení jednotlivých anténních prvků, což je obtížné dosáhnout s oddělenými rádiovými a anténními komponentami kvůli fázovým nekonzistencím v napájecích kabelech. Integrovaný návrh AAU umožňuje přesnější kalibraci a řízení anténních prvků, což umožňuje implementaci sofistikovaných algoritmů formování svazku, které dynamicky směrují rádiové svazky k uživatelům, čímž zlepšují pokrytí a kapacitu.

AAU také řeší praktické výzvy nasazení tím, že snižuje prostorové nároky na lokalitě a zjednodušuje instalaci. Tradiční lokality základnových stanic vyžadují samostatné skříně pro rádiové zařízení, napájecí kabely vedené na věže a velká anténní pole. AAU konsoliduje tyto komponenty do jediné jednotky, kterou lze namontovat přímo na místo antény, čímž se snižuje větrné zatížení, požadavky na prostor na věži a složitost instalace. Tento integrovaný přístup se stal stále důležitějším, jak se sítě vyvíjely k podpoře vyšších kmitočtových pásem a více anténních prvků, kde by se tradiční architektury staly nepraktickými kvůli kabelovým ztrátám a fyzickým omezením.

## Klíčové vlastnosti

- Integrované aktivní RF komponenty s anténními prvky
- Podpora pokročilého formování svazku a massive MIMO
- Eliminace ztrát v napájecích kabelech mezi rádiovou jednotkou a anténou
- Schopnost vícepásmového provozu
- Vysokorychlostní optické rozhraní k základnové jednotce
- Podpora provozu v pásmu milimetrových vln

## Definující specifikace

- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TS 34.114** (Rel-12) — Radiated Performance Test Procedure for UE/MS
- **TS 37.544** (Rel-16) — UE Radiated Performance Test Procedures
- **TR 38.864** (Rel-18) — Technical Report on Network Energy Savings for NR

---

📖 **Anglický originál a plná specifikace:** [AAU na 3GPP Explorer](https://3gpp-explorer.com/glossary/aau/)
