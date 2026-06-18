---
slug: "remap"
url: "/mobilnisite/slovnik/remap/"
type: "slovnik"
title: "REMAP – Remap Frame"
date: 2025-01-01
abbr: "REMAP"
fullName: "Remap Frame"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/remap/"
summary: "REMAP je specifická struktura rámce definovaná v dokumentu 3GPP TS 24.022 pro protokol rádiového spoje (RLP) v okruhově spínaných datových službách GSM a UMTS. Používá se pro signalizační a řídicí úče"
---

REMAP je specifická struktura rámce protokolu rádiového spoje (Radio Link Protocol) používaná pro signalizaci a řízení za účelem správy spolehlivého přenosu dat v okruhově spínaných sítích GSM a UMTS.

## Popis

Rámec REMAP je základní součástí protokolu rádiového spoje ([RLP](/mobilnisite/slovnik/rlp/)) podle specifikace 3GPP TS 24.022. RLP funguje na vrstvě spojení datového spoje (vrstva 2) a je zodpovědný za poskytování spolehlivé služby doručování dat ve správném pořadí přes inherentně náchylné k chybám rozhraní rádiového přenosu v okruhově spínaných datových službách GSM a UMTS, jako je fax nebo netransparentní datová volání. Rámec REMAP je jedním z několika typů rámců RLP, konkrétně navrženým pro řídicí a signalizační funkce, nikoliv pro přenos uživatelských dat.

Z architektonického hlediska se RLP nachází mezi fyzickou vrstvou a protokoly vyšších vrstev. Používá rámcovou strukturu pro segmentaci a opětovné složení datových bloků, správu potvrzení a provádění opravy chyb prostřednictvím retransmisí. Rámec REMAP obsahuje řídicí informace nezbytné pro činnost RLP. To zahrnuje pole pro pořadová čísla, identifikaci typu rámce a řídicí parametry, které řídí stavový automat protokolu, jako jsou příkazy pro reset nebo instrukce pro správu okna. Struktura rámce zahrnuje hlavičku s potřebnými řídicími bity a může obsahovat volitelné informační pole pro specifické příkazy.

Během provozu, když entita RLP potřebuje signalizovat změnu stavu protokolu, zahájit procedury obnovy nebo vyměnit řídicí parametry se svým protějškem, vygeneruje a odešle rámec REMAP. Například, pokud jsou detekovány nadměrné chyby, může být rámec REMAP použit k příkazu resetování číslování sekvencí nebo k úpravě velikosti přenosového okna. Příjem rámce REMAP spouští specifické akce v přijímající entitě RLP, čímž zajišťuje, že oba konce spoje zůstanou synchronizované a mohou se zotavit z chyb. Jeho role je kritická pro udržení logického spoje, správu řízení toku a zajištění spolehlivé služby přenosu dat, na kterou spoléhají aplikace vyšších vrstev, i když se podmínky rádiového přenosu mění.

## K čemu slouží

Rámec REMAP byl zaveden, aby řešil potřebu robustní signalizace v pásmu (in-band) v rámci protokolu rádiového spoje pro okruhově spínané datové služby GSM. Rané mobilní datové služby vyžadovaly mechanismus pro spolehlivou správu datového spoje přes nespolehlivý rádiový kanál. Pouhé datové rámce byly nedostatečné; byl nutný vyhrazený řídicí rámec pro koordinaci dvou protějšků [RLP](/mobilnisite/slovnik/rlp/), zvládání chybových scénářů a správu parametrů protokolu bez poškození proudů uživatelských dat.

Před standardizovanými protokoly, jako je RLP, byl přenos dat přes rádiové rozhraní náchylný k vysoké chybovosti a vyžadoval složitá proprietární řešení na vrstvě spojení. Vytvoření RLP a v jeho rámci rámce REMAP poskytlo standardizovanou, spolehlivou metodu pro přenos dat. Rámec REMAP konkrétně řeší problém koordinace protokolu. Umožňuje protějškům vyměňovat si řídicí informace – jako jsou požadavky na reset nebo aktualizace okna – plynule v rámci stejného logického kanálu používaného pro data, čímž zajišťuje, že se spoj může přizpůsobit měnícím se podmínkám a zotavit se z poruch bez nutnosti zásahu vyšších vrstev. To bylo zásadní pro podporu faxu, vytáčeného připojení a dalších okruhově spínaných přenosových služeb, u kterých se očekávalo spolehlivé fungování přes mobilní sítě.

## Klíčové vlastnosti

- Definovaný typ řídicího rámce v rámci protokolu rádiového spoje (RLP)
- Přenáší signalizační a řídicí informace mezi entitami RLP
- Používá se pro synchronizaci stavu protokolu a procedury obnovy po chybě
- Obsahuje pole pro pořadová čísla a řídicí příkazy
- Funguje přes rozhraní Um (rádiové) v sítích GSM/UMTS
- Nezbytný pro provoz spolehlivé okruhově spínané datové služby

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 24.022** (Rel-19) — Radio Link Protocol (RLP) for Circuit Switched Data

---

📖 **Anglický originál a plná specifikace:** [REMAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/remap/)
