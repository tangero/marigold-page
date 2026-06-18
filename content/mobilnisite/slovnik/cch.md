---
slug: "cch"
url: "/mobilnisite/slovnik/cch/"
type: "slovnik"
title: "CCH – Control Channel"
date: 2025-01-01
abbr: "CCH"
fullName: "Control Channel"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cch/"
summary: "Řídicí kanál (CCH) je logický kanál v systémech 3GPP určený pro přenos informací řídicí roviny mezi sítí a uživatelským zařízením. Přenáší nezbytnou signalizaci pro přístup k síti, přidělování prostře"
---

CCH je logický kanál určený pro přenos informací řídicí roviny a nezbytné signalizace mezi sítí a uživatelským zařízením pro přístup, přidělování prostředků a správu mobility.

## Popis

Řídicí kanál (CCH) představuje třídu logických kanálů v rámci protokolového zásobníku 3GPP, konkrétně ve vrstvách řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) a řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)), jejichž hlavní funkcí je přenos signalizačních informací řídicí roviny. Na rozdíl od kanálů pro přenos dat ([TCH](/mobilnisite/slovnik/tch/)), které přenášejí uživatelská data, CCH přenášejí nezbytné příkazy, konfigurační zprávy a systémové informace potřebné k navázání, udržování a ukončení spojení mezi uživatelským zařízením (UE) a sítí. Tyto kanály jsou mapovány na transportní kanály a následně na fyzické kanály pro přenos přes rozhraní vzduchu. Oddělení řídicí a uživatelské roviny pomocí vyhrazených kanálů je základním architektonickým principem v celulárních sítích, který zajišťuje, že kritická signalizace zůstává spolehlivá a má odpovídající prioritu i za podmínek vysokého zatížení přenosem dat.

CCH fungují na úrovni logických kanálů, které jsou definovány typem přenášených informací. Klíčové příklady zahrnují vysílací řídicí kanál ([BCCH](/mobilnisite/slovnik/bcch/)) pro sestupné systémové informace, kanál pro volání ([PCCH](/mobilnisite/slovnik/pcch/)) pro oznámení o volání, společný řídicí kanál ([CCCH](/mobilnisite/slovnik/ccch/)) pro úvodní procedury přístupu, pokud neexistuje vyhrazené spojení, a vyhrazený řídicí kanál ([DCCH](/mobilnisite/slovnik/dcch/)) pro signalizaci typu bod–bod po navázání spojení řízení rádiových prostředků (RRC). Vrstva MAC je zodpovědná za multiplexování těchto logických kanálů na dostupné transportní kanály (jako je vysílací kanál ([BCH](/mobilnisite/slovnik/bch/)), kanál pro volání (PCH) nebo sestupný sdílený kanál (DL-SCH)) a aplikuje plánování a správu priorit. Fyzická vrstva následně mapuje tyto transportní kanály na fyzické prostředky (např. specifické časově-frekvenční zdroje v OFDMA/SC-FDMA pro LTE/NR).

Role CCH je všudypřítomná v celé interakci UE se sítí. V pohotovostním režimu UE sleduje BCCH pro získání kritických systémových parametrů a PCCH pro indikace volání. Během náhodného přístupu se používá CCCH pro úvodní výměnu zpráv, jako je Žádost o RRC spojení. Po úspěšném navázání spojení je nakonfigurován DCCH pro přenos všech následných vyhrazených RRC signalizací, jako jsou příkazy k předání, konfigurace měření a příkazy bezpečnostního režimu. Spolehlivost a integrita těchto kanálů jsou prvořadé a jsou často chráněny robustním kódováním kanálu, mechanismy hybridního automatického opakování na vyžádání (HARQ) a pro vyhrazenou signalizaci také šifrováním a ochranou integrity na RRC vrstvě. Návrh a správa CCH přímo ovlivňují klíčové ukazatele výkonnosti, jako je doba navázání hovoru, úspěšnost předání a celková stabilita systému.

## K čemu slouží

Řídicí kanál existuje proto, aby poskytoval spolehlivou a řízenou cestu pro signalizaci, která řídí všechny síťové operace. Přenos uživatelských dat (uživatelská rovina) by byl bez podkladových řídicích mechanismů pro přidělování prostředků, správu mobility, zajištění bezpečnosti a udržování kvality spojení bezvýznamný. CCH řeší základní problém oddělení kritického síťového řídicího provozu od uživatelských dat přenášených s nejlepším úsilím, a zajišťuje tak, že signalizační zprávy dostávají potřebnou prioritu, spolehlivost a zabezpečení. Toto oddělení umožňuje optimalizované přidělování prostředků, kde mohou být řídicí informace efektivně vysílány mnoha uživatelům nebo zasílány s vysokou spolehlivostí konkrétním uživatelům, aniž by byly ovlivněny zahlcením uživatelskými daty.

Historicky, dokonce i v před-3GPP systémech, bylo rozlišení mezi řídicími kanály a kanály pro přenos dat zásadní. Vytvoření a standardizace specifických typů CCH v UMTS (od R99 dále) a jejich vývoj přes LTE a 5G NR tuto architekturu formalizovaly v rámci paketově přepínaného rámce. Předchozí přístupy v jednodušších systémech mohly míchat řídicí a datový provoz, ale složitost sítí 3GPP – s funkcemi jako bezproblémová mobilita, diferenciace kvality služeb a pokročilé řízení rádiových prostředků – si vyžádala sofistikovanou, vrstvenou strukturu řídicích kanálů. Architektura CCH řeší omezení ad-hoc signalizace tím, že poskytuje předvídatelné, standardizované toky zpráv pro každou síťovou proceduru, od vyhledávání buňky po uvolnění spojení, což je klíčové pro interoperabilitu mezi zařízeními od různých výrobců a pro zajištění konzistentního uživatelského zážitku.

## Klíčové vlastnosti

- Přenáší síťovou signalizaci řídicí roviny (RRC, NAS) odděleně od uživatelských dat
- Zahrnuje typy logických kanálů pro vysílání (BCCH), volání (PCCH), společný řídicí kanál (CCCH) a vyhrazený řídicí kanál (DCCH)
- Mapován na transportní a fyzické kanály prostřednictvím procedur vrstvy MAC a PHY
- Zajišťuje vysokou spolehlivost a prioritu pro kritické síťové příkazy
- Podporuje nezbytné procedury: získání systémových informací, náhodný přístup, navazování spojení, předání a hlášení měření
- Chráněn ochranou integrity a šifrováním (pro DCCH) na RRC vrstvě

## Související pojmy

- [BCCH – Broadcast Control Channel](/mobilnisite/slovnik/bcch/)
- [DCCH – Dedicated Control Channel](/mobilnisite/slovnik/dcch/)
- [CCCH – Common Control Channel](/mobilnisite/slovnik/ccch/)
- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 25.301** (Rel-19) — UE-UTRAN Radio Interface Protocol Architecture
- **TS 25.302** (Rel-19) — UTRA Physical Layer Services
- **TS 25.322** (Rel-19) — RLC Protocol Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications
- **TS 36.855** (Rel-13) — E-UTRA Positioning Enhancements Study

---

📖 **Anglický originál a plná specifikace:** [CCH na 3GPP Explorer](https://3gpp-explorer.com/glossary/cch/)
