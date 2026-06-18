---
slug: "win"
url: "/mobilnisite/slovnik/win/"
type: "slovnik"
title: "WIN – Wireless Intelligent Network"
date: 2025-01-01
abbr: "WIN"
fullName: "Wireless Intelligent Network"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/win/"
summary: "Wireless Intelligent Network (WIN) je servisní architektura umožňující pokročilé, inteligentní telekomunikační služby v bezdrátových sítích. Poskytuje rámec pro tvorbu, nasazení a provoz služeb odděle"
---

WIN je servisní architektura, která umožňuje pokročilé, inteligentní telekomunikační služby v bezdrátových sítích oddělením servisní logiky od základní přepínací infrastruktury.

## Popis

Wireless Intelligent Network (WIN) je standardizovaná architektura, která zavádí inteligenci do bezdrátových sítí oddělením servisní logiky od základních funkcí řízení hovorů a spojení. Vychází z konceptu Inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) přizpůsobeného pro mobilní prostředí. Základní princip spočívá v použití vyhrazených síťových uzlů, jako jsou Service Control Points ([SCP](/mobilnisite/slovnik/scp/)), které obsahují servisní logiku, a Service Switching Points ([SSP](/mobilnisite/slovnik/ssp/)) v rámci Mobile Switching Centers ([MSC](/mobilnisite/slovnik/msc/)), které detekují spouštěče služeb a komunikují s SCP. Toto oddělení umožňuje centralizované řízení a správu služeb.

Architektonicky WIN definuje sadu spouštěčů, známých jako Detection Points ([DP](/mobilnisite/slovnik/dp/)), vestavěných do Basic Call State Model ([BCSM](/mobilnisite/slovnik/bcsm/)) MSC/SSP. Když událost hovoru odpovídá nakonfigurovanému spouštěči, SSP pozastaví zpracování hovoru a odešle dotaz, typicky pomocí signalizačního protokolu ANSI-41 (nebo později 3GPP2), na SCP. SCP provede servisní logiku, učiní rozhodnutí (např. zkontroluje stav předplaceného účtu, aplikuje screening hovorů) a vrátí instrukce SSP, jak s hovorem pokračovat. Tato interakce je standardizována prostřednictvím WIN protokolů a Application Programming Interfaces ([API](/mobilnisite/slovnik/api/)).

Klíčové komponenty zahrnují SCP, SSP, Intelligent Peripheral (IP) pro specializované zdroje, jako jsou hlasové hlášky, a Service Management System ([SMS](/mobilnisite/slovnik/sms/)) pro provozní správu. WIN podporuje služby jako Wireless Prepaid, Voice Controlled Services, Calling Name Presentation a Location-Based Charging. Jeho úlohou je poskytovat flexibilní, na dodavateli nezávislou platformu pro nasazování přidaných služeb bez nutnosti rozsáhlých upgradů každého přepínače v síti, čímž se zkracuje doba uvedení nových nabídek na trh a umožňuje personalizované zkušenosti účastníků.

## K čemu slouží

WIN byl vytvořen, aby řešil omezení tradičních bezdrátových sítí, kde byla servisní logika těsně integrována a pevně zakódována do jednotlivých přepínacích systémů. To činilo zavádění nových služeb pomalým, nákladným a složitým, protože vyžadovalo softwarové upgrady na četných síťových prvcích. Primární motivací bylo umožnit rychlou tvorbu a nasazení služeb v konkurenčním prostředí, což operátorům dovoluje diferencovat své nabídky a zvyšovat průměrný výnos na uživatele (ARPU).

Historicky se vyvinul z pevných standardů Inteligentní sítě (IN), přičemž adaptoval koncepty jako Intelligent Network Application Part (INAP) pro specifické potřeby severoamerických celulárních sítí založených na ANSI-41/TIA/EIA-41 (AMPS, TDMA, CDMA). Řešil problém přenositelnosti služeb a interoperability napříč sítěmi více dodavatelů. Standardizací servisní architektury a rozhraní mezi přepínacími a řídicími funkcemi WIN umožnil operátorům získávat aplikace servisní logiky od jiných dodavatelů než jsou dodavatelé jejich přepínačů, což podporovalo inovace a konkurenci ve vrstvě služeb.

## Klíčové vlastnosti

- Oddělení servisní logiky od přepínací infrastruktury
- Standardizovaný model detekce spouštěčů a řízení hovorů (BCSM)
- Centralizované řízení služeb prostřednictvím Service Control Points (SCP)
- Podpora pokročilých služeb, jako jsou předplacené a služby založené na poloze
- Využití Intelligent Peripherals pro specializované zdroje
- Standardizované signalizační protokoly (např. rozšíření ANSI-41 WIN)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [WIN na 3GPP Explorer](https://3gpp-explorer.com/glossary/win/)
