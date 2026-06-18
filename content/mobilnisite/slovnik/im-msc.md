---
slug: "im-msc"
url: "/mobilnisite/slovnik/im-msc/"
type: "slovnik"
title: "IM-MSC – Intermediate Mobile Switching Centre"
date: 2025-01-01
abbr: "IM-MSC"
fullName: "Intermediate Mobile Switching Centre"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/im-msc/"
summary: "Mezilehlá MSC (IM-MSC) je ústředna mobilního přepojování, která během nastavování volání ukončeného do mobilní sítě přeposílá signalizaci řízení hovoru a uživatelský provoz mezi Gateway MSC (GMSC) a n"
---

IM-MSC (Intermediate Mobile Switching Centre) je mezilehlá ústředna mobilního přepojování, která během nastavování volání ukončeného do mobilní sítě přeposílá signalizaci řízení hovoru a uživatelský provoz mezi Gateway MSC a navštívenou MSC, pokud není možné přímé směrování.

## Popis

Mezilehlá ústředna mobilního přepojování (IM-MSC) je funkční entita v obvodu přepínané ([CS](/mobilnisite/slovnik/cs/)) části jádra sítě systémů GSM a UMTS. Působí během fáze nastavování volání ukončeného do mobilní sítě (volání k mobilnímu účastníkovi). Hlavní scénář zahrnuje Gateway [MSC](/mobilnisite/slovnik/msc/) ([GMSC](/mobilnisite/slovnik/gmsc/)), která přijme volání z externí sítě, dotazuje Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) pro získání směrovacích informací (Mobile Station Roaming Number, [MSRN](/mobilnisite/slovnik/msrn/)). Pokud MSRN odkazuje na síť, kde GMSC nemůže vytvořit přímé trunky nebo signalizační spojení s navštívenou MSC ([VMSC](/mobilnisite/slovnik/vmsc/)) obsluhující cílového účastníka, použije se jako prostředník IM-MSC.

Z architektonického hlediska je IM-MSC standardní MSC, která vykonává jak funkce řízení hovoru, tak přepojování. Přijímá zprávu Initial Address Message ([IAM](/mobilnisite/slovnik/iam/)) od GMSC prostřednictvím signalizace [ISUP](/mobilnisite/slovnik/isup/), která obsahuje MSRN. IM-MSC poté tento MSRN analyzuje a, vystupujíc jako výchozí přepínač, přepošle novou IAM směrem k cílové VMSC. Vytváří trunkové spojení na obou stranách a stává se tak tranzitním přepínačem v cestě hovoru. IM-MSC zůstává ve signalizační a přenosové cestě po celou dobu trvání hovoru a zpracovává následné zprávy řízení hovoru jako Answer (ANM), Release (REL) a Release Complete (RLC).

Její role je definována v 3GPP TS 23.119, 'Optimal Routing of Circuit-Switched calls.' Specifikace popisuje postupy pro scénáře optimálního a neoptimálního směrování. IM-MSC je klíčová v případech neoptimálního směrování, například když GMSC a VMSC patří různým síťovým operátorům bez přímé dohody o propojení, nebo uvnitř sítě jediného operátora používajícího složité hierarchické směrovací plány. IM-MSC zajišťuje zpětnou kompatibilitu a vzájemné propojení různých síťových uzlů a starších směrovacích schémat, udržujíc úspěšnost dokončení hovorů tam, kde přímé směrování není možné.

## K čemu slouží

IM-MSC byla zavedena, aby řešila praktické problémy se směrováním v rozsáhlých, víceoperačních nebo geograficky rozptýlených sítích GSM/UMTS. V počátcích mobilní telefonie neměly všechny MSC přímá trunková propojení kvůli nákladům, fyzickým omezením nebo komerčním dohodám. GMSC mohla potřebovat směrovat volání přes jednu nebo více mezilehlých sítí, aby dosáhla obsluhující MSC účastníka.

Bez definovaného konceptu IM-MSC by nastavování hovoru selhalo, pokud by GMSC nedokázala interpretovat směrovací číslo (MSRN) nebo neměla cestu do sítě označené tímto číslem. IM-MSC standardizuje chování tranzitního přepínače v cestě mobilního hovoru a zajišťuje, že signalizace (ISUP) a uživatelský provoz mohou být předvídatelně přeposílány. Řeší tak omezení vyžadující plně propojenou síť mezi všemi MSC a GMSC, což je ekonomicky i technicky nepraktické.

Historicky, jak se sítě vyvíjely a roamingové dohody rozšiřovaly, potřeba standardizované zprostředkovatelské funkce se stala zřejmou. IM-MSC umožňuje flexibilní plánování sítě, hierarchické směrování a propojování sítí od různých dodavatelů nebo operátorů, čímž zajišťuje spolehlivé doručování volání pro služby ukončené do mobilní sítě napříč složitou globální infrastrukturou.

## Klíčové vlastnosti

- Působí jako tranzitní přepínač pro ISUP signalizaci mezi GMSC a VMSC
- Vytváří a spravuje mezilehlá trunková spojení pro uživatelský provoz
- Umožňuje směrování hovorů, když nejsou dostupné přímé cesty z GMSC na VMSC
- Podporuje standardní postupy řízení hovoru (odpověď, uvolnění atd.)
- Umožňuje propojení sítí různých operátorů a dodavatelů
- Umožňuje hierarchické a neoptimální scénáře směrování definované v TS 23.119

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [VMSC – Visited Mobile Switching Center](/mobilnisite/slovnik/vmsc/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [ISUP – MIME ISDN User Part Multi-purpose Internet Mail Extension](/mobilnisite/slovnik/isup/)
- [MSRN – Mobile Subscriber Roaming Number](/mobilnisite/slovnik/msrn/)

## Definující specifikace

- **TS 23.119** (Rel-19) — Gateway Location Register (GLR) Stage 2 Description
- **TR 23.909** (Rel-5) — Gateway Location Register (GLR) Architecture

---

📖 **Anglický originál a plná specifikace:** [IM-MSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/im-msc/)
