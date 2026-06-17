---
slug: "egqm"
url: "/mobilnisite/slovnik/egqm/"
type: "slovnik"
title: "EGQM – Enhanced Goal, Question, Metric"
date: 2025-01-01
abbr: "EGQM"
fullName: "Enhanced Goal, Question, Metric"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/egqm/"
summary: "EGQM je strukturovaný rámec v rámci 3GPP pro definici a správu metrik výkonu a kvalitativních cílů v telekomunikačních sítích. Poskytuje systematickou metodologii pro překlad vysokorozměrných obchodní"
---

EGQM je strukturovaný rámec 3GPP pro překlad vysokorozměrných servisních cílů na měřitelné technické parametry za účelem správy metrik výkonu, definice SLA a optimalizace sítí.

## Popis

Rámec Enhanced Goal, Question, Metric (EGQM) je metodologický přístup definovaný v technických specifikacích 3GPP pro správu výkonu. Funguje v širším kontextu Telecommunication Management Network (TMN) a architektury správy sítě ([NM](/mobilnisite/slovnik/nm/)) dle 3GPP. Tento rámec není fyzickou komponentou, ale konceptuálním modelem a souborem směrnic používaných operátory sítí, výrobci zařízení a normalizačními orgány. Strukturuje proces odvozování smysluplných a akčních metrik z vysokorozměrných cílů.

EGQM funguje na principu hierarchického rozkladu. Začíná vysokorozměrným cílem (Goal), což je obchodní nebo servisní cíl (např. 'Zajistit službu VoLTE vysoké kvality'). Z tohoto cíle jsou formulovány konkrétní otázky (Questions), na které je třeba odpovědět, abychom zjistili, zda je cíl naplňován (např. 'Jaká je míra hovorových výpadků?' nebo 'Jaké je end-to-end zpoždění?'). Pro každou otázku je definována jedna nebo více metrik (Metric). Metrika je kvantifikovatelné měření s jasnou definicí, vzorcem, metodou sběru a jednotkou (např. 'Poměr výpadků hovorů VoLTE' měřený v procentech, vypočítaný z konkrétních čítačů v core a přístupové síti).

Klíčovými komponentami modelu EGQM jsou samotné entity Cíl, Otázka a Metrika spolu s jejich atributy a vztahy, jak je specifikováno v 3GPP TS 32.404. Jeho role v síti je zásadní pro funkce správy výkonu (PM) a správy poruch ([FM](/mobilnisite/slovnik/fm/)). Systémy správy sítě ([NMS](/mobilnisite/slovnik/nms/)) a systémy správy prvků ([EMS](/mobilnisite/slovnik/ems/)) jsou navrženy tak, aby shromažďovaly data na základě metrik definovaných EGQM. Tato data jsou pak používána pro reportování, analýzu, spouštění alarmů a řízení optimalizačních akcí. Tím, že poskytuje standardizovaný způsob definice metrik, EGQM zajišťuje, že data o výkonu jsou srovnatelná napříč různými síťovými prvky, výrobci a dokonce i operátory, což je klíčové pro více-dodavatelská síťová prostředí a roamingové scénáře.

## K čemu slouží

EGQM byl vytvořen, aby řešil problém nekonzistentních, ad-hoc a často nejednoznačných definic metrik výkonu ve složitých, více-dodavatelských telekomunikačních sítích. Před jeho formalizací mohli různí výrobci definovat podobně znějící metriky (např. 'dostupnost') mírně odlišnými způsoby, což ztěžovalo celosíťové hodnocení výkonu a ověřování SLA. Primární problém, který řeší, je vytvoření jasné a sledovatelné vazby mezi tím, čeho chce obchod dosáhnout, a tím, co síť skutečně měří.

Historicky, jak se sítě vyvíjely z jedno-dodavatelských, okruhově přepínaných systémů na více-dodavatelská, paketově přepínaná a na služby bohatá prostředí jako IMS a LTE, potřeba společného jazyka pro správu se stala naléhavou. Operátoři potřebovali spravovat kvalitu služeb end-to-end napříč doménami (RAN, Core, Transport) od různých dodavatelů. EGQM poskytl strukturovanou metodologii pro překlenutí propasti mezi cíli na úrovni služeb a tisíci surových čítačů a měřidel vystavovaných síťovým zařízením.

Jeho motivací bylo zlepšit efektivitu a účinnost síťových operací a plánování. Díky dobře definovaným metrikám mohou operátoři přesněji identifikovat degradaci, prokazovat soulad se SLA a činit investiční rozhodnutí založená na datech. Také usnadňuje automatizaci správy, protože systémy mohou být naprogramovány tak, aby reagovaly na přesně definované překročení prahových hodnot. V podstatě EGQM přináší technickou důslednost do často subjektivní oblasti správy kvality služeb a výkonu.

## Klíčové vlastnosti

- Strukturovaný třívrstvý model: Cíl -> Otázka -> Metrika
- Poskytuje jednoznačné definice metrik výkonu
- Zajišťuje sledovatelnost od obchodních cílů k technickým měřením
- Standardizuje vzorce metrik, jednotky a metodiky sběru
- Podporuje správu více-dodavatelských a více-technologických sítí
- Základ pro automatizovanou správu výkonu a reportování

## Definující specifikace

- **TS 32.404** (Rel-19) — Performance Management Definitions & Template
- **TS 32.405** (Rel-19) — UTRAN Performance Measurements Specification
- **TS 32.406** (Rel-19) — Performance Management for CN PS Domain

---

📖 **Anglický originál a plná specifikace:** [EGQM na 3GPP Explorer](https://3gpp-explorer.com/glossary/egqm/)
