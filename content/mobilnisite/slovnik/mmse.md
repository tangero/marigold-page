---
slug: "mmse"
url: "/mobilnisite/slovnik/mmse/"
type: "slovnik"
title: "MMSE – Multimedia Messaging Service Environment"
date: 2025-01-01
abbr: "MMSE"
fullName: "Multimedia Messaging Service Environment"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/mmse/"
summary: "Kompletní soubor síťových prvků, rozhraní a protokolů, které společně umožňují službu multimediálních zpráv (MMS). Zahrnuje MMSC, přidružené databáze, funkce pro propojování a připojení k externím sít"
---

MMSE je kompletní soubor síťových prvků, rozhraní a protokolů, které společně umožňují službu multimediálních zpráv (Multimedia Messaging Service).

## Popis

Multimedia Messaging Service Environment (MMSE) označuje celou systémovou architekturu a soubor funkčních entit potřebných k poskytování služby multimediálních zpráv. Nejde o jediný uzel, ale o logické prostředí zahrnující několik klíčových komponent definovaných specifikacemi 3GPP. Ústřední entitou je Multimedia Messaging Service Centre (MMSC), který se sám skládá z [MMS](/mobilnisite/slovnik/mms/) Relay a MMS Server. MMS Relay je zodpovědné za směrování, přenos a adaptaci zpráv mezi různými entitami, zatímco MMS Server zvládá funkce ukládání, například dočasné uložení zpráv, když je příjemce nedostupný. Kromě MMSC zahrnuje MMSE další kritické síťové prvky, jako jsou MMS User Databases (které ukládají uživatelské profily a nastavení specifická pro MMS), a různé funkce pro propojování.

Prostředí funguje prostřednictvím souboru standardizovaných referenčních bodů (rozhraní), označených MM1 až MM8. MM1 je rozhraní mezi MMS User Agent (na koncovém zařízení) a MMS Relay/Server, používané pro odesílání, doručování a oznamování zpráv, typicky implementované přes WAP nebo [HTTP](/mobilnisite/slovnik/http/). MM3 je rozhraní pro připojení MMSC k externím serverům, jako jsou emailové servery (SMTP) nebo jiné systémy zasílání zpráv. MM4 je klíčové rozhraní pro výměnu MMS mezi operátory, které umožňuje MMSC v jedné síti předat zprávy MMSC v jiné síti. MM5 je rozhraní k databázím účastníků, jako je [HLR](/mobilnisite/slovnik/hlr/) nebo [HSS](/mobilnisite/slovnik/hss/), pro informace o směrování a poskytování služeb. MM7 je rozhraní pro poskytovatele služeb s přidanou hodnotou (VASP) pro odesílání zpráv (např. pro služby doručování obsahu). Tato rozhraní zajišťují interoperabilitu jak v rámci sítě jednoho operátora, tak mezi různými operátory po celém světě.

Z procesního hlediska MMSE spravuje kompletní životní cyklus MMS. To zahrnuje odeslání zprávy z User Agent odesílatele, překlad adres a směrování (potenciálně zahrnující komunikaci mezi operátory), adaptaci a překódování médií podle schopností zařízení příjemce, uložení, oznámení příjemci a konečné doručení nebo načtení. Prostředí také integruje s účtovacími systémy (přes rozhraní jako MM8) pro generování záznamů pro účtování transakcí se zprávami. MMSE tedy představuje kompletní backendovou infrastrukturu, která umožňuje službu MMS, a skrývá její složitost před koncovým uživatelem, který jednoduše používá aplikaci MMS ve svém telefonu.

## K čemu slouží

Koncept Multimedia Messaging Service Environment byl definován, aby poskytl komplexní, standardizovaný rámec pro nasazení [MMS](/mobilnisite/slovnik/mms/). Bez standardizovaného prostředí by každý výrobce nebo operátor mohl službu implementovat pomocí proprietární architektury a rozhraní, což by vedlo k fragmentaci a neschopnosti účastníků na různých sítích si vyměňovat multimediální zprávy. Specifikace MMSE tento problém vyřešila definováním jasného, interoperabilního ekosystému, kde jsou všechny funkční entity a rozhraní mezi nimi standardizovány.

Tento přístup řešil několik klíčových problémů. Zajistil, že koncová zařízení od jakéhokoli výrobce se mohou připojit k jakémukoli MMSC vyhovujícímu standardu. Umožnil globální interoperabilitu mezi mobilními operátory přísnou definicí rozhraní MM4 pro výměnu zpráv mezi operátory. Také usnadnil vytvoření živého ekosystému pro služby s přidanou hodnotou definicí rozhraní MM7 pro poskytovatele obsahu třetích stran. Vytvořením tohoto holistického prostředí umožnila 3GPP rychlé a rozšířené nasazení MMS jako globálně konzistentní služby, což bylo klíčové pro její komerční úspěch a přijetí uživateli v letech 2000.

## Klíčové vlastnosti

- Zahrnuje všechny síťové entity: MMSC (Relay/Server), uživatelské databáze, rozhraní pro VASP
- Definuje kompletní sadu standardizovaných referenčních bodů (MM1-MM8) pro interoperabilitu
- Podporuje komplexní zpracování zpráv: odeslání, směrování, adaptaci, uložení, doručení
- Umožňuje zasílání zpráv mezi operátory prostřednictvím standardizovaného rozhraní MM4
- Poskytuje rozhraní pro externí systémy (email přes MM3) a služby s přidanou hodnotou (MM7)
- Integruje se s databázemi účastníků v jádru sítě (HLR/HSS přes MM5) pro řízení služeb

## Definující specifikace

- **TS 23.140** (Rel-6) — MMS Non-Realtime Service Definition
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.270** (Rel-19) — MMS Charging Management Specification
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 36.306** (Rel-19) — E-UTRA UE Radio Access Capability Parameters
- **TS 36.867** (Rel-13) — LTE DL 4 Rx Antenna Port Study TR
- **TS 36.884** (Rel-13) — MMSE-IRC Receiver Performance for LTE BS
- **TR 38.812** (Rel-16) — Study on NOMA for NR
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study
- **TR 38.922** (Rel-19) — Study on IMT Parameters for NR in Higher Bands

---

📖 **Anglický originál a plná specifikace:** [MMSE na 3GPP Explorer](https://3gpp-explorer.com/glossary/mmse/)
