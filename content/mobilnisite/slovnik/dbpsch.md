---
slug: "dbpsch"
url: "/mobilnisite/slovnik/dbpsch/"
type: "slovnik"
title: "DBPSCH – Dedicated Basic Physical Sub Channel"
date: 2025-01-01
abbr: "DBPSCH"
fullName: "Dedicated Basic Physical Sub Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/dbpsch/"
summary: "Vyhrazený fyzický kanál v GSM/EDGE rádiové přístupové síti (GERAN) používaný pro přenos uživatelských dat a řídicí signalizace. Představuje základní přidělený fyzický zdroj pro komunikaci mobilní stan"
---

DBPSCH je vyhrazený fyzický kanál v sítích GSM/EDGE, který poskytuje základní fyzický zdroj pro přenos uživatelských dat a řídicí signalizace pro služby s přepojováním okruhů i paketů.

## Popis

Dedicated Basic Physical Sub Channel (DBPSCH) je základní součástí architektury fyzické vrstvy GSM, konkrétně v rámci [GERAN](/mobilnisite/slovnik/geran/) (GSM/[EDGE](/mobilnisite/slovnik/edge/) Radio Access Network). Představuje nejmenší granularitu přidělování vyhrazeného fyzického zdroje mobilní stanici a funguje v rámci [TDMA](/mobilnisite/slovnik/tdma/) (Time Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)) struktury, která definuje rádiové rozhraní GSM. Každý DBPSCH odpovídá konkrétnímu časovému slotu v rámci TDMA rámce na určeném rádiovém kmitočtovém kanálu a poskytuje fyzické médium pro přenos uživatelských dat a řídicích informací mezi mobilní stanicí a podsystémem základnové stanice.

Architektonicky DBPSCH funguje na fyzické vrstvě (vrstva 1) protokolového zásobníku GSM a slouží jako základ pro různé logické kanály přenášející různé typy informací. Kanál využívá v základní formě modulaci [GMSK](/mobilnisite/slovnik/gmsk/) (Gaussian Minimum Shift Keying), přičemž EDGE (Enhanced Data rates for GSM Evolution) zavádí pro vyšší datové rychlosti modulaci [8-PSK](/mobilnisite/slovnik/8-psk/). Každý DBPSCH zabírá šířku pásma 200 kHz a funguje v rámci kmitočtových pásem GSM (typicky 900 MHz, 1800 MHz nebo 1900 MHz). Časové sloty jsou organizovány do mnohorámců obsahujících 26 TDMA rámců pro kanály přenosu hovoru nebo 51 TDMA rámců pro řídicí kanály.

Provoz DBPSCH zahrnuje přesnou časovou synchronizaci mezi mobilní stanicí a základnovou stanicí, přičemž každý časový slot trvá 577 mikrosekund a obsahuje 148 bitů informace. To zahrnuje koncové bity, šifrované datové bity, bity tréninkové sekvence pro odhad kanálu a ochranné bity. Kanál podporuje různé kódovací schémata (od CS-1 do CS-4 pro [GPRS](/mobilnisite/slovnik/gprs/) a MCS-1 do MCS-9 pro EDGE), která poskytují různé úrovně ochrany proti chybám a různé datové rychlosti. DBPSCH může přenášet buď provoz s přepojováním okruhů (například hovory používající kodeky Full Rate nebo Half Rate), nebo data s přepojováním paketů (prostřednictvím GPRS nebo EDGE), přičemž konkrétní konfiguraci určují protokoly vyšších vrstev na základě požadavků služby.

Klíčové součásti systému DBPSCH zahrnují rádiové přijímače/vysílače na straně mobilní i základnové stanice, mechanismy synchronizace TDMA rámců, jednotky pro kódování a prokládání kanálu a obvody pro modulaci/demodulaci. Výkon kanálu je charakterizován parametry, jako je poměr nosná/rušení ([C/I](/mobilnisite/slovnik/c-i/)), chybovost bitů (BER) a chybovost bloků (BLER), které určují kvalitu služby, kterou uživatel zažívá. DBPSCH také zahrnuje mechanismy řízení výkonu pro optimalizaci vysílacího výkonu a minimalizaci rušení v rámci celulární sítě.

V širší síťové architektuře slouží DBPSCH jako fyzické rozhraní mezi mobilní stanicí a základnovou stanicí (BTS), přičemž v buňce typicky současně funguje více DBPSCH kanálů pro obsluhu více uživatelů. Přidělování a správu kanálů řídí řadič základnových stanic (BSC) prostřednictvím vyhrazených signalizačních procedur. DBPSCH tvoří základ pro pokročilejší typy kanálů, jako je Dedicated Traffic Channel (DTCH) pro uživatelská data a Dedicated Control Channel (DCCH) pro signalizaci, což demonstruje jeho zásadní roli v hierarchii kanálů GSM.

## K čemu slouží

DBPSCH byl vytvořen, aby poskytoval vyhrazený, spolehlivý fyzický komunikační kanál pro jednotlivé mobilní uživatele v rámci celulárního systému GSM. Před GSM analogové celulární systémy, jako byl AMPS (Advanced Mobile Phone System), používaly FDMA (Frequency Division Multiple Access), které přidělovaly celé kmitočtové kanály uživatelům, což vedlo k neefektivnímu využití spektra. TDMA přístup GSM, implementovaný prostřednictvím fyzických kanálů jako DBPSCH, umožnil více uživatelům sdílet stejný kmitočtový kanál jeho rozdělením na časové sloty, což dramaticky zvýšilo kapacitu při zachování vyhrazených spojení pro každého aktivního uživatele.

Primární problém, který DBPSCH řeší, je poskytnutí garantovaného přístupu k prostředkům fyzické vrstvy pro mobilní stanice vyžadující nepřetržitou komunikaci, ať už pro hovory s přepojováním okruhů nebo pro datové relace s přepojováním paketů. Na rozdíl od společných řídicích kanálů, které jsou sdíleny všemi uživateli v buňce, nabízí DBPSCH vyhrazené prostředky, které zajišťují konzistentní kvalitu služby a spolehlivý přenos dat. Tento vyhrazený přístup byl nezbytný pro podporu služeb v reálném čase, jako jsou hovory, které nesnesou proměnlivá zpoždění a problémy s kolizemi spojené se sdílenými kanály.

Historicky DBPSCH představoval významný pokrok v celulární technologii tím, že umožnil digitální přenos v mobilních sítích. Návrh kanálu řešil omezení předchozích analogových systémů začleněním digitální modulace, kódování pro opravu chyb a přesného časového řízení. Jak se GSM vyvíjelo pro podporu paketových dat prostřednictvím GPRS a vyšších datových rychlostí prostřednictvím EDGE, DBPSCH si zachoval svou základní roli při podpoře vylepšených modulačních schémat a kódovacích rychlostí. Pokračující specifikace kanálu v rámci více vydání 3GPP demonstruje jeho trvalý význam jako základního stavebního kamene pro vyhrazenou komunikaci v GERAN, a to i přesto, že novější technologie jako UMTS a LTE zavedly odlišné struktury fyzických kanálů.

## Klíčové vlastnosti

- Vyhrazené přidělování časového slotu založené na TDMA na nosných o šířce 200 kHz
- Podpora modulačních schémat GMSK i 8-PSK
- Konfigurovatelná kódovací schémata kanálu (CS-1 až CS-4 pro GPRS, MCS-1 až MCS-9 pro EDGE)
- Synchronizace fyzické vrstvy prostřednictvím tréninkových sekvencí a mechanismů časového předstihu
- Integrované řízení výkonu pro správu rušení a šetření baterie
- Podpora multiplexování služeb s přepojováním okruhů i paketů

## Související pojmy

- [TDMA – Time Division Multiple Access](/mobilnisite/slovnik/tdma/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)
- [GPRS – CSI GPRS CAMEL Subscription Information](/mobilnisite/slovnik/gprs/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)

## Definující specifikace

- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [DBPSCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/dbpsch/)
