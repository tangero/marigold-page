---
slug: "mgv-s"
url: "/mobilnisite/slovnik/mgv-s/"
type: "slovnik"
title: "MGV-S – MBMS key Generation and Validation Storage"
date: 2025-01-01
abbr: "MGV-S"
fullName: "MBMS key Generation and Validation Storage"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mgv-s/"
summary: "Funkce zabezpečeného úložiště, která spolupracuje s MGV-F za účelem ochrany dlouhodobých kryptografických klíčů MBMS, jako je MBMS uživatelský klíč (MUK) a MBMS servisní klíč (MSK). Zajišťuje trvalé a"
---

MGV-S je funkce zabezpečeného úložiště, která chrání dlouhodobé kryptografické klíče MBMS a zajišťuje jejich trvalé a chráněné uchování pro autentizaci účastníků a odvozování servisních klíčů.

## Popis

[MBMS](/mobilnisite/slovnik/mbms/) key Generation and Validation Storage (MGV-S) je logická bezpečnostní úložná entita definovaná ve specifikacích 3GPP, která funguje v tandemu s [MGV-F](/mobilnisite/slovnik/mgv-f/) (Generation and Validation Function). Zatímco MGV-F je zodpovědná za aktivní generování a zpracování klíčů, MGV-S poskytuje zabezpečené úložiště pro dlouhodobý, citlivý klíčový materiál. Typicky je umístěna společně nebo úzce integrována do MBMS Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)), ačkoli je logicky oddělená. Primárním obsahem MGV-S jsou MBMS uživatelské klíče ([MUK](/mobilnisite/slovnik/muk/)) a MBMS servisní klíče ([MSK](/mobilnisite/slovnik/msk/)). MUK je unikátní klíč sdílený mezi sítí a modulom USIM (User Services Identity Module) jednotlivého účastníka pro konkrétní službu MBMS. MSK je klíč asociovaný se službou MBMS a používá se k ochraně klíčů MBMS Traffic Keys ([MTK](/mobilnisite/slovnik/mtk/)) specifických pro danou relaci během vysílání.

Z architektonického hlediska MGV-S komunikuje s MGV-F. Když MGV-F vygeneruje nový MUK pro přihlášeného uživatele, bezpečně tento klíč uloží do MGV-S. Podobně, když je pro službu vygenerován nebo aktualizován MSK, je uložen v MGV-S. MGV-F načítá klíče z MGV-S v případě potřeby, například pro změnu klíče služby nebo ověření stavu předplatného uživatele. Bezpečnost MGV-S je prvořadá, protože kompromitace uložených klíčů by narušila důvěrnost služeb MBMS. Její implementace proto zahrnuje silné přístupové kontroly, odolný hardware (jako jsou Hardware Security Modules - HSM) a robustní auditování. Návrh zajišťuje, že klíčový materiál není nikdy vystaven v čitelné podobě mimo toto chráněné prostředí.

Jeho fungování je nedílnou součástí toku předplatného a aktivace služby MBMS. Během přihlášení ke službě MGV-F vygeneruje MUK a uloží jej do MGV-S. Tento MUK je následně bezpečně zaveden do USIM uživatele, často prostřednictvím protokolů Over-The-Air ([OTA](/mobilnisite/slovnik/ota/)) využívajících stávající zabezpečení mobilní sítě. MUK v USIM a MUK v MGV-S tvoří sdílené tajemství. Později, když se uživatel pokusí přistoupit k vysílání MBMS, může síť ověřit jeho práva na základě přítomnosti odpovídajícího MUK v MGV-S. Pro probíhající relace MGV-F načte příslušný MSK z MGV-S, aby zašifroval aktuální MTK pro vysílání. Oddělením aktivní zpracovatelské funkce (MGV-F) od funkce zabezpečeného úložiště (MGV-S) architektura sleduje osvědčený bezpečnostní princip rozdělení odpovědností, čímž omezuje prostor pro útoky a usnadňuje bezpečnější a lépe spravovatelný životní cyklus klíčů.

## K čemu slouží

MGV-S byl vytvořen, aby splnil kritický požadavek v bezpečnostní architektuře [MBMS](/mobilnisite/slovnik/mbms/): potřebu vysoce zabezpečeného, trvalého a spolehlivého úložiště pro dlouhodobý kryptografický klíčový materiál. MGV-F se stará o dynamické generování klíčů pro relace, ale základní klíče identifikující účastníky (MUK) a služby (MSK) musí být uchovány po dobu trvání předplatného nebo nabídky služby, což mohou být roky. Ukládání těchto citlivých klíčů v paměti nebo databázích všeobecného určení aktivní funkce MGV-F by představovalo významné bezpečnostní riziko.

Účelem MGV-S je poskytnout pro tyto klíče vyhrazené, opevněné úložiště, které řeší omezení nedostatečných postupů ukládání klíčů. Zajišťuje důvěrnost a integritu hlavních klíčů, na kterých závisí celý řetězec zabezpečení vysílání. Logickým oddělením úložiště od zpracování návrh také zvyšuje provozní bezpečnost a soulad s požadavky. Umožňuje implementovat MGV-S na specializovaném, certifikovaném zabezpečeném hardwaru (HSM), což poskytuje fyzickou a logickou ochranu proti extrakci klíčů. Toto oddělení bylo motivováno potřebou splnit přísné požadavky na ochranu obsahu, které vyžadují mediální a vysílací společnosti pro prémiové služby mobilní televize. MGV-S tedy existuje, aby poskytl důvěryhodný kotvící bod pro správu digitálních práv MBMS, a zajistil tak, že obchodní model podmíněného přístupu k vysílacím službám je technicky robustní a odolný proti útokům.

## Klíčové vlastnosti

- Zabezpečené trvalé úložiště pro dlouhodobé klíče MBMS: MUK (uživatelský klíč) a MSK (servisní klíč)
- Logicky oddělené od aktivní zpracovatelské funkce MGV-F, ale s ní komunikující
- Navrženo pro vysokou bezpečnost, často implementováno pomocí Hardware Security Modules (HSM)
- Poskytuje důvěryhodné úložiště pro informace o vazbě účastník-sluzba
- Nezbytné pro ověření autorizace uživatele při přístupu ke službě MBMS
- Umožňuje zabezpečenou správu životního cyklu klíčů, včetně archivace a bezpečného mazání

## Související pojmy

- [MGV-F – MBMS key Generation and Validation Function](/mobilnisite/slovnik/mgv-f/)
- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 33.246** (Rel-19) — MBMS Security Specification

---

📖 **Anglický originál a plná specifikace:** [MGV-S na 3GPP Explorer](https://3gpp-explorer.com/glossary/mgv-s/)
