---
slug: "slpkmf"
url: "/mobilnisite/slovnik/slpkmf/"
type: "slovnik"
title: "SLPKMF – SideLink Positioning Key Management Function"
date: 2025-01-01
abbr: "SLPKMF"
fullName: "SideLink Positioning Key Management Function"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/slpkmf/"
summary: "Síťová funkce zavedená v 5G pro služby bezprostřední blízkosti (ProSe) a komunikaci vozidlo-se-vším (V2X). Je zodpovědná za generování, správu a distribuci kryptografických klíčů používaných k zabezpe"
---

SLPKMF je síťová funkce v 5G ProSe a V2X, která generuje, spravuje a distribuuje kryptografické klíče pro zabezpečení integrity a důvěrnosti polohovacích komunikací přes rozhraní Sidelink.

## Popis

Funkce správy klíčů pro polohování přes Sidelink (SLPKMF) je bezpečnostní funkce definovaná ve 3GPP Release 18 jako součást vylepšené architektury pro polohování přes Sidelink a služby bezprostřední blízkosti ([ProSe](/mobilnisite/slovnik/prose/)). Funguje v rámci bezpečnostního rámce pro přímou komunikaci mezi zařízeními ([D2D](/mobilnisite/slovnik/d2d/)), známou jako Sidelink ([SL](/mobilnisite/slovnik/sl/)), která je klíčová pro [V2X](/mobilnisite/slovnik/v2x/), veřejnou bezpečnost a komerční ProSe aplikace. Hlavní úlohou SLPKMF je spravovat životní cyklus kryptografických klíčů speciálně používaných pro zabezpečení polohovacích procedur prováděných přes Sidelink. To zahrnuje generování, ukládání, distribuci a odvolávání klíčů, jako je Sidelink Positioning Key (SLPK). Když uživatelská zařízení (UE) potřebují provádět zabezpečené relativní polohování (např. pro prevenci kolizí ve V2X), vyžadují ověřené a z hlediska integrity chráněné zprávy polohovacích měření. SLPKMF, typicky umístěná v domovské síti, poskytuje potřebné klíče autorizovaným UE prostřednictvím zabezpečené signalizace s dalšími síťovými funkcemi, jako je Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) a ProSe Function. UE tyto klíče používá k odvození sezení klíčů pro ochranu zpráv protokolu Sidelink Positioning Protocol ([SLPP](/mobilnisite/slovnik/slpp/)) nebo souvisejících polohovacích referenčních signálů. Funkce zajišťuje, že se v zabezpečených polohovacích výměnách mohou účastnit pouze autorizovaná zařízení, čímž brání falšování, opakovaným útokům a odposlechu citlivých polohových dat. Její provoz je úzce spojen s celkovou bezpečnostní architekturou ProSe, interaguje s ProSe Key Management Function (KMF) a využívá bezpečnostní mechanismy jádra 5G sítě.

## K čemu slouží

SLPKMF byla vytvořena k řešení specifických bezpečnostních požadavků pro polohování přes Sidelink, což je schopnost, která se stala kritickou s rozvojem [V2X](/mobilnisite/slovnik/v2x/) a pokročilých [ProSe](/mobilnisite/slovnik/prose/) služeb v 5G NR. Dřívější verze ProSe a V2X se zaměřovaly na základní zabezpečení komunikace, ale postrádaly standardizovaný, vyhrazený mechanismus pro zabezpečení polohově související signalizace a měření vyměňovaných přímo mezi zařízeními. Jak se objevily aplikace jako autonomní řízení a vysoce přesné relativní polohování, potřeba zabezpečených a důvěryhodných polohových informací se stala prvořadou, aby se předešlo bezpečnostně kritickým hrozbám, jako je falšování polohy v systémech prevence kolizí. SLPKMF to řeší poskytnutím standardizovaného, sítí asistovaného rámce správy klíčů šitého na míru pro polohování přes Sidelink. Odstraňuje omezení ad-hoc nebo aplikačně-vrstvového zabezpečení integrací do důvěryhodného modelu sítě 3GPP, což umožňuje centralizovanou správu politik, správu životního cyklu klíčů a podporu roamingových scénářů. Její zavedení v Release 18 bylo motivováno potřebou umožnit zabezpečené, vysoce přesné polohovací služby pro V2X, průmyslový IoT a veřejnou bezpečnost, kde je integrita polohových dat stejně důležitá jako samotná komunikace.

## Klíčové vlastnosti

- Generuje a spravuje kryptografické klíče určené pro zabezpečení polohování přes Sidelink (např. SLPK)
- Distribuuje polohovací klíče autorizovaným UE prostřednictvím zabezpečených síťových procedur
- Integruje se s bezpečnostní architekturou jádra 5G sítě a ProSe funkcemi
- Podporuje odvozování klíčů pro zabezpečení zpráv protokolu Sidelink Positioning Protocol (SLPP)
- Umožňuje ochranu integrity a důvěrnosti pro přímá polohovací měření mezi zařízeními
- Nezbytná pro zabezpečené V2X aplikace, jako je relativní polohování a prevence kolizí

## Související pojmy

- [ProSe – Proximity-based Services](/mobilnisite/slovnik/prose/)

## Definující specifikace

- **TS 24.514** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.586** (Rel-19) — SLPKMF Service Based Interface Protocol
- **TS 33.533** (Rel-19) — Security for 5G Ranging & Sidelink Positioning

---

📖 **Anglický originál a plná specifikace:** [SLPKMF na 3GPP Explorer](https://3gpp-explorer.com/glossary/slpkmf/)
