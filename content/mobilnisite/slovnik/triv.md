---
slug: "triv"
url: "/mobilnisite/slovnik/triv/"
type: "slovnik"
title: "TRIV – Time Resource Indicator Value"
date: 2025-01-01
abbr: "TRIV"
fullName: "Time Resource Indicator Value"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/triv/"
summary: "Pole v řídicí informaci pro sestupný směr (Downlink Control Information, DCI), které udává konkrétní přidělení časových zdrojů pro vysílání nebo příjem. Je nezbytné pro dynamické plánování, zejména ve"
---

TRIV je pole v řídicí informaci pro sestupný směr (Downlink Control Information), které udává konkrétní přidělení časových zdrojů pro vysílání nebo příjem. Je nezbytné pro dynamické plánování v 5G NR.

## Popis

Hodnota indikátoru časového zdroje (Time Resource Indicator Value, TRIV) je parametr ve formátech řídicí informace pro sestupný směr (Downlink Control Information, [DCI](/mobilnisite/slovnik/dci/)) používaných v 3GPP 5G New Radio (NR). DCI je přenášena přes fyzický řídicí kanál sestupného směru (Physical Downlink Control Channel, [PDCCH](/mobilnisite/slovnik/pdcch/)) a obsahuje plánovací přiřazení pro přenosy v sestupném i vzestupném směru. TRIV konkrétně odkazuje na záznam v nakonfigurované tabulce přidělení časových zdrojů, čímž definuje počáteční symbol a délku plánovaného přenosu z hlediska [OFDM](/mobilnisite/slovnik/ofdm/) symbolů v rámci slotu nebo přes hranice slotů. Tento mechanismus poskytuje gNB jemně odstupňovanou kontrolu nad tím, kdy má UE data vysílat nebo přijímat, a přizpůsobuje se tak požadavkům na latenci, typu provozu a stavu kanálu.

Provozně plánovač gNB určí vhodné časové zdroje pro příjem UE na fyzickém sdíleném kanálu sestupného směru (Physical Downlink Shared Channel, [PDSCH](/mobilnisite/slovnik/pdsch/)) nebo přenos na fyzickém sdíleném kanálu vzestupného směru (Physical Uplink Shared Channel, [PUSCH](/mobilnisite/slovnik/pusch/)). Toto přidělení je namapováno na index v předdefinované nebo [RRC](/mobilnisite/slovnik/rrc/) nakonfigurované tabulce (např. pdsch-TimeDomainAllocationList nebo pusch-TimeDomainAllocationList). Index je následně zakódován do pole TRIV v rámci DCI. Velikost pole TRIV závisí na počtu záznamů v příslušné tabulce. Po dekódování DCI UE extrahuje hodnotu TRIV, nalezne příslušnou tabulku (která je známá prostřednictvím RRC konfigurace nebo výchozích hodnot specifikace) a identifikuje přesný indikátor začátku a délky ([SLIV](/mobilnisite/slovnik/sliv/)) nebo přímo počáteční symbol a dobu trvání. To UE přesně sděluje, které OFDM symboly má použít pro plánovanou komunikaci.

Zavedení TRIV podporuje klíčovou vlastnost 5G NR, kterou je ultraštíhlý a flexibilní design. Na rozdíl od rigidnějšího plánování v LTE založeného na podrámcích NR podporuje proměnné formáty slotů, minisloty (zahrnující méně než 14 symbolů) a dynamický [TDD](/mobilnisite/slovnik/tdd/). TRIV ve spojení s přiřazením kmitočtových zdrojů tuto flexibilitu umožňuje. Umožňuje přenosy s velmi nízkou latencí (např. zahájení příjmu PDSCH jen několik symbolů po PDCCH) a efektivní multiplexování různých služeb (např. eMBB a URLLC) v rámci stejné nosné. Tabulkový přístup také šetří režii DCI, protože několik bitů může indikovat složité časové vzory. Správná interpretace TRIV je tedy pro UE zásadní pro správné časové zarovnání jejího vysílání nebo příjmu, což zajišťuje efektivní využití zdrojů a splnění přísných požadavků na výkonnost 5G.

## K čemu slouží

TRIV byl vytvořen, aby řešil potřebu vysoce flexibilního a efektivního přidělování časových zdrojů v 5G NR, což byl požadavek, který mechanismy plánování LTE plně nenaplňovaly. LTE používalo pevný 1ms podrámec a předdefinované časové vztahy (např. hodnoty k0, k2), které byly dostačující pro širokopásmová data, ale postrádaly granularitu a dynamiku potřebnou pro rozmanité případy užití 5G, jako je ultra-spolehlivá komunikace s nízkou latencí (URLLC) a komunikace typu hromadného strojového provozu (mMTC). Rigidní struktura byla neefektivní pro provoz s proměnnou velikostí paketů a omezeními latence.

Jeho vývoj byl motivován snahou oddělit časování plánování od pevné mřížky, což umožňuje funkce jako plánování minislotů a dynamické přizpůsobování vzoru TDD pro vzestupný/sestupný směr. TRIV poskytuje kompaktní, tabulkami řízenou metodu signalizace libovolného časového přidělení, od jediného OFDM symbolu po celý slot nebo dokonce více slotů. Tím řeší problém signalizační režie; namísto přímého kódování hodnot začátku a délky (což by mohlo vyžadovat mnoho bitů) krátký index odkazuje na předem dohodnutou konfiguraci, čímž optimalizuje efektivitu řídicího kanálu.

Historicky byla indikace časového zdroje v LTE implicitní nebo polostatická. TRIV, zavedený v NR Rel-15 a dále vylepšovaný v pozdějších vydáních, představuje posun k explicitnímu, dynamickému a vysoce konfigurovatelnému plánování. Umožňuje síti rychle se přizpůsobit měnícím se potřebám provozu – například okamžitě naplánovat paket URLLC přes minislot, který prorazí probíhající přenos eMBB – čímž naplňuje slib 5G podporovat heterogenní služby na jednotném rádiovém rozhraní.

## Klíčové vlastnosti

- Pole v DCI, které indikuje index do tabulky přidělení časových zdrojů.
- Definuje počáteční symbol a dobu trvání (v OFDM symbolech) pro přenos PDSCH nebo PUSCH.
- Umožňuje podporu flexibilních formátů slotů a plánování minislotů.
- Snižuje signalizační režii DCI prostřednictvím indexace založené na tabulkách.
- Konfigurovatelné prostřednictvím RRC signalizace, což umožňuje síťově specifické vzorce přidělování.
- Nezbytné pro dynamický TDD a komunikaci s nízkou latencí v 5G NR.

## Související pojmy

- [DCI – Downlink Control Information](/mobilnisite/slovnik/dci/)
- [PDCCH – Physical Downlink Control Channel](/mobilnisite/slovnik/pdcch/)
- [SLIV – Start and Length Indicator Value](/mobilnisite/slovnik/sliv/)

## Definující specifikace

- **TS 38.321** (Rel-19) — NR MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [TRIV na 3GPP Explorer](https://3gpp-explorer.com/glossary/triv/)
