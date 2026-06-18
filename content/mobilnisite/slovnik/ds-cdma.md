---
slug: "ds-cdma"
url: "/mobilnisite/slovnik/ds-cdma/"
type: "slovnik"
title: "DS-CDMA – Direct-Sequence Code Division Multiple Access"
date: 2025-01-01
abbr: "DS-CDMA"
fullName: "Direct-Sequence Code Division Multiple Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ds-cdma/"
summary: "Metoda mnohonásobného přístupu se spektrálním rozprostřením (spread spectrum), při které jsou uživatelská data vynásobena vysokorychlostním pseudonáhodným kódem, čímž se rozprostře šířka pásma signálu"
---

DS-CDMA je základní rádiové rozhraní (air interface) pro 3G UMTS, při kterém jsou uživatelská data vynásobena vysokorychlostním pseudonáhodným kódem, čímž se rozprostře šířka pásma signálu a umožní současné sdílení stejného kmitočtového pásma více uživateli.

## Popis

Direct-Sequence Code Division [Multiple Access](/mobilnisite/slovnik/multiple-access/) (DS-CDMA) je základní schéma mnohonásobného přístupu pro 3G systém Universal Mobile Telecommunications System (UMTS) standardizovaný organizací 3GPP. Funguje na principu rozprostření (spreading) uživatelského datového signálu přes široké pásmo pomocí unikátního vysokorychlostního pseudonáhodného šumového ([PN](/mobilnisite/slovnik/pn/)) kódu, známého jako rozprostírací kód (spreading code). Datové bity každého uživatele jsou kombinovány (modulo-2 součet) s tímto rozprostíracím kódem, který má mnohem vyšší rychlost čipů (např. 3,84 Mcps pro UMTS) než původní rychlost datových symbolů. Tento proces přemění úzkopásmový datový signál na širokopásmový signál s charakterem podobným šumu. V přijímači je stejný unikátní kód použit ke korelaci a 'složení' (de-spreading) požadovaného signálu zpět do původní šířky pásma, zatímco rušivé signály (od jiných uživatelů nebo šum) jsou dále rozprostřeny a následně odfiltrovány. To poskytuje zisk zpracování (processing gain) a odolnost vůči úzkopásmovému rušení.

Architektura systému DS-CDMA v UMTS zahrnuje několik klíčových komponent fyzické vrstvy. Proces rozprostření je prováděn kanalizačními kódy (kódy Orthogonal Variable Spreading Factor), které oddělují fyzické kanály ze stejného zdroje, a skramblovacími kódy (Goldovy kódy nebo dlouhé PN kódy), které rozlišují různá uživatelská zařízení (UE) nebo NodeB. Širokopásmové [CDMA](/mobilnisite/slovnik/cdma/) ([WCDMA](/mobilnisite/slovnik/wcdma/)) rádiové rozhraní využívá dvě spárovaná pásma o šířce 5 MHz pro režim Frequency Division Duplex ([FDD](/mobilnisite/slovnik/fdd/)). Mezi klíčové fyzické kanály patří Dedicated Physical Channel ([DPCH](/mobilnisite/slovnik/dpch/)) pro uživatelská data a řízení, Common Pilot Channel ([CPICH](/mobilnisite/slovnik/cpich/)) pro odhad charakteristik přenosové cesty a synchronizační kanály. Systém využívá řízení výkonu, zejména rychlé uzavřené řízení výkonu (fast closed-loop power control) na frekvenci 1500 Hz, pro potlačení problému blízký-vzdálený (near-far problem), který je vlastní CDMA technologii, kdy silný signál od blízkého uživatele může přehlušit slabší signály od vzdálených uživatelů.

Role DS-CDMA v síti 3GPP je základní pro [UTRAN](/mobilnisite/slovnik/utran/) (UMTS Terrestrial Radio Access Network). Poskytuje fyzickou vrstvu pro jak služby s přepojováním okruhů (circuit-switched), tak služby s přepojováním paketů (packet-switched), podporuje proměnné datové rychlosti díky použití různých Spreading Factors (SF). Tato technika inherentně podporuje měkký předávání hovoru (soft handover), kdy může UE komunikovat současně s více NodeB, čímž se zlepšuje spolehlivost předávání. Její povaha se spektrálním rozprostřením také nabízí inherentní zabezpečení díky nejasnosti rozprostíracích kódů a poskytuje kmitočtovou diverzitu, což činí spojení robustním vůči vícecestému útlumu (multipath fading), zejména při kombinaci s Rake přijímačem, který kombinuje signály z různých šířicích se drah.

## K čemu slouží

DS-CDMA byl vyvinut pro splnění požadavků IMT-2000 Mezinárodní telekomunikační unie (ITU) na systémy mobilní komunikace třetí generace (3G), které vyžadovaly vyšší datové rychlosti, lepší spektrální účinnost a podporu multimediálních služeb ve srovnání se systémy 2G generace, jako je GSM (které používalo TDMA/FDMA). Primární problém, který řešil, bylo umožnit více uživatelům současně sdílet stejné široké kmitočtové pásmo bez striktního časového nebo kmitočtového rozdělení, čímž se zvýšila kapacita a usnadnila flexibilnější alokace šířky pásma. Jeho vytvoření bylo motivováno potřebou robustního rádiového rozhraní, které by mohlo poskytnout vyšší kapacitu v celulárním prostředí, podporovat služby s proměnnou přenosovou rychlostí a umožnit plynulá předávání hovorů.

Ve srovnání s TDMA přístupem 2G GSM nabízelo DS-CDMA několik teoretických výhod. Poskytovalo inherentní kmitočtovou diverzitu, což jej činilo odolnějším vůči vícecestému útlumu a úzkopásmovému rušení. Použití rozprostíracích kódů umožnilo měkký kapacitní limit, kdy přidání dalších uživatelů postupně degraduje kvalitu pro všechny, spíše než aby vytvořilo tvrdé blokování. To bylo klíčové pro podporu trhavé (bursty) povahy paketových dat. Dále zjednodušilo kmitočtové plánování, protože stejný kmitočet může být použit v každé buňce (faktor opakování kmitočtu 1), na rozdíl od GSM, které vyžadovalo pečlivé plánování, aby se zabránilo rušení na stejném kanálu. DS-CDMA tvořilo základ pro WCDMA FDD režim, který se stal globálně dominantní 3G technologií.

## Klíčové vlastnosti

- Širokopásmový přenos se spektrálním rozprostřením (např. šířka pásma 5 MHz)
- Unikátní rozprostírací a skramblovací kódy pro oddělení uživatelů/kanálů
- Rychlé řízení výkonu (1500 Hz) pro zmírnění problému blízký-vzdálený (near-far problem)
- Podpora měkkého (soft) a měkčího (softer) předávání hovoru
- Proměnné datové rychlosti díky nastavitelným Spreading Factors
- Odolnost vůči vícecestému útlumu pomocí Rake přijímačů

## Související pojmy

- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)
- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)
- [HSPA – High Speed Packet Access](/mobilnisite/slovnik/hspa/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.201** (Rel-19) — UTRA Physical Layer General Description
- **TS 25.212** (Rel-19) — UTRA FDD Layer 1 Multiplexing & Channel Coding

---

📖 **Anglický originál a plná specifikace:** [DS-CDMA na 3GPP Explorer](https://3gpp-explorer.com/glossary/ds-cdma/)
