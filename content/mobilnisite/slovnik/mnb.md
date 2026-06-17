---
slug: "mnb"
url: "/mobilnisite/slovnik/mnb/"
type: "slovnik"
title: "MNB – Macro NodeB"
date: 2025-01-01
abbr: "MNB"
fullName: "Macro NodeB"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mnb/"
summary: "Výkonná základnová stanice v síti 3G UMTS, poskytující pokrytí široké oblasti, typicky z věže nebo střechy. Tvoří primární vrstvu mobilní sítě a zpracovává provoz pro uživatele napříč rozsáhlými geogr"
---

MNB je výkonová základnová stanice 3G UMTS, která poskytuje pokrytí široké oblasti z věže nebo střechy a tvoří primární síťovou vrstvu pro uživatele napříč rozsáhlými geografickými oblastmi.

## Popis

Macro NodeB (MNB) je standardní, výkonná základnová stanice používaná v sítích 3G Universal Mobile Telecommunications System (UMTS). Je klíčovou součástí UMTS Terrestrial Radio Access Network (UTRAN). Architektonicky obsahuje rádiové transceivery, antény a jednotky pro zpracování základního pásma nezbytné pro komunikaci s uživatelským zařízením (UE) přes rozhraní vzduchu. Připojuje se k řadiči rádiové sítě (RNC) přes rozhraní Iub pomocí [ATM](/mobilnisite/slovnik/atm/) nebo IP přenosu. RNC poskytuje centralizovanou správu pro více NodeB, řídí funkce jako předávání hovoru (handover), správu rádiových zdrojů a šifrování. Samotný MNB je zodpovědný za zpracování fyzické vrstvy, včetně modulace/demodulace, kódování a vysílání/příjmu signálu Wideband Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (WCDMA).

Funguje tak, že vytváří jednu nebo více buněk, z nichž každá je definována specifickou kmitočtovou nosnou a primárním scrambling kódem. MNB vysílá společné pilotní kanály ([CPICH](/mobilnisite/slovnik/cpich/)), které UE měří pro výběr buňky a handover. Vytváří vyhrazené kanály pro jednotlivá uživatelská spojení a spravuje smyčky řízení výkonu nezbytné pro WCDMA k překonání problému blízký-vzdálený. MNB přijímá uživatelská data a signalizaci od RNC, zpracuje je do rádiových rámců a vysílá je přes rozhraní vzduchu. Naopak přijímá signály od UE, provádí RAKE kombinaci pro zpracování vícecestných signálů a posílá dekódovaná data zpět do RNC. Jeho vysoký vysílací výkon (typicky desítky wattů) a zvýšené umístění antény (na stožárech nebo budovách) jsou navrženy tak, aby poskytovaly pokrytí na velké ploše, často o poloměru několika kilometrů.

Jeho úlohou v síti je poskytovat základní vrstvu všudypřítomného pokrytí a kapacity. Makro buňky jsou pracovními koňmi sítě, navrženými pro kontinuální pokrytí v městských, příměstských a venkovských oblastech. Zpracovávají většinu mobilního provozu, zejména od rychle se pohybujících uživatelů. Síť je často plánována jako hierarchická struktura buněk ([HCS](/mobilnisite/slovnik/hcs/)), kde Macro NodeB poskytují zastřešující vrstvu pokrytí, doplněnou o nízkovýkonové mikro, piko a femtobuňky (Home NodeB) pro zvýšení kapacity a vnitřní pokrytí. Výkon a hustota nasazení MNB přímo určují celkovou kvalitu služeb a kapacitu sítě 3G.

## K čemu slouží

Macro NodeB byl vytvořen jako základní bod rádiového přístupu pro sítě 3G UMTS, navržený k poskytnutí pokrytí široké oblasti nezbytného pro celostátní mobilní službu. Řešil problém poskytování datových služeb s vyšší kapacitou a lepší kvality hovoru ve srovnání se sítěmi 2G GSM, které byly primárně optimalizovány pro přepojování okruhů hlasu. MNB, využívající technologii WCDMA, umožnil efektivnější využití rádiového spektra a podporoval vyšší datové rychlosti, což umožnilo rané služby mobilního internetu.

Jeho konstrukce s vysokým výkonem a velkou buňkou řešila ekonomickou a praktickou výzvu zavádění nové generace sítě. Nasazení menšího počtu výkonných stanic na existujících věžích bylo pro počáteční pokrytí nákladově efektivnější než nasazení husté sítě nízkovýkonových uzlů. Architektura MNB/RNC poskytla kontrolovanou migrační cestu ze sítě 2G, umožňující operátorům znovu využít stanoviště a přenosovou síť. Tento centralizovaný model RNC však také přinesl omezení v latenci a efektivitě, která pozdější generace (LTE a 5G) řešily přechodem na plošší architekturu s větší inteligencí v základnové stanici (eNodeB/gNB). MNB vytvořil model pro buněčné pokrytí, který je základem všech moderních sítí, i když se technologie uvnitř základnové stanice dramaticky vyvinula.

## Klíčové vlastnosti

- Vysoký vysílací výkon (např. 20W–40W na nosnou) pro pokrytí široké oblasti až o poloměru několika kilometrů
- Podpora rozhraní vzduchu WCDMA s proměnnými spreading faktory
- Provádění rychlé uzavřené smyčky řízení výkonu na příkaz od UE
- Připojení k řídicímu řadiči rádiové sítě (RNC) přes rozhraní Iub
- Podpora více buněk a sektorů (typicky konfigurace se 3 sektory)
- Vysílání společných kanálů (např. CPICH, P-CCPCH) pro vyhledávání buňky a systémové informace

## Definující specifikace

- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report

---

📖 **Anglický originál a plná specifikace:** [MNB na 3GPP Explorer](https://3gpp-explorer.com/glossary/mnb/)
