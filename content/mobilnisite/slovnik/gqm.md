---
slug: "gqm"
url: "/mobilnisite/slovnik/gqm/"
type: "slovnik"
title: "GQM – Goal, Question, Metric"
date: 2025-01-01
abbr: "GQM"
fullName: "Goal, Question, Metric"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/gqm/"
summary: "Strukturovaná metodologie definovaná v 3GPP pro navrhování systémů měření výkonnosti v telekomunikačním managementu. Poskytuje logický rámec pro odvození měřitelných metrik (M) z vysokostupňových obch"
---

GQM je strukturovaná metodologie pro navrhování systémů měření výkonnosti, která poskytuje rámec pro odvození měřitelných metrik z vysokostupňových cílů prostřednictvím formulace konkrétních otázek, na které metriky musí odpovídat.

## Popis

Přístup GQM (Goal, Question, Metric – Cíl, Otázka, Metrika) je shora dolů směřující, cílům orientovaný rámec standardizovaný v rámci specifikací 3GPP pro Telekomunikační management (TM), především v řadě 32.4xx (např. TS 32.404, 32.405, 32.406). Nejde o konkrétní protokol nebo rozhraní, ale o metodologickou šablonu pro definování toho, co a proč měřit v kontextu správy sítě. Proces začíná identifikací jasných, vysokostupňových Cílů (G). Tyto cíle jsou typicky obchodně orientované (např. 'zlepšit spokojenost zákazníků', 'snížit provozní náklady') nebo technicko-provozní (např. 'optimalizovat využití rádiových zdrojů', 'zajistit dostupnost služby').

Pro každý definovaný Cíl je formulována sada zpřesněných Otázek (Q). Tyto otázky rozkládají abstraktní cíl na konkrétní, zodpověditelné dotazy. Například pro cíl 'zlepšit spokojenost zákazníků' může otázka znít 'Jaká je aktuální míra hovorových výpadků na geografickou oblast?' nebo 'Jak často dochází k bufferingu při streamování videa?'. Otázky slouží jako most mezi kvalitativním cílem a kvantitativními daty.

Nakonec je pro každou Otázku definována jedna nebo více konkrétních Metrik (M). Metrika je kvantifikovatelné měření s jasným zdrojem dat, metodou sběru a výpočetním vzorcem. Podle předchozího příkladu by metriky mohly být 'Poměr hovorových výpadků (%) vypočtený ze zpráv o uvolnění [RRC](/mobilnisite/slovnik/rrc/) spojení s příčinou "radio link failure"' nebo 'Poměr přerušování videa měřený na relaci účastníka z reportů o kvalitě uživatelského prožitku (QoE) na aplikační vrstvě'. Specifikace 3GPP poskytují katalogy standardních metrik a detailně popisují, jak jsou odvozeny z měření v síti (např. z dat měření výkonnosti - PM, správy poruch - [FM](/mobilnisite/slovnik/fm/)). Rámec GQM zajišťuje, že každá sebraná metrika má sledovatelný účel přímo spojený se strategickým cílem, čímž předchází sběru dat samotnému pro sebe a zaměřuje prostředky managementu na akceschopné poznatky.

## K čemu slouží

Metodologie GQM byla přijata a standardizována 3GPP, aby do řízení výkonnosti komplexních telekomunikačních sítí vnesla důslednost, konzistenci a sladění. Před takovými strukturovanými přístupy operátoři často sbírali z síťových prvků obrovská množství dat bez jasné strategie, což vedlo k situacím 'bohatým na data, ale chudým na informace'. Bylo obtížné určit, které metriky jsou skutečně důležité pro obchodní výsledky nebo provozní efektivitu, což vedlo k plýtvání úložnou kapacitou, výpočetními zdroji a časem analytiků.

3GPP zavedlo GQM do svých specifikací managementu, aby tento problém vyřešilo. Jeho hlavním účelem je zajistit, aby systém měření výkonnosti byl řízen obchodními a provozními cíli. Vynucením jasné vazby od Cíle přes Otázku k Metrice zaručuje, že sebraná data jsou relevantní a akceschopná. To je obzvláště kritické v prostředích s více dodavateli, protože poskytuje společný jazyk a rámec pro definování klíčových ukazatelů výkonnosti ([KPI](/mobilnisite/slovnik/kpi/)) a klíčových ukazatelů kvality ([KQI](/mobilnisite/slovnik/kqi/)). Umožňuje operátorům navrhovat jejich systémy správy sítě a operační podpory ([OSS](/mobilnisite/slovnik/oss/)) způsobem orientovaným na cíle, čímž zvyšuje efektivitu optimalizace sítě, plánování kapacity, diagnostiky poruch a zajištění kvality služeb. Proměňuje management z reaktivního cvičení v prosívání dat v proaktivní, cíli řízený proces.

## Klíčové vlastnosti

- Shora dolů směřující, cíli řízený rámec pro definování metrik výkonnosti
- Vytváří jasnou vazbu sledovatelnosti od obchodních/provozních cílů k surovým měřením
- Strukturovaný třívrstvý model: Cíle (abstraktní) -> Otázky (konkrétní) -> Metriky (kvantitativní)
- Předchází zbytečnému sběru dat tím, že zajišťuje, aby každá metrika měla svůj účel
- Usnadňuje sladění mezi obchodními, provozními a technickými týmy v tom, co měřit
- Poskytuje standardizovanou metodologii odkazovanou v katalozích specifikací managementu 3GPP

## Definující specifikace

- **TS 32.404** (Rel-19) — Performance Management Definitions & Template
- **TS 32.405** (Rel-19) — UTRAN Performance Measurements Specification
- **TS 32.406** (Rel-19) — Performance Management for CN PS Domain

---

📖 **Anglický originál a plná specifikace:** [GQM na 3GPP Explorer](https://3gpp-explorer.com/glossary/gqm/)
