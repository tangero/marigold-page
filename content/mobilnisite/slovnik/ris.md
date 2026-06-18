---
slug: "ris"
url: "/mobilnisite/slovnik/ris/"
type: "slovnik"
title: "RIS – Radio Interface Synchronization"
date: 2025-01-01
abbr: "RIS"
fullName: "Radio Interface Synchronization"
category: "Radio Access Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ris/"
summary: "Funkce zajišťující synchronizaci rádiového rozhraní mezi uživatelským zařízením (UE) a sítí. Je klíčová pro udržení časového sladění, které je zásadní pro spolehlivou komunikaci, procedury předávání s"
---

RIS je funkce zajišťující synchronizaci rádiového rozhraní mezi uživatelským zařízením (UE) a sítí, což je klíčové pro časové sladění, spolehlivou komunikaci, procedury předávání spojení a řízení rušení.

## Popis

Radio Interface Synchronization (RIS) je základní mechanismus v systémech 3GPP, který zajišťuje, že časování rádiového vysílání a příjmu mezi uživatelským zařízením (UE) a základnovou stanicí (Node B v UMTS, eNodeB v LTE, gNB v NR) je přesně sladěno. Tato synchronizace funguje na více úrovních. Na úrovni rámce zajišťuje, že UE a síť pracují se stejnou hranicí 10ms rádiového rámce, což je nezbytné pro správnou interpretaci řídicích kanálů a plánovacích informací. Na jemnější úrovni je udržována synchronizace na úrovni slotů a symbolů, což je kritické pro systémy založené na ortogonálním frekvenčním multiplexu ([OFDM](/mobilnisite/slovnik/ofdm/)), jako jsou LTE a NR, aby byla zachována ortogonalita mezi subnosnými vlnami a zabráněno mezisymbolovému rušení.

Proces je typicky zahájen a udržován prostřednictvím synchronizačních signálů vysílaných buňkou. V LTE se jedná o Primární synchronizační signál ([PSS](/mobilnisite/slovnik/pss/)) a Sekundární synchronizační signál ([SSS](/mobilnisite/slovnik/sss/)). UE provádí procedury vyhledávání buněk, aby tyto signály detekovalo, získalo časování slotů a rámců a identifikovalo Fyzický identifikátor buňky ([PCI](/mobilnisite/slovnik/pci/)). Po připojení je kontinuální synchronizace udržována pomocí referenčních signálů a příkazů časového předstihu (Timing Advance) ze sítě. Síť měří časování uplinkových přenosů UE a posílá příkazy Timing Advance ([TA](/mobilnisite/slovnik/ta/)), kterými instruuje UE, aby posunulo nebo oddálilo časování svého vysílání. Tím se kompenzuje zpoždění šíření způsobené vzdáleností UE od základnové stanice, což zajišťuje, že všechny signály UE dorazí na základnovou stanici v očekávaném časovém okně.

RIS není samostatný protokol, ale všudypřítomný funkční požadavek zabudovaný do procedur fyzické vrstvy a vrstvy 2. Její architektura zahrnuje zpracování na fyzické vrstvě UE, funkce plánovače a řízení rádiových zdrojů základnové stanice a podkladovou transportní síť, která musí dodat časovou referenci (např. z [GPS](/mobilnisite/slovnik/gps/) nebo [IEEE](/mobilnisite/slovnik/ieee/) 1588) k základnové stanici. Její role je naprosto klíčová; bez správné RIS by selhaly základní funkce, jako je náhodný přístup, příjem pagingu, plánování dat a předávání spojení. Je základem stability sítě, spektrální účinnosti a kvality služeb pro všechny připojené uživatele.

## K čemu slouží

Radio Interface Synchronization existuje, aby řešila základní problém koordinace přenosů ve sdíleném bezdrátovém médiu. V každém celulárním systému více uživatelů současně vysílá a přijímá data. Bez přesné časové kontroly by se tyto signály chaoticky překrývaly, způsobovaly by vážné rušení a spolehlivá demodulace by byla nemožná. RIS poskytuje časový rámec, který umožňuje duplexování s časovým dělením ([TDD](/mobilnisite/slovnik/tdd/)), plánované přidělování zdrojů a principy ortogonality u OFDMA a SC-FDMA.

Historicky byla synchronizace základním požadavkem již od prvních digitálních celulárních standardů. Motivací pro standardizaci jejích mechanismů v rámci 3GPP bylo zajistit interoperabilitu mezi zařízeními od různých výrobců a definovat přesné výkonnostní požadavky (např. časovou přesnost, dobu akvizice) nezbytné pro funkční síť. Před formální specifikací se implementace mohly lišit, což vedlo k potenciálním problémům s kompatibilitou. RIS řeší omezení nesynchronizovaného, konkurenčního přístupu, který je pro celulární sítě s vysokou hustotou uživatelů vysoce neefektivní. Umožňuje síti přejít od náhodného přístupu náchylného ke kolizím k deterministickému, plánovanému přístupu, který je základem výkonu moderních celulárních sítí, pokud jde o propustnost dat a latenci.

## Klíčové vlastnosti

- Umožňuje časové sladění mezi UE a sítí na úrovni rámce, slotu a symbolu
- Umožňuje procedury vyhledávání buňky a počátečního přístupu prostřednictvím synchronizačních signálů (PSS/SSS)
- Podporuje mechanismus časového předstihu (Timing Advance) pro uplinkovou synchronizaci
- Nezbytná pro udržení ortogonality v systémech OFDM/OFDMA za účelem prevence rušení
- Kritická pro úspěšné procedury předávání spojení a mobility
- Tvoří základ plánovaného přidělování zdrojů a efektivního využití spektra

## Definující specifikace

- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [RIS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ris/)
