---
slug: "fbi"
url: "/mobilnisite/slovnik/fbi/"
type: "slovnik"
title: "FBI – Final Block Indicator"
date: 2025-01-01
abbr: "FBI"
fullName: "Final Block Indicator"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/fbi/"
summary: "Řídicí bit používaný v protokolech spojové vrstvy, zejména v GSM Radio Link Protocol (RLP) a příbuzných standardech. Signalizuje, že aktuální blok je poslední v sekvenci nebo paketu vyšší vrstvy, což"
---

FBI je řídicí bit v protokolech spojové vrstvy, jako je GSM RLP, který signalizuje, že aktuální blok je poslední v sekvenci, což umožňuje správné znovusestavení a správu okna.

## Popis

Final Block Indicator (FBI) je jednobitová příznaková informace používaná ve struktuře rámců některých protokolů spojové vrstvy v systémech 3GPP, nejvýznamněji v GSM Radio Link Protocol (RLP) a Link Access Protocol on the Dm channel (LAPDm). Její primární funkcí je vymezit hranice datových jednotek (PDU) protokolů vyšších vrstev, které jsou segmentovány do více rámců spojové vrstvy. Při typickém provozu může být zpráva síťové vrstvy (vrstva 3) příliš velká, aby se vešla do jediného rámce vrstvy 2. Vysílající entita tuto zprávu segmentuje do více RLP rámců. Všechny rámce nesoucí segmenty stejné zprávy vrstvy 3, kromě posledního, mají svůj FBI bit nastaven na '0'. Rámec obsahující poslední segment má svůj FBI bit nastaven na '1'.

Na přijímací straně entita protokolu spojové vrstvy ukládá příchozí rámce do vyrovnávací paměti. Kontroluje FBI bit každého rámce. Dokud je FBI=0, přijímač chápe, že se očekávají další rámce patřící do aktuální sekvence, a pokračuje v ukládání datové části do vyrovnávací paměti. Když je přijat rámec s FBI=1, přijímač ví, že se jedná o koncový rámec sekvence. Následně může zřetězit všechny datové části z rámců této sekvence (ve správném pořadí pomocí sekvenčních čísel) a rekonstruovat původní, kompletní PDU vrstvy 3. Toto rekonstruované PDU je pak předáno vyšší vrstvě. Tento mechanismus je klíčový pro transparentní přenos proměnně dlouhých signalizačních zpráv přes rozhraní rádiového přenosu.

Bit FBI funguje ve spojení s dalšími řídicími poli rámce, jako je Send Sequence Number (N(S)) a bit Poll/Final v některých kontextech protokolu. Například v LAPDm je FBI součástí formátu rámce pro informační rámce (I-rámce). Jeho použití je řízeno specifickými stavovými automaty v rámci protokolu, aby byla zajištěna spolehlivá a uspořádaná doručování. Koncept není jedinečný pro 3GPP, ale je standardní technikou v protokolech spojové vrstvy (podobně jako příznak 'More Fragments' v IP). V technických specifikacích 3GPP jsou podrobnosti jeho implementace, jako je jeho pozice v hlavičce rámce a jeho interakce s potvrzovacími mechanismy protokolu, přesně definovány, aby byla zajištěna interoperabilita mezi mobilními stanicemi a síťovým zařízením.

## K čemu slouží

Final Block Indicator byl zaveden, aby vyřešil problém efektivní přepravy proměnně dlouhých a potenciálně velkých signalizačních a uživatelských datových zpráv přes rádiový spoj s omezenou a pevnou velikostí rámce. Rané digitální bezdrátové systémy potřebovaly metodu pro přizpůsobení paketů vyšších vrstev omezeným transportním blokům fyzické vrstvy, aniž by bylo nutné, aby vyšší vrstvy znaly velikost rádiového rámce. FBI poskytuje jednoduchý signalizační mechanismus v přenosovém pásmu pro segmentaci a znovusestavení na spojové vrstvě.

Bez takového indikátoru by přijímač neměl žádný způsob, jak zjistit, kdy je segmentovaná zpráva kompletní, což by vedlo buď k uváznutí protokolu (nekonečné čekání na další data), nebo k závislosti na zprávách pevné délky, což by bylo velmi neefektivní. FBI umožňuje spojové vrstvě poskytovat vyšší vrstvě transparentní službu, skrývaje složitosti segmentace. To bylo obzvláště důležité pro GSM a následné systémy, aby podporovaly širokou škálu služeb – od krátkých signalizačních zpráv po delší datové pakety pro služby jako SMS nebo raná datová přenosy v okruhově přepínaném režimu – pomocí společného, spolehlivého protokolu spojové vrstvy. Jeho vznik byl motivován potřebou robustního a efektivního přenosu dat v prostředí s omezenými zdroji a náchylném k chybám, čímž se stal základním prvkem spolehlivé datové komunikace v celulárních sítích.

## Klíčové vlastnosti

- Jednobitová příznaková informace v hlavičkách rámců spojové vrstvy (např. RLP, LAPDm)
- Signalizuje poslední rámec v sekvenci segmentovaných dat vyšší vrstvy
- Umožňuje transparentní segmentaci a znovusestavení (SAR) na vrstvě 2
- Funguje ve spojení s sekvenčními čísly rámců pro uspořádané doručování
- Umožňuje efektivní přenos proměnně dlouhých datových jednotek protokolu
- Základní pro fungování spolehlivých protokolů spojové vrstvy v GSM/UMTS

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.705** (Rel-13) — UMTS Small Data Transmission Enhancements Study
- **TS 43.064** (Rel-19) — GPRS Radio Interface Lower-Layer Functions

---

📖 **Anglický originál a plná specifikace:** [FBI na 3GPP Explorer](https://3gpp-explorer.com/glossary/fbi/)
