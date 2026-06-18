---
slug: "neho"
url: "/mobilnisite/slovnik/neho/"
type: "slovnik"
title: "NEHO – Network Evaluated Handover"
date: 2025-01-01
abbr: "NEHO"
fullName: "Network Evaluated Handover"
category: "Mobility"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/neho/"
summary: "Network Evaluated Handover (NEHO) je mechanismus rozhodování o předání spojení, při kterém síť (např. základnová stanice nebo RNC) primárně vyhodnocuje měření a rozhoduje o předání spojení pro uživate"
---

NEHO je mechanismus rozhodování o předání spojení, při kterém síť vyhodnocuje měření a rozhoduje o předání spojení pro UE, což je v protikladu k Mobile Evaluated Handover (MEHO).

## Popis

Network Evaluated Handover (NEHO) je základní koncept správy mobility v celulárních sítích, definovaný zejména ve specifikacích 3GPP pro GSM, UMTS a LTE. Odkazuje na proceduru předání spojení, při které rozhodnutí o zahájení předání spojení z jedné buňky do druhé provádí síťová infrastruktura na základě měřicích hlášení, která přijímá od uživatelského zařízení (UE). Proces je řízen sítí. Role UE spočívá primárně v provádění rádiových měření na obsluhující buňce a sousedních buňkách podle pokynů sítě (prostřednictvím zpráv řízení měření) a v odesílání těchto měřicích hlášení zpět k síťové entitě (např. Base Station Controller ([BSC](/mobilnisite/slovnik/bsc/)) v GSM, Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) v UMTS nebo eNodeB v LTE).

Po přijetí těchto hlášení síťová entita (bod rozhodování) data zpracuje. Aplikuje algoritmy a konfigurovatelné parametry (jako jsou hystereze předání, ofsety a prahové hodnoty pro sílu signálu (RxLev) a kvalitu (RxQual)), aby určila, zda je předání spojení nutné, a pokud ano, na kterou cílovou buňku. Vyhodnocení bere v úvahu faktory, jako pokles úrovně přijímaného signálu z obsluhující buňky pod práh zatímco signál ze sousední buňky je dostatečně silnější, nebo zhoršení kvality spoje obsluhující buňky. Síť má také širší přehled a může zvažovat zatížení sítě, kapacitu buněk a priority účastníků, což UE nemůže posoudit.

Po rozhodnutí síť orchestruje celé provedení předání spojení. Rezervuje prostředky v cílové buňce, odešle příkaz k předání spojení k UE (např. HANDOVER COMMAND v GSM, RADIO BEARER RECONFIGURATION v LTE) a koordinuje se základnovou sítí pro přepojení cesty uživatelské roviny. UE příkaz následuje, odpojí se od staré buňky a synchronizuje se s novou. Toto centralizované řízení umožňuje optimalizované celosíťové řízení mobility, vyrovnávání zatížení a důsledné prosazování politik, je však závislé na včasném a přesném hlášení měření od UE.

## K čemu slouží

NEHO existuje za účelem poskytnutí centralizované, síťově optimalizované kontroly nad mobilitou, což je klíčové pro efektivní správu rádiových prostředků, udržení kvality hovoru a zajištění celkové stability sítě. V raných celulárních systémech, jako je GSM, měla síť ([BSC](/mobilnisite/slovnik/bsc/)) plnou kontrolu kvůli omezené inteligenci a výpočetnímu výkonu raných mobilních terminálů. Tento přístup umožnil operátorům implementovat složité algoritmy předání spojení přizpůsobené jejich síťové topologii, plánování kmitočtů a cílům správy provozu z jednoho centrálního bodu.

Řeší problém nekoordinovaných rozhodnutí o mobilitě, která by mohla nastat, pokud by UE jednala autonomně. Čistě uživatelsky orientované rozhodnutí ([MEHO](/mobilnisite/slovnik/meho/)) by mohlo vést k "ping-pong" předáním spojení mezi buňkami nebo k předání spojení do již přetížených buněk, což by degradovalo celkový výkon sítě. NEHO umožňuje síti zvažovat globální parametry, jako je zatížení buňky, dostupná kapacita a úrovně interference, což umožňuje funkce jako předání spojení založené na zatížení a řízené opakování volání. Tato centralizovaná inteligence je nezbytná pro funkce jako hierarchické buněčné struktury (makro/mikro buňky) a pro prosazování politik operátora týkajících se roamingu účastníků a kontinuity služeb. Zatímco pozdější technologie zavedly více uživatelsky asistované a síťově řízené paradigmy (jako v LTE a 5G), základní princip NEHO – kde je síť konečnou rozhodovací autoritou na základě shromážděných dat – zůstává základním kamenem řízené celulární mobility.

## Klíčové vlastnosti

- Rozhodnutí o předání spojení provádí síťová entita (BSC, RNC, eNodeB, gNB)
- UE poskytuje měřicí hlášení podle pokynů síťového řízení měření
- Síť aplikuje konfigurovatelné algoritmy a prahové hodnoty (hystereze, ofsety) pro vyhodnocení hlášení
- Umožňuje celosíťovou optimalizaci (vyrovnávání zatížení, směrování provozu)
- Podporuje složité buněčné struktury a hierarchické sítě
- Umožňuje řízení předání spojení založené na politikách (např. priorita účastníka, typ služby)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [NEHO na 3GPP Explorer](https://3gpp-explorer.com/glossary/neho/)
