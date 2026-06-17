---
slug: "cps"
url: "/mobilnisite/slovnik/cps/"
type: "slovnik"
title: "CPS – Contiguous Partial Sensing"
date: 2025-01-01
abbr: "CPS"
fullName: "Contiguous Partial Sensing"
category: "Radio Access Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cps/"
summary: "Contiguous Partial Sensing (CPS, kontinuální částečné snímání) je metoda výběru zdrojů v sidelink komunikaci LTE a NR, určená speciálně pro autonomní plánování režimu 2 (Mode 2). Umožňuje uživatelském"
---

CPS je metoda výběru prostředků v sidelink komunikaci, při níž UE detekuje pouze souvislou podmnožinu fondu zdrojů za účelem efektivního výběru vysílacích zdrojů, což snižuje energetickou náročnost a režii zpracování.

## Popis

Contiguous Partial Sensing (CPS, kontinuální částečné snímání) je základní mechanismus ve frameworku sidelink (SL) 3GPP navržený pro přidělování zdrojů v režimu 2 (distribuované plánování). V režimu 2 si UE autonomně vybírají své vysílací zdroje z předdefinovaného fondu zdrojů bez centralizovaného plánování ze sítě. CPS poskytuje metodu, jak může UE tento výběr provést monitorováním („snímáním“) rádiových zdrojů. Na rozdíl od úplného snímání, které vyžaduje monitorování všech podrámců či časových slotů v rámci okna snímání, CPS stanoví povinnost snímání pouze souvislého bloku zdrojů. Tento souvislý blok je definován relativně k potenciální vysílací příležitosti, kterou UE vyhodnocuje.

Operační princip spočívá v tom, že UE vybere kandidátní zdroj využívající jeden podrámec (SSR) nebo více podrámců ve výběrovém okně. Pro každého takového kandidáta musí UE detekovat specifickou sadu souvislých podrámců bezprostředně předcházejících tomuto kandidátnímu zdroji. Přesná poloha a délka tohoto okna snímání jsou definovány parametry jako délka okna snímání (např. 1000 podrámců v LTE) a specifická souvislá podmnožina potřebná pro vyhodnocení. Během tohoto období snímání UE měří sílu přijímaného signálu (např. S-RSSI), dekóduje Sidelink Control Information (SCI) z jiných UE za účelem identifikace rezervovaných zdrojů a vytváří si obraz o obsazenosti kanálu.

Na základě údajů nasbíraných během okna kontinuálního částečného snímání UE uplatňuje vylučovací pravidla. Ze své kandidátní sady vyloučí všechny zdroje, které jsou označeny jako rezervované prostřednictvím SCI od jiných UE, a všechny zdroje, kde naměřená síla signálu překročí nastavenou prahovou hodnotu, což indikuje vysoké rušení nebo obsazenost. Ze zbývající sady způsobilých zdrojů UE náhodně vybere jeden pro své vysílání. Tento proces vyvažuje potřebu spolehlivého výběru zdrojů s prevencí kolizí s imperativem šetření životnosti baterie a výpočetní kapacity UE. CPS je klíčovým prvkem umožňujícím škálovatelnou a efektivní přímou komunikaci, zejména pro vozidlové (V2X) aplikace a aplikace IoT, kde mohou mít zařízení omezený příkon.

## K čemu slouží

CPS bylo zavedeno za účelem řešení významné spotřeby energie a výpočetní zátěže spojené s úplným snímáním v autonomní sidelink komunikaci. Rané návrhy sidelink a [D2D](/mobilnisite/slovnik/d2d/) vyžadovaly, aby UE před každým výběrem vysílání detekovaly celý fond zdrojů v rozšířeném okně (např. 1000 ms). Toto nepřetržité monitorování všech podrámců bylo nepřijatelně energeticky náročné, zejména pro zařízení napájená bateriemi, jako jsou chytré telefony, nositelná zařízení či senzory, a omezovalo praktičnost dlouhodobých přímých komunikačních relací.

Vytvoření CPS motivovala potřeba umožnit proveditelné fungování režimu 2 (Mode 2) pro širší spektrum případů užití, včetně náročných požadavků komunikace Vozidlo se vším (V2X). Scénáře V2X vyžadují výměnu paketů s nízkou latencí a vysokou spolehlivostí, ale vozidlová UE, přestože jsou často připojena ke zdroji napájení, také těží ze snížené složitosti. CPS poskytuje standardizovanou, predikovatelnou metodu výběru zdrojů, která významně snižuje pracovní cyklus snímání. Tím, že detekuje pouze souvislou část časové osy, může být přijímač UE aktivní po kratší dobu, což vede k přímé úspoře energie. To učinilo sidelink komunikaci životaschopnější technologií pro veřejně-bezpečnostní zařízení a koncové body IoT s omezeným příkonem, čímž rozšířilo ekosystém mimo aplikace s vysokým příkonem.

## Klíčové vlastnosti

- Snižuje spotřebu energie UE díky snímání pouze souvislé podmnožiny fondu zdrojů
- Definuje deterministické okno snímání relativně ke každému kandidátnímu vysílacímu zdroji
- Umožňuje autonomní výběr zdrojů (režim 2, Mode 2) pro sidelink komunikaci
- Využívá dekódování Sidelink Control Information (SCI) k identifikaci rezervovaných zdrojů
- Aplikuje měření S-RSSI a vyloučení založené na prahové hodnotě, aby se zabránilo přetíženým zdrojům
- Poskytuje základ pro pokročilejší techniky částečného snímání v pozdějších verzích standardu

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 24.147** (Rel-19) — IMS Conferencing Protocol Details
- **TS 25.424** (Rel-19) — UTRAN Iur Interface Data Transport & Signalling
- **TS 25.426** (Rel-19) — UTRAN Iur/Iub Transport Bearers
- **TS 25.434** (Rel-19) — UTRAN Iub Interface Data Transport and Signalling
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework
- **TR 32.901** (Rel-19) — UDC Application Data Models Study
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TR 37.985** (Rel-19) — Overview of V2X features in LTE and NR

---

📖 **Anglický originál a plná specifikace:** [CPS na 3GPP Explorer](https://3gpp-explorer.com/glossary/cps/)
