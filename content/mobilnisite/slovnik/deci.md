---
slug: "deci"
url: "/mobilnisite/slovnik/deci/"
type: "slovnik"
title: "DECi – Dynamic Error Condition #i for Dynamic C/I conditions"
date: 2025-01-01
abbr: "DECi"
fullName: "Dynamic Error Condition #i for Dynamic C/I conditions"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/deci/"
summary: "DECi je standardizovaná testovací podmínka definovaná v 3GPP pro hodnocení výkonu řečového kodeku za dynamických scénářů poměru nosná/rušení (C/I). Simuluje realistické změny rádiového kanálu k posouz"
---

DECi je standardizovaná 3GPP testovací podmínka pro hodnocení výkonu řečového kodeku za dynamických scénářů poměru nosná/rušení (C/I) za účelem posouzení odolnosti a kvality v mobilních prostředích.

## Popis

DECi, neboli Dynamic Error Condition #i (dynamická chybová podmínka č. i) pro dynamické [C/I](/mobilnisite/slovnik/c-i/) podmínky, je specifická testovací metodologie standardizovaná v 3GPP TS 26.077 pro hodnocení výkonu řečových kodeků. Patří do rodiny testovacích podmínek navržených k simulaci dynamických a často náročných rádiových prostředí, s nimiž se setkáváme v mobilní komunikaci. Písmeno 'i' v DECi představuje specifický index nebo konfiguraci v rámci sady předdefinovaných dynamických chybových podmínek, z nichž každá je charakterizována konkrétním vzorem časových změn poměru nosná/rušení (C/I). Tyto vzory modelují kolísající kvalitu signálu, kterou uživatel zažívá vlivem faktorů, jako je pohyb, útlum a rušení.

Jádrem DECi je aplikace časově proměnného chybového vzoru na bitový proud představující zakódovanou řeč. Tento vzor není jednoduchá statická míra bitových chyb, ale sekvence napodobující to, jak se poměr C/I – a následně i chybové charakteristiky kanálu – dynamicky mění. Testovací zařízení nebo simulační framework zavádí chyby do přenášeného bitového proudu podle tohoto předdefinovaného DECi vzoru. Poškozený bitový proud je následně dekódován testovaným řečovým kodekem. Výstupní kvalita řeči je hodnocena pomocí subjektivních poslechových testů (jako je Mean Opinion Score – [MOS](/mobilnisite/slovnik/mos/)) nebo objektivních percepčních měr kvality (jako je Perceptual Evaluation of Speech Quality – PESQ).

Z architektonického hlediska je DECi implementováno v rámci frameworků pro testování shody a benchmarkování výkonu řečových kodeků. Mezi klíčové komponenty patří generátor testovacích sekvencí vytvářející DECi chybový vzor, simulátor kanálu aplikující tento vzor k poškození bitového proudu, dekodér kodeku, který musí zpracovat poškozená data, a modul pro hodnocení kvality. Jeho úlohou je poskytnout reprodukovatelný, standardizovaný zátěžový test, který posouvá kodeky za ideální statické podmínky a odhaluje, jak dobře fungují mechanismy pro maskování chyb, zpracování vymazaných rámců a další mechanismy odolnosti.

Testováním v podmínkách DECi mohou inženýři ověřit, že řečový kodek (např. [AMR](/mobilnisite/slovnik/amr/), [AMR-WB](/mobilnisite/slovnik/amr-wb/), [EVS](/mobilnisite/slovnik/evs/)) udržuje přijatelnou kvalitu i při nedokonalém a rychle se měnícím rádiovém spojení. To je klíčové pro zajištění konzistentní kvality hlasové služby v reálných nasazeních, kde se uživatelé pohybují mezi buňkami, zažívají stínění signálu nebo se setkávají s rušením. Framework DECi umožňuje komparativní analýzu různých kodeků nebo režimů kodeků, což usměrňuje výběr a konfiguraci pro optimální výkon v různorodých provozních podmínkách mobilní sítě.

## K čemu slouží

DECi bylo vytvořeno, aby řešilo omezení testování řečových kodeků za statických chybových podmínek v mobilních systémech. Rané testování kodeků často spoléhalo na testy se statickou mírou bitových chyb ([BER](/mobilnisite/slovnik/ber/)) nebo mírou vymazání rámců ([FER](/mobilnisite/slovnik/fer/)), které přesně neodrážely časově proměnnou povahu zhoršení rádiového kanálu v živé síti. Poměr [C/I](/mobilnisite/slovnik/c-i/) v mobilním prostředí se dynamicky mění vlivem rychlého útlumu, pomalého útlumu, přechodů mezi buňkami a rušení. Kodek, který dobře funguje při konstantní FER 1 %, může katastrofálně selhat při vzoru s chybovými shluky, kdy je ztraceno několik po sobě jdoucích rámců. DECi poskytuje standardizovaný, realistický dynamický model k odhalení takových slabin.

Motivace vycházela z potřeby garantovat kvalitu hlasu koncového uživatele v 3GPP systémech, jako jsou UMTS a LTE, zejména pro služby přepojování okruhů a později Voice over LTE (VoLTE). S vývojem sítí si zajištění vysoké kvality hlasu – základní služby – vyžádalo sofistikovanější testovací metodologie. DECi, zavedené ve verzi 8 spolu s pokroky v řečových kodecích jako AMR-WB, umožnilo důkladné benchmarkování za podmínek napodobujících skutečný uživatelský zážitek při pohybu a na okraji buňky. Vyřešilo problém nedostatečné predikce výkonu a umožnilo síťovým operátorům a výrobcům zařízení vybírat a implementovat kodeky, které poskytují spolehlivou kvalitu hlasu nejen v laboratorně dokonalých podmínkách, ale i v náročných a proměnlivých rádiových podmínkách reálného světa.

Historicky bylo vytvoření DECi a jeho zařazení do TS 26.077 součástí širšího úsilí 3GPP o standardizaci charakterizace výkonu řečových a audiokodeků. Zaplnilo kritickou mezeru mezi jednoduchými modely kanálu používanými při testování fyzické vrstvy a potřebou záruk výkonu na aplikační vrstvě (kvalita řeči). Definováním konkrétních dynamických C/I podmínek poskytlo společný jazyk a testovací benchmark pro průmysl, což pohánělo zlepšování v algoritmech odolnosti a schopnosti vyrovnávat se s chybami kodeků.

## Klíčové vlastnosti

- Standardizované vzory dynamických změn C/I pro reprodukovatelné testování
- Modeluje realistické časově proměnné degradace rádiového kanálu, jako je útlum
- Hodnotí odolnost řečového kodeku a schopnosti maskování chyb
- Používá se pro subjektivní (MOS) a objektivní (např. PESQ) hodnocení kvality
- Podporuje benchmarkování výkonu různých kodeků (AMR, EVS) a jejich režimů
- Integruje se do 3GPP frameworků pro testy shody a výkonu

## Definující specifikace

- **TS 26.077** (Rel-19) — AMR Noise Suppression Minimum Performance Requirements

---

📖 **Anglický originál a plná specifikace:** [DECi na 3GPP Explorer](https://3gpp-explorer.com/glossary/deci/)
