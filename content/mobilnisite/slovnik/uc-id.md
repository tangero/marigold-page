---
slug: "uc-id"
url: "/mobilnisite/slovnik/uc-id/"
type: "slovnik"
title: "UC-ID – UTRAN Cell Identifier"
date: 2025-01-01
abbr: "UC-ID"
fullName: "UTRAN Cell Identifier"
category: "Identifier"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/uc-id/"
summary: "Jedinečný identifikátor buňky v rámci UTRANu (UMTS Terrestrial Radio Access Network). Je klíčový pro správu buněk, procedury předávání hovoru (handover) a plánování sítě, protože umožňuje síti rozlišo"
---

UC-ID je jedinečný identifikátor buňky v rámci UTRANu, který slouží k rozlišení různých rádiových buněk pro účely správy, předávání hovoru (handover) a plánování sítě.

## Popis

[UTRAN](/mobilnisite/slovnik/utran/) Cell Identifier (UC-ID) je základní identifikátor používaný v architektuře 3GPP UMTS (Universal Mobile Telecommunications System). Jednoznačně identifikuje konkrétní buňku v rámci UTRANu, což je rádiová přístupová síť pro 3G UMTS. UC-ID je klíčovou součástí adresního schématu buňky a je hojně využíván při správě sítě, signalizaci řízení rádiových prostředků ([RRC](/mobilnisite/slovnik/rrc/)) a v provozních a údržbových (O&M) funkcích. Umožňuje síťovým prvkům, jako je Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)) a Node B (základnová stanice UMTS), přesně odkazovat na jednotlivé buňky a spravovat je.

Z architektonického hlediska je UC-ID součástí konfiguračních dat buňky a je vysílán na vysílacím kanálu buňky. Je strukturován tak, aby zajišťoval jedinečnost v rámci rozsahu jednoho UTRANu. Tento identifikátor se používá na různých rozhraních a v protokolech, nejvýznamněji na rozhraní Iur (mezi RNC) a rozhraní Iub (mezi RNC a Node B), jak je specifikováno v 3GPP TS 25.423 a TS 25.430. V těchto rozhraních je UC-ID zahrnut v zprávách souvisejících se zřizováním buňky, rekonfigurací buňky, hlášením měření a přípravou a provedením předání hovoru (handover).

Z funkční perspektivy umožňuje UC-ID několik klíčových síťových operací. Během procedur mobility, jako je handover, jsou zdrojové a cílové buňky identifikovány pomocí svých UC-ID, aby bylo zajištěno správné převedení uživatelského zařízení (UE). Pro správu a optimalizaci sítě umožňuje UC-ID operátorům monitorovat výkonnostní metriky (např. přerušení hovorů, vytížení) na úrovni jednotlivých buněk. Hraje také roli při konfiguraci seznamu sousedních buněk, kde jsou definovány UC-ID přilehlých buněk, aby pomohly UE při měřeních a převýběru buňky. Stabilita a jedinečnost tohoto identifikátoru jsou prvořadé pro konzistentní provoz rádiové přístupové sítě.

## K čemu slouží

UC-ID byl zaveden, aby vyřešil potřebu standardizované, jednoznačné metody identifikace jednotlivých rádiových buněk v rámci UMTS UTRANu. Před standardizací 3GPP mohla proprietární schémata identifikace buněk vést k problémům s interoperabilitou mezi síťovými zařízeními od různých dodavatelů. Vytvoření jednotného identifikátoru bylo zásadní pro více-dodavatelský ekosystém sítí UMTS.

Jeho primárním účelem je umožnit přesnou správu a řízení na úrovni buňky napříč síťovými rozhraními. V distribuované architektuře UTRANu, kde [RNC](/mobilnisite/slovnik/rnc/) řídí více Node B a buněk, je spolehlivý identifikátor buňky nezbytný pro signalizaci, konfiguraci a správu chyb. Řeší problém nejednoznačnosti buňky ve scénářích, jako jsou handovery mezi RNC (měkký handover), nebo při hlášení měření specifických pro buňku z Node B do RNC.

UC-ID navíc podporuje škálovatelnost a automatizaci sítě. Jak sítě houstly s větším počtem buněk, ruční sledování založené na nestandardních identifikátorech se stalo nepraktickým. UC-ID poskytuje základní prvek pro automatizované O&M systémy, správu výkonnosti a funkce samoorganizujících se sítí ([SON](/mobilnisite/slovnik/son/)), které se objevily v pozdějších vydáních 3GPP, přestože jeho základní definice zůstala od svého zavedení stabilní.

## Klíčové vlastnosti

- Jednoznačně identifikuje buňku v rámci UTRANu
- Používá se v signalizačních zprávách na rozhraních Iur a Iub
- Nezbytný pro procedury předávání hovoru (handover) a správy mobility
- Umožňuje monitorování a správu výkonnosti na úrovni konkrétní buňky
- Vysílán jako součást systémové informace pro referenci UE
- Základní prvek pro konfiguraci vztahů se sousedními buňkami

## Související pojmy

- [UTRAN – Universal Terrestrial Radio Access Network](/mobilnisite/slovnik/utran/)
- [CGI – Cell Global Identifier](/mobilnisite/slovnik/cgi/)
- [RNC – Radio Network Controller](/mobilnisite/slovnik/rnc/)

## Definující specifikace

- **TS 25.423** (Rel-19) — UTRAN RNSAP Specification
- **TS 25.430** (Rel-19) — Introduction to Iub Interface Specifications

---

📖 **Anglický originál a plná specifikace:** [UC-ID na 3GPP Explorer](https://3gpp-explorer.com/glossary/uc-id/)
