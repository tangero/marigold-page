---
slug: "so"
url: "/mobilnisite/slovnik/so/"
type: "slovnik"
title: "SO – Security Objective"
date: 2026-01-01
abbr: "SO"
fullName: "Security Objective"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/so/"
summary: "Formální výrok definující konkrétní bezpečnostní vlastnost nebo cíl, který musí být dosažen v rámci systému nebo podsystému 3GPP. Slouží jako základní požadavek pro návrh a hodnocení bezpečnostních me"
---

SO (bezpečnostní cíl) je formální výrok definující konkrétní bezpečnostní vlastnost nebo cíl, který musí být dosažen v rámci systému 3GPP, aby sloužil jako základní požadavek pro návrh bezpečnostních mechanismů.

## Popis

Bezpečnostní cíl (SO) v 3GPP je přesný, deklarativní výrok, který vymezuje konkrétní bezpečnostní výsledek nebo stav, který musí systém udržovat. Je to klíčová součást metodiky zajištění bezpečnosti 3GPP, která tvoří most mezi vysokou úrovní bezpečnostních požadavků a podrobnými technickými bezpečnostními funkcemi a mechanismy implementovanými ve specifikacích. SO jsou odvozeny z důkladné analýzy hrozeb a posouzení rizik systémové architektury. Jsou formulovány tak, aby byly testovatelné a ověřitelné, a poskytují jasná kritéria, vůči nimž lze hodnotit bezpečnost síťového produktu nebo systému.

Proces definování a používání SO zahrnuje několik klíčových fází. Nejprve analytici bezpečnosti modelují systém, identifikují aktiva (např. uživatelská data, signalizační zprávy, síťové funkce) a potenciální hrozby proti nim. Z těchto hrozeb jsou formulovány bezpečnostní cíle, které přímo čelí zranitelnostem. Například hrozba 'odposlechu dat uživatelské roviny' vede k SO jako 'Systém musí poskytovat ochranu důvěrnosti dat uživatelské roviny mezi UE a sítí.' Tyto SO jsou pak mapovány na konkrétní bezpečnostní funkce, jako jsou šifrovací algoritmy definované v bezpečnostních specifikacích 3GPP (řada TS 33.). Skutečná implementace těchto funkcí v síťových prvcích a UE je následně testována na shodu s těmito cíli.

Jejich role je zásadní pro celý bezpečnostní životní cyklus 3GPP. SO poskytují plán pro bezpečnostní návrh a zajišťují, že každý specifikovaný bezpečnostní mechanismus má jasný účel spojený s reálnou hrozbou. Jsou nezbytné pro rámce bezpečnostní certifikace, jako jsou specifikace pro zajištění bezpečnosti ([SCAS](/mobilnisite/slovnik/scas/)) pro síťové vybavení definované 3GPP. Během hodnocení je pro produkt vytvořen dokument Bezpečnostního cíle (Security Target), který uvádí SO, jež produkt deklaruje jako podporované. Hodnotitelé pak produkt testují, aby ověřili, že těmto cílům vyhovuje, čímž poskytují operátorům záruku, že zařízení je odolné vůči definovaným útokům. Tento přístup založený na cílech vytváří standardizovanou, opakovatelnou a důslednou metodu pro validaci bezpečnosti v celém globálním dodavatelském řetězci.

## K čemu slouží

Koncept bezpečnostních cílů byl zaveden, aby vnesl strukturu, důslednost a jasnost do procesu bezpečnostního inženýrství v rámci 3GPP. Dřívější přístupy k zabezpečení v telekomunikacích často zahrnovaly ad-hoc nebo implicitní požadavky, což ztěžovalo systematické zajištění, že všechny aspekty systému jsou chráněny proti komplexnímu souboru hrozeb. Jak se mobilní sítě vyvinuly ve složité systémy založené na IP (počínaje 3G a plně realizované v 4G/LTE), útočná plocha se dramaticky rozšířila, což si vyžádalo formalizovanější bezpečnostní metodologii.

Vytvoření rámce SO řeší problém zajištění komplexní bezpečnosti v prostředí s více dodavateli, které vyžaduje interoperabilitu. Řeší výzvu převodu bezpečnostních cílů na vysoké úrovni (např. 'chránit soukromí uživatele') na konkrétní, implementovatelné a testovatelné technické požadavky. Definováním SO poskytuje 3GPP společný jazyk a soubor kritérií pro dodavatele zařízení, síťové operátory a testovací laboratoře. To umožňuje nezávislá bezpečnostní hodnocení, kde se různé strany mohou shodnout na tom, co 'bezpečné' znamená pro konkrétní síťovou funkci. Posouvá bezpečnost z pozice kvalitativní dodatečné úvahy na kvantifikovatelnou a auditovatelnou vlastnost systému, což je klíčové pro udržení důvěry v mobilní komunikace, jak se stávají nedílnou součástí národní infrastruktury, finančních systémů a osobního života.

## Klíčové vlastnosti

- Formální, deklarativní výroky požadovaných bezpečnostních vlastností
- Odvozeny ze systematické analýzy hrozeb a rizik (TRA)
- Poskytují sledovatelnost od hrozeb k bezpečnostním funkcím
- Slouží jako základ pro bezpečnostní testování a hodnotící kritéria
- Nezbytné pro soulad se specifikacemi pro zajištění bezpečnosti (SCAS)
- Umožňují standardizovaný proces bezpečnostní certifikace síťového vybavení

## Definující specifikace

- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 32.851** (Rel-12) — Network Sharing OAM Requirements
- **TR 33.857** (Rel-17) — Enhanced Security for Non-Public Networks
- **TR 33.916** (Rel-19) — 3GPP Security Assurance Methodology (SECAM)
- **TS 36.322** (Rel-19) — E-UTRA Radio Link Control Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [SO na 3GPP Explorer](https://3gpp-explorer.com/glossary/so/)
