---
author: Patrick Zandl
categories:
- AI
- Factory.ai
- CLI
- agenti
- vývoj softwaru
layout: post
post_excerpt: Factory.ai představil Droid, CLI AI agenta pro vývoj softwaru, který dosáhl nejlepšího výsledku 58,75 % v benchmarku Terminal-Bench a je dostupný zdarma.
summary_points:
- Droid od Factory.ai je CLI AI agent pro automatizaci vývoje softwaru v terminálu
- Dosáhl nejlepšího výsledku 58,75 % v benchmarku Terminal-Bench mezi všemi AI agenty
- Podporuje všechny hlavní jazykové modely včetně Claude Opus, GPT-5 a Sonnet
- Zvládá složité úlohy od programování přes správu závislostí až po bezpečnostní úlohy
- Dostupný zdarma s měsíčním zkušebním obdobím na app.factory.ai
title: Droid - CLI AI agent pro vývoj softwaru dosáhl nejlepšího výsledku v benchmarku
---

Společnost Factory.ai, která se specializuje na AI agenty pro vývoj softwaru, představila CLI agent [Droid](https://app.factory.ai), jenž dosáhl nejlepšího výsledku v benchmarku Terminal-Bench s úspěšností 58,75 %. Agent automatizuje složité vývojářské úlohy přímo v příkazové řádce a podporuje všechny hlavní jazykové modely.

## Co je Droid a k čemu slouží

Droid je AI agent navržený pro práci v terminálovém prostředí, který dokáže autonomně řešit široké spektrum vývojářských úloh. Zvládá programování, správu build procesů a závislostí, datové a strojové učení, síťové konfigurace, bezpečnostní úlohy i základní práci s příkazovou řádkou.

Agent pracuje jako asistent, který dokáže porozumět zadání v přirozeném jazyce a přeložit ho do sekvence příkazů a operací potřebných k vyřešení problému. Například dokáže modernizovat build proces ve Fortranu, nakonfigurovat git webový server, vytrénovat reinforcement learning agenty nebo vyčistit repozitář od tajných klíčů.

## Výsledky v benchmarku Terminal-Bench

[Terminal-Bench](https://www.tbench.ai/) je otevřený benchmark hodnotící schopnost AI agentů dokončit složité úlohy v terminálu. Obsahuje 80 lidmi ověřených úloh, z nichž každá má časový limit a je považována za vyřešenou pouze když projdou všechny následné testy.

Droid obsadil první místo s výsledkem 58,8 % mezi všemi testovanými agenty. Překonal i proprietární řešení od vývojářů modelů - Droid s Claude Opus dosáhl 58,8 % oproti Claude Code s 43,2 %, zatímco Droid s GPT-5 dosáhl 52,5 % oproti Codex CLI s 42,8 %.

## Podporované modely a výkon

Droid podporuje všechny hlavní jazykové modely a vývojáři si mohou vybrat podle svých preferencí a rozpočtu:

- **Claude Opus 4.1**: Nejlepší celkový výkon (58,8 %), zvládá i náročné úlohy vyžadující pokročilé ladění a bezpečnostní exploity
- **GPT-5**: Střední výkon (52,5 %), lepší znalosti v oblastech ML a editace videa, výrazně nižší náklady
- **Claude Sonnet 4**: Solidní výkon (50,5 %), vyvážený poměr cena/výkon

Zajímavé je, že architektura Droid dokáže z každého modelu vytěžit více než konkurenční řešení. Levnější model Sonnet v Droid překonává dražší Opus v jiných agentech, což ukazuje důležitost designu agenta nad samotným výběrem modelu.

## Jak Droid pracuje

Agent používa několik pokročilých technik pro zajištění spolehlivého výkonu:

**Plánování úloh**: Droid si vytváří a aktualizuje plán postupu, což mu pomáhá zůstat organizovaný během dlouhých úloh. Každý dokončený krok označí a připomene si, co má dělat dál.

**Povědomí o prostředí**: Při zahájení práce si agent zjistí informace o systému, dostupných programovacích jazycích, obsahu git repozitáře a běžících procesech. Tyto údaje mu pomáhají rychleji se orientovat a vyhýbat se redundantním příkazům.

**Podpora dlouhodobých procesů**: Droid dokáže spouštět služby a servery, které běží na pozadí i po ukončení jeho práce. Všechny spuštěné procesy sleduje pro pozdější úklid.

**Optimalizace rychlosti**: Agent je naladěn na rychlé dokončování úloh. Ví, jak dlouho trvají různé operace, a dokáže volit rychlejší alternativy nebo nastavit inteligentní časové limity.

## Praktické příklady použití

Droid prokázal schopnost řešit reálné problémy, které by jinak vyžadovaly značné úsilí vývojáře:

**Bezpečnostní analýza**: V jednom testu měl za úkol získat MinIO přihlašovací údaje uložené v proměnných prostředí. Zatímco popis úlohy naznačoval jednoduché hledání, skutečné řešení vyžadovalo exploitaci známé zranitelnosti CVE-2023-28432. Droid s Claude Opus tuto zranitelnost spolehlivě rozpoznal a využil.

**Diagnostika sítě**: V jiném případě měl vyřešit problém s curl příkazem. Rychle opravil okamžitý problém, ale také identifikoval hlubší příčinu - simulovaný malware, který opravy rušil. U složitějších modelů dokázal tento základní problém spolehlivě vyřešit.

## Dostupnost a cena

Droid je dostupný ve všech rozhraních Factory.ai s měsíčním zkušebním obdobím zdarma na [app.factory.ai](https://app.factory.ai). Vývojáři mohou pracovat s agentem lokálně i v cloudu a delegovat na něj práci ve větším měřítku.

Finální výsledky, ať už jde o sadu pull requestů, nakonfigurovanou infrastrukturu nebo vyšetřování incidentu, jsou dobře prozkoumané, přesné a ověřené, takže je lze snadno zkontrolovat a nasadit do produkce.

Agent reprezentuje posun v automatizaci vývoje softwaru, kdy jeden vývojář může řídit objem práce celého týmu díky spolehlivému AI asistentovi pracujícímu v terminálovém prostředí.