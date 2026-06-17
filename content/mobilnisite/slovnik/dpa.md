---
slug: "dpa"
url: "/mobilnisite/slovnik/dpa/"
type: "slovnik"
title: "DPA – Differential Power Analysis"
date: 2025-01-01
abbr: "DPA"
fullName: "Differential Power Analysis"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/dpa/"
summary: "Metoda útoku vedlejším kanálem, která analyzuje odchylky v odběru energie zařízení za účelem získání tajných kryptografických klíčů. Představuje významné bezpečnostní riziko pro mobilní a IoT zařízení"
---

DPA je metoda vedlejšího kanálu, která analyzuje odchylky v odběru energie zařízení za účelem získání tajných kryptografických klíčů, což představuje významné bezpečnostní riziko pro mobilní a IoT zařízení.

## Popis

Differential Power Analysis (DPA) je sofistikovaná forma útoku vedlejším kanálem, který cílí na kryptografické implementace v hardwaru, jako jsou SIM karty, USIMy a bezpečnostní prvky v mobilních zařízeních. Na rozdíl od tradiční kryptoanalýzy, která útočí na matematický algoritmus, DPA využívá fyzikálních charakteristik zařízení během jeho činnosti. Útok funguje na principu statistické analýzy korelace mezi odběrem energie zařízení a mezilehlými datovými hodnotami zpracovávanými během kryptografických operací, jako je šifrování nebo generování digitálního podpisu. Shromážděním velkého počtu záznamů (traces) odběru energie během zpracování známých nebo zvolených vstupů může útočník pomocí statistických metod odvodit bity tajného klíče. Odběr energie se mírně liší v závislosti na tom, zda zařízení zpracovává '0' nebo '1', a tyto nepatrné odchylky, analyzované napříč mnoha operacemi, mohou odhalit klíč.

Architektura útoku DPA zahrnuje několik klíčových komponent: cílové zařízení, měřicí sestavu pro zachycení odběru energie (často využívající osciloskop a proudovou sondu) a analytický software. Útočník typicky ovládá vstup do kryptografické operace, například zasíláním autentizačních výzev SIM kartě. Pro každý vstup je zaznamenán vysokorozlišující záznam odběru energie zařízení. Tyto záznamy jsou následně zpracovány pomocí statistických funkcí, jako je rozdíl průměrů (Difference of Means) nebo korelační analýza, k identifikaci bodů, kde je odběr energie závislý na konkrétních mezilehlých hodnotách závislých na klíči. Útok je neinvazivní a lze jej provést bez fyzického poškození zařízení, což z něj činí účinnou hrozbu.

V kontextu 3GPP představuje DPA kritický problém pro bezpečnost autentizačních a dohodových protokolů ([AKA](/mobilnisite/slovnik/aka/)) a pro integritu aplikací na UICC (Universal Integrated Circuit Card). Specifikace jako 3GPP TS 35.205 a 35.909 definují testovací metodologie a požadavky na odolnost proti DPA a dalším útokům vedlejším kanálem. Tyto normy ukládají, že kryptografické implementace v bezpečnostních prvcích definovaných 3GPP musí obsahovat protiopatření, jako je vyvažování odběru energie, vstřikování šumu nebo algoritmické maskování, ke zmírnění rizika. Role analýzy DPA v 3GPP je tedy dvojí: představuje zdokumentovaný vektor útoku, proti kterému je nutné se bránit, a zároveň pohání vývoj bezpečnějších hardwarových a softwarových implementací k ochraně identity uživatele, důvěrnosti a přístupu k síti.

## K čemu slouží

Koncept Differential Power Analysis nevytvořila organizace 3GPP, ale byl identifikován jako kritická bezpečnostní hrozba, kterou tento normalizační orgán potřeboval řešit. Jeho účelem ve specifikacích 3GPP je definovat známou metodologii útoku, aby mohli implementátoři testovat a ověřovat odolnost svých kryptografických modulů. Před formálním uznáním útoků vedlejším kanálem, jako je DPA, se bezpečnostní hodnocení primárně zaměřovala na logické zranitelnosti a zranitelnosti na úrovni protokolů. Fyzická implementace algoritmů byla často považována za černou skříňku, o které se předpokládalo, že je bezpečná, pokud byl algoritmus správný.

Motivace pro zahrnutí DPA do norem 3GPP vyvstala z rostoucí hodnoty a citlivosti dat a služeb v mobilních sítích spolu s rozšířením zařízení v potenciálně nepřátelském prostředí. Útočníci mohli použít relativně levné vybavení k extrakci tajných klíčů ze SIM karet nebo vestavěných bezpečnostních prvků, čímž ohrozili soukromí uživatelů a bezpečnost sítě. Standardizací popisů útoků a testovacích požadavků (např. v TS 35.205 pro algoritmus MILENAGE) zajišťuje 3GPP základní úroveň fyzické bezpečnosti v celém ekosystému. Tím se řeší omezení předchozích přístupů, které přehlížely úniky na úrovni implementace, a zvyšuje se tak celková bezpečnostní laťka pro telekomunikační průmysl.

## Klíčové vlastnosti

- Statistická analýza záznamů odběru energie za účelem získání kryptografických klíčů
- Neinvazivní metoda útoku vyžadující fyzický přístup k zařízení, nikoliv však jeho dekapsulaci
- Cílí na kryptografické operace jako AES, DES a algoritmy s veřejným klíčem
- Spoléhá na korelaci mezi datově závislými odchylkami v odběru energie a bity tajného klíče
- Definována jako standardní vektor útoku v 3GPP specifikacích pro bezpečnostní hodnocení
- Pohání implementaci hardwarových a softwarových protiopatření v UICC a SE (Secure Elements)

## Související pojmy

- [AKA – Authentication and Key Agreement](/mobilnisite/slovnik/aka/)

## Definující specifikace

- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP
- **TS 35.205** (Rel-19) — MILENAGE Algorithm Set: General Overview
- **TS 35.234** (Rel-19) — MILENAGE-256 Algorithm Set Specification
- **TR 35.909** (Rel-19) — 3GPP MILENAGE Algorithm Design Report
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen
- **TR 35.937** (Rel-19) — MILENAGE-256 Algorithm Set Specification

---

📖 **Anglický originál a plná specifikace:** [DPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/dpa/)
