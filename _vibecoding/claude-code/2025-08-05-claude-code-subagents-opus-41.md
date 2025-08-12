---
author: Patrick Zandl
categories:
- AI
- Anthropic
- Claude
- Claude Code
- LLM
layout: vibecoding-default
post_excerpt: Anthropic rozšířil Claude Code o správu kontextu, podporu podsystémů a čtení PDF. Současně vydal vylepšený model Opus 4.1 s lepším výkonem při kódování.
summary_points:
- Claude Code získává automatické čištění volání nástrojů pro delší pracovní relace
- Nová podpora @-mention umožňuje přímé volání specializovaných podagentů
- Přidána přímá podpora čtení PDF souborů ze souborového systému
- Claude Opus 4.1 dosahuje 74,5% úspěšnosti na SWE-bench Verified
- Opus 4.1 zlepšuje refaktoring kódu napříč více soubory
title: Claude Code získává nové funkce pro správu kontextu a Anthropic vydává Opus 4.1
---

Společnost Anthropic, která vyvíjí konverzační umělou inteligenci Claude, představila 4. srpna 2025 tři nové funkce pro svůj vývojářský nástroj [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Následující den pak vydala vylepšenou verzi svého nejpokročilejšího modelu [Claude Opus 4.1](https://www.anthropic.com/news/claude-opus-4-1), který dosahuje lepších výsledků při práci s kódem a logickém uvažování.

## Automatická správa kontextu pomocí funkce Microcompact

První novinkou je funkce Microcompact, která řeší problém postupného zaplňování kontextového okna během dlouhých pracovních relací. Když se kontext začne blížit svému limitu, systém automaticky vymaže starší volání nástrojů, které už nejsou potřebné. To umožňuje pokračovat v práci bez nutnosti úplné kompaktace kontextu, přičemž si zachovává nejdůležitější informace o projektu.

Tato funkce pracuje na pozadí bez nutnosti zásahu uživatele. Vývojáři tak mohou pracovat na rozsáhlejších projektech delší dobu, aniž by museli ručně spravovat historii komunikace nebo restartovat relaci kvůli vyčerpání kontextu.

## Vylepšená práce s podagenty

Druhá novinka se týká práce s podagenty (subagents) - specializovanými pomocníky pro konkrétní úkoly. Claude Code nyní podporuje jejich přímé volání pomocí @-mention syntaxe. Stačí napsat například `@code-reviewer` pro zavolání agenta specializovaného na kontrolu kódu.

Každému podagentovi lze nyní přiřadit konkrétní model podle složitosti jeho úkolů. Pro komplexní plánovací úlohy lze použít výkonnější Opus 4, zatímco pro jednodušší operace postačí rychlejší a levnější Haiku 3.5. Toto nastavení umožňuje optimalizovat spotřebu tokenů a výkon podle skutečných potřeb jednotlivých úloh.

Dokumentace k práci s podagenty je dostupná na [stránkách Anthropic](https://docs.anthropic.com/en/docs/claude-code/sub-agents).

## Přímá podpora PDF souborů

Třetí funkcí je nativní podpora čtení PDF dokumentů. Claude Code nyní dokáže číst PDF soubory přímo ze souborového systému bez nutnosti jejich konverze do jiného formátu. Soubory lze referencovat stejným způsobem jako jakýkoliv jiný typ souboru.

Tato funkce usnadňuje práci s technickou dokumentací, specifikacemi nebo výzkumnými články, které jsou často distribuovány právě ve formátu PDF. Vývojáři tak mohou přímo pracovat s originálními dokumenty bez nutnosti jejich předchozího převodu nebo extrakce textu.

## Claude Opus 4.1 zlepšuje práci s kódem

Anthropic 5. srpna 2025 vydal [Claude Opus 4.1](https://www.anthropic.com/news/claude-opus-4-1), vylepšenou verzi svého nejvýkonnějšího modelu. Hlavní zlepšení se týkají především práce s kódem, kde model dosahuje 74,5% úspěšnosti na benchmarku SWE-bench Verified, což představuje nový rekord společnosti v této oblasti.

Podle zpětné vazby od partnerů model výrazně zlepšuje schopnost refaktoringu kódu napříč více soubory. Společnost Rakuten Group uvádí, že Opus 4.1 dokáže přesně identifikovat potřebné opravy v rozsáhlých kódových základnách bez zbytečných úprav nebo zavlečení chyb. Vývojářský tým Rakutenu preferuje tuto přesnost pro každodenní ladění aplikací.

Platforma Windsurf, která poskytuje vývojářské prostředí s integrací umělé inteligence, reportuje zlepšení o jednu směrodatnou odchylku oproti Opus 4 na jejich benchmarku pro juniorní vývojáře. Toto zlepšení je srovnatelné se skokem mezi modely Sonnet 3.7 a Sonnet 4.

Model je dostupný přes [API Anthropic](https://docs.anthropic.com) s identifikátorem `claude-opus-4-1-20250805`, stejně jako přes Amazon Bedrock a Google Cloud Vertex AI. Cena zůstává stejná jako u předchozí verze Opus 4. Placení uživatelé Claude.ai a uživatelé Claude Code mají k modelu přístup automaticky.

## Benchmarky a metodologie

Opus 4.1 využívá hybridní přístup k uvažování, kdy pro některé úlohy používá rozšířené myšlení s až 64 000 tokeny. Na benchmarku SWE-bench Verified dosahuje uvedených 74,5% bez rozšířeného myšlení, pouze s jednoduchým scaffoldingem obsahujícím bash nástroj a nástroj pro editaci souborů pomocí náhrady řetězců.

Pro benchmark TAU-bench, který testuje schopnosti agentů v reálných scénářích, byl model instruován k lepšímu využití svých schopností uvažování během vícekrokových interakcí. Maximální počet kroků byl zvýšen z 30 na 100, přičemž většina trajektorií se dokončila pod 30 kroky.

Všechny tři nové funkce Claude Code jsou dostupné okamžitě. Pro jejich aktivaci stačí restartovat aplikaci, která si automaticky stáhne nejnovější aktualizaci.