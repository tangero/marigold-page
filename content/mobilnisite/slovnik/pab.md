---
slug: "pab"
url: "/mobilnisite/slovnik/pab/"
type: "slovnik"
title: "PAB – Phase Alignment Bit"
date: 2025-01-01
abbr: "PAB"
fullName: "Phase Alignment Bit"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pab/"
summary: "Phase Alignment Bit (PAB) je řídicí bit používaný v přenosových sítích založených na TDM, zejména pro okruhově spínaná spojení jako jsou linky E1/T1. Zajišťuje správné fázové zarovnání datových rámců"
---

PAB je řídicí bit používaný v přenosových sítích založených na TDM k zajištění správného fázového zarovnání datových rámců mezi síťovými prvky pro synchronizaci časování.

## Popis

Phase Alignment Bit (PAB) je základní součástí rámcové struktury fyzické vrstvy přenosových rozhraní s časovým multiplexem ([TDM](/mobilnisite/slovnik/tdm/)), jako jsou linky E1 (2,048 Mbps) a T1 (1,544 Mbps), které se běžně používají v legacy okruhově spínaných mobilních sítích (např. pro připojení rozhraní Abis nebo A). Funguje na úrovni bitu v rámci signálu zarovnání rámce (frame alignment signal) struktury TDM rámce. Primární technickou funkcí PAB je poskytnout známý, pevný referenční bod v opakujícím se rámcovém vzoru, což umožňuje přijímacímu zařízení správně identifikovat začátek každého rámce a následně demultiplexovat jednotlivé časové sloty nesoucí uživatelský provoz a signalizaci.

Z architektonického hlediska je PAB vložen do slova nebo vzoru pro zarovnání rámce definovaného doporučeními [ITU-T](/mobilnisite/slovnik/itu-t/) G.704 (pro E1) a G.704 (pro T1/J1). Ve standardním E1 rámci o 256 bitech (32 časových slotů po 8 bitech) zabírá signál zarovnání rámce specifické bitové pozice v střídajících se rámcích. Hodnota PAB je v tomto vzoru nastavena na předem stanovený stav (např. '1'). Přijímací zařízení kontinuálně monitoruje příchozí bitový proud a vyhledává tento specifický vzor. Po jeho detekci uzamkne svůj interní hodinový signál a rámcovací obvody na tento vzor, čímž dosáhne 'zarovnání rámce'. Tento proces je kontinuální, aby kompenzoval časový drift.

Jeho role v síti je pro synchronizaci klíčová. Bez správného fázového zarovnání by přijímač nesprávně interpretoval hranice časových slotů, což by vedlo k masivním bitovým chybám, zkomoleným hlasovým hovorům a neúspěšným signalizačním zprávám. V kontextech 3GPP je PAB relevantní pro přenos okruhově spínaného přenosu a signalizace v sítích GSM a raných sítích UMTS, kde je použit TDM přenos. Specifikace 48.061 podrobně popisuje jeho aplikaci pro rozhraní Ater a Abis v systému základnových stanic ([BSS](/mobilnisite/slovnik/bss/)). PAB je nízkourovňový, hardware orientovaný mechanismus, který zajišťuje integritu fyzické vrstvy předtím, než vyšší vrstvy mohou data zpracovat.

## K čemu slouží

Phase Alignment Bit existuje, aby řešil základní problém synchronizace přijímače s vysílačem v synchronních digitálních přenosových systémech. V [TDM](/mobilnisite/slovnik/tdm/) sítích jsou data přenášena jako kontinuální, nepřerušovaný proud bitů rozdělený do opakujících se rámců. Přijímač musí přesně vědět, kde každý rámec začíná, aby mohl správně extrahovat 64 kbps kanály (časové sloty) v něm obsažené. Bez spolehlivého a konzistentně vysílaného signálu zarovnání by přijímač mohl ztratit synchronizaci, což by způsobilo stav 'mimo rámec' (out-of-frame), který naruší všechny přenášené služby.

Historicky byl tento problém řešen již v nejstarších digitálních přenosových systémech definovaných [ITU-T](/mobilnisite/slovnik/itu-t/). PAB jako součást signálu zarovnání rámce poskytuje jednoduchou, robustní a vpásmovou metodu pro dosažení a udržení zarovnání rámce. Řeší omezení čistě hodinové rekonstrukce, kde lze časování hodin extrahovat z přechodů na lince, ale struktura rámce zůstává neznámá. Pevný vzor obsahující PAB dává přijímači specifický 'orientační bod', který může vyhledávat, což umožňuje rychlé počáteční zarovnání a kontinuální ověřování během provozu. Jeho vznik byl motivován potřebou spolehlivého digitálního propojování v telefonních sítích, což byl požadavek, který se přímo přenesl do přenosových segmentů raných celulárních sítí specifikovaných 3GPP.

## Klíčové vlastnosti

- Poskytuje vpásmovou signalizaci zarovnání rámce pro TDM rozhraní (E1/T1)
- Vložen do pevného, opakujícího se bitového vzoru pro spolehlivou detekci
- Umožňuje synchronizaci přijímače na hranice rámců vysílače
- Podporuje kontinuální monitorování zarovnání pro kompenzaci časového driftu
- Základní pro bezchybné demultiplexování časových slotů
- Specifikováno v 3GPP TS 48.061 pro přenos rozhraní Ater a Abis

## Definující specifikace

- **TS 48.061** (Rel-19) — BTS-TRAU Protocol for HR Speech/Data

---

📖 **Anglický originál a plná specifikace:** [PAB na 3GPP Explorer](https://3gpp-explorer.com/glossary/pab/)
