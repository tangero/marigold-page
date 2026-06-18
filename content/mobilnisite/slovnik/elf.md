---
slug: "elf"
url: "/mobilnisite/slovnik/elf/"
type: "slovnik"
title: "ELF – Executable and Linkable Format"
date: 2025-01-01
abbr: "ELF"
fullName: "Executable and Linkable Format"
category: "Other"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/elf/"
summary: "Executable and Linkable Format (ELF) je standardní formát souboru pro spustitelné soubory, objektový kód, sdílené knihovny a výpisy paměti (core dumps), používaný v rámci specifikací 3GPP pro distribu"
---

ELF je standardní formát souboru pro spustitelné soubory, objektový kód a sdílené knihovny, používaný v rámci 3GPP pro distribuci softwaru na síťových zařízeních, aby byla zajištěna interoperabilita a spolehlivé provádění na různých hardwarových platformách.

## Popis

Executable and Linkable Format (ELF) je všudypřítomný, na platformě nezávislý standard formátu binárních souborů. V kontextu 3GPP je odkazován jako standardizovaná metoda pro balení spustitelného kódu a souvisejících dat pro použití v síťových prvcích a uživatelských zařízeních (UE). Soubor ELF definuje, jak jsou strojový kód, data, tabulky symbolů, relokační informace a metadata programu organizovány do sekcí a segmentů. Tato organizace je klíčová pro systémový software, jako jsou linker a loader, které interpretují strukturu ELF, aby připravily program pro spuštění v paměti.

Technicky soubor ELF začíná hlavičkou ELF, která popisuje celkovou strukturu souboru, včetně cílové architektury (např. ARM, x86), vstupního bodu pro spuštění a offsetů k tabulce hlaviček sekcí a tabulce hlaviček programů. Tabulka hlaviček programů, používaná loadery, definuje segmenty – části souboru, které jsou mapovány do paměti během provádění, jako jsou segmenty spustitelného kódu (text) a datové segmenty. Tabulka hlaviček sekcí, používaná linkery a debuggerem, definuje jemněji členěné sekce uvnitř souboru, jako je .text pro kód, .data pro inicializované proměnné, .bss pro neinicializovaná data a .symtab pro symboly.

V prostředí sítě 3GPP je ELF formátem pro softwarové binární soubory, které běží na síťových funkcích, ať už virtualizovaných (jako u Cloud-Native Network Function – [CNF](/mobilnisite/slovnik/cnf/)) nebo na specializovaném hardwaru. Například software pro Virtualized Network Function ([VNF](/mobilnisite/slovnik/vnf/)) nebo Containerized Network Function, včetně aplikačního kódu a sdílených knihoven, je typicky distribuován a prováděn ve formátu ELF. Použití standardizovaného formátu, jako je ELF, zajišťuje, že podkladový operační systém a hypervizor na serverech typu commercial off-the-shelf ([COTS](/mobilnisite/slovnik/cots/)) mohou správně načíst, prolinkovat závislosti a provést telekomunikační software, což podporuje přenositelnost a zjednodušuje správu životního cyklu softwaru od vývoje přes nasazení až po aktualizace.

## K čemu slouží

ELF existuje k vyřešení problému nekompatibilních binárních formátů na různých výpočetních platformách a operačních systémech. Před takovými standardy často každý dodavatel systému používal proprietární formát spustitelných souborů, což extrémně ztěžovalo přenos softwaru. Vytvoření ELF, původně vyvinutého pro Unix System V.4 a později přijatého Linuxem a mnoha dalšími systémy, poskytlo společný, flexibilní a rozšiřitelný formát. To umožňuje kompilátorům, linkerům a loaderům z různých toolchainů interoperabilně vytvářet a zpracovávat binární soubory.

V rámci standardizačního rozsahu 3GPP odkazování na ELF (konkrétně v TS 31.131 pro aspekty jako bezpečné načítání softwaru) poskytuje stabilní, dobře pochopený základ pro diskusi o distribuci a provádění softwaru. Jak se sítě 3GPP s příchodem 5G vyvíjely směrem k cloud-nativním principům s využitím hardwaru [COTS](/mobilnisite/slovnik/cots/) a virtualizace, závislost na standardních softwarových formátech, jako je ELF, se stala ještě kritičtější. Umožňuje dodavatelům síťových funkcí zabalit svůj software nezávisle na finálním nasazovacím hardwaru, pokud je podporována cílová [CPU](/mobilnisite/slovnik/cpu/) architektura. Toto oddělení je klíčovým prvkem pro virtualizaci síťových funkcí ([NFV](/mobilnisite/slovnik/nfv/)) a cloud-nativní síťové architektury, podporuje diverzitu dodavatelů, usnadňuje aktualizace a efektivní využití zdrojů.

## Klíčové vlastnosti

- Standardizovaná struktura s hlavičkou ELF, tabulkou hlaviček programů a tabulkou hlaviček sekcí
- Podpora více procesorových architektur (např. ARM, x86, PowerPC)
- Definuje jak pohled pro linkování (sekce), tak pohled pro provádění (segmenty)
- Obsahuje informace o symbolech a relokacích pro dynamické linkování
- Používá se pro spustitelné soubory, sdílené knihovny, objektové soubory a výpisy paměti (core dumps)
- Umožňuje přenositelnost softwaru mezi platformami a efektivní načítání programů

## Definující specifikace

- **TS 31.131** (Rel-19) — C Language Binding for (U)SIM API

---

📖 **Anglický originál a plná specifikace:** [ELF na 3GPP Explorer](https://3gpp-explorer.com/glossary/elf/)
