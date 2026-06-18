---
slug: "rif"
url: "/mobilnisite/slovnik/rif/"
type: "slovnik"
title: "RIF – Request or Indication Flag"
date: 2025-01-01
abbr: "RIF"
fullName: "Request or Indication Flag"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/rif/"
summary: "Příznak používaný v signalizaci OAM (Operations, Administration, and Maintenance), zejména pro výměnu dat řízení výkonnosti mezi síťovými prvky nebo systémy řízení. Označuje, zda je zpráva žádostí o d"
---

RIF je příznak používaný v signalizaci OAM, který označuje, zda je zpráva žádostí o data nebo indikací poskytující data, čímž zefektivňuje komunikaci v rámci řízení výkonnosti.

## Popis

Příznak žádosti nebo indikace (RIF) je základním prvkem v rámci rámce [OAM](/mobilnisite/slovnik/oam/) (Operations, Administration, and Maintenance) definovaného 3GPP, konkrétně podrobně popsaným ve specifikacích pro řízení výkonnosti. Funguje jako binární řídicí pole vložené do zpráv řídicích protokolů vyměňovaných mezi síťovými prvky ([NE](/mobilnisite/slovnik/ne/)), systémy řízení sítě ([NMS](/mobilnisite/slovnik/nms/)) nebo systémy řízení prvků ([EMS](/mobilnisite/slovnik/ems/)). Jeho primární funkcí je jednoznačně signalizovat záměr zprávy, rozlišujíc mezi vyžádanou žádostí o data o výkonnosti a nevyžádanou indikací či hlášením obsahujícím taková data. Toto rozlišení je klíčové pro správnou interpretaci a zpracování toků řídicích informací, což zajišťuje, že systémy reagují odpovídajícím způsobem – například poskytnutím dat v reakci na žádost nebo zaznamenáním a analýzou autonomně vygenerovaného hlášení.

Z architektonického hlediska je RIF implementován v rámci protokolových vrstev odpovědných za komunikaci řízení výkonnosti, jak je definováno ve specifikacích jako 28.062 a 48.061. Tyto specifikace popisují informační modely a procedury pro výměnu dat o měření výkonnosti. Klíčovou součástí tohoto procesu je soubor dat řízení výkonnosti ([PM](/mobilnisite/slovnik/pm/)), který obsahuje čítače a měřidla pro různé síťové metriky. Když NMS potřebuje získat data ze síťového prvku, odešle žádost se stavem RIF nastaveným na 'Request'. Příjemce tento příznak interpretuje, shromáždí příslušná PM data ze svých interních měření a sestaví odpověď se stavem RIF nastaveným na 'Indication', která nese požadovaná datová zatížení.

Naopak, síťový prvek může být nakonfigurován tak, aby autonomně generoval a odesílal hlášení o výkonnosti na základě specifických spouštěčů nebo plánů, jako je periodické hlášení nebo překročení prahových hodnot. V těchto nevyžádaných scénářích je zpráva iniciována síťovým prvkem s RIF implicitně nastaveným na 'Indication', což signalizuje systému řízení, že se jedná o notifikaci typu push, nikoli o odpověď na dotaz. Tento mechanismus podporuje jak model získávání dat typu pull, tak push, což poskytuje flexibilitu v strategiích monitorování sítě. Správné použití RIF zajišťuje spolehlivou, stavově uvědomělou komunikaci mezi řídicími entitami, zabraňuje chybným interpretacím, které by mohly vést ke ztrátě dat, duplicitnímu zpracování nebo systémovým chybám, a tím tvoří základní aspekt automatizovaného zajišťování výkonnosti sítě.

## K čemu slouží

RIF byl zaveden za účelem standardizace a objasnění záměru zpráv v rámci protokolů řízení výkonnosti [OAM](/mobilnisite/slovnik/oam/). Před takovou standardizací mohla rozhraní řízení spoléhat na implicitní kontext, různé typy zpráv nebo proprietární schémata pro rozlišení mezi datovými žádostmi a hlášeními, což vedlo k potenciálním problémům s interoperabilitou mezi zařízeními od různých dodavatelů. RIF poskytuje jednoduchý, explicitní a všeobecně srozumitelný signál v samotné struktuře zprávy.

Toto explicitní signalizace řeší problém nejednoznačné komunikace v řídicích rovinách. Ve složitých sítích s více dodavateli musí systém řízení spolehlivě určit, zda příchozí zpráva vyžaduje akci (jako je zpracování datové zprávy), nebo je sama odpovědí na předchozí akci. RIF to řeší přímo tím, že záměr zprávy činí prvotřídním, identifikovatelným atributem. To snižuje složitost protokolu a potenciál chyb ve správě stavu v rámci systémů OAM, protože příznak poskytuje jasný indikátor toku transakcí uvnitř přenosu.

Historicky, jak se sítě vyvíjely směrem k automatizovanějším a škálovatelnějším rámcům OAM, rostla potřeba robustních mechanismů signalizace odolných vůči chybám. Zavedení RIF v Rel-8, spolu s rozšířenými možnostmi řízení výkonnosti, podpořilo posun odvětví k efektivnější, standardizované síťové operaci. Řešilo to omezení ad-hoc nebo dodavatelsky specifických metod a zajišťovalo, že sběr dat o výkonnosti – kritická funkce pro monitorování stavu sítě, plánování kapacity a odstraňování problémů – může být spolehlivě implementován v globálních nasazeních.

## Klíčové vlastnosti

- Binární příznak rozlišující mezi typy zpráv 'Request' (žádost) a 'Indication' (indikace)
- Vložený do zpráv protokolů OAM pro řízení výkonnosti
- Umožňuje jak modely získávání dat typu pull (žádost/odpověď), tak push (nevyžádané hlášení)
- Snižuje nejednoznačnost protokolu a zabraňuje chybné interpretaci toků řídicích dat
- Standardizován napříč síťovými prvky a systémy řízení pro zajištění interoperability
- Základní pro správné zpracování stavu v automatizovaných transakcích monitorování výkonnosti

## Související pojmy

- [OAM – Operations, Administration, and Maintenance](/mobilnisite/slovnik/oam/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)

## Definující specifikace

- **TS 28.062** (Rel-19) — Tandem Free Operation (TFO) Service Description
- **TS 48.061** (Rel-19) — BTS-TRAU Protocol for HR Speech/Data

---

📖 **Anglický originál a plná specifikace:** [RIF na 3GPP Explorer](https://3gpp-explorer.com/glossary/rif/)
