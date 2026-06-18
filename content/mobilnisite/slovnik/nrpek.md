---
slug: "nrpek"
url: "/mobilnisite/slovnik/nrpek/"
type: "slovnik"
title: "NRPEK – NR PC5 Encryption Key"
date: 2025-01-01
abbr: "NRPEK"
fullName: "NR PC5 Encryption Key"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/nrpek/"
summary: "Kryptografický klíč používaný k šifrování uživatelských dat a signalizačních zpráv na rozhraní NR PC5 (sidelink) v 5G V2X a ProSe. Zajišťuje důvěrnost pro přímou komunikaci mezi zařízeními a chrání př"
---

NRPEK je kryptografický klíč používaný k šifrování uživatelských dat a signalizačních zpráv na rozhraní NR PC5 (sidelink) za účelem zajištění důvěrnosti v 5G V2X a přímé komunikaci zařízení zařízení (ProSe).

## Popis

Klíč pro šifrování na NR PC5 (NRPEK) je základním bezpečnostním prvkem v rámci bezpečnostní architektury 5G sidelink (PC5), specificky definovaným pro služby založené na New Radio (NR) – Proximity Services ([ProSe](/mobilnisite/slovnik/prose/)) a Vehicle-to-Everything ([V2X](/mobilnisite/slovnik/v2x/)). Jedná se o symetrický klíč odvozený jako součást hierarchie klíčů během procedur autentizace a dohody o klíči pro komunikaci přes PC5. NRPEK je generován uživatelským zařízením (UE) nebo poskytnut sítí, v závislosti na bezpečnostním režimu a autorizaci služby. Jeho primární funkcí je poskytovat ochranu důvěrnosti pro data uživatelské roviny a určité signalizační zprávy řídicí roviny přenášené přímo mezi uživatelskými zařízeními (UE) přes referenční bod PC5, bez průchodu síťovou infrastrukturou.

Proces odvozování klíče NRPEK je specifikován v 3GPP TS 33.503. Typicky je odvozen z kořenového klíče vytvořeného během autentizace a autorizace pro PC5. Tento proces může zahrnovat uživatelské zařízení (UE), funkci ProSe v jádře sítě a ve scénářích V2X také funkci V2X Control Function. K odvození se používají funkce pro odvozování klíčů ([KDF](/mobilnisite/slovnik/kdf/)) se specifickými vstupními parametry, včetně parametrů čerstvosti pro zajištění separace klíčů. Po odvození a instalaci do bezpečnostního prostředí uživatelského zařízení (UE) je NRPEK používán kryptografickými algoritmy ve vrstvě [PDCP](/mobilnisite/slovnik/pdcp/) (Packet Data Convergence Protocol) pro NR sidelink k provádění operací šifrování a dešifrování dat přenášených přes rozhraní vzduch.

Role NRPEK je klíčová pro umožnění bezpečné přímé komunikace. Působí společně s klíčem pro integritu na NR PC5 ([NRPIK](/mobilnisite/slovnik/nrpik/)), který poskytuje ochranu integrity. Oddělení šifrovacího a integritního klíče je standardní bezpečnostní praxí, která omezuje dopad případného kompromitování klíče a umožňuje nezávislou správu těchto dvou bezpečnostních služeb. NRPEK se uplatňuje na každé bezpečnostní asociaci PC5, což znamená, že každá bezpečná komunikační relace nebo skupina může mít svůj vlastní unikátní šifrovací klíč, což poskytuje dopřednou důvěrnost a omezení dopadu v případě prolomení jednoho klíče. Jeho správa, včetně aktivace, deaktivace a obnovy, je řízena bezpečnostními mechanismy přístupové vrstvy ([AS](/mobilnisite/slovnik/as/)) uživatelského zařízení (UE) na základě podnětů z vyšších vrstev nebo ze sítě.

## K čemu slouží

NRPEK byl zaveden, aby řešil specifické požadavky na důvěrnost v komunikaci přes 5G NR sidelink, která je klíčová pro pokročilé aplikace [V2X](/mobilnisite/slovnik/v2x/) a [ProSe](/mobilnisite/slovnik/prose/). Předchozí zabezpečení PC5 založené na LTE (definované pro LTE V2X) vytvořilo základ, ale potřebovalo vylepšení pro nové případy užití, vyšší přenosové rychlosti a cíle nižší latence 5G NR. Vytvoření vyhrazeného klíče pro šifrování na NR PC5 bylo motivováno potřebou robustního, standardizovaného kryptografického řešení, které by mohlo chránit citlivá data vyměňovaná přímo mezi vozidly, mezi chodci a infrastrukturou nebo ve scénářích veřejné bezpečnosti, kde může být síťové pokrytí omezené nebo narušené.

Bez NRPEK by přímá komunikace mezi zařízeními přes 5G NR rozhraní vzduch byla zranitelná vůči odposlechu, což by ohrožovalo soukromí a bezpečnost uživatelů. Například v autonomním řízení musí být data o poloze, sdílení senzorů a zprávy pro koordinaci manévrů důvěrné, aby se zabránilo sledování nebo škodlivému rušení. NRPEK jako součást komplexního bezpečnostního rámce NR PC5 tento problém řeší tím, že poskytuje standardizovaný, na algoritmech agilní šifrovací mechanismus integrovaný do architektury 5G systému. Odstraňuje omezení zabezpečení sidelink před 5G tím, že je nativně navržen pro flexibilní číselnou řadu, přidělování zdrojů a požadavky na služby v NR, a zajišťuje, aby se bezpečnost nestala úzkým hrdlem pro výkon nebo inovace v přímých komunikačních službách.

## Klíčové vlastnosti

- Poskytuje ochranu důvěrnosti pro data uživatelské roviny na rozhraní NR PC5.
- Je odvozen z kořenového klíče vytvořeného během specifických procedur autentizace a autorizace pro PC5.
- Je používán kryptografickými algoritmy vrstvy NR PDCP pro šifrování/dešifrování.
- Působí ve spojení se samostatným klíčem NRPIK pro integritu, v souladu s principem separace klíčů.
- Spravován na každou bezpečnostní asociaci PC5, což umožňuje klíčování specifické pro relaci a dopřednou důvěrnost.
- Podporuje agilitu algoritmů, umožňující použití různých šifrovacích algoritmů definovaných 3GPP.

## Definující specifikace

- **TS 24.587** (Rel-19) — V2X Services Protocols for 5G System
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G
- **TS 33.536** (Rel-19) — 5G V2X Security for NR PC5

---

📖 **Anglický originál a plná specifikace:** [NRPEK na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrpek/)
