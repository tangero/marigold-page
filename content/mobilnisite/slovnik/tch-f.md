---
slug: "tch-f"
url: "/mobilnisite/slovnik/tch-f/"
type: "slovnik"
title: "TCH/F – Traffic Channel / Full Rate"
date: 2025-01-01
abbr: "TCH/F"
fullName: "Traffic Channel / Full Rate"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tch-f/"
summary: "Základní GSM kanál pro přenos hovorů (traffic channel) pracující s plnou rychlostí, který přenáší řeč nebo data jednoho uživatele v rámci jedné fyzické časové štěrbiny na TDMA rámec. Představuje zákla"
---

TCH/F je standardní GSM kanál pro přenos hovorů (traffic channel) s plnou přenosovou rychlostí (full rate), který přenáší řeč nebo data jednoho uživatele v rámci jedné časové štěrbiny (timeslot) na rámec a slouží jako základní okruhově přepínaný (circuit-switched) přenosový kanál pro hlas.

## Popis

[TCH](/mobilnisite/slovnik/tch/)/F je logický kanál pro přenos hovorů v GSM systému, který pracuje s plnou rychlostí, což znamená, že zabírá jednu časovou štěrbinu v každém [TDMA](/mobilnisite/slovnik/tdma/) rámci na daném rádiovém kmitočtovém kanálu. Je primárním přenosovým kanálem pro okruhově přepínané hlasové a datové služby. Pro hlas tradičně přenášel řeč kódovanou GSM plnorychlostním (Full-Rate, [FR](/mobilnisite/slovnik/fr/)) řečovým kodekem, který pracoval s čistou přenosovou rychlostí 13 kbit/s. Hrubá přenosová rychlost kanálu je 22,8 kbit/s, přičemž rozdíl je využit pro kanálové kódování (konvoluční kódování pro ochranu proti chybám) a signalizaci v pásmu.

TCH/F je strukturován v rámci 26-rámcové TDMA multirámce. V této multirámci je 24 rámců využito pro uživatelský provoz (řeč nebo data), jeden rámec je přidělen pro pomalu přidružený řídicí kanál (Slow Associated Control Channel, [SACCH](/mobilnisite/slovnik/sacch/)), který přenáší pravidelné měřicí reporty a signalizaci, a jeden rámec je nevyužitý. Tato struktura zajišťuje, že řídicí informace nezbytné pro udržení hovoru (jako měření pro předání hovoru) jsou přenášeny spolu s uživatelskými daty bez nutnosti samostatného fyzického kanálu. Kanálové kódování aplikované na řečové rámce je navrženo tak, aby opravovalo chyby způsobené rádiovým kanálem, a využívá konvoluční kódy a prokládání přes více časových úseků (burstů) pro potlačení vlivu útlumu (fading).

Pro datové služby může být TCH/F využit pro přenos okruhově přepínaných dat rychlostí 9,6 kbit/s nebo nižší. V této konfiguraci jsou aplikovány různé schémata kanálového kódování pro ochranu datových bitů. TCH/F je po dobu trvání hovoru vždy asociován s vyhrazeným fyzickým zdrojem, podle paradigmatu okruhového přepojování. Jeho správa je klíčovou funkcí řadiče základnových stanic (Base Station Controller, [BSC](/mobilnisite/slovnik/bsc/)), který zajišťuje alokaci, správu a uvolňování prostředků TCH/F během sestavování hovoru, předání hovoru a jeho ukončení.

## K čemu slouží

[TCH](/mobilnisite/slovnik/tch/)/F byl vytvořen jako ústřední kanál pro přenos hovorů pro původní GSM systém za účelem poskytování digitální, okruhově přepínané hlasové telefonie. Před GSM trpěly analogové celulární systémy (jako NMT nebo AMPS) nízkou kvalitou hlasu, nedostatkem zabezpečení a neefektivním využitím spektra. TCH/F, ve spojení s GSM plnorychlostním kodekem, byl navržen tak, aby nabídl výrazné zlepšení: digitální kvalitu hlasu, vnitřní šifrovací schopnosti a strukturovaný [TDMA](/mobilnisite/slovnik/tdma/) přístup, který umožňoval více uživatelům sdílet jeden rádiový nosič.

Řešil základní problém vytvoření spolehlivé, vyhrazené komunikační cesty pro jednotlivého uživatele v digitální celulární síti. Označení 'plná rychlost' (full-rate) stanovilo základní jednotku spotřeby rádiových zdrojů pro jeden hlasový hovor. Tato jednoduchost byla klíčová pro počáteční plánování sítě, dimenzování a algoritmy předání hovoru. Zatímco pozdější vylepšení zavedla poloviční rychlost (half-rate) a adaptivní kodeky pro větší kapacitu, TCH/F zůstal referenčním bodem pro zaručenou kvalitu řeči a záložní možností, když pokročilejší kanály nebyly podporovány mobilní stanicí nebo síťovými podmínkami.

## Klíčové vlastnosti

- Zabírá jednu fyzickou časovou štěrbinu v každém TDMA rámci na přiděleném rádiovém kmitočtu.
- Slouží jako primární přenosový kanál pro okruhově přepínané hlasové služby (s využitím FR kodeku) a datové služby.
- Následuje strukturu 26-rámcové multirámce s 24 rámci pro provoz, 1 rámcem pro SACCH a 1 nevyužitým rámcem.
- Používá konvoluční kanálové kódování a prokládání pro ochranu řeči/dat proti přenosovým chybám.
- Poskytuje vyhrazené spojení s konstantní přenosovou rychlostí po dobu trvání hovoru.
- Tvoří základ pro správu rádiových zdrojů, včetně procedur předání hovoru a řízení výkonu.

## Související pojmy

- [TCH/AHS – Traffic Channel / Adaptive Multi-Rate Half Rate Speech](/mobilnisite/slovnik/tch-ahs/)
- [TCH-FS – Traffic Channel Full rate Speech](/mobilnisite/slovnik/tch-fs/)
- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)
- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [TCH/F na 3GPP Explorer](https://3gpp-explorer.com/glossary/tch-f/)
