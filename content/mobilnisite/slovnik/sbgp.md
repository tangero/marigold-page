---
slug: "sbgp"
url: "/mobilnisite/slovnik/sbgp/"
type: "slovnik"
title: "SBGP – Special Burst Generation Gap"
date: 2025-01-01
abbr: "SBGP"
fullName: "Special Burst Generation Gap"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sbgp/"
summary: "Časovací parametr v UMTS (WCDMA), který definuje ochranný interval pro generování speciálních burstů v komprimovaném režimu. Zajišťuje správné vysílání a příjem při vytváření mezer ve struktuře rámců"
---

SBGP je časovací parametr UMTS, který definuje ochranný interval pro generování speciálních burstů v komprimovaném režimu, aby byla zajištěna správná vysílání a příjem při vytváření měřicích mezer.

## Popis

Special Burst Generation Gap (SBGP, interval generování speciálních burstů) je koncept definovaný ve specifikacích 3GPP pro UMTS, konkrétně v TS 25.224, která podrobně popisuje procedury fyzické vrstvy Node B. Jde o klíčový parametr v rámci provozu komprimovaného režimu [WCDMA](/mobilnisite/slovnik/wcdma/). Komprimovaný režim vytváří ve standardních rámcích vysílací mezery, aby Uživatelské zařízení (UE) mohlo bez druhého přijímače provádět měření na jiných kmitočtech nebo technologiích rádiového přístupu (např. GSM). SBGP konkrétně definuje časový vztah a ochranný interval spojený s generováním a vysíláním 'speciálních burstů'. Tyto speciální bursty jsou vysílány v rámcích sousedících s vysílací mezerou, aby byla zachována kontinuita smyčky řízení výkonu a odhadu kanálu. Parametr SBGP zajišťuje, že Node B má dostatek času pro generování těchto speciálních burstů a UE pro jejich zpracování, čímž zabraňuje překrytí s měřicí mezerou a vzniku interference. Funguje ve spojení s dalšími parametry komprimovaného režimu, jako je Transmission Gap Pattern Sequence (TGPS) a Transmission Gap Starting Slot (TGSS). Jeho úlohou je zajistit, že zavedení měřicích mezer nezhorší kvalitu probíhajícího spojení, což umožňuje plynulou mobilitu a rozhodování o předávání spojení v prostředí s více [RAT](/mobilnisite/slovnik/rat/).

## K čemu slouží

SBGP byl zaveden, aby vyřešil problém provádění měření mezi kmitočty a mezi systémy v UMTS bez nutnosti nákladných UE s dvojím přijímačem. V raných nasazeních UMTS nepřetržité vysílání na jediném kmitočtu znemožňovalo UE přeladění pro měření jiných buněk. Komprimovaný režim a následně i parametr SBGP byly vytvořeny pro vkládání záměrných mezer do vysílání. SBGP zajišťuje spolehlivé generování a umístění speciálních burstů, které nesou klíčové pilotní a řídicí informace těsně před těmito mezerami a po nich. Tím řeší omezení spočívající v možné ztrátě řízení výkonu a synchronizace během mezery, což mohlo vést k přerušeným hovorům nebo neúspěšným předáním spojení. Byl klíčovým prvkem pro předávání spojení z UMTS na GSM a pro vrstvená síťová nasazení, což zlepšilo robustnost mobility a efektivitu sítě v éře 3G.

## Klíčové vlastnosti

- Definuje ochranný interval pro vysílání speciálních burstů v komprimovaném režimu
- Zajišťuje časové sladění mezi normálními rámci a vysílacími mezerami
- Udržuje kontinuitu smyčky řízení výkonu během měřicích intervalů
- Podporuje procedury měření mezi kmitočty a mezi různými RAT
- Parametr konfigurovaný RNC a prováděný Node B
- Kritický pro spolehlivost mobility a předávání spojení v UMTS

## Související pojmy

- [UMTS – Universal Mobile Telecommunications System](/mobilnisite/slovnik/umts/)
- [WCDMA – Wideband Code Division Multiple Access](/mobilnisite/slovnik/wcdma/)

## Definující specifikace

- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures

---

📖 **Anglický originál a plná specifikace:** [SBGP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sbgp/)
