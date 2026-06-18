---
slug: "trau"
url: "/mobilnisite/slovnik/trau/"
type: "slovnik"
title: "TRAU – Transcoder and Rate Adaptation Unit (Frame)"
date: 2025-01-01
abbr: "TRAU"
fullName: "Transcoder and Rate Adaptation Unit (Frame)"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/trau/"
summary: "V sítích GSM/EDGE je TRAU funkční jednotka, která provádí převod řečového kódování a adaptaci datové rychlosti. TRAU rámec je formátovaná datová jednotka nesoucí komprimovanou řeč nebo adaptovaná data"
---

TRAU je funkční jednotka v sítích GSM/EDGE, která provádí převod řečového kódování (transkódování) a adaptaci datové rychlosti; používá specifický rámcový formát pro přenos komprimovaných dat přes rozhraní Abis za účelem optimalizace šířky pásma přenosové sítě (backhaul).

## Popis

Transcoder and Rate Adaptation Unit (TRAU) je klíčová funkční entita v GSM rádiové přístupové síti ([GERAN](/mobilnisite/slovnik/geran/)). Fyzicky se funkce TRAU typicky nachází v lokalitě řadiče základnových stanic ([BSC](/mobilnisite/slovnik/bsc/)) nebo v lokalitě ústředny mobilní sítě ([MSC](/mobilnisite/slovnik/msc/)). Jejím hlavním úkolem je převádět mezi 64 kbit/s [PCM](/mobilnisite/slovnik/pcm/) (Pulse Code Modulation) řečí používanou v jádře sítě (rozhraní A) a řečovými kodeky s nižší přenosovou rychlostí a kompresí (jako Full Rate, Half Rate, Enhanced Full Rate) používanými přes rádiové rozhraní (Um) za účelem úspory spektra. Pro datové služby provádí adaptaci rychlosti, přizpůsobuje uživatelské datové toky dostupným kanálům.

Činnost se točí kolem TRAU rámce, což je strukturovaný kontejner pro tyto převedená data při jejich přenosu přes rozhraní Abis (mezi [BTS](/mobilnisite/slovnik/bts/) a BSC) nebo rozhraní Ater (mezi BTS a TRAU, pokud jsou oddělené). Když mobilní stanice vysílá řeč, je zakódována pomocí řečového kodeku (např. 13 kbit/s pro [FR](/mobilnisite/slovnik/fr/)). BTS zabalí tato data do TRAU rámce, který přidá řídicí a synchronizační bity. Tento rámec je odeslán přes spoj Abis do TRAU. TRAU extrahuje komprimovanou řeč, dekóduje ji zpět na 64 kbit/s PCM (pokud je určena pro jádro sítě s přepojováním okruhů), nebo ji může pouze přeposlat v komprimované formě při použití Transcoder Free Operation (TrFO). Opačný proces probíhá pro provoz ve směru k uživateli (downlink).

Klíčové součásti funkce TRAU zahrnují samotný řečový transkodér, jednotku pro adaptaci rychlosti dat a logiku pro rámcování a submultiplexování. Struktura rámcování umožňuje multiplexovat více uživatelských kanálů s nízkou rychlostí (např. čtyři subkanály po 16 kbit/s) do jediného 64 kbit/s časového slotu na rozhraní Abis, což dramaticky zvyšuje efektivitu přenosové sítě (backhaul). Role TRAU je klíčová pro oddělení efektivity rádiového rozhraní od standardní infrastruktury jádra sítě založené na PCM, což umožňuje pokrok v řečovém kódování na rádiovém rozhraní bez nutnosti změny přenosové sítě jádra.

## K čemu slouží

TRAU bylo vytvořeno k vyřešení základního problému raných digitálních mobilních sítí: nesouladu mezi úspornými, ale kvalitativně omezenými řečovými kodeky potřebnými pro vzácné rádiové spektrum a standardní, vysoce kvalitní 64 kbit/s [PCM](/mobilnisite/slovnik/pcm/) řečí vyžadovanou existující telefonní sítí s přepojováním okruhů (jádro [PSTN](/mobilnisite/slovnik/pstn/)/ISDN). Bez transkódování by rádiově specifické kodeky vyžadovaly nestandardní infrastrukturu od konce ke konci, což bylo nepraktické.

Historicky, ve specifikacích GSM z éry R99, TRAU umožnilo operátorům umístit komplexní, procesorově náročnou funkci transkódování centrálně (v BSC nebo MSC), čímž byly vzdálené jednotky BTS jednodušší a levnější. Toto architektonické rozhodnutí optimalizovalo náklady a údržbu. Dále byl formát TRAU rámce a s ním spojené submultiplexování na rozhraní Abis navrženo tak, aby maximalizovalo využití často drahých pronajatých linek spojujících věže BTS s řadičem, přenášejíce více hovorů v jediném 64 kbit/s PCM slotu.

TRAU překonalo omezení sítí s pevnou rychlostí zavedením adaptability. Umožnilo postupně zavádět nové, efektivnější řečové kodeky (od FR přes HR a EFR až po AMR) při zachování zpětné kompatibility s jádrem sítě. Poskytlo také nezbytnou funkci adaptace rychlosti pro datové služby s přepojováním okruhů (jako je fax), což umožnilo podporu různých rychlostí koncového zařízení přes rádiový kanál.

## Klíčové vlastnosti

- Převod řečového kódování (transkódování) mezi rádiovými kodeky (např. FR, HR, EFR, AMR) a 64 kbit/s PCM
- Adaptace rychlosti pro datové služby s přepojováním okruhů
- Definuje strukturu TRAU rámce pro přenos přes rozhraní Abis/Ater
- Submultiplexování více kanálů s nízkou rychlostí do jediného 64 kbit/s časového slotu
- Podpora řídicí signalizace v pásmu (in-band) uvnitř TRAU rámce
- Umožňuje provoz bez transkodéru (Transcoder Free Operation, TrFO) pro obcházení kodeku od konce ke konci

## Související pojmy

- [BSC – Base Station Controller](/mobilnisite/slovnik/bsc/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 23.205** (Rel-19) — Bearer Independent CS Core Network Stage 2
- **TS 23.226** (Rel-19) — Global Text Telephony (GTT) Stage 2
- **TS 23.877** (Rel-6) — Speech Recognition Framework Analysis
- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description
- **TS 46.061** (Rel-19) — GSM EFR Frame Substitution and Muting Procedure
- **TS 48.061** (Rel-19) — BTS-TRAU Protocol for HR Speech/Data

---

📖 **Anglický originál a plná specifikace:** [TRAU na 3GPP Explorer](https://3gpp-explorer.com/glossary/trau/)
