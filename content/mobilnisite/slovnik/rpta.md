---
slug: "rpta"
url: "/mobilnisite/slovnik/rpta/"
type: "slovnik"
title: "RPTA – Radio Planning Tool Access"
date: 2025-01-01
abbr: "RPTA"
fullName: "Radio Planning Tool Access"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/rpta/"
summary: "Standardizované rozhraní a informační model, který umožňuje nástroji pro plánování rádiové sítě (RPT) bezpečný přístup k datům pro plánování sítě a jejich výměnu se systémem pro správu sítě (NMS) nebo"
---

RPTA je standardizované rozhraní a informační model, který umožňuje nástroji pro plánování rádiové sítě (Radio Planning Tool) bezpečný přístup k datům pro plánování sítě a jejich výměnu se systémem pro správu sítě (Network Management System) nebo OSS.

## Popis

Radio Planning Tool Access (RPTA) specifikuje standardizované mechanismy pro interoperabilitu mezi nástrojem pro plánování rádiové sítě ([RPT](/mobilnisite/slovnik/rpt/)) a externími systémy, především systémem pro správu sítě ([NMS](/mobilnisite/slovnik/nms/)), jak je definováno v 3GPP TS 28.667 a TS 28.668. RPTA není nástroj sám o sobě, ale definuje přístupový rámec včetně referenčních bodů, datových modelů a procedur. Z architektonického hlediska vytváří rozhraní (často založené na webových službách/[API](/mobilnisite/slovnik/api/)), přes které může RPT získávat potřebná vstupní data z NMS a nahrávat zpět své výsledky plánování. Klíčová data získaná prostřednictvím RPTA zahrnují živá nebo historická data o výkonu sítě ([PM](/mobilnisite/slovnik/pm/) data), data správy konfigurace ([CM](/mobilnisite/slovnik/cm/) data) stávajících síťových prvků, data správy poruch ([FM](/mobilnisite/slovnik/fm/) data) a informace o inventáři. Tento přísun živých dat umožňuje RPT provádět realistické analýzy typu 'co kdyby' a optimalizace založené na skutečném stavu sítě, nikoli pouze na teoretických modelech. Naopak, RPT může nahrát svůj výstup, jako je například seznam doporučených nových lokalit buněk, změny parametrů antén nebo plány využití kmitočtů, do NMS. NMS pak může tato doporučení použít pro generování síťových konfiguračních skriptů nebo pracovních příkazů k implementaci. Rámec RPTA zajišťuje konzistenci dat, zabezpečení (autentizaci a autorizaci) a sémantické porozumění mezi plánovacím nástrojem a systémem správy, které mohou být od různých dodavatelů. Je klíčovým prvkem pro uzavřenou smyčku automatizace v životním cyklu správy sítě.

## K čemu slouží

RPTA bylo vytvořeno k řešení problému datových úložišť a ručního, chybám podléhajícího přenosu dat mezi doménami plánování sítě a provozu sítě. Historicky plánovací týmy používaly samostatné nástroje se statickými vstupy, zatímco provozní týmy spravovaly živou síť prostřednictvím [NMS](/mobilnisite/slovnik/nms/). Srovnání plánovacích předpokladů se skutečným stavem bylo obtížné. RPTA tuto mezeru překlenuje poskytnutím standardizovaného, automatizovaného datového kanálu. Jeho primárním účelem je zlepšit přesnost a relevanci plánování sítě tím, že je založeno na reálných provozních datech (např. skutečné hotspoty provozu, naměřené rušení). Dále zefektivňuje proces nasazení tím, že umožňuje, aby výstupy plánování byly přímo přijímány NMS pro automatizovanou konfiguraci, čímž se zkracuje doba od návrhu k implementaci. Specifikace ve verzi 12 byla motivována snahou průmyslu o integrovanější a automatizovanější správu sítě, což je klíčový aspekt vize 3GPP pro samoorganizující se sítě ([SON](/mobilnisite/slovnik/son/)), kde plánování, nasazení, optimalizace a řešení problémů jsou úzce propojené procesy.

## Klíčové vlastnosti

- Standardizované rozhraní pro interoperabilitu mezi RPT a NMS
- Zabezpečené protokoly pro výměnu dat a mechanismy autentizace
- Informační model pro data relevantní pro plánování (PM, CM, FM a inventární data)
- Podpora operací dotazování na data (pull) i nahrávání výsledků (push)
- Umožňuje ladění a kalibraci modelů pomocí měření ze živé sítě
- Umožňuje automatizované zřizování na základě doporučení z plánování

## Související pojmy

- [RPT – Radio Planning Tool](/mobilnisite/slovnik/rpt/)
- [NMS – Network Management Subsystem](/mobilnisite/slovnik/nms/)
- [SON – Self-Organizing Network](/mobilnisite/slovnik/son/)

## Definující specifikace

- **TS 28.667** (Rel-19) — RPTA IRP Requirements
- **TS 28.668** (Rel-19) — RPTA Integration Reference Point Requirements

---

📖 **Anglický originál a plná specifikace:** [RPTA na 3GPP Explorer](https://3gpp-explorer.com/glossary/rpta/)
