---
slug: "siwf"
url: "/mobilnisite/slovnik/siwf/"
type: "slovnik"
title: "SIWF – Shared Inter Working Function"
date: 2025-01-01
abbr: "SIWF"
fullName: "Shared Inter Working Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/siwf/"
summary: "Síťová funkce v raných vydáních 3GPP (Rel-4/5), která poskytovala sdílené propojení mezi jádrovou sítí s přepojováním okruhů (CS) a externími sítěmi, jako je PSTN. Umožňovala efektivní sdílení prostře"
---

SIWF je síťová funkce v raných vydáních 3GPP, která poskytovala sdílené propojení (interworking) mezi jádrem s přepojováním okruhů a externími sítěmi, což umožňovalo efektivní sdílení prostředků pro signalizaci a převod médií.

## Popis

Shared Inter Working Function (SIWF, sdílená funkce pro vzájemné propojení) byl prvek jádrové sítě představený ve 3GPP Release 4 jako součást evoluce směrem k plně IP jádru. Z architektonického hlediska se nacházel v doméně s přepojováním okruhů ([CS](/mobilnisite/slovnik/cs/)) a fungoval jako sdílená brána nebo mediační bod. Jeho primární rolí bylo zajišťovat vzájemné propojení mezi mobilní CS doménou a různými externími sítěmi, především veřejnou telefonní komutovanou sítí ([PSTN](/mobilnisite/slovnik/pstn/)) a dalšími staršími telefonními systémy. Na rozdíl od vyhrazených propojovacích jednotek u každého [MSC](/mobilnisite/slovnik/msc/) byl SIWF navržen jako sdružený prostředek, obsluhující více ústředen mobilního přepojování (MSC) nebo mediálních bran ([MGW](/mobilnisite/slovnik/mgw/)) v rámci sítě. Tento sdílený model představoval klíčový architektonický posun.

Provozně SIWF řídil dvě kritické oblasti: signalizaci a převod přenosu uživatelské roviny. Pro signalizaci překládal mezi mobilními signalizačními protokoly (jako BICC nebo [SIP-I](/mobilnisite/slovnik/sip-i/) používané v jádru) a starším signalizačním protokolem [ISUP](/mobilnisite/slovnik/isup/) převládajícím v PSTN. V případě uživatelské roviny zajišťoval převod hlasového provozu mezi paketovým přenosem (např. přes IP nebo [ATM](/mobilnisite/slovnik/atm/)) používaným v jádru 3GPP a tradičními [TDM](/mobilnisite/slovnik/tdm/) (Time-Division Multiplexing) okruhy PSTN. To zahrnovalo transkódování kodeků a adaptaci přenosových protokolů.

Implementace SIWF byla úzce spojena s oddělením řídicí a uživatelské roviny prosazovaným ve Release 4. Mohla být nasazena jako samostatný uzel, nebo její funkce mohly být integrovány do mediální brány. Díky centralizaci propojovacích schopností umožňovala síťovým operátorům zjednodušit topologii jádrové sítě, snížit počet síťových rozhraní vyžadujících správu a dosáhnout úspor z rozsahu. Její sdílená povaha znamenala nižší kapitálové a provozní náklady ve srovnání s nasazením propojovacích funkcionalit na každém místě MSC, což usnadňovalo nákladově efektivnější migrační cestu ze starších TDM jader k paketovým sítím nové generace (NGN).

## K čemu slouží

SIWF byla vytvořena, aby řešila výzvy a náklady spojené s přechodem od tradičních mobilních sítí s přepojováním okruhů k architekturám s přepojováním paketů na počátku 21. století. Před Release 4 bylo propojení s PSTN typicky zajišťováno vyhrazenou funkcionalitou v rámci každé ústředny mobilního přepojování (MSC), což vedlo k duplikaci zařízení a neefektivnímu využití prostředků v celé síti. Když operátoři začali nasazovat páteřní sítě založené na paketech (pomocí IP nebo ATM), vznikla potřeba efektivnější brány pro propojení starého a nového světa.

Primární problém, který řešila, bylo umožnění bezproblémové komunikace hlasu a signalizace mezi vznikajícím paketovým jádrem 3GPP a všudypřítomnou, zavedenou PSTN, aniž by to vyžadovalo masivní a současnou přestavbu celé síťové infrastruktury. Vytvořením sdíleného, centralizovaného prostředku pro vzájemné propojení poskytlo 3GPP pragmatický migrační nástroj. Snížilo náklady a složitost zavádění mediálních bran s přepojováním paketů (MGW) a funkcí řízení stavu hovoru (CSCF) tím, že jim umožnilo připojit se ke společnému SIWF pro veškerý provoz se starší PSTN. Tento přístup snížil překážky pro přijetí nových síťových architektur a podpořil strategický posun odvětví směrem k plně IP sítím.

## Klíčové vlastnosti

- Architektura sdíleného prostředku obsluhujícího více MSC nebo mediálních bran
- Signalizační propojení mezi protokoly BICC/SIP-I a starším protokolem ISUP
- Převod médií v uživatelské rovině mezi paketovými (IP/ATM) a TDM okruhy
- Centralizovaný bod pro transkódování kodeků a adaptaci přenosu
- Podpora konceptu oddělení řídicí a uživatelské roviny z Release 4
- Snižuje složitost sítě a náklady na propojení s PSTN

## Související pojmy

- [PSTN – Public Switched Telecommunications Network](/mobilnisite/slovnik/pstn/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain

---

📖 **Anglický originál a plná specifikace:** [SIWF na 3GPP Explorer](https://3gpp-explorer.com/glossary/siwf/)
