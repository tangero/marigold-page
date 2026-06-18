---
slug: "gmt"
url: "/mobilnisite/slovnik/gmt/"
type: "slovnik"
title: "GMT – Greenwich Mean Time"
date: 2025-01-01
abbr: "GMT"
fullName: "Greenwich Mean Time"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gmt/"
summary: "Greenwichský střední čas (GMT) je globální časový standard používaný jako referenční bod pro synchronizaci v sítích 3GPP. Poskytuje společný časový základ pro síťové prvky, časová razítka v logech a k"
---

GMT je globální časový standard používaný jako referenční bod pro synchronizaci v sítích 3GPP, který poskytuje společný časový základ pro síťové prvky, záznamy v logech a časově citlivé operace.

## Popis

Greenwichský střední čas (GMT) je časový standard založený na středním slunečním čase v Královské observatoři v Greenwichi v Londýně. Ve specifikacích 3GPP slouží GMT jako základní časová reference pro synchronizaci sítě a časové značkování. Nejde o časové pásmo, ale o časovou stupnici, historicky definovanou rotací Země. V moderní telekomunikaci se GMT často prakticky používá zaměnitelně s koordinovaným světovým časem ([UTC](/mobilnisite/slovnik/utc/)), přičemž UTC je přesnější atomový časový standard, který zahrnuje přestupné sekundy pro vyrovnání nepravidelností v rotaci Země. Použití GMT ve standardech 3GPP zajišťuje globálně uznávanou a jednoznačnou časovou referenci.

Z architektonického hlediska je GMT integrováno do systémů 3GPP jako reference pro časové značkování událostí a synchronizaci síťových operací. Síťové prvky, jako jsou systémy účtování, funkce zákonného odposlechu a systémy správy sítě, spoléhají na časová razítka GMT pro zaznamenávání událostí, jako jsou časy zahájení/ukončení hovoru, zahájení datové relace a bezpečnostní incidenty. Tato časová reference je klíčová pro korelaci událostí napříč různými síťovými doménami a geografickými lokalitami. Implementace zahrnuje přístup síťových prvků ke spolehlivému časovému zdroji, často prostřednictvím protokolu [NTP](/mobilnisite/slovnik/ntp/) (Network Time Protocol) nebo [PTP](/mobilnisite/slovnik/ptp/) (Precision Time Protocol), které jsou synchronizovány s UTC/GMT.

Role GMT se rozšiřuje o zajištění chronologické přesnosti v záznamech pro účtování, kde jsou přesná časová razítka nezbytná pro generování přesných záznamů účtovatelných událostí. V zákonném odposlechu jsou časová razítka GMT povinná pro informace související s odposlechem, aby byla zachována právní přípustnost důkazů a umožněny vyšetřování přesahující jurisdikce. Dále systémy správy sítě používají GMT pro zaznamenávání alarmů, měření výkonu a změn konfigurace, což usnadňuje řešení problémů a auditní trasování. Specifikace GMT v dokumentech, jako je 3GPP TS 29.458 (pro Service Capability Exposure Function) a TS 29.658 (pro interakci s aplikačním serverem), podtrhuje její význam v časových razítcích [API](/mobilnisite/slovnik/api/) a frameworkech pro vystavování služeb.

Ačkoli je GMT samo o sobě jednoduchý koncept, jeho konzistentní aplikace napříč sítěmi 3GPP je složitá a vyžaduje robustní mechanismy distribuce času. Operátoři sítí musí zajistit, aby všechny relevantní uzly byly synchronizovány v rámci přijatelných tolerancí, aby se předešlo nesrovnalostem. Této synchronizace je často dosaženo prostřednictvím hierarchických architektur distribuce času s primárními referenčními hodinami (PRTC), které jsou dohledatelné k národním časovým laboratořím. Použití GMT namísto místních časových pásem odstraňuje nejednoznačnost a zjednodušuje zpracování časově citlivých dat v mezinárodních sítích, což z něj činí základní kámen globální telekomunikační interoperability.

## K čemu slouží

Účelem specifikace greenwichského středního času (GMT) ve standardech 3GPP je stanovit univerzální a jednoznačnou časovou referenci pro všechny síťové operace. Telekomunikační sítě jsou ze své podstaty globální, přičemž události se odehrávají napříč více časovými pásmy a jurisdikcemi. Použití místního času by zavedlo složitost a potenciální chyby v korelaci událostí, účtování a bezpečnostních funkcích. GMT poskytuje neutrální, globálně uznávanou základní linii, která zajišťuje konzistenci v časovém značkování, což je zásadní pro provozní, komerční a právní integritu.

Historicky se potřeba společné časové reference stala naléhavou s nástupem digitálních ústředen a automatizovaných systémů účtování. Rané telekomunikační systémy často spoléhaly na místní čas hodin, což vedlo k nesrovnalostem ve scénářích s více operátory. Zavedení GMT ve standardech pro účtování (např. řada 3GPP TS 32.) a zákonný odposlech tyto problémy řeší tím, že nařizuje jediný časový standard. To umožňuje bezproblémovou interoperabilitu mezi různými síťovými operátory a poskytovateli služeb, zejména v roamingu, kdy aktivity účastníka zasahují do více sítí.

GMT dále řeší omezení předchozích ad-hoc přístupů, kdy byla časová synchronizace specifická pro operátora a náchylná k odchylkám. Standardizací na GMT 3GPP zajišťuje, že časově citlivé funkce, jako je generování záznamů o hovorech ([CDR](/mobilnisite/slovnik/cdr/)), zaznamenávání událostí a bezpečnostní monitoring, jsou sladěné. To je obzvláště důležité pro dodržování regulatorních požadavků, kde jsou přesná časová razítka vyžadována pro účtovací spory, detekci podvodů a mandáty pro zákonný odposlech. V podstatě GMT slouží jako časové pojivo, které spojuje různé síťové prvky v koherentní a odpovědný systém.

## Klíčové vlastnosti

- Poskytuje globálně uznávanou časovou referenci pro synchronizaci sítě
- Zajišťuje jednoznačné časové značkování pro záznamy o účtování a fakturaci
- Je povinné pro zákonný odposlech, aby byla zachována právní přípustnost důkazů
- Umožňuje korelaci událostí napříč různými síťovými doménami a geografickými oblastmi
- Používá se v síťovém managementu pro zaznamenávání alarmů a dat o výkonu
- Je integrováno do API 3GPP (např. SCEF, AS) pro konzistentní časové značkování při vystavování služeb

## Související pojmy

- [UTC – Coordinated Universal Time](/mobilnisite/slovnik/utc/)
- [NTP – Network Time Protocol](/mobilnisite/slovnik/ntp/)
- [PTP – Physical Termination Point](/mobilnisite/slovnik/ptp/)

## Definující specifikace

- **TS 29.458** (Rel-8) — SIP Transfer of Tariff Info for Charging
- **TS 29.658** (Rel-19) — SIP Transfer of Tariff Information

---

📖 **Anglický originál a plná specifikace:** [GMT na 3GPP Explorer](https://3gpp-explorer.com/glossary/gmt/)
