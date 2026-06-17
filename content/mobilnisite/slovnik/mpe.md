---
slug: "mpe"
url: "/mobilnisite/slovnik/mpe/"
type: "slovnik"
title: "MPE – Maximum Permissible Exposure"
date: 2025-01-01
abbr: "MPE"
fullName: "Maximum Permissible Exposure"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mpe/"
summary: "Maximum Permissible Exposure (MPE) je regulační a bezpečnostní rámec v 3GPP, který definuje limity pro lidskou expozici elektromagnetickému poli (EMF) z rádiových zařízení, zejména pro frekvence nad 6"
---

MPE je regulační rámec 3GPP, který definuje bezpečnostní limity pro lidskou expozici elektromagnetickému poli z rádiových zařízení a zajišťuje jejich dodržování prostřednictvím řízení výkonu nebo svazku, když se v blízkosti nachází osoba.

## Popis

Maximum Permissible Exposure (MPE) je komplexní rámec integrovaný do specifikací 3GPP, primárně pro New Radio (NR), který zajišťuje dodržování mezinárodních bezpečnostních předpisů týkajících se lidské expozice vysokofrekvenčnímu elektromagnetickému poli (RF-EMF). Tento rámec získává na významu zejména pro frekvenční rozsahy nad 6 GHz, jako jsou pásma milimetrových vln (mmWave), kde použití směrových antén s vysokým ziskem a beamforming může vést k lokalizované vysoké hustotě výkonu. Rámec MPE funguje na principu dynamického řízení ekvivalentního izotropně vyzářeného výkonu ([EIRP](/mobilnisite/slovnik/eirp/)) zařízení na základě odhadované vzdálenosti od lidského těla. Základní mechanismus spočívá v tom, že UE nebo síťový uzel provádí detekci přiblížení, často za použití senzorů nebo na základě předpokládaných scénářů použití, a následně aplikuje potřebné snížení výkonu nebo úpravy svazku, aby byla zajištěna hustota výkonu v určené vzdálenosti pod regulačními limity definovanými orgány jako ICNIRP nebo [FCC](/mobilnisite/slovnik/fcc/).

Z architektonického hlediska jsou požadavky MPE zakotveny ve vrstvách Radio Resource Control ([RRC](/mobilnisite/slovnik/rrc/)) a Medium Access Control ([MAC](/mobilnisite/slovnik/mac/)) v UE, jak je podrobně popsáno ve specifikacích jako 38.331 a 38.321. UE musí hlásit svou schopnost podporovat požadavky MPE a svůj maximální povolený EIRP za různých podmínek. Síť může konfigurovat parametry související s MPE prostřednictvím signalizace RRC. Klíčovou součástí je procedura hlášení MPE, při které může UE informovat síť o změnách ve svém provozním stavu souvisejících s expozičními limity, což může síť vyvolat ke změně konfigurace vysílacího výkonu UE, modulačního schématu nebo vzorů beamforming.

V praxi rámec MPE zavádí nová pole v blocích systémových informací (SIBs) a v RRC zprávách pro předávání informací o politice MPE. Například SIB1 může vysílat buňkově specifické parametry MPE. Vrstva MAC v UE zajišťuje prosazování těchto pravidel v reálném čase, případně omezuje výkon pro každý přenos. To zajišťuje, že ani během špičkového přenosu dat zařízení nepřekročí expoziční limity. Role MPE tedy není jen v regulační shodě, ale také v umožnění bezpečného a veřejně přijatelného nasazení vysokofrekvenčních 5G a budoucích 6G technologií, které spoléhají na koncentrovanou energii svazku pro kapacitu a pokrytí.

## K čemu slouží

Rámec MPE byl zaveden ve 3GPP Release 16, aby vyřešil kritickou mezeru v dodržování bezpečnostních předpisů pro nové rádiové technologie, zejména ty pracující v milimetrovém spektru (mmWave). Před Rel-16 byly limity expozice [EMF](/mobilnisite/slovnik/emf/) řízeny pomocí statických, konzervativních limitů výkonu, které nezohledňovaly dynamickou a směrovou povahu beamforming v 5G NR. Jak sítě začaly nasazovat frekvence nad 6 GHz, stávající metrika SAR (Specific Absorption Rate) pro nižší frekvence se stala méně použitelnou a relevantní metrikou se stala hustota výkonu. Statický přístup byl neefektivní, protože mohl zbytečně omezovat výkon sítě, i když se v blízkém poli antény nenacházel člověk.

Vytvoření MPE bylo motivováno potřebou uvolnit plný výkonový potenciál pásem mmWave při důsledném zajištění bezpečnosti uživatelů. Bez dynamického rámce by regulátoři mohli uvalit nadměrně omezující limity výkonu, což by narušilo zisky v pokrytí a kapacitě slibované 5G. MPE to řeší tím, že umožňuje inteligentní, kontextově citlivé řízení výkonu. Umožňuje zařízením vysílat s vyššími výkony, když je zajištěna bezpečná vzdálenost (např. pevné bezdrátové přípojné zařízení [CPE](/mobilnisite/slovnik/cpe/) na střeše), a inteligentně snížit výkon, když je v blízkosti osoba (např. smartphone v ruce). Tím řeší jak technickou výzvu efektivního využití spektra, tak společenskou potřebu prokazatelně bezpečné bezdrátové technologie, což usnadňuje plynulejší regulační schvalování a veřejné přijetí.

## Klíčové vlastnosti

- Dynamické řízení EIRP na základě detekce přiblížení
- Integrace s protokoly vrstvy NR RRC a MAC pro signalizaci a řízení
- Podpora frekvenčních rozsahů nad 6 GHz (FR2) a až do 52,6 GHz
- Hlášení schopností UE týkající se shody s MPE a maximálního výkonu
- Síťově konfigurovatelné politiky MPE vysílané v systémových informacích
- Koordinace řízení svazku pro zajištění shody bez výrazného zhoršení služby

## Související pojmy

- [NR – New Radio](/mobilnisite/slovnik/nr/)
- [EIRP – Effective Isotropic Radiated Power](/mobilnisite/slovnik/eirp/)
- [EMF – Electric and Magnetic Fields](/mobilnisite/slovnik/emf/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [MAC – Message Authentication Code](/mobilnisite/slovnik/mac/)

## Definující specifikace

- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [MPE na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpe/)
