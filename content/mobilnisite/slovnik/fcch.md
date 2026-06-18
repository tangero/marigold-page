---
slug: "fcch"
url: "/mobilnisite/slovnik/fcch/"
type: "slovnik"
title: "FCCH – Frequency Correction Channel"
date: 2025-01-01
abbr: "FCCH"
fullName: "Frequency Correction Channel"
category: "Physical Layer"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fcch/"
summary: "Frequency Correction Channel (FCCH) je downlinkový rozhlasový kanál v systému GSM používaný k poskytnutí frekvenční reference mobilní stanici pro synchronizaci. Vysílá specifický nemodulovaný posun km"
---

FCCH je downlinkový rozhlasový kanál v GSM, který poskytuje mobilní stanici referenci pro synchronizaci frekvence vysíláním specifického nemodulovaného posunu kmitočtu nosné vlny.

## Popis

Frequency Correction Channel (FCCH) je základní fyzický kanál na rádiovém rozhraní GSM (Global System for Mobile Communications), pracující na downlinku od základnové stanice ([BTS](/mobilnisite/slovnik/bts/)) k mobilní stanici ([MS](/mobilnisite/slovnik/ms/)). Je to rozhlasový kanál vysílaný v konkrétním časovém slotu (TS0) na nosné Broadcast Control Channel ([BCCH](/mobilnisite/slovnik/bcch/)). Jediným účelem FCCH je poskytnout MS absolutní frekvenční referenci. Technicky vysílá dávku 148 bitů, všechny nastavené na binární '0'. Když je tento vzor zpracován pomocí modulačního schématu Gaussian Minimum Shift Keying ([GMSK](/mobilnisite/slovnik/gmsk/)) používaného v GSM, vytvoří čistou, nemodulovanou sinusovku se specifickým frekvenčním posunem 67,7 kHz nad nominálním kmitočtem nosné. Výsledkem je snadno identifikovatelný signál s konstantní frekvencí.

MS tento signál využívá během počátečního procesu výběru buňky a synchronizace. Když je MS zapnuta nebo vstoupí do nové oblasti, prohledává určená pásma kmitočtů GSM. Při detekci potenciální nosné BCCH vyhledá dávku FCCH. Přijímač MS obsahuje smyčku frekvenční korekce, která se zamkne na tento signál s posunem 67,7 kHz. Identifikací této přesné frekvence může MS přesně korigovat případný drift vlastního lokálního oscilátoru a synchronizovat frekvenci svého přijímače s frekvencí BTS. Tento proces je znám jako frekvenční synchronizace. Po úspěšné frekvenční korekci prostřednictvím FCCH pokračuje MS v synchronizaci časování slotů detekcí Synchronization Channel ([SCH](/mobilnisite/slovnik/sch/)), který bezprostředně následuje po FCCH v struktuře víceryhové rámcové struktury.

Z architektonického hlediska je FCCH jedním z logických kanálů mapovaných na časové sloty fyzické vrstvy. Je to vyhrazený řídicí kanál. Jeho vysílání je periodické a probíhá v rámci 51rámcové víceryhové struktury BCCH. Konkrétně se jedna dávka FCCH vysílá ve slotu 0 každého 10. nebo 11. rámce v rámci této víceryhy, v závislosti na konkrétní konfiguraci buňky. Tento pravidelný vzor umožňuje MS nejen provést počáteční synchronizaci, ale také při příjmu v buňce průběžně monitorovat a korigovat frekvenční drift. FCCH je kritická součást přístupové vrstvy GSM, která umožňuje spolehlivou demodulaci všech následujících kanálů, včetně Broadcast Control Channel (BCCH) přenášejícího systémové informace, a Common Control Channels ([CCCH](/mobilnisite/slovnik/ccch/)) používaných pro sestavení hovoru.

## K čemu slouží

FCCH byl vytvořen k řešení základního problému raných celulárních rádiových systémů: umožnit levnému mobilnímu telefonu pro masový trh rychle a přesně synchronizovat svůj přijímač s kmitočtem nosné rádiové sítě navzdory inherentním omezením hardwaru přístroje. Spotřebitelské oscilátory v mobilních telefonech mohou mít významný frekvenční drift způsobený změnami teploty, stárnutím a cenovými omezeními. Bez přesné frekvenční reference nemůže [MS](/mobilnisite/slovnik/ms/) spolehlivě demodulovat digitální signály z [BTS](/mobilnisite/slovnik/bts/), které využívají úzká pásma a přesné časování.

Před GSM používaly některé analogové systémy složitější nebo méně efektivní metody synchronizace. Konstruktéři GSM potřebovali jednoduchý, robustní a vždy dostupný signál, který by MS dokázala detekovat i při velké počáteční frekvenční chybě. Účelem FCCH je poskytnout tento jednoznačný 'maják' pro frekvenční korekci. Řeší omezení levných lokálních oscilátorů tím, že dává MS účinný nástroj k zarovnání na frekvenční mřížku sítě ještě před pokusem o dekódování dat. Toto je nezbytný první krok v hierarchickém procesu synchronizace (nejprve frekvence, poté čas), který umožňuje přístup do celulární sítě.

K jeho vytvoření motivovala potřeba standardizovaného a efektivního postupu vyhledávání buněk, který by minimalizoval čas potřebný telefonu k nalezení a příjmu v síti, čímž by se šetřila životnost baterie a zlepšila uživatelská zkušenost. Vyčleněním specifického kanálu s jedinečným, snadno identifikovatelným modulačním vzorem (tón 67,7 kHz) GSM zajistilo, že implementace MS mohla být jak účinná, tak ekonomická. FCCH spolu se SCH tvoří základní kámen počátečního synchronizačního postupu GSM, který byl díky svému úspěšnému návrhu inspirací pro pozdější technologie 3GPP, jež implementovaly analogické synchronizační signály (např. Primary Synchronization Signal v UMTS a LTE).

## Klíčové vlastnosti

- Vysílá specifický frekvenční posun 67,7 kHz od nosné, čímž vytváří čistou sinusovku pro snadnou detekci.
- Používá dávku bitů obsahující samé nuly modulovaných pomocí GMSK ke generování svého jedinečného signálu pro frekvenční korekci.
- Periodicky vysílán ve slotu 0 nosné BCCH v rámci 51rámcové víceryhové struktury.
- Poskytuje absolutní frekvenční referenci pro synchronizaci přijímače Mobilní Stanice.
- Umožňuje MS korigovat drift lokálního oscilátoru, což je předpoklad pro demodulaci všech ostatních kanálů GSM.
- Spolupracuje se Synchronization Channel (SCH) k dosažení plné časové a frekvenční synchronizace.

## Související pojmy

- [SCH – Synchronization Channel](/mobilnisite/slovnik/sch/)
- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)
- [GERAN – GSM EDGE Radio Access Network](/mobilnisite/slovnik/geran/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.225** (Rel-19) — UTRA TDD Physical Layer Measurements

---

📖 **Anglický originál a plná specifikace:** [FCCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/fcch/)
