---
slug: "tch"
url: "/mobilnisite/slovnik/tch/"
type: "slovnik"
title: "TCH – Traffic Channel"
date: 2025-01-01
abbr: "TCH"
fullName: "Traffic Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/tch/"
summary: "Traffic Channel (TCH) je vyhrazený fyzický kanál v systémech GSM, UMTS a příbuzných 2G/3G sítích, který přenáší uživatelská data, jako je hlas nebo paketová data, mezi mobilní stanicí a sítí. Je dynam"
---

TCH je vyhrazený fyzický kanál v systémech GSM a UMTS, který přenáší hlasová nebo paketová data uživatele a je dynamicky přidělován na dobu hovoru nebo relace.

## Popis

Traffic Channel (TCH) je základním přenosovým kanálem v přepojovaných okruzích mobilních sítí, jako je GSM a jeho vývojové systémy. Jedná se o obousměrný, bod-bod kanál zřízený mezi mobilní stanicí ([MS](/mobilnisite/slovnik/ms/)) a základnovou stanicí ([BTS](/mobilnisite/slovnik/bts/)) po dobu trvání hovoru nebo datové relace. TCH přenáší zakódovanou uživatelskou náplň, kterou může být hlas (pomocí kodeků jako Full Rate, Enhanced Full Rate nebo Adaptive Multi-Rate) nebo data (pomocí přepojovaných datových přenosů s rychlostmi až několik desítek kbps). Ve struktuře rozhraní GSM jsou TCH mapovány na konkrétní časové sloty v rámci [TDMA](/mobilnisite/slovnik/tdma/) rámců. Například plnorychlostní TCH zabírá jeden časový slot na rámec, zatímco poloviční TCH umožňuje sdílení jednoho časového slotu dvěma hovory prostřednictvím časového multiplexu, čímž se zdvojnásobí kapacita na úkor nižší kvality hlasu.

Provoz zahrnuje několik vrstev. Na fyzické vrstvě je TCH přidělen konkrétní absolutní číslo rádiového kmitočtového kanálu ([ARFCN](/mobilnisite/slovnik/arfcn/)) a časový slot. Data procházejí kanálovým kódováním (např. konvolučním kódováním pro ochranu proti chybám), prokládáním pro potlačení chybových shluků a šifrováním pro důvěrnost. Zakódované bity jsou následně modulovány (v GSM pomocí [GMSK](/mobilnisite/slovnik/gmsk/)) a vysílány. Na straně sítě BTS spravuje přidělování TCH, řízení výkonu a procedury předávání spojení. TCH je úzce propojen s přidruženými řídicími kanály, jako je pomalý přidružený řídicí kanál ([SACCH](/mobilnisite/slovnik/sacch/)) a rychlý přidružený řídicí kanál ([FACCH](/mobilnisite/slovnik/facch/)), které přenášejí vnitropásmovou signalizaci (např. pro příkazy k předání spojení) tak, že "kradou" rámce z TCH.

V UMTS (3G) se tento koncept vyvíjí, ale terminologie TCH zůstává pro přepojované okruhy. Zde jsou TCH vyhrazené transportní kanály ([DCH](/mobilnisite/slovnik/dch/) - Dedicated Channel) charakterizované specifickými rozprostíracími kódy a smyčkami řízení výkonu. Podporují proměnné přenosové rychlosti a pokročilejší kódování. TCH zůstává klíčový pro hlasové služby až do úplného přechodu na VoIP v pozdějších technologiích. V rámci specifikací jsou výkon a testování TCH podrobně popsány v dokumentech pokrývajících rádiové aspekty (řada 25 pro UMTS, řada 45 pro GSM), protokolovou architekturu (řada 24, řada 44) a testování výkonu (řada 34, řada 36 pro propojení s LTE).

## K čemu slouží

Traffic Channel byl vytvořen, aby poskytoval spolehlivou, vyhrazenou cestu pro uživatelský provoz v raných digitálních celulárních systémech, primárně pro hlas. Před GSM používaly analogové systémy, jako je AMPS, pro každý hovor vyhrazené páry kmitočtů, ale postrádaly robustní digitální kódování a efektivní využití spektra. TCH v GSM zavedl digitální přepojované okruhy s vícenásobným přístupem s časovým dělením (TDMA), což umožnilo více uživatelům sdílet jeden rádiový nosič. To dramaticky zlepšilo spektrální účinnost a kapacitu ve srovnání s analogovými systémy a umožnilo masové rozšíření mobilní telefonie.

TCH vyřešil základní problém vytvoření jasného, nepřerušovaného komunikačního spojení po dobu trvání hovoru. Oddělil uživatelský provoz od signalizačního provozu (na řídicích kanálech), což zajistilo, že nastavení hovoru, správa mobility a další řídicí funkce nezasahovaly do hlasového/datového toku. Toto oddělení zlepšilo spolehlivost a umožnilo pokročilé funkce, jako je předávání spojení bez přerušení hovoru – přidružené řídicí kanály (SACCH/FACCH) mohly přenášet potřebnou signalizaci, zatímco TCH přenášel hlas. Pro datové služby TCH poskytovaly první mobilní datové přenosy (např. prostřednictvím Circuit Switched Data - CSD), i při nízkých rychlostech, a připravily cestu pro paketově přepojovaný GPRS.

Jak se sítě vyvíjely k 3G (UMTS) a později k LTE/5G, čistě přepojovaný model TCH se stal pro efektivní zpracování dat limitujícím. TCH však zůstaly nezbytné pro podporu starších hlasových služeb a interoperabilitu. Jejich konstrukční principy ovlivnily pozdější vyhrazené přenosy v paketově přepojovaných systémech. Rozsáhlé specifikace napříč vydáními (R99 až Rel-19) odrážejí pokračující údržbu pro zpětnou kompatibilitu, testování a optimalizaci, zejména pro mechanismy hlasového navrácení (CS Fallback) v LTE a 5G nestandalone nasazeních, kde TCH v 2G/3G sítích zůstává klíčovou hlasovou kotvou.

## Klíčové vlastnosti

- Vyhrazený obousměrný kanál pro hlas uživatele nebo přepojovaná data
- Dynamické přidělení a uvolnění na dobu hovoru/relace
- Podporuje konfigurace plné a poloviční rychlosti pro kompromis mezi kapacitou a kvalitou
- Zahrnuje kanálové kódování, prokládání a šifrování pro robustní a bezpečný přenos
- Spolupracuje s přidruženými řídicími kanály (SACCH/FACCH) pro signalizaci během hovoru
- Mapován na konkrétní časové sloty (GSM) nebo vyhrazené kódy/řízení výkonu (UMTS)

## Související pojmy

- [SACCH – Standalone Associated Control CHannel](/mobilnisite/slovnik/sacch/)
- [FACCH – Fast Associated Control CHannel](/mobilnisite/slovnik/facch/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TR 25.914** (Rel-19) — 3G UE Radio Performance Test Methods
- **TS 32.401** (Rel-19) — Performance Management Concept & Requirements
- **TS 34.124** (Rel-19) — EMC Requirements for 3G UTRA Terminals
- **TS 36.124** (Rel-19) — EMC for E-UTRA User Equipment
- **TS 36.938** (Rel-9) — E-UTRAN to 3GPP2/Mobile WiMAX Mobility
- **TS 43.051** (Rel-19) — GERAN Stage 2 Service Description
- **TS 44.060** (Rel-19) — GERAN RLC/MAC Protocol Specification
- **TS 44.160** (Rel-16) — GERAN Iu Mode RLC/MAC Protocol Specification
- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [TCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/tch/)
