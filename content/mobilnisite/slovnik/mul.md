---
slug: "mul"
url: "/mobilnisite/slovnik/mul/"
type: "slovnik"
title: "MUL – Multiplier for NB-IoT Uplink"
date: 2025-01-01
abbr: "MUL"
fullName: "Multiplier for NB-IoT Uplink"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mul/"
summary: "MUL je parametr definující odsazení mezi číslem kanálu pro NB-IoT uplink a uplink EARFCN. Je klíčový pro výpočet přesné nosné frekvence uplinku v nasazeních NB-IoT, zajišťuje přesnou alokaci rádiových"
---

MUL je parametr, který definuje odsazení mezi číslem kanálu pro NB-IoT uplink a uplink EARFCN pro výpočet přesné nosné frekvence uplinku.

## Popis

Multiplikátor pro NB-IoT uplink (MUL) je základní parametr specifikovaný ve standardech 3GPP pro technologii Narrowband Internet of Things (NB-IoT). Funguje v rámci architektury rádiového přístupového sítě LTE, konkrétně pro směr uplink. NB-IoT využívá velmi úzkou šířku pásma 180 kHz a může být nasazeno ve třech režimech: in-band, guard-band nebo standalone. Parametr MUL je zásadní pro určení přesné nosné frekvence kanálu NB-IoT uplink vzhledem k nosné frekvenci LTE uplink, známé jako Uplink [E-UTRA](/mobilnisite/slovnik/e-utra/) Absolute Radio Frequency Channel Number ([EARFCN](/mobilnisite/slovnik/earfcn/)). Výpočet zahrnuje číslo kanálu NB-IoT uplink (NUL) a odsazení MUL pro odvození skutečné frekvence v MHz, což zajišťuje správné umístění nosné NB-IoT v rámci dostupného spektra.

Z architektonického hlediska je MUL definován ve specifikacích základnové stanice (eNodeB) a uživatelského zařízení (UE), což zajišťuje, že oba konce rádiového spoje používají stejnou alokaci frekvence. Parametr je součástí systémové informace vysílané eNodeB, která umožňuje UE synchronizaci a přístup k síti. Mezi klíčové zúčastněné komponenty patří Physical Uplink Shared Channel (PUSCH) a Physical Uplink Control Channel (PUCCH) pro NB-IoT, které spoléhají na přesné nastavení frekvence pro modulaci a přenos. Hodnota MUL je typicky celočíselné odsazení, které v kombinaci s uplink EARFCN LTE a vzorcem specifikovaným v 3GPP TS 36.104 dává nosnou frekvenci NB-IoT uplink. Tento přesný výpočet je zásadní pro zabránění interference s přilehlými nosnými LTE a dalšími nasazeními NB-IoT.

V síti hraje MUL klíčovou roli v efektivitě využití spektra a koexistenci. Pro in-band nasazení, kde NB-IoT sdílí spektrum s LTE, pomáhá MUM umístit nosnou NB-IoT uvnitř zdrojového bloku LTE bez způsobení škodlivé interference. V režimech guard-band nebo standalone zajišťuje správné zarovnání nosné NB-IoT v určeném frekvenčním pásmu. Parametr je součástí širšího návrhu fyzické vrstvy NB-IoT, který zahrnuje funkce jako single-tone a multi-tone přenosy uplinku. Umožněním přesného určení frekvence podporuje MUL spolehlivou komunikaci uplink pro IoT zařízení, která často mají nízký výkon a požadavky na rozšířené pokrytí. Jeho specifikace napříč více releasy (např. Rel-13 až Rel-18) zajišťuje zpětnou kompatibilitu a vývoj s novými vylepšeními NB-IoT.

## K čemu slouží

MUL byl zaveden v 3GPP Release 13, aby řešil potřebu přesného frekvenčního zarovnání v přenosech NB-IoT uplink. NB-IoT je nízkopříkonová širokoplošná ([LPWA](/mobilnisite/slovnik/lpwa/)) technologie navržená pro masivní nasazení IoT, vyžadující efektivní využití omezeného spektra. Před NB-IoT používaly sítě LTE pro výpočet frekvence [EARFCN](/mobilnisite/slovnik/earfcn/), ale úzkopásmová povaha NB-IoT a flexibilní režimy nasazení (in-band, guard-band, standalone) si vyžádaly specifický parametr odsazení pro definici jeho uplink nosné vzhledem k existujícím nosným LTE. Tím byly vyřešeny problémy s interferencí a nepřesnou alokací frekvence, které mohly degradovat výkon jak služeb NB-IoT, tak LTE.

Vznik MUL byl motivován rostoucí poptávkou po konektivitě pro IoT, kde zařízení jako senzory a měřiče vyžadují spolehlivou, nízkonákladovou komunikaci. Historické přístupy v LTE nebyly optimalizovány pro takové úzkopásmové aplikace s nízkou přenosovou rychlostí. MUL umožňuje síťovým operátorům nasadit NB-IoT bezproblémově v rámci jejich stávajícího spektra LTE, maximalizovat využití zdrojů bez nutnosti přepracování celého systému frekvenčního plánování. Řeší omezení předchozích metod tím, že poskytuje standardizovaný, škálovatelný způsob výpočtu frekvencí NB-IoT uplink, což zajišťuje globální interoperabilitu a konzistentní výkon napříč různými scénáři nasazení.

## Klíčové vlastnosti

- Definuje odsazení mezi číslem kanálu pro NB-IoT uplink a uplink EARFCN
- Umožňuje přesný výpočet nosné frekvence NB-IoT uplink
- Podporuje všechny režimy nasazení NB-IoT: in-band, guard-band a standalone
- Vysílán v systémové informaci pro synchronizaci UE
- Nedílná součást správy interference a efektivity využití spektra
- Specifikován v několika technických specifikacích 3GPP (např. 36.104, 36.108)

## Související pojmy

- [EARFCN – E-UTRAN Absolute Radio Frequency Channel Number](/mobilnisite/slovnik/earfcn/)
- [LTE – Local Terminal Emulator](/mobilnisite/slovnik/lte/)

## Definující specifikace

- **TS 36.104** (Rel-19) — Base Station (BS) radio transmission and reception
- **TS 36.108** (Rel-19) — Satellite Access Node RF Requirements
- **TS 36.141** (Rel-19) — E-UTRA BS Conformance Testing
- **TS 36.181** (Rel-19) — E-UTRA RF Test Methods for Satellite Access Node

---

📖 **Anglický originál a plná specifikace:** [MUL na 3GPP Explorer](https://3gpp-explorer.com/glossary/mul/)
