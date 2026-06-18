---
slug: "ret"
url: "/mobilnisite/slovnik/ret/"
type: "slovnik"
title: "RET – Remote Electrical Tilting"
date: 2025-01-01
abbr: "RET"
fullName: "Remote Electrical Tilting"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/ret/"
summary: "RET umožňuje dálkové nastavení elektrického sklonu antény (downtilt) prostřednictvím řídicí jednotky, čímž optimalizuje pokrytí buňky a kapacitu bez fyzických návštěv stanoviště. Je klíčová pro dynami"
---

RET je metoda pro dálkové nastavení elektrického sklonu antény (downtilt) za účelem optimalizace pokrytí buňky a kapacity, snížení rušení a zlepšení kvality služeb bez nutnosti fyzických návštěv stanoviště.

## Popis

Remote Electrical Tilting (RET) je technologie, která umožňuje dálkové nastavení elektrického sklonu (downtilt) antény základnové stanice prostřednictvím řídicí jednotky, typicky zařízení kompatibilního se standardem Antenna Interface Standards Group (AISG). Systém se skládá z RET řadiče, často integrovaného do základnové stanice nebo samostatné jednotky, který komunikuje s dálkovou řídicí jednotkou (RCU) připojenou k anténě prostřednictvím sériového rozhraní, obvykle za použití protokolu AISG přes koaxiální kabel nebo samostatné řídicí linky. Toto uspořádání umožňuje přesné řízení vyzařovacího diagramu antény změnou fázového vztahu mezi anténními prvky, čímž se mění směr vertikálního svazku bez mechanického pohybu.

Z architektonického hlediska je RET součástí rámce provozu a údržby (O&M) v sítích 3GPP a rozhraní se systémy správy sítě pro automatizovanou optimalizaci. Ve specifikacích, jako jsou 3GPP TS 37.460 a 37.461, je RET definován v kontextu rozhraní Itf-N pro správu výkonu, což operátorům umožňuje upravovat parametry sklonu na základě metrik výkonu sítě v reálném čase. Funkce RET je integrována do uzlů rádiové přístupové sítě (RAN), jako jsou NodeB v UMTS nebo [eNB](/mobilnisite/slovnik/enb/) v LTE, a podporuje jak ruční, tak automatické úpravy sklonu prostřednictvím standardizovaných příkazů.

Klíčové komponenty zahrnují RET aktuátor uvnitř antény, který fyzicky nastavuje elektrický sklon, a řídicí software, který překládá optimalizační algoritmy sítě do příkazů pro sklon. Technologie funguje tak, že z RET řadiče jsou odesílány řídicí signály do RCU, která následně nastavuje fázové posouvače v anténním poli, čímž upravuje elevaci svazku. Tento proces je klíčový pro optimalizaci pokrytí, snížení mezibuněčného rušení a zvýšení kapacity v hustých městských nebo heterogenních nasazeních sítě. Role RET se rozšiřuje na funkce samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)), kde automatizuje úpravy sklonu pro vyvažování zátěže a koordinaci rušení.

V sítích 5G zůstává RET relevantní pro antény Massive [MIMO](/mobilnisite/slovnik/mimo/), kde je dynamické beamforming a řízení sklonu zásadní pro pokrytí milimetrovými vlnami a efektivitu multi-user MIMO. Vývoj RET zahrnuje podporu pro vícekmitočtové antény a integraci s pokročilými inteligentními řadiči RAN (RIC) v architekturách O-RAN, což umožňuje jemnější a real-time optimalizaci. Celkově je RET základní technologií pro efektivní správu RAN, která snižuje provozní náklady a zlepšuje výkon sítě prostřednictvím dálkového, softwarově řízeného ovládání antény.

## K čemu slouží

RET byla zavedena k řešení provozních neefektivit a nákladů spojených s ručním nastavováním sklonu antény, které vyžadovalo fyzické návštěvy stanovišť techniky. Před RET byl sklon antény nastaven mechanicky během instalace a dal se změnit pouze výstupem na stožár, což vedlo k vysokým mzdovým nákladům, bezpečnostním rizikům a pomalé reakci na změny v síti. Technologie umožňuje dynamickou optimalizaci sítě tím, že umožňuje dálkové, softwarové řízení sklonu antény, což usnadňuje rychlou adaptaci na provozní vzorce, podmínky rušení a požadavky na pokrytí.

Historicky, jak se mobilní sítě vyvíjely od 2G přes 3G a dále, se stala kritickou potřeba jemnější kontroly rádiových zdrojů kvůli rostoucí hustotě uživatelů a datovým požadavkům. RET řeší problémy, jako jsou díry v pokrytí, mezibuněčné rušení a kapacitní úzká místa, tím, že umožňuje automatické úpravy sklonu jako součást optimalizačních rutin sítě. Byla motivována snahou o samokonfigurovatelné a samooptymalizující se sítě, které snižují potřebu ručního zásahu a umožňují efektivnější využití spektra a infrastruktury.

V kontextu standardů 3GPP byl vznik RET hnán požadavky operátorů na snížení provozních výdajů ([OPEX](/mobilnisite/slovnik/opex/)) a zlepšení kvality služeb. Řeší omezení statických konfigurací antén, které se nemohly přizpůsobit denním nebo sezónním změnám provozu. Integrací RET do řídicích rozhraní, jako je Itf-N, standardizoval 3GPP možnosti dálkového ovládání, čímž připravil cestu pro pokročilé funkce [SON](/mobilnisite/slovnik/son/) a podpořil přechod k automatizované, inteligentní správě RAN v érách 4G a 5G.

## Klíčové vlastnosti

- Dálkové ovládání elektrického sklonu antény prostřednictvím standardizovaných rozhraní (např. AISG)
- Integrace se systémy správy sítě pro automatizovanou optimalizaci
- Podpora jak ručních, tak automatizovaných příkazů pro úpravu sklonu
- Snížení provozních nákladů eliminací fyzických návštěv stanoviště
- Zlepšení pokrytí a kapacity prostřednictvím dynamického směrování svazku
- Kompatibilita s vícekmitočtovými a víceanténními systémy

## Související pojmy

- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.401** (Rel-19) — UTRAN Overall Architecture
- **TS 28.652** (Rel-19) — UTRAN Network Resource Model (NRM) IRP Information Service
- **TS 32.642** (Rel-11) — UTRAN Network Resource Model for Configuration Management
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 37.460** (Rel-19) — Iuant Interface Introduction
- **TS 37.461** (Rel-19) — Iuant Interface Layer 1 Specification
- **TS 37.462** (Rel-19) — Iuant Interface Data Link Layer for RETAP/TMAAP
- **TS 37.466** (Rel-19) — Iuant Interface Introduction & RETAP/TMAAP
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification

---

📖 **Anglický originál a plná specifikace:** [RET na 3GPP Explorer](https://3gpp-explorer.com/glossary/ret/)
