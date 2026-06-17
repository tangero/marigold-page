---
slug: "hpl"
url: "/mobilnisite/slovnik/hpl/"
type: "slovnik"
title: "HPL – Horizontal Protection Level"
date: 2025-01-01
abbr: "HPL"
fullName: "Horizontal Protection Level"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/hpl/"
summary: "Horizontal Protection Level (HPL, úroveň horizontální ochrany) je klíčová metrika integrity v systémech určování polohy. Představuje poloměr kružnice, u níž je zaručeno, že obsahuje skutečnou horizont"
---

HPL je poloměr kružnice, u níž je zaručeno, že obsahuje skutečnou horizontální polohu se stanovenou úrovní spolehlivosti; používá se jako metrika integrity pro služby vysoce přesného určování polohy v 3GPP.

## Popis

Horizontal Protection Level (HPL, úroveň horizontální ochrany) je statistická míra integrity (důvěryhodnosti) vypočteného horizontálního určení polohy. Nejde o samotnou chybu polohy, ale o horní mez horizontální chyby polohy, kterou v reálném čase vypočítává systém určování polohy. Konkrétně HPL definuje poloměr kružnice se středem v odhadované poloze, uvnitř které se skutečná horizontální poloha zařízení nachází s velmi vysokou pravděpodobností (např. 99,999 %). Pokud HPL překročí předdefinovaný výstražný limit (alert limit) pro danou aplikaci, systém musí vydat výstrahu integrity, což signalizuje, že určení polohy není pro bezpečné použití dostatečně spolehlivé.

Ve specifikacích 3GPP, zavedených ve verzi 17 pro rozšířené služby určování polohy, je HPL součástí širšího rámce pro určování polohy s vysokou integritou. Výpočet HPL typicky zahrnuje analýzu geometrie použitých satelitů nebo základnových stanic (Geometric Dilution of Precision – [GDOP](/mobilnisite/slovnik/gdop/)), odhadovaných chyb měření vzdálenosti (zbytky pseudovzdálenosti) a známé modely chyb pro každý zdroj signálu. Pro určování polohy založené na [GNSS](/mobilnisite/slovnik/gnss/) se zohledňují faktory jako chyby satelitních hodin/efemerid, ionosférické zpoždění a šum přijímače. Pro pozemní určování polohy (např. pomocí signálů LTE nebo NR) se uvažují chyby z časového předstihu (timing advance), měření úhlu příchodu a vícecestného šíření. Polohovací engine, který může být v zařízení (UE-based) nebo v síti (UE-assisted), tyto výpočty provádí a poskytuje jak odhad polohy, tak přidružený HPL.

Role HPL v rámci architektury 3GPP je spojena se službami určování polohy ([LCS](/mobilnisite/slovnik/lcs/)) a funkcí Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)). Když aplikace (jako autonomní systém vozidla) požaduje polohu s vysokou integritou, LMF nebo polohovací engine v UE musí spolu se souřadnicemi poskytnout i HPL. Aplikace následně porovná HPL se svým vlastním Horizontal Alert Limit ([HAL](/mobilnisite/slovnik/hal/)). Pokud platí HPL < HAL, je určení polohy považováno za použitelné. Toto monitorování integrity je kontinuální. Specifikace (např. TS 37.355 pro LTE positioning protocol a TS 38.857 pro NR positioning) definují, jak se data související s HPL (jako modely chyb a úrovně spolehlivosti) přenášejí mezi sítí a UE, aby podpořily tyto výpočty pro různé metody určování polohy včetně [A-GNSS](/mobilnisite/slovnik/a-gnss/), [OTDOA](/mobilnisite/slovnik/otdoa/) a multi-RTT.

## K čemu slouží

Snaha o standardizaci Horizontal Protection Level v rámci 3GPP, počínaje verzí 17, byla motivována přísnými požadavky nových vertikálních aplikací závislých na vysoce spolehlivém a přesném určování polohy. Zatímco tradiční určování polohy v celulárních sítích (např. pro tísňové služby nebo základní služby založené na poloze) se soustředilo především na přesnost, aplikace jako autonomní vozidla, pokročilé operace dronů a průmyslová automatizace vyžadují jak vysokou přesnost, tak garantovanou integritu. Integrita odpovídá na kritickou otázku: „Mohu tomuto určení polohy dostatečně věřit, abych na jeho základě učinil rozhodnutí kritické z hlediska bezpečnosti?“

Před formálním zahrnutím poskytovaly specifikace 3GPP pro určování polohy odhady přesnosti, ale postrádaly standardizovaný rámec pro metriky integrity, jako je HPL. To byla překážka pro aplikace, kde jde o bezpečnost života, které vyžadují soulad se standardy jako jsou ty z letectví (RAIM) nebo automobilového průmyslu ([ISO](/mobilnisite/slovnik/iso/) 26262). Zavedení HPL tuto mezeru zaplňuje. Umožňuje celulárním sítím – ať už samostatným, nebo jako doplněk či náhrada GNSS – poskytovat služby určování polohy se známými, ohraničenými úrovněmi chyb. To je obzvláště důležité v městských kaňonech nebo jiných prostředích s omezeným příjmem GNSS, kde mohou celulární signály zlepšit dostupnost. Definováním HPL umožňuje 3GPP jednotný integritní rámec napříč hybridními zdroji určování polohy (GNSS + pozemní), což usnadňuje vývoj spolehlivých polohovacích řešení pro V2X, UAV a další klíčové IoT případy užití, které tvoří jádro evoluce 5G-Advanced.

## Klíčové vlastnosti

- Statistická mez horizontální chyby polohy pro danou úroveň spolehlivosti
- Základní součást monitorování integrity polohovacího systému
- Vypočítává se v reálném čase na základě geometrie měření a modelů chyb
- Porovnává se s aplikačně specifickým Horizontal Alert Limit (HAL)
- Podporuje metody určování polohy založené na GNSS i pozemní (LTE/NR)
- Standardizováno v 3GPP pro služby určování polohy s vysokou integritou

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TR 38.857** (Rel-17) — Study on NR Positioning Enhancements

---

📖 **Anglický originál a plná specifikace:** [HPL na 3GPP Explorer](https://3gpp-explorer.com/glossary/hpl/)
