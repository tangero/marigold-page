---
slug: "csv"
url: "/mobilnisite/slovnik/csv/"
type: "slovnik"
title: "CSV – Comma Separated Version"
date: 2025-01-01
abbr: "CSV"
fullName: "Comma Separated Version"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/csv/"
summary: "CSV je standardizovaný datový formát definovaný 3GPP pro reprezentaci strukturovaných informací pomocí hodnot oddělených čárkou. Používá se ve specifikacích pro konfiguraci, reportování a výměnu dat,"
---

CSV je standardizovaný datový formát pro reprezentaci strukturovaných informací pomocí hodnot oddělených čárkou, používaný v 3GPP pro správu sítě, testování a analýzy, který poskytuje jednoduchý a interoperabilní formát.

## Popis

Comma Separated Version (CSV) v 3GPP označuje specifický textový datový formát, kde každý řádek představuje datový záznam a pole v rámci záznamu jsou oddělena čárkami. Je formálně specifikován v rámci více technických specifikací (TS), aby byla zajištěna konzistence ve způsobu strukturování, kódování a interpretace dat síťovými prvky, manažerskými systémy a testovacím zařízením. Formát typicky zahrnuje hlavičkový řádek definující názvy sloupců, po kterém následují datové řádky obsahující odpovídající hodnoty. Tato standardizace je klíčová pro interoperabilitu, neboť umožňuje implementacím různých dodavatelů vytvářet a spotřebovávat datové soubory, které dodržují stejná syntaktická a sémantická pravidla.

Architektonicky CSV není síťový protokol ani funkční komponenta, ale formát pro reprezentaci dat používaný v rámci různých rozhraní a procedur definovaných 3GPP. Používá se v kontextech jako je reportování výkonnostních měření, správa konfigurace, správa chyb a zpracování dat účastníků. Například ve správě sítě může funkce Network Data Analytics Function ([NWDAF](/mobilnisite/slovnik/nwdaf/)) exportovat výsledky analýz ve formátu CSV pro externí využití nebo služba Management Data Analytics Service ([MDAS](/mobilnisite/slovnik/mdas/)) může používat CSV soubory pro vstup konfiguračních parametrů. Jednoduchost formátu usnadňuje jeho generování, parsování a integraci s externími nástroji, jako jsou databáze, tabulkové procesory a software pro vizualizaci dat.

Klíčové komponenty specifikace CSV zahrnují pravidla pro použití oddělovače (typicky čárky), zpracování speciálních znaků (jako uvozovky pro zapouzdření polí obsahujících čárky nebo zalomení řádků), znakovou sadu (obvykle [UTF-8](/mobilnisite/slovnik/utf-8/)) a zacházení s chybějícími nebo nulovými hodnotami. Specifikace 3GPP mohou definovat konkrétní schémata CSV pro určité případy použití, s detaily povinných a volitelných sloupců, datových typů (např. celé číslo, řetězec, časové razítko) a výčtů hodnot. Toto zajišťuje, že data vyměňovaná mezi síťovými funkcemi nebo mezi sítí a externími systémy jsou jednoznačná a strojově čitelná.

V provozu se CSV soubory často používají pro hromadné operace, jako je nahrání seznamu politik účastníků do funkce Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)) nebo stažení záznamů podrobností o hovorech ([CDR](/mobilnisite/slovnik/cdr/)) z funkce Charging Data Function ([CDF](/mobilnisite/slovnik/cdf/)). Formát podporuje jak vstupní (např. provisioning), tak výstupní (např. reportování) datové toky. Jeho role spočívá v tom, že slouží jako lehký, na platformě nezávislý prostředník pro výměnu strukturovaných dat, což snižuje potřebu složitých binárních formátů nebo proprietárních schémat. Ačkoli se nejedná o protokol v reálném čase, CSV usnadňuje offline a dávkové zpracování dat, které je nezbytné pro provozní podpůrné systémy ([OSS](/mobilnisite/slovnik/oss/)), obchodní podpůrné systémy ([BSS](/mobilnisite/slovnik/bss/)) a analytiku následného zpracování.

## K čemu slouží

CSV bylo zavedeno, aby vyřešilo potřebu jednoduchého, standardizovaného a široce podporovaného datového formátu v rámci ekosystémů 3GPP. Před jeho formální specifikací byly pro výměnu dat často používány ad-hoc textové formáty nebo proprietární binární formáty, což vedlo k problémům s interoperabilitou, zvýšeným nákladům na integraci a chybám v interpretaci dat. Formát hodnot oddělených čárkou, který je de facto standardem v mnoha odvětvích, byl přijat, aby bylo možné využít existující nástroje a odborné znalosti, a zajistit tak, že telekomunikační data mohou být snadno spotřebována aplikacemi třetích stran bez specializovaných parserů.

Motivace pro standardizaci CSV v 3GPP, zejména od Release 17 dále, pramení z rostoucí složitosti 5G sítí a zvyšujícího se objemu dat generovaných pro správu, analýzu a účtování. Formáty jako XML a JSON, ačkoli výkonné, mohou být pro velké datové sady příliš rozvláčné a výpočetně náročné na zpracování. CSV nabízí kompaktní, člověkem čitelnou alternativu, která je efektivní pro tabulková data, což ji činí vhodnou pro log soubory, výkonnostní reporty a konfigurační šablony. Jeho zařazení do specifikací jako TS 26.258 (pro analýzu mediálního streamování) a TS 26.926 (pro monitorování kvality uživatelského prožitku) odráží jeho užitečnost při zpracování strukturovaných metrik a měření.

Historicky omezení předchozích přístupů zahrnovala nekonzistentní oddělovače polí, různé escape mechanismy a nedostatek formálních definic schémat, což komplikovalo automatizované zpracování dat. Definováním CSV v 3GPP specifikacích jsou tyto nejednoznačnosti odstraněny, což umožňuje spolehlivou výměnu dat napříč síťovými funkcemi, manažerskými systémy a externími partnery. Tato standardizace podporuje automatizaci, snižuje potřebu manuálního zásahu a zvyšuje celkovou efektivitu síťových operací a zajištění služeb.

## Klíčové vlastnosti

- Standardizovaný oddělovač polí (čárka) pro konzistentní parsování
- Podpora hlavičkových řádků pro definici názvů sloupců a sémantiky dat
- Mechanismy uvozování pro zpracování polí obsahujících čárky nebo zalomení řádků
- Znaková sada UTF-8 pro zajištění kompatibility s mezinárodními texty
- Definice specifických schémat pro jednotlivé případy použití v technických specifikacích 3GPP
- Lehký formát vhodný pro hromadný přenos dat a offline zpracování

## Související pojmy

- [NWDAF – Network Data Analytics Function](/mobilnisite/slovnik/nwdaf/)
- [MDAS – Management Data Analytics Service](/mobilnisite/slovnik/mdas/)
- [CDR – Call Detail Record](/mobilnisite/slovnik/cdr/)

## Definující specifikace

- **TS 26.258** (Rel-19) — IVAS Codec Floating-Point C Code Specification
- **TR 26.926** (Rel-19) — Traffic Models & Quality Evaluation for Media/XR in 5G
- **TR 26.955** (Rel-19) — Video Codec Analysis for 5G Services
- **TR 26.956** (Rel-19) — Beyond 2D Video Formats & Codecs Study

---

📖 **Anglický originál a plná specifikace:** [CSV na 3GPP Explorer](https://3gpp-explorer.com/glossary/csv/)
