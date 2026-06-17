---
slug: "lla"
url: "/mobilnisite/slovnik/lla/"
type: "slovnik"
title: "LLA – Logical Layered Architecture"
date: 2025-01-01
abbr: "LLA"
fullName: "Logical Layered Architecture"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/lla/"
summary: "Konceptuální rámec definovaný 3GPP pro strukturování systémů řízení telekomunikací. Organizuje řídicí funkce do samostatných logických vrstev – Business, Service a Network – aby oddělil jednotlivé obl"
---

LLA je konceptuální rámec 3GPP, který strukturovaně organizuje systémy řízení rozdělením funkcí do samostatných vrstev Business, Service a Network, aby oddělil jednotlivé oblasti odpovědnosti a umožnil automatizované, komplexní řízení.

## Popis

Logical Layered Architecture (LLA) je základní rámec pro řízení standardizovaný 3GPP, především v rámci specifikací série Telecom Management (TM) (např. 32.101). Poskytuje vysokou logickou předlohu pro organizaci Operations Support Systems ([OSS](/mobilnisite/slovnik/oss/)) a řídicích funkcí nezávisle na jejich fyzické implementaci. Architektura je rozdělena do tří hlavních vrstev, z nichž každá má odlišné zaměření a odpovědnost: Business Management Layer (BML), Service Management Layer (SML) a Network Management Layer ([NML](/mobilnisite/slovnik/nml/)). Existuje také podkladová Element Management Layer ([EML](/mobilnisite/slovnik/eml/)) a Network Element Layer (NEL), přičemž klíčové logické oddělení je mezi prvními třemi vrstvami.

Business Management Layer (BML) je nejvyšší vrstva, která se zabývá celkovými obchodními cíli, strategiemi a politikami poskytovatele služeb. Zpracovává úkoly jako obchodní plánování, správa smluv a finanční reporting. Převádí obchodní cíle na politiky a požadavky pro nižší vrstvu. Service Management Layer (SML) funguje jako prostředník a zaměřuje se na služby orientované na zákazníka (např. VoIP, [IPTV](/mobilnisite/slovnik/iptv/), síťové řezy). Její funkce zahrnují objednávání služeb, zřizování, zajišťování kvality, řešení problémů a zprostředkování fakturace. Přijímá obchodní pokyny z BML a převádí je na technické příkazy a politiky pro síťovou vrstvu.

Network Management Layer (NML) je odpovědná za logické a fyzické síťové zdroje, které služby poskytují. Řídí síť z pohledu komplexního provozu a vykonává funkce jako správa síťového inventáře, konfigurace, poruch, výkonu a zabezpečení (FCAPS). Přijímá požadavky specifické pro služby ze SML (např. 'zřiď VPN s 100 Mbps mezi body A a B') a provádí potřebné konfigurace na příslušných síťových prvcích prostřednictvím Element Management Layer (EML). EML poskytuje výrobci specifické řízení jednotlivých síťových prvků nebo jejich skupin, zatímco NEL představuje skutečné řízené síťové zdroje (např. gNB, [MME](/mobilnisite/slovnik/mme/), router). Informace proudí těmito vrstvami směrem nahoru (pro stav, alarmy, data o výkonu) i dolů (pro příkazy, politiky), což umožňuje automatizaci se zpětnou vazbou.

## K čemu slouží

LLA byl vyvinut pro řešení složitosti a výzev interoperability při řízení rozsáhlých telekomunikačních sítí s více dodavateli. Před jeho formalizací byly řídicí systémy často monolitické, vertikálně integrované a těsně provázané s konkrétními síťovými technologiemi nebo dodavateli. To ztěžovalo zavádění nových služeb, integraci systémů od různých dodavatelů a dosažení komplexní automatizace. LLA poskytuje standardizované, logické oddělení jednotlivých oblastí odpovědnosti pro překonání těchto omezení.

Jeho hlavním účelem je umožnit efektivní, škálovatelné a automatizované řízení definováním jasných hranic a odpovědností mezi obchodními, služebními a síťovými doménami. Oddělením 'co' (obchodní/služební záměr) od 'jak' (síťová implementace) umožňuje každé vrstvě se vyvíjet nezávisle. Například nová služba může být navržena na SML bez nutnosti změn v podkladové [NML](/mobilnisite/slovnik/nml/), pokud síť dokáže podporovat požadované schopnosti. Tato architektura je konceptuálním základem pro moderní systémy [OSS](/mobilnisite/slovnik/oss/)/[BSS](/mobilnisite/slovnik/bss/) a je zásadní pro realizaci řídicích paradigmat jako DevOps, intent-based networking a automatizace se zpětnou vazbou v 5G a dalších generacích. Přímo podporuje řízení komplexních konceptů, jako je síťové dělení (network slicing), kde musí být požadavek obchodního zákazníka na síťový řez (BML/SML) převeden na orchestraci a zajištění vyhrazené sady síťových zdrojů (NML/EML).

## Klíčové vlastnosti

- Jasné oddělení jednotlivých oblastí řízení do vrstev Business, Service a Network
- Poskytuje rámec pro interoperabilitu mezi různými komponentami OSS a dodavateli
- Umožňuje převod obchodních cílů na technické síťové konfigurace
- Podporuje komplexní řízení životního cyklu služeb (objednávání, zřizování, zajištění kvality)
- Tvoří konceptuální základ pro řízení FCAPS (Fault, Configuration, Accounting, Performance, Security)
- Umožňuje automatizaci a operace se zpětnou vazbou napříč různými řídicími doménami

## Definující specifikace

- **TS 32.101** (Rel-19) — Management principles and high-level requirements
- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.819** (Rel-8) — Element Management Layer OS Functions
- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)

---

📖 **Anglický originál a plná specifikace:** [LLA na 3GPP Explorer](https://3gpp-explorer.com/glossary/lla/)
