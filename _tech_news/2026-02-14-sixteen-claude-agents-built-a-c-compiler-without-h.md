---
author: Marisa Aigen
category: umělá inteligence
companies:
- Anthropic
date: '2026-02-14 12:00:00'
description: Anthropic nasadil šestnáct AI agentů Claude Opus 4.6 k autonomnímu vývoji
  C kompilátoru v Rustu od nuly. Agenti pracovali paralelně na sdíleném repozitáři,
  koordinovali změny a vytvořili kompilátor schopen sestavit Linux 6.9 kernel pro
  x86, ARM i RISC-V.
importance: 5
layout: tech_news_article
original_title: Sixteen Claude Agents Built a C Compiler Without Human Intervention...
  Almost
publishedAt: '2026-02-14T12:00:00+00:00'
slug: sixteen-claude-agents-built-a-c-compiler-without-h
source:
  emoji: 📰
  id: null
  name: InfoQ.com
title: Šestnáct agentů Claude postavilo C kompilátor bez lidského zásahu... téměř
url: https://www.infoq.com/news/2026/02/claude-built-c-compiler/
urlToImage: https://res.infoq.com/news/2026/02/claude-built-c-compiler/en/headerimage/claude-built-c-compiler-1771067001094.jpeg
urlToImageBackup: https://res.infoq.com/news/2026/02/claude-built-c-compiler/en/headerimage/claude-built-c-compiler-1771067001094.jpeg
---

## Souhrn
Výzkumník Anthropic Nicholas Carlini využil šestnáct AI agentů Claude Opus 4.6 k vytvoření funkčního C kompilátoru napsaného v programovacím jazyce Rust, a to téměř bez jakéhokoli lidského zásahu. Agenti fungovali paralelně na sdíleném Git repozitáři, koordinovali své úpravy a dosáhli kompilátoru, který zvládl sestavení Linuxového jádra verze 6.9 pro procesorové architektury x86, ARM a RISC-V, stejně jako řadu dalších open-source projektů. Celý proces zahrnoval přibližně 2000 relací agentů a náklady na API činily kolem 20 000 dolarů.

## Klíčové body
- Šestnáct paralelních instancí Claude Opus 4.6, každá v samostatném Docker kontejneru, sdílelo Git repozitář pro koordinaci změn.
- Kompilátor v Rustu zkompiloval Linux 6.9 kernel a další projekty, což demonstruje reálnou funkčnost.
- Jednoduchá smyčka udržovala agenty v práci, dokud úkol nedokončily, pak přecházely k dalšímu.
- Žádný lidský zásah během provozu, pouze počáteční setup harnessu pro autonomní fungování.
- Experiment rozšiřuje hranice dlouhodobých autonomních AI týmů v software engineeringu.

## Podrobnosti
Anthropic, firma specializující se na vývoj bezpečných velkých jazykových modelů (LLM), provedl tento experiment pro zkoumání limitů autonomního vývoje softwaru. C kompilátor slouží k převodu zdrojového kódu v jazyce C na strojový kód pro konkrétní procesorovou architekturu, což je základní nástroj pro tvorbu operačních systémů a systémového softwaru. Volba Rustu pro jeho implementaci je logická, protože tento jazyk nabízí paměťovou bezpečnost a vysoký výkon bez garbage collection, což ho činí vhodným pro kompilátory jako je například Rustův vlastní cargo.

Carlini umístil každého agenta do samostatného Docker kontejneru, který zajišťuje izolaci prostředí, ale agenti měli přístup k centrálnímu Git repozitáři pro synchronizaci změn. Klíčovým prvkem byl harness – jednoduchý řídicí cyklus, který agenta nutil pokračovat v práci na úkolu, dokud nebyl dokončen. Pokud model potřeboval objasnění nebo se zasekl, smyčka ho vrátila k úkolu bez čekání na člověka. Tento přístup řeší běžný problém LLM, kdy po částečném řešení dlouhého problému model zastaví a čeká na vstup.

Paralelní provoz dramaticky zkrátil čas: místo sekvenčního zpracování agenti řešili více úkolů současně, jako je návrh parseru, generování kódu pro backend nebo testování. Výsledek je kompilátor, který nejen sestavil Linux 6.9 – jádro podporující širokou škálu hardware – ale i ověřil svou robustnost na reálných projektech. Nicméně Carlini zdůrazňuje, že kompilátor je spíše artefaktem; hlavní hodnota spočívá v metodice pro dlouhodobé autonomní týmy agentů. Experiment ukázal, jak minimalizovat lidskou intervenci při složitých projektech, kde agenti musí koordinovat změny a řešit konflikty v repozitáři.

## Proč je to důležité
Tento pokus posouvá hranice schopností LLM agentů směrem k plně autonomnímu software engineeringu, což má široké implikace pro průmysl. V současnosti AI asistuje programátorům (např. GitHub Copilot generuje kódové snippetty), ale zde agenti zvládli celý projekt od návrhu po funkční produkt, což naznačuje potenciál pro nahrazení rutiních týmů vývojářů. Pro uživatele to znamená rychlejší vývoj open-source nástrojů; pro firmy jako Anthropic nebo OpenAI to otevírá dveře k škálovatelným AI týmům na složité úkoly, jako je tvorba nových kompilátorů nebo optimalizace jáder.

V širším kontextu to přispívá k pokroku směrem AGI tím, že řeší problémy dlouhodobé autonomie a paralelní spolupráce. Kriticky lze poznamenat, že náklady 20 000 dolarů na API ukazují na ekonomické bariéry pro běžné použití, a výsledný kompilátor není konkurenční stávajícím řešením jako GCC kvůli velikosti a optimalizaci. Přesto harnessový design je replikovatelný a může být aplikován na jiné domény, jako robotika nebo datové inženýrství, kde je potřeba dlouhodobá koordinace bez dohledu.

---

[Číst původní článek](https://www.infoq.com/news/2026/02/claude-built-c-compiler/)

**Zdroj:** 📰 InfoQ.com
