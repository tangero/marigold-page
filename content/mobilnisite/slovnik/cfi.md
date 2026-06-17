---
slug: "cfi"
url: "/mobilnisite/slovnik/cfi/"
type: "slovnik"
title: "CFI – Control Format Indicator"
date: 2025-01-01
abbr: "CFI"
fullName: "Control Format Indicator"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cfi/"
summary: "Control Format Indicator (CFI) je pole v Physical Control Format Indicator Channel (PCFICH) v LTE a NR. Dynamicky signalizuje počet OFDM symbolů přidělených Physical Downlink Control Channel (PDCCH) v"
---

CFI je pole v kanálu PCFICH, které dynamicky signalizuje počet OFDM symbolů přidělených kanálu PDCCH v podrámci, což umožňuje flexibilní alokaci zdrojů.

## Popis

Control Format Indicator (CFI) je základním prvkem architektury downlinkového řídicího signalizování v 3GPP LTE ([E-UTRA](/mobilnisite/slovnik/e-utra/)) a NR (New Radio). Přenáší se na Physical Control Format Indicator Channel (PCFICH), což je fyzický kanál speciálně navržený pro přenos této informace. Hodnota CFI, typicky 1, 2 nebo 3 (nebo 4 v určitých konfiguracích NR), explicitně udává počet Orthogonal Frequency Division [Multiplexing](/mobilnisite/slovnik/multiplexing/) ([OFDM](/mobilnisite/slovnik/ofdm/)) symbolů na začátku podrámce, které jsou obsazeny Physical Downlink Control Channel ([PDCCH](/mobilnisite/slovnik/pdcch/)). Tato oblast je známa jako řídicí oblast. Zbývající symboly v podrámci jsou pak k dispozici pro Physical Downlink Shared Channel ([PDSCH](/mobilnisite/slovnik/pdsch/)), který nese uživatelská data a signalizaci vyšších vrstev.

PCFICH je mapován na konkrétní Resource Elements (RE) v prvním OFDM symbolu každého downlinkového podrámce, což zajišťuje, že je jednou z prvních informací, kterou User Equipment (UE) dekóduje. UE musí úspěšně dekódovat CFI, aby vědělo, kde řídicí oblast končí a kde začíná oblast dat. Tento dekódovací proces zahrnuje odhad kanálu, demodulaci a interpretaci zakódovaných bitů CFI. Umístění PCFICH v rámci prvního symbolu je specifické pro buňku a odvozuje se z identity fyzické buňky, což pomáhá zmírnit mezibuněčné rušení tohoto kritického signálu.

Z architektonického hlediska umožňuje CFI dynamické přizpůsobování poměru zdrojů mezi řídicí a datovou oblastí na bázi jednotlivých podrámců. eNodeB (v LTE) nebo gNB (v NR) určuje potřebnou velikost řídicí oblasti na základě okamžitých faktorů, jako je počet plánovaných UE, typ řídicích informací (např. plánovací povolení, příkazy pro řízení výkonu uplinku) a použití funkcí jako agregace nosných nebo [MIMO](/mobilnisite/slovnik/mimo/). Následně zakóduje příslušnou hodnotu CFI a přenese ji na PCFICH. Tato dynamická alokace je klíčovým mechanismem efektivity, který zabraňuje tomu, aby byla řídicí oblast staticky předimenzovaná (plýtvání datovou kapacitou) nebo poddimenzovaná (neschopnost naplánovat všechny potřebné UE).

Role CFI přímo zasahuje do procedur a výkonu fyzické vrstvy. Nesprávné dekódování CFI by vedlo k tomu, že by UE špatně interpretovalo celou strukturu podrámce, což by mělo za následek nepřijetí jeho downlinkových řídicích informací ([DCI](/mobilnisite/slovnik/dci/)) a následnou ztrátu plánovaných dat. Proto je PCFICH navržen pro robustnost s využitím modulace QPSK a 32bitového kódového slova (16 bitů v NR) mapovaného na distribuované RE. CFI je vnitřně propojeno s dalšími řídicími kanály, jako je Physical [HARQ](/mobilnisite/slovnik/harq/) Indicator Channel (PHICH), jehož délka je také vázána na hodnotu CFI. V pozdějších vydáních, se zavedením vylepšeného PDCCH (EPDCCH) a flexibilnějších sad řídicích zdrojů (CORESETs) v NR, základní princip signalizace velikosti řídicí oblasti zůstává, ačkoli konkrétní mechanismy se vyvíjely.

## K čemu slouží

Control Format Indicator byl vytvořen k řešení problému rigidního a neefektivního dělení mezi řídicími a datovými zdroji v downlinku celulárních systémů. Před LTE často řídicí signalizace zabírala pevné, předdefinované části rámce, které se nemohly přizpůsobit okamžitým síťovým podmínkám. To vedlo k situacím, kdy byla řídicí oblast nevyužitá (plýtvání cennými spektrálními zdroji, které mohly nést uživatelská data), nebo se stala úzkým hrdlem při vysokém síťovém provozu, což omezovalo počet uživatelů, které bylo možné současně naplánovat.

Zavedení CFI v LTE Rel-8 bylo klíčovou inovací umožňující dynamické sdílení zdrojů. Jeho účelem je poskytnout UE nezbytnou informaci potřebnou ke správnému rozboru každého podrámce, což přímo podporuje paketově přepínané dynamické plánování, které je ústřední pro vysoký výkon LTE a NR. Tím, že umožňuje síti upravovat velikost řídicí oblasti na bázi jednotlivých podrámců (od 1 do 3 OFDM symbolů a později až 4 v určitých případech NR), systém dosahuje mnohem vyšší spektrální efektivity a flexibility. Tato přizpůsobivost je klíčová pro zvládání různorodých vzorců provozu, od několika uživatelů s velkými datovými pakety až po mnoho uživatelů s malými pakety, a pro podporu pokročilých funkcí, jako je multimedia broadcast multicast service (MBMS), kde může být velikost řídicí oblasti v určitých podrámcích snížena.

Historicky byla motivací opustit přístup založený na přepojování okruhů a přijmout plně IP a vysoce plánovanou povahu 4G a 5G. CFI je základní komponentou, která tuto efektivní plánovatelnost umožňuje. Řeší omezení statického dělení tím, že dává síti kontrolu nad kompromisem mezi režií řízení a datovou kapacitou pro každý přenosový časový interval (TTI), a optimalizuje tak výkon v reálném čase na základě skutečné poptávky.

## Klíčové vlastnosti

- Dynamicky signalizuje velikost (1–4 OFDM symbolů) downlinkové řídicí oblasti (PDCCH) pro každý podrámec
- Přenášen na vyhrazeném Physical Control Format Indicator Channel (PCFICH) v prvním OFDM symbolu
- Umožňuje efektivní a flexibilní využití spektra díky vyvažování režie řízení a datové kapacity
- Nezbytný pro UE ke správnému dekódování Physical Downlink Control Channel (PDCCH) a nalezení datové oblasti (PDSCH)
- Pro spolehlivý příjem používá robustní kanálové kódování (32bitové kódové slovo v LTE) a modulaci QPSK
- Specifické mapování pro buňku založené na identitě fyzické buňky pro minimalizaci mezibuněčného rušení

## Související pojmy

- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [PDSCH – Physical Downlink Shared Channel](/mobilnisite/slovnik/pdsch/)

## Definující specifikace

- **TS 27.002** (Rel-19) — Terminal Adaptation Functions for Asynchronous Services
- **TS 36.212** (Rel-19) — LTE Multiplexing and Channel Coding
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TR 36.976** (Rel-19) — LTE-based 5G Terrestrial Broadcast Overview
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study

---

📖 **Anglický originál a plná specifikace:** [CFI na 3GPP Explorer](https://3gpp-explorer.com/glossary/cfi/)
