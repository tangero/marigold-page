---
slug: "rpl"
url: "/mobilnisite/slovnik/rpl/"
type: "slovnik"
title: "RPL – Recovery Period Length"
date: 2025-01-01
abbr: "RPL"
fullName: "Recovery Period Length"
category: "Radio Access Network"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/rpl/"
summary: "Parametr v mechanismech řízení výkonu UMTS a LTE, který definuje časové období, po které mobilní zařízení obnovuje výkon po příkazech ke snížení výkonu. Zajišťuje stabilní úpravy vysílacího výkonu, př"
---

RPL je parametr v řízení výkonu UMTS a LTE, který definuje dobu obnovy vysílacího výkonu mobilního zařízení po přijetí příkazů ke snížení výkonu.

## Popis

Recovery Period Length (RPL, délka období obnovy) je klíčový parametr v algoritmech vnitřní smyčky řízení výkonu v rádiových přístupových technologiích 3GPP, konkrétně definovaný např. ve specifikaci TS 25.214 pro UMTS a odkazovaný v dalších. Řídí rychlost, s jakou uživatelské zařízení (UE) zvyšuje svůj vysílací výkon po přijetí po sobě jdoucích příkazů ke snížení výkonu od sítě. Konkrétně, když NodeB (v UMTS) nebo eNodeB (v LTE) odešle příkazy řízení vysílacího výkonu ([TPC](/mobilnisite/slovnik/tpc/)) ke snížení výkonu UE z důvodu dobrých podmínek kanálu, UE svůj výkon sníží. RPL určuje, kolik následných kroků zvýšení výkonu je potřeba k návratu výkonu na nominální úroveň, čímž zajišťuje postupnou obnovu a zabraňuje náhlým špičkám výkonu.

Architektonicky je RPL součástí rychlé smyčky řízení výkonu, která pracuje s vysokou frekvencí (např. 1500 Hz v UMTS) pro potlačení rychlého útlumu. Síť průběžně měří kvalitu přijímaného signálu (např. poměr signálu k interferenci, [SIR](/mobilnisite/slovnik/sir/)) a vydává TPC příkazy – buď „nahoru“, nebo „dolů“ – pro udržení cílového SIR. Když je odeslána série příkazů „dolů“, výkon UE se snižuje postupně. Parametr RPL definuje období obnovy: po posledním příkazu „dolů“ bude UE aplikovat příkazy „nahoru“ (nebo výchozí mechanismus obnovy) po stanovený počet slotů nebo podrámců, aby plynule zvýšila výkon zpět, čímž zabrání nadměrným poklesům výkonu, které by mohly zhoršit spolehlivost spojení.

Při provozu RPL spolupracuje s dalšími parametry řízení výkonu, jako je velikost kroku řízení výkonu (např. 1 dB nebo 2 dB). Například, pokud je RPL nastaven na 4 sloty a UE přijme více příkazů „dolů“, sníží výkon odpovídajícím způsobem. Poté během období obnovy 4 slotů, i když nejsou přijaty žádné explicitní příkazy „nahoru“, může UE implementovat řízený algoritmus zvýšení výkonu pro návrat k výchozí úrovni. Tento mechanismus stabilizuje smyčku řízení výkonu, snižuje oscilace a zajišťuje, že dočasná zlepšení podmínek kanálu nevedou k dlouhodobému podvýkonu. Je obzvláště důležitý ve scénářích s vysokou mobilitou, kde se podmínky útlumu rychle mění, protože vyvažuje rychlost reakce se stabilitou.

## K čemu slouží

RPL byl zaveden pro zvýšení stability a účinnosti uzavřené smyčky řízení výkonu v systémech UMTS založených na [WCDMA](/mobilnisite/slovnik/wcdma/). Rané návrhy řízení výkonu, ačkoli účinné při kompenzaci rychlého útlumu, mohly trpět oscilacemi nebo „ping-pong“ efekty, kdy úrovně výkonu nadměrně kolísaly kvůli agresivním úpravám. To mohlo zvýšit interferenci, snížit kapacitu a zhoršit kvalitu hovoru. RPL to řeší vynucením řízeného období obnovy po snížení výkonu, což vyhlazuje přechody a zabraňuje tomu, aby UE zůstávala příliš dlouho na nízkých úrovních výkonu, když se podmínky kanálu zlepší.

Historicky, jak se mobilní sítě vyvíjely pro podporu vyšších přenosových rychlostí a více uživatelů, se přesné řízení výkonu stalo klíčovým pro správu interference v systémech [CDMA](/mobilnisite/slovnik/cdma/), kde všichni uživatelé sdílejí stejnou frekvenci. Bez parametrů jako RPL by se smyčky řízení výkonu mohly stát nestabilními, což by vedlo k přerušeným hovorům nebo snížení propustnosti. Parametr umožňuje operátorům sítě vyladit kompromis mezi rychlostí reakce a stabilitou řízení výkonu a optimalizovat tak výkon systému na základě scénářů nasazení (např. městské vs. venkovské).

Dále RPL přispívá k optimalizaci životnosti baterie UE tím, že zajišťuje postupné a odůvodněné zvyšování výkonu namísto náhlých špiček. Také podporuje konzistentní kvalitu spojení, což je zásadní pro služby jako hlas přes IP nebo video v reálném čase. Jeho zařazení od Release 4 dále odráží pokračující zdokonalování mechanismů řízení výkonu pro splnění požadavků vyvíjejících se standardů 3GPP a zajištění robustního řízení rádiových zdrojů napříč generacemi.

## Klíčové vlastnosti

- Definuje dobu obnovy po příkazech ke snížení výkonu ve vnitřní smyčce řízení výkonu
- Stabilizuje smyčky řízení výkonu, aby předcházel oscilacím a ping-pong efektům
- Konfigurovatelný parametr umožňující optimalizaci sítě pro různá prostředí
- Spolupracuje s příkazy řízení vysílacího výkonu (TPC) v UMTS a LTE
- Podporuje postupné navyšování výkonu pro udržení kvality spojení během útlumu
- Zvyšuje kapacitu systému snížením zbytečných fluktuací interference

## Související pojmy

- [TPC – Transmit Power Control Command Error Rate](/mobilnisite/slovnik/tpc/)
- [SIR – Signal-to-Interference Ratio](/mobilnisite/slovnik/sir/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management
- **TS 25.214** (Rel-19) — UTRA FDD Physical Layer Procedures
- **TR 26.948** (Rel-19) — Video enhancements for 3GPP Multimedia Services

---

📖 **Anglický originál a plná specifikace:** [RPL na 3GPP Explorer](https://3gpp-explorer.com/glossary/rpl/)
