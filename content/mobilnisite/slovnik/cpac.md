---
slug: "cpac"
url: "/mobilnisite/slovnik/cpac/"
type: "slovnik"
title: "CPAC – Conditional PSCell Addition or Change"
date: 2026-01-01
abbr: "CPAC"
fullName: "Conditional PSCell Addition or Change"
category: "Mobility"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/cpac/"
summary: "Vylepšení mobility v 5G NR Duální konektivitě (EN-DC, NR-DC) a Multi-RAT Duální konektivitě (MR-DC), které umožňuje UE připravit a vyhodnotit kandidátské PSCelly před provedením změny. Zvyšuje spolehl"
---

CPAC je vylepšení mobility pro 5G v režimu duální konektivity, které umožňuje UE připravit kandidátské PSCelly a podmíněně provést jejich přidání nebo změnu na základě rádiových měření za účelem zvýšení spolehlivosti a snížení přerušení spojení.

## Popis

Conditional PSCell Addition or Change (CPAC) je sofistikovaný postup mobility zavedený ve specifikaci 3GPP Release 17 pro scénáře využívající Duální konektivitu ([DC](/mobilnisite/slovnik/dc/)), konkrétně E-UTRA-NR Duální konektivitu ([EN-DC](/mobilnisite/slovnik/en-dc/)) a NR-NR Duální konektivitu ([NR-DC](/mobilnisite/slovnik/nr-dc/)). Rozšiřuje principy Podmíněného předání spojení ([CHO](/mobilnisite/slovnik/cho/)) na správu primární vedlejší buňky (PSCell) v rámci sekundárního uzlu (SN) v konfiguraci DC. Základní koncept spočívá v tom, že síť může předkonfigurovat uživatelské zařízení (UE) s jedním nebo více kandidátskými PSCelly spolu se specifickými podmínkami provedení, typicky založenými na prahových hodnotách rádiových měření (např. RSRP, RSRQ). UE poté autonomně monitoruje tyto podmínky pro kandidátské buňky při zachování svého současného spojení. Když je splněna podmínka pro kandidátský PSCell, UE provede přidání nebo změnu PSCell bez nutnosti další signalizace od sítě v okamžiku provedení, čímž se sníží latence a riziko selhání během kritické fáze přechodu.

Z architektonického hlediska se CPAC týká koordinace mezi hlavním uzlem ([MN](/mobilnisite/slovnik/mn/)) a kandidátským sekundárním uzlem (C-SN). Postup je iniciován MN, který požaduje přípravu zdrojů kandidátského PSCell od jednoho nebo více C-SN prostřednictvím rozhraní Xn (nebo X2 v případě EN-DC). C-SN poskytne nezbytnou konfiguraci, včetně identity buňky nového PSCell, konfigurace přenosových kanálů a bezpečnostních parametrů, které jsou zapouzdřeny v příkazu 'Conditional PSCell Addition/Change' odeslaném UE prostřednictvím [RRC](/mobilnisite/slovnik/rrc/) signalizace z MN. Tento příkaz zahrnuje podmínku (podmínky) provedení pro každého kandidáta. UE tuto konfiguraci uloží a začne vyhodnocovat podmínky. Mezi klíčové zprávy RRC patří zpráva RRCReconfiguration pro doručení konfigurace CPAC a následná zpráva RRCReconfigurationComplete po úspěšném provedení.

Fáze provedení je řízena UE. Po splnění podmínky UE provede synchronizaci a proceduru náhodného přístupu k cílovému PSCell, aplikuje uloženou konfiguraci a uvolní zdroje starého PSCell, pokud je to relevantní. Poté informuje MN o úspěšné změně prostřednictvím zprávy RRCReconfigurationComplete. Síť následně aktualizuje svůj kontext a může zahájit procedury přesměrování dat a přepnutí přenosové cesty. CPAC je zvláště užitečný v prostředích s vysokou mobilitou nebo náročnými rádiovými podmínkami, kde se podmínky pro současný PSCell mohou rychle zhoršovat. Přípravou alternativ předem CPAC zvyšuje robustnost mobility, minimalizuje přerušení přenosu dat a přispívá k vyšší spolehlivosti a plynulému uživatelskému zážitku v pokročilých 5G sítích využívajících agregaci nosných a duální konektivitu.

## K čemu slouží

CPAC byl vytvořen, aby řešil specifické výzvy robustnosti mobility vlastní nasazením Duální konektivity a Multi-RAT Duální konektivity. V tradičních postupech přidání/změny PSCell typu 'blind' nebo spouštěných měřením je rozhodnutí a provedení řízeno sítí a sekvenční, což může vést k selháním, pokud se rádiové podmínky zhorší rychleji, než síť dokáže zareagovat. To je zvláště problematické pro PSCell, který často pracuje na vyšších frekvencích (např. mmWave) s výraznějšími výkyvy signálu. Primární problém, který CPAC řeší, je snížení míry selhání předání spojení a selhání rádiového spoje (RLF) spojených se sekundárním uzlem, čímž se zlepšuje celková stabilita spojení a kontinuita služby.

Historický kontext vychází z úspěšné aplikace Podmíněného předání spojení ([CHO](/mobilnisite/slovnik/cho/)) pro primární buňku, zavedeného v dřívějších releasech. S ohledem na výhody CHO při snižování selhání předání spojení pro PCell, 3GPP identifikovalo podobnou potřebu pro primární buňku sekundárního uzlu (PSCell) ve scénářích [DC](/mobilnisite/slovnik/dc/). Předchozí přístupy spoléhaly na včasné hlášení měření a síťové zpracování, což zavádělo latenci a jediný bod selhání. Pokud by signalizační cesta byla zpožděna nebo spojení se zdrojovým PSCell selhalo před dokončením, postup by selhal, což by mohlo způsobit přerušení spoje DC. CPAC toto zmírňuje decentralizací rozhodnutí o provedení na UE, které má nejaktuálnější znalosti o svém rádiovém prostředí, což umožňuje rychlejší a spolehlivější přechod při splnění předdefinovaných podmínek.

CPAC dále podporuje vývoj směrem k autonomnějšímu a inteligentnějšímu chování UE v sítích 5G-Advanced. Umožňuje vyrovnávání síťového zatížení a optimalizaci tím, že síti umožňuje předkonfigurovat více kandidátských buněk, potenciálně v různých uzlech nebo frekvenčních vrstvách. To připravuje síť pro případy použití ultra-spolehlivé komunikace s nízkou latencí (URLLC) a scénáře s vysokou mobilitou, jako jsou komunikace v vozidlech, kde je předvídatelná a robustní mobilita nezbytná. Řešením mezery v robustnosti mobility PSCell je CPAC klíčovým enablerem spolehlivé multikonektivity, která je zásadní pro dosažení vysokých datových rychlostí a konzistentního výkonu slibovaného technologií 5G a dalších generací.

## Klíčové vlastnosti

- Předkonfigurace kandidátských PSCell s podmínkami provedení
- Autonomní vyhodnocení a provedení změny PSCell uživatelským zařízením (UE)
- Snížení signalizační latence a pravděpodobnosti selhání předání spojení
- Zvýšená robustnost mobility pro spoje sekundárního uzlu
- Podpora více kandidátských PSCell od jednoho nebo více kandidátských sekundárních uzlů
- Bezproblémová integrace se stávajícími architekturami a signalizačními postupy MR-DC a EN-DC

## Definující specifikace

- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 37.340** (Rel-19) — Multi-Connectivity Operation Overview
- **TS 37.483** (Rel-19) — E1 Application Protocol (E1AP)
- **TS 38.306** (Rel-19) — NR UE Radio Access Capability Parameters
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification
- **TS 38.423** (Rel-19) — Xn Application Protocol (XnAP) specification
- **TS 38.473** (Rel-19) — 5G F1 Application Protocol (F1AP)

---

📖 **Anglický originál a plná specifikace:** [CPAC na 3GPP Explorer](https://3gpp-explorer.com/glossary/cpac/)
