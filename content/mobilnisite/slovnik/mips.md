---
slug: "mips"
url: "/mobilnisite/slovnik/mips/"
type: "slovnik"
title: "MIPS – Million Instructions Per Second"
date: 2025-01-01
abbr: "MIPS"
fullName: "Million Instructions Per Second"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mips/"
summary: "Obecná metrika pro měření hrubé výpočetní rychlosti centrální procesorové jednotky (CPU), udávající, kolik milionů instrukcí dokáže provést za sekundu. V kontextu 3GPP se používá jako referenční hodno"
---

MIPS je obecná metrika pro měření hrubé rychlosti zpracování CPU v milionech instrukcí za sekundu, používaná v 3GPP jako referenční hodnota pro odhad výpočetního výkonu potřebného pro síťové uzly a uživatelská zařízení k podpoře nových funkcí.

## Popis

Million Instructions Per Second (MIPS) je standardní jednotka měření výkonu [CPU](/mobilnisite/slovnik/cpu/), která představuje počet základních strojových instrukcí, jež procesor dokáže provést za jednu sekundu, počítaný v milionech. V dokumentech standardizace 3GPP není MIPS protokol ani součást síťové architektury, ale praktická technická metrika. Používá se v technických zprávách a studiích proveditelnosti ke kvantifikaci výpočetní složitosti nebo procesní zátěže navrhovaných algoritmů a funkcí. Například při posuzování nové funkce, jako je sofistikovaný šifrovací algoritmus nebo složité schéma kódování kanálu pro mobilní standard, mohou studie odhadnout dodatečné nároky na MIPS potřebné pro její implementaci v cílovém zařízení, jako je základnový procesor v mobilním terminálu nebo karta v uzlu jádra sítě.

Použití MIPS v specifikacích 3GPP se typicky nachází v kontextu systémových požadavků a hodnocení výkonu. Specifikace jako 3GPP TS 22.907 (Požadavky na služby pro V2X) nebo TR 23.977 (Požadavky na služby pro IP multimediální subsystém) mohou odkazovat na MIPS jako součást kritérií pro hodnocení proveditelnosti implementace. Proces zahrnuje analýzu výpočetních kroků navrhované funkce pro zpracování signálu – jako je turbo dekódování, detekce [MIMO](/mobilnisite/slovnik/mimo/) nebo kryptografické operace – a její převedení na odhadovaný rozpočet MIPS. Tento rozpočet je pak porovnán s předpokládanými schopnostmi současné polovodičové technologie, aby se určilo, zda je funkce prakticky realizovatelná pro nasazení v zamýšleném časovém rámci.

Je klíčové si uvědomit, že MIPS je zjednodušená a často kritizovaná metrika, protože různé architektury procesorů (např. RISC vs. CISC) a instrukční sady mohou provádět různý objem práce na instrukci. Její hodnota v 3GPP je proto primárně pro vysokourovňovou srovnávací analýzu a hrubé odhady, nikoli pro přesné záruky výkonu. Metrika pomáhá pracovním skupinám odpovídat na otázky, zda zamýšlená kategorie UE (např. nízkonákladový IoT senzor) nebo síťový prvek (např. virtualizovaná síťová funkce) bude mít dostatečnou výpočetní rezervu pro běh nového softwaru bez překročení cílů nákladů nebo spotřeby energie. Tato analýza podkládá rozhodnutí o tom, zda funkci standardizovat, učinit její podporu povinnou, nebo ji definovat jako volitelnou schopnost.

## K čemu slouží

Účelem odkazování na MIPS ve standardech 3GPP je ukotvit vývoj funkcí a systémový design v praktických realitách hardwarové implementace. Jak se mobilní systémy vyvíjejí, každá nová generace zavádí výpočetně náročnější techniky – jako je modulace vyššího řádu, pokročilé anténní systémy a složité protokolové zásobníky – pro zvýšení přenosových rychlostí, kapacity a funkcionality. Metrika MIPS poskytuje společný, byť přibližný, jazyk pro inženýry, aby mohli diskutovat, zda výpočetní výkon dostupný v křemíkových čipech v době vydání standardu dokáže podpořit tyto nové nároky.

Historicky byl výpočetní výkon významným omezením, zejména pro uživatelská zařízení napájená bateriemi. Rané studie proveditelnosti pro funkce 3G musely zajistit, že algoritmy nejsou pouze teoreticky lepší, ale také implementovatelné v rámci energetického a nákladového rámce komerčních zařízení. Použití MIPS jako referenční hodnoty pomohlo v rané fázi standardizačního procesu identifikovat potenciální závažné překážky. Řešilo to omezení čistě teoretických návrhů, které ignorovaly implementační složitost, a zajistilo, že standardy jsou životaschopné pro reálné produkty.

Motivací pro zahrnutí odhadů MIPS do dokumentů jako TR 21.905 (Slovník pro specifikace 3GPP) a různých technických zpráv je udržovat spojení mezi abstraktním systémovým designem a konkrétním inženýrstvím. Slouží jako kontrola zdravého rozumu, která zajišťuje, že neustálý tlak na vyšší výkon v oblastech, jako je datová propustnost nebo zabezpečení, nepředběhne pokroky v dostupném zpracování podle Moorova zákona. Zohledněním MIPS pomáhá 3GPP vyvažovat inovace s možnostmi nasazení, čímž podporuje standardy, které vedou ke komerčně úspěšným a široce přijímaným technologiím.

## Klíčové vlastnosti

- Kvantifikuje hrubou rychlost zpracování CPU v milionech instrukcí za sekundu
- Používá se jako vysokourovňová referenční hodnota pro výpočetní složitost ve studiích proveditelnosti
- Pomáhá odhadnout procesní zátěž pro nové algoritmy a funkce protokolů
- Podkládá rozhodnutí o povinných versus volitelných schopnostech ve standardech
- Poskytuje společný referenční bod pro diskuse mezi systémovými a hardwarovými inženýry
- Napomáhá posouzení životaschopnosti implementace pro různé kategorie UE a síťové uzly

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TR 22.907** (Rel-4) — UMTS IC Card and Terminal Concepts
- **TR 23.977** (Rel-19) — Bandwidth/Resource Savings & Speech Quality Requirements

---

📖 **Anglický originál a plná specifikace:** [MIPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/mips/)
