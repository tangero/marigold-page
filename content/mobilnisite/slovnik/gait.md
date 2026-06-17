---
slug: "gait"
url: "/mobilnisite/slovnik/gait/"
type: "slovnik"
title: "GAIT – GSM/ANSI-136 Interoperability"
date: 2025-01-01
abbr: "GAIT"
fullName: "GSM/ANSI-136 Interoperability"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/gait/"
summary: "GAIT (GSM/ANSI-136 Interoperability) je specifikace 3GPP umožňující dvou režimovým mobilním telefonům bezproblémově fungovat napříč sítěmi GSM a ANSI-136 (TDMA). Byla klíčová pro globální roaming a ko"
---

GAIT je specifikace 3GPP umožňující dvou režimovým mobilním telefonům bezproblémově fungovat napříč sítěmi GSM a ANSI-136 (TDMA) pro globální roaming a kontinuitu služeb.

## Popis

GAIT, standardizovaný v 3GPP Release 7, definuje komplexní rámec interoperability pro dvou režimové mobilní stanice schopné fungovat na sítích GSM (Global System for Mobile Communications) i ANSI-136 (American National Standards Institute 136, známý také jako TDMA - Time Division [Multiple Access](/mobilnisite/slovnik/multiple-access/)). Architektura je založena na mobilní stanici podporující GAIT, která obsahuje dvojité rádiové transceivery a sofistikované protokolové zásobníky pro zvládnutí odlišných specifikací rádiového rozhraní, modulačních schémat a síťových signalizačních procedur obou systémů. Mezi klíčové komponenty patří dvou režimový modul identifikace účastníka (SIM) podporující funkce GSM SIM a ANSI-136 R-UIM (Removable User Identity Module) spolu s inteligentními algoritmy pro výběr sítě, které automaticky volí preferovaný systém na základě nastavení operátora, síly signálu a dostupnosti služeb.

Technologie funguje pomocí vrstvového přístupu k protokolům, kde mobilní stanice spravuje paralelní instance protokolů vrstvy 1 (fyzická vrstva), vrstvy 2 (linková vrstva) a vrstvy 3 (síťová vrstva) pro každý systém. Po zapnutí provádí GAIT mobil skenování a výběr systému podle předdefinovaných prioritních seznamů uložených v SIM nebo paměti zařízení. Jakmile se připojí k síti, udržuje, je-li to možné, registrační stavy v obou systémech, což umožňuje bezproblémové možnosti předávání hovorů mezi sítěmi GSM a ANSI-136 prostřednictvím mezisystémových signalizačních procedur definovaných ve specifikaci. Mobilní stanice zpracovává postupy autentizace, šifrování a správy mobility odpovídající každému typu sítě a podle potřeby překládá mezi různými formáty zpráv a sekvencemi protokolů.

V síťové architektuře vyžaduje GAIT podporu od síťových prvků GSM i ANSI-136, včetně základnových stanic, ústředen a domovských registrů polohy. Zatímco samotné sítě zůstávají z velké části nezměněny, interoperability je dosažena díky dvou režimovým schopnostem telefonu a koordinovanému zajištění mezi operátory různých technologií. Specifikace definuje postupy pro mezisystémový provoz týkající se výběru/převýběru buňky, aktualizace polohy, předávání hovorů a navázání/ukončení hovoru napříč oběma technologiemi. Role GAIT byla zvláště důležitá během přechodného období, kdy mnoho operátorů migrovalo ze sítí ANSI-136 na sítě GSM/UMTS, což jim umožnilo udržovat služby pro stávající účastníky sítě TDMA při současném rozšiřování infrastruktury GSM.

## K čemu slouží

GAIT byl vytvořen, aby řešil fragmentaci mezi dvěma dominantními technologiemi celulárních sítí 2G po celém světě: GSM (převládající v Evropě, Asii a stále více globálně) a ANSI-136/TDMA (převládající v Severní a Jižní Americe). Tato technologická propast vytvářela významné překážky pro globální roaming, protože účastníci z regionů GSM nemohli používat své telefony na územích s ANSI-136 a naopak. Specifikace vznikla během období konsolidace odvětví a migrace technologií, kdy mnoho operátorů ANSI-136 plánovalo přechod na sítě GSM a později UMTS.

Primární problémy, které GAIT řešil, zahrnovaly umožnění skutečného globálního roamingu pro účastníky, snížení potřeby více telefonů při cestování mezi technologickými regiony a usnadnění plynulejší migrace sítí pro operátory. Před GAIT potřebovali účastníci samostatná zařízení pro sítě GSM a ANSI-136 nebo se spoléhali na omezené roamingové dohody, které často poskytovaly neoptimální služby. Pro operátory poskytl GAIT cestu k postupnému převedení své základny účastníků z ANSI-136 na GSM bez nutnosti okamžité výměny zařízení, čímž se snížil odliv zákazníků a kapitálové výdaje. Specifikace také řešila obchodní potřebu výrobců telefonů vytvářet zařízení s širší přitažlivostí pro trh díky podpoře obou hlavních standardů 2G v jednom produktu.

Historicky GAIT představoval pragmatické řešení během sbližování celulárních standardů na počátku 21. století. Zatímco technologie 3G se objevovaly, instalovaná základna sítí 2G zůstávala obrovská a odvětví potřebovalo řešení interoperability, která by mohla překlenout více technologických generací. GAIT tuto potřebu naplnil tím, že poskytl standardizované postupy zajišťující předvídatelný výkon a kompatibilitu napříč implementacemi různých výrobců, což nakonec podpořilo přechod odvětví k jednotnějším globálním standardům.

## Klíčové vlastnosti

- Dvou režimový provoz podporující obě rádiová rozhraní GSM a ANSI-136
- Automatický výběr sítě na základě uložených preferenčních seznamů
- Možnosti mezisystémového předávání hovorů mezi sítěmi GSM a ANSI-136
- Sjednocená správa identity účastníka napříč oběma technologiemi
- Podpora kontinuity služeb během technologických přechodů
- Standardizované postupy testování a certifikace pro interoperabilitu

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TR 22.936** (Rel-19) — Multi-system terminal behavior study

---

📖 **Anglický originál a plná specifikace:** [GAIT na 3GPP Explorer](https://3gpp-explorer.com/glossary/gait/)
