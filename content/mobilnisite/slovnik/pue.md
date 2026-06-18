---
slug: "pue"
url: "/mobilnisite/slovnik/pue/"
type: "slovnik"
title: "PUE – Power Usage Effectiveness"
date: 2025-01-01
abbr: "PUE"
fullName: "Power Usage Effectiveness"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/pue/"
summary: "PUE je metrika definovaná 3GPP pro měření energetické účinnosti datového centra sítě nebo místa s technologickým vybavením. Je to poměr celkové energie spotřebované zařízením k energii spotřebované IT"
---

PUE je poměr celkové energie spotřebované zařízením k energii spotřebované IT zařízením, definovaný 3GPP pro měření energetické účinnosti datového centra sítě nebo místa s technologickým vybavením.

## Popis

Power Usage Effectiveness (PUE) je klíčový ukazatel výkonu ([KPI](/mobilnisite/slovnik/kpi/)) pro energetickou účinnost, standardizovaný 3GPP pro telekomunikační průmysl, zejména v rámci specifikací pro management, jako je TS 32.972. Je to metrika používaná k hodnocení, jak efektivně datové centrum sítě, centrální ústředna nebo místo základnové stanice využívá energii. Konkrétně je PUE definován jako poměr celkového množství energie spotřebované celým zařízením (včetně chlazení, osvětlení, ztrát v rozvodu energie a podpůrných systémů) k energii spotřebované výhradně informačními technologiemi ([IT](/mobilnisite/slovnik/it/)) nebo telekomunikačním zařízením, které vykonává skutečnou výpočetní nebo síťovou zátěž.

Výpočet je přímočarý: PUE = Celková energie zařízení / Energie IT zařízení. Ideální, dokonalá hodnota PUE by byla 1,0, což by znamenalo, že veškerá příchozí energie je použita přímo IT/síťovým zařízením bez žádné režie. Ve skutečnosti jsou hodnoty PUE vždy větší než 1,0. Například PUE 1,5 znamená, že z každých 1,5 wattů odebraných ze sítě pohání IT zařízení 1 watt a 0,5 wattu spotřebuje podpůrná infrastruktura. Architektura pro měření PUE zahrnuje komplexní měření energie v různých bodech uvnitř místa. Měřiče jsou vyžadovány na hlavním přívodu energie do zařízení (měření celkové energie) a na napájecích rozvaděčích ([PDU](/mobilnisite/slovnik/pdu/)) napájejících serverové racky, směrovače, základnové jednotky a další základní síťové prvky (měření energie IT).

PUE funguje jako nástroj pro srovnávání a sledování trendů. Síťoví operátoři nasazují systémy pro správu energie ([EMS](/mobilnisite/slovnik/ems/)), které shromažďují data z těchto měřičů, aby vypočítaly PUE téměř v reálném čase nebo za definovaná období. Sledováním PUE mohou operátoři identifikovat neefektivity. Rostoucí PUE může naznačovat selhávající chladicí zařízení, nedostatečně vytížené servery nebo špatné řízení proudění vzduchu. Jeho role v síti je klíčová pro udržitelný provoz a správu nákladů. Poskytuje jednoduché, univerzální číslo, které operátorům umožňuje porovnávat různá místa mezi sebou, sledovat dopad projektů na zvýšení účinnosti (jako je instalace volného chlazení nebo modernizace na účinnější systémy UPS) a podávat zprávy o environmentálním výkonu zainteresovaným stranám a regulátorům.

## K čemu slouží

PUE byl přijat a definován 3GPP, aby řešil prudce rostoucí spotřebu energie a provozní náklady infrastruktury mobilních sítí, zejména s explozivním nárůstem datového provozu u 4G a 5G. Základním problémem je, že významná část elektřiny spotřebované síťovým místem nepohání rádiové jednotky nebo procesory poskytující služby, ale je promrhána na pomocné systémy, jako je chlazení a přeměna energie. Před standardizovanými metrikami, jako je PUE, operátoři neměli konzistentní způsob, jak tento odpad měřit a porovnávat, což ztěžovalo stanovení priorit investic do energetické účinnosti.

Vytvoření PUE jako metriky pro management v 3GPP bylo motivováno ekonomickými i environmentálními tlaky. Z provozního hlediska je energie jednou z největších položek provozních výdajů (OpEx) mobilního operátora. Snížení PUE přímo snižuje účty za elektřinu. Z environmentálního hlediska čelí telekomunikační průmysl rostoucímu tlaku na snížení uhlíkové stopy. Zlepšení PUE snižuje celkovou energii potřebnou na jednotku síťového provozu, což přispívá k cílům udržitelnosti. Standardizace 3GPP poskytla společný jazyk a metodologii, umožňující spravedlivé srovnávání v rámci odvětví a umožňující vývoj zařízení dodavatelů a řešení pro místa navržená k optimalizaci tohoto konkrétního [KPI](/mobilnisite/slovnik/kpi/).

Řeší omezení předchozích, často subjektivních hodnocení účinnosti místa. Poskytnutím jasného, kvantifikovatelného vzorce mění PUE správu energie z umění na vědu. Umožňuje operátorům stanovit konkrétní cíle (např. dosáhnout PUE 1,3 pro všechna nová datová centra), měřit pokrok a ospravedlnit kapitálové výdaje na zelené technologie. V kontextu 5G a zhušťování sítě, kde počet míst roste, je kontrola PUE na každém místě klíčová pro škálovatelný a udržitelný růst sítě.

## Klíčové vlastnosti

- Standardizovaná metrika 3GPP pro energetickou účinnost datového centra/místa
- Definována jako poměr celkové energie zařízení k energii IT zařízení
- Vyžaduje měření na vstupu do zařízení a v rozvodu energie k IT zařízení
- Používá se pro srovnávání, analýzu trendů a ověřování projektů na zvýšení účinnosti
- Nižší hodnota PUE znamená vyšší celkovou energetickou účinnost
- Integrální součást systémů pro správu energie (EMS) sítě

## Související pojmy

- [KPI – Key Performance Indicators](/mobilnisite/slovnik/kpi/)

## Definující specifikace

- **TR 32.972** (Rel-19) — Energy Efficiency Study for 5G Networks

---

📖 **Anglický originál a plná specifikace:** [PUE na 3GPP Explorer](https://3gpp-explorer.com/glossary/pue/)
