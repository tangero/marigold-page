---
slug: "pws"
url: "/mobilnisite/slovnik/pws/"
type: "slovnik"
title: "PWS – Plane Wave Synthesizer"
date: 2026-01-01
abbr: "PWS"
fullName: "Plane Wave Synthesizer"
category: "Physical Layer"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/pws/"
summary: "Technika nebo zařízení pro zpracování signálu používané v systémech anténních polí, zejména pro Massive MIMO a beamforming, za účelem generování rovinných vlnových front přes aperturu pole. Syntetizuj"
---

PWS je technika nebo zařízení pro zpracování signálu používané v systémech anténních polí pro generování rovnoměrných rovinných vlnových front za účelem zjednodušení odhadu kanálu, kalibrace a testování.

## Popis

Plane Wave Synthesizer (PWS) je pokročilá metodologie v rádiových přístupových sítích 3GPP, konkrétně relevantní pro testování Over-the-Air ([OTA](/mobilnisite/slovnik/ota/)), kalibraci antén a ověřování výkonu rozsáhlých anténních systémů, jako je Massive [MIMO](/mobilnisite/slovnik/mimo/). Odkazuje na systém nebo algoritmus, který vytváří elektromagnetické pole připomínající rovinnou vlnu – vlnu s konstantními fázovými frontami v definované oblasti – v blízkosti testovaného anténního pole. Toho je dosaženo pečlivým řízením amplitudy a fáze signálů přiváděných do více sondovacích antén nebo prvků pole v testovací komoře tak, aby jejich superpozice vytvořila téměř rovnoměrnou vlnovou frontu nad testovaným zařízením ([DUT](/mobilnisite/slovnik/dut/)). PWS umožňuje přesnou charakterizaci beamformingových diagramů, zisku a účinnosti bez nutnosti přímého kabelového připojení ke každému anténnímu prvku, což je u integrovaných polí nepraktické.

Z architektonického hlediska sestava PWS obvykle zahrnuje vektorový generátor signálů, více-sondové anténní pole (často uspořádané v kruhu nebo kouli kolem DUT) a řídicí jednotku, která vypočítává komplexní váhy pro každou sondu k syntéze požadovaného směru a polarizace rovinné vlny. Klíčovými komponentami jsou emulátor přenosového kanálu, který modeluje dráhu ve volném prostoru k DUT, a kalibrační systém, který zajišťuje známou a kompenzovanou odezvu sond. Z provozního hlediska PWS funguje řešením inverzního problému: při daných cílových parametrech rovinné vlny (např. úhel příchodu, polarizace) vypočítává excitační signály pro sondy tak, aby jejich vyzařovaná pole interferovala konstruktivně a vytvořila rovinnou vlnu v místě DUT. To zahrnuje techniky digitálního zpracování signálu, jako jsou algoritmy precodingu nebo beamformingu, často implementované v FPGA nebo vyhrazeném hardwaru pro provoz v reálném čase.

V kontextu specifikací 3GPP se techniky PWS používají pro testování shody a hodnocení výkonu antén UE a základnových stanic, zejména pro frekvence FR2 (mmWave), kde jsou anténní pole vysoce integrovaná. PWS usnadňuje standardizované metodologie OTA testování definované ve specifikacích jako 3GPP TR 38.810 a 38.141, umožňující reprodukovatelná měření metrik jako Celkový vyzařovaný výkon ([TRP](/mobilnisite/slovnik/trp/)) a Celková izotropní citlivost (TIS). Syntetizací rovinných vln z více směrů může emulovat realistická vícecestná prostředí nebo specifické beamformingové scénáře a ověřovat tak správnou funkci algoritmů pro nasměrování a sledování svazku v DUT. Jeho role je klíčová pro zajištění, aby systémy Massive MIMO splňovaly regulatorní a výkonnostní požadavky nákladově efektivním způsobem, neboť odstraňuje potřebu rozměrných a nákladných vedených testovacích sestav pro každý anténní port.

## K čemu slouží

Plane Wave Synthesizer byl vyvinut pro řešení výzev spojených s testováním a kalibrací rozsáhlých anténních polí, zejména pro systémy Massive [MIMO](/mobilnisite/slovnik/mimo/) a mmWave v 5G NR, kde se tradiční metody vedeného testování stávají neproveditelnými. V těchto systémech jsou antény integrovány s [RF](/mobilnisite/slovnik/rf/) front-endy, což ztěžuje nebo znemožňuje individuální přístup k portům. Předchozí přístupy spoléhaly na vzdálená pole nebo kompaktní rozsahy pro testování antén, které jsou velké, drahé a neškálovatelné pro hromadnou výrobu. PWS poskytuje řízené řešení v laboratorních podmínkách, které syntetizuje podmínky dalekého pole v nastavení blízkého pole, což umožňuje přesná [OTA](/mobilnisite/slovnik/ota/) měření v kompaktní komoře.

Historicky, jak 3GPP pokročilo od LTE k 5G, přechod na vyšší frekvence (např. mmWave) a masivní počet antén si vyžádal nové paradigmata testování pro ověření výkonu beamformingu a regulatorní shody. PWS to řeší tím, že umožňuje výrobcům a testovacím laboratořím emulovat realistická rádiová prostředí a dopad rovinné vlny, což je nezbytné pro vyhodnocení beamformingového zisku, úrovní postranních laloků a prostorových charakteristik. Řeší omezení dřívějších OTA metod, kterým chyběla přesnost v řízení vlnové fronty, což vedlo k nejistotám měření. Standardizací technik založených na PWS ve specifikacích 3GPP zajišťuje konzistentní a reprodukovatelné testování napříč průmyslem, což podporuje nasazování spolehlivých zařízení a základnových stanic 5G. To je motivováno potřebou nákladově efektivního testování ve velkých objemech pro splnění požadavků globálního nasazení 5G.

## Klíčové vlastnosti

- Syntetizuje rovnoměrné rovinné vlnové fronty pro řízené OTA testování
- Umožňuje testování integrovaných anténních polí bez přímého přístupu k portům
- Podporuje více-sondová uspořádání pro emulaci různých úhlů příchodu a polarizací
- Usnadňuje měření TRP, TIS a beamformingových diagramů v kompaktních komorách
- Integruje emulaci kanálu pro testování realistických vícecestných scénářů
- Standardizováno v 3GPP pro testování shody a ověřování výkonu zařízení 5G NR

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.268** (Rel-20) — Public Warning System (PWS) Requirements
- **TR 22.968** (Rel-19) — Study on Public Warning System (PWS)
- **TS 29.168** (Rel-19) — SBc-AP Protocol Specification
- **TR 33.969** (Rel-19) — Security for Public Warning System (PWS)
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview
- **TS 36.304** (Rel-19) — UE Idle Mode Procedures in E-UTRA
- **TS 36.401** (Rel-19) — E-UTRAN Overall Architecture Description
- **TS 36.410** (Rel-19) — S1 Interface: General Aspects and Principles
- **TS 36.413** (Rel-19) — S1 Application Protocol (S1AP)
- **TR 37.941** (Rel-19) — RF Conformance Testing Background for Radiated BS Requirements
- **TS 38.141** (Rel-19) — NR Base Station RF Conformance Testing Part 1
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- … a dalších 1 specifikací

---

📖 **Anglický originál a plná specifikace:** [PWS na 3GPP Explorer](https://3gpp-explorer.com/glossary/pws/)
