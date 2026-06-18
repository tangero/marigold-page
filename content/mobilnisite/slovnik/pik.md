---
slug: "pik"
url: "/mobilnisite/slovnik/pik/"
type: "slovnik"
title: "PIK – ProSe Integrity Key"
date: 2025-01-01
abbr: "PIK"
fullName: "ProSe Integrity Key"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/pik/"
summary: "Klíč integrity ProSe (PIK) je kryptografický klíč používaný k zajištění integrity a autenticity zpráv vyměňovaných v přímé komunikaci služeb ProSe (Proximity Services). Chrání proti neoprávněným změná"
---

PIK je kryptografický klíč používaný k zajištění integrity a autenticity zpráv v přímé komunikaci zařízení zařízení typu ProSe, který chrání proti neoprávněným změnám a falšování.

## Popis

Klíč integrity [ProSe](/mobilnisite/slovnik/prose/) (PIK) je bezpečnostní přihlašovací údaj definovaný v architektuře 3GPP pro služby ProSe (Proximity Services). Jedná se o symetrický klíč odvozený jako součást hierarchie bezpečnostních klíčů ProSe. PIK je konkrétně generován pro použití mezi dvěma uživatelskými zařízeními (UE) s podporou ProSe, která vstupují do přímé komunikace jeden k jednomu, nebo v rámci skupiny ProSe typu jeden k mnoha. Jeho primární funkcí je poskytovat ochranu integrity a ověřování původu dat pro datové přenosy uživatelské roviny přenášené přes referenční bod PC5, což je přímé rozhraní mezi zařízeními.

Generování PIK je vázáno na proceduru navázání klíče ProSe. Typicky je odvozen z klíče vyšší úrovně, jako je klíč ProSe (PK), který je sám navázán prostřednictvím síťově asistovaných procedur nebo přímé derivace z přihlašovacích údajů uložených na UE. Přesný derivační algoritmus je specifikován v bezpečnostních specifikacích 3GPP. Po odvození a sdílení mezi komunikujícími stranami se PIK používá k výpočtu kódu autentizace zprávy ([MAC](/mobilnisite/slovnik/mac/)) pro datové pakety. Přijímající UE přepočítá MAC pomocí své kopie PIK a porovná jej s přijatým MAC, čímž ověří integritu paketu a jeho původ od legitimního protějšku.

Architektonicky PIK funguje na úrovni přístupové vrstvy pro rozhraní PC5. Je spravován funkcí ProSe v síti během počátečního zřizování klíčů, ale následně je lokálně používán UE bez průběžného zapojení sítě, což umožňuje zabezpečenou komunikaci i mimo síťové pokrytí, což je zásadní pro případy použití veřejné bezpečnosti. Klíč je asociován s konkrétní relací nebo skupinou ProSe a má omezenou životnost, po jejímž uplynutí musí být obnoven prostřednictvím procedury změny klíče, aby byla zachována bezpečnost.

Role PIK je zásadní pro model důvěry služeb ProSe. Zajištěním, že přijatá data nebyla během přenosu změněna a pocházejí z autorizovaného zařízení ve skupině ProSe, umožňuje spolehlivou přímou komunikaci pro kritické služby. Tato ochrana integrity je předpokladem pro mnohé aplikace ProSe, zejména ty, které zahrnují citlivé informace nebo funkce velení a řízení ve veřejné bezpečnosti a kritických komunikacích.

## K čemu slouží

PIK byl zaveden, aby řešil specifické bezpečnostní požadavky přímé komunikace zařízení zařízení ([D2D](/mobilnisite/slovnik/d2d/)) standardizované jako [ProSe](/mobilnisite/slovnik/prose/) ve verzi 3GPP Release 13. Tradiční bezpečnost v mobilních sítích spoléhá na trvalou síťovou infrastrukturu (např. základnové stanice, jádro sítě) pro správu klíčů a poskytování bezpečnostních služeb. ProSe však umožňuje UE komunikovat přímo přes rozhraní PC5, potenciálně bez síťového pokrytí. Tento posun paradigmatu vytvořil potřebu bezpečnostního mechanismu, který by mohl fungovat nezávisle na síti a zároveň zachovávat robustní ochranu.

Předchozí přístupy pro ad-hoc komunikaci postrádaly standardizovanou, na úrovni mobilních sítí bezpečnost integrovanou s přihlašovacími údaji operátora. Účelem PIK je poskytnout standardizovanou, kryptograficky silnou metodu pro zajištění integrity zpráv v těchto přímých spojích. Řeší problémy neoprávněných změn zpráv a útoků vydávání se za jiného ve scénářích D2D. Bez PIK by komunikace ProSe byly zranitelné vůči škodlivým aktérům vkládajícím falešná data nebo vydávajícím se za legitimní uživatele, což je nepřijatelné pro aplikace veřejné bezpečnosti, jako je přímá komunikace mezi záchranáři během výpadků sítě.

Jeho vytvoření bylo motivováno snahou umožnit komerční a kritické služby založené na blízkosti na platformách LTE a později 5G NR. PIK jako součást širšího bezpečnostního rámce ProSe umožňuje operátorům nabízet zabezpečené služby D2D s důvěrou, s vědomím, že integrita komunikace je chráněna klíči zakořeněnými v bezpečnostní infrastruktuře operátora, a to i když zařízení fungují v samostatném přímém režimu.

## Klíčové vlastnosti

- Poskytuje ochranu integrity a ověřování původu dat pro datové přenosy uživatelské roviny na PC5.
- Je odvozen z hierarchie klíčů ProSe, což zajišťuje kryptograficky zabezpečený vazbu na přihlašovací údaje operátora.
- Umožňuje zabezpečenou přímou komunikaci mezi UE nezávisle na síťovém pokrytí.
- Je využíván v režimech komunikace ProSe typu jeden k jednomu i jeden k mnoha.
- Má definovanou životnost a podléhá obnově prostřednictvím procedur změny klíče.
- Je specifikován v rámci bezpečnostní architektury 3GPP (TS 33.303) pro standardizaci a interoperabilitu.

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS

---

📖 **Anglický originál a plná specifikace:** [PIK na 3GPP Explorer](https://3gpp-explorer.com/glossary/pik/)
