---
slug: "darp"
url: "/mobilnisite/slovnik/darp/"
type: "slovnik"
title: "DARP – Downlink Advanced Receiver Performance"
date: 2025-01-01
abbr: "DARP"
fullName: "Downlink Advanced Receiver Performance"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/darp/"
summary: "DARP je specifikace 3GPP pro zvýšený výkon přijímače v sítích GSM/EDGE, která umožňuje zařízením efektivně fungovat v náročných rádiových podmínkách. Definuje požadavky na citlivost přijímače, díky ni"
---

DARP je specifikace 3GPP pro sítě GSM/EDGE, která definuje zvýšené požadavky na citlivost přijímače, což umožňuje mobilním zařízením udržet připojení i při slabším signálu a vyšší interferenci.

## Popis

Downlink Advanced Receiver Performance (DARP) je standardizovaná sada požadavků na výkon přijímače definovaná 3GPP pro mobilní stanice GSM/[EDGE](/mobilnisite/slovnik/edge/). Specifikace stanovuje minimální výkonnostní kritéria pro přijímače pracující v obtížných rádiových podmínkách, se zvláštním zaměřením na scénáře s vysokou interferencí a nízkou úrovní signálu. Požadavky DARP jsou specifikovány v dokumentu 3GPP TS 45.015 a souvisejících materiálech a poskytují rámec pro konzistentní výkon přijímače napříč různými výrobci zařízení.

V jádru DARP definuje konkrétní testovací případy a výkonnostní metriky, které musí mobilní přijímače splňovat. Ty zahrnují požadavky na citlivost pro různé modulační schémata ([GMSK](/mobilnisite/slovnik/gmsk/) pro GSM, 8PSK pro EDGE) za různých podmínek interference. Specifikace stanovuje referenční interferenční scénáře, jako je ko-kanálová interference a interference na sousedním kanále, vůči nimž se měří výkon přijímače. DARP Fáze I a Fáze [II](/mobilnisite/slovnik/ii/) představují progresivní úrovně výkonu, přičemž Fáze II zavádí přísnější požadavky na schopnost potlačování interference.

Technická implementace DARP zahrnuje pokročilé techniky zpracování signálu v řetězci mobilního přijímače. Klíčové komponenty zahrnují vylepšené algoritmy ekvalizace, zdokonalené metody odhadu kanálu a sofistikované mechanismy potlačení interference. Přijímač musí udržovat stanovené míry chybovosti bitů ([BER](/mobilnisite/slovnik/ber/)) a bloků ([BLER](/mobilnisite/slovnik/bler/)) i v případě, že požadovaný signál je výrazně slabší než rušivé signály. To vyžaduje pokročilé schopnosti digitálního zpracování signálu, včetně adaptivního filtrování, odhadu sekvence s maximální věrohodností (MLSE) a potenciálně technik kombinování s potlačením interference ([IRC](/mobilnisite/slovnik/irc/)).

Role DARP v síťové architektuře je primárně na fyzické vrstvě rádiového rozhraní GSM/EDGE. Přímo ovlivňuje správu rádiových prostředků tím, že umožňuje efektivnější vzory opakování využití frekvencí a lepší plánování pokrytí. Síťoví operátoři mohou nasazovat buňky s těsnějším faktorem opakování frekvencí s vědomím, že zařízení kompatibilní s DARP zvládnou výsledné úrovně interference. To vede ke zvýšení síťové kapacity bez nutnosti přidělení dalšího spektra. Technologie také zlepšuje pokrytí v oblastech na okraji buňky, kde je kvalita signálu typicky slabá.

Výkonnostní požadavky jsou ověřovány prostřednictvím standardizovaných testovacích postupů definovaných ve specifikacích 3GPP. Tyto testy simulují reálné interferenční scénáře pomocí specifických referenčních měřicích kanálů (RMC) a definovaných rušivých signálů. Výrobci musí prostřednictvím důkladného laboratorního testování před certifikací prokázat, že jejich zařízení splňují nebo překračují požadavky DARP. Tím je zajištěna interoperabilita a konzistentní uživatelský komfort napříč různými sítěmi a typy zařízení.

## K čemu slouží

DARP byl vytvořen k řešení rostoucích požadavků na kapacitu a výzev v pokrytí v sítích GSM s nárůstem využívání mobilních dat. Před DARP měly přijímače GSM omezené schopnosti potlačování interference, což nutilo síťové operátory používat konzervativní frekvenční plánování s velkými faktory opakování frekvencí. Tento přístup plýtval cennými spektrálními zdroji a omezoval síťovou kapacitu. Jak se sítě GSM vyvíjely pro podporu [EDGE](/mobilnisite/slovnik/edge/) a vyšších přenosových rychlostí, stala se potřeba robustnějších přijímačů klíčovou pro udržení kvality služeb v prostředích omezených interferencí.

Historický kontext vývoje DARP zahrnuje přechod od hlasově orientovaných sítí GSM k sítím GSM s podporou dat (EDGE). Tradiční přijímače GSM byly navrženy primárně pro hlasové služby s relativně nízkými datovými rychlostmi. Se zavedením EDGE a jeho modulace vyššího řádu (8PSK) čelily přijímače větším výzvám při udržování spolehlivého spojení za špatných rádiových podmínek. DARP poskytl standardizovaný rámec pro výkon přijímače, který síťovým operátorům umožnil nasazovat spektrálně efektivnější sítě při zajištění zpětné kompatibility se stávajícími zařízeními.

DARP řeší několik klíčových problémů při nasazování a provozu sítí GSM/EDGE. Umožňuje vyšší síťovou kapacitu prostřednictvím těsnějšího opakování využití frekvencí, což umožňuje obsloužit více uživatelů ve stejném spektru. Zlepšuje pokrytí v náročných prostředích, jako jsou městské kaňony, vnitřní prostory a oblasti na okraji buňky. Technologie také zlepšuje uživatelský komfort udržováním vyšších datových rychlostí a lepší kvality hovoru ve scénářích náchylných k interferenci. Stanovením standardizovaných výkonnostních požadavků DARP zajišťuje, že všechna kompatibilní zařízení poskytují konzistentní výkon, což usnadňuje síťové plánování a optimalizaci.

## Klíčové vlastnosti

- Zvýšené požadavky na citlivost přijímače pro modulační schémata GSM a EDGE
- Standardizované schopnosti potlačování ko-kanálové interference a interference na sousedním kanále
- Progresivní úrovně výkonu (Fáze I a Fáze II) s rostoucí přísností
- Podpora modulací GMSK (GSM) i 8PSK (EDGE) za podmínek interference
- Definované testovací postupy a výkonnostní metriky ve specifikacích 3GPP
- Zpětná kompatibilita se zařízeními bez podpory DARP při současném umožnění zlepšení síťové kapacity

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)
- [EDGE – Enhanced Data rates for Global Evolution](/mobilnisite/slovnik/edge/)

## Definující specifikace

- **TS 45.015** (Rel-19) — DARP Phase II Requirements for Release 5 MS
- **TR 45.912** (Rel-19) — GERAN Evolution Feasibility Study
- **TR 45.913** (Rel-19) — Optimized Transmit Pulse Shape for EGPRS2-B
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity
- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study

---

📖 **Anglický originál a plná specifikace:** [DARP na 3GPP Explorer](https://3gpp-explorer.com/glossary/darp/)
