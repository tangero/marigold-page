---
slug: "emc"
url: "/mobilnisite/slovnik/emc/"
type: "slovnik"
title: "EMC – Electromagnetic Compatibility"
date: 2025-01-01
abbr: "EMC"
fullName: "Electromagnetic Compatibility"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/emc/"
summary: "EMC zajišťuje, že telekomunikační zařízení může správně fungovat ve svém elektromagnetickém prostředí, aniž by způsobovalo nepřijatelné rušení jiným zařízením. Zahrnuje dva aspekty: odolnost (imunitu"
---

EMC je vlastnost zajišťující, že telekomunikační zařízení funguje správně, aniž by způsobovalo nebo bylo narušováno elektromagnetickým rušením; zahrnuje jak odolnost vůči vnějšímu rušení, tak kontrolu vlastních emisí.

## Popis

Elektromagnetická kompatibilita (EMC) je schopnost elektrických a elektronických zařízení, včetně zařízení a systémů definovaných 3GPP, uspokojivě fungovat ve svém elektromagnetickém prostředí, aniž by do tohoto prostředí zaváděla nepřijatelné elektromagnetické poruchy pro jiná zařízení. Jedná se o obor s dvojím zaměřením, který zahrnuje **Emise** a **Odolnost (imunitu)**. Emise označují nežádoucí generování elektromagnetické energie zařízením, které musí být udržováno pod stanovenými limity, aby nedocházelo k rušení jiných zařízení. Odolnost (nebo citlivost) označuje schopnost zařízení fungovat podle zamýšleného účelu bez zhoršení výkonu při vystavení definovaným úrovním elektromagnetického rušení z vnějších zdrojů, jako jsou jiné rádiové vysílače, elektrostatický výboj nebo kolísání napájecí sítě.

Technická implementace EMC v rámci 3GPP zahrnuje širokou škálu standardizovaných testovacích metod specifikovaných v mnoha technických specifikacích (TS). Pro emise testy měří jak vyzařované emise (energie šířená prostorem), tak vodivé emise (energie vázaná na napájecí nebo telekomunikační kabely). Pro odolnost testy vystavují zařízení různým stresorům: vyzařovaným rádiovofrekvenčním polím, vodivým [RF](/mobilnisite/slovnik/rf/) rušením, elektrostatickému výboji ([ESD](/mobilnisite/slovnik/esd/)), elektrickým rychlým přechodovým jevům (EFT), rázům a poklesům napětí. Testované zařízení ([EUT](/mobilnisite/slovnik/eut/)) musí během těchto testů a po jejich skončení nadále splňovat svá minimální kritéria výkonu ([MPC](/mobilnisite/slovnik/mpc/)). Pro základnovou stanici může MPC znamenat udržení komunikačního spojení s testovacím UE; pro UE to může být udržení kvality hovoru nebo datového přenosu.

Role EMC v síti je naprosto zásadní pro nasazení a provoz. Jedná se o nezbytný regulační požadavek prakticky ve všech jurisdikcích po celém světě (např. označení [CE](/mobilnisite/slovnik/ce/) v EU, [FCC](/mobilnisite/slovnik/fcc/) Part 15 v USA). Bez splnění požadavků EMC nelze zařízení legálně uvést na trh. Z pohledu síťového operátora EMC zajišťuje, že nově instalovaný gNB nenaruší provoz sousedních LTE [eNB](/mobilnisite/slovnik/enb/) nebo jiného kritického zařízení na lokalitě (jako jsou mikrovlnné přenosové spoje). Naopak zajišťuje, že samotný gNB nefunguje chybně v důsledku rušení z blízkého vysílače. Tato vzájemná kompatibilita je nezbytná pro předvídatelný a kvalitní provoz hustých, více technologických a více dodavatelských rádiových přístupových sítí, zejména na sdílených infrastrukturních lokalitách, jako jsou střechy a stožáry.

## K čemu slouží

Účelem standardizace EMC je zaručit koexistenci a spolehlivý provoz množství elektronických zařízení v moderním světě. Jak se rádiové spektrum stávalo stále přeplněnějším a elektronická zařízení pronikala do všech aspektů života, riziko neúmyslného elektromagnetického rušení exponenciálně rostlo. Mobilní telefon, který naruší protiblokovací brzdový systém automobilu, nebo základnová stanice, která přeruší příjem sousedovy televize, jsou nepřijatelné scénáře. Standardy EMC byly vytvořeny, aby takovým situacím předcházely stanovením společné technické základny pro všechny výrobce zařízení.

EMC řeší kritický problém nepředvídatelných interakcí v komplexních elektromagnetických prostředích. Před rozšířenou regulací EMC se problémy s rušením často řešily reaktivně a nákladně až po nasazení. Standardizované požadavky EMC přesouvají zodpovědnost do fáze návrhu a předtržního testování, což zajišťuje, že produkty jsou z podstaty elektromagneticky „dobře vychované“. To je obzvláště důležité pro systémy kritické z hlediska bezpečnosti a veřejnou telekomunikační infrastrukturu, kde by selhání způsobené rušením mohlo mít závažné následky. Pro 3GPP zahrnutí odkazů na EMC zajišťuje, že specifikace rádiového výkonu, které definují, jsou dosažitelné v reálných podmínkách, kde je rušení přítomno.

Podrobné zpracování v mnoha vydáních 3GPP vychází z vývojové povahy samotné rádiové technologie. Každá nová generace (UMTS, LTE, NR) přinesla nová kmitočtová pásma, širší šířky pásma, složitější modulační schémata (jako [OFDMA](/mobilnisite/slovnik/ofdma/)) a pokročilé anténní systémy (MIMO, beamforming). Tyto technologické pokroky mění jak emisní profily zařízení, tak jejich potenciální citlivost. Proto musí být požadavky na testování EMC neustále aktualizovány a zpřesňovány. 3GPP spolupracuje se specializovanými standardizačními orgány pro EMC (jako jsou ETSI TC ERM a CISPR), aby odkazy na nejnovější testovací standardy zajistily, že zařízení 5G NR je například hodnoceno metodami vhodnými pro jeho specifické vlastnosti, jako jsou emise s řiditelným vyzařovacím diagramem a provoz v mmWave pásmech.

## Klíčové vlastnosti

- Dvojí zaměření na kontrolu emisí zařízení a zajištění odolnosti zařízení vůči vnějším rušivým vlivům
- Komplexní soubor standardizovaných testovacích metod pro vyzařované a vodivé jevy
- Definuje minimální kritéria výkonu (MPC) pro zařízení během testů odolnosti
- Pokrývá všechny typy zařízení 3GPP: uživatelská zařízení (UE), základnové stanice a převaděče
- Řeší širokou škálu zdrojů rušení: RF pole, ESD, rázové přepětí, rychlé přechodové jevy
- Nezbytné pro globální regulatorní shodu a přístup na trh (CE, FCC)

## Související pojmy

- [EM – Electromagnetic Emanations](/mobilnisite/slovnik/em/)
- [ESD – Equivalent Spatial Domain](/mobilnisite/slovnik/esd/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.113** (Rel-19) — EMC Requirements for UTRA Base Stations & Repeaters
- **TS 34.124** (Rel-19) — EMC Requirements for 3G UTRA Terminals
- **TS 36.113** (Rel-19) — EMC Requirements for E-UTRA Base Stations
- **TS 36.124** (Rel-19) — EMC for E-UTRA User Equipment
- **TS 37.113** (Rel-19) — EMC Requirements for Multi-Standard Radio Base Stations
- **TS 37.114** (Rel-19) — EMC for Active Antenna System Base Stations
- **TS 37.840** (Rel-12) — RF & EMC Requirements for Active Antenna Systems
- **TS 37.842** (Rel-13) — BS RF Requirements for Active Antenna Systems
- **TR 37.843** (Rel-15) — AAS BS Radiated RF Requirement Background
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.113** (Rel-19) — NR Base Station EMC Specification
- **TS 38.114** (Rel-19) — EMC Requirements for NR Repeaters and NCR
- **TS 38.175** (Rel-19) — EMC for NR IAB Nodes
- **TS 38.809** (Rel-16) — IAB Radio Transmission & Reception Background
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [EMC na 3GPP Explorer](https://3gpp-explorer.com/glossary/emc/)
